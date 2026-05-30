# Stratum V2: Architecture and Implementation

A protocol-engineer-level walkthrough of Stratum V2 (SV2), with emphasis on its role topology and the four sub-protocols that compose it. Where useful, the document references concrete messages, byte layouts, state transitions, and the Stratum Reference Implementation (SRI). It assumes familiarity with Bitcoin mining, proof-of-work, and TCP/Noise-class transports.

---

## 1. Why V2 exists

Stratum V1 was a community-built JSON-RPC line protocol that grew up around 2012 and became the de-facto pool protocol. Despite being ubiquitous, it has well-known deficiencies that V2 was explicitly designed to address:

- **Plaintext transport.** V1 runs over raw TCP. Anyone on path can rewrite `mining.notify` and `mining.submit` messages — the basis for hashrate hijacking attacks observed in the wild.
- **No authentication.** Pools cannot prove identity to miners; miners cannot prove identity to pools beyond an opaque username/password.
- **JSON overhead.** Notifications carry whitespace, base16 strings, redundant identifiers. Bandwidth-bound farms (satellite, rural ISPs, large data centers bridging WAN) pay for this on every job rotation.
- **Pool-only template construction.** V1 miners hash whatever the pool tells them to hash. The pool unilaterally decides which transactions are included, giving pool operators an out-of-band lever over Bitcoin's transaction inclusion policy.
- **Coupled jobs and connections.** Every miner has its own connection; per-miner extranonce assignment is implicit and difficult to multiplex.

SV2 is a complete re-design — binary framing, encrypted-and-authenticated transport, explicit channel abstraction, and an optional **work-selection** path that lets the mining side construct its own templates from a local Bitcoin node.

It is specified across a set of BIP-style documents maintained by the SV2 working group; the public spec lives at `github.com/stratum-mining/sv2-spec`.

---

## 2. Role topology

SV2 decomposes "miner → pool" into a graph of roles that may all live in the same process, all live on different hosts, or anywhere in between. Knowing where the role boundaries fall is the prerequisite to making sense of the sub-protocols.

```
                                +-----------------------------+
                                |        Mining Pool          |
                                |  (Pool Service + JDS)       |
                                +---^-------------------^-----+
                                    |                   |
                          Mining    |          Job Decl.|
                          Protocol  |          Protocol |
                                    |                   |
+-------------+   V1/V2   +---------+----------+        |
|  Mining     |---------->|  Proxy  /  Farm    +--------+
|  Device(s)  |   Mining  |  (Translator or    |
+-------------+   Proto.  |    JD Client)      |<-----------+
                          +---------+----------+            |
                                    | Template Dist.        |
                                    | Protocol              |
                                +---v----------+            |
                                | Template     |  Job Negot.|
                                | Provider     |  (variant) |
                                | (bitcoind)   +------------+
                                +--------------+
```

The named roles in the spec:

**Mining Device (MD).** The hashing endpoint — an ASIC controller board, a CPU miner, or a software miner. Speaks the **Mining Protocol** upstream and nothing else. In a fully-deployed V2 farm an MD is usually a _standard channel_ on a proxy.

**Mining Proxy / Translator Proxy.** Aggregates many downstream miners — either V1 (`stratum+tcp://`) miners translated to V2 upstream, or already-V2 devices multiplexed onto an extended channel. In SRI this is split into:

- `translator` — V1 ⇨ V2 bridge for legacy ASIC firmware.
- `mining-proxy` — V2 ⇨ V2 aggregator.

**Mining Pool Service (Pool).** Authenticates miners, opens channels, sets targets, issues jobs (in V1-style flow), and accepts share submissions.

**Job Declarator Server (JDS).** Pool-side role that processes work-selection requests. When a miner wants to mine its own template, the JDS verifies the proposed template is well-formed and returns a token authorising it.

**Job Declarator Client (JDC).** Miner-side role co-located with the farm. Owns the local Bitcoin node, picks templates from it, and negotiates them with the JDS. In SRI this binary is `jd-client`.

**Template Provider (TP).** A Bitcoin node that emits new candidate templates over the **Template Distribution Protocol**. In practice this is a patched `bitcoind` exposing the TDP socket; the SRI also ships a TP simulator for tests.

A given deployment uses some subset:

