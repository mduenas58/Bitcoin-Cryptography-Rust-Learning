# Introduction to Bitcoin Mining (MIN 101) — Master Study Guide

> Course: **MIN 101 – Introduction to Bitcoin mining** · Professor: Loïc Morel · Level: Beginner · Plan ₿ Academy Goal: Understand Bitcoin mining and proof-of-work from scratch.

This guide has two parts:

1. **Key concepts, chapter by chapter** — a complete overview of all the material, structured for mastery.
2. **A 100-question quiz** — each question has a marked correct answer and an explanation.

---

## Part A — Key Concepts by Chapter

### The big picture (mental model)

The single chain of ideas that holds the whole course together:

**transactions → blocks → mining → blockchain → reward**

A user creates a transaction; transactions are grouped into a block; a miner validates that block by spending energy (proof-of-work); the validated block is appended to the blockchain; and the miner is paid a reward. Every later chapter adds technical detail to one link in this chain.

---

### Part 1 — Introduction

#### 1.1 Course overview

The course is organized in five parts: (1) Introduction, (2) How proof-of-work works, (3) The mining incentive system, (4) The mining industry, (5) Final section. MIN 101 deliberately skips Bitcoin basics (covered in BTC 101) and goes straight to mining. Learning objectives: understand proof-of-work and its role; analyze the difficulty adjustment; know the real meaning of mining terminology; describe how a block is built and its components; identify major developments in the mining industry.

#### 1.2 Bitcoin mining made easy

- The **blockchain** is like a large public notebook shared by everyone, recording who sent bitcoins to whom. No single person holds it — thousands of computers maintain the same version, so no trust in one party is required.
- A **transaction** is not added instantly; it is broadcast to the network and waits to be included in the next packet, called a **block**.
- A **block** is simply a set of grouped transactions. Publishing a block is not enough — you must prove it deserves to be added.
- **Mining** is the work of validating a block by consuming energy. Miners use specialized computers that burn electricity to perform an enormous number of trials in a loop until they find a proof the network accepts.
- Once validated, the block is broadcast; other nodes quickly check it and append it to the chain of previous blocks — hence "block-chain."
- Miners are not volunteers: a validated block earns them (a) newly created bitcoins and (b) the fees of the transactions they included. This is programmed monetary issuance plus a fee market.

---

### Part 2 — How Proof of Work Works

#### 2.1 The Bitcoin transaction path

- A **transaction** is a data structure transferring ownership of bitcoins. It consumes outputs of past transactions (**UTXOs**) as **inputs**, and creates new **outputs** defining who owns the coins next and under what conditions.
- Bitcoins are not held in an account; they are **locked by spending conditions**. To spend a UTXO you must provide cryptographic proof of the right to unlock it — usually a **digital signature** from a **private key**. This is why securing private keys is essential.
- The digital signature does two jobs: **authorizes the spend** (proves possession of the expected private key) and **protects integrity** (ties the authorization to the exact transaction details, so any later alteration invalidates the signature).
- **Nodes** (e.g., Bitcoin Core) form a **peer-to-peer** network — no central server. A node verifies a transaction (valid signatures; inputs reference existing UTXOs; those UTXOs are unspent; outputs ≤ inputs so no coins are created from nothing), then relays it to peers, who relay it onward. Propagation reaches most of the network in seconds.
- The **mempool** (memory + pool) is the waiting room: temporary storage for valid but unconfirmed transactions. There is **no single mempool** — each node keeps its own, so contents can differ slightly between nodes.
- The **blockchain** is a public time-stamping register that solves **double spending** without a central authority. Satoshi: "The only way to confirm the absence of a transaction is to be aware of all transactions." Each block includes the **hash of the previous block's header**, chaining blocks together: altering a past block changes its hash and breaks every subsequent link.
- A miner's concrete objective: build a new block extending the chain with pending transactions, then make it valid via proof-of-work.

#### 2.2 Building a Bitcoin block

- Each miner builds its own **candidate block** from transactions in its mempool: choose which transactions to include, organize them per Bitcoin rules, and produce the block **metadata** (header).
- Transaction selection follows economics: block capacity is limited, so miners prioritize the highest **fee rate** (fees per unit of space, in **sats/vB**) to maximize revenue per byte.
- A block has two main parts: a **list of transactions** and an **80-byte header** (its "identity card"). You don't mine the whole block — **you mine only the header**, which commits to the block's contents and links it to the chain.
- The **Merkle tree** summarizes all transactions into one hash, the **Merkle root**: hash each transaction, pair and concatenate and re-hash repeatedly until one root remains. Changing any single transaction (even one bit) changes the root, hence the header. Since **SegWit**, there are effectively two nested Merkle trees (signatures separated from the rest).
- The **block header is 80 bytes with exactly 6 fields**:
    1. **version** — which rules/upgrade signals the block follows.
    2. **previousblockhash** — hash of the previous block's header; this is what links blocks into a chain.
    3. **merkleroot** — fingerprint of all transactions; ties the header to block content.
    4. **time** — a Unix timestamp chosen by the miner (within validity constraints).
    5. **nbits** — the encoded difficulty target.
    6. **nonce** — a value the miner freely changes to make repeated attempts.

#### 2.3 The hash, the target and the nonce

