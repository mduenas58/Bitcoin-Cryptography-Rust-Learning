# Cryptographic vs. Non-Cryptographic Hash Functions

### A Technical Treatment Oriented to Bitcoin

---

## 1. Definitions and Common Ground

A **hash function** `H: {0,1}* → {0,1}^n` maps an arbitrary-length input (the _message_ or _preimage_) to a fixed-length output (the _digest_, _hash_, or _image_). Both cryptographic and non-cryptographic families share three baseline properties:

- **Determinism** — `H(x)` always yields the same output for the same input.
- **Fixed output size** — independent of input length (e.g., SHA-256 → 256 bits).
- **Efficiency** — computable in `O(n)` time over the input length.

The divergence is entirely about the **adversarial model**. Non-cryptographic hashes assume inputs are random or benign. Cryptographic hashes assume a computationally bounded _adversary_ is actively trying to break them.

---

## 2. The Security Properties That Separate Them

Cryptographic hash functions must satisfy three formal properties. Let `n` be the digest length in bits.

|Property|Definition|Generic attack cost (ideal function)|
|---|---|---|
|**Preimage resistance**|Given `y`, infeasible to find any `x` with `H(x) = y`|`O(2^n)`|
|**Second-preimage resistance**|Given `x₁`, infeasible to find `x₂ ≠ x₁` with `H(x₂) = H(x₁)`|`O(2^n)`|
|**Collision resistance**|Infeasible to find _any_ pair `x₁ ≠ x₂` with `H(x₁) = H(x₂)`|`O(2^{n/2})` (birthday bound)|

The **birthday bound** is critical: collision resistance only gives you `n/2` bits of security. SHA-256 therefore provides ~128 bits of collision resistance and ~256 bits of preimage resistance. This is why Bitcoin's 256-bit digests target a 128-bit security floor.

Additional properties cryptographic functions are expected to exhibit:

- **Avalanche effect** — flipping one input bit flips ~50% of output bits, with no statistical correlation between input and output deltas.
- **Pseudorandomness** — output is computationally indistinguishable from a uniform random string.
- **No exploitable structure** — no algebraic shortcuts (e.g., `H(a) ⊕ H(b)` reveals nothing about `H(a‖b)`).

