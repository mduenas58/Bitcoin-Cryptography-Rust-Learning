# Programming Bitcoin

### Building Digital Money From Scratch — One Line of Code at a Time

_A developer-focused, TED-style talk (~30 min). Audience: engineers who can read Python and want to understand Bitcoin from first principles — not just use a library, but build the primitives themselves._

_Code snippets are Python 3, in the spirit of Jimmy Song's "Programming Bitcoin." Every slide includes a visual suggestion and speaker notes._

---

## ACT I — THE HOOK: WHY BUILD MONEY FROM SCRATCH?

---

### Slide 1 — Title

**PROGRAMMING BITCOIN** _Building digital money from scratch, one line of code at a time_

- Speaker name / handle
- "No frameworks. No `import bitcoin`. Just math and bytes."

**Visual:** Black background. A single blinking terminal cursor. As you speak, one line types itself: `>>> private_key = 0xdeadbeef...`

**Speaker note:** Open in silence. Let the cursor blink for three seconds before you say a word. The whole talk is a promise: by the end, that one line of code will mean something.

---

### Slide 2 — The Question That Started It All

> "Can two strangers, who will never meet and do not trust each other, agree on who owns what — without a referee?"

- Every payment system before 2009 answered: _no, you need a referee_ (a bank, Visa, PayPal).
- The referee is also a single point of failure, censorship, and control.
- Bitcoin's claim: the referee can be replaced by **math everyone can verify**.

**Visual:** Two figures on opposite cliffs, a chasm between them. A bank logo sits on a bridge in the middle — then dissolves into equations.

**Speaker note:** This is the emotional core. Frame it as a _trust_ problem, not a _money_ problem. Engineers feel trust problems in their bones — distributed systems, Byzantine generals.

---

### Slide 3 — The Double-Spend Problem

- A digital coin is just a number. Numbers can be copied.
- Email an attachment → you both have a copy. That's fine for cat photos. **Catastrophic for money.**
- If I can spend the same coin twice, the currency is worthless.
- Banks solve this with a private ledger they alone can edit. Bitcoin solves it with a **public ledger nobody can secretly edit.**

**Visual:** A `$10` file being copy-pasted into infinity (Ctrl+C / Ctrl+V), then a red "REJECTED" stamp.

**Speaker note:** Name the villain early. The entire architecture exists to defeat the double-spend. Keep coming back to it.

---

### Slide 4 — The Promise of This Talk

By the end, you'll understand — and could code — the four pillars:

1. **Finite fields** — the number system Bitcoin computes in
2. **Elliptic curves** — the trapdoor that makes keys possible
3. **Signatures** — proving ownership without revealing secrets
4. **Transactions & Script** — the language that moves the money

> "Bitcoin isn't magic. It's about 2,000 lines of ideas you already half-know."

**Visual:** Four stone blocks stacking into an arch labeled "BITCOIN." Remove any one and it collapses.

**Speaker note:** Set expectations. This is a build, not a tour. Promise that every abstraction will be opened up.

---

## ACT II — THE BUILDING BLOCKS

---

### Slide 5 — Why Not Just Use Regular Numbers?

- Cryptography needs operations that are **easy forward, infeasible backward** — and that **never round, never overflow, never leak**.
- Real numbers have infinities, rounding errors, and infinite precision. Useless for exact, reproducible, global agreement.
- The fix: do all math inside a **finite field** — a closed universe of integers where every machine on Earth computes the _exact_ same answer.

**Visual:** An infinite number line (ℝ) fading out vs. a tidy clock face labeled `0 … p-1`.

**Speaker note:** Motivate finite fields as an engineering requirement, not abstract algebra. "Determinism across 15,000 nodes" sells it.

---

### Slide 6 — Finite Fields: Clock Arithmetic

A finite field **F(p)** is the set `{0, 1, 2, …, p−1}` with all math done **mod p** (p prime).