- **Pool-controlled (V2 minimal).** Pool only. Miners take work; no JD or TP.
- **Self-mining mode.** JDC + TP at the miner. Useful for solo / federated mining.
- **Work-selection mode (the marquee deployment).** Pool + JDS + JDC + TP. The miner picks transactions and only goes to the pool for payment routing.

---

## 3. Transport: framing and Noise

### 3.1 Wire framing

Every SV2 message — encrypted or not — is preceded by a **6-byte common header**:

```
 0               1               2               3
 0 1 2 3 4 5 6 7 0 1 2 3 4 5 6 7 0 1 2 3 4 5 6 7 0 1 2 3 4 5 6 7
+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
|        extension_type         |   msg_type    |               |
+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+    msg_length |
|                                                               |
+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
|                          payload (msg_length bytes)           |
+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
```

- `extension_type` (U16, LE) — namespacing field. The high bit (`channel_msg`, `0x8000`) flags that the first 4 bytes of the payload are a `channel_id` (U32 LE). The remaining 15 bits identify the extension; `0x0000` is "base SV2".
- `msg_type` (U8) — the per-sub-protocol opcode (see §5–§7).
- `msg_length` (U24, LE) — payload length, capped at 16 MiB by the field width and in practice much lower by Noise (see below).

Type primitives are little-endian fixed widths: `U8/U16/U24/U32/U64`, `B0_255`/ `B0_64K` (length-prefixed byte strings with `U8`/`U16` length), `STR0_255` (`B0_255` interpreted as UTF-8), `SEQ0_64K[T]` (`U16` count + `T` items), plus `PUBKEY` (`B0_32`), `SIGNATURE` (`B0_64`), and `B0_31` for short ASCII.

Codec is hand-rolled, not Protobuf. Implementations parse directly from the wire buffer (`binary_sv2` crate in SRI does zero-copy decode where possible).

### 3.2 Noise layer

The transport is **Noise** with the pattern `Noise_NX_25519_ChaChaPoly_BLAKE2s`.

Pattern recap:

```
NX:
  -> e
  <- e, ee, s, es, SIGNATURE_NOISE_MESSAGE
```

- _Initiator_ (downstream) sends an ephemeral key.
- _Responder_ (upstream) sends its ephemeral, performs `ee`, then transmits its static public key (encrypted under the just-derived key), performs `es`, and finally sends a **signature blob** that binds its static key to a pool-authority key out-of-band.
- After the second message the channel is in transport mode; payloads are `ChaChaPoly`-AEAD-encrypted with associated data drawn from the Noise state.

The signature blob (`SignatureNoiseMessage`) carries:

```
version           U16
valid_from        U32  (unix seconds)
not_valid_after   U32
signature         SIGNATURE      // Ed25519 over the static key + validity range,
                                 // signed by the pool's *authority* key (out-of-band)
```

This is what closes the trust loop: a miner that knows the **pool authority public key** (configured locally; in practice published by the pool operator like a TLS fingerprint) can verify that the static key it just learned belongs to a server within a stated validity window. There is no PKI — by design, no CAs to compromise or downgrade through. Compromise of the static key has bounded blast radius via `not_valid_after`.

**Why NX and not IK or XX?** NX means the initiator does not need to know the responder's static key in advance, but still gets server authentication. That maps neatly to "miner connects to pool URL it learned out of band" without making miners ship static keys. IK was rejected because requiring a pre-known responder key complicates ops; XX is symmetric but adds a round-trip for static-key transmission that NX achieves in one fewer leg.

**Encrypted frame layout.** A Noise transport message is framed as a `U16` length prefix followed by the ciphertext (which includes the 16-byte Poly1305 tag). Maximum cleartext per Noise message is **65 519 bytes** (`2^16 − 17`). Larger SV2 messages — rare in practice — are fragmented across multiple Noise frames before SV2 reassembly.

### 3.3 SetupConnection

Once the Noise handshake completes, the initiator immediately sends a `SetupConnection` message that declares which sub-protocol it wants to speak:

```
protocol          U8     // 0 Mining, 1 Job Declaration,
                         // 2 Template Distribution
min_version       U16
max_version       U16
flags             U32    // per-sub-protocol meaning
endpoint_host     STR0_255
endpoint_port     U16
vendor            STR0_255
hardware_version  STR0_255
firmware          STR0_255
device_id         STR0_255
```

