This 20-hour plan is built on the Pareto Principle (80/20 rule). In modern cryptography, 80% of real-world security comes from correctly applying a handful of core concepts: **AES-GCM, SHA-256, HMAC, ECDH, and ECDSA**. 

We will entirely skip ancient history (Caesar ciphers, Enigma), deep mathematical proofs (number theory deep dives), and niche algorithms (Blowfish, DES) to focus purely on what powers the modern internet.

### **The 80/20 Resource Stack**
Before starting, acquire or bookmark these:
1. **Book:** *Real-World Cryptography* by David Wong (The single best 80/20 crypto book; highly visual, zero unnecessary math).
2. **Video:** *Cryptography 101* by Kirill Zotov (YouTube) – Excellent whiteboard explanations of modern protocols.
3. **Interactive:** *Cryptopals Crypto Challenges* (cryptopals.com) – For hands-on breaking.
4. **Tool:** *CyberChef* (gchq.github.io/CyberChef) – A visual tool to drag-and-drop crypto operations.

---

### **Session 1: The Cryptographic Mindset & Symmetric Encryption**
*The 80/20: Understanding that crypto is about *states* (Confidentiality, Integrity, Authentication) and that AES is the undisputed king of symmetric crypto.*
* **Minutes 0-30:** Threat models. Why "rolling your own crypto" is fatal. Kerckhoffs's Principle (security through obscurity doesn't work). 
* **Minutes 30-75:** AES (Advanced Encryption Standard). How it works conceptually (SubBytes, ShiftRows, MixColumns). Why key sizes (128 vs 256) matter less than proper implementation.
* **Minutes 75-105:** **Resource:** Read *Real-World Cryptography* Chapter 2. Watch Zotov's "AES Explained" video.
* **Minutes 105-120 (15-min Review):** 
  * *Feynman Prompt:* Explain to an imaginary 10-year-old why hiding the algorithm is a bad idea, but hiding the key is a good idea.

### **Session 2: Symmetric Crypto in Practice (Modes of Operation)**
*The 80/20: ECB is bad. GCM is good. Never use AES naked.*
* **Minutes 0-30:** Why we need Modes of Operation (AES only encrypts 16-byte blocks). The infamous ECB penguin (why encrypting block-by-block leaks patterns).
* **Minutes 30-75:** CBC (Cipher Block Chaining) and its vulnerability to Padding Oracle attacks. 
* **Minutes 75-105:** **AEAD (Authenticated Encryption with Associated Data)**. Why you *must* encrypt and authenticate together. Enter **AES-GCM**. How it works (Counter mode + GMAC). *Resource:* CyberChef: Encrypt an image with ECB vs. GCM to see the visual difference.
* **Minutes 105-120 (15-min Review):** 
  * *Feynman Prompt:* Why is AES-GCM the industry standard for symmetric encryption today? What happens if you use AES-ECB?

### **Session 3: Hash Functions & Data Integrity**
*The 80/20: Hashes are not encryption. They are one-way fingerprints. SHA-256 is the standard.*
* **Minutes 0-30:** Properties of a cryptographic hash: Deterministic, fast to compute, one-way (pre-image resistance), collision resistance.
* **Minutes 30-75:** The Merkle-Damgård construction (how SHA-256 works internally). Length extension attacks (why SHA-256 needs HMAC). Salting vs. Peppering for password hashing (introduce Argon2/Bcrypt here—do not use SHA for passwords!).
* **Minutes 75-105:** **Resource:** Read *Real-World Cryptography* Chapter 5. Use CyberChef to hash a file, change one byte, and watch the hash completely change (Avalanche effect).
* **Minutes 105-120 (15-min Review):** 
  * *Feynman Prompt:* If a hash is one-way, how do websites verify your password when you log in?

### **Session 4: Message Authentication Codes (MAC) & HMAC**
*The 80/20: Encryption does not guarantee integrity. You must use a MAC to prove a message wasn't tampered with.*
* **Minutes 0-30:** The "Encrypt-then-MAC" vs "MAC-then-Encrypt" debate. Why Encrypt-then-MAC is the only safe choice (and why AES-GCM solves this natively).
* **Minutes 30-75:** How HMAC works (Hash-based MAC). Why double-hashing prevents length extension attacks. 
* **Minutes 75-105:** **Resource:** Watch Zotov's video on MAC. Do Cryptopals Set 2, Challenge 28 (Implement SHA-1 keyed MAC / HMAC).
* **Minutes 105-120 (15-min Review):** 
  * *Feynman Prompt:* If an attacker flips a bit in an AES-CBC encrypted message, why is that dangerous? How does HMAC stop them?

### **Session 5: Key Exchange & The Diffie-Hellman Miracle**
*The 80/20: How two people can agree on a secret over a public channel without ever meeting.*
* **Minutes 0-45:** The Discrete Logarithm Problem. Finite Field Diffie-Hellman (DH). Painting the famous "color mixing" analogy. 
* **Minutes 45-105:** **Elliptic Curve Cryptography (ECC)**. Why ECC does the same thing as DH but with vastly smaller keys. Introduce **ECDH** (Elliptic Curve Diffie-Hellman). *Resource:* Read *Real-World Cryptography* Chapter 10 & 11. Watch "Diffie Hellman Key Exchange" by Computerphile.
* **Minutes 105-120 (15-min Review):** 
  * *Feynman Prompt:* Draw the DH color-mixing diagram from memory. Explain why a man-in-the-middle cannot compute the final secret color.