Non-cryptographic functions (CRC32, MurmurHash, FNV-1a, CityHash, xxHash, Java's `Object.hashCode`) provide **none** of these guarantees. They optimize for speed and uniform distribution over _non-adversarial_ inputs. CRC32 is even _linear_ — `CRC(a ⊕ b) = CRC(a) ⊕ CRC(b)` — making targeted collisions trivial to construct by hand.

---

## 3. Side-by-Side Comparison

|Dimension|Non-Cryptographic|Cryptographic|
|---|---|---|
|Primary goal|Speed, uniform bucket distribution|Adversarial security|
|Throughput|Multiple GB/s (xxHash ~10+ GB/s)|Slower (SHA-256 ~hundreds MB/s without HW accel)|
|Collision resistance|None (intentional, easy to forge)|`2^{n/2}` work required|
|Preimage resistance|None|`2^n` work required|
|Reversibility|Often partially reversible|Computationally one-way|
|Typical digest size|32–64 bits|256–512 bits|
|Examples|CRC32, MurmurHash3, xxHash, FNV, SipHash*|SHA-256, SHA-3, BLAKE2/3, RIPEMD-160|
|Use cases|Hash tables, checksums, bloom filters, sharding|Signatures, PoW, commitments, integrity vs. attackers|

*SipHash is a keyed PRF — a hardened middle ground used to defend hash tables against algorithmic complexity DoS attacks, but it is not a general collision-resistant hash.

---

## 4. The Bitcoin Hash Stack

Bitcoin relies on **two** cryptographic primitives, almost always used as nested constructions:

- **SHA-256** (FIPS 180-4) — Merkle–Damgård construction over a Davies–Meyer compression function, 64 rounds.
- **RIPEMD-160** — 160-bit digest, used only for address derivation to shorten public-key fingerprints.

Two derived constructions appear everywhere:

```
HASH256(x) = SHA256(SHA256(x))      // "double SHA-256"
HASH160(x) = RIPEMD160(SHA256(x))   // public-key → address fingerprint
```

The double-SHA-256 ("hash256") was Satoshi's choice partly as a hedge against **length-extension attacks**, to which the bare Merkle–Damgård SHA-256 is vulnerable. Given `H(m)` and `len(m)`, an attacker can compute `H(m ‖ padding ‖ m')` without knowing `m`. Wrapping the output in a second SHA-256 pass destroys the exploitable internal-state exposure.

---

## 5. Real Scenarios in Bitcoin

### Scenario A — Proof of Work (preimage-style search)

A miner assembles an 80-byte block header (version, prev-block hash, Merkle root, timestamp, `nBits` target, nonce) and searches for a nonce such that:

```
HASH256(block_header) ≤ target
```

interpreted as a 256-bit little-endian integer. Because SHA-256 is preimage-resistant and exhibits full avalanche, there is **no strategy better than brute force**: each nonce is an independent Bernoulli trial. This is precisely what makes PoW a fair, unforgeable lottery.

- At a difficulty `D`, expected hashes per block ≈ `D × 2^32`.
- A non-cryptographic hash would be catastrophic here: predictable structure or short digests would let a miner _compute_ a valid nonce algebraically instead of searching, collapsing the security of the entire chain.

When the nonce space (`2^32`) is exhausted, miners mutate the coinbase `extraNonce` (changing the Merkle root) and re-search — relying on the avalanche property so the new search space is effectively independent.

### Scenario B — Merkle Trees (second-preimage & collision resistance)

Each block commits to its transactions via a Merkle root built with double-SHA-256:

```
parent = HASH256(left_child ‖ right_child)
```

This enables **SPV (Simplified Payment Verification)**: a light client verifies a transaction is in a block using an `O(log n)` Merkle proof rather than downloading the full block. Security rests on collision resistance — if an attacker could find two transaction sets hashing to the same root, they could swap transactions undetected.

> **Historical note (CVE-2012-2459):** Bitcoin's Merkle tree duplicates the last hash when a level has an odd number of nodes. This introduced a _second-preimage_ weakness allowing distinct transaction lists to produce identical roots, enabling a block-invalidation DoS. The fix rejects blocks containing duplicate txids at the same tree level. This is a concrete example of how an _implementation detail_ can undermine an otherwise sound cryptographic property.

### Scenario C — Address Derivation (one-wayness as fingerprinting)

A legacy P2PKH address is derived as:

```
pubKeyHash = HASH160(pubKey)              = RIPEMD160(SHA256(pubKey))
address    = Base58Check(0x00 ‖ pubKeyHash)
```

Base58Check appends a 4-byte checksum = first 4 bytes of `HASH256(payload)`. This checksum catches typos — a _non-adversarial_ error-detection role that a cryptographic hash is being used for, but where even a CRC would technically suffice for the typo-catching function alone. The choice of SHA-256 keeps the primitive set minimal.

HASH160 also serves a privacy/efficiency role: the public key stays hidden behind a 160-bit fingerprint until the coins are spent, providing a layer of defense should ECDSA ever be weakened.

### Scenario D — Transaction IDs and Signature Commitments

```
txid = HASH256(serialized_transaction)
```

The txid is a collision-resistant commitment to a transaction's contents. The **transaction malleability** problem (famously implicated in the 2014 Mt. Gox narrative) arose because the txid originally hashed over the _signature_ fields, which could be altered without invalidating the signature — changing the txid without changing the transaction's effect. **SegWit (BIP 141)** resolved this by moving witness data outside the hashed txid serialization. Note this was _not_ a break of SHA-256's collision resistance — it was malleable _input encoding_ feeding a perfectly sound hash.

### Scenario E — Where Bitcoin Uses _Non-Cryptographic_ Hashing

Bitcoin Core internals legitimately use fast, non-cryptographic hashing where no adversary controls a security boundary:

- **`CCoinsMap` / mempool indexing** — in-memory hash maps keyed by txid/outpoint use a cheap hash (`SipHash` seeded with a per-node random key) over the already-cryptographic identifiers. SipHash's keying defends against algorithmic-complexity DoS, not against forgery.
- **Bloom filters (BIP 37)** and **compact block filters (BIP 158, using SipHash)** — probabilistic membership structures where occasional false positives are acceptable and speed dominates.

The design principle: **use cryptographic hashes only at trust boundaries; use fast hashes for everything internal.**

---

## 6. Failure Modes — Why the Distinction Matters

Concrete consequences of using the wrong class of function:

- **MD5 / SHA-1 collisions** — SHA-1 was broken in practice (Google's _SHATTERED_, 2017, ~`2^63` work). Any system using SHA-1 for commitments inherited forgeable signatures. Bitcoin's choice of SHA-256 with a 128-bit collision margin provides substantial headroom.
- **Using CRC32 as a commitment** — its linearity lets an attacker construct collisions in microseconds; a blockchain built on it could be rewritten at will.
- **Length-extension on bare SHA-256** — would allow forging extended messages in naive MAC constructions; sidestepped by double-SHA-256 and (elsewhere) by HMAC/SHA-3.

---

## 7. Decision Heuristic

```
Does an adversary benefit from finding a collision or preimage,
or from controlling/reversing the output?
        │
        ├── YES → Cryptographic hash (SHA-256, SHA-3, BLAKE3)
        │           PoW, Merkle roots, txids, addresses, signatures, commitments
        │
        └── NO  → Non-cryptographic hash (xxHash, SipHash, CRC)
                    hash tables, checksums, bloom filters, sharding, dedup
```

---

## 8. Summary

The line between cryptographic and non-cryptographic hashing is **not speed or output size — it is the assumed adversary.** Bitcoin's security model is built almost entirely on the cryptographic guarantees of SHA-256 (and RIPEMD-160 for addressing): proof of work depends on preimage resistance and avalanche, Merkle trees and txids depend on collision and second-preimage resistance, and double-hashing constructions defend against structural weaknesses like length extension. Where no adversary controls the boundary — internal indexing, filtering, dedup — Bitcoin deliberately drops to fast non-cryptographic hashing. Choosing correctly between the two is a load-bearing architectural decision, and the historical incidents (CVE-2012-2459, malleability/SegWit, SHA-1's deprecation) are reminders that subtle misuse of the _right_ primitive is as dangerous as picking the wrong class entirely.