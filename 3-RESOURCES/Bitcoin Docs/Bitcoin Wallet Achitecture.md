# Bitcoin Wallet Architecture — Curated Study Companion

A chapter-by-chapter guide that takes you from first principles to mastery of how Bitcoin wallets are built. For each chapter you get:

- **Explanation** — what the chapter is about and why it matters.
- **Resources** — curated, technical references ordered roughly beginner → advanced.
- **5 questions** — graded from foundational to expert, to test and deepen mastery.

The canonical primary sources you will see referenced repeatedly:

- **BIPs** (Bitcoin Improvement Proposals) — `github.com/bitcoin/bips`. Especially BIP-32, BIP-39, BIP-43, BIP-44, BIP-49, BIP-84, BIP-86, BIP-141, BIP-340/341/342, BIP-380–386 (descriptors).
- **Mastering Bitcoin, 3rd ed.** by Andreas Antonopoulos & David Harding (free on GitHub: `github.com/bitcoinbook/bitcoinbook`).
- **Programming Bitcoin** by Jimmy Song (`github.com/jimmysong/programmingbitcoin`).
- **learnmeabitcoin.com** by Greg Walker — exceptional visual explanations.
- **Bitcoin Optech** newsletter & topics (`bitcoinops.org`).

---

## 1 — Introduction

### 1.1 — Course Introduction

**Explanation.** This chapter frames the whole journey: a Bitcoin wallet does not "store coins." It stores and manages **keys**, and derives **addresses** that lock outputs on the blockchain. The course builds bottom-up: cryptographic primitives (hashing, elliptic curve signatures) → human-facing secrets (mnemonics, passphrases) → deterministic key trees (BIP-32/39/44) → address and descriptor formats. Understanding this map up front makes every later chapter feel like filling in a known slot rather than learning disconnected facts. The mental model to lock in: **entropy → mnemonic → seed → master key → key tree → addresses**, with hash functions and ECC as the math underneath.

**Resources.**

- _Mastering Bitcoin, 3rd ed._ — Ch. 1 ("What Is Bitcoin?") and Ch. 5 ("Wallet Recovery"/"Keys & Addresses" overview). Best conceptual on-ramp.
- learnmeabitcoin.com — "Bitcoin" beginner guide and the "Technical" section index.
- Bitcoin whitepaper (`bitcoin.org/bitcoin.pdf`) — read once for context on what wallets ultimately interact with.
- Jameson Lopp's "Bitcoin Resources" (`lopp.net/bitcoin-information.html`) — curated index for going deeper on any subtopic.
- Bitcoin Core docs & `bitcoin-cli` reference — to ground theory in a real wallet.

**Questions.**

1. _(Foundational)_ In one sentence, what does a Bitcoin wallet actually store, and what does it explicitly **not** store?
2. _(Core)_ Trace the high-level pipeline from a user's random entropy to a receiving address, naming each intermediate artifact.
3. _(Applied)_ Why can two different wallet applications recover the exact same funds from the same 12 words? What standards make this interoperability possible?
4. _(Analytical)_ "Hot" vs "cold" wallets differ in key handling, not in the cryptography. What is the actual security boundary that distinguishes them?
5. _(Mastery)_ If you had to teach this course in reverse (addresses → entropy), where would the explanation break down, and what does that tell you about the necessary ordering of the dependencies?

---

## 2 — Hash Functions

### 2.1 — Introduction to Hash Functions

**Explanation.** A cryptographic hash maps arbitrary-length input to a fixed-length digest with three defining properties: **preimage resistance** (can't invert), **second-preimage / collision resistance** (can't find two inputs with the same output), and the **avalanche effect** (tiny input change → unpredictable, ~50% output bit flip). In Bitcoin, hashes are everywhere: transaction IDs, Merkle trees, proof-of-work, address encoding (HASH160 = RIPEMD160∘SHA256), and key derivation. This chapter builds the intuition for _why_ these properties make hashes a reliable building block — deterministic yet effectively one-way.

**Resources.**

- _Programming Bitcoin_, Ch. 4 (serialization/hashing context) and helper functions `hash256`, `hash160`.
- learnmeabitcoin.com — "Hash Function (SHA-256)" and "HASH256 / HASH160" pages.
- _Serious Cryptography_ by Jean-Philippe Aumasson — Ch. 6 "Hash Functions" (the best rigorous-but-readable treatment).
- NIST FIPS 180-4 (Secure Hash Standard) — the authoritative spec.
- Khan Academy / Computerphile videos on cryptographic hashing for intuition.

**Questions.**

