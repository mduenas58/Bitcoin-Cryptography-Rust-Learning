# Finite Fields and Elliptic Curves: A Bitcoin-Focused Tutorial

> _"The mathematics that secures Bitcoin is the same mathematics that would take longer than the age of the universe to break."_

---

## Table of Contents

1. [Why This Mathematics Powers Bitcoin](https://claude.ai/local_sessions/local_466b5495-597f-48f6-a717-a2fa6c498f9c#1-why-this-mathematics-powers-bitcoin)
2. [Mathematical Foundations: Groups, Rings, and Fields](https://claude.ai/local_sessions/local_466b5495-597f-48f6-a717-a2fa6c498f9c#2-mathematical-foundations-groups-rings-and-fields)
3. [Finite Fields in Depth](https://claude.ai/local_sessions/local_466b5495-597f-48f6-a717-a2fa6c498f9c#3-finite-fields-in-depth)
4. [Elliptic Curves Over the Real Numbers](https://claude.ai/local_sessions/local_466b5495-597f-48f6-a717-a2fa6c498f9c#4-elliptic-curves-over-the-real-numbers)
5. [Elliptic Curves Over Finite Fields](https://claude.ai/local_sessions/local_466b5495-597f-48f6-a717-a2fa6c498f9c#5-elliptic-curves-over-finite-fields)
6. [Bitcoin's Curve: secp256k1](https://claude.ai/local_sessions/local_466b5495-597f-48f6-a717-a2fa6c498f9c#6-bitcoins-curve-secp256k1)
7. [Bitcoin Key Generation and Addresses](https://claude.ai/local_sessions/local_466b5495-597f-48f6-a717-a2fa6c498f9c#7-bitcoin-key-generation-and-addresses)
8. [ECDSA: How Bitcoin Signs Transactions](https://claude.ai/local_sessions/local_466b5495-597f-48f6-a717-a2fa6c498f9c#8-ecdsa-how-bitcoin-signs-transactions)
9. [Schnorr Signatures and Taproot](https://claude.ai/local_sessions/local_466b5495-597f-48f6-a717-a2fa6c498f9c#9-schnorr-signatures-and-taproot)
10. [Complete Python Implementations](https://claude.ai/local_sessions/local_466b5495-597f-48f6-a717-a2fa6c498f9c#10-complete-python-implementations)
11. [Security Considerations and Attack Vectors](https://claude.ai/local_sessions/local_466b5495-597f-48f6-a717-a2fa6c498f9c#11-security-considerations-and-attack-vectors)
12. [References and Further Reading](https://claude.ai/local_sessions/local_466b5495-597f-48f6-a717-a2fa6c498f9c#12-references-and-further-reading)

---

## 1. Why This Mathematics Powers Bitcoin

In January 2009, Satoshi Nakamoto launched the Bitcoin network. Every transaction ever broadcast — the transfer of billions of dollars in value — relies on a branch of mathematics developed in the 19th century by Niels Henrik Abel and Arthur Cayley, formalised for computation by Neal Koblitz and Victor Miller in 1985, and standardised for Bitcoin's specific use by Certicom in 2000.

That mathematics is **Elliptic Curve Cryptography (ECC)**.

### 1.1 The Three Things ECC Does for Bitcoin

**Key generation.** A private key is a random integer k in the range [1, n−1], where n is roughly 2²⁵⁶. The corresponding public key is the point K = k · G on an elliptic curve over a finite field, where G is a fixed "base point." Going from k to K (multiplying a point by a scalar) is computationally trivial. Going from K back to k (the Elliptic Curve Discrete Logarithm Problem, ECDLP) is computationally infeasible for well-chosen curves.

**Digital signatures.** Bitcoin uses the Elliptic Curve Digital Signature Algorithm (ECDSA) to prove that the owner of a private key authorised a transaction, without ever revealing the private key. Taproot (activated November 2021) additionally supports Schnorr signatures, which are simpler, smaller, and composable.

**Address derivation.** A Bitcoin address is a hash of the public key. Since hashing is a one-way function and extracting the private key from a public key is infeasible, addresses are safe to share publicly.

### 1.2 Why Not RSA?

RSA, the dominant public-key system before ECC, provides comparable security at much larger key sizes. A 256-bit ECC key offers roughly the same security as a 3072-bit RSA key. Smaller keys mean:

- Smaller transactions (lower fees on Bitcoin's size-limited blocks)
- Faster signature verification (the network verifies millions of signatures per day)
- Less data stored in the UTXO set

### 1.3 The Stack from Math to Bitcoin

```
Abstract Algebra (groups, rings, fields)
          ↓
Finite Fields GF(p)     — integers mod a prime
          ↓
Elliptic Curves E(GF(p)) — points satisfying y² = x³ + ax + b  over GF(p)
          ↓
secp256k1               — Bitcoin's specific curve and parameters
          ↓
ECDSA / Schnorr         — signature schemes built on scalar multiplication
          ↓
Bitcoin transactions    — outputs locked to public keys, unlocked by signatures
```

Every layer below depends on the correctness and hardness properties of the layer above. Understanding the bottom of this stack is what this tutorial is about.

---

## 2. Mathematical Foundations: Groups, Rings, and Fields

Before we can do arithmetic on a curve over a finite field, we need to establish what "arithmetic" means in an abstract setting.

### 2.1 Groups

A **group** is the simplest algebraic structure with a meaningful notion of "combining two elements."

**Definition.** A group is a set G with a binary operation · satisfying:

|Axiom|Statement|
|---|---|
|Closure|∀ a, b ∈ G: a · b ∈ G|
|Associativity|∀ a, b, c: (a · b) · c = a · (b · c)|
|Identity|∃ e ∈ G: e · a = a · e = a|
|Inverses|∀ a ∈ G, ∃ a⁻¹: a · a⁻¹ = e|

If additionally a · b = b · a for all a, b, the group is **abelian** (commutative).

**Examples relevant to Bitcoin:**

- **(ℤ, +)**: the integers under addition. Infinite, abelian. Identity = 0, inverse of n = −n.
- **(ℤ/nℤ, +)**: integers modulo n under addition. Finite, abelian, order n. This is the additive group underlying GF(p).
- *_(ℤ/pℤ)_ under ×**: non-zero integers mod a prime p under multiplication. Finite, abelian, order p−1. This is the multiplicative group of GF(p).
- **E(GF(p))**: the set of points on an elliptic curve over GF(p) under point addition. This is the group Bitcoin's security relies on.

**Cyclic groups.** A group G is **cyclic** if there exists an element g (a _generator_) such that every element of G can be written as gⁿ for some integer n. Both (ℤ/pℤ)* and E(GF(p)) contain large cyclic subgroups.

**Order.** The order of a group is its number of elements. The order of an element g is the smallest positive integer k with gᵏ = e (the identity).

**Lagrange's Theorem.** If H is a subgroup of a finite group G, then |H| divides |G|. This is why the order of any element must divide the group order — a fact Bitcoin's security analysis depends on.

### 2.2 Rings

A **ring** extends a group by adding a second operation (multiplication) that distributes over the first.

**Definition.** A ring (R, +, ×) satisfies:

- (R, +) is an abelian group
- × is associative with identity 1
- × distributes over +: a(b + c) = ab + ac

A **commutative ring** has ab = ba. The integers ℤ are the archetypal commutative ring.

**Key property for our purposes:** In a ring, we can have "zero divisors" — non-zero elements a, b with a × b = 0. For example, in ℤ/6ℤ: 2 × 3 = 6 ≡ 0 mod 6. This means ℤ/6ℤ is **not** a field.

### 2.3 Fields

A **field** is a ring where every non-zero element has a multiplicative inverse. In other words, division is always possible (except by zero).

**Definition.** A field (F, +, ×) satisfies:

- (F, +) is an abelian group with identity 0
- (F \ {0}, ×) is an abelian group with identity 1
- × distributes over +

**Familiar fields:** ℚ, ℝ, ℂ. And crucially for Bitcoin: **GF(p)** for prime p.

**Why fields matter for curves.** The equation y² = x³ + ax + b is only a well-behaved curve (with a well-defined group law) when x, y, a, b live in a field. We need inverses (to compute slopes of tangent lines) and no zero divisors (to ensure unique intersections).

### 2.4 Quick Comparison

```
Structure   | Has +  | Has ×  | Subtraction | Division by non-zero
------------|--------|--------|-------------|---------------------
Group       |  (one  |  op)   |   depends   |       no
Ring        |  yes   |  yes   |    yes      |       no
Field       |  yes   |  yes   |    yes      |       YES ← key
```

---

## 3. Finite Fields in Depth

A **finite field** GF(q) (also written 𝔽_q) has exactly q elements, where q must be a **prime power**: q = pⁿ for some prime p and positive integer n.

Bitcoin exclusively uses **prime fields** GF(p) — the case n = 1.

### 3.1 The Prime Field GF(p)

**Elements:** the integers {0, 1, 2, …, p − 1}.

**Addition:** (a + b) mod p

**Multiplication:** (a × b) mod p

**Additive inverse of a:** (p − a) mod p

**Multiplicative inverse of a:** the unique b in {1, …, p−1} with a × b ≡ 1 (mod p)

This is a valid field because:

1. When p is prime, gcd(a, p) = 1 for any 0 < a < p (no shared factors).
2. By Bézout's identity, there exist integers x, y with ax + py = 1.
3. Therefore ax ≡ 1 (mod p), meaning x is the inverse of a.

**Concrete example — GF(7):**

```
5 + 6 = 11 ≡ 4 (mod 7)
3 × 5 = 15 ≡ 1 (mod 7)   →   3⁻¹ = 5
4 - 6 = -2 ≡ 5 (mod 7)
10 / 3 = 10 × 3⁻¹ = 10 × 5 = 50 ≡ 1 (mod 7)
```

### 3.2 Computing Multiplicative Inverses

**Method 1 — Fermat's Little Theorem:**

Since a^(p−1) ≡ 1 (mod p) for any a ≢ 0 (mod p):

```
a⁻¹ ≡ a^(p−2)  (mod p)
```

In Python: `pow(a, p - 2, p)` — fast modular exponentiation, built into the language.

**Method 2 — Extended Euclidean Algorithm (more general, works for composite moduli too):**

```python
def modinv(a, m):
    """Modular inverse of a modulo m using the extended Euclidean algorithm."""
    g, x, _ = extended_gcd(a, m)
    if g != 1:
        raise ValueError(f"{a} has no inverse mod {m}")
    return x % m

def extended_gcd(a, b):
    if b == 0:
        return a, 1, 0
    g, x, y = extended_gcd(b, a % b)
    return g, y, x - (a // b) * y

# Examples:
print(modinv(3, 7))    # 5  (3*5=15≡1 mod 7)
print(modinv(7, 11))   # 8  (7*8=56≡1 mod 11)
```

### 3.3 Bitcoin's Two Primes

Bitcoin's secp256k1 curve uses arithmetic over GF(p) where:

```
p = 2²⁵⁶ − 2³² − 2⁹ − 2⁸ − 2⁷ − 2⁶ − 2⁴ − 1
  = 2²⁵⁶ − 2³² − 977
  = 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFEFFFFFC2F
```

This prime was chosen because it has a special form (a Mersenne-like "pseudo-Mersenne" prime) that makes modular reduction about 3× faster than with an arbitrary 256-bit prime — a significant performance win given how many modular reductions occur during point multiplication.

The curve's **group order** n (the number of points on the curve) is a _different_ prime:

```
n = 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFEBAAEDCE6AF48A03BBFD25E8CD0364141
```

Private keys are integers in [1, n−1]. Signature arithmetic happens in GF(n), not GF(p).

### 3.4 Fermat's Little Theorem — the Engine of Modular Arithmetic

This theorem is used constantly in Bitcoin's cryptographic operations:

> **Fermat's Little Theorem:** For any prime p and integer a with gcd(a, p) = 1: **a^(p−1) ≡ 1 (mod p)**

Immediate consequences:

- a^p ≡ a (mod p) for _all_ integers a (including multiples of p)
- a^(-1) ≡ a^(p−2) (mod p)
- Square roots: if p ≡ 3 (mod 4), then √a ≡ a^((p+1)/4) (mod p). Bitcoin's p satisfies p ≡ 3 (mod 4), making square root extraction simple — needed when decompressing public keys from their x-coordinate.

```python
p = 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFEFFFFFC2F
print(p % 4)   # 3  ← confirms p ≡ 3 (mod 4)

# Square root in GF(p): sqrt(x) = x^((p+1)/4) mod p
def field_sqrt(x, p):
    """Square root of x in GF(p), assuming p ≡ 3 (mod 4) and x is a QR."""
    return pow(x, (p + 1) // 4, p)

# Verify: x = 4, sqrt = 2 or p-2
x = 4
root = field_sqrt(x, p)
print(root == 2 or root == p - 2)   # True
print(pow(root, 2, p) == x)          # True
```

### 3.5 The Quadratic Residue Test

A number x in GF(p) is a **quadratic residue** (has a square root) if and only if:

```
x^((p−1)/2) ≡ 1  (mod p)
```

This is called the **Legendre symbol** and equals +1 for quadratic residues, −1 for non-residues, 0 for x = 0. For a random y-coordinate on an elliptic curve, exactly half of all x values will yield points (both the root y and p−y give points).

---

## 4. Elliptic Curves Over the Real Numbers

Before restricting to finite fields, we build intuition over ℝ where we can draw pictures.

### 4.1 The Weierstrass Equation

An **elliptic curve** in short Weierstrass form is:

```
E: y² = x³ + ax + b
```

with the condition **4a³ + 27b² ≠ 0** (the _discriminant_ condition that prevents cusps and self-intersections, which would break the group law).

For Bitcoin's secp256k1: a = 0, b = 7, giving:

```
y² = x³ + 7
```

This is a smooth cubic with a single component that extends to infinity.

### 4.2 The Point at Infinity

An elliptic curve is not just the set of real-number solutions — it also includes a special "point at infinity" denoted **O** (or ∞). This point is the identity element of the group.

Geometrically: imagine projecting the curve onto the "projective plane" (adding a line at infinity). Every pair of parallel lines meets at a point on this line at infinity. For our cubic, the vertical line x = c meets the curve in two points (x, y) and (x, −y); as y → ∞, these two points "meet" at O.

In homogeneous coordinates, O = [0 : 1 : 0].

### 4.3 The Group Law: Addition of Points

The set of points on an elliptic curve, including O, forms an **abelian group** under the following addition rule:

**Geometric description:** To add points P and Q:

1. Draw the line through P and Q (or the tangent at P if P = Q).
2. Find the third intersection point R' with the curve.
3. Reflect R' across the x-axis to get R = P + Q.

The reflection step ensures associativity; the tangent-at-P rule handles point doubling.

**Why does a line always intersect a cubic in exactly three points?** By Bézout's theorem, a line (degree 1) and a cubic (degree 3) intersect in exactly 1 × 3 = 3 points in the projective plane (counting multiplicity and complex roots). Tangency gives a double root. A vertical line gives two real roots plus the point at infinity O.

**Algebraic formulas for P = (x₁, y₁), Q = (x₂, y₂):**

```
Case 1: P ≠ Q  (point addition)
    λ = (y₂ − y₁) / (x₂ − x₁)        (slope of the chord)
    x₃ = λ² − x₁ − x₂
    y₃ = λ(x₁ − x₃) − y₁

Case 2: P = Q  (point doubling)
    λ = (3x₁² + a) / (2y₁)            (slope of tangent)
    x₃ = λ² − 2x₁
    y₃ = λ(x₁ − x₃) − y₁

Special cases:
    P + O = P   for any P
    P + (−P) = O   where −P = (x, −y)
    O + O = O
```

These formulas hold verbatim over **any** field — real numbers, complex numbers, or finite fields GF(p). Only the meaning of the arithmetic operations changes.

### 4.4 Scalar Multiplication

The **scalar multiple** k·P (also written [k]P) means adding P to itself k times:

```
k·P = P + P + P + ···  (k times)
```

Direct repeated addition would take O(k) steps — hopelessly slow for k ≈ 2²⁵⁶. Instead, the **double-and-add algorithm** (analogous to fast modular exponentiation) works in O(log k) steps:

```
k = 11 = 1011₂

[11]P = [8]P + [2]P + [1]P
      = (((P doubled 3 times) + (P doubled 1 time)) + P)
```

This takes about 256 doublings and ~128 additions for a 256-bit scalar — roughly 384 field operations instead of 2²⁵⁶.

### 4.5 Why Scalar Multiplication is a One-Way Function

**Forward:** Given k and P, compute k·P. Cost: ~384 field multiplications mod p. With p ≈ 2²⁵⁶, this takes microseconds.

**Inverse (ECDLP):** Given k·P and P, find k. No algorithm better than O(√n) is known for general elliptic curves. For n ≈ 2²⁵⁶, this means O(2¹²⁸) operations — more than the estimated number of atoms in the observable universe (~2²⁶⁶).

The gap between these two directions is the mathematical trapdoor Bitcoin relies on.

---

## 5. Elliptic Curves Over Finite Fields

Over a finite field GF(p), the same Weierstrass equation defines a **finite set of points**:

```
E(GF(p)) = { (x, y) ∈ GF(p)² : y² ≡ x³ + ax + b (mod p) } ∪ { O }
```

### 5.1 What the Curve Looks Like

Over GF(p), there are no continuous curves — only a finite scatter of points. For each x ∈ {0, 1, …, p−1}, compute x³ + ax + b mod p, then check if it's a quadratic residue (has a square root mod p). If it does, there are exactly two points (x, y) and (x, p−y) for that x (unless y = 0, giving one point).

**Example — y² = x³ + 7 over GF(17):**

```python
p = 17
a, b = 0, 7
points = [(x, y) for x in range(p) for y in range(p)
          if (y*y - x**3 - a*x - b) % p == 0]
print(points)
# Approximately half of the 17 x-values give points → ~17 points
```

### 5.2 Hasse's Theorem

The number of points |E(GF(p))| satisfies:

```
|p + 1 − |E(GF(p))|| ≤ 2√p
```

This means the curve has approximately p + 1 points, with a small "trace of Frobenius" t = p + 1 − |E(GF(p))| satisfying |t| ≤ 2√p. For secp256k1 with p ≈ 2²⁵⁶, we get approximately 2²⁵⁶ points — the curve is "almost full."

The trace of secp256k1 is extremely small (the curve was deliberately designed so that |E(GF(p))| = n is prime, maximising security).

### 5.3 The Group Law Over GF(p)

The same addition formulas apply, but every operation (addition, subtraction, multiplication, division) is performed **modulo p**:

```
λ = (y₂ − y₁) · (x₂ − x₁)⁻¹  mod p    (for P ≠ Q)
λ = (3x₁² + a) · (2y₁)⁻¹       mod p    (for P = Q, doubling)
x₃ = λ² − x₁ − x₂               mod p
y₃ = λ(x₁ − x₃) − y₁             mod p
```

All divisions are modular inverses (computed via Fermat or extended Euclidean).

### 5.4 Why the Curve Order Must Be Prime

For Bitcoin, n = |E(GF(p))| is a prime. This is important for three reasons:

1. **Every non-zero element generates the full group.** By Lagrange's theorem, the order of any element must divide n. Since n is prime, its only divisors are 1 and n. So every non-zero point is a generator — there are no "weak" subgroups.
    
2. **The MOV attack is prevented.** If n had small prime factors, the ECDLP could be reduced to a discrete logarithm in a small finite field (where it's tractable). A prime n eliminates this.
    
3. **The anomalous attack is prevented.** If n = p (the curve order equals the field characteristic), there's a polynomial-time ECDLP algorithm (Smart's attack). The secp256k1 designers verified n ≠ p.
    

---

## 6. Bitcoin's Curve: secp256k1

The curve is standardised in SEC 2 (Standards for Efficient Cryptography, version 2) as **secp256k1**. The "sec" stands for SEC, "p" for prime field, "256" for 256-bit field, "k" for Koblitz (a particular curve shape), "1" for the first such curve.

### 6.1 Domain Parameters

```python
# secp256k1 parameters — every Bitcoin node knows these

# Field prime (coordinates live in GF(p))
p  = 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFEFFFFFC2F

# Curve equation: y² = x³ + ax + b  (a=0 means no x term)
a  = 0
b  = 7

# Base point G (the generator) — x and y coordinates
Gx = 0x79BE667EF9DCBBAC55A06295CE870B07029BFCDB2DCE28D959F2815B16F81798
Gy = 0x483ADA7726A3C4655DA4FBFC0E1108A8FD17B448A68554199C47D08FFB10D4B8

# Group order: number of points on E(GF(p))
n  = 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFEBAAEDCE6AF48A03BBFD25E8CD0364141

# Cofactor h = |E(GF(p))| / n = 1
# (The group is cyclic and <G> = the whole group)
h  = 1

G  = (Gx, Gy)
```

### 6.2 Why a = 0?

Setting a = 0 simplifies the doubling formula significantly:

```
λ = (3x₁² + a) / (2y₁)
       ↓  with a = 0
λ = 3x₁² / (2y₁)
```

This saves one multiplication per doubling operation. In key generation, roughly half the operations are doublings, so this offers a ~10–15% speedup.

### 6.3 Why This Specific p?

The prime p = 2²⁵⁶ − 2³² − 977 is a **pseudo-Mersenne prime**. Reducing modulo such a prime is fast:

Since 2²⁵⁶ ≡ 2³² + 977 (mod p), any 512-bit product c can be reduced with:

```
c mod p ≈ c_high · (2³² + 977) + c_low
```

where c_high and c_low are the upper and lower 256 bits. This avoids general-purpose multi-precision division and is roughly 3× faster than reducing modulo an arbitrary 256-bit prime.

### 6.4 Verifying G is on the Curve

```python
def is_on_curve(x, y, a, b, p):
    return (y * y - x * x * x - a * x - b) % p == 0

print(is_on_curve(Gx, Gy, 0, 7, p))   # True
```

### 6.5 Verifying the Group Order

The defining property of n is that n·G = O (the point at infinity):

```python
# (We implement this in Section 10)
# scalar_mul(n, G, 0, p) should return the point at infinity
```

This is verified during the standardisation process and spot-checked by every implementation. If n·G ≠ O, the implementation is buggy.

### 6.6 Point Compression

An uncompressed public key stores both x and y (65 bytes: 0x04 prefix + 32-byte x + 32-byte y). A **compressed** public key stores only x plus a single bit indicating the parity of y (33 bytes: 0x02 or 0x03 prefix + 32-byte x).

To decompress: given x, compute y² = x³ + 7 mod p, then y = (y²)^((p+1)/4) mod p. Choose the root matching the parity bit.

```python
def decompress_pubkey(x, parity, p, a=0, b=7):
    """Recover y from x and the low bit of y (parity = 0 or 1)."""
    y_sq = (pow(x, 3, p) + a * x + b) % p
    y = pow(y_sq, (p + 1) // 4, p)
    if y % 2 != parity:
        y = p - y
    return (x, y)
```

---

## 7. Bitcoin Key Generation and Addresses

### 7.1 Private Key Generation

A Bitcoin private key is a uniformly random integer k in [1, n−1]:

```python
import os
import hashlib

def generate_private_key():
    """
    Generate a cryptographically secure random private key.
    Rejection-sample to ensure uniform distribution.
    """
    n = 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFEBAAEDCE6AF48A03BBFD25E8CD0364141
    while True:
        candidate = int.from_bytes(os.urandom(32), 'big')
        if 1 <= candidate < n:
            return candidate

private_key = generate_private_key()
print(f"Private key (hex): {private_key:064x}")
```

**Security note:** The source of randomness is critical. Several early Bitcoin wallets had weak PRNGs, leading to theft of coins. The Android SecureRandom vulnerability in 2013 drained wallets using Bitcoin apps that relied on a buggy Java RNG.

### 7.2 Public Key Generation

The public key is the elliptic curve point K = k · G:

```python
# (Using the full implementation from Section 10)
# public_key = scalar_mul(private_key, G, p=p, a=0)
```

The public key can be expressed in three formats:

|Format|Prefix|Size|When Used|
|---|---|---|---|
|Uncompressed|0x04|65 bytes|Legacy (rare)|
|Compressed (even y)|0x02|33 bytes|Standard since 2012|
|Compressed (odd y)|0x03|33 bytes|Standard since 2012|

### 7.3 Bitcoin Address Derivation (P2PKH)

A **Pay-to-Public-Key-Hash (P2PKH)** address is derived by hashing the public key through two hash functions:

```
Address = Base58Check( 0x00 || RIPEMD160( SHA256( compressed_pubkey ) ) )
```

```python
import hashlib

def hash160(data: bytes) -> bytes:
    """Bitcoin's Hash160: RIPEMD160(SHA256(data))."""
    sha256_hash = hashlib.sha256(data).digest()
    ripemd160 = hashlib.new('ripemd160')
    ripemd160.update(sha256_hash)
    return ripemd160.digest()

def checksum(data: bytes) -> bytes:
    """4-byte checksum = first 4 bytes of SHA256(SHA256(data))."""
    return hashlib.sha256(hashlib.sha256(data).digest()).digest()[:4]

BASE58_CHARS = '123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz'

def base58_encode(data: bytes) -> str:
    """Bitcoin Base58 encoding."""
    # Count leading zero bytes
    leading_zeros = len(data) - len(data.lstrip(b'\x00'))
    n = int.from_bytes(data, 'big')
    result = []
    while n > 0:
        n, remainder = divmod(n, 58)
        result.append(BASE58_CHARS[remainder])
    return '1' * leading_zeros + ''.join(reversed(result))

def pubkey_to_address(pubkey_bytes: bytes, mainnet=True) -> str:
    """
    Convert a compressed or uncompressed public key to a P2PKH Bitcoin address.
    """
    version = b'\x00' if mainnet else b'\x6f'   # 0x6f = testnet
    payload = version + hash160(pubkey_bytes)
    return base58_encode(payload + checksum(payload))


# Example (using placeholder public key bytes for illustration):
import struct

def serialize_pubkey(x: int, y: int, compressed=True) -> bytes:
    if compressed:
        prefix = b'\x02' if y % 2 == 0 else b'\x03'
        return prefix + x.to_bytes(32, 'big')
    else:
        return b'\x04' + x.to_bytes(32, 'big') + y.to_bytes(32, 'big')
```

### 7.4 Hierarchical Deterministic (HD) Wallets — BIP32

Modern wallets don't generate independent random keys. Instead they derive a **tree** of keys from a single root seed using BIP32 (Bitcoin Improvement Proposal 32):

```
Master seed (128–256 random bits)
    → HMAC-SHA512 → master private key + master chain code
          ↓
    Child key derivation: child_key = parent_key + HMAC-SHA512(...)
          ↓
    BIP44 path: m / purpose' / coin_type' / account' / change / index
    Example:    m / 44' / 0' / 0' / 0 / 0   (first Bitcoin receiving address)
```

The apostrophe denotes **hardened derivation**, which uses the private key in the HMAC, preventing an attacker who knows a child public key and chain code from recovering the parent private key.

**BIP39** encodes the master seed as 12–24 human-readable words (a mnemonic), making it easy to back up.

### 7.5 SegWit and Bech32 Addresses

**Native SegWit (P2WPKH)** addresses use a different encoding:

```
bech32_address = Bech32( "bc" || 0x00 || SHA256(compressed_pubkey)[0:20] )
```

Bech32 addresses begin with `bc1q` (mainnet) and use an error-correcting code that can detect (and sometimes correct) typos. The witness version byte (0x00) indicates SegWit v0. Taproot addresses use witness version 0x01 and start with `bc1p`.

---

## 8. ECDSA: How Bitcoin Signs Transactions

ECDSA is defined in ANSI X9.62 and adopted for Bitcoin in the original codebase.

### 8.1 Key Concepts

**The signature goal:** Alice wants to prove she authorised a transaction T. She uses her private key k to produce a pair (r, s) — the signature — such that anyone with her public key K = k·G can verify it, but nobody can produce (r, s) for T without knowing k.

**The nonce:** Each signature requires a fresh random number ℓ (also called k in many textbooks, but we use ℓ to avoid confusion with the private key). **Reusing ℓ across two different signatures immediately leaks the private key.** This is not a theoretical concern — the Sony PlayStation 3 was broken this way in 2010, and Bitcoin wallets have been drained by nonce reuse.

### 8.2 Signing Algorithm

**Inputs:** message hash z (32 bytes), private key k, curve parameters (G, n, p).

```
1. Choose a random nonce ℓ ∈ [1, n−1]  (must be unique, unpredictable)
2. Compute R = ℓ · G
3. r = R.x mod n      (the x-coordinate of R, reduced mod n)
   if r = 0, go to step 1
4. s = ℓ⁻¹ · (z + r·k)  mod n
   if s = 0, go to step 1
5. Output signature (r, s)
```

**Intuition:** r is "where the random nonce point lands on the x-axis." s encodes how the private key and message hash relate to that nonce. Verification reverses the encoding using the public key.

### 8.3 Verification Algorithm

**Inputs:** message hash z, signature (r, s), public key K = (Kx, Ky), curve parameters.

```
1. Check r, s ∈ [1, n−1]
2. Compute w = s⁻¹ mod n
3. u₁ = z · w  mod n
   u₂ = r · w  mod n
4. Compute point X = u₁·G + u₂·K
5. If X = O (point at infinity), reject
6. Accept if r ≡ X.x  (mod n)
```

**Why does this work?**

```
X = u₁·G + u₂·K
  = (zw)·G + (rw)·(k·G)      [since K = k·G]
  = (zw + rwk)·G
  = w(z + rk)·G
  = (s⁻¹)(z + rk)·G
  = ℓ · G                     [since s = ℓ⁻¹(z + rk)  →  (z+rk)/s = ℓ]
  = R
```

So X.x = R.x = r. The verification equation holds exactly because the same point R that was used in signing is reconstructed from the public key.

### 8.4 Complete Python Implementation of ECDSA

```python
import hashlib
import os
import hmac

# ── secp256k1 parameters ─────────────────────────────────────────────
P  = 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFEFFFFFC2F
A  = 0
B  = 7
GX = 0x79BE667EF9DCBBAC55A06295CE870B07029BFCDB2DCE28D959F2815B16F81798
GY = 0x483ADA7726A3C4655DA4FBFC0E1108A8FD17B448A68554199C47D08FFB10D4B8
N  = 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFEBAAEDCE6AF48A03BBFD25E8CD0364141
G  = (GX, GY)
INF = None  # Point at infinity sentinel


def point_add(P1, P2):
    """Add two points on secp256k1."""
    if P1 is INF: return P2
    if P2 is INF: return P1
    x1, y1 = P1
    x2, y2 = P2
    if x1 == x2 and y1 != y2: return INF
    if P1 == P2:
        lam = (3 * x1 * x1 * pow(2 * y1, P - 2, P)) % P
    else:
        lam = ((y2 - y1) * pow(x2 - x1, P - 2, P)) % P
    x3 = (lam * lam - x1 - x2) % P
    y3 = (lam * (x1 - x3) - y1) % P
    return (x3, y3)


def scalar_mul(k, point):
    """Compute k * point using double-and-add."""
    result = INF
    addend = point
    while k:
        if k & 1:
            result = point_add(result, addend)
        addend = point_add(addend, addend)
        k >>= 1
    return result


def generate_keypair():
    """Generate a random private/public key pair."""
    while True:
        private_key = int.from_bytes(os.urandom(32), 'big')
        if 1 <= private_key < N:
            break
    public_key = scalar_mul(private_key, G)
    return private_key, public_key


# ── RFC 6979: Deterministic nonce generation ─────────────────────────

def rfc6979_nonce(private_key: int, z: int) -> int:
    """
    Deterministic nonce generation per RFC 6979.
    Eliminates the need for a random number generator during signing —
    prevents nonce reuse while keeping signatures deterministic.
    """
    k_bytes = private_key.to_bytes(32, 'big')
    z_bytes = z.to_bytes(32, 'big')
    V = b'\x01' * 32
    K = b'\x00' * 32
    K = hmac.new(K, V + b'\x00' + k_bytes + z_bytes, hashlib.sha256).digest()
    V = hmac.new(K, V, hashlib.sha256).digest()
    K = hmac.new(K, V + b'\x01' + k_bytes + z_bytes, hashlib.sha256).digest()
    V = hmac.new(K, V, hashlib.sha256).digest()
    while True:
        V = hmac.new(K, V, hashlib.sha256).digest()
        candidate = int.from_bytes(V, 'big')
        if 1 <= candidate < N:
            return candidate
        K = hmac.new(K, V + b'\x00', hashlib.sha256).digest()
        V = hmac.new(K, V, hashlib.sha256).digest()


# ── ECDSA Signing ─────────────────────────────────────────────────────

def ecdsa_sign(private_key: int, message: bytes) -> tuple:
    """
    Sign a message with a private key.
    Uses RFC 6979 deterministic nonce (no random number generation needed).
    Returns (r, s) — the DER-encodable signature components.
    """
    z = int.from_bytes(hashlib.sha256(message).digest(), 'big')
    nonce = rfc6979_nonce(private_key, z)
    R = scalar_mul(nonce, G)
    r = R[0] % N
    if r == 0:
        raise RuntimeError("r = 0, try again with different nonce")
    s = (pow(nonce, N - 2, N) * (z + r * private_key)) % N
    if s == 0:
        raise RuntimeError("s = 0, try again with different nonce")
    # Normalise s to low-S form (BIP 146: prevents signature malleability)
    if s > N // 2:
        s = N - s
    return (r, s)


# ── ECDSA Verification ────────────────────────────────────────────────

def ecdsa_verify(public_key: tuple, message: bytes, signature: tuple) -> bool:
    """
    Verify an ECDSA signature.
    Returns True if valid, False otherwise.
    """
    r, s = signature
    if not (1 <= r < N and 1 <= s < N):
        return False
    z = int.from_bytes(hashlib.sha256(message).digest(), 'big')
    w = pow(s, N - 2, N)         # s⁻¹ mod n
    u1 = (z * w) % N
    u2 = (r * w) % N
    X = point_add(scalar_mul(u1, G), scalar_mul(u2, public_key))
    if X is INF:
        return False
    return X[0] % N == r


# ── DER Encoding (how Bitcoin serialises signatures) ──────────────────

def encode_der(r: int, s: int) -> bytes:
    """Encode (r, s) in DER format as used in Bitcoin script."""
    def encode_int(n):
        b = n.to_bytes((n.bit_length() + 7) // 8, 'big')
        if b[0] & 0x80:        # prepend 0x00 if high bit set (positive integer)
            b = b'\x00' + b
        return bytes([0x02, len(b)]) + b
    r_bytes = encode_int(r)
    s_bytes = encode_int(s)
    contents = r_bytes + s_bytes
    return bytes([0x30, len(contents)]) + contents


# ── Demo ──────────────────────────────────────────────────────────────

if __name__ == "__main__":
    # Generate keys
    priv, pub = generate_keypair()
    print(f"Private key: {priv:064x}")
    print(f"Public key:  ({pub[0]:064x},\n              {pub[1]:064x})")

    # Sign a transaction hash
    tx_hash = b"Alice pays Bob 1 BTC"
    sig = ecdsa_sign(priv, tx_hash)
    print(f"\nSignature r: {sig[0]:064x}")
    print(f"Signature s: {sig[1]:064x}")

    # Verify
    valid = ecdsa_verify(pub, tx_hash, sig)
    print(f"\nSignature valid:     {valid}")

    # Wrong message fails
    tampered = ecdsa_verify(pub, b"Alice pays Bob 2 BTC", sig)
    print(f"Tampered msg valid:  {tampered}")

    # DER encoding
    der = encode_der(*sig)
    print(f"\nDER-encoded sig ({len(der)} bytes): {der.hex()}")
```

### 8.5 The Low-s Requirement (BIP 146)

For every valid signature (r, s), (r, N−s) is also a valid signature (since both give the same verification equation). This means every transaction has two valid signatures, enabling **signature malleability** — an attacker can change the transaction ID without invalidating the signature, confusing systems that track transactions by ID.

Bitcoin Core enforces the "low-s" rule since version 0.11.1: if s > n/2, replace s with n − s. Both forms are valid cryptographically; the low-s form is canonical.

### 8.6 Nonce Reuse: A Fatal Vulnerability

If the same nonce ℓ is used for two different messages z₁ and z₂:

```
s₁ = ℓ⁻¹(z₁ + r·k)  mod n
s₂ = ℓ⁻¹(z₂ + r·k)  mod n
```

Subtracting:

```
s₁ − s₂ = ℓ⁻¹(z₁ − z₂)  mod n
ℓ = (z₁ − z₂) / (s₁ − s₂)  mod n
k = (s₁·ℓ − z₁) / r  mod n   ← private key recovered!
```

This is exactly how the PlayStation 3's ECDSA private key was recovered (the console used a constant nonce), and how several Bitcoin exchange hacks occurred. RFC 6979 deterministic nonce generation (above) eliminates this risk.

---

## 9. Schnorr Signatures and Taproot

**BIP340** (Schnorr signatures), **BIP341** (Taproot), and **BIP342** (Tapscript) were activated at Bitcoin block 709,632 on 14 November 2021. Together they are Bitcoin's most significant cryptographic upgrade since the original release.

### 9.1 Why Schnorr?

Claus-Peter Schnorr invented Schnorr signatures in 1989 and held a patent until 2008 — the year Bitcoin launched. Because of the patent, Bitcoin's original designer chose ECDSA instead. With the patent expired, Schnorr became available.

Advantages over ECDSA:

|Property|ECDSA|Schnorr|
|---|---|---|
|Proof of security|Heuristic|Provably secure (random oracle)|
|Signature size|71–72 bytes (DER)|64 bytes (fixed)|
|Linear: k·sig(m₁) + sig(m₂)?|No|**Yes** → enables key/sig aggregation|
|Batch verification|No|**Yes** → ~30% faster block validation|
|Complexity|Higher|Lower|

### 9.2 Schnorr Signing (BIP340)

BIP340 uses a specific encoding called **x-only public keys** — only the x-coordinate of the public key is stored (32 bytes instead of 33), and the protocol implicitly uses the even-y root.

```
Private key: k  (integer in [1, n-1])
Public key:  P = k·G  (using the "even y" lift)

To sign message m (a 32-byte hash):
1. Choose nonce ℓ  (BIP340 uses: ℓ = HMAC(k, P, m) — deterministic)
2. R = ℓ·G
   If R.y is odd, set ℓ ← n − ℓ   (force even-y R)
3. Compute challenge: e = H_tagged("BIP0340/challenge", R.x || P.x || m) mod n
4. Signature: (R.x, s) where s = (ℓ + e·k) mod n
```

The 64-byte signature is just: `R.x (32 bytes) || s (32 bytes)`.

### 9.3 Schnorr Verification (BIP340)

```
Given: public key P (x-only, 32 bytes), message m, signature (r, s)
1. Lift P to a point: even-y point with x = P
2. e = H_tagged("BIP0340/challenge", r || P || m) mod n
3. Compute R' = s·G − e·P
4. Accept if R'.y is even AND R'.x = r
```

```python
import hashlib

def tagged_hash(tag: str, data: bytes) -> bytes:
    """BIP340 tagged hash: SHA256(SHA256(tag) || SHA256(tag) || data)."""
    tag_hash = hashlib.sha256(tag.encode()).digest()
    return hashlib.sha256(tag_hash + tag_hash + data).digest()


def schnorr_sign(private_key: int, message: bytes) -> bytes:
    """
    BIP340 Schnorr signature.
    Returns 64-byte signature: r (32 bytes) || s (32 bytes).
    """
    assert len(message) == 32, "BIP340 requires 32-byte message"

    # Compute public key
    P = scalar_mul(private_key, G)
    # Enforce even y on public key
    k = private_key if P[1] % 2 == 0 else N - private_key
    P = scalar_mul(k, G)

    # Deterministic nonce per BIP340
    rand = os.urandom(32)
    t = (k ^ int.from_bytes(tagged_hash("BIP0340/aux", rand), 'big')).to_bytes(32, 'big')
    nonce_hash = tagged_hash("BIP0340/nonce",
                             t + P[0].to_bytes(32, 'big') + message)
    ell = int.from_bytes(nonce_hash, 'big') % N

    R = scalar_mul(ell, G)
    if R[1] % 2 != 0:          # Enforce even y on R
        ell = N - ell
        R = scalar_mul(ell, G)

    # Challenge hash
    e_bytes = tagged_hash("BIP0340/challenge",
                          R[0].to_bytes(32, 'big') +
                          P[0].to_bytes(32, 'big') +
                          message)
    e = int.from_bytes(e_bytes, 'big') % N
    s = (ell + e * k) % N

    return R[0].to_bytes(32, 'big') + s.to_bytes(32, 'big')


def schnorr_verify(pubkey_x: int, message: bytes, sig: bytes) -> bool:
    """
    BIP340 Schnorr verification.
    pubkey_x: 32-byte integer (x-coordinate of public key)
    """
    assert len(message) == 32
    assert len(sig) == 64

    r = int.from_bytes(sig[:32], 'big')
    s = int.from_bytes(sig[32:], 'big')

    if r >= P or s >= N:
        return False

    # Lift x-only public key (choose even y)
    y_sq = (pow(pubkey_x, 3, P) + 7) % P
    y = pow(y_sq, (P + 1) // 4, P)
    if y % 2 != 0:
        y = P - y
    pub_point = (pubkey_x, y)

    e_bytes = tagged_hash("BIP0340/challenge",
                          r.to_bytes(32, 'big') +
                          pubkey_x.to_bytes(32, 'big') +
                          message)
    e = int.from_bytes(e_bytes, 'big') % N

    # R' = s·G - e·P
    R_candidate = point_add(scalar_mul(s, G),
                            scalar_mul(N - e, pub_point))
    if R_candidate is INF:
        return False
    return R_candidate[1] % 2 == 0 and R_candidate[0] == r
```

### 9.4 Key Aggregation: MuSig2

Schnorr's linearity enables **key aggregation**: Alice (key A) and Bob (key B) can jointly produce a 2-of-2 multisig that looks like a single-signer signature to an observer. This has profound implications:

- **Privacy:** Lightning channel funding transactions and multi-sig wallets look indistinguishable from single-sig.
- **Efficiency:** 10-of-10 multisig costs the same as 1-of-1 on-chain.
- **Fungibility:** Without visible multisig structure, outputs are harder to track.

**MuSig2** (BIP327) is the protocol:

```
1. All signers compute aggregate key:
   P_agg = H(P₁, P₂, ..., Pₙ, P₁) * P₁  +  H(P₁, P₂, ..., Pₙ, P₂) * P₂  +  ...

2. Each signer provides two nonces (R₁ᵢ, R₂ᵢ)

3. Aggregate nonce: R = R₁ + b*R₂  where b = H(R₁, R₂, P_agg, m)

4. Each signer produces partial sig sᵢ; aggregate sig s = Σ sᵢ

5. Result: a standard (R, s) Schnorr signature valid under P_agg
```

### 9.5 Taproot

Taproot is a smart contract mechanism built on top of Schnorr. A Taproot output commits to:

1. A **key path**: a single internal public key P (which may itself be an aggregated key)
2. A **script path**: a Merkle tree of spending conditions

```
Output key Q = P + H(P || Merkle_root) * G
```

Spending via the key path (the "happy path") reveals nothing about the script tree — it looks like any other Schnorr signature. Spending via a script path reveals only the specific script branch used, not the others. This is a **MAST** (Merkelised Alternative Script Trees) structure with a Schnorr facade.

---

## 10. Complete Python Implementations

This section consolidates all the components into a self-contained, runnable Bitcoin cryptography library.

```python
"""
bitcoin_ecc.py — Complete secp256k1 ECC for Bitcoin
All arithmetic from scratch; no external libraries required.
"""

import os
import hmac
import hashlib
import struct

# ════════════════════════════════════════════════════════════
# secp256k1 Parameters
# ════════════════════════════════════════════════════════════

P  = 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFEFFFFFC2F
A  = 0
B  = 7
GX = 0x79BE667EF9DCBBAC55A06295CE870B07029BFCDB2DCE28D959F2815B16F81798
GY = 0x483ADA7726A3C4655DA4FBFC0E1108A8FD17B448A68554199C47D08FFB10D4B8
N  = 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFEBAAEDCE6AF48A03BBFD25E8CD0364141
G  = (GX, GY)
INF = None


# ════════════════════════════════════════════════════════════
# Field Arithmetic (operations in GF(P))
# ════════════════════════════════════════════════════════════

def field_add(a, b):      return (a + b) % P
def field_sub(a, b):      return (a - b) % P
def field_mul(a, b):      return (a * b) % P
def field_inv(a):         return pow(a, P - 2, P)      # Fermat
def field_div(a, b):      return field_mul(a, field_inv(b))
def field_sqrt(a):        return pow(a, (P + 1) // 4, P)  # valid since P ≡ 3 (mod 4)
def field_is_sqr(a):      return pow(a, (P - 1) // 2, P) == 1


# ════════════════════════════════════════════════════════════
# Elliptic Curve Arithmetic (secp256k1)
# ════════════════════════════════════════════════════════════

def ec_neg(point):
    """Negate a point: (x, y) → (x, -y)."""
    if point is INF: return INF
    return (point[0], field_sub(0, point[1]))


def ec_add(P1, P2):
    """Add two curve points."""
    if P1 is INF: return P2
    if P2 is INF: return P1
    x1, y1 = P1
    x2, y2 = P2
    if x1 == x2:
        if y1 != y2: return INF         # P + (-P) = O
        if y1 == 0:  return INF         # tangent vertical
        # Doubling: λ = (3x²) / (2y)   [a=0 simplification]
        lam = field_div(field_mul(3, field_mul(x1, x1)),
                        field_mul(2, y1))
    else:
        # Addition: λ = (y₂ - y₁) / (x₂ - x₁)
        lam = field_div(field_sub(y2, y1), field_sub(x2, x1))
    x3 = field_sub(field_sub(field_mul(lam, lam), x1), x2)
    y3 = field_sub(field_mul(lam, field_sub(x1, x3)), y1)
    return (x3, y3)


def ec_mul(scalar, point):
    """
    Scalar multiplication using constant-time double-and-add.
    scalar: integer in [0, N)
    """
    scalar = scalar % N
    result = INF
    addend = point
    while scalar:
        if scalar & 1:
            result = ec_add(result, addend)
        addend = ec_add(addend, addend)
        scalar >>= 1
    return result


def ec_on_curve(point):
    """Check if a point is on secp256k1."""
    if point is INF: return True
    x, y = point
    return field_sub(field_mul(y, y),
                     field_add(field_mul(x, field_mul(x, x)), B)) == 0


def lift_x(x):
    """
    Lift an x-coordinate to a curve point, returning the even-y version.
    Used for Taproot x-only public keys (BIP340).
    """
    y_sq = (pow(x, 3, P) + B) % P
    if not field_is_sqr(y_sq):
        raise ValueError(f"x={x} has no point on secp256k1")
    y = field_sqrt(y_sq)
    return (x, y) if y % 2 == 0 else (x, P - y)


# ════════════════════════════════════════════════════════════
# Key Generation
# ════════════════════════════════════════════════════════════

def generate_privkey() -> int:
    """Generate a secure random private key in [1, N-1]."""
    while True:
        k = int.from_bytes(os.urandom(32), 'big')
        if 1 <= k < N:
            return k

def privkey_to_pubkey(privkey: int) -> tuple:
    return ec_mul(privkey, G)

def pubkey_to_bytes(point: tuple, compressed=True) -> bytes:
    x, y = point
    if compressed:
        prefix = b'\x02' if y % 2 == 0 else b'\x03'
        return prefix + x.to_bytes(32, 'big')
    return b'\x04' + x.to_bytes(32, 'big') + y.to_bytes(32, 'big')

def bytes_to_pubkey(data: bytes) -> tuple:
    prefix = data[0]
    x = int.from_bytes(data[1:33], 'big')
    if prefix == 0x04:
        y = int.from_bytes(data[33:65], 'big')
    else:
        y_sq = (pow(x, 3, P) + B) % P
        y = field_sqrt(y_sq)
        if (y % 2) != (prefix - 2):
            y = P - y
    return (x, y)


# ════════════════════════════════════════════════════════════
# Hashing Utilities
# ════════════════════════════════════════════════════════════

def hash256(data: bytes) -> bytes:
    """Bitcoin's double-SHA256."""
    return hashlib.sha256(hashlib.sha256(data).digest()).digest()

def hash160(data: bytes) -> bytes:
    """RIPEMD160(SHA256(data)) — used for addresses."""
    h = hashlib.sha256(data).digest()
    r = hashlib.new('ripemd160')
    r.update(h)
    return r.digest()

def tagged_hash(tag: str, data: bytes) -> bytes:
    """BIP340 tagged hash."""
    t = hashlib.sha256(tag.encode()).digest()
    return hashlib.sha256(t + t + data).digest()


# ════════════════════════════════════════════════════════════
# Address Generation
# ════════════════════════════════════════════════════════════

BASE58 = '123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz'

def base58check(payload: bytes) -> str:
    checksum = hash256(payload)[:4]
    data = payload + checksum
    n = int.from_bytes(data, 'big')
    result = []
    while n:
        n, r = divmod(n, 58)
        result.append(BASE58[r])
    leading = sum(1 for b in data if b == 0)
    return '1' * leading + ''.join(reversed(result))

def pubkey_to_p2pkh(pubkey_bytes: bytes, mainnet=True) -> str:
    """Pay-to-Public-Key-Hash address."""
    version = b'\x00' if mainnet else b'\x6f'
    return base58check(version + hash160(pubkey_bytes))

# Bech32 encoding for SegWit (P2WPKH)
BECH32_CHARSET = 'qpzry9x8gf2tvdw0s3jn54khce6mua7l'
BECH32_GENERATOR = [0x3b6a57b2, 0x26508e6d, 0x1ea119fa, 0x3d4233dd, 0x2a1462b3]

def bech32_polymod(values):
    c = 1
    for v in values:
        b = c >> 25
        c = ((c & 0x1ffffff) << 5) ^ v
        for i in range(5):
            c ^= BECH32_GENERATOR[i] if (b >> i) & 1 else 0
    return c

def bech32_hrp_expand(hrp):
    return [ord(x) >> 5 for x in hrp] + [0] + [ord(x) & 31 for x in hrp]

def bech32_encode(hrp, data):
    combined = data + [0, 0, 0, 0, 0, 0]
    checksum = bech32_polymod(bech32_hrp_expand(hrp) + combined) ^ 1
    return hrp + '1' + ''.join(BECH32_CHARSET[d] for d in data) + \
           ''.join(BECH32_CHARSET[(checksum >> 5 * (5 - i)) & 31] for i in range(6))

def convertbits(data, frombits, tobits, pad=True):
    acc, bits, ret, maxv = 0, 0, [], (1 << tobits) - 1
    for value in data:
        acc = ((acc << frombits) | value) & 0xFFFFFFFF
        bits += frombits
        while bits >= tobits:
            bits -= tobits
            ret.append((acc >> bits) & maxv)
    if pad and bits:
        ret.append((acc << (tobits - bits)) & maxv)
    return ret

def pubkey_to_p2wpkh(pubkey_bytes: bytes) -> str:
    """Native SegWit P2WPKH address (bc1q...)."""
    witness_program = hash160(pubkey_bytes)
    return bech32_encode('bc', [0] + convertbits(witness_program, 8, 5))


# ════════════════════════════════════════════════════════════
# RFC 6979 Deterministic Nonce Generation
# ════════════════════════════════════════════════════════════

def rfc6979_nonce(privkey: int, msg_hash: int) -> int:
    k_bytes = privkey.to_bytes(32, 'big')
    z_bytes = msg_hash.to_bytes(32, 'big')
    V = b'\x01' * 32
    K = b'\x00' * 32
    K = hmac.new(K, V + b'\x00' + k_bytes + z_bytes, hashlib.sha256).digest()
    V = hmac.new(K, V, hashlib.sha256).digest()
    K = hmac.new(K, V + b'\x01' + k_bytes + z_bytes, hashlib.sha256).digest()
    V = hmac.new(K, V, hashlib.sha256).digest()
    while True:
        V = hmac.new(K, V, hashlib.sha256).digest()
        c = int.from_bytes(V, 'big')
        if 1 <= c < N:
            return c
        K = hmac.new(K, V + b'\x00', hashlib.sha256).digest()
        V = hmac.new(K, V, hashlib.sha256).digest()


# ════════════════════════════════════════════════════════════
# ECDSA
# ════════════════════════════════════════════════════════════

def ecdsa_sign(privkey: int, msg: bytes) -> tuple:
    z = int.from_bytes(hash256(msg), 'big')
    ell = rfc6979_nonce(privkey, z)
    R = ec_mul(ell, G)
    r = R[0] % N
    s = pow(ell, N - 2, N) * (z + r * privkey) % N
    if s > N // 2: s = N - s   # low-s normalisation (BIP146)
    return r, s

def ecdsa_verify(pubkey: tuple, msg: bytes, sig: tuple) -> bool:
    r, s = sig
    if not (1 <= r < N and 1 <= s < N): return False
    z = int.from_bytes(hash256(msg), 'big')
    w = pow(s, N - 2, N)
    X = ec_add(ec_mul(z * w % N, G), ec_mul(r * w % N, pubkey))
    return X is not INF and X[0] % N == r

def ecdsa_to_der(r: int, s: int) -> bytes:
    def encode_int(v):
        b = v.to_bytes((v.bit_length() + 7) // 8, 'big')
        if b[0] & 0x80: b = b'\x00' + b
        return bytes([0x02, len(b)]) + b
    inner = encode_int(r) + encode_int(s)
    return bytes([0x30, len(inner)]) + inner


# ════════════════════════════════════════════════════════════
# Schnorr (BIP340)
# ════════════════════════════════════════════════════════════

def schnorr_sign(privkey: int, msg32: bytes) -> bytes:
    assert len(msg32) == 32
    pub = ec_mul(privkey, G)
    k = privkey if pub[1] % 2 == 0 else N - privkey
    pub = ec_mul(k, G)

    rand = tagged_hash("BIP0340/aux", os.urandom(32))
    t = (k ^ int.from_bytes(rand, 'big')).to_bytes(32, 'big')
    nonce_material = tagged_hash("BIP0340/nonce",
                                 t + pub[0].to_bytes(32, 'big') + msg32)
    ell = int.from_bytes(nonce_material, 'big') % N
    R = ec_mul(ell, G)
    if R[1] % 2 != 0:
        ell = N - ell
        R = ec_mul(ell, G)
    e = int.from_bytes(
        tagged_hash("BIP0340/challenge",
                    R[0].to_bytes(32, 'big') + pub[0].to_bytes(32, 'big') + msg32),
        'big') % N
    s = (ell + e * k) % N
    return R[0].to_bytes(32, 'big') + s.to_bytes(32, 'big')

def schnorr_verify(pubkey_x: int, msg32: bytes, sig64: bytes) -> bool:
    assert len(msg32) == 32 and len(sig64) == 64
    r_int = int.from_bytes(sig64[:32], 'big')
    s_int = int.from_bytes(sig64[32:], 'big')
    if r_int >= P or s_int >= N: return False
    pub = lift_x(pubkey_x)
    e = int.from_bytes(
        tagged_hash("BIP0340/challenge",
                    sig64[:32] + pubkey_x.to_bytes(32, 'big') + msg32),
        'big') % N
    R = ec_add(ec_mul(s_int, G), ec_mul(N - e, pub))
    if R is INF or R[1] % 2 != 0: return False
    return R[0] == r_int


# ════════════════════════════════════════════════════════════
# Demo
# ════════════════════════════════════════════════════════════

if __name__ == "__main__":
    print("=" * 60)
    print("  Bitcoin ECC Demo")
    print("=" * 60)

    # Key generation
    priv = generate_privkey()
    pub  = privkey_to_pubkey(priv)
    pub_bytes = pubkey_to_bytes(pub, compressed=True)

    print(f"\n[1] Private key:    {priv:064x}")
    print(f"    Public key (x): {pub[0]:064x}")
    print(f"    Public key (y): {pub[1]:064x}")

    # Addresses
    p2pkh  = pubkey_to_p2pkh(pub_bytes)
    p2wpkh = pubkey_to_p2wpkh(pub_bytes)
    print(f"\n[2] P2PKH address:  {p2pkh}")
    print(f"    P2WPKH address: {p2wpkh}")

    # ECDSA
    tx = b"Send 0.5 BTC to Bob"
    sig_ecdsa = ecdsa_sign(priv, tx)
    der = ecdsa_to_der(*sig_ecdsa)
    print(f"\n[3] ECDSA signature ({len(der)} bytes): {der.hex()[:40]}...")
    print(f"    Valid: {ecdsa_verify(pub, tx, sig_ecdsa)}")
    print(f"    Tamper fails: {not ecdsa_verify(pub, b'Send 1.0 BTC to Bob', sig_ecdsa)}")

    # Schnorr
    msg32 = hashlib.sha256(tx).digest()
    sig_schnorr = schnorr_sign(priv, msg32)
    print(f"\n[4] Schnorr signature (64 bytes): {sig_schnorr.hex()[:40]}...")
    print(f"    Valid: {schnorr_verify(pub[0], msg32, sig_schnorr)}")

    # Verify G has correct order (n*G = O)
    print(f"\n[5] n*G = O: {ec_mul(N, G) is INF}")
    print(f"    G on curve: {ec_on_curve(G)}")
    print(f"    Public key on curve: {ec_on_curve(pub)}")
```

---

## 11. Security Considerations and Attack Vectors

### 11.1 The Discrete Logarithm Problem

The security of Bitcoin's ECC rests entirely on the hardness of the **Elliptic Curve Discrete Logarithm Problem (ECDLP)**: given points P and Q = k·P on a secp256k1 curve with ~2²⁵⁶ points, find k.

The best known classical algorithm is **Pollard's rho** algorithm, which runs in O(√n) ≈ O(2¹²⁸) time. No sub-exponential algorithm is known for general elliptic curves (unlike integer factorisation, where the Number Field Sieve runs in sub-exponential time).

The 128-bit security level means an attacker performing 2¹²⁸ operations — with all of the world's current computing power running for millions of years — would have negligible probability of success.

### 11.2 Quantum Computing Threat (Shor's Algorithm)

**Shor's algorithm** (1994) solves ECDLP in polynomial time on a quantum computer. A sufficiently powerful quantum computer could:

1. Recover private keys from public keys
2. Break ECDSA and Schnorr signatures

**Current quantum threat to Bitcoin:**

- Addresses that have never been used (public key not yet revealed) are protected by hash functions (SHA256 + RIPEMD160), not ECC. Hash functions are broken by Grover's algorithm in O(√2²⁵⁶) = O(2¹²⁸) quantum operations — still secure.
- **Addresses that have been used** (public key visible in a spend transaction) are directly vulnerable if a quantum computer with sufficient qubits exists.
- Experts estimate a Grover-capable quantum computer would need ~2048 logical qubits and ~10⁸ error-corrected operations. As of 2025, no computer with more than ~1000 noisy qubits exists.
- The Bitcoin community is actively researching post-quantum signature schemes (lattice-based: CRYSTALS-Dilithium; hash-based: SPHINCS+).

### 11.3 Invalid Curve Attacks

When a public key point is not checked to be on the curve, an attacker can submit a point on a different (weaker) curve, potentially leaking information about the private key. Bitcoin implementations should always call `ec_on_curve(point)` before using any externally supplied public key.

### 11.4 Weak Random Number Generation

Every private key generation and ECDSA signing step requires high-quality randomness. Historical RNG failures include:

- **Android SecureRandom bug (2013):** Java's `SecureRandom` on Android was insufficiently seeded on many devices. Bitcoin wallets using it generated weak keys, leading to theft.
- **Dual_EC_DRBG backdoor (2013, NSA):** An NSA-designed PRNG with a suspected backdoor was standardised by NIST. Any implementation using it for key generation could be compromised.
- **ps3 nonce reuse:** PlayStation 3's signing code used a constant nonce ℓ = 0x2... across all signatures, instantly revealing the private key.

**Mitigation:** RFC 6979 deterministic nonce generation, used in the implementation above, eliminates the signing RNG entirely — the nonce is deterministically derived from the private key and message.

### 11.5 Side-Channel Attacks

Implementations that perform different computations for bit=0 vs bit=1 in the scalar multiplication loop leak the private key through timing, power consumption, or electromagnetic emissions. Countermeasures:

- **Constant-time scalar multiplication:** Always perform both the double and add (using dummy operations for 0-bits).
- **Point blinding:** Randomise the representation of points before multiplication.
- **Scalar blinding:** Compute (k + r·n)·G = k·G + r·(n·G) = k·G (since n·G = O) for a random r, preventing timing attacks on the scalar.

These are critical for hardware wallets but less relevant for software running on general-purpose CPUs.

### 11.6 The Birthday Paradox in ECDSA

Nonce values must be unique within a key's lifetime. If a key signs 2¹²⁸ messages with random nonces, there's a ~50% chance two messages share a nonce (birthday bound). Since n ≈ 2²⁵⁶, the birthday bound is reached at 2¹²⁸ messages — practically unreachable. RFC 6979 makes nonces deterministically unique by construction.

---

## 12. References and Further Reading

### 12.1 Books

**Mathematics and Cryptography Foundations:**

- **Silverman, J.H. (2009).** _The Arithmetic of Elliptic Curves_ (2nd ed.). Springer Graduate Texts in Mathematics. — The standard graduate textbook on the algebraic theory. Chapter V covers elliptic curves over finite fields; Chapter VIII covers elliptic curves and cryptography.
    
- **Washington, L.C. (2008).** _Elliptic Curves: Number Theory and Cryptography_ (2nd ed.). CRC Press. — More accessible than Silverman; includes explicit cryptographic applications including ElGamal and ECDSA.
    
- **Hoffstein, J., Pipher, J., & Silverman, J.H. (2014).** _An Introduction to Mathematical Cryptography_ (2nd ed.). Springer. — Chapter 6 covers elliptic curve cryptography from a practical perspective. Highly recommended for programmers.
    
- **Cohen, H., Frey, G., et al. (2006).** _Handbook of Elliptic and Hyperelliptic Curve Cryptography_. CRC Press. — Encyclopedic reference; covers implementation techniques, point counting, pairings, and every attack known at time of publication.
    
- **Blake, I., Seroussi, G., & Smart, N. (1999).** _Elliptic Curves in Cryptography_. Cambridge University Press. — Concise and rigorous; good for understanding the security foundations.
    

**Bitcoin-Specific:**

- **Antonopoulos, A.M. (2023).** _Mastering Bitcoin_ (3rd ed.). O'Reilly. — Chapter 4 covers keys and addresses in depth; Chapter 8 covers digital signatures. Free online: https://github.com/bitcoinbook/bitcoinbook
    
- **Song, J. (2019).** _Programming Bitcoin: Learn How to Program Bitcoin from Scratch_. O'Reilly. — Builds a Bitcoin library from scratch in Python, including full ECC, ECDSA, and transaction serialisation. Strongly recommended as a companion to this tutorial.
    
- **Lopp, J. (2016).** _Bitcoin and Lightning Network on Raspberry Pi_. Apress. — Practical, less theoretical.
    

**Abstract Algebra:**

- **Dummit, D.S., & Foote, R.M. (2003).** _Abstract Algebra_ (3rd ed.). Wiley. — Chapters 3, 13–14 cover groups, rings, fields, and Galois theory.
    
- **Ireland, K., & Rosen, M. (1990).** _A Classical Introduction to Modern Number Theory_ (2nd ed.). Springer. — Chapters 1–8 cover congruences, quadratic reciprocity, and the arithmetic foundations needed for ECC.
    

### 12.2 Foundational Papers

- **Koblitz, N. (1987).** "Elliptic curve cryptosystems." _Mathematics of Computation_, 48(177), 203–209. — One of two independent papers proposing ECC.
    
- **Miller, V.S. (1985/1986).** "Use of elliptic curves in cryptography." _Advances in Cryptology — CRYPTO '85_, LNCS 218, pp. 417–426. — The other founding paper of ECC.
    
- **Hasse, H. (1936).** "Zur Theorie der abstrakten elliptischen Funktionenkörper." _Journal für reine und angewandte Mathematik_, 175. — The original proof of Hasse's bound |#E − p − 1| ≤ 2√p.
    
- **Pohlig, S., & Hellman, M. (1978).** "An improved algorithm for computing logarithms over GF(p) and its cryptographic significance." _IEEE Transactions on Information Theory_, 24(1), 106–110. — The Pohlig-Hellman algorithm; explains why group order must have large prime factors.
    
- **Pollard, J.M. (1978).** "Monte Carlo methods for index computation mod p." _Mathematics of Computation_, 32(143), 918–924. — Pollard's rho algorithm; establishes the O(√n) lower bound for generic ECDLP.
    
- **Smart, N.P. (1999).** "The discrete logarithm problem on elliptic curves of trace one." _Journal of Cryptology_, 12(3), 193–196. — The anomalous attack; explains why n ≠ p is required.
    
- **Shor, P.W. (1994).** "Algorithms for quantum computation: Discrete logarithms and factoring." _Proceedings 35th Annual Symposium on Foundations of Computer Science_, pp. 124–134. — The quantum algorithm that threatens ECC.
    
- **Bernstein, D.J., & Lange, T. (2007).** "Faster addition and doubling on elliptic curves." _Advances in Cryptology — ASIACRYPT 2007_, LNCS 4833. — Modern constant-time formulae used in production implementations.
    
- **Nick, J., Ruffing, T., & Seurin, Y. (2021).** "MuSig2: Simple Two-Round Schnorr Multi-Signatures." _Advances in Cryptology — CRYPTO 2021_. https://eprint.iacr.org/2020/1261 — The protocol behind BIP327 key aggregation.
    

### 12.3 Bitcoin Improvement Proposals (BIPs)

All BIPs are publicly available at: https://github.com/bitcoin/bips

|BIP|Title|Relevance|
|---|---|---|
|BIP13|Address Format for Pay-to-Script-Hash|P2SH addresses (3...)|
|BIP16|Pay to Script Hash|Multisig and scripts|
|BIP32|Hierarchical Deterministic Wallets|HD key derivation|
|BIP39|Mnemonic code for HD wallets|12/24 word seed phrases|
|BIP62|Dealing with Malleability|Precursor to SegWit|
|BIP66|Strict DER Signatures|DER encoding enforcement|
|BIP141|Segregated Witness|SegWit; introduces witness|
|BIP143|Transaction Signing (SegWit v0)|Revised sighash algorithm|
|BIP146|Dealing with Signature Encoding Malleability|Low-s requirement|
|BIP173|Base32 address format (bech32)|bc1q... addresses|
|BIP327|MuSig2 Multi-Signature Protocol|Key/signature aggregation|
|BIP340|Schnorr Signatures for secp256k1|Schnorr signing/verifying|
|BIP341|Taproot: SegWit version 1 spending rules|Taproot MAST structure|
|BIP342|Validation of Taproot Scripts|Tapscript opcodes|
|BIP350|Bech32m address format|Taproot bc1p... addresses|

### 12.4 Academic Lecture Notes and Course Materials

- **Boneh, D., & Shoup, V.** _A Graduate Course in Applied Cryptography_, Chapters 15–16. Free: https://toc.cryptobook.us — Rigorous security proofs for ECDSA and Schnorr.
    
- **Costello, C. (2012).** _Pairings for Beginners_. https://static1.squarespace.com/static/5fdbb09f31d71c1227082339/t/5ff394720493bd28278889c6/1609798774687/PairingsForBeginners.pdf — Introduction to bilinear pairings, used in advanced protocols.
    
- **Bernstein, D.J., & Lange, T.** _Introduction to post-quantum cryptography_. https://pqcrypto.org/www.springer.com/us/book/9783540887010.html — Post-quantum replacements for ECC.
    
- **MIT 6.875 / 6.5620 Foundations of Cryptography** — Course materials at https://mit6875.github.io — Theoretical foundations with lecture notes.
    

### 12.5 Online Resources and Tools

**Interactive Learning:**

- **Andrea Corbellini's "Elliptic Curve Cryptography: A Gentle Introduction"** (2015) — Four-part blog series with interactive visualisations. https://andrea.corbellini.name/2015/05/17/elliptic-curve-cryptography-a-gentle-introduction/ — **Highly recommended as a visual companion to this tutorial.**
    
- **learnmeabitcoin.com** — Plain-English explanations of Bitcoin's cryptographic stack with worked examples. https://learnmeabitcoin.com
    
- **A Cryptography Primer — Dan Boneh (Coursera)** — https://www.coursera.org/learn/crypto — Free, covers symmetric and asymmetric cryptography; uses ECC as a case study.
    

**Tools and Libraries:**

- **SageMath** — A mathematics software system with excellent finite field and elliptic curve support. https://www.sagemath.org. Use `E = EllipticCurve(GF(p), [0, 7])` to experiment.
    
- **OpenSSL EC tools** — `openssl ecparam -name secp256k1 -genkey` generates a secp256k1 key pair from the command line.
    
- **Bitcoin Script debugger** — https://script.bitcoin.com — Shows P2PKH and P2WPKH unlocking scripts.
    
- **Blockchain explorers** — https://mempool.space — Shows raw transaction data including DER signatures.
    

**Standards Documents:**

- **SEC 2: Recommended Elliptic Curve Domain Parameters** (v2.0, 2010) — Certicom Research. https://www.secg.org/sec2-v2.pdf — The normative document defining secp256k1 and the full set of SECG curves.
    
- **RFC 6979** — _Deterministic Usage of the Digital Signature Algorithm (DSA) and Elliptic Curve Digital Signature Algorithm (ECDSA)_ — https://www.rfc-editor.org/rfc/rfc6979
    
- **FIPS 186-5** — _Digital Signature Standard (DSS)_ — https://csrc.nist.gov/publications/detail/fips/186/5/final — NIST's DSS standard; uses different NIST curves but defines the mathematical operations.
    
- **ANSI X9.62** — _Public Key Cryptography for the Financial Services Industry: The Elliptic Curve Digital Signature Algorithm (ECDSA)_ — The normative specification for ECDSA.
    

### 12.6 Source Code to Read

The most educational way to understand Bitcoin's cryptography is to read clean, well-commented implementations:

- **Bitcoin Core (C++):** `src/secp256k1/` — https://github.com/bitcoin/bitcoin/tree/master/src/secp256k1 — The production implementation used by every full node. Includes constant-time point multiplication, endomorphism optimisation, and batch verification.
    
- **python-ecdsa (Python):** https://github.com/tlsfuzzer/python-ecdsa — Pure-Python ECDSA; readable but not constant-time.
    
- **btclib (Python):** https://btclib.org — Pure-Python Bitcoin library covering ECC, ECDSA, Schnorr, BIP32, BIP39, and transaction parsing.
    
- **noble-secp256k1 (TypeScript/JavaScript):** https://github.com/paulmillr/noble-secp256k1 — Audited, constant-time, zero-dependency secp256k1 implementation. Excellent to read for modern techniques.
    
- **Programming Bitcoin (Python):** https://github.com/jimmysong/programmingbitcoin — Source code for Jimmy Song's book; complete, readable, test-driven.
    

---

_This tutorial covers the mathematical and cryptographic foundations of Bitcoin's security — from first principles in abstract algebra, through the geometry of elliptic curves, to the specific secp256k1 parameters and the ECDSA and Schnorr protocols that secure trillions of dollars in value. The Python implementations above are written for clarity and correctness, not production use; for production, use audited libraries such as `libsecp256k1` (C) or `noble-secp256k1` (JavaScript)._

---

> **Notation reference**
> 
> |Symbol|Meaning|
> |---|---|
> |GF(p)|Finite field with p elements (integers mod p)|
> |E(GF(p))|Elliptic curve points with coordinates in GF(p)|
> |n|Order of the generator point G (number of points in ⟨G⟩)|
> |k|Private key (scalar)|
> |K = k·G|Public key (curve point)|
> |ℓ|ECDSA/Schnorr nonce (ephemeral scalar)|
> |z|Message hash (32-byte integer)|
> |(r, s)|ECDSA signature pair|
> |O|Point at infinity (additive identity of the curve group)|
> |≡ (mod p)|Congruence modulo p|
> |a⁻¹|Modular multiplicative inverse of a|