- It's a clock. On a 12-hour clock, `11 + 3 = 2`. In F(7), `5 + 4 = 2`.
- "Finite" = exactly p elements. "Field" = `+`, `−`, `×`, `÷` all work and stay inside the set.
- Primality is the secret ingredient — it guarantees **division always works** (more in two slides).

```python
class FieldElement:
    def __init__(self, num, prime):
        if num >= prime or num < 0:
            raise ValueError(f"{num} not in field 0..{prime-1}")
        self.num, self.prime = num, prime

    def __add__(self, other):
        return FieldElement((self.num + other.num) % self.prime, self.prime)
```

**Visual:** A clock face for F(7); animate `5 + 4` wrapping past 7 to land on 2.

**Speaker note:** The clock metaphor is the load-bearing image of Act II. Reuse it.

---

### Slide 7 — The Magic of Prime Fields: Division

**Q: Why must p be prime?** Because it guarantees **every non-zero element has a multiplicative inverse** — so you can divide.

- If `gcd(a, p) = 1`, Bézout's identity gives `a·x + p·y = 1`, so `a·x ≡ 1 (mod p)`. That `x` is `a⁻¹`.
- When p is prime, _every_ non-zero `a` is coprime to p → _everything_ is invertible.
- Composite p breaks this: some elements share a factor and have no inverse.

```python
# Fermat's Little Theorem: a^(p-1) ≡ 1, so a^(p-2) ≡ a⁻¹
def __truediv__(self, other):
    inv = pow(other.num, self.prime - 2, self.prime)
    return FieldElement((self.num * inv) % self.prime, self.prime)
```

**Visual:** A combination lock; for a prime modulus every dial setting has exactly one "undo" turn.

**Speaker note:** This is the first "aha." Division existing at all is what lets point addition (Slide 11) work. Plant that seed now.

---

### Slide 8 — Elliptic Curves: A Strange-Looking Equation

The general short Weierstrass form:

> **y² = x³ + a·x + b**

- Despite the name, no ellipses involved — the name is historical baggage from elliptic integrals.
- It's just a curve. What matters is a bizarre, beautiful property: **you can "add" two points on it and get a third point on it.**

```python
class Point:
    def __init__(self, x, y, a, b):
        if y**2 != x**3 + a*x + b:        # point must be ON the curve
            raise ValueError(f"({x},{y}) is not on the curve")
        self.x, self.y, self.a, self.b = x, y, a, b
```

**Visual:** A smooth, symmetric curve over the reals — the classic elliptic curve silhouette, mirrored across the x-axis.

**Speaker note:** Don't apologize for the math. Tease the "adding points" idea as something almost magical you'll reveal next.

---

### Slide 9 — Bitcoin's Curve: secp256k1

Bitcoin doesn't use just any curve. It uses **secp256k1**:

> **y² = x³ + 7** (so a = 0, b = 7)

over the prime field with

> **p = 2²⁵⁶ − 2³² − 977**

- That `a = 0, b = 7` simplicity enables real implementation speedups.
- The field is staggeringly large: p ≈ 1.16 × 10⁷⁷ — comparable to the number of atoms in the observable universe.

```python
P = 2**256 - 2**32 - 977
A, B = 0, 7
# Curve points now live in F(p), not the smooth real curve.
```

**Visual:** Side-by-side: the pretty smooth curve (reals) vs. a scatter of disconnected dots (the curve over F(p)). Same equation, wildly different picture.

**Speaker note:** The reveal: over a finite field the curve isn't a curve at all — it's a cloud of points. The algebra still works; the geometry becomes intuition only.

---

### Slide 10 — Point Addition: The Chord-and-Tangent Trick

How do you "add" P + Q on an elliptic curve?

1. Draw a line through P and Q.
2. It hits the curve at exactly one third point.
3. Reflect that point over the x-axis. **That reflection is P + Q.**