1. _(Foundational)_ Define preimage resistance, second-preimage resistance, and collision resistance, and give a Bitcoin example that relies on each.
2. _(Core)_ Why does Bitcoin frequently double-hash (e.g., SHA256(SHA256(x)))? What class of attack is this partly intended to mitigate?
3. _(Applied)_ Compute, conceptually, the steps to turn a public key into a HASH160 value. Which two hash functions are composed and in what order?
4. _(Analytical)_ The "birthday bound" says collisions become likely near 2^(n/2) work. For SHA-256, what does that imply about its collision security level, and why is 256-bit output chosen over 128-bit?
5. _(Mastery)_ Explain why collision resistance (not just preimage resistance) matters for transaction IDs and Merkle trees, and describe a concrete failure scenario if the hash were only preimage resistant.

### 2.2 — The Inner Workings of SHA256

**Explanation.** SHA-256 is a Merkle–Damgård construction over a Davies–Meyer-style compression function. The pipeline: **pad** the message (append `0x80`, zero-fill, append the 64-bit length) so it's a multiple of 512 bits; split into 512-bit blocks; expand each block into 64 32-bit words via the message schedule (σ functions); then run 64 rounds mixing eight working registers (a–h) with round constants `K`, the `Ch` and `Maj` functions, and `Σ0/Σ1` rotations; finally add the result back into the running hash state (the feed-forward that makes it one-way). Knowing this internal structure explains both SHA-256's strength and the **length-extension weakness** that motivates HMAC.

**Resources.**

- learnmeabitcoin.com — "SHA-256" step-by-step page (shows padding, schedule, rounds).
- NIST FIPS 180-4 §6.2 — the exact round equations and constants.
- "SHA-256 from scratch" implementation walkthroughs (e.g., in Python/Go on GitHub); building one yourself is the single best learning exercise here.
- _Serious Cryptography_, Ch. 6 — Merkle–Damgård, Davies–Meyer, length extension.
- The interactive "SHA-256 animation" (sha256algorithm.com) — visualizes every round.

**Questions.**

1. _(Foundational)_ Why must SHA-256 pad its input, and what three components make up the padding?
2. _(Core)_ What are the eight working variables and how does the round function use `Ch`, `Maj`, `Σ0`, and `Σ1`?
3. _(Applied)_ Describe the message schedule: how are the 16 input words expanded into 64, and what role do `σ0`/`σ1` play?
4. _(Analytical)_ Where exactly does the "feed-forward" (final modular addition of the pre-block state) occur, and why is it essential to one-wayness?
5. _(Mastery)_ Using the Merkle–Damgård structure, explain precisely how a length-extension attack works against `SHA256(secret ‖ message)`, and why HMAC's nested construction defeats it.

### 2.3 — The Algorithms Used for Derivation

**Explanation.** Two derived constructions built on hashes power wallet key derivation: **HMAC** (a keyed PRF/MAC, `H((K⊕opad)‖H((K⊕ipad)‖m))`) and **PBKDF2** (slow, salted key stretching that runs HMAC `c` times per output block and XORs the results). BIP-39 uses **PBKDF2-HMAC-SHA512** (2048 iterations, salt = "mnemonic"+passphrase) to turn a mnemonic into a 512-bit seed; BIP-32 uses **HMAC-SHA512** to turn that seed into the master key and every child key. This chapter connects the raw hash to its practical wallet roles and explains the security reasoning (PRF behavior, work factor, length-extension resistance).

**Resources.**

- RFC 2104 (HMAC), FIPS 198-1 (HMAC), RFC 2898/PKCS#5 (PBKDF2), RFC 6070 (PBKDF2 test vectors) — primary specs.
- BIP-39 (PBKDF2 usage) and BIP-32 (HMAC-SHA512 usage) — see exact parameters.
- learnmeabitcoin.com — "HMAC-SHA512" and "mnemonic seed" pages.
- _Serious Cryptography_, Ch. 7 "Keyed Hashing" — HMAC's security proof intuition.
- OWASP Password Storage Cheat Sheet — modern guidance on PBKDF2 vs scrypt/Argon2.

**Questions.**

1. _(Foundational)_ Why is naive `H(key ‖ message)` insecure as a MAC, and how does HMAC's two-pad, two-hash design fix it?
2. _(Core)_ In PBKDF2, what is the purpose of the salt and the iteration count, and how are the per-iteration outputs combined?
3. _(Applied)_ State the exact BIP-39 PBKDF2 parameters (PRF, password, salt, iteration count, output length).
4. _(Analytical)_ PBKDF2 is CPU-hard but not memory-hard. What attack hardware does this leave it vulnerable to, and which KDFs address that gap?
5. _(Mastery)_ In BIP-32, HMAC's "key" and "message" roles are assigned opposite to BIP-39's PBKDF2 usage. Explain both assignments and why each makes sense for its security goal.