The responder replies with `SetupConnection.Success { used_version, flags }` or `SetupConnection.Error { flags, error_code }` where `error_code` is one of a small fixed set (`unsupported-feature-flags`, `unsupported-protocol`, `protocol-version-mismatch`).

A single Noise connection carries exactly one sub-protocol. Multi-protocol roles (e.g., a JDC that also runs as a Mining Protocol upstream for the local proxy) hold multiple connections.

---

## 4. Channels — the core abstraction

Stratum V1 mixed "TCP connection" and "logical work stream". V2 separates them. One Noise connection carries one or more **channels**, each with its own:

- `channel_id` (U32, scoped to the connection)
- `target` (U256 difficulty, can be updated independently)
- `extranonce_prefix` (server-assigned bytes prefixed to the coinbase nonce field)
- `job_id` (last issued job)
- `version_rolling_mask`

There are three channel kinds:

**Standard channel.** Bound to a single device. Server commits to a fixed merkle path and coinbase template; the device only varies nonce, version bits (via rolling mask) and the trailing portion of `nTime`. This is the **most bandwidth-efficient** form — `NewMiningJob` carries no merkle path, no coinbase. A device with a standard channel can mine on a header alone (≈80 bytes) per share.

**Extended channel.** Bound to a multi-device proxy. Server returns a coinbase prefix, coinbase suffix, and merkle path; the proxy may roll a larger extranonce across many downstream MDs. `NewExtendedMiningJob` carries the merkle path and coinbase fragments. This is the equivalent of a V1 connection but encapsulated as one logical channel.

**Group channel.** A virtual aggregation of standard channels for broadcast efficiency — when a new prev_hash arrives, the server can publish one `SetNewPrevHash` against `channel_id = group_channel_id` and the receiver fans it out to every member standard channel without per-channel duplication.

The choice between standard/extended is the single biggest performance lever in a deployment. Field deployments routinely use standard channels for every device and group them via a group channel on the proxy↔pool link.

---

## 5. Mining Protocol (sub-protocol 0)

The Mining Protocol is what actually carries shares. It is the closest analog to V1 `mining.notify` / `mining.submit`.

### 5.1 SetupConnection flags

```
0x01  REQUIRES_STANDARD_JOBS    // Client cannot interpret extended jobs
0x02  REQUIRES_WORK_SELECTION   // Client wants to declare its own jobs (JDP)
0x04  REQUIRES_VERSION_ROLLING  // Client supports BIP320 version rolling
```

The reply echoes a subset back to negotiate the intersection.

### 5.2 Channel lifecycle

```
DOWN -> UP : OpenStandardMiningChannel  { request_id, user_identity, nominal_hash_rate, max_target }
UP   -> DOWN: OpenStandardMiningChannel.Success
              { request_id, channel_id, target, extranonce_prefix, group_channel_id }
              or .Error { request_id, error_code }
```

`nominal_hash_rate` is in H/s (F32). The server uses it to choose an initial target sized for the device. `max_target` lets the device cap how easy the target can get (matters for FPGA / weird hardware that has a minimum useful work amount).

For extended channels the proxy sends:

```
OpenExtendedMiningChannel
  { request_id, user_identity, nominal_hash_rate, max_target,
    min_extranonce_size }   // proxy needs at least this many bytes to subdivide
```

and receives `OpenExtendedMiningChannel.Success` with `extranonce_size` (total) and `extranonce_prefix` (server-allocated portion).

`UpdateChannel { channel_id, nominal_hash_rate, maximum_target }` adjusts the target mid-flight (e.g., after device thermal throttling). `CloseChannel { channel_id, reason_code }` tears it down.

### 5.3 Work distribution

For standard channels:

```
NewMiningJob
  { channel_id, job_id, future_job: bool, version, merkle_root }
SetNewPrevHash
  { channel_id, job_id, prev_hash, min_ntime, nbits }
SetTarget
  { channel_id, maximum_target }
```

Note `merkle_root` is **already computed** — that is the entire bandwidth win of standard channels. The server has committed to a coinbase and the client is not allowed to alter the coinbase. The client only varies header fields.

