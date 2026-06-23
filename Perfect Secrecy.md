# Perfect Secrecy

## The statement

An encryption scheme has **perfect secrecy** if observing a ciphertext gives an adversary _no_ information whatsoever about the plaintext. Formally, for a scheme with message space $\mathcal{M}$, key space $\mathcal{K}$, and ciphertext space $\mathcal{C}$:

> For every probability distribution over $\mathcal{M}$, every message $m \in \mathcal{M}$, and every ciphertext $c \in \mathcal{C}$ with $\Pr[C = c] > 0$: $$\Pr[M = m \mid C = c] = \Pr[M = m].$$

In words: the _a posteriori_ probability that the plaintext was $m$, after seeing the ciphertext $c$, is exactly the same as the _a priori_ probability of $m$ before seeing anything. The ciphertext and the plaintext are statistically independent random variables.

This definition is due to **Claude Shannon** (1949, _Communication Theory of Secrecy Systems_). It is also called **information-theoretic security** or **unconditional security**, because it holds against an adversary with unlimited computing power — it makes no assumptions about how fast the attacker can compute.

---

## Why this is the right definition

The intuition we want to capture is "the ciphertext leaks nothing about the message." Shannon's condition formalizes exactly that. There are three equivalent ways to say the same thing, and seeing why they coincide is the heart of understanding the concept.

### Formulation 1 — Posterior equals prior

$$\Pr[M = m \mid C = c] = \Pr[M = m]$$

Whatever you believed about the message before, you believe the identical thing afterward. The ciphertext updated nothing.

### Formulation 2 — Independence of message and ciphertext

$$\Pr[M = m,, C = c] = \Pr[M = m] \cdot \Pr[C = c]$$

$M$ and $C$ are independent. This is just Bayes' rule applied to Formulation 1. Independence is the cleanest way to express "no information," because two independent variables share zero mutual information.

### Formulation 3 — Ciphertext distribution is message-independent

$$\Pr[C = c \mid M = m_0] = \Pr[C = c \mid M = m_1] \quad\text{for all } m_0, m_1, c.$$

The probability of producing a given ciphertext is the same no matter which message was encrypted. An eavesdropper sees the _same_ distribution of ciphertexts regardless of the plaintext, so the ciphertext cannot discriminate between candidate messages.

**These three are provably equivalent.** Formulation 3 is usually the most convenient to verify for a concrete scheme, because it does not reference the message distribution at all.

### An information-theoretic restatement

Using Shannon entropy, perfect secrecy is equivalent to $$H(M \mid C) = H(M),$$ i.e. the conditional uncertainty about the message _given_ the ciphertext equals the original uncertainty. Equivalently, the **mutual information** is zero: $$I(M; C) = 0.$$ The channel from message to ciphertext, as seen by the attacker, transmits zero bits of information about the plaintext.

---

## The canonical example: the One-Time Pad

The **one-time pad (OTP)** is the standard scheme that achieves perfect secrecy.

- **Messages, keys, ciphertexts** are all $n$-bit strings: $\mathcal{M} = \mathcal{K} = \mathcal{C} = {0,1}^n$.
- The **key** $k$ is chosen _uniformly at random_ and used **only once**.
- **Encryption:** $c = m \oplus k$ (bitwise XOR).
- **Decryption:** $m = c \oplus k$ (XOR is its own inverse).

### Why it is perfectly secret

Fix any ciphertext $c$ and any message $m$. The encryption produces $c$ from $m$ exactly when the key happens to be $k = m \oplus c$. Since the key is uniform over ${0,1}^n$, that specific key occurs with probability $2^{-n}$: $$\Pr[C = c \mid M = m] = \Pr[K = m \oplus c] = 2^{-n}.$$ This value $2^{-n}$ does **not depend on $m$** — it is the same for every message. That is precisely Formulation 3, so the OTP has perfect secrecy.

