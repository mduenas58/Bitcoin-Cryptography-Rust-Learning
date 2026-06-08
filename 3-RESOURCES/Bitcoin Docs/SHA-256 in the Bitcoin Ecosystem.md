# SHA-256 in the Bitcoin Ecosystem

### Every Instance, Enumerated, with Examples

---

## 0. The Two Canonical Constructions

Almost all Bitcoin usage wraps SHA-256 in one of two forms. Memorize these; the rest of the document references them constantly.

```
SHA256(x)                              // single pass, FIPS 180-4
HASH256(x) = SHA256(SHA256(x))         // "double SHA-256" / dSHA256 / Hash256
HASH160(x) = RIPEMD160(SHA256(x))      // SHA-256 then RIPEMD-160
```

`HASH256` is the workhorse. Satoshi used the double pass primarily to neutralize **length-extension attacks** intrinsic to SHA-256's Merkle–Damgård structure.

---

## 1. Proof of Work — Block Header Hashing

**Construction:** `HASH256(block_header)`, output read as a little-endian 256-bit integer.

The 80-byte header: `version (4) ‖ prevBlockHash (32) ‖ merkleRoot (32) ‖ time (4) ‖ nBits (4) ‖ nonce (4)`.

```
block_hash = HASH256(header)   must satisfy   block_hash ≤ target(nBits)
```

**Example (Genesis block, height 0):**

```
header hash = 000000000019d6689c085ae165831e93
              4ff763ae46a2a6c172b3f1b60a8ce26f
```

The leading zero bytes are the visible signature of a hash below target. Miners iterate the `nonce` (and, once `2^32` is exhausted, the coinbase `extraNonce`, which changes the Merkle root) until the inequality holds.

---

## 2. Block Identity (Block Hash)

**Construction:** `HASH256(block_header)` — _identical computation to PoW._

A block's "hash"/ID is just its PoW result. There is no separate block-ID hash. The `prevBlockHash` field chains each block to its parent, which is what makes tampering with history require redoing all subsequent PoW.

```
prevBlockHash(block N+1) == HASH256(header(block N))
```

---

## 3. Transaction IDs (txid)

**Construction:** `HASH256(legacy_serialized_tx)`, displayed byte-reversed (big-endian).

```
txid = HASH256(nVersion ‖ inputs ‖ outputs ‖ nLockTime)
```

**Example (Genesis coinbase tx):**

```
txid = 4a5e1e4baab89f3a32518a88c31bc87f
       618f76673e2cc77ab2127b7afdeda33b
```

For **SegWit** transactions the legacy txid _excludes_ witness data — this is the malleability fix from BIP 141.

---

## 4. Witness Transaction IDs (wtxid)

**Construction:** `HASH256(full_tx_including_witness)`.

Introduced by SegWit (BIP 141). The wtxid commits to signatures/witness data, while the txid does not.

```
wtxid = HASH256(nVersion ‖ marker ‖ flag ‖ inputs ‖ outputs ‖ witness ‖ nLockTime)
```

The coinbase wtxid is defined as all-zeros by convention.

---

## 5. Merkle Root (Transaction Merkle Tree)

**Construction:** pairwise `HASH256(left ‖ right)` up the tree.

```
parent = HASH256(child_L ‖ child_R)
```

Leaves are txids. Odd nodes at a level duplicate the last hash (the source of CVE-2012-2459). The root goes into the block header, and SPV proofs (`O(log n)`) rely on it.

---

## 6. Witness Commitment (SegWit)

**Construction:** `HASH256` Merkle root over **wtxids**, then committed inside the coinbase.

```
witness_root        = merkle_root_over_wtxids        (HASH256 internally)
witness_commitment  = HASH256(witness_root ‖ witness_reserved_value)
```

Stored in a coinbase output prefixed with `0x6a24aa21a9ed`. This is how SegWit data is bound to the block without changing the legacy header/Merkle structure.

---

## 7. Address Derivation — P2PKH (Legacy)

**Construction:** `HASH160` (= SHA-256 then RIPEMD-160), wrapped in Base58Check.

```
pubKeyHash = HASH160(pubKey) = RIPEMD160(SHA256(pubKey))
address    = Base58Check(0x00 ‖ pubKeyHash)
```