- P + P (doubling)? Use the **tangent** line instead of a chord.
- Add a point to its mirror image → the line is vertical → you "fall off" the curve to the **point at infinity (O)**, the identity element.

**Visual:** Animated three-step: chord → intersection → reflection. Then a second animation for the tangent (doubling) case.

**Speaker note:** This is the showpiece visual of the talk. Slow down. Let the animation breathe. People remember the bouncing line.

---

### Slide 11 — Point Addition, In Code

For P = (x₁,y₁), Q = (x₂,y₂), the slope λ does all the work:

- **Different points:** `λ = (y₂ − y₁) / (x₂ − x₁)`
- **Doubling (P = Q):** `λ = (3x₁² + a) / (2y₁)`

Then: `x₃ = λ² − x₁ − x₂` and `y₃ = λ(x₁ − x₃) − y₁`.

```python
def __add__(self, other):
    if self.x == other.x and self.y != other.y:
        return Point(None, None, self.a, self.b)   # point at infinity
    if self.x != other.x:
        s = (other.y - self.y) / (other.x - self.x)
    else:                                          # doubling
        s = (3 * self.x**2 + self.a) / (2 * self.y)
    x3 = s**2 - self.x - other.x
    y3 = s * (self.x - x3) - self.y
    return Point(x3, y3, self.a, self.b)
```

> Notice the **division**. That's exactly why we needed a prime field (Slide 7). The pieces are clicking together.

**Visual:** Highlight the two `/` operators in red, with arrows back to Slide 7's inverse code.

**Speaker note:** Call out the callback explicitly. The audience should feel the architecture assembling.

---

### Slide 12 — Scalar Multiplication: Adding a Point to Itself

`k·P` means "add P to itself k times." This single operation is the heart of every Bitcoin key.

- Naively adding k times is impossible for huge k. Instead: **double-and-add** → only ~256 steps for a 256-bit k.

```python
def __rmul__(self, coefficient):
    coef = coefficient
    current = self
    result = Point(None, None, self.a, self.b)  # identity (infinity)
    while coef:
        if coef & 1:
            result += current        # add
        current += current           # double
        coef >>= 1
    return result
```

**Visual:** A staircase: "naive" = 2²⁵⁶ steps (a vertical wall to the moon) vs. "double-and-add" = 256 steps (a short flight). Dramatize the scale gap.

**Speaker note:** Forward direction is _fast_. Hold that thought — the next slide is the punchline.

---

### Slide 13 — The One-Way Door (ECDLP)

`k·P` is easy to compute. Going backward — finding `k` from `P` and `Q = k·P` — is the **Elliptic Curve Discrete Logarithm Problem**, and it is _infeasible._

- No structure links the output's position to the size of k. The points scatter unpredictably across the field.
- Best known attack ≈ √n steps. For secp256k1, n ≈ 2²⁵⁶, so √n ≈ **2¹²⁸ operations** — beyond all the computers that will ever exist.
- **This asymmetry IS the security.** Easy forward, impossible backward.

|Direction|Operation|Cost|
|---|---|---|
|Forward|k·P (sign / make key)|~256 steps|
|Backward|recover k (break key)|~2¹²⁸ steps|

**Visual:** A revolving door labeled "EASY →" on one side and "🚫 ∞" on the way back.

**Speaker note:** The trapdoor. This is the whole reason a public key can be public. Land it hard, then pause.

---

### Slide 14 — Keys, At Last

Now the title-slide line means something:

- **Private key** = a secret number `e` (just a 256-bit integer).
- **Public key** = the point `P = e·G`, where **G** is a fixed, agreed-upon **generator point** on secp256k1.
- Anyone can compute P from e. **Nobody** can compute e from P. (Slide 13.)

```python
G = S256Point(Gx, Gy)        # the famous generator, baked into the protocol
e = 0xdeadbeef_cafe_...      # private key — keep this secret forever
P = e * G                    # public key — share freely
```

**Visual:** The Slide 1 terminal line reappears — now annotated: `e` glows red ("SECRET"), `P` glows green ("PUBLIC").

