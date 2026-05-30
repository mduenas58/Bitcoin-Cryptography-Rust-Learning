# Deep Dive into Bitcoin: From Technology Stack to Future Scaling

> **A technical guide for developers, engineers, and technically-minded learners who want to understand Bitcoin from first principles — not just how to use it, but how it actually works.**

---

## Table of Contents

1. [Module 1: The Bitcoin Technology Stack](https://claude.ai/local_sessions/local_6308c29b-4764-4e8b-88be-7f12d6cac521#module-1-the-bitcoin-technology-stack)
2. [Module 2: Bitcoin Structure](https://claude.ai/local_sessions/local_6308c29b-4764-4e8b-88be-7f12d6cac521#module-2-bitcoin-structure)
3. [Module 3: Blockchain Mechanics & Transaction Validation](https://claude.ai/local_sessions/local_6308c29b-4764-4e8b-88be-7f12d6cac521#module-3-blockchain-mechanics--transaction-validation)
4. [Module 4: Scalability, Privacy, and Development](https://claude.ai/local_sessions/local_6308c29b-4764-4e8b-88be-7f12d6cac521#module-4-scalability-privacy-and-development)

---

## Module 1: The Bitcoin Technology Stack

Bitcoin is not a single monolithic system. It is a carefully composed stack of protocols and technologies, each layer serving a distinct purpose. Understanding this layered model is the foundation for everything else in this guide.

### 1.1 Overview of the Layered Architecture

Bitcoin's architecture can be modeled as four layers, often designated Layer 0 through Layer 3. Each layer abstracts complexity from the layers above it and depends on guarantees from the layers below.

```
┌────────────────────────────────────────────┐
│   Layer 3: Application Layer               │
│   (Wallets, exchanges, dApps, BTCPay)      │
├────────────────────────────────────────────┤
│   Layer 2: Scaling / Off-Chain Layer       │
│   (Lightning Network, Statechains, RGB)    │
├────────────────────────────────────────────┤
│   Layer 1: Blockchain / Consensus Layer    │
│   (Bitcoin Core, UTXO set, Script, PoW)    │
├────────────────────────────────────────────┤
│   Layer 0: P2P Network Layer               │
│   (TCP/IP, node discovery, gossip)         │
└────────────────────────────────────────────┘
```

_[Diagram: Four-layer stack of Bitcoin architecture, with arrows indicating dependency direction upward]_

---

### 1.2 Layer 0 — The P2P Network

**Layer 0** is the transport and networking substrate. Bitcoin operates as a **peer-to-peer (P2P) network** — there is no central server. Every full node is both a client and a server simultaneously.

**Key responsibilities of Layer 0:**

- **Node Discovery:** When a new node joins the network, it connects to a small set of seed nodes (hardcoded DNS seeds in Bitcoin Core). These peers share their own peer lists, allowing the node to build a connection set of 8–125 peers.
- **Message Propagation (Gossip Protocol):** Transactions and blocks are propagated by flooding — each node receiving a new piece of data validates it and forwards it to all its connected peers that haven't already seen it. This is the **inv → getdata → tx/block** message exchange pattern.
- **Network Topology:** The network is intentionally unstructured and permissionless. Thousands of nodes worldwide run Bitcoin Core (or compatible implementations) and maintain a full copy of the blockchain.

**Communication Protocol:**

Bitcoin uses a **binary P2P protocol over TCP**, typically on port **8333** (mainnet) or **18333** (testnet). Messages follow a standard envelope format:

```
┌─────────────┬─────────────┬─────────────┬────────────────┐
│ Magic Bytes │ Command     │ Length      │ Checksum       │
│ (4 bytes)   │ (12 bytes)  │ (4 bytes)   │ (4 bytes)      │
├─────────────┴─────────────┴─────────────┴────────────────┤
│ Payload (variable length)                                 │
└───────────────────────────────────────────────────────────┘
```

The **magic bytes** (`0xF9BEB4D9` for mainnet) act as a network identifier, preventing cross-network message confusion.

**Common P2P message types:**

|Message|Purpose|
|---|---|
|`version`|Handshake: announce node version, height, services|
|`verack`|Acknowledge handshake|
|`inv`|Announce inventory (tx hash or block hash)|
|`getdata`|Request full data for a known hash|
|`tx`|Transmit a raw transaction|
|`block`|Transmit a full block|
|`getblocks`|Request a list of block hashes|
|`ping/pong`|Keepalive|

---

### 1.3 Layer 1 — The Blockchain / Consensus Layer

**Layer 1** is Bitcoin's core: the **blockchain itself**, maintained through a **distributed consensus mechanism**. This is where the canonical state of all bitcoin ownership is recorded and agreed upon.

**Key components of Layer 1:**

- **The Blockchain:** A chain of blocks, each containing a set of valid transactions. Blocks are linked cryptographically — each block commits to the hash of the one before it, creating a tamper-evident history.
- **The UTXO Set:** The current state of the Bitcoin ledger — a database of all unspent transaction outputs. Every node maintains this set independently and reaches the same result by replaying all transactions from genesis.
- **Script:** Bitcoin's non-Turing-complete stack-based scripting language used to define and validate spending conditions (locking and unlocking scripts).
- **Proof-of-Work (PoW):** The consensus mechanism that makes rewriting history computationally prohibitive. Covered in depth in Module 3.
- **Difficulty Adjustment:** An algorithm that recalibrates mining difficulty every 2,016 blocks (~2 weeks) to maintain a target block time of approximately 10 minutes.

**What Layer 1 guarantees:**

- **Immutability:** Once a transaction has sufficient confirmations, reversing it requires redoing all subsequent PoW — economically infeasible.
- **Trustlessness:** Anyone with a full node can independently verify every transaction and block without trusting any third party.
- **Censorship resistance:** No single entity controls which transactions get included in blocks; miners compete and users can always try again or increase fees.

---

### 1.4 Layer 2 — Scaling / Off-Chain Protocols

**Layer 2** refers to protocols that operate _above_ Layer 1, using it as a settlement layer while enabling faster, cheaper, or more private transactions off-chain. The most prominent example is the **Lightning Network (LN)**.

**The core idea:** Two parties lock funds into a multi-signature Bitcoin transaction (a **payment channel**). They can then transact with each other an unlimited number of times off-chain by exchanging cryptographically signed **commitment transactions**. Only two on-chain transactions are ever needed: the **channel open** and the **channel close**.

**Lightning Network mechanics (summary):**

1. **Channel open:** Alice and Bob create a 2-of-2 multisig UTXO on-chain (the **funding transaction**).
2. **Off-chain payments:** They exchange signed commitment transactions that reassign the channel balance. Neither broadcasts these unless the channel closes.
3. **HTLCs (Hash Time-Locked Contracts):** Payments can be **routed** across a network of channels using HTLCs — conditional outputs that release funds only if the recipient reveals a hash preimage, enabling atomic multi-hop payments.
4. **Channel close:** Either party broadcasts the latest commitment transaction to settle on-chain.

**Other Layer 2 / adjacent protocols:**

- **Statechains:** Transfer UTXO ownership off-chain with the cooperation of a statechain entity, without touching the blockchain.
- **RGB Protocol:** Client-side validated smart contracts and token issuance on top of Bitcoin, leveraging LN for transport.
- **Fedimint:** Federated Chaumian e-cash mints anchored to Bitcoin, enabling highly private off-chain transactions.

---

### 1.5 Layer 3 — The Application Layer

**Layer 3** sits atop Layers 1 and 2 and encompasses all user-facing applications and business logic: wallets (hardware, software, custodial), exchanges, payment processors (e.g., **BTCPay Server**), and developer libraries. This layer is what most end users interact with and is outside Bitcoin's consensus rules — it can be built and changed freely.

---

## Module 2: Bitcoin Structure

Understanding _how Bitcoin data is structured_ is the difference between treating Bitcoin as a black box and understanding it as an engineer.

### 2.1 Anatomy of a Block

A **block** is the fundamental data unit of the blockchain. Each block is a container for a batch of valid transactions, plus the metadata required to link it to the chain and prove the computational work done to mine it.

_[Diagram: Block structure — Magic Number → Block Size → Block Header → Transaction Counter → Transactions list]_

**Top-level block structure (as serialized on the wire):**

|Field|Size|Description|
|---|---|---|
|**Magic Number**|4 bytes|Network identifier (`0xF9BEB4D9` for mainnet). Marks the start of a block.|
|**Block Size**|4 bytes|Size of the remaining block data in bytes (little-endian uint32).|
|**Block Header**|80 bytes|The core metadata of the block (see below).|
|**Transaction Counter**|1–9 bytes|**VarInt** — the number of transactions in this block.|
|**Transactions**|Variable|The raw serialized transactions.|

> **Note on VarInt:** Bitcoin uses a compact variable-length integer encoding. Values < 0xFD fit in 1 byte. Values up to 0xFFFF use 3 bytes (0xFD + 2 bytes). Values up to 0xFFFFFFFF use 5 bytes (0xFE + 4 bytes). Values above that use 9 bytes (0xFF + 8 bytes).

---

### 2.2 The Block Header (80 bytes)

The **block header** is the most critical 80 bytes in Bitcoin. It is _this_ 80-byte chunk that miners hash billions of times per second during mining. It commits to the entire content of the block without encoding all transactions inline.

_[Diagram: Block Header — 6 fields labeled with byte offsets and sizes]_

```
Offset  Size    Field
──────  ──────  ─────────────────────────────────────────────
0       4 B     Version
4       32 B    Previous Block Hash
36      32 B    Merkle Root
68      4 B     Time (Unix timestamp)
72      4 B     Bits (Compact difficulty target)
76      4 B     Nonce
──────  ──────
Total:  80 B
```

**Field-by-field breakdown:**

- **Version (4 bytes):** Indicates the block validation rules in use. Used historically for **BIP signaling** (miners set bits in the version field to signal readiness for soft fork activation, e.g., SegWit via BIP9).
    
- **Previous Block Hash (32 bytes):** The **double SHA-256** hash of the _preceding_ block header. This is what forms the chain — changing any past block changes its hash, which invalidates every subsequent block's "Previous Block Hash" field, requiring all subsequent PoW to be redone.
    
- **Merkle Root (32 bytes):** A single 32-byte hash that is the root of a **Merkle tree** constructed from all transaction IDs (TXIDs) in the block. It provides an efficient cryptographic commitment to the full transaction set. If any transaction is added, removed, or modified, the Merkle root changes, which changes the block header, which invalidates the PoW.
    
    ```
    How a Merkle Tree is built:
    
    TXIDs:    [TX1]  [TX2]  [TX3]  [TX4]
                   \  /          \  /
    Level 1:    Hash(TX1+TX2)  Hash(TX3+TX4)
                        \          /
    Merkle Root:    Hash(H12 + H34)
    ```
    
    _If there's an odd number of transactions, the last TXID is duplicated._
    
- **Time (4 bytes):** Unix timestamp of when the miner started hashing this block. Nodes accept blocks with timestamps within ±2 hours of their own clock. Not a perfectly precise timestamp — it's set by the miner.
    
- **Bits (4 bytes):** A compact encoding of the current **difficulty target** — the threshold below which the block hash must fall for the block to be valid. It is recalculated every 2,016 blocks. The full 256-bit target is decoded from this 4-byte compact form.
    
- **Nonce (4 bytes):** A 32-bit number that miners increment (and exhaust, cycling through 0–4,294,967,295) while searching for a valid block hash. When the nonce space is exhausted, miners typically change the **coinbase transaction** (which changes the Merkle root) and try again.
    

---

### 2.3 The Merkle Tree in Detail

_[Diagram: Merkle tree with 4 transactions, showing hash computation at each level up to the root]_

The Merkle tree has two important properties for Bitcoin:

1. **Efficient verification (SPV):** A **Simplified Payment Verification (SPV)** client — like a mobile wallet that doesn't download the full blockchain — can verify that a specific transaction is in a block by requesting only `log₂(n)` hashes (a **Merkle proof**), rather than all `n` transactions.
    
2. **Tamper detection:** Any change to any transaction changes the Merkle root, which changes the block header, which invalidates the block's PoW.
    

---

### 2.4 The UTXO Model vs. the Account Model

Bitcoin uses a **UTXO (Unspent Transaction Output)** model to track ownership. This is fundamentally different from the **account model** used by Ethereum and traditional banking.

_[Diagram: Side-by-side comparison — UTXO model (coins as discrete outputs) vs. Account model (running balance)]_

#### The Account Model (e.g., Ethereum, banks)

In the account model, the ledger stores a _balance_ for each address:

```
Address A: 5 ETH
Address B: 2 ETH
Address C: 10 ETH
```

When Alice sends 3 ETH to Bob, the ledger simply decrements Alice's balance by 3 and increments Bob's by 3. Simple — but it requires trusting that the state is correct.

#### The UTXO Model (Bitcoin)

In Bitcoin, there are **no balances** — only a set of discrete, unspent transaction outputs. Think of UTXOs as **cash bills**: each one has a fixed denomination, belongs to exactly one owner, and must be spent in full.

```
The UTXO Set (simplified):
──────────────────────────────────────────────────────────
TXID:VOUT          Amount      Locking Script (owner)
──────────────────────────────────────────────────────────
abc123:0           0.5 BTC     OP_DUP OP_HASH160 <Alice's pubkey hash> ...
abc123:1           0.3 BTC     OP_DUP OP_HASH160 <Bob's pubkey hash> ...
def456:0           1.2 BTC     OP_DUP OP_HASH160 <Alice's pubkey hash> ...
──────────────────────────────────────────────────────────
```

**Alice's "balance"** is the sum of all UTXOs locked to her address — `0.5 + 1.2 = 1.7 BTC`. This sum is computed by the wallet; the blockchain itself only knows about individual UTXOs.

**Spending a UTXO:**

When Alice wants to send 1 BTC to Charlie:

1. Alice selects UTXOs to spend as **inputs** (e.g., `abc123:0` for 0.5 BTC and `def456:0` for 1.2 BTC — total 1.7 BTC).
2. The transaction creates new **outputs**: 1.0 BTC locked to Charlie, and ~0.69 BTC back to Alice as **change**. (The difference — ~0.01 BTC — is the **miner fee**, implicitly defined as inputs minus outputs.)
3. The spent UTXOs (`abc123:0` and `def456:0`) are removed from the UTXO set. The new outputs are added.

**Why UTXO is superior for Bitcoin's goals:**

|Property|UTXO Model|Account Model|
|---|---|---|
|**Privacy**|Better (new addresses per transaction)|Worse (persistent identity)|
|**Parallelism**|High (UTXOs are independent)|Low (account state must serialize)|
|**Replay attacks**|Naturally prevented (each UTXO spent once)|Requires explicit nonce mechanism|
|**State size**|Only unspent outputs stored|All accounts stored|
|**Simplicity**|More complex to reason about for users|Simpler mental model|

---

## Module 3: Blockchain Mechanics & Transaction Validation

### 3.1 The Lifecycle of a Bitcoin Transaction

A Bitcoin transaction is a cryptographically signed data structure that destroys existing UTXOs and creates new ones. Let's trace its full lifecycle.

_[Diagram: Transaction lifecycle — Creation → Signing → Broadcast → Mempool → Mining → Block → Confirmations]_

#### Step 1: Transaction Construction

A transaction is built with the following raw structure:

```
Transaction:
├── Version (4 bytes)        — tx format version (currently 1 or 2)
├── Inputs (VarInt + list)
│   └── Input:
│       ├── Previous TXID (32 bytes) — hash of the tx containing the UTXO
│       ├── Previous Vout (4 bytes)  — output index within that tx
│       ├── ScriptSig (VarInt + bytes) — unlocking script (or empty for SegWit)
│       └── Sequence (4 bytes)       — used for RBF and timelocks
├── Outputs (VarInt + list)
│   └── Output:
│       ├── Value (8 bytes)          — amount in satoshis (1 BTC = 100,000,000 sat)
│       └── ScriptPubKey (VarInt + bytes) — locking script (spending condition)
├── Witness (SegWit only)    — witness data (signatures, scripts) per input
└── Locktime (4 bytes)       — earliest block/time the tx can be mined
```

#### Step 2: Signing

Before broadcast, inputs must be **signed** by the owner of the referenced UTXOs.

For a standard **P2PKH (Pay-to-Public-Key-Hash)** output — the most common legacy output type:

1. The wallet constructs a **signature hash (sighash)** — a serialization of the transaction with the input's ScriptPubKey inserted in place of the ScriptSig, hashed with `SHA256d` (double SHA-256).
2. The wallet signs this hash using **ECDSA** (Elliptic Curve Digital Signature Algorithm) with the private key corresponding to the address.
3. The resulting **DER-encoded signature** plus the **public key** are placed in the `ScriptSig` field of the input.

```python
# Conceptual signing flow (pseudocode)
sighash = SHA256d(serialize_tx_for_signing(tx, input_index, script_pubkey))
signature = ECDSA.sign(private_key, sighash)
script_sig = encode_push(signature + SIGHASH_ALL) + encode_push(public_key)
```

**SIGHASH types** determine which parts of the transaction are committed to by the signature:

|SIGHASH type|What is signed|
|---|---|
|`SIGHASH_ALL` (0x01)|All inputs and outputs (most common)|
|`SIGHASH_NONE` (0x02)|All inputs, no outputs|
|`SIGHASH_SINGLE` (0x03)|All inputs, only the corresponding output|
|`SIGHASH_ANYONECANPAY`|Combined with above; signs only this one input|

#### Step 3: Broadcast to the Network

The signed raw transaction is serialized to hex and broadcast to one or more nodes via the P2P `tx` message (or via RPC: `sendrawtransaction`). Each receiving node performs **mempool admission checks** before forwarding it further.

#### Step 4: The Mempool

Each node maintains a **mempool** (memory pool) — a local, non-consensus data structure holding valid but unconfirmed transactions awaiting inclusion in a block.

**Mempool admission checks performed by each node:**

- All referenced UTXOs exist and are unspent.
- The transaction is properly formatted (valid serialization, non-zero outputs).
- The total input value ≥ total output value (no inflation).
- The unlocking script (`ScriptSig` / witness) correctly satisfies the locking script (`ScriptPubKey`) of each referenced UTXO.
- No conflicting transaction already in the mempool (double-spend attempt).
- The fee rate meets the node's minimum relay fee (default: 1 sat/vByte in Bitcoin Core).
- The transaction is not already confirmed in the chain.

Transactions that pass all checks are added to the mempool and relayed to peers. Transactions in the mempool are **not guaranteed** to be confirmed — they can be evicted if the mempool fills up (default limit: 300 MB) and higher-fee transactions arrive.

#### Step 5: Mining — Block Inclusion

Miners select transactions from the mempool to include in the next block. Their primary incentive is to maximize **fee revenue** (plus the block subsidy), so they typically employ a **fee-rate-first selection** strategy, filling blocks up to the weight limit with the highest fee-rate transactions.

The transaction is included in a block and broadcast to the network. Once that block is found and propagated, the transaction has **1 confirmation**. With each subsequent block mined on top of it, it gains another confirmation. By convention, **6 confirmations** (~60 minutes) is considered irreversible for most purposes.

---

### 3.2 Proof-of-Work: The Heart of Bitcoin Consensus

**Proof-of-Work (PoW)** is the mechanism by which Bitcoin achieves decentralized consensus. It makes the cost of rewriting history proportional to the honest network's cumulative computational work — a property no other consensus mechanism has replicated at Bitcoin's security level.

_[Diagram: Mining loop — assemble block header → hash → compare to target → if above target, increment nonce → repeat; if below target, broadcast block]_

#### The Hashing Process: SHA-256

Bitcoin uses **SHA-256** applied _twice_ — often written as **SHA256d** or **HASH256**:

```
Block Hash = SHA256( SHA256( Block Header ) )
```

SHA-256 produces a 256-bit (32-byte) output. For a block to be valid, its hash — interpreted as a 256-bit big-endian integer — must be _less than or equal to_ the current **difficulty target**.

**Example of a valid block hash:**

```
0000000000000000000350d1b5e92d8a5a99a36f7a39e0a3f03ad0a3a3ea5a2d
```

Note the leading zeros. The more leading zeros required, the harder (and rarer) the valid hash.

#### The Mining Loop

```python
# Simplified mining pseudocode
block_header = assemble_header(
    version=version,
    prev_hash=previous_block_hash,
    merkle_root=compute_merkle_root(transactions),
    timestamp=current_time(),
    bits=current_difficulty_bits,
    nonce=0
)

while True:
    candidate_hash = SHA256d(block_header)
    if candidate_hash < target:
        broadcast_block(block_header, transactions)
        break
    block_header.nonce += 1
    if block_header.nonce > 0xFFFFFFFF:
        # Nonce space exhausted — change the coinbase extra nonce
        # (which changes the Merkle root, giving a fresh nonce space)
        block_header.nonce = 0
        increment_extranonce(transactions[0])  # coinbase tx
        block_header.merkle_root = compute_merkle_root(transactions)
```

Since SHA-256 is a **one-way function**, there is no shortcut. The only way to find a valid hash is brute force. The probability of any single hash being valid is approximately `1 / difficulty`. At the time of writing, the Bitcoin network performs on the order of **700 exahashes per second (700 × 10¹⁸ hashes/sec)**.

#### Difficulty Adjustment

Every **2,016 blocks**, Bitcoin adjusts the difficulty target using the following algorithm:

```
New Target = Old Target × (Actual Time for 2016 blocks / Expected Time)
           = Old Target × (Actual Time / 1,209,600 seconds)
```

Where 1,209,600 seconds = 2 weeks (2,016 blocks × 10 minutes × 60 seconds).

**Bounds:** The adjustment is capped at a factor of **4× in either direction** per period, preventing extreme oscillations.

**Difficulty** is derived from the target:

```
Difficulty = Genesis Target / Current Target
           ≈ 0x00000000FFFF0000... / Current Target
```

A higher difficulty means a smaller target (more leading zeros required) — harder mining. A lower difficulty means a larger target — easier.

_[Diagram: Graph of Bitcoin difficulty over time, showing exponential growth as hashrate increased]_

#### Block Propagation

Once a valid block is found, the miner immediately broadcasts it via the P2P network. Speed matters — every second of delay means other miners are working on a competing block, risking a **stale block** (a valid block that loses the race and gets orphaned).

Protocols like **Compact Block Relay (BIP 152)** optimize propagation: instead of sending the full block, miners send only a block header + short transaction IDs. Peers reconstruct the full block from their mempools, requesting only the transactions they're missing.

---

### 3.3 Script: Bitcoin's Locking and Unlocking Language

**Bitcoin Script** is a stack-based, **intentionally non-Turing-complete** scripting language. Non-Turing-complete means it has no loops — scripts are guaranteed to terminate, preventing denial-of-service attacks via infinite execution.

Every UTXO has a **locking script** (`ScriptPubKey`) that defines the condition to spend it. Every spending input provides an **unlocking script** (`ScriptSig` or witness data) that must satisfy the locking script.

**Validation:** The unlocking script runs first, pushing data onto the stack. Then the locking script runs against the same stack. If the final stack contains a single non-zero value (TRUE), the spend is valid.

#### Standard Script Types

**P2PKH (Pay-to-Public-Key-Hash)** — the classic legacy address type (`1...`):

```
Locking (ScriptPubKey):
  OP_DUP OP_HASH160 <pubKeyHash> OP_EQUALVERIFY OP_CHECKSIG

Unlocking (ScriptSig):
  <signature> <publicKey>

Execution (simplified):
  Stack after ScriptSig:  [<sig>, <pubKey>]
  OP_DUP:                 [<sig>, <pubKey>, <pubKey>]
  OP_HASH160:             [<sig>, <pubKey>, HASH160(<pubKey>)]
  PUSH <pubKeyHash>:      [<sig>, <pubKey>, HASH160(<pubKey>), <pubKeyHash>]
  OP_EQUALVERIFY:         [<sig>, <pubKey>]  — fails if hashes differ
  OP_CHECKSIG:            [TRUE]             — verifies ECDSA sig against pubKey
```

**P2SH (Pay-to-Script-Hash)** — allows complex conditions hashed into an address (`3...`):

```
Locking (ScriptPubKey):
  OP_HASH160 <scriptHash> OP_EQUAL

Unlocking (ScriptSig):
  <data...> <redeemScript>

(Node hashes the redeemScript, checks it matches scriptHash, then executes redeemScript)
```

**P2WPKH (Pay-to-Witness-Public-Key-Hash)** — SegWit native address (`bc1q...`):

```
Locking (ScriptPubKey):
  OP_0 <20-byte pubKeyHash>

Witness (replaces ScriptSig):
  [<signature>, <publicKey>]
```

**P2TR (Pay-to-Taproot)** — Taproot address (`bc1p...`):

```
Locking (ScriptPubKey):
  OP_1 <32-byte tweaked pubKey>

Witness:
  Key path: [<Schnorr signature>]
  Script path: [<script>, <control block>]
```

#### Signature Verification

`OP_CHECKSIG` is where the cryptographic security of Bitcoin lives:

1. Pop the **public key** and **signature** from the stack.
2. Compute the **sighash** of the transaction (same process as during signing).
3. Verify the signature against the sighash using the public key via **ECDSA** (legacy) or **Schnorr** (Taproot).
4. Push `TRUE` or `FALSE` to the stack.

**ECDSA** uses the `secp256k1` elliptic curve — the same curve used throughout Bitcoin. A private key is a 256-bit integer; the public key is the corresponding point on the curve (compressed to 33 bytes: a parity byte + the 32-byte x-coordinate).

---

## Module 4: Scalability, Privacy, and Development

### 4.1 Scalability

Bitcoin's base layer is intentionally constrained. Understanding _why_ those constraints exist — and what's being done about them — requires understanding the **decentralization trilemma**: it is extremely difficult for a blockchain to simultaneously maximize decentralization, security, and throughput.

#### The Base Layer Limitations

**Block size / Block weight limit:**

- Prior to SegWit: 1 MB block size limit → ~3–7 transactions per second (TPS).
- After SegWit: The limit became 4 million **weight units** (vBytes). A typical SegWit transaction weighs ~140 vBytes. This allows ~7–15 TPS in practice.
- For context: VISA processes ~24,000 TPS globally.

**Why not simply increase the block size?** Larger blocks:

- Take longer to propagate, increasing the rate of **orphaned blocks** and centralization toward large mining pools with fast connections.
- Require more storage and bandwidth to run a full node, reducing the number of independent validators.
- Increase the UTXO set size, raising the resource requirements for full nodes.

**Block time — 10 minutes:**

A 10-minute block interval gives enough time for a block to propagate globally before the next one is found. Reducing block time (as Litecoin does at 2.5 minutes) increases orphan rates and weakens the security model.

---

#### SegWit (Segregated Witness) — BIP141

**SegWit**, activated in August 2017, is one of the most significant Bitcoin upgrades. It restructured how transaction data is serialized, with two primary benefits:

**1. Transaction malleability fix:**

Before SegWit, a third party could modify a transaction's `ScriptSig` data (and therefore its TXID) without invalidating it — a property called **transaction malleability**. This broke protocols that relied on unconfirmed TXIDs (like Lightning channels). SegWit moved signature data to the **witness**, which is excluded from TXID computation.

**2. Effective block capacity increase:**

SegWit introduced **weight units**: legacy data costs 4 weight units per byte; witness data costs only 1 weight unit per byte. Since signatures (the bulk of transaction data) moved to the witness, SegWit transactions are effectively "lighter" — allowing more transactions per block.

```
Block weight limit: 4,000,000 weight units

Legacy tx (P2PKH):   ~600 weight units per tx → ~3-4 TPS
SegWit tx (P2WPKH):  ~444 weight units per tx → ~5-7 TPS
```

**3. Script versioning:**

SegWit introduced a **script version byte** in output scripts (`OP_0`, `OP_1`, ...). This enables future soft fork upgrades to define new script semantics without requiring a new output type. Taproot (`OP_1`) is the first use of this.

---

#### Lightning Network (LN) — Layer 2 Scaling

As detailed in Module 1, the Lightning Network enables **millions of TPS** by taking the vast majority of transactions off-chain.

_[Diagram: Alice → Bob → Carol payment routing via HTLC chain through Lightning channels]_

**Key scalability properties:**

- Payments settle instantly (sub-second) rather than waiting 10 minutes.
- Fees are measured in **millisatoshis** — fractions of a satoshi — making micropayments viable.
- The network processes payments without touching the blockchain at all; only channel opens/closes appear on-chain.
- **Routing** discovers paths through the channel graph using the **BOLT 7** gossip protocol and the **Dijkstra/modified Bellman-Ford** algorithm for path-finding.

**Limitations of LN:**

- Requires online presence (or a **watchtower**) to detect and punish cheating peers.
- Liquidity management: channels must have sufficient outbound/inbound capacity on the right side.
- Not suitable for large payments (routing liquidity constraints).

---

#### Schnorr Signatures & Taproot — BIP340/341/342

**Taproot**, activated in November 2021, is Bitcoin's most significant upgrade since SegWit. It bundles three BIPs:

**BIP340 — Schnorr Signatures:**

- Replace ECDSA for Taproot outputs.
- **Linear:** `sig(a + b) = sig(a) + sig(b)` — enables **key aggregation** (MuSig2).
- **Smaller:** 64 bytes instead of 71–73 bytes (DER-encoded ECDSA).
- **Faster** to verify in batch.
- **Non-malleable** by design.

**BIP341 — Taproot:**

Taproot outputs commit to a **tweaked public key** that encodes two spending paths:

```
Taproot output = P + H(P || merkle_root) × G

Where:
  P = internal public key (the "key path" spending key)
  merkle_root = root of a Merkle tree of scripts (the "script paths")
  G = secp256k1 generator point
  H() = tagged hash function
```

- **Key path spend:** If all parties agree, they use MuSig2 to produce a single Schnorr signature — indistinguishable on-chain from a simple single-sig payment. A Lightning channel close, a multisig, and a HTLC all _look the same_ on-chain when cooperatively closed.
- **Script path spend:** If cooperation fails, the spender reveals the specific script they want to use, proves it's committed in the Merkle tree, and executes it. Only the _used_ script is revealed — all other spending conditions remain private.

**Privacy and efficiency benefits of Taproot:**

- Complex smart contracts (multisig, time locks, LN channels) are **indistinguishable** from simple payments on-chain in the cooperative case.
- Reduces the on-chain footprint of LN channel operations.
- Enables **PTLCs (Point Time-Locked Contracts)** — a replacement for HTLCs that use Schnorr adaptor signatures, eliminating the payment hash correlation vulnerability in current LN routing.

**BIP342 — Tapscript:**

Updates the Script interpreter for Taproot script paths. Notably enables `OP_CHECKSIGADD` for efficient multi-sig and adds the Schnorr signature opcode.

---

### 4.2 Privacy

#### Bitcoin is Pseudonymous, Not Anonymous

A widespread misconception is that Bitcoin is anonymous. In reality, Bitcoin is **pseudonymous**: every transaction is permanently and publicly recorded on the blockchain. The pseudonym is the Bitcoin address — a hash of a public key. But addresses can often be linked to real identities.

_[Diagram: Blockchain explorer showing address activity — illustrating how address clustering works]_

**Why Bitcoin privacy is weaker than it appears:**

- **Address reuse:** If you receive two payments to the same address, an observer can link them.
- **Input clustering heuristic:** A common chain analysis assumption is that all inputs in a transaction are controlled by the same entity (they were all signed, so the same wallet likely controls them).
- **Change address detection:** Heuristics can often identify which output is the change (e.g., a round-number payment vs. an irregular change amount).
- **KYC leakage:** If any address in a transaction cluster is linked to a KYC'd exchange account, the entire cluster can be de-anonymized.
- **UTXO graph analysis:** Blockchain analytics firms (Chainalysis, Elliptic) construct probabilistic ownership graphs of the entire UTXO history.

**Best practices for privacy on-chain:**

- Use a **new address for every payment** (HD wallets — BIP32/44 — make this automatic).
- Avoid address reuse.
- Use **full nodes** rather than SPV wallets that leak address-to-IP mappings.
- Use **Tor or I2P** to mask your node's IP address when broadcasting transactions.
- Prefer **SegWit and Taproot** outputs — they are less fingerprintable.

---

#### CoinJoin

**CoinJoin** (proposed by Gregory Maxwell in 2013) is a trustless technique to combine multiple users' transactions into a single transaction, breaking the input-clustering heuristic.

_[Diagram: CoinJoin — inputs from 5 users → single transaction → 5 equal-amount outputs, indistinguishable]_

**How it works:**

1. Alice wants to send 0.1 BTC, Bob wants to send 0.1 BTC, Carol wants to send 0.1 BTC.
2. They coordinate (via a server or P2P protocol) to build a single transaction with:
    - 3 inputs (one from each)
    - 3 **equal-denomination outputs** of 0.1 BTC (plus change outputs)
3. Each party signs only after verifying their input and output are present.
4. No party can steal funds (signing is atomic) and the coordinator sees no more than each individual party sees.

**Equal-denomination outputs** are key: an observer cannot tell which input funded which output when outputs are identical amounts. This is the **anonymity set** — the larger the set, the stronger the privacy.

**CoinJoin implementations:**

|Implementation|Architecture|Notes|
|---|---|---|
|**JoinMarket**|Decentralized market (makers/takers)|Most private; no central coordinator|
|**Wasabi Wallet**|Centralized coordinator|ZeroLink protocol; client-side filtering|
|**Whirlpool (Samourai)**|Centralized coordinator|Fixed denominations; multiple remixes|
|**Joinstr**|Nostr-based coordination|Experimental; fully decentralized|

---

#### Taproot's Privacy Improvements

As described in 4.1, **Taproot** improves privacy at the protocol level:

- **Script uniformity:** Key-path Taproot spends all look identical on-chain. A LN channel close, a 5-of-7 multisig vault, a time-locked inheritance contract, and a regular payment are cryptographically indistinguishable in the cooperative case.
- **Script hiding:** In a script-path spend, only the specific script branch used is revealed. Other branches remain hidden.
- **PTLCs:** When PTLCs replace HTLCs in LN, individual payment route hops will no longer share a common payment hash, eliminating a significant correlation attack vector for LN routing nodes.

---

### 4.3 Development: Interacting with Bitcoin

There is a rich ecosystem of tools and libraries for Bitcoin development. Here's an opinionated overview by layer and use case.

#### Bitcoin Core: The Reference Implementation

**Bitcoin Core** is the dominant full node implementation. It is the reference for protocol behavior and provides:

- A full node with P2P connectivity and blockchain sync.
- A **JSON-RPC API** for querying blockchain data, submitting transactions, and managing a built-in wallet.
- `bitcoin-cli` — a command-line client for the RPC interface.

**Common `bitcoin-cli` commands:**

```bash
# Get general blockchain info
bitcoin-cli getblockchaininfo

# Get a specific block by hash
bitcoin-cli getblock <blockhash> 2

# Decode a raw transaction
bitcoin-cli decoderawtransaction <hex>

# Get a UTXO's details
bitcoin-cli gettxout <txid> <vout>

# Create, sign, and send a raw transaction
bitcoin-cli createrawtransaction '[{"txid":"<txid>","vout":0}]' '{"<address>":0.001}'
bitcoin-cli signrawtransactionwithwallet <hex>
bitcoin-cli sendrawtransaction <signed_hex>

# List unspent UTXOs in the node's wallet
bitcoin-cli listunspent

# Get the current mempool
bitcoin-cli getrawmempool true
```

**bitcoin.conf — key settings:**

```ini
# bitcoin.conf
network=signet          # Use Signet for development (safe testnet with faucet)
server=1                # Enable RPC server
rpcuser=myuser
rpcpassword=mypassword
rpcbind=127.0.0.1
rpcport=38332           # Signet RPC port (mainnet: 8332)
txindex=1               # Index all transactions (needed for many queries)
```

---

#### Libraries for Bitcoin Development

**Go — btcsuite/btcd:**

`btcd` is a full Bitcoin node implementation in Go. The `btcsuite` ecosystem provides excellent libraries for low-level Bitcoin work.

```go
package main

import (
    "fmt"
    "github.com/btcsuite/btcd/btcec/v2"
    "github.com/btcsuite/btcd/btcutil"
    "github.com/btcsuite/btcd/chaincfg"
    "crypto/rand"
)

func main() {
    // Generate a new private key
    privKey, err := btcec.NewPrivateKey()
    if err != nil {
        panic(err)
    }

    // Derive the public key
    pubKey := privKey.PubKey()

    // Derive a P2WPKH address (native SegWit, bc1q...)
    pubKeyHash := btcutil.Hash160(pubKey.SerializeCompressed())
    addr, err := btcutil.NewAddressWitnessPubKeyHash(pubKeyHash, &chaincfg.MainNetParams)
    if err != nil {
        panic(err)
    }

    fmt.Printf("Private Key (WIF): %s\n", /* encode to WIF */ "...")
    fmt.Printf("Address:           %s\n", addr.EncodeAddress())
}
```

Key `btcsuite` packages:

|Package|Purpose|
|---|---|
|`btcd/wire`|P2P message serialization/deserialization|
|`btcd/blockchain`|Block validation, chain management|
|`btcd/txscript`|Script engine, script construction/parsing|
|`btcd/btcec`|secp256k1 ECDSA and Schnorr crypto|
|`btcutil`|Address encoding/decoding, WIF, HD wallets|
|`btcwallet`|Wallet management|
|`neutrino`|BIP157/158 compact client filter SPV client|

---

**JavaScript — bitcoinjs-lib:**

`bitcoinjs-lib` is the most widely used JavaScript library for Bitcoin. It is used extensively in web wallets, exchanges, and payment tools.

```javascript
const bitcoin = require('bitcoinjs-lib');
const { ECPairFactory } = require('ecpair');
const ecc = require('tiny-secp256k1');
const ECPair = ECPairFactory(ecc);

// Generate a new key pair and P2WPKH address
const keyPair = ECPair.makeRandom();
const { address } = bitcoin.payments.p2wpkh({
  pubkey: keyPair.publicKey,
  network: bitcoin.networks.bitcoin
});
console.log('Address:', address);  // bc1q...

// Build and sign a transaction
const psbt = new bitcoin.Psbt({ network: bitcoin.networks.bitcoin });

psbt.addInput({
  hash: '<previous txid>',
  index: 0,
  witnessUtxo: {
    script: Buffer.from('<scriptPubKey hex>', 'hex'),
    value: 100000  // satoshis
  }
});

psbt.addOutput({
  address: '<recipient address>',
  value: 90000  // satoshis (10000 sat fee)
});

psbt.signInput(0, keyPair);
psbt.finalizeAllInputs();

const rawTx = psbt.extractTransaction().toHex();
console.log('Signed TX:', rawTx);
```

**Note on PSBTs:** The example above uses **PSBT (Partially Signed Bitcoin Transaction)** format (BIP174). PSBTs are the standard interchange format for multi-party signing workflows — hardware wallets, multisig coordinators, and CoinJoin all use PSBTs to pass partially-signed transactions between parties without trusting any single party with all private keys.

---

**Python — python-bitcoinlib:**

```python
from bitcoin import SelectParams
from bitcoin.core import CTransaction, CTxIn, CTxOut, COutPoint, lx, COIN
from bitcoin.core.script import CScript, OP_DUP, OP_HASH160, OP_EQUALVERIFY, OP_CHECKSIG
from bitcoin.wallet import CBitcoinAddress, CBitcoinSecret
import hashlib

SelectParams('mainnet')

# Decode an address to get its script
address = CBitcoinAddress('1A1zP1eP5QGefi2DMPTfTL5SLmv7Divf Na')
script_pubkey = address.to_scriptPubKey()
print(script_pubkey)
# Output: CScript([OP_DUP, OP_HASH160, <20-byte hash>, OP_EQUALVERIFY, OP_CHECKSIG])
```

---

#### Development Environments

**Signet** (BIP325) is the recommended development network:

- A testnet variant with centralized block signing — no real mining, so blocks are produced reliably every ~10 minutes.
- Coins are worthless but obtainable from faucets.
- Closely mirrors mainnet behavior (same script rules, same SegWit/Taproot support).

**Regtest** (Regression Test mode) is for pure local development:

- You control block production entirely (`bitcoin-cli generatetoaddress 101 <addr>`).
- No network connection required.
- Ideal for testing transaction flows and smart contracts without any external dependencies.

```bash
# Start Bitcoin Core in regtest mode
bitcoind -regtest -daemon

# Mine 101 blocks to a local address (101 because coinbase matures at 100 confirmations)
bitcoin-cli -regtest generatetoaddress 101 $(bitcoin-cli -regtest getnewaddress)

# Check balance
bitcoin-cli -regtest getbalance
```

---

## Conclusion

Bitcoin's elegance lies in how its components compose. The P2P network ensures censorship resistance. The UTXO model and Script language define ownership without accounts. SHA-256 PoW and the longest-chain rule create trustless consensus. SegWit and Taproot optimize for efficiency and privacy. The Lightning Network extends Bitcoin's reach to near-instant micropayments. And the entire system runs without a central authority — verified independently by thousands of nodes worldwide.

**The key mental models to internalize:**

1. **Bitcoin is a protocol, not a company.** Consensus rules are enforced by every full node independently.
2. **UTXOs are coins, not balances.** The blockchain tracks discrete outputs, not account states.
3. **The block header is the nucleus.** Mining, linking, and verification all operate on this 80-byte structure.
4. **Script enables programmable money.** Spending conditions are arbitrary programs — from simple signatures to time-locks to multi-party agreements.
5. **Layer 2 extends, not replaces, Layer 1.** Lightning uses Bitcoin's security guarantees as its foundation — it doesn't bypass them.
6. **Privacy is not the default.** It requires deliberate design choices at the wallet, transaction, and protocol level.

---

## Further Reading & Resources

- **Bitcoin Developer Documentation:** https://developer.bitcoin.org
- **Bitcoin Improvement Proposals (BIPs):** https://github.com/bitcoin/bips
- **Mastering Bitcoin (Andreas Antonopoulos):** https://github.com/bitcoinbook/bitcoinbook
- **Learning Bitcoin from the Command Line:** https://github.com/BlockchainCommons/Learning-Bitcoin-from-the-Command-Line
- **Bitcoin Optech Newsletter:** https://bitcoinops.org
- **BOLT Specifications (Lightning Network):** https://github.com/lightning/bolts
- **btcd source code:** https://github.com/btcsuite/btcd
- **bitcoinjs-lib:** https://github.com/bitcoinjs/bitcoinjs-lib

---

_Guide version 1.0 — May 2026_ _Technical content accurate as of Bitcoin Core 27.x and Lightning Network BOLTs as of 2025._