---

## 3 — Digital Signatures

### 3.1 — Digital Signatures and Elliptic Curves

**Explanation.** Bitcoin's keys live on the elliptic curve **secp256k1**: `y² = x³ + 7` over a large prime field. Points form a group under a geometric "addition" law; the hard problem that secures everything is the **Elliptic Curve Discrete Log Problem (ECDLP)**: given points `G` and `P = k·G`, recovering the scalar `k` is infeasible. A private key is a scalar `k`; the public key is the point `k·G`. Signatures (ECDSA, and since Taproot, Schnorr) prove knowledge of `k` without revealing it. This chapter builds the algebra: point addition, point doubling, scalar multiplication, and the group order `n`.

**Resources.**

- _Programming Bitcoin_, Ch. 1–3 (finite fields, elliptic curves, ECC) — the gold standard hands-on path; you implement secp256k1.
- learnmeabitcoin.com — "Elliptic Curve Cryptography" and "Public Key" pages.
- _Mastering Bitcoin_, Ch. 4 "Keys and Addresses."
- Andrea Corbellini, "Elliptic Curve Cryptography: a gentle introduction" (4-part blog series) — excellent math intuition with diagrams.
- SEC 2 / SEC 1 standards (Certicom) — secp256k1 domain parameters and ECDSA spec.

**Questions.**

1. _(Foundational)_ Write the secp256k1 curve equation and explain what `G` and `n` represent.
2. _(Core)_ Describe geometrically how point addition and point doubling work, and what happens at the point at infinity.
3. _(Applied)_ Why is scalar multiplication `k·G` easy to compute but hard to invert? Name the hard problem.
4. _(Analytical)_ What security level (in bits) does secp256k1 provide, and how does that relate to the 256-bit field and the group order `n`?
5. _(Mastery)_ Why must a private key be in the range `[1, n−1]`? What goes wrong if a value `≥ n` or `0` is used, and where is this checked during BIP-32 derivation?

### 3.2 — Calculating the Public Key from the Private Key

