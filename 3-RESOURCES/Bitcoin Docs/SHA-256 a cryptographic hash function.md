SHA-256 is a cryptographic hash function that takes any input and deterministically produces a 256-bit (32-byte) fingerprint. It is the backbone of Bitcoin — used in proof-of-work mining, transaction IDs, Merkle trees, and address derivation. Here's how it works, step by step.

**Step 1 — Pre-processing.** The input message is converted to bits, then padded so its total length ≡ 448 (mod 512). A 64-bit big-endian encoding of the original message length is appended, making the final padded message an exact multiple of 512 bits. The result is split into 512-bit blocks.

**Step 2 — Initialization.** Eight 32-bit words (H0–H7) are set to the fractional parts of the square roots of the first 8 primes. Sixty-four round constants (K0–K63) come from the fractional parts of the cube roots of the first 64 primes. These are not magic numbers — they exist precisely to eliminate any hidden structure.

**Step 3 — Message schedule.** Each 512-bit block is expanded into 64 32-bit words (W0–W63). The first 16 words come directly from the block. Words W16–W63 are computed as: `W[i] = σ1(W[i-2]) + W[i-7] + σ0(W[i-15]) + W[i-16]`, where σ0 and σ1 are combinations of right-rotate and right-shift operations.

**Step 4 — 64 compression rounds.** Eight working variables (a–h) are loaded from the current hash state. Each round mixes them using majority functions, choice functions, and the schedule word plus a round constant. The avalanche effect means flipping one input bit eventually flips ~50% of output bits.

**Step 5 — Add to hash.** After all 64 rounds, the round output is added (mod 2³²) back to the initial hash values H0–H7 for this block.

**Step 6 — Output.** After all blocks are processed, H0–H7 are concatenated to form the final 256-bit digest.The interactive stepper above lets you walk through each of the 5 stages. Here are the most important conceptual points to internalize:

**Why padding?** SHA-256 can only process 512-bit blocks. Padding ensures the message fits exactly — the appended 1-bit marks the end, the zeros fill space, and the 64-bit length field prevents length-extension attacks (partially).

**Why irrational number constants?** The H0–H7 initial values and K0–K63 round constants come from square roots and cube roots of primes. This eliminates any "backdoor-friendly" structure — there's no hidden reason those bits were chosen.

**The schedule expands diffusion.** W0–W15 are just the raw message bits. But W16–W63 mix in earlier words via rotations and XORs, meaning every input bit eventually influences the compression function in multiple rounds through multiple paths.

**The avalanche effect is the whole point.** Flip one bit of your input, and by round 64 you've changed roughly half the output bits. This is what makes SHA-256 useful — you cannot deduce the input from the output, and you cannot engineer a specific output.

**In Bitcoin specifically**, SHA-256 is run twice (`SHA256d`) to close a known length-extension vulnerability, and miners are literally searching for inputs where the double-SHA-256 output starts with a certain number of zero bits — the proof-of-work target.

SHA-256's compression function is where the actual cryptographic work happens. It runs 64 times per 512-bit block, and each round takes all 8 working registers, mashes them together with bitwise operations, and produces a new state. Here is a precise breakdown.Here is the full conceptual picture to go alongside the simulator:

**Why only `a` and `e` get new values.** In each round, six of the eight registers simply shift right — `b←a`, `c←b`, `d←c`, `f←e`, `g←f`, `h←g`. This is free — no computation. Only `a` and `e` receive freshly computed values. This design means a single round is cheap but the information from W[i] and K[i] gradually permeates every register across 64 rounds.

**What `Ch` and `Maj` actually do.** `Ch(e,f,g)` is a bitwise multiplexer: each bit of `e` selects whether the output bit comes from `f` or `g`. If bit 17 of `e` is 1, take bit 17 of `f`; if 0, take bit 17 of `g`. `Maj(a,b,c)` is a bitwise democracy: each output bit is 1 if at least two of the three input bits are 1. These are nonlinear operations — the output cannot be easily inverted.

**Why three rotation amounts per sigma.** `Σ₀(a)` uses rotations of 2, 13, and 22. `Σ₁(e)` uses 6, 11, and 25. The amounts were chosen so that XORing the three rotations together guarantees every output bit depends on many input bits. Using just one rotation would leave too much linearity — an attacker could reason about it algebraically.

**The avalanche builds slowly then explodes.** In round 1, only `a` and `e` have changed. By round 10, through the shift chain and T₁/T₂ feedback, the new values have propagated to all eight registers. By round 30, every output bit of every register depends on essentially every input bit. By round 64, you have full diffusion — the avalanche effect is complete.

**Why 64 rounds specifically.** SHA-256's designers tested the minimum number of rounds needed to make all known attacks (differential cryptanalysis, linear cryptanalysis) computationally infeasible. 64 provides a large security margin. The current best known attack on the full 64-round SHA-256 is a theoretical preimage attack requiring 2²⁵¹·⁷ operations — effectively impossible.

**The final addition step matters.** After all 64 rounds, the resulting `a–h` values are added back to the original `H0–H7` for that block (mod 2³²). This makes SHA-256 a Merkle–Damgård construction — each block's output feeds into the next block as the new starting state, chaining them all together into the final 256-bit digest.

SHA-256's compression function is where the actual cryptographic work happens. It runs 64 times per 512-bit block, and each round takes all 8 working registers, mashes them together with bitwise operations, and produces a new state. Here is a precise breakdown.

V

visualize

V

visualize show_widget

Here is the full conceptual picture to go alongside the simulator:

**Why only `a` and `e` get new values.** In each round, six of the eight registers simply shift right — `b←a`, `c←b`, `d←c`, `f←e`, `g←f`, `h←g`. This is free — no computation. Only `a` and `e` receive freshly computed values. This design means a single round is cheap but the information from W[i] and K[i] gradually permeates every register across 64 rounds.

**What `Ch` and `Maj` actually do.** `Ch(e,f,g)` is a bitwise multiplexer: each bit of `e` selects whether the output bit comes from `f` or `g`. If bit 17 of `e` is 1, take bit 17 of `f`; if 0, take bit 17 of `g`. `Maj(a,b,c)` is a bitwise democracy: each output bit is 1 if at least two of the three input bits are 1. These are nonlinear operations — the output cannot be easily inverted.

**Why three rotation amounts per sigma.** `Σ₀(a)` uses rotations of 2, 13, and 22. `Σ₁(e)` uses 6, 11, and 25. The amounts were chosen so that XORing the three rotations together guarantees every output bit depends on many input bits. Using just one rotation would leave too much linearity — an attacker could reason about it algebraically.

**The avalanche builds slowly then explodes.** In round 1, only `a` and `e` have changed. By round 10, through the shift chain and T₁/T₂ feedback, the new values have propagated to all eight registers. By round 30, every output bit of every register depends on essentially every input bit. By round 64, you have full diffusion — the avalanche effect is complete.

**Why 64 rounds specifically.** SHA-256's designers tested the minimum number of rounds needed to make all known attacks (differential cryptanalysis, linear cryptanalysis) computationally infeasible. 64 provides a large security margin. The current best known attack on the full 64-round SHA-256 is a theoretical preimage attack requiring 2²⁵¹·⁷ operations — effectively impossible.

**The final addition step matters.** After all 64 rounds, the resulting `a–h` values are added back to the original `H0–H7` for that block (mod 2³²). This makes SHA-256 a Merkle–Damgård construction — each block's output feeds into the next block as the new starting state, chaining them all together into the final 256-bit digest.