Intuitively: for _any_ observed ciphertext, _every_ plaintext is possible, and all are equally consistent with what the attacker sees. Given the ciphertext `1011`, the true message could be `0000` (if the key was `1011`), or `1111` (if the key was `0100`), or anything else — each explanation requires a key that is exactly as likely as any other. The ciphertext rules nothing out.

---

## Shannon's impossibility theorem — the price of perfection

Perfect secrecy is not free. Shannon proved a hard limit:

> **Theorem.** If a scheme has perfect secrecy, then $|\mathcal{K}| \ge |\mathcal{M}|$ — the key space must be at least as large as the message space.

When messages and keys are uniform, this means the key must be **at least as long as the message**.

### Sketch of the argument

Suppose, for contradiction, that there are fewer keys than messages ($|\mathcal{K}| < |\mathcal{M}|$). Take any ciphertext $c$ that can actually occur. Decrypting $c$ under each of the keys yields at most $|\mathcal{K}|$ distinct messages. Because there are strictly more messages than keys, some message $m^*$ is **not** reachable by decrypting $c$ under any key — meaning $\Pr[M = m^* \mid C = c] = 0$. But if $m^*$ had nonzero prior probability, then $0 = \Pr[M = m^* \mid C = c] \ne \Pr[M = m^*]$, violating perfect secrecy. Hence we must have $|\mathcal{K}| \ge |\mathcal{M}|$. $\blacksquare$

### Practical consequence

This theorem is why perfect secrecy is rarely used in practice. To send a 1-gigabyte file with perfect secrecy you need a 1-gigabyte key, pre-shared through some secure channel, and the key can never be reused. If you already have a secure channel to share a key that large, you could often just use it to send the message. This key-distribution burden is the OTP's fatal practical flaw.

---

## Critical caveats (how perfect secrecy is broken in practice)

The math is airtight, but the assumptions are demanding. Real-world "OTP" implementations usually fail one of these:

1. **The key must be truly random.** If the key comes from a pseudorandom generator, the scheme is at best _computationally_ secure, not perfectly secret — a powerful adversary could in principle distinguish the PRG output.
    
2. **The key must never be reused.** Reusing a pad on two messages $m_1, m_2$ leaks $c_1 \oplus c_2 = m_1 \oplus m_2$, which removes the key entirely and exposes the XOR of the two plaintexts — often enough to recover both. This is the "two-time pad" mistake (famously broken in the VENONA project).
    
3. **It protects only confidentiality of content.** Perfect secrecy hides _what_ the message says, but not its **length** (the ciphertext length equals the message length), nor the fact that communication occurred, nor metadata. It provides **no integrity or authentication** — an attacker who flips a bit in the ciphertext flips the corresponding plaintext bit undetected.
    

---

## Perfect secrecy vs. computational security

||**Perfect / information-theoretic**|**Computational**|
|---|---|---|
|Adversary power|Unbounded|Polynomial-time (bounded)|
|Security guarantee|Absolute, unconditional|Holds unless a hard problem is solved|
|Key length|$\ge$ message length|Short (e.g. 128–256 bits)|
|Relies on unproven assumptions|No|Yes (e.g. factoring, discrete log are hard)|
|Practicality|Limited (key distribution)|Ubiquitous (AES, RSA, ECC, …)|

Modern cryptography almost always settles for **computational security**: it weakens the adversary to "efficient" (polynomial-time) algorithms in exchange for short, reusable keys. This is what makes AES, TLS, and public-key cryptography usable. Perfect secrecy remains the theoretical gold standard and is used where the stakes justify the cost (e.g. certain diplomatic and military channels) — and its ideas reappear in **secret sharing** and the security of **quantum key distribution**.

---

## Summary

Perfect secrecy says the ciphertext is statistically independent of the plaintext: $\Pr[M = m \mid C = c] = \Pr[M = m]$, equivalently $I(M; C) = 0$. The one-time pad achieves it because XOR with a uniform, single-use key makes every ciphertext equally likely for every message. Shannon's theorem shows the price is unavoidable — the key must be at least as long as everything you will ever encrypt — which is why practical cryptography trades this absolute guarantee for the computational security that short, reusable keys can provide.