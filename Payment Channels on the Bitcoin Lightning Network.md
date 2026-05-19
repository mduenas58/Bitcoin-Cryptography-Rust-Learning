# Payment Channels on the Bitcoin Lightning Network

## A deep dive into channel lifecycle: open, update, and close

> Scope: This document focuses on the **bilateral payment channel** as specified by the original Poon–Dryja construction and codified in the Lightning BOLT specifications (primarily BOLT #2 "Peer Protocol for Channel Management" and BOLT #3 "Bitcoin Transaction and Script Formats"). HTLCs and multi-hop routing are referenced only where they intersect channel state; they are not the primary subject.

---

## 1. Motivation and core problem

Bitcoin's base layer commits every state transition to a global, replicated ledger. Block space is scarce, confirmation is probabilistic, and fees scale with demand. For a system that must clear millions of small, latency-sensitive payments, on-chain settlement of each one is structurally impossible.

A **payment channel** is a construct that lets two parties transact an unbounded number of times by exchanging cryptographically-enforceable promises off-chain, while touching the base layer only twice in the common case: once to open the channel and once to close it. The intermediate states are kept "alive" by a credible threat: if either party deviates, the other can publish proof to the blockchain and confiscate the cheater's funds.

The construction must satisfy three properties simultaneously:

1. **Trust-minimization** — neither party can steal funds, even given full control of the network and arbitrary computation.
2. **Instant finality from the participants' perspective** — once a state update is signed and revoked, the receiver can treat the new balance as final without waiting for block confirmation.
3. **Unilateral exit** — at any moment, either party can settle the latest agreed state on-chain without the cooperation of the other.

The Poon–Dryja channel is the canonical solution. It achieves these via three primitives: a 2-of-2 multisig funding output, asymmetric commitment transactions with delayed self-spends, and a revocation mechanism built around a deterministic key-derivation tree.

---

## 2. Cryptographic primitives and notation

Throughout, I'll use the following notation, consistent with BOLT #3:

- Two parties: **A** (the funder, who initiated `open_channel`) and **B** (the fundee, who responded with `accept_channel`).
- `payment_basepoint`, `delayed_payment_basepoint`, `htlc_basepoint`, `revocation_basepoint`: long-lived per-party public keys exchanged in `open_channel`/`accept_channel`.
- `per_commitment_point` — a per-state ephemeral point. State `i` uses `per_commitment_point_i = per_commitment_secret_i · G`, where the secret is derived from a 256-bit `per_commitment_seed` via the BOLT #3 deterministic key-tree (a structured pseudorandom hash chain that allows compact storage of all revoked secrets — see §6).
- `to_self_delay` — a `OP_CHECKSEQUENCEVERIFY` value (in blocks) negotiated at open time. It's the contestation window during which a published commitment can be revoked. Each side specifies the delay imposed on **the other's** local commitment.
- `dust_limit_satoshis` — the minimum output value below which outputs are dropped (and the funds folded into miner fees, since they can't be economically spent).

The per-commitment derived keys are tweaked combinations of the basepoints and the per-commitment point. For state `i` from A's perspective:

```
localpubkey_i        = payment_basepoint_A          + SHA256(per_commitment_point_i || payment_basepoint_A) · G
local_delayedpubkey_i = delayed_payment_basepoint_A + SHA256(per_commitment_point_i || delayed_payment_basepoint_A) · G
revocationpubkey_i   = revocation_basepoint_B · SHA256(revocation_basepoint_B || per_commitment_point_i)
                     + per_commitment_point_i      · SHA256(per_commitment_point_i || revocation_basepoint_B)
```

The crucial property of `revocationpubkey_i` is that its **private key** can only be reconstructed by someone who knows both the `revocation_basepoint_secret` (held by B) **and** the `per_commitment_secret_i` (held by A). Neither party alone can sign with it. Revocation happens precisely when A discloses `per_commitment_secret_i` to B — at that moment, and only at that moment, B (and only B) acquires the ability to sign for `revocationpubkey_i`.

This asymmetry is the linchpin of the entire protocol. Hold onto it; everything below pivots on it.

---

## 3. Channel opening

### 3.1 Negotiation messages

Opening proceeds through a fixed message exchange over the encrypted Lightning transport (BOLT #8 Noise_XK):

```
A → B : open_channel        (chain_hash, temporary_channel_id, funding_satoshis,
                              push_msat, dust_limit, max_htlc_value_in_flight,
                              channel_reserve, htlc_minimum, feerate_per_kw,
                              to_self_delay, max_accepted_htlcs,
                              funding_pubkey, *_basepoints, first_per_commitment_point,
                              channel_flags)
B → A : accept_channel      (minimum_depth, funding_pubkey, *_basepoints,
                              first_per_commitment_point, and B's parameters)
A → B : funding_created     (temporary_channel_id, funding_txid, funding_output_index,
                              signature_for_B's_first_commitment_tx)
B → A : funding_signed      (channel_id, signature_for_A's_first_commitment_tx)
A     : broadcasts funding transaction to the Bitcoin network
A,B   : wait for `minimum_depth` confirmations
A → B : channel_ready
B → A : channel_ready
```

The `temporary_channel_id` is a random 32-byte identifier used until the funding outpoint exists; the canonical `channel_id` is then `funding_txid XOR funding_output_index` (zero-padded), giving a stable handle even across reorganizations of identifiers.

### 3.2 The funding transaction

The funding transaction is an ordinary on-chain Bitcoin transaction whose relevant output is a 2-of-2 multisig (today, almost always a P2WSH-wrapped one; with the rollout of Taproot channels under BOLT #3's `option_simple_taproot`, it becomes a single MuSig2-aggregated key in a P2TR output):

```
witnessScript = 2 <funding_pubkey_A> <funding_pubkey_B> 2 OP_CHECKMULTISIG
scriptPubKey  = OP_0 <SHA256(witnessScript)>           // P2WSH
```

Crucially, **A does not broadcast this transaction until B has signed A's first commitment transaction**. Otherwise, the funds would be locked in a 2-of-2 with B holding veto power and no pre-signed escape hatch, allowing B to extort A indefinitely. The exchange order — `funding_created` carries A's signature on B's first commitment, then `funding_signed` carries B's signature on A's first commitment, then A broadcasts funding — is precisely designed to eliminate this hostage scenario.

For dual-funded channels (BOLT #2's `option_dual_fund`, building on PSBT-based interactive transaction construction in BOLT #2 v2 / "v2 channel open"), both parties contribute inputs and the protocol becomes a multi-round PSBT exchange. The principle is unchanged: no party signs the funding inputs until they hold valid pre-signed unilateral exits.

### 3.3 The initial commitment transactions

Before the funding tx is broadcast, two **commitment transactions** exist — one held by each party, both spending the same (not-yet-existing) funding output. They are asymmetric: A's commitment can only be broadcast by A and pays out under terms favorable for B to punish; B's is the mirror image.

For the initial state where A funded the entire `funding_satoshis` and pushed `push_msat` to B:

**A's local commitment (the one A holds and can broadcast):**

- Input: funding output (requires both signatures; A pre-signs at broadcast time, B's signature was received in `funding_signed`).
- `nLocktime` and `nSequence` are obfuscated to encode the commitment number (an anti-surveillance feature — see §4.4).
- Output 1 — `to_local`: pays `local_balance` to a script
    
    ```
    OP_IF    # Punishment path — B publishes within to_self_delay    <revocationpubkey>OP_ELSE    `to_self_delay`    OP_CHECKSEQUENCEVERIFY    OP_DROP    <local_delayedpubkey>OP_ENDIFOP_CHECKSIG
    ```
    
- Output 2 — `to_remote`: pays `remote_balance` directly to B's `remotepubkey` (in `option_anchors`, wrapped with a 1-block CSV; pre-anchors it was a bare P2WPKH).
- (In states with in-flight payments, additional HTLC outputs appear here, each with their own revocable script. Omitted for this lifecycle-focused doc.)
- Under `option_anchors_zero_fee_htlc_tx` / `option_anchor_outputs`, two additional 330-sat anchor outputs appear — one paying A's funding key, one paying B's — to support fee-bumping via CPFP without requiring the commitment tx itself to commit to a fee rate that may become inadequate by the time it's published.

**B's local commitment** is the structural mirror: B's funds sit behind the revocable+CSV-delayed script, A's funds are immediate.

This asymmetry — _I am delayed and revocable, you are immediate_ — is what permits unilateral close. When A broadcasts A's commitment, A is the one whose funds are held hostage by the `to_self_delay`, giving B time to publish a revocation if A cheated. B has no such delay because B is not the one choosing to broadcast.

### 3.4 Confirmation and "locking in"

After `minimum_depth` confirmations (typically 3–6; the receiving side proposes the value, balancing reorg risk against time-to-usable), both peers send `channel_ready` (formerly `funding_locked`), and the channel is operational. The current state is commitment number 0, with `per_commitment_point` exchanged during channel open ready for use as the **next** state's revocation target.

---

## 4. Updating the channel

### 4.1 The state machine

State updates proceed through a strict four-message protocol per change, ensuring that at no point does either party hold a binding new state without simultaneously holding the revocation for the old one. The key insight: a new commitment is only "safe" once the previous one has been revoked.

For a balance change initiated by A:

```
1. A → B : update_add_htlc / update_fee / update_fulfill_htlc / ...      (proposed change)
2. A → B : commitment_signed   (A's signature on B's new commitment tx)
3. B → A : revoke_and_ack       (B reveals per_commitment_secret_{n-1},
                                  giving B's next per_commitment_point)
4. B → A : commitment_signed   (B's signature on A's new commitment tx)
5. A → B : revoke_and_ack       (A reveals per_commitment_secret_{n-1},
                                  giving A's next per_commitment_point)
```

After step 2, B holds a fully-valid new commitment but A is still entitled to broadcast the old one (the new one isn't binding on A yet — A doesn't have B's signature on A's new commitment). After step 3, A has received B's revocation secret for the old commitment, so if B now publishes its old commitment, A can sweep all of B's funds. From this moment forward, B is committed to the new state. Steps 4 and 5 mirror the same dance for A.

There is a brief asymmetric window between steps 2 and 4 in which the two parties are at different "heights" — B has committed to state `n` while A is still on state `n-1`. The protocol tolerates this because each side's commitment is internally consistent and each side's published-state risk is bounded by what they themselves signed.

### 4.2 What "revocation" actually is

When B sends `revoke_and_ack`, B is doing two things:

1. **Disclosing `per_commitment_secret_{n-1}`** — the scalar whose corresponding point was baked into the `revocationpubkey` of B's now-previous local commitment. With this scalar in hand, A can construct the private key for `revocationpubkey_{n-1}` (the construction uses both B's `revocation_basepoint_secret`, which only B knows, and A's now-disclosed `per_commitment_secret_{n-1}` — but wait, that's backwards from §2).
    
    Let me restate precisely, because this is the easiest place to get the direction confused: in B's local commitment, the **revocation key in B's `to_local` output is constructed from A's `revocation_basepoint` and B's `per_commitment_point`**. To produce a signature on that key, one needs A's `revocation_basepoint_secret` (which A always has) **plus** B's `per_commitment_secret` (which only B knows — until B reveals it during revocation). So when B reveals `per_commitment_secret_{n-1}`, A — and only A — gains the ability to sign for the revocation path on B's old commitment.
    
2. **Publishing the next `per_commitment_point_{n+1}`**, so that A can construct subsequent commitments that target the new revocation key.
    

The revealed secret is stored in a compact derivation tree (BOLT #3 appendix on "per-commitment secret requirements"). Storing all revoked secrets naively would cost 32 bytes × 2^48 commitments. The tree lets a holder remember only ~49 hashes regardless of how many revocations have occurred, while still being able to reconstruct any individual past secret on demand if the counterparty publishes the corresponding old commitment.

### 4.3 Fee updates

The commitment transaction must allocate a fee for its own confirmation should it ever be broadcast. Pre-anchors, this was a thorny problem: the fee was baked into the commitment at signing time, and if mempool conditions diverged from the signed rate, the tx might be unconfirmable. `update_fee` allows the channel funder (originally A) to propose a new feerate, which is then folded into the next commitment via the standard four-message dance.

`option_anchors_zero_fee_htlc_tx` (currently the standard for new channels) leaves the commitment transaction itself paying a (potentially stale) fee but adds the two anchor outputs so either party can CPFP-bump it to a current feerate. Separately — and this is what the "zero fee HTLC tx" in the option's name refers to — the second-stage HTLC-success and HTLC-timeout transactions are signed with `SIGHASH_SINGLE | SIGHASH_ANYONECANPAY` and zero fee, allowing the publisher to add their own input/output to fee-bump at publish time. Together these decouple liveness from the original signing-time feerate prediction — a substantial robustness improvement, and the reason this option is now near-universally negotiated.

### 4.4 The obfuscated commitment number

Every commitment transaction encodes its commitment number in the upper 24 bits of `nSequence` (input) and the lower 24 bits of `nLocktime`, XOR-masked with a per-channel obfuscation key derived from the two `payment_basepoints`. Why bother? So an outside observer who sees a commitment transaction land on-chain cannot trivially tell which state was published; without this, a watcher could detect when an old commitment was being broadcast (since the obfuscated commitment number would be smaller than the current one) and front-run the legitimate counterparty's revocation. Obfuscation forces an attacker to also know the channel's basepoints, which are not publicly broadcast.

---

## 5. Closing the channel

There are exactly two closure modes: **mutual (cooperative)** and **unilateral (force) close**.

### 5.1 Mutual close

When both parties are online and agreeable, mutual close is the cheap, clean exit. It produces a single on-chain transaction with no time-locked outputs and no contestation period — the funds are immediately spendable.

```
A → B : shutdown    (channel_id, scriptpubkey_A_wants_settlement_to)
B → A : shutdown    (channel_id, scriptpubkey_B_wants_settlement_to)
```

After exchanging `shutdown`, no new HTLCs may be added; both sides drain in-flight HTLCs (settling or failing each) and wait until the commitment has no pending updates. Then:

```
A → B : closing_signed   (proposed_fee_satoshis, signature)
B → A : closing_signed   (counter-proposal or same fee, signature)
... possibly several rounds ...
```

The negotiated `closing_tx` is a single 2-of-2-spending transaction with two outputs (or one, if a side has below-dust balance), paying each party their current balance to their nominated `scriptPubKey`. Once both signatures match on the same fee, either party broadcasts. There is no `to_self_delay` and no revocation key — the transaction is final the moment it confirms.

Under `option_simple_close` (a more recent simplification), the negotiation is reduced: each party simply signs its own paying-out version of the close, and either party can combine the signatures into a settled tx. This sidesteps the iterated fee haggling that the original `closing_signed` round-trip required.

### 5.2 Unilateral (force) close

If one party goes offline, becomes unresponsive, or actively misbehaves, the other can force-close by broadcasting its **latest local commitment transaction** to the Bitcoin network.

The published commitment carries the asymmetry described in §3.3:

- The broadcaster's own outputs (`to_local`, and any HTLC outputs they're entitled to) are locked behind `to_self_delay` (`OP_CHECKSEQUENCEVERIFY`). They cannot sweep these for, say, 144 blocks (~1 day) — the standard window during which the counterparty can publish a revocation if the broadcaster cheated.
- The counterparty's `to_remote` output is spendable immediately (or after the trivial 1-block CSV under `option_anchors`). They do not need to wait.

If the broadcast commitment was the latest agreed state, the contestation window passes without incident and the broadcaster sweeps with a second on-chain tx after `to_self_delay` blocks.

If the broadcast commitment was an **old, revoked** state — i.e., the broadcaster is attempting to roll back the channel to a balance more favorable to them — the counterparty (who holds the revocation secret for that old state, having received it in `revoke_and_ack` at the time it was superseded) constructs and broadcasts a **penalty transaction** (also called a "justice transaction") spending the cheater's `to_local` output via the revocation path:

```
witness for to_local script:
  <revocation_signature> <revocationpubkey> <empty_for_OP_IF_true>
```

The penalty tx sweeps **the entire `to_local` balance to the honest party**. This is the "all-or-nothing" punishment: any deviation from the latest state forfeits the cheater's full channel balance, not merely the disputed delta. Game-theoretically, this is what makes cheating uniformly unprofitable.

The penalty must land within `to_self_delay` blocks of the broadcast commitment confirming. If the honest party is offline for that entire window, the cheater wins. This motivates **watchtowers** (BOLT #13-track / Eltoo separate, plus various out-of-spec implementations like LND's lnd-watchtower and Eclair's): third parties paid to monitor the chain and broadcast a pre-signed penalty on the user's behalf without learning channel contents (modern designs use encrypted blobs keyed by the commitment txid prefix).

### 5.3 Resolving HTLCs across a unilateral close

When a force close happens with HTLCs in flight, additional second-stage transactions come into play. Each HTLC output is itself a script with three spending paths (timeout, success, revocation), and resolving them on-chain requires either an `htlc_timeout_tx` or `htlc_success_tx` (pre-signed at commitment time under `option_anchors_zero_fee_htlc_tx`, so they can be fee-bumped via SIGHASH_SINGLE|ANYONECANPAY plus CPFP from the anchors).

Each second-stage HTLC tx itself produces an output locked behind `to_self_delay` and the revocation key, so the cascading revocation logic extends to in-flight payments as well. The full HTLC dance is large enough to deserve its own document; the relevant point for channel lifecycle is that **closure does not become final until every HTLC has resolved**, which can extend the practical close window significantly beyond `to_self_delay` if there are many or long-CLTV-locked HTLCs in flight.

---

## 6. The revocation key tree

Storage of revoked per-commitment secrets is a non-trivial engineering problem at scale. A channel may host millions of state updates over its lifetime; storing 32 bytes for each is unbounded.

BOLT #3 specifies a deterministic key tree exploiting the structure of commitment-number indexing. Let `I` be the commitment number (counting from 2^48 - 1 downward, for reasons of subtree alignment). Given a "seed" secret, a function `generate_from_seed(seed, I)` produces `per_commitment_secret_I` by repeatedly hashing along the bit positions that differ from a parent node. The crucial structural property: **the secret for any commitment `I` can be derived from the secret of any ancestor in the tree, but not vice versa**.

This means a channel can publish secrets in monotonically-decreasing index order, and the recipient need only store the secret at each "frontier" position (at most ~48 of them, one per bit position of the index space). Any past secret can be regenerated on demand by walking down from the appropriate ancestor.

The practical effect: each party stores ~49 × 32 bytes = ~1.5 KB regardless of channel lifetime, while retaining the ability to construct a penalty for any old commitment the counterparty might publish. Without this trick, watchtowers and long-lived channels would be storage-quadratic disasters.

---

## 7. Failure modes specific to closure

A few subtleties bite implementers and operators:

- **Stale-state broadcast after restoration from backup.** If a node restores from a backup that doesn't reflect the latest state, it may inadvertently broadcast a revoked commitment, triggering its own punishment. BOLT #2's `option_data_loss_protect` (and the stronger `option_static_remotekey` and the SCB / Static Channel Backup discipline) mitigate this by having peers reveal, on reconnect, enough information for the lagging side to **avoid** broadcasting (typically by handing over the channel to the counterparty's mercy via cooperative close, accepting loss of in-flight HTLCs but not full balance).
    
- **Fee starvation of the commitment tx.** Under pre-anchor channels, a commitment signed during a low-fee regime may be unconfirmable in a high-fee regime. With no `to_self_delay` mechanism to "buy time," in extreme cases the contestation window can pass without the commitment ever confirming, leaving outputs unspendable. `option_anchors_zero_fee_htlc_tx` solves this by allowing fee-bumping via the two anchor outputs.
    
- **Pinning attacks.** An adversary can broadcast a low-fee transaction that conflicts with a victim's intended sweep, exploiting Bitcoin's mempool replacement rules to prevent the victim from getting their tx confirmed within `to_self_delay`. Mitigations (RBF rule changes, package relay, v3 transactions) are active areas of Bitcoin Core work; in the interim, conservative `to_self_delay` values and short channels-per-counterparty are the operational defenses.
    
- **Force-close fee burden.** Force closure is expensive — one commitment tx, possibly several HTLC second-stage txs, plus the eventual sweep — and the funder typically bears the brunt because the commitment fee is denominated in `to_local` of the funder under the original anchorless rules. With anchors, fees are decoupled and either party can fee-bump, but the on-chain footprint of a unilateral close is still 5–20× larger than a cooperative close. The economic incentive to stay cooperative is real.
    

---

## 8. What changes with Taproot channels (`option_simple_taproot`)

The post-Taproot iteration of channels, finalized over 2023–2024 and rolling out gradually, replaces the funding 2-of-2 with a single MuSig2-aggregated P2TR output, indistinguishable on-chain from any single-key Taproot output. Commitment transactions become smaller and cheaper, and the entire on-chain footprint of a channel becomes plausibly deniable as ordinary single-sig activity. Cooperative closes are particularly improved: they look identical to a routine self-transfer.

The lifecycle protocol itself — open, update, revoke, close — is structurally unchanged. The cryptography shifts from ECDSA over 2-of-2 multisig to Schnorr over MuSig2, and the revocation construction migrates to leverage taproot script paths, but the four-message update dance, the asymmetric commitments, and the revocation-secret economy remain the same.

---

## 9. Mental model

If you remember nothing else from this document, hold onto this:

A Lightning channel is two parties each holding an unfinished Bitcoin transaction that spends a shared 2-of-2 output. The transaction is "unfinished" only in the sense that it's pre-signed but unbroadcast — it's fully valid and could be published unilaterally. Every update replaces these transactions with new pre-signed ones, but only after each party has handed the other a _cryptographic suicide note_ for the previous version — a secret that, if the old version is ever published, lets the counterparty take everything. The blockchain serves not as a settlement layer in the common case, but as a court of last resort whose mere existence makes appeals to it unnecessary.

That is the entire idea. Everything else — HTLCs, multi-hop routing, watchtowers, splicing, Taproot variants — is decoration on this core.

---

## References

- Poon, J. & Dryja, T. (2016). _The Bitcoin Lightning Network: Scalable Off-Chain Instant Payments._ (Original whitepaper, draft 0.5.9.2.)
- BOLT #2 — Peer Protocol for Channel Management. github.com/lightning/bolts/blob/master/02-peer-protocol.md
- BOLT #3 — Bitcoin Transaction and Script Formats. github.com/lightning/bolts/blob/master/03-transactions.md
- BOLT #5 — Recommendations for On-chain Transaction Handling.
- Russell, R. et al. _Lightning Network In-Progress Specifications_, including `option_anchors_zero_fee_htlc_tx` and `option_simple_taproot`.
- Decker, C. & Wattenhofer, R. (2015). _A Fast and Scalable Payment Network with Bitcoin Duplex Micropayment Channels._ (Alternative pre-Poon-Dryja construction; useful for historical context.)
- Decker, C., Russell, R., Osuntokun, O. (2018). _eltoo: A Simple Layer2 Protocol for Bitcoin._ (Proposed simplification of revocation that requires `SIGHASH_NOINPUT`/`ANYPREVOUT`; not yet activated on Bitcoin.)