**Speaker note:** Payoff moment. Explicitly say "Remember slide one?" and bring the cursor back. The room should feel the loop close.

---

### Slide 15 — Signatures: Proving You Know a Secret Without Revealing It

ECDSA lets you prove "I know `e`" without ever showing `e`.

- **Sign** a message hash `z` with private key `e` → produces `(r, s)`.
- **Verify** with public key `P`, `z`, and `(r, s)` → true/false. No secret exposed.

```python
def sign(self, z):
    k = deterministic_k(z)          # RFC 6979: never reuse k!
    r = (k * G).x.num
    k_inv = pow(k, N - 2, N)
    s = (z + r * self.secret) * k_inv % N
    return Signature(r, s)
```

**Visual:** A wax seal pressed onto an envelope. The seal proves the sender owns the signet ring — without handing over the ring.

**Speaker note:** Cryptographic signatures are the most underappreciated idea in computing. Sell the wonder: _prove knowledge without disclosure._

---

### Slide 16 — The Catastrophe of a Reused Nonce

That `k` in the signature? Use it twice and you leak the private key.

- Two signatures with the same `k` → solve two equations, two unknowns → recover `e`. Game over.
- This is not theoretical: the **2010 PlayStation 3 (Sony ECDSA) hack** broke the console's signing key this exact way.
- Fix: **RFC 6979** — derive `k` deterministically from the message and key. No randomness to get wrong.

**Visual:** A split screen: "k reused" → a vault door swinging wide open; "RFC 6979" → the door welded shut.

**Speaker note:** Engineers love a war story. The PS3 hack makes the abstract danger concrete and memorable.

---

## ACT III — ASSEMBLING THE MONEY

---

### Slide 17 — From Numbers to Bytes: Serialization

A public key is a point `(x, y)`. To put it on the wire (or in a transaction), you serialize it.