`future_job = true` means the job is valid for the _next_ prev_hash, which the server will commit later via a `SetNewPrevHash` carrying the same `job_id`. This permits zero-latency rotation when a block is found: the pool pre-publishes jobs for several candidate prev_hashes and just flips the active one when the chain tip moves.

For extended channels:

```
NewExtendedMiningJob
  { channel_id, job_id, future_job, version, version_rolling_allowed,
    merkle_path: SEQ0_255[U256],
    coinbase_tx_prefix: B0_64K,
    coinbase_tx_suffix: B0_64K }
```

The proxy fills its extranonce in between the prefix and suffix, computes the coinbase txid, builds the merkle root, and either hashes directly or distributes sub-templates downstream.

### 5.4 Share submission

```
SubmitSharesStandard
  { channel_id, sequence_number, job_id, nonce, ntime, version }

SubmitSharesExtended
  { channel_id, sequence_number, job_id, nonce, ntime, version,
    extranonce: B0_32 }     // only the proxy-controlled bytes
```

Server responses are batched:

```
SubmitShares.Success { channel_id, last_sequence_number,
                       new_submits_accepted_count, new_shares_sum }
SubmitShares.Error   { channel_id, sequence_number, error_code }
```

`sequence_number` is the share counter scoped per channel — the server only ACKs up through `last_sequence_number`, making bulk-accept the common path and giving the client a credit-style flow control signal.

Error codes are an enum: `invalid-channel-id`, `stale-share`, `difficulty-too-low`, `invalid-job-id`, `invalid-nonce`, `invalid-version`, etc.

### 5.5 Custom jobs (work selection)

When `REQUIRES_WORK_SELECTION` was negotiated, the miner can send:

```
SetCustomMiningJob
  { channel_id, request_id, token: B0_255,
    version, prev_hash, min_ntime, nbits,
    coinbase_tx_version, coinbase_prefix, coinbase_tx_input_n_sequence,
    coinbase_tx_value_remaining,
    coinbase_tx_outputs: B0_64K,
    coinbase_tx_locktime,
    merkle_path: SEQ0_255[U256] }
```

`token` is the JD-issued capability returned by `AllocateMiningJobToken.Success` (§6). The pool validates that the token authorised this particular template and either accepts (`SetCustomMiningJob.Success { channel_id, request_id, job_id }`, which immediately becomes the active job for that channel) or rejects with an error code.

This is the single most important message in SV2 from a Bitcoin-decentralisation perspective. Once the token is in hand, the _miner_ — not the pool — is the entity choosing transaction inclusion.

### 5.6 Misc Mining Protocol messages

- `SetExtranoncePrefix { channel_id, extranonce_prefix }` — rotate the prefix without re-opening the channel.
- `Reconnect { new_host, new_port }` — soft redirect.
- `SetGroupChannel { group_channel_id, channel_ids: SEQ0_64K[U32] }` — bind standard channels to a group for fan-out.

---

## 6. Job Declaration Protocol (sub-protocol 1)

The JDP runs **between the JDC (miner side) and the JDS (pool side)**. Its job is to convert a locally-built template into a `token` that the Mining Protocol will accept as a `SetCustomMiningJob`.

The flow has two purposes:

1. **Token allocation** — a coarse-grained authorization that says "this miner is allowed to declare jobs charging coinbase outputs in pattern X, paying pool fee Y". This happens infrequently.
2. **Per-template declaration** — declare a specific candidate block. Happens every time a new template is mined on.

### 6.1 Token allocation

```
JDC -> JDS : AllocateMiningJobToken
  { user_identifier: STR0_255, request_id }

JDS -> JDC : AllocateMiningJobToken.Success
  { request_id,
    mining_job_token: B0_255,
    coinbase_output_max_additional_size: U32,
    coinbase_output: B0_64K,
    async_mining_allowed: bool }
```

`coinbase_output` is the pool's payout output(s); `coinbase_output_max_additional_size` is the byte budget the miner may add to the coinbase tx (for tags, OP_RETURN, etc.) beyond the pool's outputs without invalidating the token.

`async_mining_allowed` is critical: if `true`, the JDC may start hashing on a declared template **before** the JDS confirms it (the pool will retroactively validate). If `false`, the JDC must wait for `DeclareMiningJob.Success` before it points devices at the new job.

