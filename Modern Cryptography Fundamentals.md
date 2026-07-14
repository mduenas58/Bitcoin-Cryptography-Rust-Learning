# Modern Cryptography Fundamentals — 20-Hour Pareto Plan

**For:** A beginner to both the math and the code, who wants to _understand deeply_ (why the primitives work and what security they give), not just use libraries.

**Shape:** 10 sessions × 2 hours = 20 hours. Each session is ~1h 45m of focused learning + a **15-minute active review** at the end. Theory-first, with light hands-on "feel it" exercises that reinforce understanding rather than turn you into an implementer.

**The Pareto bet:** Roughly 20% of cryptography's ideas explain 80% of everything else. Those ideas are: the _threat-model mindset_, _just-enough modular arithmetic_, _randomness_, _symmetric encryption + modes_, _hash functions_, _authentication (MAC/AEAD)_, _public-key + the two hard problems_, _elliptic curves + signatures_, and _how it all assembles into TLS/PKI_. This plan spends all 20 hours there and deliberately skips the long tail (exotic ciphers, deep proofs, niche protocols).

---

## How to use this plan

- **Don't passively watch.** After every concept, close the tab and explain it out loud in one sentence. If you can't, rewatch that piece.
- **Keep a one-page "crypto cheat sheet"** as you go. Add one line per primitive: _what it provides, what breaks it, when to use it._ By Session 10 this page IS your mental model.
- **The 15-minute review is non-negotiable.** It's where learning gets consolidated. Format below.
- **Golden rule to internalize from day one:** _Never roll your own crypto._ The goal here is to understand the tools well enough to use vetted libraries correctly and reason about security — not to build production ciphers.

### The 15-minute review format (use every session)

1. **Recall (5 min)** — Without looking, write the 3–5 key terms from today and define each in one line.
2. **Connect (5 min)** — Answer: _What problem did today's primitive solve that yesterday's couldn't?_ Add the link to your cheat sheet.
3. **Flag (5 min)** — Write down the single thing that's still fuzzy. That becomes your first task next session.

---

## Core resources (used throughout)

|Resource|Type|Why it's here|Link|
|---|---|---|---|
|**Crypto 101** (Laurens Van Houtte)|Free book/PDF|The best free, beginner-friendly, from-zero intro. Your spine for the early sessions.|https://www.crypto101.io/|
|**Cryptography I — Dan Boneh (Stanford)**|Free online course|The gold-standard university course. Enroll free ("Full Course, No Certificate"); lectures also free on the course preview page. Use targeted lectures, not the whole firehose.|https://www.coursera.org/learn/crypto|
|**Serious Cryptography, 2nd Ed.** (Aumasson, 2024)|Book (paid)|The single best modern, practical reference. Optional but ideal for going deep on any topic.|https://nostarch.com/serious-cryptography-2nd-edition|
|**Computerphile — cryptography playlist**|Free videos|Short, intuitive explainers (AES, Diffie-Hellman, hashing, TLS). Great for first-contact intuition.|https://www.youtube.com/user/Computerphile|
|**Khan Academy — Journey into Cryptography**|Free course|Gentle, visual on the math foundations (modular arithmetic, primes).|https://www.khanacademy.org/computing/computer-science/cryptography|

> Tip: For each session, do the **primary** resource first (build the model), then dip into a **supplement** only if something is fuzzy. Don't try to consume everything.

---

## Session 1 — The Mindset: What Cryptography Actually Promises

**Goal:** Stop thinking "secret codes," start thinking "security goals under an attacker model." This frame makes every later topic click.

**Pareto concepts**

- The four goals: **confidentiality, integrity, authentication, non-repudiation**.
- **Kerckhoffs's principle:** security lives in the _key_, not the secrecy of the algorithm.
- **Threat / attacker models:** passive eavesdropper vs active tamperer; what "the adversary can do" means.
- Why **"don't roll your own crypto"** is the field's first commandment.
- Vocabulary: plaintext, ciphertext, key, cipher, encode ≠ encrypt.

**Resources**

- Primary: Crypto 101 — Chapters 1–2 (intro & "Exclusive OR").
- Supplement: Computerphile, _"Secret Key Exchange"_ and _"What is Cryptography?"_ style intros.

**Light exercise:** By hand, XOR two short bit strings and back again. Convince yourself XOR is reversible and is the atom of encryption.

**15-min review** (recall / connect / flag).

---

## Session 2 — Just-Enough Math I: Modular Arithmetic & Primes

**Goal:** Get comfortable in "clock arithmetic." This is the language every public-key system speaks.

**Pareto concepts**

- **Modular arithmetic:** `a mod n`, congruence, why everything "wraps around."
- **Primes** and why they matter; coprimality.
- **GCD** and the **Euclidean algorithm**.
- Intuition for **one-way functions:** easy forward, hard backward.