- **Uncompressed SEC:** `04 || x || y` → 65 bytes.
- **Compressed SEC:** `02/03 || x` → 33 bytes. (y is recoverable: the curve gives two y's; one byte says which.)
- Compression saves ~32 bytes _per key_ — at Bitcoin's scale, gigabytes of chain space.

```python
def sec(self, compressed=True):
    if compressed:
        prefix = b'\x02' if self.y.num % 2 == 0 else b'\x03'
        return prefix + self.x.num.to_bytes(32, 'big')
    return b'\x04' + self.x.num.to_bytes(32,'big') + self.y.num.to_bytes(32,'big')
```

**Visual:** A 65-byte bar shrinking to a 33-byte bar; a tiny "½ y discarded, recomputed on demand" tag.

**Speaker note:** Serialization is where pure math meets the messy real protocol. Keep momentum — these are short, satisfying wins.

---

### Slide 18 — From Public Key to Bitcoin Address

An address is a public key, hashed and human-proofed.

1. `HASH160(pubkey)` = RIPEMD160(SHA256(pubkey)) → 20 bytes.
2. Prepend a network byte, append a 4-byte checksum (double-SHA256).
3. **Base58Check** encode → the `1...` address you recognize.

- Hashing shrinks 33 bytes → 20 and adds a quantum-resistance hedge (the pubkey stays hidden until you spend).
- The checksum means a typo'd address is rejected, not sent into the void.

```python
def address(self, compressed=True, testnet=False):
    h160 = hash160(self.sec(compressed))
    prefix = b'\x6f' if testnet else b'\x00'
    return encode_base58_checksum(prefix + h160)
```

**Visual:** A pipeline diagram: pubkey → SHA256 → RIPEMD160 → +checksum → Base58 → `1A1zP1eP...`.

**Speaker note:** This is the layer users actually see. Connect it back: "that string in your wallet is just `e·G`, hashed and dressed up."

---

### Slide 19 — What a Transaction Actually Is

A Bitcoin transaction is not "send $10 to Bob." It's a data structure:

- **Inputs:** pointers to previous outputs you're spending (+ unlocking proof).
- **Outputs:** new locked boxes, each with an amount and a lock.
- **Version, locktime:** housekeeping.

> **Coins don't move. Outputs get consumed and new outputs get created.** A bitcoin is just an _unspent transaction output_ (UTXO) you can unlock.

```
tx
├── version
├── inputs[]   → (prev_tx_id, index, scriptSig, sequence)
├── outputs[]  → (amount, scriptPubKey)
└── locktime
```

**Visual:** Chain of boxes: outputs feeding into inputs feeding into new outputs. No coins ever "travel" — boxes get unlocked and re-created.

**Speaker note:** This reframes everyone's mental model. The UTXO insight is the single biggest "I finally get it" moment for developers.

---

### Slide 20 — The Anatomy, In Bytes

Every transaction is parsed and serialized field-by-field. No JSON, no schema server — just a precise byte layout every node agrees on.

```python
class Tx:
    def __init__(self, version, tx_ins, tx_outs, locktime):
        self.version  = version
        self.tx_ins   = tx_ins      # list of TxIn
        self.tx_outs  = tx_outs     # list of TxOut
        self.locktime = locktime

    @classmethod
    def parse(cls, stream):
        version = little_endian_to_int(stream.read(4))
        num_inputs = read_varint(stream)
        inputs = [TxIn.parse(stream) for _ in range(num_inputs)]
        ...
```

- Amounts are in **satoshis** (1 BTC = 100,000,000 sats). Integers only — no floats anywhere near money.
- Multi-byte counts use **varints**; numbers are **little-endian**. Details matter: one wrong byte = invalid tx.

**Visual:** A hex dump of a real raw transaction with colored field boundaries (version / input count / inputs / outputs / locktime).

**Speaker note:** Show a real hex blob. Engineers trust what they can see on the wire. "This is the whole truth — everything else is interpretation."

---

### Slide 21 — Fees: The Invisible Rule

> **Fee = sum(inputs) − sum(outputs).** Whatever you don't assign to an output, the miner keeps.

- There is no explicit "fee" field. It's implicit — and unforgiving.
- Forget an input, or fat-finger an output amount, and you can **burn a fortune** as fees. (It has happened — multi-BTC fees by accident.)
- Fees are how the network prioritizes you and, long-term, how miners get paid as the block subsidy halves toward zero.

**Visual:** A scale: inputs on the left pan, outputs on the right; the gap is labeled "→ miner." A cautionary "💸 oops" if the gap is huge.

**Speaker note:** The implicit-fee design surprises people. It's a great example of Bitcoin's "the rules are math, and math doesn't forgive" ethos.

---

## ACT IV — THE LANGUAGE OF MONEY: SCRIPT

---

### Slide 22 — Bitcoin Has a Programming Language

Every output is locked by a tiny program written in **Script** — a stack-based, intentionally limited, Forth-like language.

- **scriptPubKey** (on the output) = the lock / the puzzle.
- **scriptSig** (on the input) = the key / the solution.
- To spend: run `scriptSig` then `scriptPubKey` together; if the stack ends with a truthy value, **the money moves.**

**Visual:** A padlock (scriptPubKey) and a key (scriptSig) snapping together; a green "VALID" when they fit.

**Speaker note:** Surprise the room: "Bitcoin isn't just money — it's programmable money. There's a VM in every UTXO."

---

### Slide 23 — Script Runs on a Stack

No loops. No variables. Just push data and run operations on a stack — deliberately **not Turing-complete** (so validation always terminates; no infinite loops to DoS the network).

```
scriptSig:     <sig> <pubkey>
scriptPubKey:  OP_DUP OP_HASH160 <hash> OP_EQUALVERIFY OP_CHECKSIG

Stack trace (Pay-to-Public-Key-Hash, P2PKH):
  <sig> <pubkey>                 ← push from scriptSig
  <sig> <pubkey> <pubkey>        ← OP_DUP
  <sig> <hash(pubkey)>           ← OP_HASH160
  <sig> <hash> <hash>            ← push expected <hash>
  <sig>                          ← OP_EQUALVERIFY (hashes match?)
  TRUE                           ← OP_CHECKSIG (signature valid?)
```

**Visual:** Animate a literal stack of plates, each op pushing/popping, ending on a single green "TRUE" plate.

**Speaker note:** Walk the trace one line at a time, clicking through. This is the most "programming" slide — let the developers savor it.

---

### Slide 24 — The Limits Are the Point

Why such a weak language? Because **a global money network can't afford surprises.**

- Not Turing-complete → every script provably halts. No gas, no runaway loops.
- Small opcode set → smaller attack surface, easier to reason about.
- Constraints aren't a bug; they're a security posture. "Boring" is a feature when the stake is everyone's savings.

> Ethereum chose the opposite trade-off (full Turing-completeness + gas). Neither is "right" — they're different answers to _how much programmability is safe?_

**Visual:** A dial labeled "Programmability ↔ Safety," with Bitcoin near "Safety" and a contrasting marker near "Programmability."

**Speaker note:** Pre-empt the "why not just use Ethereum?" question by framing it as an honest engineering trade-off, not a rivalry.

---

### Slide 25 — Smart Contracts, Bitcoin-Style

Even a limited Script enables real contracts by composing opcodes:

- **Multisig (2-of-3):** funds need any 2 of 3 keys — corporate treasuries, escrow.
- **Timelocks (`OP_CHECKLOCKTIMEVERIFY`):** "spendable only after block N" — inheritance, vesting, payment channels.
- **P2SH / P2WSH:** lock to the _hash_ of a script; reveal and satisfy it only when spending. The sender doesn't need to know the contract's guts.

**Visual:** Three mini-icons: a 2-of-3 vault, an hourglass timelock, a wrapped "hash of a contract" box.

**Speaker note:** Dispel the myth that "Bitcoin can't do smart contracts." It can — conservatively and on purpose.

---

### Slide 26 — Putting It Together: Build, Sign, Broadcast

The full developer workflow, end to end:

```python
# 1. Construct the outputs (where the money goes)
tx_out = TxOut(amount=int(0.01e8), script_pubkey=address_to_script(bob_addr))

# 2. Reference the input (what you're spending)
tx_in  = TxIn(prev_tx, prev_index)

# 3. Assemble the transaction
tx = Tx(1, [tx_in], [tx_out, change_out], 0, testnet=True)

# 4. Sign each input with your private key
tx.sign_input(0, private_key)

# 5. Serialize to hex and broadcast to the network
raw = tx.serialize().hex()
broadcast(raw)        # off it goes to thousands of nodes
```

**Visual:** Five-step pipeline with a glowing packet leaving the laptop and fanning out to a network of nodes.

**Speaker note:** This is the summit. Everything from Act II–IV converges in five function calls. Let the audience feel the whole machine turn over.

---

### Slide 27 — What the Network Does With It

Your raw transaction now faces thousands of independent referees:

1. Every node **independently re-runs** your scripts and re-verifies your signatures (the math from Act II).
2. Valid? It enters the **mempool** and propagates.
3. A miner includes it in a block; **proof-of-work** orders it; confirmations stack up.
4. No one approved it. Everyone _verified_ it. **That's the referee replaced by math** — the promise from Slide 2, delivered.

**Visual:** Your packet rippling across a node graph, each node flashing "✓ verified," converging into a mined block.

**Speaker note:** Close the Act I loop out loud: "Remember the two strangers and the chasm? This is the bridge — and it's made of arithmetic."

---

## ACT V — THE BIGGER PICTURE & CALL TO ACTION

---

### Slide 28 — The Stack You Just Built

|Layer|What it is|Slides|
|---|---|---|
|Finite fields|Deterministic clock arithmetic|5–7|
|Elliptic curves|The one-way trapdoor (secp256k1)|8–13|
|Keys & signatures|Own + prove without revealing|14–16|
|Serialization & addresses|Math → bytes humans can use|17–18|
|Transactions & fees|Consuming and creating UTXOs|19–21|
|Script|Programmable, deliberately limited locks|22–25|

> ~2,000 lines of Python. No `import bitcoin`. You could write every layer yourself.

**Visual:** The Slide 4 arch, now fully built and labeled, glowing.

**Speaker note:** The recap. People should feel the distance traveled — from "a coin is just a number" to a working money protocol.

---

### Slide 29 — Why Build It Yourself?

- **You can't trust what you can't verify.** Reading the math beats trusting a brand.
- Every abstraction you open up is one fewer place a bug — or a lie — can hide.
- The skills transfer: finite fields, ECC, hashing, and signatures power TLS, SSH, passkeys, and every blockchain after Bitcoin.
- "From scratch" isn't nostalgia. It's how you earn the right to have an opinion.

**Visual:** An engineer lifting the hood of a car labeled "Bitcoin" — gears inside are all the slides' icons.

**Speaker note:** Make it personal and aspirational. The payoff of this talk isn't trivia; it's _agency._

---

### Slide 30 — Your First Week

A concrete starting path:

1. **Read** Jimmy Song's _Programming Bitcoin_ — build the library chapter by chapter.
2. **Code** `FieldElement` and `Point` tonight. Make the unit tests pass. (~100 lines.)
3. **Play** on **testnet** — free coins, zero risk. Send your first self-built transaction.
4. **Run a node** (Bitcoin Core). Watch _your_ machine verify the whole chain.
5. **Read the source.** It's open. The referee is published.

**Visual:** A five-checkbox "Week 1" checklist that fills in as you speak.

**Speaker note:** Lower the activation energy. Give the room something to do _tonight_, while the inspiration is hot.

---

### Slide 31 — Closing: The Cursor Returns

_(Back to the black screen and blinking cursor from Slide 1.)_

```python
>>> private_key = 0xdeadbeef...
>>> public_key  = private_key * G
>>> # You now know exactly what these two lines mean.
```

> **"Money used to be something you were handed. Now it's something you can read, verify, and build. Go build."**

- Thank you.
- `@yourhandle` · slides + code repo · _Programming Bitcoin_, Jimmy Song

**Visual:** The cursor blinks once more, then the screen prints `>>> _` and holds.

**Speaker note:** End where you began. Silence for two beats after the last line. Don't fill it. Let the loop close and walk off.

---

## APPENDIX — Speaker Toolkit

**Core metaphors (reuse deliberately):**

- Finite field = a _clock_ (wrap-around arithmetic).
- ECDLP = a _one-way revolving door_ (easy in, impossible out).
- Signature = a _wax seal_ (proves the ring without handing it over).
- Transaction = _consuming and re-creating locked boxes_, not moving coins.
- Script = a _padlock and key_ that must snap together.

**Data points worth memorizing:**

- p = 2²⁵⁶ − 2³² − 977 ≈ 1.16 × 10⁷⁷ (≈ atoms in the observable universe).
- Breaking a key ≈ 2¹²⁸ operations (√n, generic attack).
- 1 BTC = 100,000,000 satoshis; all amounts are integers.
- Compressed pubkey 33 bytes vs. uncompressed 65 bytes.
- Real-world nonce-reuse break: 2010 Sony PS3 ECDSA key.

**Pacing:** Acts I–II ~12 min (earn trust with fundamentals), Act III–IV ~12 min (momentum, code), Act V ~6 min (inspire + CTA). Linger on Slides 10, 13, 19, 23, 27 — they carry the talk.

**Delivery rule:** Every time you introduce an abstraction, _open it up_ before moving on. The whole thesis is "no magic." Never violate it.