### 6.2 Declaring a specific template

```
JDC -> JDS : DeclareMiningJob
  { request_id,
    mining_job_token: B0_255,
    version: U32,
    coinbase_prefix: B0_64K,        // input script bytes before extranonce
    coinbase_suffix: B0_64K,
    tx_short_hash_list: SEQ0_64K[B0_6],   // 6-byte short hashes of full tx set
    tx_short_hash_nonce: U64,             // SipHash key the JDC used
    excess_data: B0_32 }
```

The miner does **not** send the full transactions. Instead it sends a list of 6-byte SipHash-2-4 short IDs keyed by `tx_short_hash_nonce`. This is the same short-ID trick BIP152 (compact blocks) uses, sized for the JDS's mempool to collide-detect with high probability.

JDS replies with either of:

```
JDS -> JDC : DeclareMiningJob.Success
  { request_id, new_mining_job_token: B0_255 }
```

This `new_mining_job_token` is the one the JDC then plugs into `SetCustomMiningJob` on its Mining Protocol upstream link.

Or, if the JDS could not resolve all the short hashes against its mempool:

```
JDS -> JDC : ProvideMissingTransactions
  { request_id, unknown_tx_position_list: SEQ0_64K[U16] }

JDC -> JDS : ProvideMissingTransactions.Success
  { request_id, transaction_list: SEQ0_64K[B0_16M] }
```

The miner then ships full raw transactions for the positions the JDS could not match. The JDS revalidates and (assuming success) returns `DeclareMiningJob.Success`. The reverse direction also exists — `IdentifyTransactions{,.Success}` — when the JDS wants to challenge the JDC about specific position(s) for fraud-proof reasons.

### 6.3 Submit solution

When a share at network difficulty (an actual block) is found, the miner closes the loop:

```
JDC -> JDS : SubmitSolution
  { extranonce: B0_32, prev_hash: U256, ntime, nonce, nbits, version }
```

The JDS, having already accepted the declared template, reconstructs the full block from its stored declaration + the supplied header fields and broadcasts it on the Bitcoin p2p network (typically via its own node).

### 6.4 Why this works

The economic argument is: the _pool_ still routes the payout (coinbase outputs are constrained by the token), but the _miner_ chose the transaction set. A pool that wants to censor a transaction would have to refuse the JD declaration — but that just causes the miner to mine the same template anyway under `async_mining_allowed` and find a different pool. The pool's leverage over inclusion policy collapses to "accept or lose hashrate".

---

## 7. Template Distribution Protocol (sub-protocol 2)

The TDP runs **between the JDC and a Template Provider** — in practice a patched `bitcoind`. It is the simplest sub-protocol because it just plumbs `getblocktemplate`- class data over SV2 transport.

### 7.1 Subscribing

After `SetupConnection`, the JDC immediately tells the TP how much room to leave in the coinbase outputs:

```
JDC -> TP : CoinbaseOutputDataSize
  { coinbase_output_max_additional_size: U32 }
```

This is the same budget the JDS allocated in §6.1, propagated forward so the TP's template selection doesn't blow past the block weight limit.

### 7.2 Templates

```
TP -> JDC : NewTemplate
  { template_id: U64,
    future_template: bool,
    version: U32,
    coinbase_tx_version: U32,
    coinbase_prefix: B0_64K,
    coinbase_tx_input_sequence: U32,
    coinbase_tx_value_remaining: U64,
    coinbase_tx_outputs_count: U32,
    coinbase_tx_outputs: B0_64K,
    coinbase_tx_locktime: U32,
    merkle_path: SEQ0_255[U256] }

TP -> JDC : SetNewPrevHash
  { template_id, prev_hash, header_timestamp, nbits, target }
```

Notable design choices:

- The TP does _not_ send the full tx list; the JDC asks for any transactions it doesn't already have via `RequestTransactionData { template_id }` → `RequestTransactionData.Success { excess_data, transaction_list }`. This keeps TDP cheap on every template refresh.
- `future_template = true` and `SetNewPrevHash` referencing the same `template_id` mirror the `future_job` pattern on the Mining Protocol — pre-issue, then commit.
- `coinbase_tx_value_remaining` is the amount of subsidy + fees not yet claimed by TP-provided outputs; the JDC's added outputs (and pool outputs, via JDS) consume this budget.