- A **hash function** maps any input to a fixed-size output (fingerprint). Properties: (1) changing one input bit changes the output completely and unpredictably; (2) it is **irreversible** (can't go output → input); (3) practically impossible to find two inputs with the same hash (collision resistance).
- Bitcoin mining uses **SHA-256 applied twice** = **SHA256d**: `hash = SHA256(SHA256(message))`. The "message" is the 80-byte block header.
- **Proof-of-work** is not solving a puzzle but a **trial-and-error search**: find a header whose `SHA256d(header)`, interpreted as a number, is **≤ the target**. Formally: `SHA256d(block_header) <= target`.
- The **target** is a 256-bit number. **Lower target = harder** (fewer valid results below it); **higher target = easier**.
- The **asymmetry** is the key property: producing a proof is expensive (many hashes), but **verifying** it is trivial (hash once, compare to target).
- The **nonce** is a **32-bit** field (~4.29 billion values, 0 to 2³²−1). Changing it changes the header and therefore the hash, enabling new attempts. The loop: build candidate block → hash header → if hash > target, change nonce → repeat.
- The nonce alone may be exhausted; any change inside the transactions changes the Merkle root and thus the header. An **extra-nonce** further multiplies the search space (detailed in 3.3).
- Why "proof of work": **"proof"** because anyone can verify instantly; **"work"** because finding it costs real computation and energy. Satoshi's two stated advantages: (1) **seals economic history** — rewriting a block means redoing its work plus all later blocks; with each new block, every UTXO accumulates more security; (2) **defines majority rule and neutralizes Sybil attacks** — the majority is the chain with the most accumulated work ("one CPU = one vote," not "one IP = one vote"), so spinning up many identities gives no advantage without added compute.

#### 2.4 The history of proof of work

Proof-of-work predates Bitcoin; Satoshi assembled existing ideas.

- **Hashcash** (Adam Back, **1997**): considered the invention of the proof-of-work principle. To deter **e-mail spam**, each message must carry a proof (a hash with a required number of leading zeros) that is cheap to verify but costly to mass-produce. No centralized filtering, no identity, no reputation system needed. Not used for e-mail today, but it imposes a marginal cost on an automatable digital action.
- **Bit Gold** (Nick Szabo, late 1990s–early 2000s): a conceptual project for **digital scarcity** via proof-of-work, recording proofs in a register to establish ownership. Never deployed, but introduced the ideas that computation can create scarcity and that timestamping builds a hard-to-rewrite history.
- **RPOW – Reusable Proofs of Work** (Hal Finney, **2004**): proofs of work that could be **exchanged** rather than merely consumed, with verification and transfer without duplication. A direct precursor to Bitcoin.
- Bitcoin reuses the mechanism but gives it a **central, collective role**: proof-of-work decides who writes the next block and makes the register costly to falsify.

#### 2.5 Adjusting the difficulty target

- Bitcoin targets an **average of one block every 10 minutes** — an average over a long period, not a per-block guarantee. Mining is probabilistic: each hash is an independent attempt, like a continuous lottery draw.
- **Why 10 minutes?** A practical compromise. Shorter intervals give faster confirmations but cause more temporary **network splits**: when two valid blocks appear at the same height during propagation, the network briefly divides (block A vs. block B). The losing branch becomes a **stale block** (loosely called "orphan"). 10 minutes usually lets the winning block propagate before a competitor appears, limiting wasted work.
- **Hashrate** = hash computations per second (H/s, TH/s, EH/s…), by one miner or the whole network. More hashrate at a fixed target → blocks found faster.
- **Difficulty adjustment**: every **2016 blocks** (~2 weeks) each node recalculates the target from the time the last 2016 blocks actually took.
    - Found too fast → hashrate rose → **lower the target** (harder).
    - Found too slow → hashrate fell → **raise the target** (easier).
    - Formula: `Tn = To × (Ta / Tt)` where `To` = old target, `Ta` = actual elapsed time, `Tt` = target time = 1,209,600 seconds (2 weeks). Example: `To = 18,045,755,102`, `Ta = 1,000,000 s` → `Tn ≈ 14,918,779,020` (lower → harder, since blocks came too fast).
- **Clamping**: adjustment is limited to a **factor of 4** in either direction to prevent abrupt swings.
- **Off-by-one bug**: the original code measures time across **2015** intervals instead of 2016, so difficulty is very slightly overestimated and blocks come ~0.05% slower than target. Never fixed (would need a hard fork; relevant only to the theoretical "time warp" attack).
- **Target representation**: stored compactly in the 32-bit **nBits** field (an exponent byte + 3-byte coefficient, like base-256 scientific notation), not as the raw 256-bit value.

---

### Part 3 — The Bitcoin Mining Incentive System

#### 3.1 Block reward

- Mining has real costs (electricity, hardware, maintenance, premises, cooling). The **reward** aligns miners' private interest with the network's collective interest, via **game theory**: producing a valid block pays; cheating gets the block rejected, wasting its cost. In a competitive field, honesty is the most profitable strategy.
- The **block reward** = **block subsidy** + **transaction fees**, claimed by the winning miner when the block is added to the chain.
- **Block subsidy** = the monetary-creation part: new bitcoins minted **ex nihilo**, capped and defined by protocol (identical for all miners; a miner may technically claim less). Two roles: (1) incentivize mining/security, especially early when fees were tiny; (2) distribute new currency openly and neutrally to anyone who mines. Downside: it dilutes existing holders — a form of **monetary inflation** (destined to fall to zero, see halving).
- **Transaction fees** = the usage-based part. Block space is scarce (a block ~every 10 min, limited capacity), so a **fee market** forms. The winning miner collects **all** fees of the transactions it included.
- **Fees are not an output.** A transaction spends inputs and creates outputs; **fee = total inputs − total outputs**. Example: inputs 100,000 + 150,000 = 250,000 sats; outputs 35,000 + 42,000 + 170,000 = 247,000 sats → **3,000 sats fee**. Technically the fee sats are destroyed and the miner gains the right to recreate the same amount.
- **Fee rate** = `fee / weight (vB)`, in **sats/vB**. Example: 1,974 sats / 141 vB ≈ **14 sats/vB**. Miners maximize revenue per unit of space, which is why low-fee transactions linger in mempools.
- **Spam protection**: fees impose a cost on flooding. Nodes apply local relay policies and a minimum threshold — Bitcoin Core's **minRelayTxFee** default is **0.1 sat/vB**; below it, transactions usually aren't relayed.

#### 3.2 Halving

- **Halving** is a protocol event that **halves the block subsidy** (not fees). Triggered by **block height**, every **210,000 blocks** (~4 years), not by date.
    
- Genesis subsidy (2009): **50 BTC**. `subsidy(n) = 50 / 2^n` after n halvings (in code, `nSubsidy >>= halvings`).
    
- Past/upcoming halvings:
    
    |Event|Height|Date|New subsidy|
    |---|---|---|---|
    |Halving 1|210,000|Nov 28, 2012|25 BTC|
    |Halving 2|420,000|Jul 9, 2016|12.5 BTC|
    |Halving 3|630,000|May 11, 2020|6.25 BTC|
    |Halving 4|840,000|Apr 20, 2024|3.125 BTC|
    |Halving 5 (upcoming)|1,050,000|Spring 2028 (est.)|1.5625 BTC|
    
- **End of issuance**: 1 BTC = 100,000,000 sats. Halving continues until the subsidy drops below 1 satoshi. The final subsidy ends at the **33rd halving**, block **6,930,000**, around the year **2140**. By the 7th halving, >99% of all bitcoins are already issued (the 99% threshold ~2032–2036), then it takes ~100+ years to mine the final 1%.
    
- **Why never exactly 21 million?** Mechanically, the subsidy falls below 1 sat before reaching the theoretical total (granularity + rounding). Plus: miners sometimes under-claim subsidy; the genesis block's coins are unspendable/not in the UTXO set; historical bugs (duplicate coinbase IDs); and coins lost or destroyed (unspendable scripts, OP_RETURN, lost keys). So 21M is a useful approximation, never the actual figure.
    

#### 3.3 The coinbase transaction

- The **coinbase transaction** is always the **first transaction** in a block and is how the winning miner collects the reward. It has a TXID, outputs, and sits in the Merkle tree — but it **spends no existing UTXO**; it creates bitcoins from scratch. A block **without** a coinbase is invalid.
- ⚠️ Naming: "coinbase" the transaction has **no connection** to the Coinbase exchange company.
- **Roles**: (1) pay the miner the subsidy + fees; (2) anchor the SegWit **witness commitment**; (3) carry arbitrary technical data (pool organization).
- **Structure**: exactly **one input** pointing to a deliberately **fake UTXO** — TXID of all zeros (`000…000`) and index `0xffffffff`. Its **scriptSig** is otherwise free (no real UTXO to unlock), so miners can put nearly anything in it. Plus one or more standard outputs paying the reward to the miner's address(es); total outputs must not exceed **max subsidy + fees**. The fee portion must exactly equal the sum of (inputs − outputs) of all other transactions in the block.
- **Uses of the free scriptSig field**:
    - **BIP-34** (soft fork, March 2013, from block 227,930): block **version 2** requires the **block height** at the start of the coinbase scriptSig — ensures uniqueness of each coinbase/block.
    - **Extra-nonce**: extends the 32-bit nonce search space. Changing the extra-nonce changes the coinbase scriptSig → its TXID → the Merkle root → the header, giving a fresh space of hashes to explore.
    - **Pool/miner identification**: pools insert unique per-miner identifiers (to avoid duplicate work) and a pool tag (for block attribution and statistics).
    - **SegWit commitment** (soft fork, 2017): witnesses (signatures) are grouped in a separate Merkle tree whose root is committed in a coinbase **OP_RETURN output** — so separately stored witnesses are still committed to the header.
    - **Arbitrary messages**: e.g., Satoshi's Genesis-block message, "The Times 03/Jan/2009 Chancellor on brink of second bailout for banks," encoded in hex in the coinbase scriptSig.
- **Maturity period**: coinbase outputs are not immediately spendable — they require a **100-block maturity**, i.e. **101 confirmations**. This prevents newly created reward coins from circulating before the block is deeply buried, avoiding cascade problems if a reorganization abandons the block. (Related rule of thumb: a transaction is treated as effectively immutable after **6 confirmations**.)

---

### Part 4 — The Bitcoin Mining Industry

#### 4.1 The evolution of mining machines

- **CPU (2009 onward)**: early mining ran on ordinary computer CPUs — Bitcoin was a single program acting as wallet, node, and miner. A CPU is general-purpose, not optimized for repetitive hashing, but early difficulty was low enough. Proof-of-work doesn't require any specific hardware; any technical advantage becomes an economic one. (Today the **NerdMiner** project still CPU-mines with ~0 chance.)
- **GPU**: the real bottleneck was **parallelism**, not raw power. GPUs run the same operation across many cores (hundreds to thousands), ideal for repeated hashing — far more hashes/sec than a CPU at similar power. As BTC gained dollar value, mining shifted from participation to profit; dedicated multi-GPU rigs appeared. Between mid-2010 and mid-2011 difficulty multiplied by **~1,000**.
- **FPGA**: an intermediate step — reprogrammable chips configured to implement SHA256d directly, gaining energy efficiency over CPU/GPU, paving the way to ASICs.
- **ASIC** (Application-Specific Integrated Circuit): a chip designed for a **single task** — running **SHA256d** at maximum speed and efficiency. Far more hashes/sec than a GPU at lower power; GPU mining became uncompetitive. Mining became an industrial, capital-intensive activity with hardware obsolescence as newer generations arrive.
- **Mining farms**: buildings or container sites packed with thousands of ASICs running 24/7. Challenges: cheap, stable, large-scale power; heat management (to avoid throttling); dust/humidity control; real-time monitoring. Run by industrial, sometimes public, players — e.g., **MARA Holdings (Nasdaq: MARA)** and **Riot Platforms (Nasdaq: RIOT)**. Competitiveness hinges on electricity cost, equipment cost/depreciation, cooling, reliability, and communications. Home mining can still make sense with very cheap power or heat reuse, but requires an ASIC and a way to reduce income variance — i.e., a pool.

#### 4.2 Grouping into mining pools

- A **mining pool** aggregates many independent miners' compute so the group finds blocks more often; the reward is shared by internal pool rules (details in MIN 201). Pool participants are often called **"hashers"** (they hash data the pool sends them rather than doing all mining work themselves).
- **Pool ≠ farm**: a **farm** is a physical site operated by one entity; a **pool** is a (usually virtual) grouping of dispersed machines under common coordination. A farm can join a pool.
- **Why pool — variance reduction**: mining is probabilistic. Long-run earnings ≈ your share of total hashrate (**law of large numbers**), but short/medium-term earnings are wildly irregular = **variance**. Example: with 0.0001% of hashrate (network ~144 blocks/day), expectation ≈ 0.000144 block/day → one block on average every ~6,944 days (~19 years), and you might find nothing for years while paying costs. A pool finds blocks often and pays each member a frequent fraction — it **sells predictability** at the cost of shared rewards and fees.
- **History**: **Braiins Pool** (formerly **Slush Pool / Bitcoin.cz**) was the **first** Bitcoin mining pool, mining its first block on **December 16, 2010**, and within days captured ~3.5% of global hashrate. Pools use protocols like **Stratum** (later **Stratum V2**) to coordinate distributed work.
- **Modern situation (early 2026)**: global hashrate is on the order of **zetta-hashes/sec** (1 ZH/s = 1,000 EH/s); almost all blocks come from pools. Leading pools by share (mempool.space, Dec 16, 2025 – Jan 16, 2026): Foundry USA (~29.6%), AntPool (~17.2%), ViaBTC (~11.7%), F2Pool (~10.7%), SpiderPool (~8.0%), MARA Pool (~5.2%), then SECPOOL, Luxor, Binance Pool, OCEAN, and others. Shares change constantly; check mempool.space for current data.

---

## Part B — 100-Question Quiz

For each question, the correct option is marked **✓** and followed by an explanation.

### Section 1 — Mining made easy & the big picture (1.2)

**Q1. In the simplified model, what is the blockchain compared to?** 
A. A bank vault 
==B. A large public notebook shared by everyone ✓== 
C. A private database held by Satoshi 
D. A central government registry
_Explanation:_ The blockchain is described as a large public notebook, shared by all, recording who sent bitcoins to whom — maintained collectively rather than by one trusted party.

**Q2. Why can't the Bitcoin ledger be held by a single person?** 
A. It would be too large to store 
==B. It would have to be trusted ✓== 
C. It is illegal in most countries 
D. Computers cannot copy it
_Explanation:_ If one person held the notebook, everyone would have to trust them. Bitcoin instead has thousands of computers maintain the same version, removing the need for trust.

**Q3. What is the correct mental chain of ideas for how Bitcoin works?** 
A. mining → reward → transactions → blocks 
B. blocks → blockchain → transactions → mining 
==C. transactions → blocks → mining → blockchain → reward ✓== 
D. reward → mining → blockchain → blocks
_Explanation:_ The course's guiding thread is: transactions are created, grouped into blocks, a miner validates a block via energy, the block is appended to the blockchain, and the miner is rewarded.

**Q4. In the simplified view, what does mining fundamentally consume?** 
A. Water 
==B. Energy/electricity ✓== 
C. Gold reserves 
D. Bandwidth only
_Explanation:_ Mining is the work of validating a block by consuming energy; specialized computers burn electricity running many trials until they find an accepted proof.

**Q5. The two types of income a miner receives for a valid block are:** 
==A. Newly created bitcoins and transaction fees ✓== 
B. A salary and a bonus 
C. Interest and dividends 
D. Government subsidies and tips
_Explanation:_ A validated block earns the miner newly issued bitcoins (programmed issuance) plus the fees paid by users for the included transactions.

### Section 2 — The Bitcoin transaction path (2.1)

**Q6. What does a Bitcoin transaction consume as its inputs?** 
A. Future outputs 
==B. Existing UTXOs (unspent outputs of past transactions) ✓== 
C. Mempool entries 
D. Block headers
_Explanation:_ A transaction consumes outputs from past transactions — UTXOs — referencing them as inputs, then creates new outputs.

**Q7. How are bitcoins held, according to the course?** 
A. In an account like a bank balance 
==B. Locked by spending conditions, not in an account ✓== 
C. In a central wallet server 
D. As physical tokens
_Explanation:_ Bitcoins are not in an account; they are locked by spending conditions. To spend a UTXO you must prove you can satisfy its condition.

**Q8. What is most commonly used to prove the right to spend a UTXO?** 
==A. A digital signature generated from a private key ✓== 
B. A password 
C. An SSL certificate 
D. A hash of the next block
_Explanation:_ The spending proof usually takes the form of a digital signature produced with the private key that satisfies the UTXO's condition.

**Q9. Which TWO roles does a digital signature play in a Bitcoin transaction?** 
A. Encryption and compression 
==B. Authorizing the spend and protecting integrity ✓== 
C. Mining and timestamping 
D. Routing and relaying
_Explanation:_ The signature authorizes the expenditure (proves possession of the expected private key) and protects integrity (binds the authorization to the transaction's exact details).

**Q10. What kind of network is Bitcoin?** 
A. Client-server with a central server 
==B. Peer-to-peer with no central server ✓== 
C. A single supercomputer 
D. A cloud database
_Explanation:_ Bitcoin is peer-to-peer: there is no central server; nodes collectively verify, store, and relay transactions and blocks.

**Q11. Which of the following is NOT a check a node performs on a transaction?** 
A. Signatures are valid 
B. Inputs reference existing UTXOs 
C. The referenced UTXOs are unspent 
==D. The sender has a verified government ID ✓==
_Explanation:_ Nodes verify signatures, that inputs reference existing unspent UTXOs, and that outputs ≤ inputs. Identity verification is not part of Bitcoin's rules.

**Q12. What does a node do with a valid but unconfirmed transaction after verifying it?** 
A. Adds it directly to the blockchain 
B. Signs it with its private key 
==C. Relays it to its peers ✓== 
D. Deletes it
_Explanation:_ If the transaction passes checks, the node propagates (relays) it to connected peers, who in turn verify and relay it.

**Q13. What is the mempool?** 
A. A permanent archive of confirmed transactions 
==B. Temporary storage for valid but unconfirmed transactions ✓== 
C. A field in the block header 
D. The list of mining pools
_Explanation:_ The mempool (memory + pool) is the waiting room: a temporary store of valid but still-unconfirmed transactions.

**Q14. Which statement about mempools is correct?** 
A. There is one global mempool shared by all nodes 
==B. Each node maintains its own mempool, so contents can differ ✓== 
C. The mempool lives inside each block 
D. The mempool is a central server
_Explanation:_ There is no single mempool; each node keeps its own with local constraints, so two nodes may hold slightly different contents.

**Q15. What core problem does the blockchain solve without a central authority?** 
A. Slow internet 
==B. Double spending ✓== 
C. Password recovery 
D. Email spam
_Explanation:_ As an intangible currency, Bitcoin must prevent double spending without a central authority; the blockchain provides a shared, ordered record of all spending.

**Q16. Complete Satoshi's idea: "The only way to confirm the absence of a transaction is to ___."** A. trust a central bank 
==B. be aware of all transactions ✓== 
C. know all private keys 
D. count all nodes
_Explanation:_ To know a coin hasn't already been spent, you need a common record of all past spending — hence a shared transaction history.

**Q17. How does the blockchain make the register practically impossible to rewrite?** 
==A. Each block includes the hash of the previous block's header ✓== 
B. Each block is signed by Satoshi 
C. Blocks are stored on government servers 
D. Each transaction is encrypted twice
_Explanation:_ Every block contains the previous block's header hash. Altering a past block changes its hash and breaks the link to every following block.

### Section 3 — Building a Bitcoin block (2.2)

**Q18. What is a candidate block?** 
A. A block already validated but not shared 
==B. A block prepared by a miner but not yet valid ✓== 
C. A block stored in the mempool 
D. A block created by a wallet
_Explanation:_ Each miner assembles a candidate block from mempool transactions before attempting to find a valid proof of work; it is not yet valid.

**Q19. What economic metric guides a miner's transaction selection?** 
A. Total fee amount 
==B. The fee rate (sats/vB) ✓== 
C. UTXO age 
D. Number of inputs
_Explanation:_ Because block space is limited, miners prioritize the highest fee rate — fees relative to the space used — to maximize revenue per byte.

**Q20. A Bitcoin block consists of which two main parts?** 
==A. A header and a list of transactions ✓== 
B. A nonce and a mempool 
C. Inputs and outputs only 
D. A wallet and a signature
_Explanation:_ A block has a list of transactions plus an 80-byte header that acts as the block's identity card.

**Q21. What is actually hashed during proof of work?** 
A. The full list of transactions 
==B. The 80-byte block header ✓== 
C. The block height 
D. The entire mempool
_Explanation:_ You don't mine the whole block — you mine only the header, which commits to the contents and links the block to the chain.

**Q22. What is the size of the block header?** 
A. 40 bytes 
B. 64 bytes 
==C. 80 bytes ✓== 
D. 256 bytes
_Explanation:_ The block header is exactly 80 bytes and contains exactly 6 fields.

**Q23. How many fields does the block header contain?** 
A. 4 
==B. 6 ✓== 
C. 8 
D. 10
_Explanation:_ The header has six fields: version, previous block hash, Merkle root, time, nbits, and nonce.

**Q24. What is the Merkle root?** 
A. The hash of the previous block 
==B. A single hash summarizing all transactions in the block ✓== 
C. The miner's address 
D. The difficulty target
_Explanation:_ The Merkle root is one hash derived from all transactions via the Merkle tree; changing any transaction changes the root.

**Q25. How is the Merkle root built?** 
A. By hashing only the first transaction 
==B. By hashing transactions, then pairing/concatenating/re-hashing repeatedly until one hash remains ✓== 
C. By adding all transaction amounts 
D. By signing each transaction
_Explanation:_ Transaction hashes are paired, concatenated, and hashed again layer by layer until a single final hash — the Merkle root — remains.

**Q26. Why can't all transactions simply be listed in the header?** 
==A. The header has a fixed, small size (80 bytes) ✓== 
B. Transactions are secret 
C. Nodes refuse to read them 
D. It would violate SegWit
_Explanation:_ A block may contain thousands of transactions while the header is fixed at 80 bytes; the Merkle root compresses them into one commitment.

**Q27. Since SegWit, how many Merkle trees are effectively nested in a block?** 
A. One 
==B. Two ✓== 
C. Four 
D. Sixty-four
_Explanation:_ SegWit separates signatures (witnesses) from the rest, creating effectively two nested Merkle trees, though the header still commits to all content.

**Q28. Which header field links a block to its predecessor?** 
A. nonce 
==B. previousblockhash ✓== 
C. merkleroot 
D. nbits
_Explanation:_ The previous block hash field is the hash of the prior block's header; it is what chains blocks together.

**Q29. Which header field encodes the current difficulty?** 
A. version 
B. time 
==C. nbits ✓== 
D. nonce
_Explanation:_ The nbits field encodes the active difficulty target in compact form.

**Q30. Who chooses the timestamp in the header, within validity constraints?** 
A. The node that relays the block 
==B. The miner ✓== 
C. The recipient of the transaction 
D. The Bitcoin Foundation
_Explanation:_ The time field is a Unix timestamp chosen by the miner (subject to validity constraints) indicating roughly when the block was mined.

### Section 4 — The hash, the target and the nonce (2.3)

**Q31. Which of the following is a property of a cryptographic hash function?** 
A. It is easily reversible 
==B. Changing one input bit changes the output completely and unpredictably ✓== 
C. Many inputs trivially share the same output 
D. It compresses without changing on edits
_Explanation:_ A hash function produces a fixed-size output where flipping a single input bit changes the output entirely; it is also irreversible and collision-resistant.

**Q32. Which hash function does Bitcoin mining use?** 
==A. SHA256d (SHA-256 applied twice) ✓== 
B. SHA512d 
C. SHA1d 
D. RIPEMD160d
_Explanation:_ Bitcoin mining uses double SHA-256: `hash = SHA256(SHA256(message))`, denoted SHA256d.

**Q33. The validity condition for a block is:** 
A. SHA256d(header) > target 
==B. SHA256d(header) ≤ target ✓== 
C. SHA256d(header) = target exactly 
D. SHA256d(header) ≥ target
_Explanation:_ A block is valid when its header hash, read as a number, is less than or equal to the difficulty target.

**Q34. The target is a number of how many bits?** 
A. 32 
B. 80 
==C. 256 ✓== 
D. 512
_Explanation:_ The target is a 256-bit number, the same size as the SHA256d output, so the two can be compared as numbers.

**Q35. If the target decreases, mining becomes:** 
A. Easier 
==B. Harder ✓== 
C. Impossible 
D. Unchanged
_Explanation:_ A lower target leaves fewer valid results below the threshold, so more attempts are needed — mining is harder.

**Q36. What makes proof of work an efficient system?** 
A. Producing and verifying both take equal effort 
==B. Producing a proof is costly but verifying it is fast and cheap ✓== 
C. Verification requires special hardware 
D. Only Satoshi can verify it
_Explanation:_ The key asymmetry: finding a valid hash takes enormous work, but any node verifies it with a single hash and comparison.

**Q37. Proof of work is best described as:** 
A. Solving a complex equation 
==B. A trial-and-error search for a valid hash ✓== 
C. A negotiation between nodes 
D. A vote among wallets
_Explanation:_ It's not really a problem to solve but a trial-and-error search: keep changing the header until its hash falls at or below the target.

**Q38. What is the size of the nonce field?** 
A. 16 bits 
==B. 32 bits ✓== 
C. 64 bits 
D. 256 bits
_Explanation:_ The nonce is a 32-bit value, giving about 4.29 billion possible values (0 to 2³²−1).

**Q39. What is the purpose of the nonce?** 
A. To store the difficulty 
==B. To vary the header so the miner can retry with a new hash ✓== 
C. To list transactions 
D. To set the block size
_Explanation:_ Changing the nonce changes the header and thus the hash, letting the miner make repeated independent attempts.

**Q40. Why is it called "proof of work"?** 
==A. "Proof" = instantly verifiable; "work" = it costs real computation/energy ✓== 
B. Because miners prove they own coins 
C. Because nodes work in shifts 
D. Because it proves a transaction is signed
_Explanation:_ "Proof" because any node can verify the hash in a fraction of a second; "work" because reaching that hash takes many attempts and real energy cost.

**Q41. According to Satoshi, proof of work neutralizes which attack?** 
A. Phishing 
==B. Sybil attack (mass identity creation) ✓== 
C. SQL injection 
D. Man-in-the-middle
_Explanation:_ Because the majority is the chain with the most accumulated work ("one CPU = one vote"), creating many fake identities/IPs gives no advantage, neutralizing Sybil attacks.

### Section 5 — History of proof of work (2.4)

**Q42. Who invented Hashcash?** 
A. Nick Szabo 
==B. Adam Back ✓== 
C. Hal Finney 
D. David Chaum
_Explanation:_ Hashcash, considered the invention of the proof-of-work principle, was proposed by Adam Back.

**Q43. In what year was Hashcash proposed?** 
A. 1993 
B. 1995 
==C. 1997 ✓== 
D. 2004
_Explanation:_ Hashcash was first proposed in 1997.

**Q44. What problem was Hashcash mainly designed to reduce?** 
A. Double spending 
==B. E-mail spam ✓== 
C. Lost private keys 
D. DNS phishing
_Explanation:_ Hashcash imposes a small computational cost per e-mail, making mass spamming expensive while leaving normal use cheap.

**Q45. Who conceived Bit Gold?** 
==A. Nick Szabo ✓== 
B. Satoshi Nakamoto 
C. Hal Finney 
D. Wei Dai
_Explanation:_ Bit Gold, a conceptual project for digital scarcity based on proof of work, was proposed by Nick Szabo.

**Q46. What does RPOW stand for?** 
A. Random Proofs of Work 
==B. Reusable Proofs of Work ✓== 
C. Recursive Proofs of Work 
D. Replayed Proofs of Work 
_Explanation:_ RPOW = Reusable Proofs of Work, proposed by Hal Finney in 2004 — proofs that could be exchanged rather than merely consumed.

**Q47. What new role did Bitcoin give to proof of work that its predecessors did not?** 
A. Encrypting messages 
==B. Deciding who writes the next block and making the register costly to falsify ✓== 
C. Replacing private keys 
D. Filtering spam
_Explanation:_ Hashcash, Bit Gold, and RPOW used PoW to impose cost/scarcity; Bitcoin gave it a central, collective role: choosing the next block writer and securing the ledger against tampering.

### Section 6 — Adjusting the difficulty target (2.5)

**Q48. What average block interval does Bitcoin target?** 
A. 1 minute 
==B. 10 minutes ✓== 
C. 30 minutes 
D. 60 minutes
_Explanation:_ Bitcoin aims for an average of one block every 10 minutes, measured over a long period rather than guaranteed per block.

**Q49. Why is the interval between blocks inherently variable?** 
A. Because of the deterministic nature of hashing 
==B. Because of the probabilistic nature of hashing ✓== 
C. Because nodes disagree 
D. Because the target changes every block
_Explanation:_ Each hash is an independent attempt with constant success probability, like a continuous lottery — so discovery times are random even at constant hashrate.

**Q50. After how many blocks is the difficulty target adjusted?** 
A. 210,000 
==B. 2,016 ✓== 
C. 2,100 
D. 4,096
_Explanation:_ Every 2016 blocks (~2 weeks) each node recalculates the target based on how long those blocks actually took.

**Q51. If the last 2016 blocks were found too quickly, what happens to the target?** 
A. It rises (easier) 
==B. It lowers (harder) ✓== 
C. It stays the same 
D. The block size grows
_Explanation:_ Blocks found too fast imply higher hashrate, so the network lowers the target to make mining harder and slow production back toward 10 minutes.

**Q52. What does the hashrate measure?** 
A. Transactions per second 
==B. Hashes (attempts) per second ✓== 
C. Bytes per second 
D. Blocks per day
_Explanation:_ Hashrate is the number of hash computations per second (H/s, TH/s, EH/s), i.e., attempts to find a hash below the target.

**Q53. In the formula Tn = To × (Ta / Tt), what is Tt?** 
A. The new target 
B. The actual elapsed time 
==C. The target time (1,209,600 seconds) ✓== 
D. The total hashrate
_Explanation:_ Tt is the target time — 2 weeks, or 1,209,600 seconds — against which the actual elapsed time Ta is compared.

**Q54. The difficulty adjustment per period is clamped to a maximum factor of:** 
A. 2 
==B. 4 ✓== 
C. 10 
D. 16
_Explanation:_ The actual time used is constrained to between one quarter and four times the old target — a factor-of-4 limit preventing abrupt swings.

**Q55. What is the consequence of the original "off-by-one" bug in difficulty adjustment?** 
==A. Blocks are mined ~0.05% slower than the 10-minute target ✓== 
B. The supply exceeds 21 million 
C. Difficulty never changes 
D. Blocks are mined twice as fast
_Explanation:_ The code measures 2015 intervals instead of 2016, so difficulty is slightly overestimated and blocks come ~0.05% slower than target. It's never been fixed (would require a hard fork).

**Q56. Why is the target stored as the compact nBits field instead of its full form?** 
A. To hide it from nodes 
==B. Because the full 256-bit value would take too much space ✓== 
C. Because it changes every second 
D. To encrypt it
_Explanation:_ Storing the raw 256-bit target would waste header space, so nBits encodes it compactly as an exponent byte plus a 3-byte coefficient.

**Q57. A discarded block from a temporary chain split is correctly called a:** 
A. Genesis block 
==B. Stale block ✓== 
C. Coinbase block 
D. Candidate block
_Explanation:_ When the network resynchronizes on the branch with more work, the abandoned block becomes a "stale block" (loosely, and incorrectly, an "orphan").

### Section 7 — Block reward (3.1)

**Q58. The block reward is composed of:** 
A. Subsidy + difficulty 
==B. Block subsidy + transaction fees ✓== 
C. Fees + nonce 
D. Hashrate + fees
_Explanation:_ The reward the winning miner collects is the block subsidy (new coins) plus all fees of the included transactions.

**Q59. What principle makes honest mining the rational strategy?** 
A. Altruism 
==B. Game theory — a cheating miner's block is rejected, wasting its cost ✓== 
C. Government regulation 
D. Random chance
_Explanation:_ The protocol makes honesty rational: valid blocks pay, but a cheating block is rejected by nodes, so its production cost is a direct loss.

**Q60. The block subsidy corresponds to:** 
A. Transaction fees 
==B. New monetary creation (bitcoins minted ex nihilo) ✓== 
C. A user deposit 
D. A spam penalty
_Explanation:_ The subsidy is the money-creation part of the reward: new bitcoins created from nothing, capped and defined by protocol.

**Q61. Which is NOT a stated role of the block subsidy?** 
A. Incentivizing mining and security 
B. Distributing new currency openly and neutrally 
==C. Guaranteeing a fixed BTC price ✓== 
D. Compensating miners when fees are low
_Explanation:_ The subsidy incentivizes participation/security and distributes currency neutrally; it does not control or guarantee price.

**Q62. Are transaction fees a dedicated output in a Bitcoin transaction?** 
A. Yes 
B. Yes, but only for SegWit transactions 
==C. No — fees are inputs minus outputs ✓== 
D. No, but they were before 2012
_Explanation:_ Fees are not an output; they equal total inputs minus total outputs — the value consumed but not recreated.

**Q63. A transaction has inputs of 100,000 and 150,000 sats and outputs of 35,000, 42,000, and 170,000 sats. What is the fee?** 
==A. 3,000 sats ✓== 
B. 5,000 sats 
C. 247,000 sats 
D. 250,000 sats
_Explanation:_ Inputs = 250,000; outputs = 247,000; fee = 250,000 − 247,000 = 3,000 sats.

**Q64. The fee rate is expressed in:** 
A. BTC per block 
==B. sats/vB (satoshis per virtual byte) ✓== 
C. hashes per second 
D. blocks per day
_Explanation:_ Competitiveness is measured as fee rate = fee / weight (vB), in satoshis per virtual byte.

**Q65. A transaction weighing 141 vB pays 1,974 sats. Its fee rate is about:** 
A. 7 sats/vB 
==B. 14 sats/vB ✓== 
C. 28 sats/vB 
D. 141 sats/vB
_Explanation:_ 1,974 / 141 ≈ 14 sats/vB.

**Q66. What is Bitcoin Core's default minimum relay fee threshold (minRelayTxFee)?** 
A. 1 sat/vB 
==B. 0.1 sat/vB ✓== 
C. 10 sats/vB 
D. 0 sats/vB
_Explanation:_ By default, Bitcoin Core won't relay transactions below 0.1 sat/vB (minRelayTxFee), one of the local policies protecting against spam.

**Q67. Why does limited block space create a fee market?** 
A. Miners set fixed prices 
==B. When demand for space exceeds supply, users bid higher fees to be included ✓== 
C. Nodes auction blocks to the public 
D. The protocol mandates rising fees
_Explanation:_ Block space is scarce (~one block per 10 minutes, limited capacity); when demand exceeds supply, fees rise as users compete for inclusion.

### Section 8 — Halving (3.2)

**Q68. What does a halving do?** 
A. Halves the difficulty target 
==B. Halves the block subsidy ✓== 
C. Halves transaction fees 
D. Halves the block size
_Explanation:_ Halving halves the block subsidy (the new coins per block); it does not affect transaction fees.

**Q69. A halving is triggered by:** 
A. A calendar date 
==B. Block height — every 210,000 blocks ✓== 
C. A vote of miners 
D. The difficulty adjustment
_Explanation:_ Halving occurs at every multiple of 210,000 in block height (~4 years), not on a fixed date.

**Q70. What was the block subsidy when Bitcoin launched in 2009?** 
A. 100 BTC 
==B. 50 BTC ✓== 
C. 25 BTC 
D. 12.5 BTC
_Explanation:_ The initial subsidy was 50 BTC per block, halving at each subsequent halving event.

**Q71. The formula for the subsidy after n halvings is:** 
A. 50 × 2^n 
==B. 50 / 2^n ✓== 
C. 21,000,000 / n 
D. 50 − n 
_Explanation:_ subsidy(n) = 50 / 2^n BTC; in code, the 50-BTC value is right-shifted by the number of halvings.

**Q72. At what block height did the fourth halving occur (April 20, 2024)?** 
A. 630,000 
==B. 840,000 ✓== 
C. 1,050,000 
D. 900,000
_Explanation:_ The fourth halving took place at height 840,000 on April 20, 2024, reducing the subsidy to 3.125 BTC.

**Q73. Approximately when does the upcoming fifth halving occur, and to what subsidy?** 
A. 2026, 3.125 BTC 
==B. Spring 2028 (est.), 1.5625 BTC ✓== 
C. 2030, 1 BTC 
D. 2032, 0.78 BTC
_Explanation:_ The fifth halving is estimated for spring 2028 at height 1,050,000, reducing the subsidy to 1.5625 BTC.

**Q74. Which halving is the last one, ending the subsidy?** 
A. The 21st 
==B. The 33rd ✓== 
C. The 64th 
D. The 38th
_Explanation:_ At the 33rd halving (block 6,930,000, ~year 2140) the subsidy falls below 1 satoshi and issuance ends.

**Q75. How many satoshis are in 1 BTC?** 
A. 1,000 
B. 1,000,000 
==C. 100,000,000 ✓== 
D. 21,000,000
_Explanation:_ 1 BTC = 100,000,000 sats; once the halved subsidy would fall below 1 sat, no further coins can be created.

**Q76. Why will there never be exactly 21,000,000 BTC?** 
A. Miners refuse to mine 
==B. The subsidy falls below 1 sat before reaching the theoretical total, plus rounding, under-claimed rewards, and lost coins ✓== 
C. The protocol caps it at 20 million 
D. Governments confiscate the rest
_Explanation:_ Due to satoshi granularity and rounding, issuance stops short of 21M; additional reductions come from under-claimed subsidies, genesis coins, historical bugs, and lost/destroyed coins.

### Section 9 — The coinbase transaction (3.3)

**Q77. Where is the coinbase transaction located in a block?** 
A. It is always the last transaction 
==B. It is always the first transaction ✓== 
C. It is in the header 
D. It is outside the Merkle tree
_Explanation:_ The coinbase is always the very first transaction in the block; it lets the winning miner receive the reward.

**Q78. What makes the coinbase transaction different from a normal transaction?** 
A. It has no TXID 
B. It has no outputs 
==C. It spends no real existing UTXO — it creates coins from scratch ✓== 
D. It is not in the Merkle tree
_Explanation:_ Unlike normal transactions, the coinbase consumes no real UTXO; it creates the subsidy from nothing and collects the fees.

**Q79. The coinbase input references a fake UTXO with which TXID and index?** 
A. A random TXID and index 0 
B. An all-zeros TXID and index 0xffffffff 
==✓ C. The previous block hash and index 1== 
D. The Merkle root and index 0xffffffff
_Explanation:_ The single coinbase input points to a non-existent UTXO: a TXID of all zeros followed by the index 0xffffffff.

**Q80. Is a block valid without a coinbase transaction?** 
A. Yes, if fees are zero 
B. Yes, for empty blocks 
==C. No — a block without a coinbase is rejected ✓== 
D. Only before BIP-34
_Explanation:_ The coinbase is mandatory; a block lacking one is invalid and systematically rejected by nodes.

**Q81. Since BIP-34 (2013), what must the coinbase scriptSig begin with?** 
A. The difficulty target 
==B. The block height ✓== 
C. The miner's hashrate 
D. The Merkle root
_Explanation:_ BIP-34 (version-2 blocks, from block 227,930) requires the coinbase scriptSig to start with the block's height, ensuring uniqueness.

**Q82. What is the extra-nonce, and where does it live?** 
A. A second header field 
==B. Extra search space placed in the coinbase scriptSig, used when the 32-bit nonce is exhausted ✓== 
C. A field in every transaction 
D. Part of the difficulty target
_Explanation:_ When the 32-bit nonce is fully tested, miners vary the extra-nonce in the coinbase scriptSig, changing the TXID → Merkle root → header, opening a fresh hash space.

**Q83. Since SegWit (2017), the witness commitment is recorded where?** 
A. In the version field 
==B. In a coinbase OP_RETURN output ✓== 
C. In the coinbase scriptSig 
D. In the previous block hash
_Explanation:_ SegWit groups witnesses in a separate Merkle tree whose root is committed in an OP_RETURN output of the coinbase transaction.

**Q84. The famous Genesis-block coinbase message references:** 
==A. A 2009 newspaper headline about a bank bailout ✓== 
B. A poem by Satoshi 
C. A list of early adopters 
D. The Bitcoin whitepaper title
_Explanation:_ Satoshi encoded "The Times 03/Jan/2009 Chancellor on brink of second bailout for banks" in hex in the Genesis coinbase scriptSig.

**Q85. After how many confirmations do coinbase outputs become spendable?** 
A. 6 
B. 100 
==C. 101 ✓== 
D. 210
_Explanation:_ Coinbase outputs have a 100-block maturity period, so 101 confirmations are required before they can be spent.

**Q86. Why does the coinbase have a maturity period?** 
A. To slow down miners 
==B. To prevent newly created reward coins from circulating before the block is deeply buried, avoiding reorganization cascades ✓== 
C. To collect extra fees 
D. To comply with tax law
_Explanation:_ If reward coins could be spent immediately and a reorg later abandoned the block, those coins (and downstream spends) would become invalid; maturity makes that scenario unrealistic.

### Section 10 — The mining industry (4.1 & 4.2)

**Q87. What hardware was mainly used to mine in Bitcoin's earliest days?** 
==A. CPU ✓== 
B. GPU 
C. FPGA 
D. ASIC
_Explanation:_ In 2009 and the early years, mining ran on ordinary computer CPUs, since difficulty was low enough.

**Q88. What does ASIC stand for?** 
A. Automated Silicon Integrated Circuit 
==B. Application-Specific Integrated Circuit ✓== 
C. Advanced Secure Integrated Circuit 
D. Application-Shared Integrated Circuit
_Explanation:_ An ASIC is an Application-Specific Integrated Circuit — a chip designed for one task: running SHA256d at maximum speed and efficiency.

**Q89. Why did mining move from CPUs to GPUs?** 
A. GPUs are cheaper to buy 
==B. GPUs excel at running the same operation in parallel across many cores ✓== 
C. GPUs use no electricity 
D. CPUs cannot compute SHA256
_Explanation:_ The bottleneck was parallelism; GPUs run identical operations across hundreds or thousands of cores, ideal for repeated hashing, yielding far more hashes/sec than a CPU.

**Q90. Between mid-2010 and mid-2011, mining difficulty multiplied by roughly:** 
A. 50 
B. 100 
==C. 1,000 ✓== 
D. 10,000
_Explanation:_ Difficulty rose by a factor of about 1,000 in that period, driven largely by the shift to GPUs.

**Q91. What intermediate hardware came between GPUs and ASICs?** 
A. TPUs 
==B. FPGAs ✓== 
C. DSPs 
D. Quantum chips
_Explanation:_ FPGAs — reprogrammable chips configured to implement SHA256d directly — bridged the GPU and ASIC eras, improving energy efficiency.

**Q92. What is the single most important factor for competitiveness in industrial mining?** 
A. Software licenses 
==B. Electricity cost ✓== 
C. Office ergonomics 
D. Wage costs
_Explanation:_ At scale, profitability hinges on cost per unit of computation, primarily driven by the cost of electricity.

**Q93. What is a mining farm?** 
A. A virtual grouping of dispersed miners 
==B. A physical site where one entity operates many ASICs ✓== 
C. A pool payout method 
D. A type of ASIC chip
_Explanation:_ A farm is a building or container site filled with ASICs running 24/7, operated by a single entity — distinct from a pool.

**Q94. What is the primary purpose of a mining pool?** 
A. To increase the block size 
==B. To reduce income variance by pooling hashrate ✓== 
C. To lower the difficulty target 
D. To manufacture ASICs
_Explanation:_ By combining many miners' hashrate, a pool finds blocks more often and pays members frequent fractions, smoothing out highly irregular solo income.

**Q95. Participants in a mining pool are often called:** 
A. Nodes 
==B. Hashers ✓== 
C. Validators 
D. Stakers
_Explanation:_ Pool participants are called "hashers" because they simply hash the data the pool sends, rather than performing all mining work themselves.

**Q96. Which statistical law explains why long-run block frequency converges to your share of hashrate?** 
A. Bayes' theorem 
==B. The law of large numbers ✓== 
C. The birthday paradox 
D. Principle of least action
_Explanation:_ Each hash is an independent trial; by the law of large numbers, the frequency of found blocks converges to your fraction of total network hashrate.

**Q97. A pool essentially "sells" what to its members?** 
A. Mining machines 
B. Larger blocks 
==C. Predictability ✓== 
D. Difficulty
_Explanation:_ The pool converts volatile, widely spaced solo income into regular payouts — it sells predictability, in exchange for shared rewards and fees.

**Q98. Which was the first Bitcoin mining pool (first block Dec 16, 2010)?** 
A. AntPool 
B. Foundry USA 
==C. Braiins Pool (formerly Slush Pool / Bitcoin.cz) ✓== 
D. F2Pool
_Explanation:_ Braiins Pool, formerly Slush Pool / Bitcoin.cz, was the first mining pool, mining its first block on December 16, 2010, and quickly reaching ~3.5% of global hashrate.

**Q99. 1 ZH/s (zetta-hash per second) equals:** 
A. 1 EH/s 
B. 10 EH/s 
C. 100 EH/s 
==D. 1,000 EH/s ✓==
_Explanation:_ 1 ZH/s = 1,000 EH/s = 10²¹ hashes per second — the order of magnitude of the global hashrate by early 2026.

**Q100. A farm and a pool differ in that:** 
A. They are the same thing 
==B. A farm is a physical single-operator site; a pool is a (usually virtual) grouping of dispersed miners ✓== 
C. A pool owns the machines; a farm rents them 
D. A farm cannot join a pool
_Explanation:_ A farm is one entity's physical site of machines; a pool coordinates many geographically dispersed miners. A farm can (and often does) participate in a pool.