**Example:** `1A1zP1eP5QGefi2DMPTfTL5SLmv7DivfNa` (Satoshi's genesis reward address).

---

## 8. Address Derivation — P2SH

**Construction:** `HASH160(redeemScript)`.

```
scriptHash = HASH160(redeemScript)
address    = Base58Check(0x05 ‖ scriptHash)
```

**Example:** addresses starting with `3...`, e.g. `3J98t1WpEZ73CNmQviecrnyiWrnqRhWNLy`. Used for multisig and (legacy-wrapped) SegWit.

---

## 9. Base58Check Checksum

**Construction:** first 4 bytes of `HASH256(payload)`.

```
checksum = HASH256(version ‖ payload)[0:4]
encoded  = Base58(version ‖ payload ‖ checksum)
```

Catches typos and transcription errors across all Base58 addresses, WIF private keys, and extended keys.

---

## 10. Native SegWit / Taproot Addresses (Bech32) — the exception

**Construction:** For **P2WPKH** the program is `HASH160(pubKey)` (still SHA-256 inside). For **P2WSH** the program is a **single** `SHA256(witnessScript)` — _not_ double, _not_ RIPEMD.

```
P2WPKH program = HASH160(pubKey)        → bc1q...  (20 bytes)
P2WSH  program = SHA256(witnessScript)  → bc1q...  (32 bytes)
```

Note: Bech32/Bech32m's own checksum uses a **BCH code**, _not_ SHA-256. Taproot (P2TR) keys use tagged hashes (next item).

---

## 11. Legacy Signature Hash (SIGHASH, pre-SegWit)

**Construction:** `HASH256(modified_tx ‖ sighash_type)` — the message ECDSA signs.

```
sighash = HASH256(serialize(tx, input_index, script, sighash_flag))
```

SIGHASH flags (`ALL`, `NONE`, `SINGLE`, `ANYONECANPAY`) control which parts of the tx are committed.

---

## 12. SegWit Signature Hash (BIP 143)

**Construction:** a redesigned `HASH256` over precomputed sub-hashes, fixing quadratic hashing.

```
hashPrevouts = HASH256(all input outpoints)
hashSequence = HASH256(all nSequence)
hashOutputs  = HASH256(all outputs)
sighash      = HASH256(nVersion ‖ hashPrevouts ‖ hashSequence ‖ outpoint
                       ‖ scriptCode ‖ amount ‖ nSequence ‖ hashOutputs
                       ‖ nLockTime ‖ sighash_type)
```

Reduces per-input signing from `O(n²)` to `O(n)` hashing work.

---

## 13. Taproot Tagged Hashes (BIP 340/341/342)

**Construction:** `SHA256(SHA256(tag) ‖ SHA256(tag) ‖ x)` — single SHA-256 with domain separation.

```
tagged_hash(tag, x) = SHA256( SHA256(tag) ‖ SHA256(tag) ‖ x )
```

Used throughout Taproot: `TapLeaf`, `TapBranch`, `TapTweak`, `TapSighash`, and BIP-340 Schnorr challenge/nonce derivation. Prefixing the doubled tag hash provides cheap, collision-safe domain separation (and incidentally also blocks length extension).

---

## 14. BIP-32 HD Wallets — Key Derivation

**Construction:** `HMAC-SHA512` for child keys, but `HASH160` for the **key fingerprint**.

```
fingerprint = HASH160(parent_pubKey)[0:4]
```

(The chain-code/child math uses SHA-512, not SHA-256, but the identifier fingerprint is SHA-256-based.)

---

## 15. Mining Share / Pool Validation

**Construction:** same `HASH256(header)` as §1, checked against an easier _share_ target.

Pools verify miner-submitted shares by recomputing `HASH256` of the candidate header. Stratum splits the coinbase so miners roll `extraNonce`, recompute the §5 Merkle root, then re-hash the header.

---

## 16. Compact Block Filters (BIP 158) — _NOT_ SHA-256

Listed for contrast: BIP 158 uses **SipHash**, a fast non-cryptographic keyed hash, _not_ SHA-256 — because filter membership is not an adversarial trust boundary.

---

## Summary Table

|#|Use|Construction|Double?|
|---|---|---|---|
|1|Proof of Work|`HASH256(header)`|✔|
|2|Block identity|`HASH256(header)`|✔|
|3|txid|`HASH256(tx_legacy)`|✔|
|4|wtxid|`HASH256(tx_full)`|✔|
|5|Merkle root|`HASH256(L‖R)`|✔|
|6|Witness commitment|`HASH256(root‖reserved)`|✔|
|7|P2PKH address|`HASH160(pubKey)`|single SHA + RIPEMD|
|8|P2SH address|`HASH160(script)`|single SHA + RIPEMD|
|9|Base58Check checksum|`HASH256(payload)[0:4]`|✔|
|10|P2WSH program|`SHA256(script)`|single|
|11|Legacy SIGHASH|`HASH256(modified_tx)`|✔|
|12|SegWit SIGHASH (BIP143)|nested `HASH256`|✔|
|13|Taproot tagged hashes|`SHA256(tag‖tag‖x)`|single|
|14|BIP-32 fingerprint|`HASH160(pubKey)[0:4]`|single SHA + RIPEMD|
|15|Pool share validation|`HASH256(header)`|✔|
|16|BIP-158 filters|SipHash (not SHA-256)|—|

**Pattern:** consensus-critical commitments (PoW, txids, Merkle, sighashes) use **double** SHA-256; address/fingerprinting layers add **RIPEMD-160**; newer protocols (P2WSH, Taproot) deliberately use **single** SHA-256 with explicit domain separation instead of double-hashing.