**Resources**

- Primary: Khan Academy — _Journey into Cryptography_ (modular arithmetic, primality, "What is modular arithmetic?").
- Supplement: Crypto 101 — the number-theory preliminaries section.

**Light exercise:** Compute a few `mod` operations and one GCD by hand (e.g., gcd(48, 18)). Watch the remainder shrink to the answer.

**15-min review.**

---

## Session 3 — Just-Enough Math II: Modular Inverses, Groups & the Hard Problems

**Goal:** Understand the _exact_ math trapdoors that public-key crypto rests on — without drowning in proofs.

**Pareto concepts**

- **Modular inverses** and the **Extended Euclidean Algorithm** (the "division" of modular math).
- **Modular exponentiation** is fast; its inverse is the **Discrete Logarithm Problem (DLP)**.
- **Integer factorization** is hard — the other great trapdoor.
- Plain-English statement: _easy one way, infeasible the other_ = the foundation of RSA, Diffie-Hellman, ECC.

**Resources**

- Primary: Boneh _Cryptography I_ — the number theory / public-key intro lectures.
- Supplement: Serious Cryptography Ch. on the math of RSA/ECC (if you have it).

**Light exercise:** Trace why `3^x mod 7` jumps around unpredictably as `x` increases — feel why recovering `x` is hard.

**15-min review.**

---

## Session 4 — Randomness: The Hidden Foundation

**Goal:** See that _every_ key, nonce, and salt is only as strong as the randomness behind it. Bad randomness silently breaks great crypto.

**Pareto concepts**

- **Entropy** and what "random enough" means.
- **PRNG vs CSPRNG** (cryptographically secure) — and why the distinction is life-or-death.
- **Keys, nonces, IVs, salts:** what each is and the cardinal rule _never reuse a nonce_.
- Real-world failures from weak randomness (e.g., predictable keys).

**Resources**

- Primary: Serious Cryptography Ch. 2 ("Randomness") — or Crypto 101's randomness section if using free only.
- Supplement: Computerphile, randomness/entropy videos.

**Light exercise:** List, from memory, every place a real system needs fresh randomness. Compare to a reference.

**15-min review.**

---

## Session 5 — Symmetric Encryption & the Crucial Role of Modes

**Goal:** Understand the workhorse of bulk encryption — and why _how_ you use a block cipher matters as much as the cipher itself.

**Pareto concepts**

