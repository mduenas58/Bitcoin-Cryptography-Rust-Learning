# Key Derivation Algorithms in Bitcoin Wallets: HMAC & PBKDF2

This document explains two cryptographic primitives that sit at the heart of how modern Bitcoin wallets turn a human-friendly secret (a passphrase or a list of mnemonic words) into the cryptographic keys that actually control funds: **HMAC** and **PBKDF2**. It is written to take you from zero knowledge to a complete, implementation-level understanding, and it ties each concept back to where it is actually used in the Bitcoin standards (BIP-32, BIP-39).

---

## Table of Contents

1. [Background: why wallets need derivation algorithms](https://claude.ai/cowork/local_d24c9cb4-66e1-4884-bdeb-ed53ec0ef1f5#1-background)
2. [Cryptographic prerequisites](https://claude.ai/cowork/local_d24c9cb4-66e1-4884-bdeb-ed53ec0ef1f5#2-prerequisites)
3. [HMAC — Hash-based Message Authentication Code](https://claude.ai/cowork/local_d24c9cb4-66e1-4884-bdeb-ed53ec0ef1f5#3-hmac)
    - 3.1 The intuition
    - 3.2 The problem HMAC solves
    - 3.3 The exact construction
    - 3.4 Worked walkthrough
    - 3.5 Security properties
    - 3.6 HMAC in Bitcoin (BIP-32)
    - 3.7 Reference implementation
4. [PBKDF2 — Password-Based Key Derivation Function 2](https://claude.ai/cowork/local_d24c9cb4-66e1-4884-bdeb-ed53ec0ef1f5#4-pbkdf2)
    - 4.1 The intuition
    - 4.2 The problem PBKDF2 solves
    - 4.3 The exact construction
    - 4.4 Worked walkthrough
    - 4.5 Security properties and limitations
    - 4.6 PBKDF2 in Bitcoin (BIP-39)
    - 4.7 Reference implementation
5. [How the two fit together in a real wallet](https://claude.ai/cowork/local_d24c9cb4-66e1-4884-bdeb-ed53ec0ef1f5#5-together)
6. [Glossary](https://claude.ai/cowork/local_d24c9cb4-66e1-4884-bdeb-ed53ec0ef1f5#6-glossary)

---

<a name="1-background"></a>

## 1. Background: why wallets need derivation algorithms

A Bitcoin private key is just a 256-bit number. Whoever knows it can spend the coins. Two practical problems follow from this:

1. **Humans cannot safely store or remember a 256-bit number.** We need a way to represent the secret as something a person can write down or memorise — a list of words (a _mnemonic_) — and then deterministically convert it back into keys.
2. **A wallet needs many keys, not one.** Reusing a single address harms privacy and complicates accounting. Wallets therefore generate whole trees of keys from a single root secret. This is called a _Hierarchical Deterministic_ (HD) wallet.

Both problems are solved with **key derivation**: a deterministic, one-way process that turns a seed secret into keys. The two workhorse algorithms are:

- **PBKDF2**, used by **BIP-39** to turn a mnemonic sentence (+ optional passphrase) into a 512-bit _seed_.
- **HMAC**, used by **BIP-32** to turn that seed into a master key and then into every child key in the tree.

Understanding these two functions means understanding essentially the entire path from "twelve words on a card" to "a key that signs a transaction."

---
<a name="2-prerequisites"></a>
## 2. Cryptographic prerequisites

### Hash functions

A cryptographic hash function `H(x)` takes input of any length and returns a fixed-length output (a _digest_). The properties that matter here:

- **Deterministic** — the same input always yields the same digest.
- **One-way (preimage resistance)** — given a digest, you cannot feasibly find an input that produces it.
- **Collision resistant** — you cannot feasibly find two inputs with the same digest.
- **Avalanche effect** — flipping one input bit changes roughly half the output bits, with no detectable pattern.

Bitcoin uses **SHA-256** (256-bit output) and **SHA-512** (512-bit output) from the SHA-2 family. SHA-512 is the one used inside both BIP-32 and BIP-39.

### Block size vs. output size

Each hash has two relevant sizes:

|Hash|Output (digest) size|Internal block size|
|---|---|---|
|SHA-256|32 bytes|64 bytes|
|SHA-512|64 bytes|128 bytes|

The **block size** is the chunk size the compression function processes internally. HMAC's key-padding logic is defined in terms of the _block size_, not the output size — a detail people frequently get wrong.

### Bitwise XOR

XOR (`⊕`) compares two bits and returns 1 when they differ. It is its own inverse (`a ⊕ b ⊕ b = a`), which is why it appears constantly in cryptographic mixing.

---

<a name="3-hmac"></a>

## 3. HMAC — Hash-based Message Authentication Code

### 3.1 The intuition

HMAC answers a deceptively simple question: _"How do I combine a secret key and a message with a hash function, so that only someone who knows the key could have produced the result?"_

The naive answer — "just hash the key glued to the message," i.e. `H(key ‖ message)` — is **broken** (explained below). HMAC is the carefully designed correct way to do it. Think of it as a keyed fingerprint: the same key and message always produce the same tag, but you can't forge the tag or recover the key from it.

### 3.2 The problem HMAC solves

Two distinct goals:

1. **Authentication / integrity (its original purpose).** A sender and receiver share a secret key. The sender computes `tag = HMAC(key, message)` and sends `(message, tag)`. The receiver recomputes the tag; if it matches, the message is authentic and unmodified. An attacker who doesn't know the key cannot produce a valid tag for a tampered message.
    
2. **Key derivation (how Bitcoin uses it).** HMAC behaves like a _pseudorandom function_ (PRF): for a fixed key, its output is computationally indistinguishable from random, and its 512-bit result can be split into pieces and used as new key material. BIP-32 exploits exactly this.
    

**Why not just `H(key ‖ message)`?** Hash functions in the SHA-2 family use the _Merkle–Damgård_ construction, which makes them vulnerable to a **length-extension attack**. If an attacker knows `H(key ‖ message)` and the length of the secret, they can compute `H(key ‖ message ‖ padding ‖ extra)` for attacker-chosen `extra` — _without knowing the key_. That lets them forge a valid tag for a longer message. HMAC's nested, double-hash structure defeats this.

### 3.3 The exact construction

HMAC is standardised in **RFC 2104** and **FIPS 198-1**. The definition:

```
HMAC(K, m) = H( (K0 ⊕ opad) ‖ H( (K0 ⊕ ipad) ‖ m ) )
```

Where:

- `H` is the underlying hash (SHA-512 in Bitcoin).
- `m` is the message.
- `B` is the hash's **block size** in bytes (128 for SHA-512).
- `K0` is the key, normalised to exactly `B` bytes:
    - If the key is **longer** than `B`, replace it with `H(key)` (then pad).
    - If the key is **shorter** than `B`, right-pad it with zero bytes to length `B`.
    - If it is exactly `B`, use it as is.
- `ipad` = the byte `0x36` repeated `B` times (the "inner pad").
- `opad` = the byte `0x5c` repeated `B` times (the "outer pad").
- `‖` denotes concatenation.

Step by step:

1. Normalise the key to `K0` (length `B`).
2. **Inner hash:** XOR `K0` with `ipad`, prepend to the message, hash it: `inner = H((K0 ⊕ ipad) ‖ m)`.
3. **Outer hash:** XOR `K0` with `opad`, prepend the inner digest, hash again: `HMAC = H((K0 ⊕ opad) ‖ inner)`.

The two different pad constants (`0x36` and `0x5c` differ in 4 bits per byte) ensure the inner and outer keys are effectively different keys, which is essential to the security proof.

### 3.4 Worked walkthrough

Suppose `H = SHA-512` (block size `B = 128`), key `K = "key"`, message `m = "msg"`.

1. `K` is 3 bytes < 128, so `K0` = `"key"` followed by 125 zero bytes.
2. Compute `K0 ⊕ ipad`: every byte XORed with `0x36`. The three key bytes change; the 125 zero bytes become `0x36`.
3. `inner = SHA512( (K0 ⊕ ipad) ‖ "msg" )` → a 64-byte digest.
4. Compute `K0 ⊕ opad`: every byte XORed with `0x5c`.
5. `HMAC = SHA512( (K0 ⊕ opad) ‖ inner )` → the final 64-byte tag.

The result is 64 bytes (512 bits) of output that depends on _every_ bit of both key and message, with no exploitable structure.

### 3.5 Security properties

- **PRF / pseudorandomness.** Under standard assumptions about the compression function, HMAC is a secure pseudorandom function. This is the property key derivation relies on.
- **Length-extension resistant.** The outer hash wraps the inner digest, so an attacker who sees the output cannot extend the internal hash state.
- **Provable security.** HMAC has a security proof (Bellare et al.) reducing its security to reasonable assumptions about the underlying compression function — notably, HMAC can remain a secure MAC even if the hash is only _weakly_ collision resistant. This robustness is why HMAC-SHA1 stayed usable as a MAC long after SHA-1 collisions were found (though SHA-256/512 are preferred today).
- **Constant-time verification.** When _verifying_ a tag, compare using a constant-time equality check to avoid timing side channels.

### 3.6 HMAC in Bitcoin (BIP-32)

BIP-32 defines hierarchical deterministic wallets, and **HMAC-SHA512 is the engine of the entire key tree.** Every derivation produces 64 bytes that are split into two 32-byte halves: the left half becomes (part of) a key, the right half becomes the _chain code_ (extra entropy carried alongside each key).

**Master key generation** — from the BIP-39 seed `S`:

```
I = HMAC-SHA512(key = "Bitcoin seed", message = S)
IL = I[0:32]   # master private key
IR = I[32:64]  # master chain code
```

Notice the _string_ `"Bitcoin seed"` is used as the HMAC key and the seed as the message — HMAC's roles are inverted from the "authenticate a message" framing because here it is purely a PRF.

**Child key derivation (CKD)** — to derive child index `i` from a parent:

- **Normal (non-hardened) child**, `i < 2³¹`:
    
    ```
    I = HMAC-SHA512(key = c_par, message = serP(point(k_par)) ‖ ser32(i))
    ```
    
    (the parent _public_ key bytes are hashed)
    
- **Hardened child**, `i ≥ 2³¹`:
    
    ```
    I = HMAC-SHA512(key = c_par, message = 0x00 ‖ ser256(k_par) ‖ ser32(i))
    ```
    
    (the parent _private_ key bytes are hashed; the `0x00` prefix pads it to 33 bytes)
    

In both cases:

```
IL = I[0:32];  IR = I[32:64]
child_private_key = (IL + k_par) mod n        # n = secp256k1 curve order
child_chain_code  = IR
```

The parent chain code is always the HMAC _key_; this is the secret entropy that prevents anyone from deriving children without it. Hardened derivation feeds the private key into the HMAC so that knowing a parent _public_ key + a child private key cannot expose the parent private key — closing the privacy/security gap that non-hardened derivation leaves open.

So: **PBKDF2 makes the seed once; HMAC-SHA512 then expands it into the whole tree.**

### 3.7 Reference implementation

```python
import hashlib, hmac

# Using the standard library (preferred — audited & constant-time verify helper)
def hmac_sha512(key: bytes, msg: bytes) -> bytes:
    return hmac.new(key, msg, hashlib.sha512).digest()

# BIP-32 master key from a seed
def bip32_master_key(seed: bytes):
    I = hmac_sha512(b"Bitcoin seed", seed)
    return I[:32], I[32:]   # (master private key, master chain code)


# --- HMAC from scratch, to show the construction explicitly ---
def hmac_from_scratch(key: bytes, msg: bytes, hashfunc=hashlib.sha512,
                      block_size=128) -> bytes:
    if len(key) > block_size:
        key = hashfunc(key).digest()
    key = key.ljust(block_size, b"\x00")           # zero-pad to block size
    ipad = bytes(b ^ 0x36 for b in key)
    opad = bytes(b ^ 0x5c for b in key)
    inner = hashfunc(ipad + msg).digest()
    return hashfunc(opad + inner).digest()

assert hmac_from_scratch(b"key", b"msg") == hmac_sha512(b"key", b"msg")
```

> Practical note: in production, always use a vetted library (`hmac` in Python, `crypto.createHmac` in Node, etc.). The from-scratch version is for understanding only.

---
<a name="4-pbkdf2"></a>
## 4. PBKDF2 — Password-Based Key Derivation Function 2

### 4.1 The intuition

People choose weak, low-entropy secrets (passwords, passphrases). An attacker who gets hold of a derived value can _guess_ candidate passwords and check each one. To make that guessing expensive, PBKDF2 deliberately makes the derivation **slow and repeated** — it runs a PRF (HMAC) thousands or millions of times. One legitimate derivation costs you a fraction of a second; a brute-force attacker trying billions of guesses pays that cost billions of times over.

It also mixes in a **salt** so that identical passwords produce different outputs, defeating precomputed lookup ("rainbow") tables.

### 4.2 The problem PBKDF2 solves

PBKDF2 (defined in **RFC 2898 / PKCS #5 v2.0**, with test vectors in RFC 6070) is a **password-based key derivation function**. Its job: turn a low-entropy password + salt into a high-entropy cryptographic key of any requested length, while imposing a tunable computational cost. Three design levers:

1. **Salt** — a non-secret random value mixed with the password, making each derivation unique and breaking precomputation.
2. **Iteration count `c`** — how many times the underlying PRF is applied. Higher = slower = more attack-resistant. This is the "work factor."
3. **Derived key length `dkLen`** — the number of output bytes requested.

### 4.3 The exact construction

PBKDF2 is parameterised by a PRF (almost always HMAC with some hash):

```
DK = PBKDF2(PRF, Password, Salt, c, dkLen)
```

The output of length `dkLen` is assembled from blocks `T_1, T_2, …, T_l` where `l = ceil(dkLen / hLen)` and `hLen` is the PRF output size:

```
DK = T_1 ‖ T_2 ‖ … ‖ T_l   (truncated to dkLen)
```

Each block `T_i` is produced by an iterated XOR chain:

```
T_i = U_1 ⊕ U_2 ⊕ … ⊕ U_c
```

where

```
U_1 = PRF(Password, Salt ‖ INT_32_BE(i))
U_2 = PRF(Password, U_1)
U_3 = PRF(Password, U_2)
...
U_c = PRF(Password, U_{c-1})
```

Reading that carefully:

- For each output block `i`, the **first** PRF call hashes the salt concatenated with the 4-byte big-endian block index `i`.
- Each subsequent `U` feeds the previous PRF output back in (a chain). Because each step depends on the previous one, the `c` iterations **cannot be parallelised within a block** — this is what makes the cost real.
- The `c` intermediate values are **XORed together** to form the block. (XOR, not just "take the last one," so a weakness in any single iteration doesn't dominate.)
- Multiple blocks (`i = 1, 2, …`) are only needed when `dkLen` exceeds the PRF output size.

The **password is the HMAC key** and the **salt/chain value is the HMAC message** — note this is the opposite assignment from BIP-32's master-key use of HMAC.

### 4.4 Worked walkthrough

Say `PRF = HMAC-SHA512` (`hLen = 64` bytes), `dkLen = 64`, `c = 2048`.

1. `l = ceil(64 / 64) = 1`, so we need only block `T_1`.
2. `U_1 = HMAC-SHA512(Password, Salt ‖ 0x00000001)`.
3. `U_2 = HMAC-SHA512(Password, U_1)`.
4. … continue until `U_2048 = HMAC-SHA512(Password, U_2047)`.
5. `T_1 = U_1 ⊕ U_2 ⊕ … ⊕ U_2048`.
6. `DK = T_1` (already 64 bytes, no truncation needed).

That is exactly the BIP-39 computation (see below). 2048 HMAC-SHA512 calls take only milliseconds on a phone but multiply an attacker's per-guess cost 2048-fold.

### 4.5 Security properties and limitations

**Strengths**

- **Salting** defeats rainbow tables and ensures identical passwords diverge.
- **Tunable work factor** lets you raise `c` over the years as hardware speeds up.
- **Standardised, simple, ubiquitous**, with official test vectors (RFC 6070).

**Limitations (important to understand)**

- **PBKDF2 is only CPU-hard, not memory-hard.** It uses negligible memory, so attackers can build massively parallel crackers on **GPUs, FPGAs, and ASICs** that evaluate enormous numbers of guesses cheaply. Newer KDFs — **scrypt**, **bcrypt**, and especially **Argon2** (the Password Hashing Competition winner) — deliberately consume large amounts of memory to neutralise this hardware advantage.
- **Choice of iteration count matters.** RFC guidance and OWASP recommendations have risen over time. For password storage today, OWASP suggests on the order of hundreds of thousands to over a million iterations for PBKDF2-HMAC-SHA256. (BIP-39 uses a _fixed_ 2048 — see the caveat below.)
- **Per-block parallelism for long outputs.** Different output blocks `T_i` are independent, so requesting a very long `dkLen` does not increase per-guess cost proportionally for the attacker.

**Constant-time / side channels** — comparisons of derived keys should be constant-time, as with HMAC.

### 4.6 PBKDF2 in Bitcoin (BIP-39)

**BIP-39** specifies how a mnemonic sentence becomes a binary seed. The mnemonic (generated from entropy + a checksum, mapped to a wordlist) is human-facing; the _seed_ is what feeds BIP-32.

The conversion is **exactly one PBKDF2 call**, with fixed parameters:

```
seed = PBKDF2(
    PRF      = HMAC-SHA512,
    Password = NFKD(mnemonic_sentence),     # the words, UTF-8 NFKD-normalised
    Salt     = NFKD("mnemonic" + passphrase),  # literal "mnemonic" + optional passphrase
    c        = 2048,
    dkLen    = 64 bytes                      # 512-bit seed
)
```

Key details:

- **Iteration count is fixed at 2048.** This is low by modern password-storage standards. The rationale: the mnemonic itself already carries high entropy (128–256 bits), so brute-forcing the _words_ is infeasible regardless of iterations. The 2048 iterations mainly protect the _optional passphrase_ against guessing and keep derivation fast on constrained hardware.
- **The salt is the string `"mnemonic"` concatenated with an optional user passphrase** (the BIP-39 "25th word"). With no passphrase the salt is just `"mnemonic"`. Because the passphrase changes the salt, every passphrase yields a _completely different_ seed and therefore a completely different wallet — the basis for plausible-deniability / hidden wallets.
- **NFKD Unicode normalisation** is applied to both mnemonic and passphrase so that visually identical strings with different byte encodings produce the same seed across implementations.
- The 64-byte output **is the BIP-32 seed `S`** fed into `HMAC-SHA512("Bitcoin seed", S)` from §3.6. This is the precise hand-off point between the two algorithms.

> Security caveat worth stating plainly: because BIP-39 fixes `c = 2048` and uses a short, well-known salt prefix, the _passphrase_ alone is comparatively weak against a determined attacker who already has the mnemonic. Choose a long, high-entropy passphrase if you rely on it.

### 4.7 Reference implementation

```python
import hashlib, unicodedata

# Using the standard library
def bip39_seed(mnemonic: str, passphrase: str = "") -> bytes:
    mnemonic = unicodedata.normalize("NFKD", mnemonic)
    salt = unicodedata.normalize("NFKD", "mnemonic" + passphrase)
    return hashlib.pbkdf2_hmac(
        "sha512",
        mnemonic.encode("utf-8"),
        salt.encode("utf-8"),
        2048,            # iteration count
        dklen=64,        # 512-bit seed
    )


# --- PBKDF2 from scratch, to show the construction explicitly ---
import hmac, struct

def pbkdf2_from_scratch(password: bytes, salt: bytes, c: int, dklen: int,
                        hashfunc=hashlib.sha512) -> bytes:
    hlen = hashfunc().digest_size
    blocks = -(-dklen // hlen)            # ceil division
    out = b""
    for i in range(1, blocks + 1):
        u = hmac.new(password, salt + struct.pack(">I", i), hashfunc).digest()
        t = bytearray(u)
        for _ in range(c - 1):
            u = hmac.new(password, u, hashfunc).digest()
            t = bytearray(a ^ b for a, b in zip(t, u))   # XOR accumulate
        out += bytes(t)
    return out[:dklen]

# Equivalence check against the standard library
pw, salt = b"mnemonic test", b"mnemonicpass"
assert pbkdf2_from_scratch(pw, salt, 2048, 64) == \
       hashlib.pbkdf2_hmac("sha512", pw, salt, 2048, 64)
```

---
<a name="5-together"></a>
## 5. How the two fit together in a real wallet

The full pipeline from words to a spendable key, naming each algorithm:

```
   [ user's 12/24 words ]  +  [ optional passphrase ]
                │
                │   BIP-39:  PBKDF2-HMAC-SHA512, salt = "mnemonic"+passphrase, 2048 iters
                ▼
        [ 512-bit seed S ]
                │
                │   BIP-32:  HMAC-SHA512(key="Bitcoin seed", msg=S)
                ▼
   [ master private key kₘ ‖ master chain code cₘ ]
                │
                │   BIP-32 CKD:  repeated HMAC-SHA512(key=chain code, msg=...)
                ▼
   [ child keys → grandchild keys → … the whole HD tree ]
                │
                ▼
        [ address-level private key → ECDSA/Schnorr signs a transaction ]
```

Two observations that tie everything together:

1. **HMAC-SHA512 is the shared primitive.** PBKDF2 is _built on top of_ HMAC — it is literally thousands of HMAC calls in an XOR chain. So in a real wallet, HMAC-SHA512 is the single cryptographic engine doing nearly all the derivation work; PBKDF2 and BIP-32 are two different _ways of orchestrating_ it.
    
2. **Each algorithm targets a different threat.**
    
    - PBKDF2/BIP-39 defends a potentially _low-entropy_ secret (the passphrase) against brute force by being deliberately slow.
    - HMAC/BIP-32 expands an _already high-entropy_ secret into many keys quickly, while keeping the tree structure secure (chain codes, hardened derivation).

---
<a name="6-glossary"></a>
## 6. Glossary

- **BIP-32** — Bitcoin Improvement Proposal defining Hierarchical Deterministic wallets and child key derivation via HMAC-SHA512.
- **BIP-39** — BIP defining mnemonic phrases and their conversion to a seed via PBKDF2-HMAC-SHA512.
- **Chain code** — 32 bytes of extra entropy carried with each BIP-32 key, used as the HMAC key when deriving children.
- **Derived key (DK)** — the final output of PBKDF2.
- **Hardened derivation** — BIP-32 child derivation (index ≥ 2³¹) that feeds the parent private key into HMAC, preventing parent-key exposure.
- **HMAC** — keyed hash construction `H((K⊕opad) ‖ H((K⊕ipad) ‖ m))`; a secure PRF and message authentication code.
- **Iteration count (c)** — number of PRF applications in PBKDF2; the tunable work factor.
- **Merkle–Damgård** — the iterated construction underlying SHA-2, source of the length-extension weakness HMAC guards against.
- **Mnemonic** — human-readable list of words encoding wallet entropy (BIP-39).
- **NFKD** — Unicode normalisation form applied to BIP-39 strings for cross-impl consistency.
- **PBKDF2** — Password-Based Key Derivation Function 2; slow, salted key stretching built from a PRF.
- **PRF (Pseudorandom Function)** — a function whose outputs are indistinguishable from random to anyone without the key; HMAC qualifies.
- **Salt** — non-secret value mixed into a KDF to make outputs unique and defeat precomputation.
- **Seed** — the 512-bit master secret output by BIP-39 and consumed by BIP-32.
- **secp256k1** — the elliptic curve Bitcoin uses; `n` is its group order, used to reduce derived private keys.

---

_References: RFC 2104 (HMAC), FIPS 198-1 (HMAC), RFC 2898 / PKCS #5 v2.0 (PBKDF2), RFC 6070 (PBKDF2 test vectors), BIP-32, BIP-39._