### **Session 6: Asymmetric Encryption & Hybrid Cryptography**
*The 80/20: RSA is mostly dead for encryption. Modern crypto uses ECDH to exchange a symmetric key, then uses AES. This is "Hybrid Cryptography."*
* **Minutes 0-30:** RSA basics (Prime factorization). Why RSA encryption is slow and vulnerable to modern attacks if used incorrectly.
* **Minutes 30-75:** The Hybrid Encryption pattern. This is how *every* secure message works today: 1. Generate random AES key. 2. Encrypt data with AES-GCM. 3. Encrypt the AES key with ECDH/RSA public key. 4. Send both. 
* **Minutes 75-105:** **Resource:** Read *Real-World Cryptography* Chapter 8 (Hybrid Encryption). Look up how PGP/GPG implements this exact pattern.
* **Minutes 105-120 (15-min Review):** 
  * *Feynman Prompt:* Why don't we just use RSA to encrypt a 1GB video file? Walk through the Hybrid Encryption steps.

### **Session 7: Digital Signatures & Non-Repudiation**
*The 80/20: Proving who sent a message using asymmetric crypto. ECDSA is the modern standard.*
* **Minutes 0-30:** The difference between MAC (symmetric, proves possession of shared key) and Signatures (asymmetric, proves identity to the world). 
* **Minutes 30-75:** **ECDSA** (Elliptic Curve Digital Signature Algorithm). The "Sign" and "Verify" algorithms conceptually. Why nonce reuse in ECDSA leaks the private key (a critical 80/20 failure mode).
* **Minutes 75-105:** **Resource:** Watch Zotov's "ECDSA explained" video. Read *Real-World Cryptography* Chapter 9. 
* **Minutes 105-120 (15-min Review):** 
  * *Feynman Prompt:* If I sign a contract with my private key, why can't I later claim someone else forged it? (Non-repudiation).

### **Session 8: Public Key Infrastructure (PKI) & Certificates**
*The 80/20: Signatures solve the identity problem between two people, but how do you trust a stranger's public key on the internet? Certificates.*
* **Minutes 0-45:** The TOFU (Trust On First Use) model vs. Web of Trust vs. Certificate Authorities (CAs). 
* **Minutes 45-105:** X.509 Certificates. What is actually inside a cert? (Subject, Issuer, Validity, Public Key, Signature). The Chain of Trust (Root CA -> Intermediate CA -> Leaf Cert). Certificate Revocation (CRLs vs. OCSP).
* **Minutes 75-105:* **Resource:** Open your browser, click the padlock next to any HTTPS URL, and trace the certificate path. Look at the "Signature Algorithm" (likely SHA-256 with RSA or ECDSA).
* **Minutes 105-120 (15-min Review):** 
  * *Feynman Prompt:* Explain the Chain of Trust. Why does my browser trust a certificate signed by "Let's Encrypt"?

### **Session 9: TLS - The Crown Jewel of Modern Crypto**
*The 80/20: Everything you've learned so far comes together in one protocol. TLS 1.3 is a masterpiece of cryptographic engineering.*
* **Minutes 0-30:** The evolution from SSL to TLS 1.3. Why TLS 1.2 is complex and TLS 1.3 stripped out the garbage (removed RSA key exchange, removed CBC, removed SHA-1).
* **Minutes 30-90:** The TLS 1.3 Handshake step-by-step:
  1. Client Hello (Supported groups, signatures).
  2. Server Hello + Key Share (ECDH public key).
  3. Client/Server compute shared secret (ECDH).
  4. Switch to AES-GCM for all further traffic.
  5. Certificate & Signature verification (ECDSA).
* **Minutes 90-105:** **Resource:** Read *Real-World Cryptography* Chapter 14. Watch "TLS 1.3 Explained" by Tech With Tim or similar.
* **Minutes 105-120 (15-min Review):** 
  * *Feynman Prompt:* Map every previous session to TLS 1.3. Where is the Key Exchange? Where is the Symmetric Encryption? Where is the Signature?

### **Session 10: Applied Crypto, Tooling, & Common Pitfalls**
*The 80/20: Knowing the theory is useless if you implement it wrong. Learning how to actually use crypto libraries safely.*
* **Minutes 0-45:** The "Do's and Don'ts" of implementing crypto. Never generate your own nonces/IVs. Don't compress then encrypt (CRIME attack). Use high-level libraries (like **Libsodium** or **Tink**) instead of low-level ones (like raw OpenSSL).
* **Minutes 45-105:** **Hands-on Lab:** 
  1. Download `libsodium` (or use PyNaCl in Python).
  2. Write a 20-line script that performs a complete secure exchange: Generate keys, encrypt a message using `crypto_box` (which handles ECDH + AES-GCM under the hood), and decrypt it.
  3. Use OpenSSL CLI to generate an RSA keypair and self-sign a certificate.
* **Minutes 105-120 (15-min Review):** 
  * *Feynman Prompt:* If a junior developer asks you, "Should I use OpenSSL's `AES_encrypt` function for our new app?", what is your answer and why?

### **Post-Plan Rule of Thumb:**
If you ever see a system that uses:
* DES, 3DES, RC4, MD5, or SHA-1 $\rightarrow$ **It is broken.**
* RSA for encryption (instead of signatures/key exchange) $\rightarrow$ **It is suspicious.**
* AES-CBC without a separate HMAC $\rightarrow$ **It is vulnerable.**
* *Anything else?* You are likely in the safe 80%.