### 7.3 SubmitSolution

```
JDC -> TP : SubmitSolution
  { template_id, version, header_timestamp, header_nonce, coinbase_tx: B0_64K }
```

Used when the JDC wants to short-circuit the JDS path (solo / federated mining) and broadcast the block directly from its own node.

### 7.4 TP implementation note

The reference template provider is a fork of Bitcoin Core (kept on `sjors/sv2` branches and various downstream forks). It exposes the TDP over an internal IPC mechanism and is launched in-process with the node. There is no consensus rule change — only an additional service interface.

---

## 8. The fourth "sub-protocol": Job Negotiation / Job Distribution

Earlier drafts of the spec named a separate **Job Negotiation Protocol** between the JDC and a distinct _Job Negotiator_ role. In the current spec this role has been folded: what used to be JNP messages now appear as part of the **Mining Protocol** (`SetCustomMiningJob` family) and the **Job Declaration Protocol** (token allocation + DeclareMiningJob).

If you read older posts or branches:

- "JN" / "Job Negotiator" → today's **JDS** (pool side) or **JDC** (miner side).
- "Job Distribution" → the act of sending `SetCustomMiningJob` over the Mining Protocol.

The SRI repo still has a `jd-server` / `jd-client` naming reflecting the older "Job Distributor / Negotiator" wording. Protocol IDs are stable: `0` Mining, `1` Job Declaration, `2` Template Distribution.

---

## 9. End-to-end sequence: work-selection mode

A complete share-to-block lifecycle in a pool + JDS + JDC + TP deployment:

```
1. JDC <-Noise NX-> TP            SetupConnection(proto=2)
   JDC ->            TP            CoinbaseOutputDataSize
   TP  ->            JDC           NewTemplate(template_id=T1, future=true)
   TP  ->            JDC           SetNewPrevHash(template_id=T1, prev_hash=P)

2. JDC <-Noise NX-> JDS            SetupConnection(proto=1)
   JDC ->            JDS           AllocateMiningJobToken(user="farm-1")
   JDS ->            JDC           AllocateMiningJobToken.Success(token=K, coinbase_output=O)

3. JDC builds candidate block:
   - merges TP's NewTemplate with JDS's coinbase_output O
   - computes coinbase_prefix / coinbase_suffix
   - hashes its full tx set with SipHash(short_hash_nonce=N)

4. JDC ->            JDS           DeclareMiningJob(token=K, short_hash_list, nonce=N)
   JDS performs mempool short-ID match:
   - all known => JDS validates and signs off
   - some unknown => ProvideMissingTransactions / .Success roundtrip
   JDS ->            JDC           DeclareMiningJob.Success(new_token=K')

5. JDC <-Noise NX-> Pool          SetupConnection(proto=0, flags=REQUIRES_WORK_SELECTION)
   JDC ->            Pool          OpenExtendedMiningChannel(...)
   Pool->            JDC           OpenExtendedMiningChannel.Success(channel_id=C, extranonce_prefix, target)
   JDC ->            Pool          SetCustomMiningJob(channel_id=C, token=K', version, prev_hash=P, ...)
   Pool->            JDC           SetCustomMiningJob.Success(channel_id=C, job_id=J)

6. JDC fans out to devices (Mining Protocol; standard channels under a group channel):
   JDC ->            MDs           NewMiningJob(channel_id=Ci, job_id=J, merkle_root=Mi)
                                    -- one per standard channel, merkle_root differs
                                    -- because extranonce subdivision changes the coinbase txid

7. MDs hash. On a share:
   MDi ->            JDC           SubmitSharesStandard
   JDC validates, forwards to Pool as SubmitSharesExtended on channel C.
   Pool ->           JDC           SubmitShares.Success(last_sequence_number=..)

8. On a block hit:
   JDC ->            JDS           SubmitSolution(extranonce, prev_hash, ntime, nonce, ...)
   JDS reconstructs full block, broadcasts on bitcoin p2p.
   (Optionally) JDC also -> TP SubmitSolution for redundant local broadcast.
```