**Explanation.** The public key is `P = k·G`, computed by **scalar multiplication** (efficiently via double-and-add). The result is a curve point `(x, y)`. Bitcoin serializes it either **uncompressed** (`0x04 ‖ x ‖ y`, 65 bytes) or **compressed** (`0x02`/`0x03 ‖ x`, 33 bytes — the prefix encodes `y`'s parity, since `y` is recoverable from `x` via the curve equation). Taproot (BIP-340) uses 32-byte **x-only** public keys. This chapter covers the computation and the serialization formats, including why compressed keys became standard (smaller transactions, same security).

**Resources.**

- _Programming Bitcoin_, Ch. 3 — `S256Point`, `sec()` serialization (compressed & uncompressed).
- learnmeabitcoin.com — "Public Key" page (compressed vs uncompressed visualization).
- BIP-340 §"Public Key Generation" — x-only key encoding for Schnorr/Taproot.
- _Mastering Bitcoin_, Ch. 4 — public key formats.
- secp256k1 library (Bitcoin Core's `libsecp256k1`) — the production implementation.

**Questions.**

1. _(Foundational)_ What is the formula relating a private key to its public key?
2. _(Core)_ Explain the double-and-add algorithm for scalar multiplication and its efficiency vs naive repeated addition.
3. _(Applied)_ How does a 33-byte compressed public key encode the full `(x, y)` point? What do the `0x02` and `0x03` prefixes mean?
4. _(Analytical)_ Given only `x`, how do you recover `y`? Why are there two candidates, and how is the right one selected?
5. _(Mastery)_ Compare uncompressed, compressed, and x-only public keys in terms of size, the information dropped, and the implications for address types and signature schemes (ECDSA vs Schnorr).

### 3.3 — Signing with the Private Key

**Explanation.** ECDSA signing: pick a nonce `k`, compute `R = k·G`, set `r = R.x mod n`, then `s = k⁻¹(z + r·d) mod n` where `z` is the message hash (the sighash) and `d` the private key. The signature is `(r, s)`. Verification recomputes a point from `(r, s)`, `z`, and the public key and checks its x-coordinate equals `r`. The **nonce is critical**: reusing or leaking `k` exposes the private key (the PlayStation 3 / early Bitcoin thefts). BIP-340 Schnorr signing is simpler and linear (`s = k + e·d`), enabling key/signature aggregation. RFC 6979 deterministic nonces remove the randomness risk. Low-`s` (BIP-146) prevents malleability.

**Resources.**

- _Programming Bitcoin_, Ch. 3 — ECDSA signing/verification implemented from scratch.
- BIP-340 — Schnorr signatures for Bitcoin (the modern signing scheme).
- RFC 6979 — deterministic ECDSA nonce generation.
- learnmeabitcoin.com — "Signature (ECDSA)" page.
- _Serious Cryptography_, Ch. 12 "Elliptic Curves" — ECDSA pitfalls and Schnorr.

**Questions.**

1. _(Foundational)_ What are the two components of an ECDSA signature, and what message value `z` is actually signed?
2. _(Core)_ Walk through the signing equations for `r` and `s`. What role does the nonce `k` play?
3. _(Applied)_ Why is nonce reuse catastrophic? Derive how two signatures sharing a nonce leak the private key.
4. _(Analytical)_ How does RFC 6979 deterministic nonce generation eliminate the randomness risk, and why is it preferred over an RNG?
5. _(Mastery)_ Contrast ECDSA and Schnorr (BIP-340): linearity, malleability, batch verification, and what aggregation (MuSig/key-path Taproot spends) becomes possible with Schnorr that ECDSA can't easily do.

### 3.4 — The Sighash Flags

**Explanation.** A signature commits to a specific **digest of the transaction** — but exactly _which parts_ it commits to is controlled by the **sighash flag** appended to the signature. The base types: `SIGHASH_ALL` (sign all inputs and outputs — the default), `SIGHASH_NONE` (sign inputs, no outputs), `SIGHASH_SINGLE` (sign inputs + the one output at the same index), combinable with `SIGHASH_ANYONECANPAY` (sign only this one input). Legacy sighash had quadratic-hashing and malleability issues; **BIP-143** (SegWit v0) redefined the digest algorithm, and **BIP-341** defines Taproot's sighash. These flags enable advanced constructions (crowdfunding, CoinJoin, payment channels).

**Resources.**

- BIP-143 (SegWit v0 sighash), BIP-341 §"Signature validation" (Taproot sighash), and the original legacy sighash description in _Mastering Bitcoin_ Ch. 6.
- learnmeabitcoin.com — "Sighash" page (visual breakdown of each flag).
- _Programming Bitcoin_, Ch. 7–13 — constructing sighash for legacy and SegWit.
- Bitcoin Optech Topics — "SIGHASH flags" and "SIGHASH_ANYPREVOUT" (future).
- Bitcoin Core `script/interpreter.cpp` — reference for digest construction.

**Questions.**

1. _(Foundational)_ What does `SIGHASH_ALL` commit to, and why is it the safe default?
2. _(Core)_ Describe `SIGHASH_NONE`, `SIGHASH_SINGLE`, and `SIGHASH_ANYONECANPAY` and a use case for each.
3. _(Applied)_ What is the `SIGHASH_SINGLE` "bug" / edge case when the input index exceeds the number of outputs, and how is it handled?
4. _(Analytical)_ What problems in legacy sighash (quadratic hashing, third-party malleability) did BIP-143 solve, and how?
5. _(Mastery)_ Explain how Taproot (BIP-341) sighash differs from BIP-143 (e.g., committing to all input amounts and scriptPubKeys), and why that change matters for security and for hardware-wallet fee verification.

---

## 4 — The Mnemonic Phrase

### 4.1 — Evolution of Bitcoin Wallets

**Explanation.** Wallets evolved through distinct generations: **(1) JBOK** ("just a bunch of keys") — random keys with no relationship, requiring constant backups (early Bitcoin Core `wallet.dat`); **(2) deterministic** wallets — all keys from one seed; **(3) hierarchical deterministic (HD)** wallets — BIP-32 trees that allow structured accounts and public-key-only derivation; and **(4) mnemonic-based** seeds (BIP-39) for human-friendly backup. Understanding the pain points each generation solved (backup burden, privacy, account separation, watch-only wallets) motivates every design choice in the modern standards.

**Resources.**

- _Mastering Bitcoin_, Ch. 5 — "Wallet Technology" (Type-0/Type-1/Type-2 wallet taxonomy).
- BIP-32 "Motivation" section — why determinism and hierarchy.
- Electrum documentation — an alternative seed scheme (predates/differs from BIP-39), useful for contrast.
- learnmeabitcoin.com — "HD Wallets" overview.
- Aaron van Wirdum / Bitcoin Magazine history articles on wallet development.

**Questions.**

1. _(Foundational)_ What problem with "JBOK" wallets did deterministic wallets solve?
2. _(Core)_ What does the "hierarchical" in HD wallet add beyond plain determinism?
3. _(Applied)_ How does HD derivation enable a watch-only wallet that can generate receiving addresses without any private key?
4. _(Analytical)_ Why was a human-readable mnemonic (BIP-39) layered on top of BIP-32 rather than backing up the raw seed bytes?
5. _(Mastery)_ Compare Electrum's seed scheme with BIP-39 (checksum approach, versioning, passphrase handling) and discuss the interoperability trade-offs.

### 4.2 — Entropy and Random Numbers

**Explanation.** Everything's security rests on the quality of the initial **entropy**. BIP-39 starts with 128–256 bits of entropy (for 12–24 words). The distinction between **true randomness** (hardware/physical sources) and **pseudo-randomness** (CSPRNGs seeded from the OS entropy pool) matters: a predictable RNG means predictable keys and stolen funds (real incidents: Android `SecureRandom` bug, flawed brainwallets, the "milk sad" Libbitcoin Explorer vulnerability). This chapter covers entropy sources, CSPRNGs, why dice/coin methods are sometimes used, and how entropy maps to mnemonic length.

**Resources.**

- BIP-39 §"Generating the mnemonic" — entropy → mnemonic mapping.
- _Serious Cryptography_, Ch. 2 "Randomness" — CSPRNGs, entropy pools, seeding.
- learnmeabitcoin.com — "mnemonic seed" / entropy section.
- Coldcard / Seedsigner docs on dice-roll entropy — practical air-gapped entropy.
- NIST SP 800-90A/B/C — entropy sources and DRBGs (advanced/authoritative).

**Questions.**

1. _(Foundational)_ How many bits of entropy correspond to a 12-word vs a 24-word BIP-39 mnemonic?
2. _(Core)_ Distinguish true randomness from a CSPRNG. Why is a well-seeded CSPRNG acceptable for key generation?
3. _(Applied)_ Describe a safe procedure to generate entropy with dice, and how to map it into BIP-39 entropy.
4. _(Analytical)_ Pick a historical RNG failure (e.g., Android `SecureRandom`, "milk sad") and explain the root cause and the consequence.
5. _(Mastery)_ How would you test/audit a wallet's entropy source? Discuss statistical tests, the limits of black-box testing, and why "looks random" is insufficient.

### 4.3 — The Mnemonic Phrase

**Explanation.** BIP-39 converts entropy to words: take `ENT` bits of entropy, append a checksum of the first `ENT/32` bits of `SHA256(entropy)`, split the `ENT+CS` bits into 11-bit groups, and map each group to a word in the **2048-word wordlist**. The checksum lets wallets detect typos. The wordlist is carefully designed (first 4 letters unique, no similar words, multiple languages). The phrase is _not_ the seed — it's an encoding of entropy plus checksum, later stretched by PBKDF2. This chapter covers the exact encoding, checksum validation, and wordlist design rationale.

**Resources.**

- BIP-39 (full spec + wordlists) — read the algorithm and the wordlist criteria.
- learnmeabitcoin.com — "Mnemonic Seed" interactive page (entropy↔words↔checksum).
- Ian Coleman's BIP-39 tool (`iancoleman.io/bip39`, run offline) — visualize the whole pipeline; **never use online for real funds**.
- _Programming Bitcoin_ supplementary / `python-mnemonic` (Trezor) reference library.
- SLIP-39 (Shamir backup) — for contrast on splitting mnemonics.

**Questions.**

1. _(Foundational)_ What three things does a BIP-39 mnemonic encode? (Hint: entropy + checksum, then words.)
2. _(Core)_ For 128-bit entropy, how many checksum bits are added and how many words result? Show the arithmetic.
3. _(Applied)_ How is the checksum computed and validated? What happens if one word is wrong?
4. _(Analytical)_ Why 2048 words and 11 bits per word? How does the wordlist's design (unique prefixes) help error correction and usability?
5. _(Mastery)_ The last word of a mnemonic is partly constrained by the checksum. Explain why, and how many valid "last words" exist for a given set of preceding words in a 12-word phrase.

### 4.4 — The Passphrase

**Explanation.** BIP-39 allows an optional **passphrase** (the "25th word"), which is concatenated to the salt (`"mnemonic" + passphrase`) inside PBKDF2. Any different passphrase produces a _completely different_ seed and therefore an entirely separate wallet — enabling **plausible deniability / hidden wallets**. There is no checksum on the passphrase: a typo silently yields a valid but empty wallet, and a forgotten passphrase means permanent loss. This chapter covers the mechanics, the security upside (extra factor, deniability), and the operational risks (no recovery, no validation).

**Resources.**

- BIP-39 §"From mnemonic to seed" — passphrase as salt component.
- learnmeabitcoin.com — passphrase explanation within the seed page.
- Trezor / Ledger / Coldcard docs — passphrase ("hidden wallet") UX and warnings.
- Bitcoin Optech & community write-ups on passphrase best practices and risks.
- SLIP-39 vs BIP-39 passphrase comparison (Trezor blog).

**Questions.**

1. _(Foundational)_ Where in the BIP-39 derivation does the passphrase enter, and what is the default salt without it?
2. _(Core)_ Why does changing the passphrase produce a different wallet rather than a variation of the same one?
3. _(Applied)_ What happens if a user mistypes their passphrase? Why is there no error?
4. _(Analytical)_ Explain "plausible deniability" via passphrases and one way the scheme can still leak the existence of a hidden wallet.
5. _(Mastery)_ Given BIP-39's fixed 2048 PBKDF2 iterations and short salt prefix, evaluate the real brute-force resistance of a passphrase, and recommend entropy/length guidelines with justification.

---

## 5 — Creation of Bitcoin Wallets

### 5.1 — Creation of the Seed and Master Key

**Explanation.** The 512-bit BIP-39 seed feeds BIP-32: `I = HMAC-SHA512(key="Bitcoin seed", msg=seed)`. Split `I` into `IL` (left 32 bytes → **master private key** `m`) and `IR` (right 32 bytes → **master chain code**). The chain code is extra entropy that, together with the key, defines an extended key and prevents children from being derivable by anyone who only knows the key. The master public key is `M = m·G`. This single deterministic step is the root of the entire wallet tree.

**Resources.**

- BIP-32 §"Master key generation."
- learnmeabitcoin.com — "Extended Keys" / "mnemonic seed → master key" pages.
- _Mastering Bitcoin_, Ch. 5 — "HD Wallets (BIP-32)" walkthrough.
- _Programming Bitcoin_ (HD wallet appendix / community extensions) and `bip_utils` Python library for hands-on derivation.
- BIP-32 test vectors — verify your implementation byte-for-byte.

**Questions.**

1. _(Foundational)_ What exact HMAC call generates the master key, and what is used as the HMAC key?
2. _(Core)_ How is the 64-byte HMAC output split, and what does each half become?
3. _(Applied)_ What is the chain code's purpose, and why isn't the private key alone sufficient to define an extended key?
4. _(Analytical)_ What check must be performed on `IL`, and what (rarely) happens if it fails the valid-scalar test?
5. _(Mastery)_ Why is the constant string "Bitcoin seed" used as the HMAC key here, and what would be the consequence of two different seed-derivation domains reusing the same constant?

### 5.2 — Extended Keys

**Explanation.** An **extended key** bundles a key with its chain code (and metadata: depth, parent fingerprint, child index, network/version). **xprv** (extended private) can derive both private and public children; **xpub** (extended public) can derive public children only — the basis for watch-only wallets. Serialization (Base58Check, 78 bytes) includes a version prefix that also signals address type by convention (xpub/ypub/zpub for BIP-44/49/84). Sharing an xpub reveals all your addresses and balances (a privacy consideration), but never lets anyone spend.

**Resources.**

- BIP-32 §"Serialization format" and §"Key derivation" (private vs public).
- SLIP-0132 — version-byte registry (xpub/ypub/zpub/Ypub/Zpub etc.).
- learnmeabitcoin.com — "Extended Keys" page (decode an xpub field-by-field).
- _Mastering Bitcoin_, Ch. 5 — extended keys and the xpub/xprv distinction.
- Online (offline-run) xpub decoders / `bip_utils` for parsing the 78-byte structure.

**Questions.**

1. _(Foundational)_ What two core pieces of data does every extended key contain?
2. _(Core)_ What can an xpub do that an xprv can do, and what can it **not** do?
3. _(Applied)_ List the fields in the 78-byte serialized extended key and what each means.
4. _(Analytical)_ Why is sharing an xpub a privacy risk even though it grants no spending ability? What exactly can an observer learn?
5. _(Mastery)_ xpub/ypub/zpub differ only in version bytes (SLIP-0132), yet imply different address types. Critique this convention versus using descriptors, and explain why it can cause cross-wallet import confusion.

### 5.3 — Derivation of Child Key Pairs

**Explanation.** Child key derivation (CKD) uses HMAC-SHA512 with the parent chain code as key. **Normal (non-hardened)** derivation hashes the parent _public_ key + index: it allows public derivation (xpub → child xpub) but has a vulnerability — if a child private key and the parent xpub leak together, the parent private key is exposed. **Hardened** derivation (index ≥ 2³¹, written `i'`) hashes the parent _private_ key instead, breaking that link at the cost of disabling public-only derivation. Child private key = `(IL + parent_priv) mod n`; child public key can be computed as `IL·G + parent_pub`.

**Resources.**

- BIP-32 §"Private/Public parent key → child key" (CKDpriv, CKDpub).
- learnmeabitcoin.com — "Child Key Derivation" page with the hardened/normal split.
- _Mastering Bitcoin_, Ch. 5 — "Hardened derivation" and the xpub-leak attack.
- _Programming Bitcoin_ / `bip_utils` — implement CKDpriv and CKDpub.
- BIP-32 test vectors (including the hardened paths).

**Questions.**

1. _(Foundational)_ What serves as the HMAC key during child derivation?
2. _(Core)_ What is the index threshold for hardened derivation, and how is it notated?
3. _(Applied)_ Show how a child public key can be derived two ways (from child private key, or directly from parent public key) for **normal** derivation.
4. _(Analytical)_ Describe precisely the attack where a leaked child private key + parent xpub reveals the parent private key. Why does hardening prevent it?
5. _(Mastery)_ Given the trade-off, justify the standard practice of hardening the account-level and above nodes but using non-hardened derivation for the external/internal chains and address indices.

### 5.4 — Wallet Structure and Derivation Paths

**Explanation.** BIP-44 defines a 5-level path: `m / purpose' / coin_type' / account' / change / address_index`. **Purpose** encodes the address scheme (44'=legacy P2PKH, 49'=P2SH-wrapped SegWit, 84'=native SegWit bech32, 86'=Taproot). **coin_type** distinguishes chains (0'=Bitcoin, 1'=testnet). **account** allows logical separation. **change** is 0 for receiving (external) and 1 for change (internal). **address_index** increments per address. This standardized structure is why any compliant wallet can recover funds from a seed regardless of which app created it.

**Resources.**

- BIP-43 (purpose field), BIP-44 (multi-account hierarchy), BIP-49, BIP-84, BIP-86.
- SLIP-44 — registered coin_type values.
- learnmeabitcoin.com — "Derivation Paths" page.
- _Mastering Bitcoin_, Ch. 5 — BIP-44 path structure.
- Ian Coleman BIP-39 tool (offline) — experiment with paths and see resulting addresses.

**Questions.**

1. _(Foundational)_ Write out the five BIP-44 path levels in order.
2. _(Core)_ What address type does each purpose value (44', 49', 84', 86') correspond to?
3. _(Applied)_ What do `change = 0` and `change = 1` mean, and why separate them?
4. _(Analytical)_ Why are the first three levels hardened but the last two not? Connect this to chapter 5.3's security trade-off.
5. _(Mastery)_ A user restores a seed in a wallet that defaults to a different purpose (e.g., 84' vs 44'). Explain why their balance appears empty and how to recover it, referencing gap limits and account discovery.

### 5.5 — Output Script Descriptors

**Explanation.** **Descriptors** (BIP-380–386) are a precise, self-documenting language for _exactly_ which scripts/addresses a wallet controls — e.g., `wpkh([fingerprint/84'/0'/0']xpub.../0/*)#checksum`. They specify the script function (`pkh`, `wpkh`, `sh`, `wsh`, `tr`, `multi`, `sortedmulti`), the key origin (fingerprint + path), the key (xpub/xprv), and a derivation wildcard `*`, plus a checksum. Descriptors replace the ambiguous xpub-version convention: they unambiguously encode address type and structure, are the native wallet format in modern Bitcoin Core, and are essential for multisig and watch-only setups.

**Resources.**

- BIP-380 (descriptors general), BIP-381–386 (specific script expressions, incl. `tr`, `multi`, checksum).
- Bitcoin Core docs — `doc/descriptors.md` (the authoritative practical guide).
- learnmeabitcoin.com — "Descriptors" page.
- Bitcoin Optech Topics — "Output script descriptors."
- `bitcoin-cli getdescriptorinfo` / `deriveaddresses` — hands-on practice.

**Questions.**

1. _(Foundational)_ What problem do descriptors solve that bare xpubs don't?
2. _(Core)_ Parse `wpkh([d34db33f/84'/0'/0']xpub6.../0/*)`: identify each component.
3. _(Applied)_ What does the `#checksum` suffix protect against, and how is it used?
4. _(Analytical)_ Compare `multi` vs `sortedmulti` and explain why key ordering matters for deterministic address generation in multisig.
5. _(Mastery)_ Express a Taproot key-path-plus-script-path wallet as a descriptor using `tr(...)`, and explain how the internal key and script tree are represented.

### 5.6 — Receiving Addresses

**Explanation.** An address is a user-friendly encoding of a **scriptPubKey** (the locking script). Types: **P2PKH** (`1...`, Base58Check of HASH160(pubkey)); **P2SH** (`3...`, hash of a script, used for wrapped SegWit and multisig); **P2WPKH/P2WSH** (`bc1q...`, native SegWit, Bech32, witness program v0); **P2TR** (`bc1p...`, Taproot, Bech32m, witness program v1, x-only key). Encoding includes error-detecting checksums (Base58Check's double-SHA256 prefix; Bech32/Bech32m's BCH code). This chapter ties key → script → address, and explains why address formats signal capabilities and fee characteristics.

**Resources.**

- BIP-141 (SegWit), BIP-173 (Bech32), BIP-350 (Bech32m for v1+), BIP-350/341 (Taproot addresses).
- learnmeabitcoin.com — "Address" pages (P2PKH, P2SH, P2WPKH, P2TR) with byte-level breakdowns.
- _Mastering Bitcoin_, Ch. 4 & 7 — address encoding and script types.
- _Programming Bitcoin_, Ch. 8 (P2SH) and the SegWit chapters.
- Bech32 reference implementations (sipa's demo page, run offline).

**Questions.**

1. _(Foundational)_ Match each prefix (`1`, `3`, `bc1q`, `bc1p`) to its address/script type.
2. _(Core)_ How is a P2PKH address constructed from a public key, step by step?
3. _(Applied)_ Why did SegWit move to Bech32, and what advantages (error detection, case-insensitivity, lower fees) does it bring?
4. _(Analytical)_ Why does Taproot use Bech32m instead of Bech32? What flaw in the original Bech32 checksum for v1+ witness programs prompted BIP-350?
5. _(Mastery)_ Trace the full transformation from an x-only Taproot output key to a `bc1p` address, including the witness version, witness program, and Bech32m encoding of the 5-bit groups.

### 5.7 — Address Derivation

**Explanation.** Putting it all together: from the master key, walk the BIP-44/84/86 path to the account's external chain (`.../0/*`), derive sequential child public keys, convert each to its scriptPubKey, and encode as an address. Wallets follow a **gap limit** (default 20 unused addresses) to know when to stop scanning during recovery — exceeding it can make a wallet miss funds. **Account discovery** scans accounts until one is unused. This chapter operationalizes the whole course: deterministic, repeatable address generation and the recovery logic that depends on it.

**Resources.**

- BIP-44 §"Address gap limit" and §"Account discovery."
- learnmeabitcoin.com — full "HD Wallets" walkthrough connecting path → address.
- _Mastering Bitcoin_, Ch. 5 — gap limits and recovery.
- `bip_utils` / Bitcoin Core `deriveaddresses` + `scantxoutset` — derive and scan in practice.
- BIP-32/44 test vectors and a real wallet's debug logs for end-to-end verification.

**Questions.**

1. _(Foundational)_ Starting from an account-level xpub, what path suffix derives the first receiving address?
2. _(Core)_ What is the gap limit, why does it exist, and what is the common default?
3. _(Applied)_ Describe the account discovery algorithm a wallet uses when restoring from a seed.
4. _(Analytical)_ A user received funds at the 25th address but only generated 20. Explain why a default-gap-limit recovery misses it and how to fix it.
5. _(Mastery)_ Design a recovery strategy for a wallet that used non-standard paths and large address gaps. Discuss how descriptors, custom gap limits, and `scantxoutset` combine to guarantee full fund recovery, and the performance trade-offs.

---

## How to use this guide for mastery

Work each chapter in three passes. **First pass:** read the explanation and the beginner resource, answer questions 1–2. **Second pass:** read the primary spec (the BIP) and answer questions 3–4. **Third pass — the real test of mastery:** _implement_ the chapter's concept from scratch (hash, ECC point math, BIP-32 derivation, Bech32 encoding) and verify against the official test vectors, then answer question 5 and explain it to someone else. The single highest-leverage activity across the whole curriculum is building a minimal HD wallet end-to-end in code that reproduces the BIP-32/39 test vectors byte-for-byte.

---

_Primary sources: the Bitcoin BIPs repository (github.com/bitcoin/bips), Mastering Bitcoin 3rd ed., Programming Bitcoin (Jimmy Song), learnmeabitcoin.com, Serious Cryptography (Aumasson), and Bitcoin Optech._