- **Symmetric (shared-key) encryption**; **stream vs block ciphers**.
- **AES** at a conceptual level (you don't need the internals).
- **Modes of operation:** why **ECB is broken** (the famous penguin image), and what **CBC** and **CTR** fix.
- The **one-time pad**: perfect secrecy and why it's impractical (key as long as the message).

**Resources**

- Primary: Boneh _Cryptography I_ — Week on block ciphers & modes.
- Supplement: Computerphile, _"AES Explained"_ and the _ECB Penguin_.

**Light exercise:** Look at the ECB-penguin image and write one sentence on _why_ the pattern leaks.

**15-min review.**

---

## Session 6 — Hash Functions & Password Storage

**Goal:** Master the other half of symmetric-world crypto: one-way fingerprints. These power integrity, passwords, blockchains, and signatures.

**Pareto concepts**

- Properties of a **cryptographic hash:** deterministic, fast, **preimage / second-preimage / collision resistance**.
- **SHA-2 / SHA-3** as the standards; why MD5 and SHA-1 are dead.
- **Password storage done right:** salts + slow hashes (**bcrypt, scrypt, Argon2**) — and why plain SHA-256 is _wrong_ for passwords.
- Hashes as building blocks: **Merkle trees**, commitments.

**Resources**

- Primary: Crypto 101 — hash functions chapter.
- Supplement: Computerphile, _"Hashing Algorithms and Security."_

**Light exercise:** Explain in one line why a 1-bit change to the input changes ~half the output bits (the avalanche effect) and why that's desirable.

**15-min review.**

---

## Session 7 — Integrity & Authentication: MACs and Authenticated Encryption

**Goal:** Close the biggest beginner gap: _encryption alone does not stop tampering._ Learn how real systems get confidentiality **and** integrity together.

**Pareto concepts**

- Why **confidentiality ≠ integrity** — an attacker can flip bits in ciphertext.
- **MAC** and **HMAC:** proving a message wasn't altered and came from someone with the key.
- **Authenticated Encryption (AEAD):** **AES-GCM**, ChaCha20-Poly1305 — the modern default.
- **Encrypt-then-MAC** ordering and why it matters.

**Resources**

- Primary: Boneh _Cryptography I_ — MACs & authenticated encryption lectures.
- Supplement: Serious Cryptography Ch. on authenticated encryption.

**Light exercise:** Describe an attack that succeeds against "encryption only" but fails once a MAC is added.

**15-min review.**

---

## Session 8 — Public-Key Crypto: RSA & Diffie-Hellman

**Goal:** The conceptual summit. Solve the problem symmetric crypto can't: _how do two strangers agree on a key over an open wire?_

**Pareto concepts**

- The **key-distribution problem** and the asymmetric breakthrough: **public key encrypts, private key decrypts.**
- **RSA:** built on factoring; how public/private exponents relate (ties back to Sessions 2–3).
- **Diffie-Hellman key exchange:** building a shared secret in public (the "paint mixing" analogy), built on DLP.
- **Hybrid encryption:** use slow public-key crypto to exchange a key, then fast symmetric crypto for the data (this is what real systems actually do).

**Resources**

- Primary: Boneh _Cryptography I_ — public-key / RSA / Diffie-Hellman weeks.
- Supplement: Computerphile, _"Diffie-Hellman Key Exchange"_ and _"RSA."_

**Light exercise:** Walk through the paint-mixing DH analogy and map each step to `g`, `a`, `b`, `g^a`, `g^b`, `g^ab`.

**15-min review.**

---

## Session 9 — Elliptic Curves & Digital Signatures

**Goal:** Understand the crypto that actually runs modern systems (TLS, SSH, Bitcoin) and the mechanism for proving authorship.

**Pareto concepts**

- **Elliptic Curve Cryptography (ECC):** same security as RSA at far smaller key sizes; the ECDLP trapdoor.
- **ECDH** (key exchange) and the `P = sG` relationship.
- **Digital signatures:** sign with private key, verify with public key — provides authentication + non-repudiation + integrity.
- **ECDSA / EdDSA (Ed25519)** as the modern standards.

**Resources**

- Primary: Serious Cryptography — elliptic curve and signatures chapters; or Boneh's digital-signatures lectures.
- Supplement: Computerphile, _"Elliptic Curve Cryptography."_

**Light exercise:** State the difference between _encrypting with a public key_ and _signing with a private key_ — who uses which key, and what each guarantees.

**15-min review.**

---

## Session 10 — Putting It Together: TLS, PKI, and the Road Ahead (+ Capstone Review)

**Goal:** Assemble every primitive into the protocol you use every day, then lock in the whole mental model.

**Pareto concepts**

- **TLS/HTTPS** as the grand assembly: key exchange (ECDH) → certificates → AEAD for data. See every prior session appear in one handshake.
- **PKI & certificates:** Certificate Authorities, chains of trust, what the padlock really means.
- **Forward secrecy:** why ephemeral keys protect past sessions.
- **The frontier:** the **quantum threat** (Shor's algorithm breaks RSA/ECC) and **post-quantum cryptography** (lattice-based standards like ML-KEM/Kyber). One paragraph of awareness, not depth.

**Resources**

- Primary: Computerphile, _"Transport Layer Security (TLS)"_; Crypto 101 — TLS/protocols section.
- Supplement: Serious Cryptography — final chapters (TLS, post-quantum, real-world).

**Capstone (this session's "exercise"):** Without notes, draw the full TLS handshake and label which primitive (hash, AEAD, ECDH, signature, certificate) does each job. This single diagram proves you've absorbed the 80%.

**Extended final review (15 min):** Go through your cheat sheet end to end. For each primitive answer: _what it provides, what breaks it, when to use it._ Any blank line is your next study target.

---

## What this plan deliberately skips (the 80% of effort for 20% of payoff)

So you know what you're _not_ missing yet: formal security proofs and game-based definitions, the internal round structure of AES, exotic/legacy ciphers, secret sharing, zero-knowledge proofs, homomorphic encryption, and deep protocol edge cases. All are fascinating — and all are far easier to pick up _after_ the foundation above is solid.

## Where to go next (after the 20 hours)

- **Finish Boneh's _Cryptography I_** in full, then **Cryptography II**.
- **Cryptopals Challenges** (https://cryptopals.com/) — if you later want hands-on "break real crypto" practice; superb for cementing intuition.
- **Read _Serious Cryptography_ cover to cover** as your standing reference.

---

### Sources / resource links

- Dan Boneh, _Cryptography I_ (Stanford / Coursera): https://www.coursera.org/learn/crypto
- _Crypto 101_ (free): https://www.crypto101.io/
- _Serious Cryptography_, 2nd Ed., Aumasson (No Starch, 2024): https://nostarch.com/serious-cryptography-2nd-edition
- Khan Academy, _Journey into Cryptography_: https://www.khanacademy.org/computing/computer-science/cryptography
- Computerphile (YouTube): https://www.youtube.com/user/Computerphile
- Cryptopals Challenges: https://cryptopals.com/