Step 1 happens every time the TP sees a new mempool state or block; step 4 happens every time the JDC picks a fresh template; step 6 happens whenever step 5 lands a fresh `SetCustomMiningJob.Success`. In practice all of these run at sub-second cadence and overlap heavily.

---

## 10. Stratum Reference Implementation (SRI)

The reference implementation is Rust, lives at `github.com/stratum-mining/stratum`, and is structured as a Cargo workspace.

Crate layout (annotated):

```
protocols/
  v2/
    binary-sv2/         # Wire codec for primitive types (zero-copy where possible)
    framing-sv2/        # 6-byte SV2 frame header + Noise framing
    noise-sv2/          # NX handshake + transport state machine
    codec-sv2/          # Glue: parse Noise frames -> SV2 frames -> typed messages
    subprotocols/
      common-messages/  # SetupConnection, ChannelEndpointChanged, etc.
      mining/           # Sub-protocol 0
      job-declaration/  # Sub-protocol 1
      template-distribution/  # Sub-protocol 2
    sv2-ffi/            # C ABI for embedding in non-Rust pool stacks
  v1/                   # Stratum V1 codec used by the translator
roles/
  pool/                 # Reference pool service
  jd-server/            # JDS
  jd-client/            # JDC
  mining-proxy/         # V2 -> V2 aggregator (extended channels upstream,
                        # standard channels downstream)
  translator/           # V1 (downstream) -> V2 (upstream) bridge
  mining-device/        # Test miner (CPU-only)
utils/
  message-generator/    # Scriptable e2e test harness
  bip32-derivation/     # Coinbase output derivation helpers
```

The codec separation matters: `noise_sv2` exposes a synchronous state machine (initialise → write_message → read_message), `framing_sv2` is a transport-agnostic length-prefixed framer over `bytes::BytesMut`, and `codec_sv2::StandardSv2Frame` ties them together. Async I/O is bolted on via `tokio` in the role binaries; the codec crates themselves do no I/O. This is a deliberate choice — it makes the codec embeddable in firmware that cannot afford an async runtime.

Conformance is checked by the `message-generator` test harness which scripts both sides of a connection from JSON files and asserts on the resulting message sequence. Vendor implementations are expected to clear this suite before claiming SV2 compliance.

### Other notable implementations

- **Braiins Pool** runs SV2 in production and contributed much of the original spec drafting. Braiins-OS firmware speaks V2 natively.
- **Demand Pool** (former Bitmex, now standalone) deploys SRI roles in production and has been a primary integration tester for the JD path.
- **Bitcoin Core sv2 fork** (sjors/sv2 PRs) is the upstream-tracking TP.

### V1 ↔ V2 migration

In every realistic deployment, the migration path is **terminate V1 at the proxy**:

```
[V1 ASIC] --stratum+tcp-->  [translator-proxy] --Noise/SV2--> [Pool]
```

The translator turns `mining.notify` into an SV2 `NewExtendedMiningJob` and back again. Importantly, **V1 miners do not get the security benefits** — the leg between ASIC and translator is still plaintext — but the WAN leg between farm and pool gets the full SV2 treatment. This pattern is what allows hashrate to migrate without firmware updates on every device.

---

## 11. Implementation pitfalls & open issues

A few items that bite implementers and are worth surfacing:

**1. `future_job` race against `SetNewPrevHash`.** The spec allows a miner to receive a `future_job` and then later receive its activating `SetNewPrevHash`. A naive implementation that flushes `future_job` on `SetNewPrevHash` for a _different_ job will discard the job it should be activating. The match is by `job_id`, not by arrival order.

**2. Channel-id scoping.** `channel_id` is scoped per-connection, not globally. Multi-tenant proxies that share a pool-side connection must rewrite `channel_id` in both directions; SRI's `mining-proxy` does this but a hand-rolled bridge can easily mis-map.

**3. SipHash key reuse in DeclareMiningJob.** The `tx_short_hash_nonce` MUST be fresh per declaration. Reusing it across declarations leaks structural information about the JDC's mempool. SRI rotates it on every `NewTemplate` from the TP.

**4. Noise rekey cadence.** The spec mandates rekey before the AEAD nonce wraps. ChaCha20-Poly1305 nonces are 96-bit but Noise uses a 64-bit counter — at 1M messages/sec a connection would wrap in ~584 000 years, so this is theoretical, but long-lived farm connections should still respect the rekey interval.

