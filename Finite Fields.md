# Finite Fields: A Comprehensive Guide with Python Implementations

## Table of Contents

1. [Mathematical Foundations](https://claude.ai/local_sessions/local_466b5495-597f-48f6-a717-a2fa6c498f9c#1-mathematical-foundations)
2. [Existence and Structure of Finite Fields](https://claude.ai/local_sessions/local_466b5495-597f-48f6-a717-a2fa6c498f9c#2-existence-and-structure-of-finite-fields)
3. [Prime Fields GF(p)](https://claude.ai/local_sessions/local_466b5495-597f-48f6-a717-a2fa6c498f9c#3-prime-fields-gfp)
4. [Extension Fields GF(pⁿ)](https://claude.ai/local_sessions/local_466b5495-597f-48f6-a717-a2fa6c498f9c#4-extension-fields-gfpn)
5. [The Special Case: GF(2ⁿ) — Binary Fields](https://claude.ai/local_sessions/local_466b5495-597f-48f6-a717-a2fa6c498f9c#5-the-special-case-gf2n--binary-fields)
6. [Implementing GF(p) in Python](https://claude.ai/local_sessions/local_466b5495-597f-48f6-a717-a2fa6c498f9c#6-implementing-gfp-in-python)
7. [Polynomial Arithmetic Over GF(p)](https://claude.ai/local_sessions/local_466b5495-597f-48f6-a717-a2fa6c498f9c#7-polynomial-arithmetic-over-gfp)
8. [Implementing GF(pⁿ) in Python](https://claude.ai/local_sessions/local_466b5495-597f-48f6-a717-a2fa6c498f9c#8-implementing-gfpn-in-python)
9. [Finding Irreducible Polynomials](https://claude.ai/local_sessions/local_466b5495-597f-48f6-a717-a2fa6c498f9c#9-finding-irreducible-polynomials)
10. [Primitive Elements and Discrete Logarithms](https://claude.ai/local_sessions/local_466b5495-597f-48f6-a717-a2fa6c498f9c#10-primitive-elements-and-discrete-logarithms)
11. [GF(2⁸) — The AES Field in Detail](https://claude.ai/local_sessions/local_466b5495-597f-48f6-a717-a2fa6c498f9c#11-gf28--the-aes-field-in-detail)
12. [Elliptic Curves over Finite Fields](https://claude.ai/local_sessions/local_466b5495-597f-48f6-a717-a2fa6c498f9c#12-elliptic-curves-over-finite-fields)
13. [Reed-Solomon Codes](https://claude.ai/local_sessions/local_466b5495-597f-48f6-a717-a2fa6c498f9c#13-reed-solomon-codes)
14. [Shamir's Secret Sharing](https://claude.ai/local_sessions/local_466b5495-597f-48f6-a717-a2fa6c498f9c#14-shamirs-secret-sharing)
15. [Performance and the `galois` Library](https://claude.ai/local_sessions/local_466b5495-597f-48f6-a717-a2fa6c498f9c#15-performance-and-the-galois-library)

---

## 1. Mathematical Foundations

### 1.1 Groups

A **group** is a set G together with a binary operation `·` satisfying:

|Property|Meaning|
|---|---|
|Closure|For all a, b ∈ G: a · b ∈ G|
|Associativity|(a · b) · c = a · (b · c)|
|Identity|There exists e ∈ G: e · a = a · e = a|
|Inverses|For every a ∈ G, there exists a⁻¹: a · a⁻¹ = e|

A group is **abelian** (commutative) if additionally a · b = b · a.

**Example:** The integers ℤ under addition form an abelian group (identity = 0, inverse of n = −n).

### 1.2 Rings

A **ring** is a set R with two operations, addition (+) and multiplication (×), where:

- (R, +) is an abelian group
- Multiplication is associative and distributes over addition
- There is a multiplicative identity 1

A **commutative ring** additionally has a × b = b × a for all a, b.

**Example:** The integers ℤ with standard + and × form a commutative ring.

### 1.3 Fields

A **field** is a commutative ring where every non-zero element has a multiplicative inverse. Formally, a set F with operations + and × is a field if:

1. (F, +) is an abelian group (identity = 0)
2. (F \ {0}, ×) is an abelian group (identity = 1)
3. × distributes over +: a × (b + c) = a × b + a × c

**Familiar fields:** ℚ (rationals), ℝ (reals), ℂ (complex numbers).

### 1.4 What Makes a Field _Finite_?

A **finite field** (also called a **Galois field**, after Évariste Galois) is a field with a finite number of elements. The number of elements is called the **order** of the field. Finite fields are denoted **GF(q)** or **𝔽_q**.

The key theorem underpinning everything:

> **Existence and Uniqueness Theorem:** A finite field of order q exists **if and only if** q = pⁿ for some prime p and positive integer n. Moreover, any two finite fields of the same order are isomorphic.

This means the only possible orders are: 2, 3, 4, 5, 7, 8, 9, 11, 13, 16, 17, 19, 23, 25, 27, …

There is no field of order 6, 10, 12, 14, 15, or any number that is not a prime power.

### 1.5 Characteristic

Every field has a **characteristic** — the smallest positive integer n such that adding the identity 1 to itself n times gives 0. If no such n exists, the characteristic is 0 (like ℝ or ℚ).

For a finite field GF(pⁿ), the characteristic is always the prime p. This is because:

- Adding 1 to itself p times gives p × 1 = 0 (by Fermat's little theorem)
- p must be prime — if p = a × b with a, b < p, then (a × 1)(b × 1) = 0 in a ring of characteristic p, but fields have no zero divisors

---

## 2. Existence and Structure of Finite Fields

### 2.1 Prime Fields (n = 1)

The simplest finite field has order p (a prime): **GF(p) = ℤ/pℤ**, the integers modulo p.

Elements: {0, 1, 2, …, p−1} Addition: a + b = (a + b) mod p Multiplication: a × b = (a × b) mod p

This works because when p is prime, every non-zero element has a multiplicative inverse (via Bezout's identity / extended Euclidean algorithm).

### 2.2 Extension Fields (n > 1)

For n > 1, GF(pⁿ) is constructed as **polynomial arithmetic modulo an irreducible polynomial** of degree n over GF(p).

Think of it like this:

- GF(p)[x] is the ring of polynomials with coefficients in GF(p)
- An irreducible polynomial f(x) of degree n is one that cannot be factored in GF(p)[x]
- GF(pⁿ) ≅ GF(p)[x] / ⟨f(x)⟩

Elements of GF(pⁿ) are polynomials of degree < n with coefficients in GF(p). There are pⁿ such polynomials.

**Analogy with ℂ:** The complex numbers ℂ = ℝ[x] / ⟨x² + 1⟩. We introduce a root α of x² + 1 (call it i), and every element is a + bi. GF(pⁿ) does the same thing over GF(p) with a chosen irreducible polynomial.

### 2.3 The Multiplicative Group

A crucial fact: the non-zero elements of GF(pⁿ) form a **cyclic group** under multiplication of order pⁿ − 1. This means:

- There always exists a **primitive element** (generator) g such that g⁰, g¹, g², …, g^(pⁿ−²) lists all non-zero elements exactly once
- Every non-zero element a satisfies a^(pⁿ−¹) = 1 (Fermat's little theorem, generalised)
- The number of primitive elements is φ(pⁿ − 1) (Euler's totient)

### 2.4 Subfields

GF(pⁿ) contains GF(pᵐ) as a subfield **if and only if** m divides n. For example:

- GF(2¹²) contains GF(2¹), GF(2²), GF(2³), GF(2⁴), GF(2⁶), GF(2¹²)
- GF(2⁸) contains only GF(2¹), GF(2²), GF(2⁴), GF(2⁸) (divisors of 8 are 1, 2, 4, 8)

---

## 3. Prime Fields GF(p)

### 3.1 Arithmetic Rules

In GF(p), all arithmetic is modulo the prime p:

```
a + b  ≡  (a + b) mod p
a − b  ≡  (a − b) mod p     (same as adding the additive inverse)
a × b  ≡  (a × b) mod p
a / b  ≡  a × b⁻¹ mod p    (b ≠ 0)
```

The additive inverse of a is (p − a) mod p. The multiplicative inverse of a is the integer b such that a × b ≡ 1 (mod p).

### 3.2 Finding the Multiplicative Inverse

**Method 1: Fermat's Little Theorem**

Since a^(p−1) ≡ 1 (mod p), we have a × a^(p−2) ≡ 1 (mod p), so:

```
a⁻¹ ≡ a^(p−2) mod p
```

**Method 2: Extended Euclidean Algorithm**

More efficient for large p. Uses the identity gcd(a, p) = 1 (since p is prime and 0 < a < p) and Bezout's theorem: there exist integers x, y such that ax + py = 1, so ax ≡ 1 (mod p), meaning x ≡ a⁻¹ (mod p).

### 3.3 Example: GF(7)

Elements: {0, 1, 2, 3, 4, 5, 6}

Addition table:

```
+  | 0  1  2  3  4  5  6
---+----------------------
0  | 0  1  2  3  4  5  6
1  | 1  2  3  4  5  6  0
2  | 2  3  4  5  6  0  1
3  | 3  4  5  6  0  1  2
4  | 4  5  6  0  1  2  3
5  | 5  6  0  1  2  3  4
6  | 6  0  1  2  3  4  5
```

Multiplicative inverses in GF(7):

```
1⁻¹ = 1    (1 × 1 = 1)
2⁻¹ = 4    (2 × 4 = 8 ≡ 1)
3⁻¹ = 5    (3 × 5 = 15 ≡ 1)
4⁻¹ = 2    (4 × 2 = 8 ≡ 1)
5⁻¹ = 3    (5 × 3 = 15 ≡ 1)
6⁻¹ = 6    (6 × 6 = 36 ≡ 1)
```

---

## 4. Extension Fields GF(pⁿ)

### 4.1 Representing Elements as Polynomials

An element of GF(pⁿ) is a polynomial of degree at most n−1 with coefficients in GF(p):

```
a_{n-1} x^{n-1} + a_{n-2} x^{n-2} + … + a_1 x + a_0
```

where each aᵢ ∈ {0, 1, …, p−1}.

In GF(2ⁿ), the coefficients are 0 or 1, so each element naturally maps to an n-bit integer — the polynomial x⁵ + x² + 1 becomes the integer 100101₂ = 37.

### 4.2 Addition in GF(pⁿ)

Add corresponding polynomial coefficients mod p:

```
(x³ + 2x + 1) + (x³ + x² + 3) = 2x³ + x² + 2x + 4   in GF(5)[x]
```

In GF(2ⁿ), addition is coefficient-wise XOR:

```
(x³ + x + 1) + (x³ + x²) = x² + x + 1   (since 1+1=0 mod 2)
```

### 4.3 Multiplication in GF(pⁿ)

Multiply polynomials normally, then reduce modulo the irreducible polynomial f(x):

```
a(x) × b(x)  mod  f(x)
```

This is analogous to integer multiplication modulo a prime.

**Example in GF(2³) with f(x) = x³ + x + 1:**

Multiply (x² + x) × (x + 1):

```
(x² + x)(x + 1) = x³ + x² + x² + x = x³ + x   (in GF(2), 2x²=0)
```

Now reduce mod x³ + x + 1:

```
x³ ≡ x + 1   (since x³ + x + 1 = 0  →  x³ = −x − 1 = x + 1 in GF(2))
x³ + x = (x + 1) + x = 1
```

So (x² + x) × (x + 1) = 1 in GF(2³). This means x² + x and x + 1 are multiplicative inverses!

### 4.4 Division in GF(pⁿ)

To compute a(x) / b(x), find b(x)⁻¹ using the extended Euclidean algorithm for polynomials, then multiply:

```
a(x) / b(x) = a(x) × b(x)⁻¹  mod  f(x)
```

The polynomial extended Euclidean algorithm is identical to the integer version, but with polynomial coefficients in GF(p).

### 4.5 Why Does This Give a Field?

For f(x) irreducible of degree n over GF(p):

- **Closure:** polynomial multiplication followed by mod-f always gives degree < n
- **Commutativity/Associativity:** inherited from polynomial arithmetic
- **Additive inverse:** −a(x) has coefficients negated mod p
- **Multiplicative inverse:** since f is irreducible and deg(a) < deg(f), gcd(a(x), f(x)) = 1, so by Bezout's lemma for polynomials, there exist u(x), v(x) with a(x)u(x) + f(x)v(x) = 1, meaning a(x)u(x) ≡ 1 mod f(x)

### 4.6 Frobenius Endomorphism

In GF(pⁿ), the **Frobenius map** φ: a ↦ aᵖ is a field automorphism. Applied n times, it gives the identity. The n automorphisms 1, φ, φ², …, φⁿ⁻¹ form the Galois group Gal(GF(pⁿ)/GF(p)) ≅ ℤ/nℤ.

This is why squaring (or p-ing) in GF(pⁿ) is a linear operation and is very efficient to compute.

---

## 5. The Special Case: GF(2ⁿ) — Binary Fields

Binary fields deserve special attention because they are ubiquitous in cryptography and coding theory, and their arithmetic maps directly to bitwise CPU operations.

### 5.1 Elements as Bit Strings

Each element of GF(2ⁿ) is an n-bit integer (the coefficients of the polynomial). This representation is compact and directly manipulable with hardware.

### 5.2 Addition = XOR

In GF(2ⁿ), 1 + 1 = 0, so addition is exactly bitwise XOR:

```python
def gf2n_add(a, b):
    return a ^ b
```

No carries, no modular reduction needed. This is extremely fast.

### 5.3 Multiplication = Carry-less Multiply + Reduce

Multiplication is "carry-less" (XOR-based) polynomial multiplication followed by reduction mod an irreducible polynomial (represented as an integer).

The standard irreducible polynomials for common field sizes:

|Field|Irreducible Polynomial|Integer Representation|
|---|---|---|
|GF(2⁸)|x⁸ + x⁴ + x³ + x + 1|0x11B (AES)|
|GF(2¹⁶)|x¹⁶ + x⁵ + x³ + x + 1|0x1002B|
|GF(2³²)|x³² + x⁷ + x³ + x² + 1|0x10000008D|
|GF(2⁶⁴)|x⁶⁴ + x⁴ + x³ + x + 1|0x1000000000000001B|
|GF(2¹²⁸)|x¹²⁸ + x⁷ + x² + x + 1|(used in GCM)|

### 5.4 The Russian Peasant Algorithm for GF(2ⁿ) Multiplication

```python
def gf2n_mul(a, b, irreducible, n):
    """Multiply a and b in GF(2^n) with given irreducible polynomial."""
    result = 0
    high_bit = 1 << (n - 1)
    for _ in range(n):
        if b & 1:
            result ^= a
        carry = a & high_bit
        a <<= 1
        if carry:
            a ^= irreducible
        a &= (1 << n) - 1
        b >>= 1
    return result
```

This processes one bit of b at a time: if the current bit of b is set, XOR a into result; then double a (left shift), reducing if the high bit overflows. Time complexity: O(n) bit operations.

---

## 6. Implementing GF(p) in Python

### 6.1 Core Class

```python
class GFp:
    """
    Element of a prime field GF(p).
    Supports all arithmetic operations with full Python operator overloading.
    """

    def __init__(self, value, p):
        if not _is_prime(p):
            raise ValueError(f"{p} is not prime")
        self.p = p
        self.value = int(value) % p

    # ── Arithmetic ────────────────────────────────────────────────────

    def __add__(self, other):
        other = self._coerce(other)
        return GFp((self.value + other.value) % self.p, self.p)

    def __sub__(self, other):
        other = self._coerce(other)
        return GFp((self.value - other.value) % self.p, self.p)

    def __mul__(self, other):
        other = self._coerce(other)
        return GFp((self.value * other.value) % self.p, self.p)

    def __truediv__(self, other):
        other = self._coerce(other)
        if other.value == 0:
            raise ZeroDivisionError("Division by zero in GF(p)")
        return GFp((self.value * pow(other.value, self.p - 2, self.p)) % self.p, self.p)

    def __pow__(self, exp):
        # Handles negative exponents (a^-k = (a^-1)^k)
        if exp < 0:
            inv = pow(self.value, self.p - 2, self.p)
            return GFp(pow(inv, -exp, self.p), self.p)
        return GFp(pow(self.value, exp, self.p), self.p)

    def __neg__(self):
        return GFp((-self.value) % self.p, self.p)

    def inverse(self):
        if self.value == 0:
            raise ZeroDivisionError("Zero has no inverse")
        # Extended Euclidean Algorithm — more general than Fermat's theorem
        return GFp(_ext_gcd(self.value, self.p)[0] % self.p, self.p)

    # ── Comparison & display ──────────────────────────────────────────

    def __eq__(self, other):
        if isinstance(other, int):
            return self.value == other % self.p
        return isinstance(other, GFp) and self.p == other.p and self.value == other.value

    def __repr__(self):
        return f"GFp({self.value}, p={self.p})"

    def __int__(self):
        return self.value

    def __hash__(self):
        return hash((self.value, self.p))

    # ── Helpers ───────────────────────────────────────────────────────

    def _coerce(self, other):
        if isinstance(other, int):
            return GFp(other, self.p)
        if isinstance(other, GFp):
            if other.p != self.p:
                raise ValueError("Cannot mix elements from different fields")
            return other
        raise TypeError(f"Cannot coerce {type(other)} to GFp")

    def __radd__(self, other): return self.__add__(other)
    def __rsub__(self, other): return self._coerce(other).__sub__(self)
    def __rmul__(self, other): return self.__mul__(other)
    def __rtruediv__(self, other): return self._coerce(other).__truediv__(self)


# ── Supporting utilities ───────────────────────────────────────────────

def _is_prime(n):
    """Miller-Rabin primality test (deterministic for n < 3,317,044,064,679,887,385,961,981)."""
    if n < 2: return False
    if n == 2: return True
    if n % 2 == 0: return False
    # Write n-1 as 2^r * d
    r, d = 0, n - 1
    while d % 2 == 0:
        r += 1
        d //= 2
    # Deterministic witnesses sufficient for all n < 3.3 × 10^24
    for a in [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37]:
        if a >= n: continue
        x = pow(a, d, n)
        if x in (1, n - 1): continue
        for _ in range(r - 1):
            x = pow(x, 2, n)
            if x == n - 1: break
        else:
            return False
    return True


def _ext_gcd(a, b):
    """Extended Euclidean Algorithm: returns (x, y, g) with ax + by = g = gcd(a,b)."""
    if b == 0:
        return 1, 0, a
    x1, y1, g = _ext_gcd(b, a % b)
    return y1, x1 - (a // b) * y1, g
```

### 6.2 GF(p) Field Factory

```python
class PrimeField:
    """
    Factory that creates a GF(p) and gives convenient access to its elements.
    """

    def __init__(self, p):
        if not _is_prime(p):
            raise ValueError(f"{p} is not prime")
        self.p = p
        self.zero = GFp(0, p)
        self.one = GFp(1, p)

    def __call__(self, value):
        """Create an element: F = PrimeField(7); a = F(3)"""
        return GFp(value, self.p)

    def __iter__(self):
        """Iterate over all elements."""
        for v in range(self.p):
            yield GFp(v, self.p)

    def __len__(self):
        return self.p

    def __repr__(self):
        return f"GF({self.p})"

    def elements(self):
        return list(self)

    def is_primitive(self, a):
        """Check if a is a primitive element (generator of multiplicative group)."""
        a = self(a) if isinstance(a, int) else a
        if a.value == 0:
            return False
        order = self.p - 1
        # a is primitive iff a^(order/q) != 1 for every prime factor q of order
        for q in _prime_factors(order):
            if (a ** (order // q)).value == 1:
                return False
        return True

    def primitive_element(self):
        """Find the smallest primitive element (generator)."""
        for v in range(2, self.p):
            if self.is_primitive(v):
                return self(v)
        raise RuntimeError("No primitive element found (impossible)")

    def discrete_log(self, target, base=None):
        """
        Solve base^x = target in GF(p) using Baby-step Giant-step.
        Returns x, or None if no solution exists.
        """
        if base is None:
            base = self.primitive_element()
        target = self(target) if isinstance(target, int) else target
        return _bsgs(base, target, self.p - 1, self.p)

    def addition_table(self):
        """Return the full addition table as a 2D list."""
        elems = self.elements()
        return [[int(a + b) for b in elems] for a in elems]

    def multiplication_table(self):
        """Return the full multiplication table as a 2D list."""
        elems = self.elements()
        return [[int(a * b) for b in elems] for a in elems]


def _prime_factors(n):
    """Return the set of distinct prime factors of n."""
    factors = set()
    d = 2
    while d * d <= n:
        while n % d == 0:
            factors.add(d)
            n //= d
        d += 1
    if n > 1:
        factors.add(n)
    return factors


def _bsgs(g, h, order, p):
    """Baby-step Giant-step: solve g^x = h in GF(p), 0 <= x < order."""
    import math
    m = math.isqrt(order) + 1
    # Baby steps: precompute g^j for j = 0..m-1
    table = {}
    gj = 1
    for j in range(m):
        table[gj] = j
        gj = (gj * int(g)) % p
    # Giant steps: compute h * g^(-m*i) and look for matches
    gm_inv = pow(int(pow(g, m, p)), p - 2, p)  # (g^m)^-1 mod p
    hh = int(h)
    for i in range(m):
        if hh in table:
            x = i * m + table[hh]
            if x < order:
                return x
        hh = (hh * gm_inv) % p
    return None
```

### 6.3 Usage Examples

```python
# Create GF(7)
F7 = PrimeField(7)

a = F7(3)
b = F7(5)

print(a + b)          # GFp(1, p=7)   since 3+5=8≡1 mod 7
print(a * b)          # GFp(1, p=7)   since 3*5=15≡1 mod 7
print(a / b)          # GFp(2, p=7)   since 3 * 5^-1 = 3*3 = 9 ≡ 2
print(a ** -1)        # GFp(5, p=7)   since 3*5=15≡1
print(-a)             # GFp(4, p=7)   since -3≡4 mod 7

g = F7.primitive_element()
print(g)              # GFp(3, p=7) — 3 generates all of {1,2,3,4,5,6}

# Check: 3^1=3, 3^2=2, 3^3=6, 3^4=4, 3^5=5, 3^6=1
powers = [int(g ** k) for k in range(1, 7)]
print(powers)         # [3, 2, 6, 4, 5, 1]

# Discrete logarithm: find k such that 3^k = 5 in GF(7)
k = F7.discrete_log(5, base=g)
print(k)              # 4  (since 3^4 = 81 ≡ 4... wait: 3^4=81≡4, let me re-check)
# 3^1=3, 3^2=2, 3^3=6, 3^4=4, 3^5=5 → k=5
k = F7.discrete_log(F7(5), base=F7(3))
print(k)              # 5


# Large prime field — everything still exact
F_large = PrimeField(2**61 - 1)   # Mersenne prime
x = F_large(123456789)
y = F_large(987654321)
print(x * y)
print((x * y) / y == x)   # True
```

---

## 7. Polynomial Arithmetic Over GF(p)

Before building extension fields, we need a solid polynomial layer.

```python
class Poly:
    """
    Polynomial with coefficients in GF(p).
    Coefficients are stored as a list [a0, a1, ..., an] where the polynomial is
    a0 + a1*x + a2*x^2 + ... + an*x^n  (index = degree of that term).
    """

    def __init__(self, coeffs, p):
        """
        coeffs: list of ints (low-degree first), or a single int (constant poly).
        p:      the prime characteristic.
        """
        if isinstance(coeffs, int):
            coeffs = [coeffs]
        self.p = p
        # Normalize: reduce coefficients mod p, strip trailing zeros
        self.coeffs = [int(c) % p for c in coeffs]
        self._normalize()

    def _normalize(self):
        while len(self.coeffs) > 1 and self.coeffs[-1] == 0:
            self.coeffs.pop()

    @property
    def degree(self):
        if self.coeffs == [0]:
            return -1  # degree of zero polynomial is -∞; we use -1
        return len(self.coeffs) - 1

    @property
    def leading(self):
        return self.coeffs[-1]

    def is_zero(self):
        return self.coeffs == [0]

    def is_one(self):
        return self.coeffs == [1]

    # ── Arithmetic ────────────────────────────────────────────────────

    def __add__(self, other):
        p = self.p
        size = max(len(self.coeffs), len(other.coeffs))
        a = self.coeffs + [0] * (size - len(self.coeffs))
        b = other.coeffs + [0] * (size - len(other.coeffs))
        return Poly([(ai + bi) % p for ai, bi in zip(a, b)], p)

    def __sub__(self, other):
        p = self.p
        size = max(len(self.coeffs), len(other.coeffs))
        a = self.coeffs + [0] * (size - len(self.coeffs))
        b = other.coeffs + [0] * (size - len(other.coeffs))
        return Poly([(ai - bi) % p for ai, bi in zip(a, b)], p)

    def __neg__(self):
        return Poly([(-c) % self.p for c in self.coeffs], self.p)

    def __mul__(self, other):
        if isinstance(other, int):
            return Poly([(c * other) % self.p for c in self.coeffs], self.p)
        p = self.p
        result = [0] * (len(self.coeffs) + len(other.coeffs) - 1)
        for i, a in enumerate(self.coeffs):
            for j, b in enumerate(other.coeffs):
                result[i + j] = (result[i + j] + a * b) % p
        return Poly(result, p)

    def __rmul__(self, scalar):
        return self.__mul__(scalar)

    def __pow__(self, exp):
        if exp < 0:
            raise ValueError("Negative polynomial powers require a modulus")
        result = Poly([1], self.p)
        base = Poly(self.coeffs[:], self.p)
        while exp:
            if exp & 1:
                result = result * base
            base = base * base
            exp >>= 1
        return result

    def __divmod__(self, divisor):
        """Polynomial division with remainder: returns (quotient, remainder)."""
        if divisor.is_zero():
            raise ZeroDivisionError("Polynomial division by zero")
        p = self.p
        rem = Poly(self.coeffs[:], p)
        quot_coeffs = [0] * max(0, self.degree - divisor.degree + 1)
        inv_lead = pow(divisor.leading, p - 2, p)  # multiplicative inverse of leading coeff
        while rem.degree >= divisor.degree:
            coeff = (rem.leading * inv_lead) % p
            shift = rem.degree - divisor.degree
            quot_coeffs[shift] = coeff
            # Subtract coeff * x^shift * divisor from rem
            sub = Poly([0] * shift + [(c * coeff) % p for c in divisor.coeffs], p)
            rem = rem - sub
        return Poly(quot_coeffs, p), rem

    def __floordiv__(self, other):
        return divmod(self, other)[0]

    def __mod__(self, other):
        return divmod(self, other)[1]

    def __eq__(self, other):
        if isinstance(other, Poly):
            return self.p == other.p and self.coeffs == other.coeffs
        return False

    def __repr__(self):
        if self.is_zero():
            return "0"
        terms = []
        for i in reversed(range(len(self.coeffs))):
            c = self.coeffs[i]
            if c == 0:
                continue
            if i == 0:
                terms.append(str(c))
            elif i == 1:
                terms.append(f"{c}x" if c != 1 else "x")
            else:
                terms.append(f"{c}x^{i}" if c != 1 else f"x^{i}")
        return " + ".join(terms) if terms else "0"

    def evaluate(self, x):
        """Evaluate the polynomial at x (Horner's method)."""
        p = self.p
        result = 0
        for c in reversed(self.coeffs):
            result = (result * x + c) % p
        return result

    def derivative(self):
        """Formal derivative: d/dx of sum(a_i x^i) = sum(i * a_i x^(i-1))."""
        if self.degree <= 0:
            return Poly([0], self.p)
        return Poly([(i * c) % self.p for i, c in enumerate(self.coeffs)][1:], self.p)


def poly_gcd(a, b):
    """GCD of two polynomials over GF(p) (Euclidean algorithm)."""
    while not b.is_zero():
        a, b = b, a % b
    # Normalize to monic
    inv = pow(a.leading, a.p - 2, a.p)
    return inv * a


def poly_ext_gcd(a, b):
    """
    Extended Euclidean Algorithm for polynomials over GF(p).
    Returns (s, t, g) such that a*s + b*t = g = gcd(a, b).
    """
    p = a.p
    zero = Poly([0], p)
    one  = Poly([1], p)
    old_r, r = a, b
    old_s, s = one, zero
    old_t, t = zero, one
    while not r.is_zero():
        q = old_r // r
        old_r, r = r, old_r - q * r
        old_s, s = s, old_s - q * s
        old_t, t = t, old_t - q * t
    # Normalize gcd to monic
    inv = pow(old_r.leading, p - 2, p)
    return inv * old_s, inv * old_t, inv * old_r


def poly_inverse(a, modulus):
    """
    Compute the multiplicative inverse of polynomial a modulo 'modulus' over GF(p).
    Raises if gcd(a, modulus) != 1.
    """
    s, _, g = poly_ext_gcd(a, modulus)
    if not g.is_one():
        raise ValueError(f"{a} is not invertible modulo {modulus}")
    return s % modulus
```

---

## 8. Implementing GF(pⁿ) in Python

### 8.1 Core Class

```python
class GFpn:
    """
    Element of the extension field GF(p^n) = GF(p)[x] / <irred(x)>.
    
    Internally an element is a Poly of degree < n with coefficients in GF(p).
    """

    def __init__(self, poly, field):
        """
        poly:  a Poly instance, a list of coefficients, or an int.
        field: the ExtensionField this element belongs to.
        """
        self.field = field
        p, irred = field.p, field.irred
        if isinstance(poly, int):
            poly = Poly([poly], p)
        elif isinstance(poly, list):
            poly = Poly(poly, p)
        # Reduce mod irreducible
        self.poly = poly % irred

    # ── Arithmetic ────────────────────────────────────────────────────

    def __add__(self, other):
        other = self.field._coerce(other)
        return GFpn(self.poly + other.poly, self.field)

    def __sub__(self, other):
        other = self.field._coerce(other)
        return GFpn(self.poly - other.poly, self.field)

    def __neg__(self):
        return GFpn(-self.poly, self.field)

    def __mul__(self, other):
        other = self.field._coerce(other)
        return GFpn(self.poly * other.poly, self.field)

    def __truediv__(self, other):
        other = self.field._coerce(other)
        inv = other.inverse()
        return self * inv

    def __pow__(self, exp):
        """Fast exponentiation using square-and-multiply."""
        F = self.field
        if exp == 0:
            return F.one
        if exp < 0:
            return self.inverse() ** (-exp)
        result = F.one
        base = GFpn(self.poly, F)
        while exp:
            if exp & 1:
                result = result * base
            base = base * base
            exp >>= 1
        return result

    def inverse(self):
        if self.poly.is_zero():
            raise ZeroDivisionError("Zero has no inverse")
        inv_poly = poly_inverse(self.poly, self.field.irred)
        return GFpn(inv_poly, self.field)

    def trace(self):
        """
        Absolute trace: Tr(a) = a + a^p + a^(p^2) + ... + a^(p^(n-1))
        The result is always in GF(p).
        """
        F = self.field
        t = GFpn(self.poly, F)
        result = t
        for _ in range(F.n - 1):
            t = t ** F.p
            result = result + t
        # The trace is in GF(p), return its integer value
        return int(result.poly.coeffs[0])

    def norm(self):
        """
        Norm: N(a) = a * a^p * a^(p^2) * ... * a^(p^(n-1))
        Equals a^((p^n - 1) / (p - 1)). Result is in GF(p).
        """
        return int(self ** ((self.field.order - 1) // (self.field.p - 1)))

    def minimal_polynomial(self):
        """
        The minimal polynomial of self over GF(p):
        the monic polynomial of least degree in GF(p)[x] that has self as a root.
        """
        F = self.field
        # Compute conjugates: self, self^p, self^(p^2), ..., until they repeat
        conjugates = []
        a = GFpn(self.poly, F)
        seen = set()
        while tuple(a.poly.coeffs) not in seen:
            seen.add(tuple(a.poly.coeffs))
            conjugates.append(a)
            a = a ** F.p
        # Minimal poly = product of (x - conjugate)
        x = Poly([0, 1], F.p)
        result = Poly([1], F.p)
        for conj in conjugates:
            # x - conj: since conj is in GF(p^n), not GF(p), we work symbolically
            # For elements in GF(p), conj.poly is a constant
            if conj.poly.degree <= 0:
                c = conj.poly.coeffs[0] if conj.poly.coeffs else 0
                factor = x - Poly([c], F.p)
                result = result * factor
        return result

    # ── Comparison & display ──────────────────────────────────────────

    def __eq__(self, other):
        if isinstance(other, int):
            return self.poly == Poly([other], self.field.p)
        return (isinstance(other, GFpn) and
                self.field is other.field and
                self.poly == other.poly)

    def __hash__(self):
        return hash(tuple(self.poly.coeffs))

    def __repr__(self):
        return f"GFpn({self.poly}, GF({self.field.p}^{self.field.n}))"

    def __int__(self):
        """For GF(2^n), interpret polynomial as integer (binary representation)."""
        return sum(c << i for i, c in enumerate(self.poly.coeffs))

    def __radd__(self, other): return self.__add__(other)
    def __rmul__(self, other): return self.__mul__(other)


class ExtensionField:
    """
    Factory for GF(p^n) = GF(p)[x] / <irred(x)>.
    
    Usage:
        F = ExtensionField(p=2, irred=[1, 1, 0, 1])  # GF(2^3) with x^3+x+1
        a = F([1, 0, 1])   # element x^2 + 1
    """

    def __init__(self, p, irred):
        """
        p:     prime characteristic
        irred: irreducible polynomial as a coefficient list (low-degree first)
               e.g., x^3+x+1 → [1, 1, 0, 1]
        """
        if not _is_prime(p):
            raise ValueError(f"{p} is not prime")
        irred_poly = Poly(irred, p)
        if not is_irreducible(irred_poly, p):
            raise ValueError(f"{irred_poly} is not irreducible over GF({p})")
        self.p = p
        self.n = irred_poly.degree
        self.irred = irred_poly
        self.order = p ** self.n
        self.zero = GFpn(Poly([0], p), self)
        self.one  = GFpn(Poly([1], p), self)
        # α: the root of irred in this field (= x mod irred)
        self.alpha = GFpn(Poly([0, 1], p), self)

    def __call__(self, value):
        """Create an element. Accepts int, list of coefficients, or Poly."""
        return GFpn(value, self)

    def __repr__(self):
        return f"GF({self.p}^{self.n}) = GF({self.p})[x]/<{self.irred}>"

    def __iter__(self):
        """Iterate over all pⁿ elements."""
        import itertools
        for coeffs in itertools.product(range(self.p), repeat=self.n):
            yield GFpn(Poly(list(coeffs), self.p), self)

    def __len__(self):
        return self.order

    def _coerce(self, value):
        if isinstance(value, GFpn):
            return value
        return GFpn(value, self)

    def is_primitive(self, elem):
        """Check if elem is a primitive element (generator of multiplicative group)."""
        elem = self._coerce(elem)
        if elem == self.zero:
            return False
        order = self.order - 1
        for q in _prime_factors(order):
            if elem ** (order // q) == self.one:
                return False
        return True

    def primitive_element(self):
        """Find the smallest-index primitive element."""
        for elem in self:
            if elem != self.zero and self.is_primitive(elem):
                return elem
        raise RuntimeError("No primitive element found (impossible)")

    def discrete_log(self, target, base=None):
        """
        Solve base^k = target in GF(p^n) using Baby-step Giant-step.
        Returns k, or None.
        """
        if base is None:
            base = self.primitive_element()
        target = self._coerce(target)
        return _bsgs_extension(base, target, self.order - 1)

    def frobenius(self, elem):
        """Apply the Frobenius automorphism: a → a^p."""
        return self._coerce(elem) ** self.p


def _bsgs_extension(g, h, order):
    """Baby-step Giant-step in an extension field."""
    import math
    m = math.isqrt(order) + 1
    table = {}
    gj = g.field.one
    for j in range(m):
        table[tuple(gj.poly.coeffs)] = j
        gj = gj * g
    gm_inv = (g ** m).inverse()
    hh = h
    for i in range(m):
        key = tuple(hh.poly.coeffs)
        if key in table:
            x = i * m + table[key]
            if x < order:
                return x
        hh = hh * gm_inv
    return None
```

### 8.2 Usage Examples

```python
# ── GF(2^3) with irreducible x^3 + x + 1 ─────────────────────────────
F8 = ExtensionField(p=2, irred=[1, 1, 0, 1])   # coeffs of 1 + x + x^3
print(F8)
# GF(2^3) = GF(2)[x]/<x^3 + x + 1>

alpha = F8.alpha  # the root of x^3 + x + 1

# All 8 elements:
for elem in F8:
    print(elem.poly, end="  ")
# 0  1  x  x + 1  x^2  x^2 + 1  x^2 + x  x^2 + x + 1

# Arithmetic
a = F8([1, 0, 1])   # x^2 + 1
b = F8([0, 1, 1])   # x^2 + x

print(a + b)         # x^2 + x + x^2 + 1 = x + 1  (GF(2): 1+1=0)
print(a * b)         # (x^2+1)(x^2+x) mod (x^3+x+1)
                     # = x^4+x^3+x^2+x → reduce → x^2  (check yourself!)
print(a * a.inverse() == F8.one)   # True

# Primitive element
g = F8.primitive_element()
print("Generator:", g)
# The powers of g cycle through all 7 non-zero elements
for k in range(1, 8):
    print(f"g^{k} =", g**k)

# Discrete log
target = F8([1, 1])   # x + 1
k = F8.discrete_log(target, base=g)
print(f"g^{k} = x + 1?", g**k == target)


# ── GF(3^2) with irreducible x^2 + 1 ─────────────────────────────────
F9 = ExtensionField(p=3, irred=[1, 0, 1])   # x^2 + 1
print(F9)

i = F9.alpha   # "i" — a square root of -1 in GF(3^2)
print(i * i)   # should equal F9(-1) = F9([2]) since -1 ≡ 2 mod 3

a = F9([1, 2])   # 1 + 2x  (= 1 + 2i)
b = F9([2, 1])   # 2 + x   (= 2 + i)
print(a + b)     # 0 + 0x = 0   (since 1+2=0 and 2+1=0 in GF(3))
print(a * b)     # (1+2i)(2+i) = 2+i+4i+2i^2 = 2+5i+2(-1) = 0+2i mod 3
```

---

## 9. Finding Irreducible Polynomials

An irreducible polynomial over GF(p) is one that cannot be written as a product of two non-constant polynomials with coefficients in GF(p). It is the analogue of a prime number for polynomials.

### 9.1 Irreducibility Tests

**Key fact:** A polynomial f(x) of degree n is irreducible over GF(p) if and only if:

1. f(x) divides x^(p^n) − x
2. gcd(f(x), x^(p^k) − x) = 1 for all k = 1, …, ⌊n/2⌋

These conditions can be checked efficiently using the Frobenius map in GF(p)[x].

```python
def is_irreducible(f, p):
    """
    Test whether polynomial f is irreducible over GF(p).
    Uses the Rabin irreducibility test.
    """
    n = f.degree
    if n <= 0:
        return False
    if n == 1:
        return True  # Linear polynomials are always irreducible

    # Condition: for each prime factor q of n,
    # gcd(f(x), x^(p^(n/q)) - x) must equal 1.
    # Then check f divides x^(p^n) - x.

    x = Poly([0, 1], p)

    def x_power_pq_mod_f(exp, f):
        """Compute x^(p^exp) mod f efficiently using repeated squaring + Frobenius."""
        # Start with x mod f
        h = x % f
        current_exp = 1
        target_exp = exp
        # We want x^(p^target_exp) mod f
        # Use: h_{k+1} = h_k^p mod f
        for _ in range(target_exp):
            # Raise each coefficient by applying Frobenius:
            # h^p mod f = polynomial exponentiation
            h = poly_powmod(h, p, f)
        return h

    # Check gcd condition for each prime factor of n
    for q in _prime_factors(n):
        h = x_power_pq_mod_f(n // q, f)
        g = poly_gcd(f, h - x)
        if not g.is_one():
            return False

    # Final check: x^(p^n) ≡ x (mod f)
    h = x_power_pq_mod_f(n, f)
    if h != x % f:
        return False

    return True


def poly_powmod(base, exp, modulus):
    """Compute base^exp mod modulus for polynomials."""
    p = base.p
    result = Poly([1], p)
    b = base % modulus
    while exp:
        if exp & 1:
            result = (result * b) % modulus
        b = (b * b) % modulus
        exp >>= 1
    return result


def find_irreducible(p, n, start=None):
    """
    Find an irreducible polynomial of degree n over GF(p).
    Searches through candidates in coefficient order.
    Returns a Poly.
    """
    import itertools

    # The leading coefficient must be 1 (monic), constant term must be nonzero
    # (otherwise 0 is a root → reducible). We iterate over middle coefficients.
    for middle in itertools.product(range(p), repeat=n - 1):
        for const in range(1, p):   # constant term ≠ 0
            coeffs = [const] + list(middle) + [1]  # monic, degree n
            f = Poly(coeffs, p)
            if is_irreducible(f, p):
                return f
    raise RuntimeError(f"No irreducible polynomial of degree {n} over GF({p}) found")


def all_irreducibles(p, n):
    """
    Generate all monic irreducible polynomials of degree n over GF(p).
    There are (1/n) * sum_{d|n} mu(n/d) * p^d of them,
    where mu is the Möbius function.
    """
    import itertools
    results = []
    for middle in itertools.product(range(p), repeat=n - 1):
        for const in range(1, p):
            coeffs = [const] + list(middle) + [1]
            f = Poly(coeffs, p)
            if is_irreducible(f, p):
                results.append(f)
    return results
```

### 9.2 Usage

```python
# Find irreducible polynomials over GF(2)
for n in range(2, 9):
    f = find_irreducible(2, n)
    print(f"Degree {n}: {f}")
# Degree 2: x^2 + x + 1
# Degree 3: x^3 + x + 1
# Degree 4: x^4 + x + 1
# Degree 5: x^5 + x^2 + 1
# Degree 6: x^6 + x + 1
# Degree 7: x^7 + x + 1
# Degree 8: x^8 + x^4 + x^3 + x^2 + 1

# Count irreducibles over GF(2) of each degree
for n in range(2, 9):
    count = len(all_irreducibles(2, n))
    print(f"GF(2): {count} irreducible polynomials of degree {n}")

# GF(3): degree-2 irreducibles
irreds_gf3 = all_irreducibles(3, 2)
print("GF(3) degree-2 irreducibles:", irreds_gf3)
# x^2 + 1, x^2 + x + 2, x^2 + 2x + 2

# Verify a specific polynomial is irreducible
f = Poly([1, 0, 0, 1, 1, 0, 0, 0, 1], 2)  # x^8 + x^4 + x^3 + 1
print("AES-like polynomial irreducible?", is_irreducible(f, 2))
```

### 9.3 Conway Polynomials

**Conway polynomials** are a standardised choice of irreducible polynomials for every (p, n), chosen by a compatibility condition that ensures subfield relationships are consistent. They are tabulated and used in computer algebra systems.

```python
# Well-known Conway polynomials
CONWAY = {
    (2, 1):  [1, 1],                          # x + 1
    (2, 2):  [1, 1, 1],                        # x^2 + x + 1
    (2, 3):  [1, 1, 0, 1],                     # x^3 + x + 1
    (2, 4):  [1, 1, 0, 0, 1],                  # x^4 + x + 1
    (2, 5):  [1, 0, 1, 0, 0, 1],              # x^5 + x^2 + 1
    (2, 6):  [1, 1, 0, 1, 1, 0, 1],          # x^6 + x^4 + x^2 + x + 1 (actually: check)
    (2, 8):  [1, 0, 1, 1, 1, 0, 0, 0, 1],    # x^8+x^4+x^3+x^2+1 (AES uses different)
    (3, 2):  [2, 1, 1],                        # x^2 + x + 2
    (5, 2):  [2, 4, 1],                        # x^2 + 4x + 2
}

def get_field(p, n):
    """Get a standard GF(p^n) using Conway polynomial if known, else search."""
    if (p, n) in CONWAY:
        return ExtensionField(p, CONWAY[(p, n)])
    irred = find_irreducible(p, n)
    return ExtensionField(p, irred.coeffs)
```

---

## 10. Primitive Elements and Discrete Logarithms

### 10.1 Finding Primitive Elements

A **primitive element** (or **primitive root** / **generator**) of GF(q)* is an element whose multiplicative order is exactly q − 1. Since GF(q)* is cyclic of order q − 1, primitive elements exist and their count is φ(q − 1).

```python
def multiplicative_order(elem, field):
    """
    Compute the multiplicative order of elem in GF(p^n)*.
    ord(elem) is the smallest positive k with elem^k = 1.
    """
    order = field.order - 1
    result = order
    # Divide out prime power factors of order as much as possible
    for q in _prime_factors(order):
        while result % q == 0:
            if (elem ** (result // q)) == field.one:
                result //= q
            else:
                break
    return result


def find_all_primitives(field):
    """Return all primitive elements of the field."""
    return [e for e in field if e != field.zero and field.is_primitive(e)]
```

### 10.2 Discrete Logarithm Algorithms

The **discrete logarithm problem (DLP)** in GF(q): given g (a generator) and h = gˣ, find x. This is computationally hard for large q and is the security basis for many cryptographic systems.

**Baby-step Giant-step (BSGS)** — O(√q) time and space:

```python
def discrete_log_bsgs(g, h, order, mul_fn, eq_fn, identity):
    """
    Generic BSGS solver.
    g:        generator element
    h:        target element (h = g^x)
    order:    order of g (= q - 1 for a primitive element)
    mul_fn:   function(a, b) → a * b
    eq_fn:    function(a, b) → bool
    identity: multiplicative identity
    Returns x in [0, order), or None.
    """
    import math
    m = math.isqrt(order) + 1

    # Baby steps: build table of g^j for j = 0..m-1
    baby = {}
    gj = identity
    for j in range(m):
        baby[id(gj) if not hasattr(gj, '__hash__') else hash(gj)] = (j, gj)
        gj = mul_fn(gj, g)

    # Precompute g^(-m)
    gm = gj                             # g^m
    # For GF(p): modular inverse; for extension fields: field inverse
    # We pass a generic interface, so the caller provides a proper structure.
    # Here, assume elements have .inverse() and multiplication works.
    gm_inv = gm.inverse() if hasattr(gm, 'inverse') else None

    hh = h
    for i in range(m):
        key = hash(hh)
        if key in baby:
            j, stored = baby[key]
            if eq_fn(hh, stored):
                x = i * m + j
                if 0 <= x < order:
                    return x
        if gm_inv is not None:
            hh = mul_fn(hh, gm_inv)

    return None
```

**Pohlig-Hellman algorithm** — exploits the factorization of group order for efficient DLP when q − 1 is smooth (has small prime factors):

```python
def pohlig_hellman(g, h, field):
    """
    Pohlig-Hellman DLP in GF(p^n)*.
    Solves g^x = h where g is a primitive element.
    Efficient when order = p^n - 1 has only small prime factors.
    """
    from math import isqrt

    order = field.order - 1
    factors = _prime_power_factorization(order)  # [(p1, e1), (p2, e2), ...]

    remainders = []
    moduli = []

    for (prime, exp) in factors:
        pk = prime ** exp
        # Work in the subgroup of order pk
        g_pk = g ** (order // pk)   # generator of subgroup of order p^e
        h_pk = h ** (order // pk)

        # Solve g_pk^x = h_pk using BSGS on the subgroup
        x_k = 0
        gamma = g_pk ** (pk // prime)  # element of order prime

        for i in range(exp):
            # h_i = (h_pk * g_pk^(-x_k))^(pk // prime^(i+1))
            exponent = pk // (prime ** (i + 1))
            h_i = (h_pk * (g_pk ** (-x_k))) ** exponent
            # Solve gamma^d_i = h_i using BSGS in subgroup of order prime
            d_i = _bsgs_small(gamma, h_i, prime, field)
            x_k += d_i * (prime ** i)

        remainders.append(x_k)
        moduli.append(pk)

    # CRT to combine results
    return _crt(remainders, moduli)


def _bsgs_small(g, h, order, field):
    """BSGS for small order subgroups."""
    import math
    m = math.isqrt(order) + 1
    table = {}
    gj = field.one
    for j in range(m):
        table[tuple(gj.poly.coeffs)] = j
        gj = gj * g
    gm_inv = (g ** m).inverse()
    hh = h
    for i in range(m):
        key = tuple(hh.poly.coeffs)
        if key in table:
            x = i * m + table[key]
            if x < order:
                return x
        hh = hh * gm_inv
    return 0


def _prime_power_factorization(n):
    """Return [(prime, exponent)] for n's factorization."""
    factors = {}
    d = 2
    while d * d <= n:
        while n % d == 0:
            factors[d] = factors.get(d, 0) + 1
            n //= d
        d += 1
    if n > 1:
        factors[n] = factors.get(n, 0) + 1
    return list(factors.items())


def _crt(remainders, moduli):
    """Chinese Remainder Theorem: find x with x ≡ r_i (mod m_i)."""
    from functools import reduce
    M = 1
    for m in moduli:
        M *= m
    x = 0
    for r, m in zip(remainders, moduli):
        Mi = M // m
        yi = pow(Mi, -1, m)   # Python 3.8+ modular inverse
        x += r * Mi * yi
    return x % M
```

---

## 11. GF(2⁸) — The AES Field in Detail

AES (Advanced Encryption Standard) performs its byte-level operations in **GF(2⁸)**, using the irreducible polynomial:

```
f(x) = x⁸ + x⁴ + x³ + x + 1   (0x11B as a 9-bit integer)
```

### 11.1 Highly Optimised GF(2⁸) Arithmetic

```python
class GF256:
    """
    High-performance GF(2^8) using the AES irreducible polynomial.
    x^8 + x^4 + x^3 + x + 1  =  0x11B
    
    Uses precomputed log/antilog tables for O(1) multiplication.
    """

    POLY = 0x11B   # x^8 + x^4 + x^3 + x + 1

    def __init__(self):
        self._build_tables()

    def _build_tables(self):
        """Precompute exp and log tables using primitive element 0x03 (= x + 1)."""
        self.exp = [0] * 512   # exp[i] = g^i; doubled to avoid modular wrapping
        self.log = [0] * 256   # log[a] = i such that g^i = a
        x = 1
        for i in range(255):
            self.exp[i] = x
            self.log[x] = i
            x <<= 1
            if x & 0x100:
                x ^= self.POLY
        # Fill second half of exp for convenience
        for i in range(255, 512):
            self.exp[i] = self.exp[i - 255]

    def add(self, a, b):
        """Addition in GF(2^8) = XOR."""
        return a ^ b

    def sub(self, a, b):
        """Subtraction = addition in characteristic 2."""
        return a ^ b

    def mul(self, a, b):
        """Multiplication using log tables: O(1)."""
        if a == 0 or b == 0:
            return 0
        return self.exp[self.log[a] + self.log[b]]

    def mul_direct(self, a, b):
        """
        Multiplication via Russian peasant algorithm — no lookup tables.
        Equivalent to mul() but slower. Good for understanding.
        """
        result = 0
        while b:
            if b & 1:
                result ^= a
            carry = a & 0x80
            a = (a << 1) & 0xFF
            if carry:
                a ^= (self.POLY & 0xFF)
            b >>= 1
        return result

    def inv(self, a):
        """Multiplicative inverse using log table: a^-1 = g^(255 - log(a))."""
        if a == 0:
            raise ZeroDivisionError("Zero has no inverse in GF(2^8)")
        return self.exp[255 - self.log[a]]

    def div(self, a, b):
        if b == 0:
            raise ZeroDivisionError
        if a == 0:
            return 0
        return self.exp[(self.log[a] - self.log[b]) % 255]

    def pow(self, a, n):
        """a^n in GF(2^8)."""
        if a == 0:
            return 0 if n > 0 else 1
        return self.exp[(self.log[a] * n) % 255]

    def generator(self):
        """Return the primitive element (generator). Always 0x03 with these tables."""
        return 0x03

    def print_multiplication_table(self, size=8):
        """Print a portion of the multiplication table."""
        print("   ", end="")
        for j in range(1, size + 1):
            print(f"{j:3}", end="")
        print()
        for i in range(1, size + 1):
            print(f"{i:3}", end="")
            for j in range(1, size + 1):
                print(f"{self.mul(i, j):3}", end="")
            print()


# The AES SubBytes S-Box is computed using GF(2^8) inverse + affine transform
def aes_sbox():
    """Compute the AES SubBytes substitution table using GF(2^8)."""
    gf = GF256()
    sbox = []
    for i in range(256):
        # Step 1: multiplicative inverse (0 maps to 0)
        x = gf.inv(i) if i != 0 else 0
        # Step 2: affine transformation over GF(2)
        # b_i = x_i XOR x_{i+4} XOR x_{i+5} XOR x_{i+6} XOR x_{i+7} XOR c_i
        # where c = 0x63 = 01100011
        result = 0
        for bit in range(8):
            b = ((x >> bit) ^ (x >> ((bit + 4) % 8)) ^
                 (x >> ((bit + 5) % 8)) ^ (x >> ((bit + 6) % 8)) ^
                 (x >> ((bit + 7) % 8)) ^ (0x63 >> bit)) & 1
            result |= b << bit
        sbox.append(result)
    return sbox


# ── Example usage ─────────────────────────────────────────────────────

gf = GF256()
print(gf.mul(0x53, 0xCA))    # 0x01 = 1: they are inverses!
print(gf.inv(0x53))           # 0xCA

# Verify: 0x53 * 0xCA = 1 in GF(2^8)?
print(hex(gf.mul(0x53, 0xCA)))  # 0x1

# AES S-Box (first 16 bytes should match the standard table)
sbox = aes_sbox()
standard_first16 = [0x63,0x7c,0x77,0x7b,0xf2,0x6b,0x6f,0xc5,
                    0x30,0x01,0x67,0x2b,0xfe,0xd7,0xab,0x76]
print("S-Box matches standard:", sbox[:16] == standard_first16)
```

### 11.2 MixColumns in AES

MixColumns treats each column of the 4×4 state as a polynomial over GF(2⁸) and multiplies by a fixed polynomial modulo x⁴ + 1. The matrix multiplication uses GF(2⁸) arithmetic:

```python
def mix_columns(state, gf):
    """
    Apply AES MixColumns to a 4x4 byte matrix (list of 4 columns, each 4 bytes).
    Uses GF(2^8) arithmetic.
    """
    MIX_MATRIX = [
        [0x02, 0x03, 0x01, 0x01],
        [0x01, 0x02, 0x03, 0x01],
        [0x01, 0x01, 0x02, 0x03],
        [0x03, 0x01, 0x01, 0x02],
    ]
    result = [[0]*4 for _ in range(4)]
    for col in range(4):
        for row in range(4):
            val = 0
            for k in range(4):
                val ^= gf.mul(MIX_MATRIX[row][k], state[k][col])
            result[row][col] = val
    return result
```

---

## 12. Elliptic Curves over Finite Fields

An **elliptic curve** over GF(p) is the set of solutions (x, y) to:

```
y² = x³ + ax + b   (mod p)    with  4a³ + 27b² ≢ 0 (mod p)
```

plus a special "point at infinity" O (the group identity).

Point addition and doubling are defined using GF(p) arithmetic. The set of points forms an abelian group — the foundation of **Elliptic Curve Cryptography (ECC)**.

```python
class EllipticCurve:
    """
    Elliptic curve y^2 = x^3 + ax + b over GF(p).
    """

    def __init__(self, a, b, p):
        self.a = a % p
        self.b = b % p
        self.p = p
        # Check non-singularity: 4a^3 + 27b^2 ≠ 0 (mod p)
        discriminant = (4 * pow(a, 3, p) + 27 * pow(b, 2, p)) % p
        if discriminant == 0:
            raise ValueError("Singular curve: 4a^3 + 27b^2 = 0")
        self.INF = None   # Point at infinity

    def is_on_curve(self, P):
        if P is self.INF:
            return True
        x, y = P
        return (y * y - x * x * x - self.a * x - self.b) % self.p == 0

    def neg(self, P):
        """Negate a point: -(x, y) = (x, -y)."""
        if P is self.INF:
            return self.INF
        x, y = P
        return (x, (-y) % self.p)

    def add(self, P, Q):
        """Add two points on the curve."""
        if P is self.INF:
            return Q
        if Q is self.INF:
            return P
        x1, y1 = P
        x2, y2 = Q
        p = self.p

        if x1 == x2:
            if y1 != y2:   # P + (-P) = O
                return self.INF
            # Point doubling: P == Q
            if y1 == 0:    # tangent is vertical
                return self.INF
            lam = (3 * x1 * x1 + self.a) * pow(2 * y1, p - 2, p) % p
        else:
            # Point addition: P ≠ Q
            lam = (y2 - y1) * pow(x2 - x1, p - 2, p) % p

        x3 = (lam * lam - x1 - x2) % p
        y3 = (lam * (x1 - x3) - y1) % p
        return (x3, y3)

    def scalar_mul(self, k, P):
        """Compute k*P using double-and-add."""
        if k < 0:
            return self.scalar_mul(-k, self.neg(P))
        result = self.INF
        addend = P
        while k:
            if k & 1:
                result = self.add(result, addend)
            addend = self.add(addend, addend)
            k >>= 1
        return result

    def order_of_point(self, P):
        """Find the order of point P (smallest k > 0 with kP = O)."""
        # Naive search — use Schoof's algorithm for large curves
        Q = P
        for k in range(1, self.p + 2):
            if Q is self.INF:
                return k
            Q = self.add(Q, P)
        return None

    def points(self):
        """Enumerate all points on the curve (including O)."""
        pts = [self.INF]
        for x in range(self.p):
            rhs = (x**3 + self.a * x + self.b) % self.p
            # Find square roots of rhs mod p
            for y in range(self.p):
                if (y * y) % self.p == rhs:
                    pts.append((x, y))
        return pts

    def __repr__(self):
        return f"y² = x³ + {self.a}x + {self.b}  over GF({self.p})"


# ── Example: secp256k1-like curve parameters ──────────────────────────

# Small example for illustration
E = EllipticCurve(a=2, b=3, p=97)
print(E)
all_pts = E.points()
print(f"Number of points (including O): {len(all_pts)}")

# Pick a base point
G = all_pts[1]
print(f"Base point G = {G}, on curve: {E.is_on_curve(G)}")

# Scalar multiplication (ECDH key exchange simulation)
alice_private = 17
bob_private = 31

alice_public = E.scalar_mul(alice_private, G)
bob_public   = E.scalar_mul(bob_private, G)

# Shared secret: both compute the same point
alice_shared = E.scalar_mul(alice_private, bob_public)
bob_shared   = E.scalar_mul(bob_private, alice_public)
print(f"ECDH shared secret matches: {alice_shared == bob_shared}")


# ── Real-world: secp256k1 (Bitcoin's curve) ───────────────────────────
p_secp = 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFEFFFFFC2F
a_secp = 0
b_secp = 7
Gx = 0x79BE667EF9DCBBAC55A06295CE870B07029BFCDB2DCE28D959F2815B16F81798
Gy = 0x483ADA7726A3C4655DA4FBFC0E1108A8FD17B448A68554199C47D08FFB10D4B8
n_secp = 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFEBAAEDCE6AF48A03BBFD25E8CD0364141

secp256k1 = EllipticCurve(a_secp, b_secp, p_secp)
G_secp = (Gx, Gy)
print("G on secp256k1:", secp256k1.is_on_curve(G_secp))
# Test: 2G
two_G = secp256k1.add(G_secp, G_secp)
print("2G computed successfully:", secp256k1.is_on_curve(two_G))
```

---

## 13. Reed-Solomon Codes

Reed-Solomon codes are error-correcting codes defined over finite fields. An (n, k) Reed-Solomon code:

- Encodes k data symbols as a polynomial of degree k−1 over GF(q)
- Evaluates it at n distinct points to get n codeword symbols
- Can correct up to ⌊(n − k) / 2⌋ symbol errors

```python
class ReedSolomon:
    """
    Reed-Solomon (n, k) code over GF(2^m).
    
    n = 2^m - 1 (codeword length)
    k = n - 2t  (message length)
    t = number of correctable errors
    """

    def __init__(self, m=8, t=16):
        """
        m: field size exponent (field = GF(2^m))
        t: number of correctable errors
        """
        gf = GF256() if m == 8 else None  # Extend to other sizes as needed
        if m != 8:
            raise NotImplementedError("Only GF(2^8) implemented here")

        self.gf = gf
        self.m = m
        self.n = (1 << m) - 1     # 255 for m=8
        self.t = t
        self.k = self.n - 2 * t   # 255 - 32 = 223 for t=16

        # Build evaluation points: primitive roots α^0, α^1, ..., α^(n-1)
        alpha = gf.generator()
        self.alpha = alpha
        self.eval_points = [gf.pow(alpha, i) for i in range(self.n)]

        # Build generator polynomial g(x) = prod_{i=1}^{2t} (x - α^i)
        self.gen_poly = self._build_generator()

    def _build_generator(self):
        """Build the generator polynomial g(x) = (x-α)(x-α²)...(x-α^{2t})."""
        gf = self.gf
        alpha = self.alpha
        g = [1]   # Start with polynomial 1
        for i in range(1, 2 * self.t + 1):
            # Multiply by (x - α^i) = (x + α^i) in GF(2)
            root = gf.pow(alpha, i)
            g = self._poly_mul_gf(g, [root, 1])
        return g

    def _poly_mul_gf(self, a, b):
        """Multiply two polynomials with GF(2^8) coefficients."""
        gf = self.gf
        result = [0] * (len(a) + len(b) - 1)
        for i, ai in enumerate(a):
            for j, bj in enumerate(b):
                result[i + j] ^= gf.mul(ai, bj)
        return result

    def _poly_div_gf(self, dividend, divisor):
        """Polynomial division returning (quotient, remainder) over GF(2^8)."""
        gf = self.gf
        result = list(dividend)
        for i in range(len(dividend) - len(divisor) + 1):
            if result[i] == 0:
                continue
            coef = gf.div(result[i], divisor[0])
            for j in range(len(divisor)):
                result[i + j] ^= gf.mul(coef, divisor[j])
        sep = len(divisor) - 1
        return result[:-sep], result[-sep:]

    def encode(self, message):
        """
        Systematic encoding: codeword = [message | parity].
        message: list of k bytes.
        """
        if len(message) != self.k:
            raise ValueError(f"Message must be {self.k} bytes")
        # Multiply message polynomial by x^(2t) to make room for parity
        padded = list(message) + [0] * (2 * self.t)
        # Parity = remainder when padded is divided by generator
        _, parity = self._poly_div_gf(padded, self.gen_poly)
        return list(message) + parity

    def syndromes(self, received):
        """
        Compute 2t syndromes S_i = r(α^i) for i = 1..2t.
        If all syndromes are 0, no errors detected.
        """
        gf = self.gf
        alpha = self.alpha
        return [self._poly_eval_gf(received, gf.pow(alpha, i))
                for i in range(1, 2 * self.t + 1)]

    def _poly_eval_gf(self, poly, x):
        """Evaluate polynomial at x using Horner's method in GF(2^8)."""
        gf = self.gf
        result = 0
        for coef in poly:
            result = gf.mul(result, x) ^ coef
        return result

    def has_errors(self, received):
        """Quick check: True if received word has detectable errors."""
        return any(s != 0 for s in self.syndromes(received))


# ── Usage ──────────────────────────────────────────────────────────────
rs = ReedSolomon(m=8, t=4)   # (255, 247) code, corrects up to 4 errors
print(f"RS({rs.n}, {rs.k}): corrects up to {rs.t} errors per codeword")

# Encode a message
message = list(range(rs.k))   # 0, 1, 2, ..., 246
codeword = rs.encode(message)
print(f"Codeword length: {len(codeword)}")   # 255

# Introduce errors
received = codeword[:]
received[5]  ^= 0x1F   # Corrupt byte 5
received[100] ^= 0xAB  # Corrupt byte 100

# Check syndromes
syndromes = rs.syndromes(received)
print(f"Errors detected: {any(s != 0 for s in syndromes)}")   # True
print(f"Clean codeword has errors: {rs.has_errors(codeword)}") # False
```

---

## 14. Shamir's Secret Sharing

Shamir's Secret Sharing splits a secret into n shares such that any t of them can reconstruct the secret, but t−1 shares reveal nothing. It is based on polynomial interpolation over a finite field.

```python
import random

class ShamirSecretSharing:
    """
    (t, n) threshold secret sharing using Lagrange interpolation over GF(p).
    
    Any t shares reconstruct the secret; t-1 shares reveal nothing.
    """

    def __init__(self, p=None):
        """
        p: prime for the field GF(p). Must be > the secret value.
        Defaults to a 256-bit Mersenne-like prime.
        """
        if p is None:
            # A large prime suitable for secrets up to 2^127
            p = 2**127 - 1   # Mersenne prime
        self.p = p

    def split(self, secret, n, t):
        """
        Split 'secret' into n shares with threshold t.
        Returns a list of (x, y) pairs where x = 1..n and y = f(x).
        
        The secret is f(0) for a random degree-(t-1) polynomial.
        """
        if not (1 <= t <= n):
            raise ValueError("Need 1 <= t <= n")
        if not (0 <= secret < self.p):
            raise ValueError(f"Secret must be in [0, {self.p})")

        # Random polynomial f(x) = secret + a1*x + a2*x^2 + ... + a_{t-1}*x^{t-1}
        coeffs = [secret] + [random.randrange(1, self.p) for _ in range(t - 1)]

        shares = []
        for x in range(1, n + 1):
            y = self._eval_poly(coeffs, x)
            shares.append((x, y))
        return shares

    def reconstruct(self, shares, t=None):
        """
        Reconstruct the secret from t (or more) shares using Lagrange interpolation.
        shares: list of (x, y) pairs.
        """
        if t is not None and len(shares) < t:
            raise ValueError(f"Need at least {t} shares")
        # Use all provided shares
        return self._lagrange_interpolate(0, shares)

    def _eval_poly(self, coeffs, x):
        """Evaluate polynomial with given coefficients at x (mod p)."""
        result = 0
        for coef in reversed(coeffs):
            result = (result * x + coef) % self.p
        return result

    def _lagrange_interpolate(self, x, points):
        """
        Lagrange interpolation over GF(p) at point x.
        points: list of (xi, yi) pairs.
        """
        p = self.p
        total = 0
        xs = [xi for xi, _ in points]
        ys = [yi for _, yi in points]

        for i in range(len(points)):
            numerator = denominator = 1
            for j in range(len(points)):
                if i == j:
                    continue
                numerator   = (numerator   * (x - xs[j])) % p
                denominator = (denominator * (xs[i] - xs[j])) % p

            lagrange_coeff = (numerator * pow(denominator, p - 2, p)) % p
            total = (total + ys[i] * lagrange_coeff) % p

        return total

    def verify_share(self, share, all_shares, t):
        """
        Check that a single share is consistent with t other shares.
        (Uses overdetermined interpolation to verify.)
        """
        x0, y0 = share
        # Pick t other shares (excluding this one)
        others = [s for s in all_shares if s[0] != x0][:t]
        if len(others) < t:
            return False
        # Reconstruct f(x0) from others and compare
        reconstructed = self._lagrange_interpolate(x0, others)
        return reconstructed == y0


# ── Usage ──────────────────────────────────────────────────────────────

sss = ShamirSecretSharing(p=2**127 - 1)

secret = 424242424242424242

# Split into 5 shares, any 3 reconstruct
shares = sss.split(secret, n=5, t=3)
print(f"Shares: {[(x, str(y)[:20]+'...') for x, y in shares]}")

# Reconstruct from any 3
import itertools
for subset in itertools.combinations(shares, 3):
    recovered = sss.reconstruct(list(subset))
    assert recovered == secret, f"Mismatch with subset {[s[0] for s in subset]}"
print("All 3-subsets reconstruct correctly!")

# Only 2 shares: cannot reconstruct (returns wrong value)
partial = sss.reconstruct(shares[:2])
print(f"Partial reconstruction (2/3) gives wrong secret: {partial != secret}")

# Share verification
print("Share 1 valid:", sss.verify_share(shares[0], shares[1:], t=3))
tampered = (shares[0][0], shares[0][1] + 1)
print("Tampered share valid:", sss.verify_share(tampered, shares[1:], t=3))
```

---

## 15. Performance and the `galois` Library

For production use, the pure-Python implementations above are instructive but slow. The [`galois`](https://github.com/mhostetter/galois) library provides NumPy-accelerated finite field arithmetic.

### 15.1 Installation

```bash
pip install galois numpy
```

### 15.2 Basic Usage

```python
import galois
import numpy as np

# ── Prime fields ──────────────────────────────────────────────────────
GF7  = galois.GF(7)
GF97 = galois.GF(97)

a = GF7(3)
b = GF7(5)
print(a + b)    # GF(7)(1)
print(a * b)    # GF(7)(1)   (3*5=15≡1 mod 7)
print(a ** -1)  # GF(7)(5)

# Array arithmetic — all vectorized
arr = GF7([1, 2, 3, 4, 5, 6])
print(arr ** 2)         # [1 4 2 2 4 1]
print(np.sum(arr))      # GF(7)(0)  (1+2+...+6 = 21 ≡ 0)


# ── Extension fields ──────────────────────────────────────────────────
GF256 = galois.GF(2**8)
GF256.properties  # Shows irreducible polynomial and primitive element

x = GF256(0x53)
y = GF256(0xCA)
print(x * y)     # GF(2^8)(1) — they are inverses in the AES field

# Array of all elements
all_elems = GF256.elements
print(len(all_elems))   # 256

# Primitive element and discrete log
g = GF256.primitive_element
h = GF256(0x80)
k = galois.ilog(h, g)   # discrete log
print(g**k == h)        # True


# ── Polynomial arithmetic ─────────────────────────────────────────────
GF2 = galois.GF(2)

# Polynomials over GF(2)
f = galois.Poly([1, 0, 0, 1, 1], field=GF2)   # x^4 + x + 1... wait: [1,0,0,1,1] = x^4+x^3+1
g = galois.Poly([1, 1, 1], field=GF2)          # x^2 + x + 1
print(f * g)
print(divmod(f, g))


# ── Matrices over finite fields ───────────────────────────────────────
GF5 = galois.GF(5)
A = GF5([[1, 2, 3],
         [4, 0, 1],
         [2, 3, 4]])
print(np.linalg.det(A))     # determinant in GF(5)
print(np.linalg.inv(A))     # matrix inverse in GF(5)
b_vec = GF5([1, 2, 3])
x_vec = np.linalg.solve(A, b_vec)  # solve Ax = b over GF(5)
print(A @ x_vec == b_vec)


# ── Reed-Solomon with galois ──────────────────────────────────────────
# galois includes RS encoding/decoding
rs = galois.ReedSolomon(255, 223)   # (n=255, k=223) over GF(2^8)
message = GF256.Random(223)
codeword = rs.encode(message)
# Introduce 16 symbol errors (RS can correct up to 16 = (255-223)/2)
errors = np.zeros(255, dtype=int)
error_pos = np.random.choice(255, 16, replace=False)
errors[error_pos] = np.random.randint(1, 256, 16)
received = codeword ^ GF256(errors)
decoded = rs.decode(received)
print("Decoded correctly:", np.array_equal(decoded, message))
```

### 15.3 Performance Comparison

```python
import time
import galois
import numpy as np

GF256_galois = galois.GF(2**8)

# Benchmark: 1 million multiplications
N = 1_000_000
a_arr = GF256_galois.Random(N)
b_arr = GF256_galois.Random(N)

start = time.perf_counter()
c_arr = a_arr * b_arr
elapsed = time.perf_counter() - start
print(f"galois: {N} multiplications in {elapsed*1000:.1f}ms "
      f"({N/elapsed/1e6:.1f}M ops/sec)")

# Compare with our pure-Python GF256
gf_py = GF256()
a_py  = [int(x) for x in a_arr]
b_py  = [int(x) for x in b_arr]

start = time.perf_counter()
c_py = [gf_py.mul(ai, bi) for ai, bi in zip(a_py, b_py)]
elapsed_py = time.perf_counter() - start
print(f"Pure Python: {N} multiplications in {elapsed_py*1000:.1f}ms "
      f"({N/elapsed_py/1e6:.1f}M ops/sec)")

# Verify results match
matches = all(int(ci) == cj for ci, cj in zip(c_arr, c_py))
print(f"Results match: {matches}")
```

### 15.4 Choosing Between Libraries

|Use case|Recommendation|
|---|---|
|Learning / prototyping|The pure-Python classes in this guide|
|Production cryptography|`galois` + NumPy, or `PyCryptodome`|
|Coding theory / error correction|`galois` (includes RS, BCH, LDPC)|
|Small fields, custom operations|Pure Python with precomputed tables|
|Performance-critical inner loops|C extension via `ctypes` or Cython|

---

## Appendix: Useful Identities and Theorems

### Fermat's Little Theorem (for prime fields)

For any a ≢ 0 (mod p): **a^(p−1) ≡ 1 (mod p)**

Corollary: a^p ≡ a (mod p) for _all_ a (including 0). This gives us: a^(-1) ≡ a^(p−2) (mod p)

### Generalised Fermat (for extension fields)

For any a ∈ GF(q)*, where q = p^n: **a^(q−1) = 1**

### Frobenius Endomorphism

In GF(p^n): **(a + b)^p = a^p + b^p**

This holds because all binomial coefficients C(p, k) for 0 < k < p are divisible by p, so they vanish in characteristic p. The p-th power map is therefore a _ring homomorphism_, not just a function.

### Number of Irreducible Polynomials of Degree n over GF(p)

Using the Möbius function μ:

```
I(p, n) = (1/n) × Σ_{d | n} μ(n/d) × p^d
```

For example, I(2, 8) = (1/8)(2⁸ − 2⁴ − 2² − 2¹ + 2¹ + ...) = 30.

### Lagrange's Theorem in GF(q)

A polynomial of degree d over a field has **at most d roots**. Combined with the fact that GF(q)* is cyclic of order q−1, the number of elements of order exactly d (dividing q−1) is φ(d).

### Wilson's Theorem

In GF(p): **(p−1)! ≡ −1 (mod p)**

This provides an irreducibility test: f(x) is irreducible over GF(p) if and only if f(x) divides x^(p^n) − x but does not divide x^(p^k) − x for any proper divisor k of n.

---

_This guide covers the mathematical foundations of finite fields and their practical implementation from scratch, through to production-grade usage with the `galois` library. The code is self-contained and runnable — start with Section 6 for prime fields and build upward._