**5. Async work-selection failure modes.** When `async_mining_allowed = true` and the JDS later rejects a declaration that devices are already mining, the JDC must withdraw the job — `SetCustomMiningJob.Error` from the pool is the canonical signal. A buggy JDC that ignores this can have its hashrate working on a job the pool will refuse to credit shares for.

**6. Coinbase output budget accounting.** `coinbase_output_max_additional_size` is in bytes, but the relevant constraint is weight. JDC implementations must convert correctly when the added outputs include witness data (rare for coinbase but not zero).

**7. Group channel `SetNewPrevHash`.** Servers MAY send a group-channel-scoped `SetNewPrevHash`. Clients that maintain per-standard-channel state must propagate the prev_hash to _all_ member channels atomically — partial application yields stale shares on the channels not yet updated.

**8. Spec drift.** The spec is still in BIP-draft-style flux. As of the most recent published revisions, the `Reconnect` semantics, the exact error-code enumerations, and certain JDP fields have been adjusted. Pin a spec commit hash when implementing; do not target "head".

---

## 12. Quick reference: message type IDs

These are the per-sub-protocol `msg_type` opcodes (subject to spec revision; check `subprotocols/*/src/lib.rs` in SRI for the authoritative table):

### Common

```
0x00 SetupConnection
0x01 SetupConnection.Success
0x02 SetupConnection.Error
0x03 ChannelEndpointChanged
```

### Mining Protocol

```
0x10 OpenStandardMiningChannel
0x11 OpenStandardMiningChannel.Success
0x12 OpenStandardMiningChannel.Error
0x13 OpenExtendedMiningChannel
0x14 OpenExtendedMiningChannel.Success
0x15 OpenExtendedMiningChannel.Error
0x16 UpdateChannel
0x17 UpdateChannel.Error
0x18 CloseChannel
0x19 SetExtranoncePrefix
0x1a SubmitSharesStandard
0x1b SubmitSharesExtended
0x1c SubmitShares.Success
0x1d SubmitShares.Error
0x1e NewMiningJob
0x1f NewExtendedMiningJob
0x20 SetNewPrevHash
0x21 SetTarget
0x22 SetCustomMiningJob
0x23 SetCustomMiningJob.Success
0x24 SetCustomMiningJob.Error
0x25 Reconnect
0x26 SetGroupChannel
```

### Job Declaration Protocol

```
0x50 AllocateMiningJobToken
0x51 AllocateMiningJobToken.Success
0x52 DeclareMiningJob
0x53 DeclareMiningJob.Success
0x54 DeclareMiningJob.Error
0x55 IdentifyTransactions
0x56 IdentifyTransactions.Success
0x57 ProvideMissingTransactions
0x58 ProvideMissingTransactions.Success
0x60 SubmitSolution
```

### Template Distribution Protocol

```
0x70 CoinbaseOutputDataSize
0x71 NewTemplate
0x72 SetNewPrevHash
0x73 RequestTransactionData
0x74 RequestTransactionData.Success
0x75 RequestTransactionData.Error
0x76 SubmitSolution
```

(IDs are illustrative of the layout pattern — high nibble denotes sub-protocol family; the canonical numeric values live in the spec PDFs and SRI source.)

---

## 13. Further reading

- **Spec repo.** `github.com/stratum-mining/sv2-spec` — the source-of-truth.
- **Reference implementation.** `github.com/stratum-mining/stratum`.
- **Bitcoin Core fork (TP).** `github.com/Sjors/bitcoin` branches `sv2-*`.
- **Noise framework.** Trevor Perrin, `noiseprotocol.org/noise.html`. Read it before implementing — the patterns are subtle.
- **BIP320 (version-rolling).** The negotiation Stratum V2's `version_rolling_mask` re-uses verbatim.
- **BIP152 (compact blocks).** Source of the 6-byte SipHash short-ID idiom that `DeclareMiningJob` adopts.

---

_This document targets protocol-engineer depth and emphasises sub-protocols and roles. Cryptographic security analysis of Noise NX, deployment economics, and detailed migration playbooks are deliberately out of scope._