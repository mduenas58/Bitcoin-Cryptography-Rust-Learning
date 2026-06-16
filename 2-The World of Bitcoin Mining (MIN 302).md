# The World of Bitcoin Mining (MIN 302) — Master Study Guide

> Course: **MIN 302 – The World of Bitcoin Mining** · Professor: Ajelex · Level: Advanced · Duration: 16 hours · Plan ₿ Academy Guest lecturers: Giw, Kristian, Alejandro de la Torre & Filippo Merli (DEMAND Pool), Mags, Kenobi, Jungly, Mechanic, Gianluca Goal: Take a deep dive into the mining industry — from energy source to mining pools, protocols, and geopolitics.

This guide has two parts:

1. **Key concepts, chapter by chapter** — a complete overview of all the material, structured for mastery.
2. **A 100-question quiz** — each question has a marked correct answer and an explanation.

> Prerequisite note: MIN 302 is the advanced companion to MIN 101. It assumes you already understand proof-of-work, the block header, the target/nonce, difficulty adjustment, the coinbase transaction, and halvings.

---

## Part A — Key Concepts by Chapter

### Part 1 — Introduction

#### 1.1 Course overview

MIN 302 is a comprehensive journey through the history, mechanics, and future of Bitcoin mining, originally recorded as an intensive two-day Lugano seminar and later reorganized for clear progression. It traces mining from CPU days and Satoshi's mining behavior through GPUs, FPGAs, and ASICs to global industrial scale. It covers proof-of-work, variance, and difficulty via the "dice game" analogy; hardware, infrastructure, and operational strategy (smart farm design, power-source selection, cooling, heat recovery); the geopolitical and economic implications (energy security, renewable integration, methane mitigation, community development) with case studies from Africa, Latin America, and Europe; and the cutting edge of decentralization protocols (Stratum V2, Ocean, Datum, Braidpool, Radpool). The goal is to understand mining's technical foundations and its environmental, economic, and social dimensions.

---

### Part 2 — Foundations of Bitcoin Mining

#### 2.1 Bitcoin Mining Evolution: CPU to Industrial Scale

- **Pre-history of PoW**: In **1992**, IBM researchers published a semi-proof-of-work system that was largely forgotten. **Adam Back** later independently reinvented the concept as **Hashcash**, establishing the core structure: create hashes and check difficulty via leading zeros.
- **Genesis block** (mined **January 3, 2009**): its header embeds The Times headline _"Chancellor on brink of second bailout for banks,"_ referencing the 2008 financial crisis. Its **50 BTC are permanently unspendable** (hardcoded), even by Satoshi. The Genesis hash is ~**20× lower** than required, suggesting Satoshi mined it for **5–6 days**; the next block came **6 days later on January 9**.
- **The Patoshi pattern**: discovered by **Sergio Demian Lerner in 2013** by examining **extra-nonce** values in early blocks. It revealed Satoshi's distinctive mining signature: **linear extra-nonce movements** different from other miners, and consistently **stopping before maximum efficiency** — suggesting Satoshi deliberately limited mining to avoid centralizing hash power. A **"double helix" pattern around block 1,400** (two interweaving slopes) indicates **two powerful CPUs** mining in parallel.
- **Satoshi's holdings** are estimated at **600,000–1.2 million BTC**, all unspent. Satoshi's mining **ceased July 8, 2010**, three days before the Slashdot publicity surge. A mysterious **24-hour gap in May 2010** with no blocks, followed by resumption, is theorized to be a **reorganization attack test** of Bitcoin's resilience while Satoshi held majority hash power.
- **CPU → GPU**: Despite Satoshi's **December 2009** plea for a "gentleman's agreement" against GPU mining, **Laszlo Hanyecz** published the **first open-source GPU mining** implementation in **May 2010** (initially inefficient, so CPU mining stayed viable until **mid-2011**). Laszlo also made **Bitcoin Pizza Day** (**May 22, 2010**): 10,000 BTC for pizza — the first real-world Bitcoin transaction; he spent **>100,000 BTC** total on ~eight pizzas.
- **Slashdot effect (July 11, 2010)**: a post about Bitcoin v0.3.0 caused a publicity surge and Bitcoin's **only maximum difficulty adjustment — a 300% increase** — as hundreds of miners joined; block times briefly dropped to **2.5 minutes** before difficulty restored the 10-minute target.
- **ArtForz**, the self-proclaimed "GPU king," wrote **proprietary** GPU mining software and ran the **"ArtFarm"** (24 GPUs, Bitcoin's first purpose-built mining facility), controlling an estimated **20–30%** of network hash rate in mid–late 2010.
- **ASIC revolution (2013)**: the first ASIC, an **Avalon miner delivered to Jeff Garzik in February 2013**, began the modern era — modest hash-rate gains over GPUs but **dramatically less electricity**. The arms race brought **Butterfly Labs, KnCMiner, Bitmain** (plus delays, customs issues, obsolescence). **Bitmain** became dominant, ~**75–80% of ASIC sales by 2017** with the commodity **Antminer S9**. Modern facilities consume hundreds of MW and house thousands of machines.

#### 2.2 From Dice Games to Industrial Operations

- **Mining as a dice game**: imagine players each rolling a **one-million-sided die**, trying to roll **below 10** to win the right to write the next block. This captures mining's essence: **outcomes are probabilistically predictable** (you can compute average time to a win), and the work is **hard to do but easy to verify** — verification is trustless and instant.
- **Self-adjusting difficulty**: if many players join and blocks come too fast, after ~**two weeks** the network performs a **difficulty adjustment** — conceptually swapping everyone's million-sided dice for **10-million-sided dice** (harder). If players leave and blocks slow, dice get **fewer sides** (easier). Fully automated, mathematically precise, no central control — keeping ~10-minute blocks.
- **Debunking the "complex math" myth**: mining requires **no intelligence or strategy** — just **endless repetition**. Each hash is like a dice roll: random output tested against a target; success depends only on chance and **volume of attempts**. Implication: the best tools are **specialized processors repeating one operation billions of times/sec**, and **quantum computers are not a threat** because the task is brute force, not advanced computation.
- **Hardware evolution**: CPU → GPU → **ASIC** (optimized solely for **SHA-256**). A single chip from a 5-year-old machine can **outperform 30 top GPUs** while using far less power; modern machines hold **150+ chips** doing trillions of hashes/sec.
- **Market structure**: dominated by **three Chinese manufacturers**. **Bitmain ~70%** share (Antminer). **MicroBT** is second, prioritizing reliability (premium **Whatsminer**). New entrants — **Blockstream, Block, Braiins** — aim to diversify the supply chain. **Custom firmware/auto-tuning** improves efficiency by **9–19%**. Pools have **commoditized** into a **"race to zero"** on fees.

#### 2.3 The Geopolitics of Bitcoin Mining

- **Energy security / infrastructure**: mining is a **third funding pathway** beyond taxes and utility rates. By committing to buy power **24/7**, miners give renewable projects **predictable, market-driven revenue**, accelerating payback and enabling builds in remote/transmission-limited areas. Their instant shutdown flexibility turns miners into **"virtual power plants"** that smooth supply/demand and absorb renewable intermittency.
- **Climate via waste energy**: **methane is 84× more potent than CO₂**. Miners monetize waste streams: farm **anaerobic digesters** (biogas from livestock waste), **flared associated gas** from oil & gas, and **landfill** methane capture. Striking figure: **just 35 landfills powering 320 MW could make the entire Bitcoin network carbon neutral.**
- **Economic sovereignty / censorship resistance**: nations can convert energy into **appreciating digital reserves** (unlike depleting extractive industries), breaking debt/dependency cycles tied to exporting raw goods. **El Salvador** integrates Bitcoin into national strategy despite lacking conventional strategic resources. Running **domestic pools** with significant hash power gives **censorship resistance** and inclusion even under sanctions.
- **Socioeconomic development**: mining infrastructure (power lines, internet, transport) acts as an **anchor tenant** that spills over to communities; long-term demand justifies investments that later serve households. **Heat recovery** warms homes, greenhouses, and agriculture. Case study: **Virunga National Park (Africa)** funds conservation and textile production with mining revenue, creating stable jobs.

---

### Part 3 — Mining and Energy Systems

#### 3.1 Symbiosis of Bitcoin Mining and Electrification

- **Two different worlds**: **Developing** regions (sub-Saharan Africa, India, parts of Latin America) face surging demand from population growth. Infrastructure builds in sequence — **generation → high-voltage transmission → substations → distribution** — so generation often arrives **5–10 years** before distribution/demand, creating **stranded energy**. Examples with strong generation but weak distribution: **Tanzania, Angola, Zambia, Mozambique**. **Developed** markets instead struggle to **integrate intermittent renewables** (matching variable wind/solar to demand).
- **Three grid-relevant traits of mining**: (1) **Geographic flexibility** — needs only stable internet and skilled staff; (2) **Short amortization** (~**5 years**) — fast deploy/relocate, matching infrastructure timelines; (3) **Load flexibility** — instant scale up/down with only minor restart costs.
- **Monetizing stranded energy**: e.g., **Ethiopia** monetizes excess hydro while distribution develops, earning **foreign currency**. Place mining **near generation** (high-voltage), not at distribution, to minimize transmission costs and avoid competing with retail consumers. **Electricity is ~80–85% of operating expenses**, so lowest cost is essential. The use is **temporary** — scale back/relocate as local demand grows.
- **Grid balancing in developed markets**: site miners at nodes with frequent imbalances or **negative pricing** to absorb surplus at low-but-positive rates. **Modular units (3–5 kW each)** allow precise matching. European studies: **removing miners can raise consumer bills 25%+**, since miners help cover fixed transmission/distribution costs.
- **Implementation/outlook**: best when one entity controls **both generation and mining**. Size mining to **average (not peak)** renewable output — a 100 MW solar farm at 20% capacity factor sustains ~**20 MW** steady mining. **High-voltage connections** have far lower fees. **Vertical integration** will dominate; majors like **Eletrobras, Saudi Aramco, TEPCO** are exploring mining.

#### 3.2 Gridless Mining

- **Strategic imperative**: **~600 million Africans lack electricity** (the continent most affected by energy poverty), yet Africa holds **~400 GW of potential hydro capacity**. Mining the network is geographically **concentrated**, a security risk; African **run-of-river hydro** offers a path to decentralization plus local energy access. **"Mining in the bush"** means fully **self-sufficient** remote operations, sometimes days from the nearest town.
- **Connectivity is the critical challenge**: mining needs constant pool communication — interruptions cause **rejected shares = lost revenue**. Solution: **redundant connectivity** — **Starlink** (primary, but periodic switch interruptions) plus **LTE** via high-gain directional antennas, multiple carriers, point-to-point wireless — all **bonded** so every packet goes across **all links simultaneously**. Comprehensive **local monitoring** (equipment, power, grid frequency, water levels, environment) is federated to the cloud.
- **Logistics**: "**bring everything you might possibly need**." Container transport takes **weeks** over poor roads at **10–15 km/h**, stopping at sundown (bush roads are dangerous in darkness). **Simplicity beats sophistication** — avoid smart PDUs and complex networking (failure points); carry redundant switches, spare LTE, full toolkits. Maintenance = **extended expeditions** (camp on site, bring food/gear).
- **Economics**: use **revenue-sharing** (not fixed rates), aligning incentives. Mining revenue historically **7–11 ¢/kWh** (>90% of days above 7¢); design to stay profitable at **6¢**. Producers often receive **~30% of gross revenue** — powerful with stranded energy (previously worth nothing). Remote miners can be **up to 70%** of a small grid's demand, requiring advanced load management; run-of-river hydro means adapting consumption to **water flow and community needs**. Outcomes: economic returns, renewable utilization, rural electrification, network decentralization.

#### 3.3 Designing Smarter Mining Farms

- **Core principle**: treat mining as a **resource-optimization problem**, not just maximizing hash rate. Components: **power source, cooling, infrastructure management**. The speaker (an industrial chemist with motorsport experience) built **Italy's first hydroelectric mining farm**.
- **History note**: before industrial mining (~2012), the first ASICs (e.g., Butterfly Labs' **"Jalapeño,"** USB-stick-sized) took nearly a year to ship — long lead times **persist today**. Each new chip generation rides an **efficiency curve** (less power for same hash rate), driving hardware-refresh planning.
- **Power source selection** (the most critical decision): **Hydro** = highest uptime, lowest cost. **Solar** is deceptive — peak kW ≠ all-day power (a **bell curve**, max only briefly at midday), so 24/7 mining needs **massive, expensive batteries**. Example: a 2-miner, **6.6 kW** load needs ~**160 kWh/day**, but a **15 kW** array in Lugano yields only **73.3 kWh** on the best summer day. Scaling to 100 kW can work, but **battery cost often exceeds the mining hardware**, and panel/battery production undercuts sustainability claims.
- **Cooling**: **Air** — simplest, but shortens hardware life and is **noisy** (noise is underestimated and kills urban projects). **Adiabatic** (evaporative) — good middle ground in **dry** climates (e.g., Texas). **Hydro/water cooling** — effective but needs custom water blocks per model and risks **leaks**. **Oil immersion** — most advanced: cools high-power rigs efficiently, can use free water sources; strongest long-term path.
- **Heat recovery**: nearly **all electricity becomes heat**, but **low-grade (<100 °C)** — unsuitable for steam, excellent for **space heating**. Uses: residential/industrial heating, greenhouses, food drying, pools. Real examples: **Manhattan's Bathhouse spa** (heats pools entirely with miners) and **Bitcoin Bloem** (Netherlands, heats flower greenhouses). Combining with **methane** fuel yields a **triple climate benefit** (cut emissions + heat + Bitcoin).
- **Profitability cycles**: each ASIC generation lowers older gear's profitability. Typical cycle: **order new miners 12–18 months ahead**, manufacturers using pre-order funds for R&D; arrange **sale of used gear before new arrives**. Delays can force running unprofitable machines (as in **2018**, when many lost money daily but mined to accumulate cheap BTC). The future: **smaller, heat-integrated, distributed** installs — turning heating bills into Bitcoin accumulation and aiding decentralization.

---

### Part 4 — Technical Advances in Mining Infrastructure

#### 4.1 Understanding Stratum V2 Mining Protocol

- **Header recap**: version, **prev-hash** (chains blocks), **Merkle root** (commitment to all transactions), **time** (Unix), **nbits** (difficulty), **nonce** (variable miners change). Mining sends the header to devices to find a hash **below target**. Search space = **2²⁵⁶** (a number with ~77 digits; the universe has ~10⁸² atoms).
- **Running out of nonce space**: modern devices at ~**100 TH/s** exhaust the **~4 billion** nonce values almost instantly. Extra rollable space: **prev-hash can't change**; **Merkle root** needs caution (commits transactions); **time** updates once/sec; using the **last two bytes of the version field** + nonce gives ~**300 trillion** combos — enough for one device, not large fleets.
- **Coinbase / extranonce**: to give thousands of devices unique work, change the Merkle root by modifying the **coinbase transaction**, which has an **"extranonce" field up to 96 bytes** with no semantic meaning. Pools typically reserve the **first 4 bytes** for miner identification and let miners vary the rest.
- **Actors**: **Template providers** (usually Bitcoin Core nodes) maintain the mempool, build templates, distribute them. **Pools** divide work via unique extranonces, manage payouts, and may control transaction selection.
- **Stratum V1 limitations**: only defined **pool→miner** communication (other links unspecified → trial-and-error compatibility); **JSON** encoding adds compute/bandwidth overhead at scale; and crucially it **centralizes transaction selection in pools** (miners just poll for templates), creating **censorship risk**.
- **Stratum V2**: from **Matt Corallo's 2018 "BetterHash" paper** + collaboration with **Braiins**. Three protocols: **Template Distribution Protocol** (node↔pool/miner template sharing), **Mining Protocol** (work distribution + share submission, replacing V1), and the **Job Declaration Protocol** (miners can **select their own transactions**). Uses **binary encoding** (not JSON), unique message-type IDs, and length-prefixed **framing**. The **Job Declaration Protocol** is its most revolutionary feature — restoring transaction-selection control to miners while keeping pooled reward/variance benefits.

#### 4.2 Beyond Protocol Wars to Practical Solutions

- **The real issue**: decentralization depends less on the **tool** (Stratum V2 vs. Datum, etc.) than on **participants' willingness** to prioritize decentralization over convenience/profit. **BitTorrent analogy**: the breakthrough was the shift to **decentralization**, not the specific protocol.
- **Centralization reality**: since **early 2024**, ~**90 Bitcoin addresses** capture everything from the blockchain, with **~90% of block rewards** flowing to **~five major pools**; many "independent" small pools are run by the **same entities (notably Bitmain)**, sharing custody. Miners have long accepted full **pool control over transaction selection/templates**, contradicting "**not your keys, not your coins**" and "**don't trust, verify**."
- **Ocean**: restores transparency/sovereignty — shows **templates before mining** (unlike pools that reveal blocks only after discovery), letting miners judge transaction policy. Offers **multiple template options** (Bitcoin Core default; an "all-disrespected" version accepting certain privacy transactions; a **data-free** template excluding arbitrary data) — miners have found blocks with **each**. Next step: the **Datum protocol** — miners run their **own nodes**, source transactions, and build **independent templates** while still sharing pooled rewards.
- **The FPPS problem**: **Full Pay Per Share** pays miners by hashrate **regardless of whether the pool finds blocks** — insurance that smooths variance. But Bitcoin income has shifted from predictable **50-coin subsidies** to **variable transaction fees** (congestion, fee spikes, spam/token launches), so short-term income is now unpredictable. To guarantee payments sustainably, FPPS providers must take **substantial margins**. Ocean's analysis: even during bad luck (three **empty blocks**, dry spells), Ocean miners earned **>10% above** FPPS counterparts — FPPS's true cost exceeds advertised fees.
- **Share marketplace**: Ocean's design gives FPPS-like stability **without centralization** — miners **sell shares** to buyers who pay upfront for the right to future block rewards when those shares win. Miners get **immediate cash flow**; buyers get newly mined BTC with **clear on-chain provenance** (useful for regulation); **Lightning** users can convert outbound capacity into eventual on-chain BTC. Ocean **coordinates but is never the counterparty**; prices set by **supply and demand**. Aggregating shares into **fewer outputs** saves block space. Goal: reduce centralized pool power so even extreme concentration poses minimal risk.

#### 4.3 Decentralizing Bitcoin Mining

- **Why pools exist**: reduce **payout variance**. Solo miners face long gaps and cash-flow problems; pooling makes discoveries frequent and shares payouts proportionally — turning irregular large rewards into steady income. Statistically, more participants → **variance shrinks relative to the mean**.
- **Four core pool functions**: (1) **validate shares**, (2) **store share data**, (3) **calculate rewards** (e.g., **PPLNS**), (4) **pay miners**. Easy with centralized databases/web apps; **hard in P2P**: must block **duplicate shares** network-wide, keep a **consistent share database** (re-creating problems Bitcoin itself solves), reach **Byzantine consensus** on rewards, and execute **trustless payouts** without duplication/failure.
- **P2Pool** — first serious fully decentralized attempt: a **blockchain of shares**. Every miner ran Bitcoin **and** P2Pool nodes, gossiping shares; PoW gave consensus and an immutable contribution record; **payouts embedded directly in Bitcoin coinbase transactions** (no separate coordination). **Two fatal flaws**: (1) the **linear share chain** created **race conditions** — orphaned shares earned nothing despite valid PoW; (2) **scalability** — paying everyone via the coinbase is capped by **block-size** limits.
- **Braidpool** — fixes the orphan problem with a **Directed Acyclic Graph (DAG)** of shares: multiple shares can reference the **same parent**, eliminating race conditions, so **all valid shares are compensated**. Payouts use **threshold signatures**: **Distributed Key Generation** creates shared public keys, and **Threshold Signature Schemes** let subsets sign without any single party holding the private key. Coinbase pays a **threshold key** with **timeout fallback** to designated miners (misbehavior lets one miner claim the whole reward — incentivizing honesty); subsequent off-chain transactions **accumulate rewards** without consuming block space.
- **Radpool** — introduces **Mining Service Providers (MSPs)** as intermediaries between miners and the consensus layer (two-tier), so not every miner runs a full node; miners connect via familiar **Stratum** interfaces. **MSP syndicates** maintain replicated share databases and consensus; participation rights are earned through **PoW proportional to hash rate**, preventing **Sybil** attacks. Its standout feature: **Discreet Log Contracts (DLCs)** enabling **decentralized futures markets** for mining rewards — MSPs can offer **FPPS contracts that absorb variance**, settled atomically and trustlessly, giving predictable income while preserving sovereignty.
- **Outlook**: Braidpool and Radpool face hard problems in **threshold signatures and distributed consensus** under adversarial conditions; scaling to hundreds of global participants is an open research problem. Success means beating centralized pools on performance while reducing concentration — strengthening decentralization and censorship resistance.

---

## Part B — 100-Question Quiz

For each question, the correct option is marked **✓** and followed by an explanation.

### Section 1 — Evolution: CPU to Industrial Scale (2.1)

**Q1. In what year did IBM researchers publish a semi-proof-of-work system later largely forgotten?** 
A. 1992 ✓ B. 1997 C. 2001 D. 2008 _Explanation:_ Bitcoin mining's lineage traces to a 1992 IBM semi-proof-of-work system that was largely forgotten before Adam Back independently reinvented the idea as Hashcash.

**Q2. What did Adam Back's Hashcash establish as the fundamental structure of mining?** 
A. Creating hashes and checking difficulty via leading zeros ✓ B. Staking coins to validate blocks C. Solving algebraic equations D. Voting by IP address _Explanation:_ Hashcash set the pattern we still use: produce hashes and check difficulty by requiring a number of leading zeros.

**Q3. What headline is embedded in the Genesis block header?** 
A. "Bitcoin: A Peer-to-Peer Electronic Cash System" B. "Chancellor on brink of second bailout for banks" ✓ C. "Banks collapse worldwide" D. "Digital gold is born" _Explanation:_ The Genesis block embeds The Times headline "Chancellor on brink of second bailout for banks," referencing the 2008 financial crisis that motivated Bitcoin.

**Q4. What is special about the 50 BTC in the Genesis block?** 
A. They were the first coins ever spent B. They are permanently unspendable (hardcoded) ✓ C. They were split among early miners D. They belong to Hal Finney _Explanation:_ The Genesis block's 50 BTC are hardcoded and permanently inaccessible — they cannot be spent, even by Satoshi.

**Q5. Roughly how much lower than required was the Genesis block's hash, and what does it suggest?** 
A. ~2× lower; a few minutes of mining B. ~20× lower; about 5–6 days of mining ✓ C. ~200× lower; several weeks of mining D. Exactly at target; instant mining _Explanation:_ Analysis shows the Genesis hash is ~20 times lower than necessary, suggesting Satoshi spent roughly 5–6 days mining it; the next block came 6 days later.

**Q6. Who discovered the Patoshi pattern, and in what year?** 
A. Sergio Demian Lerner, 2013 ✓ B. Adam Back, 2009 C. Laszlo Hanyecz, 2010 D. Matt Corallo, 2018 _Explanation:_ Sergio Demian Lerner identified the "Patoshi pattern" in 2013 through blockchain analysis of early-block extra-nonce values.

**Q7. What does Satoshi's habit of stopping before maximum efficiency suggest?** 
A. Faulty hardware B. A deliberate effort to avoid centralizing hash power ✓ C. Limited electricity D. A software bug _Explanation:_ Satoshi consistently stopped before reaching maximum efficiency, suggesting a deliberate choice to limit mining and avoid centralizing hash power, supporting decentralization.

**Q8. The "double helix" pattern around block 1,400 indicates Satoshi used:** 
A. A single GPU B. Two powerful CPUs mining in parallel ✓ C. An early ASIC D. A mining pool _Explanation:_ Two interweaving slopes ("double helix") in extra-nonce progression around block 1,400 suggest Satoshi ran two powerful CPUs in parallel.

**Q9. Satoshi's estimated holdings are in what range?** 
A. 50,000–100,000 BTC B. 600,000–1.2 million BTC ✓ C. 2–3 million BTC D. Exactly 1 million BTC _Explanation:_ Estimates place Satoshi's holdings between 600,000 and 1.2 million BTC, all remaining unspent.

**Q10. When did Satoshi's mining cease?** 
A. January 3, 2009 B. May 22, 2010 C. July 8, 2010 ✓ D. December 2009 _Explanation:_ Satoshi's mining stopped on July 8, 2010 — just three days before Bitcoin gained widespread Slashdot attention.

**Q11. What is the leading theory for the mysterious 24-hour no-block period in May 2010?** A. A power outage B. A reorganization attack test of Bitcoin's resilience ✓ C. A halving event D. A software update _Explanation:_ The leading theory is that Satoshi attempted a reorganization attack to test Bitcoin's resilience while controlling majority hash power.

**Q12. Who published the first open-source GPU mining implementation, and when?** A. ArtForz, 2011 B. Laszlo Hanyecz, May 2010 ✓ C. Jeff Garzik, 2013 D. Satoshi, December 2009 _Explanation:_ Laszlo Hanyecz published the first open-source GPU mining implementation in May 2010; it was initially inefficient, so CPU mining stayed viable until mid-2011.

**Q13. What is Laszlo Hanyecz also famous for?** A. Inventing ASICs B. Bitcoin Pizza Day — 10,000 BTC for pizza on May 22, 2010 ✓ C. Writing the Bitcoin whitepaper D. Founding Bitmain _Explanation:_ On May 22, 2010, Laszlo paid 10,000 BTC for pizza — the first real-world Bitcoin transaction; he spent over 100,000 BTC total on about eight pizzas.

**Q14. The Slashdot effect of July 11, 2010 triggered Bitcoin's only what?** A. Hard fork B. Maximum difficulty adjustment — a 300% increase ✓ C. Halving D. Network shutdown _Explanation:_ The publicity surge caused Bitcoin's only maximum difficulty adjustment — a 300% increase — as hundreds of new miners joined; block times briefly fell to 2.5 minutes.

**Q15. Who was the self-proclaimed "GPU king" running the "ArtFarm"?** A. ArtForz ✓ B. Laszlo Hanyecz C. Jeff Garzik D. Jihan Wu _Explanation:_ ArtForz used proprietary GPU mining software and ran the "ArtFarm" (24 GPUs, Bitcoin's first purpose-built mining facility), controlling ~20–30% of hash rate in mid–late 2010.

**Q16. The first ASIC (an Avalon miner) was delivered to whom, and when?** A. Satoshi Nakamoto, 2009 B. Jeff Garzik, February 2013 ✓ C. ArtForz, 2010 D. Adam Back, 2011 _Explanation:_ The first ASIC, an Avalon miner delivered to Jeff Garzik in February 2013, marked the beginning of the modern mining era.

**Q17. By 2017, which company dominated ASIC sales (~75–80%) with the Antminer S9?** A. MicroBT B. Butterfly Labs C. Bitmain ✓ D. KnCMiner _Explanation:_ Bitmain emerged dominant, controlling roughly 75–80% of ASIC sales by 2017 with its commodity Antminer S9.

### Section 2 — Dice Games to Industrial Operations (2.2)

**Q18. In the dice-game analogy, what must a player roll to win the right to write the next block?** A. The exact target number B. A number smaller than the target (e.g., below 10) ✓ C. The highest number D. An even number _Explanation:_ Players roll a million-sided die and whoever rolls below the target (e.g., under 10) wins the right to write transactions into the ledger — mirroring "hash below target."

**Q19. Which dual property does the dice game illustrate about mining?** A. Cheap to do, hard to verify B. Hard to do, easy to verify ✓ C. Hard to do, hard to verify D. Easy to do, easy to verify _Explanation:_ Mining is difficult to perform (many energy-spending attempts) but trivial and trustless to verify once a winning result is claimed.

**Q20. In the analogy, how does the network respond when too many players join and blocks come too fast?** A. It pauses mining B. It swaps in dice with more sides (e.g., 10-million-sided) ✓ C. It lowers the reward D. It removes players _Explanation:_ A difficulty adjustment conceptually replaces million-sided dice with 10-million-sided dice, making the target proportionally harder to restore ~10-minute blocks.

**Q21. According to the course, do miners solve complex math problems?** A. Yes, advanced calculus B. No — mining is endless repetition with no intelligence or strategy ✓ C. Yes, cryptographic equations D. Only during halvings _Explanation:_ Mining requires no reasoning; it's simply repeating a random trial against a target, with success determined by chance and volume of attempts.

**Q22. Why are quantum computers NOT considered a threat to mining itself?** A. They are too expensive B. The task is brute-force repetition, not advanced computation ✓ C. They cannot compute SHA-256 D. They are banned _Explanation:_ Mining relies on massive brute force through simple repetitive work, not advanced computation, so quantum speedups don't apply to the hashing race.

**Q23. ASICs in Bitcoin mining are optimized solely to compute what?** A. SHA-256 hashes ✓ B. RIPEMD-160 hashes C. Elliptic-curve signatures D. Random number generation _Explanation:_ Bitcoin ASICs are specialized exclusively for computing SHA-256 hashes, the function underlying Bitcoin's proof-of-work.

**Q24. Roughly how many specialized chips do modern mining machines typically contain?** A. About 10 B. About 50 C. 150 or more ✓ D. Exactly 256 _Explanation:_ Modern machines typically contain 150 or more specialized chips, performing trillions of hash calculations per second.

**Q25. Which manufacturer holds about 70% market share with the Antminer line today?** A. MicroBT B. Bitmain ✓ C. Canaan D. Braiins _Explanation:_ The industry is dominated by three Chinese manufacturers, with Bitmain holding roughly 70% share through its Antminer line.

**Q26. What does MicroBT, the second-largest manufacturer, prioritize with its Whatsminer series?** A. Lowest cost B. Reliability over cost optimization ✓ C. Smallest size D. Quietest operation _Explanation:_ MicroBT focuses on reliability over pure cost optimization with its premium Whatsminer series.

**Q27. Which of these is a new entrant aiming to diversify ASIC supply away from China?** A. Butterfly Labs B. KnCMiner C. Blockstream ✓ D. Avalon _Explanation:_ New entrants Blockstream, Block, and Braiins aim to reduce dependence on Chinese manufacturing and create more competitive dynamics.

**Q28. By how much can custom firmware auto-tuning improve mining efficiency?** A. 1–3% B. 9–19% ✓ C. 40–50% D. Over 100% _Explanation:_ Custom firmware with auto-tuning improves efficiency by 9–19% through individualized chip optimization.

**Q29. The mining-pool market has been experiencing what trend in fees?** A. Rapidly rising fees B. A "race to zero" in fees ✓ C. Fixed regulated fees D. Fees tied to BTC price _Explanation:_ Pools have become largely commoditized services, with the market experiencing a "race to zero" in fees.

### Section 3 — The Geopolitics of Bitcoin Mining (2.3)

**Q30. Bitcoin mining provides a "third pathway" for funding energy beyond which two traditional ones?** A. Loans and grants B. Taxes and utility rates ✓ C. Donations and bonds D. Exports and tariffs _Explanation:_ Mining creates a third funding pathway beyond taxes and utility rates by committing to buy power 24/7, giving projects predictable revenue.

**Q31. Why are miners described as "virtual power plants"?** A. They generate their own electricity B. Their instant shutdown flexibility smooths supply and demand ✓ C. They replace nuclear plants D. They store energy in batteries _Explanation:_ Miners can shut down instantly during peak demand without operational losses, smoothing fluctuations and helping grids absorb renewable intermittency.

**Q32. How much more potent than CO₂ is methane, per the course?** A. 10 times B. 25 times C. 84 times ✓ D. 300 times _Explanation:_ Methane is cited as 84 times more potent than CO₂, making its capture and reduction especially valuable.

**Q33. In agriculture, miners harness methane from livestock waste using what?** A. Solar panels B. Anaerobic digesters producing biogas ✓ C. Wind turbines D. Hydro dams _Explanation:_ Miners partner with farms to use anaerobic digesters, turning livestock-waste methane into biogas that powers mining while cutting emissions.

**Q34. According to the analysis cited, how many landfills powering 320 MW could make the entire Bitcoin network carbon neutral?** A. 5 B. 35 ✓ C. 100 D. 320 _Explanation:_ The course states that just 35 landfills powering 320 megawatts could make the entire Bitcoin network carbon neutral.

**Q35. Which country is highlighted as integrating Bitcoin into national strategy despite lacking conventional strategic resources?** A. Norway B. El Salvador ✓ C. Saudi Arabia D. Germany _Explanation:_ El Salvador demonstrates converting energy/strategy into Bitcoin, attracting investment and tourism despite lacking conventional strategic resources.

**Q36. How can a nation gain censorship resistance through mining?** A. By banning foreign miners B. By operating domestic pools and maintaining significant hash power ✓ C. By taxing transactions D. By controlling exchanges _Explanation:_ Running domestic pools with sufficient hash rate ensures inclusion in the global network and control over block participation even under sanctions.

**Q37. Which African case study funds conservation and supports textile production with mining revenue?** A. Serengeti B. Virunga National Park ✓ C. Kruger Park D. Lake Victoria _Explanation:_ Virunga National Park in Africa funds conservation and supports textile production with mining revenue, creating stable jobs.

### Section 4 — Symbiosis of Mining and Electrification (3.1)

**Q38. Which region is projected to experience the highest population growth (and energy demand) in coming decades?** A. Western Europe B. Sub-Saharan Africa ✓ C. East Asia D. North America _Explanation:_ Sub-Saharan Africa is projected to see the highest population growth, driving major increases in energy requirements.

**Q39. What is the correct sequence of electrical infrastructure development?** A. Distribution → substations → transmission → generation B. Generation → high-voltage transmission → substations → distribution ✓ C. Substations → generation → distribution → transmission D. Transmission → generation → distribution → substations _Explanation:_ Infrastructure develops sequentially — generation, then high-voltage transmission, then substations, then distribution — creating timing mismatches.

**Q40. Why does "stranded energy" arise in developing nations?** A. Generation arrives well before distribution networks and demand catch up (5–10 years) ✓ B. Too many miners use the grid C. Generators break down D. Exports consume all power _Explanation:_ Countries may build gigawatt generation and transmission, but distribution and demand can take 5–10 years to develop, leaving substantial unused capacity.

**Q41. What is mining's most distinctive grid-relevant trait?** A. High capital cost B. Geographic flexibility (needs only stable internet and skilled staff) ✓ C. Permanent siting D. Dependence on local markets _Explanation:_ Unlike industries tied to supply chains or markets, mining needs only stable internet and skilled staff, so it can deploy almost anywhere.

**Q42. What is the typical amortization cycle for mining hardware cited here?** A. 1 year B. About 5 years ✓ C. 10 years D. 20 years _Explanation:_ Short amortization cycles (~5 years) enable quick deployment and relocation, matching infrastructure-development timelines.

**Q43. Electricity typically represents what share of a miner's operating expenses?** A. 30–40% B. 50–60% C. 80–85% ✓ D. Over 95% _Explanation:_ Mining requires the lowest possible electricity cost because energy typically represents 80–85% of operational expenses.

**Q44. Where should mining operations be placed to maximize grid benefits and profitability?** A. At the distribution level near consumers B. Near high-voltage generation sources ✓ C. In city centers D. At substations only _Explanation:_ Locating near high-voltage generation minimizes transmission costs and avoids competing with retail consumers, maximizing both grid benefits and profitability.

**Q45. Which country is cited as monetizing excess hydro capacity via mining while distribution develops?** A. Ethiopia ✓ B. Norway C. Iceland D. Brazil _Explanation:_ Ethiopia has begun using Bitcoin mining to generate revenue (including foreign currency) from excess hydroelectric capacity while distribution infrastructure develops.

**Q46. In developed markets, miners help by absorbing power at nodes with what condition?** A. Fixed pricing B. Frequent imbalances or negative pricing ✓ C. Zero renewables D. High retail demand _Explanation:_ By siting at nodes with frequent imbalances or negative pricing, miners buy surplus that would otherwise cost producers money, benefiting producers, miners, and taxpayers.

**Q47. What modular unit size enables fine-tuned load balancing?** A. 3–5 kilowatts each ✓ B. 50–100 kilowatts each C. 1 megawatt each D. 0.1 kilowatts each _Explanation:_ Units consuming just 3–5 kW allow operations to scale precisely to match surplus capacity.

**Q48. European studies show removing miners from local grids often raises consumer bills by how much?** A. 5% B. 25% or more ✓ C. 50% D. They fall _Explanation:_ Removing miners can raise consumer bills by 25%+ because miners help cover fixed transmission and distribution costs.

**Q49. Which major energy firms are cited as exploring mining via vertical integration?** A. ExxonMobil, BP, Shell B. Eletrobras, Saudi Aramco, TEPCO ✓ C. Tesla, Google, Amazon D. EDF, Enel, Iberdrola _Explanation:_ Eletrobras, Saudi Aramco, and TEPCO are exploring mining, recognizing that direct control over energy assets offers lasting competitive advantage.

### Section 5 — Gridless Mining (3.2)

**Q50. Approximately how many people in Africa lack electricity access?** A. 100 million B. 300 million C. 600 million ✓ D. 1 billion _Explanation:_ About 600 million Africans lack electricity access, making it the continent most affected by energy poverty.

**Q51. What is Africa's approximate potential hydroelectric capacity?** A. 40 GW B. 100 GW C. 400 GW ✓ D. 1,000 GW _Explanation:_ The continent possesses nearly 400 GW of potential hydro capacity — a massive opportunity for cheap renewable energy.

**Q52. What does "mining in the bush" fundamentally require?** A. Grid connection B. Entirely self-sufficient operations ✓ C. Local utility partnership D. Urban proximity _Explanation:_ Remote African operations must be entirely self-sufficient, often days from the nearest major town by difficult roads.

**Q53. Why is connectivity the most critical technical challenge in remote mining?** A. Miners need to browse the web B. Interruptions cause rejected shares and lost revenue ✓ C. Pools require video calls D. Internet is illegal there _Explanation:_ Mining requires constant communication with pools; any interruption results in rejected shares and lost revenue.

**Q54. What is typically used as the primary connectivity in remote African mining?** A. Fiber optic B. Starlink satellite internet ✓ C. Dial-up D. Microwave relay only _Explanation:_ Starlink is the primary connection, supplemented by LTE and other links — though even Starlink experiences periodic interruptions as satellites switch.

**Q55. How is true connectivity redundancy achieved?** A. One very fast line B. Bonding multiple independent links so every packet goes across all simultaneously ✓ C. A single Starlink dish D. Restarting routers frequently _Explanation:_ Multiple links (Starlink, multi-carrier LTE, point-to-point wireless) are bonded so every data packet is sent across all available links at once.

**Q56. What equipment philosophy dominates remote mining logistics?** A. "Just-in-time delivery" B. "Bring everything you might possibly need" ✓ C. "Buy locally on site" D. "Minimize spare parts" _Explanation:_ With towns days away, every tool and spare must be planned and transported in advance — hence "bring everything you might possibly need."

**Q57. At roughly what speed do trucks transport mining containers over bush roads?** A. 60–80 km/h B. 40–50 km/h C. 10–15 km/h ✓ D. 100 km/h _Explanation:_ Trucks travel extremely slowly, often 10–15 km/h, with travel stopping at sundown because bush roads are too dangerous in darkness.

**Q58. What pricing model do most remote operations use instead of fixed electricity rates?** A. Spot-market pricing B. Revenue-sharing agreements with energy producers ✓ C. Flat monthly fees D. Pay-per-block _Explanation:_ Remote mining typically uses revenue-sharing agreements that align incentives and reduce risk, rather than fixed electricity rates.

**Q59. Historically, mining revenue averages what range per kWh?** A. 1–3 cents B. 7–11 cents ✓ C. 15–20 cents D. 25–30 cents _Explanation:_ Mining revenue historically averages 7–11 ¢/kWh, with over 90% of days above 7¢; operations are designed to stay profitable even at 6¢.

**Q60. In revenue-sharing, producers often receive about what share of gross revenue?** A. 10% B. 30% ✓ C. 50% D. 70% _Explanation:_ Miners supply equipment and expertise while producers often receive about 30% of gross revenue — especially attractive with stranded energy worth nothing before.

**Q61. Remote miners can represent up to what share of demand on small grids?** A. 10% B. 30% C. 70% ✓ D. 100% _Explanation:_ Remote miners often form the majority of demand on small grids — sometimes up to 70% — requiring advanced load management and coordination with generation.

### Section 6 — Designing Smarter Mining Farms (3.3)

**Q62. The key insight in smart farm design is to treat mining as what?** A. A hash-rate maximization contest B. A resource-optimization problem ✓ C. A real-estate investment D. A short-term trade _Explanation:_ The core insight is treating mining as a resource-optimization problem rather than simply maximizing hash rate.

**Q63. Which early ASIC was a USB-stick-sized unit that took nearly a year to ship?** A. Antminer S9 B. Butterfly Labs' "Jalapeño" ✓ C. Whatsminer M30 D. Avalon 6 _Explanation:_ The first ASIC devices, like Butterfly Labs' USB-stick-sized "Jalapeño," took nearly a year to ship — a long-lead-time problem that persists today.

**Q64. Which power source typically offers the highest uptime and lowest cost?** A. Solar B. Wind C. Hydroelectric ✓ D. Diesel _Explanation:_ Hydroelectric power typically provides the highest uptime and lowest costs, while solar requires complex, costly battery systems.

**Q65. Why is solar mining deceptive for 24-hour operations?** A. Panels are too cheap B. Generation follows a bell curve, peaking only briefly at midday ✓ C. Sunlight is constant D. It produces too much power _Explanation:_ Solar's peak kW rating doesn't translate to all-day power; output follows a bell curve, creating a mismatch with continuous mining without massive batteries.

**Q66. In the Lugano example, a 15 kW solar array produces only how much on the best summer day?** A. 20 kWh B. 73.3 kWh ✓ C. 160 kWh D. 250 kWh _Explanation:_ Even optimally, a 15 kW array yields only 73.3 kWh on the best summer days — insufficient for continuous operation without large batteries.

**Q67. What often makes scaled-up solar mining uneconomical?** A. Panel cost B. Battery capacity cost often exceeding the mining hardware investment ✓ C. Internet fees D. Cooling costs _Explanation:_ Required battery capacity can cost tens of thousands of dollars, often exceeding the mining hardware investment, and panel/battery production undercuts sustainability claims.

**Q68. Which cooling method's biggest underestimated downside is noise?** A. Air cooling ✓ B. Oil immersion C. Hydro cooling D. Adiabatic cooling _Explanation:_ Air cooling is simplest but shortens hardware life and generates disruptive noise — an underestimated factor that has doomed many urban mining projects.

**Q69. Which cooling approach is described as the most advanced and best long-term path?** A. Air cooling B. Adiabatic cooling C. Oil immersion cooling ✓ D. Fan-only cooling _Explanation:_ Oil immersion cooling can cool high-power rigs with minimal energy, integrate with free water sources, and combine efficiency and scalability — the strongest long-term path.

**Q70. Why is mining's waste heat unsuitable for generating steam?** A. It is too hot B. It is low-grade, below 100 °C ✓ C. It is toxic D. It fluctuates too much _Explanation:_ Nearly all consumed power becomes heat, but it is low-grade (below 100 °C) — unsuitable for steam, yet excellent for space heating.

**Q71. Which real example heats its pools entirely with mining rigs?** A. Bitcoin Bloem B. Manhattan's Bathhouse spa ✓ C. Virunga Park D. Riot's Rockdale site _Explanation:_ Manhattan's Bathhouse spa heats its pools entirely with mining rigs, demonstrating practical mining-based heating.

**Q72. Combining methane fuel with heat recovery yields what?** A. A single benefit B. A "triple climate benefit" (cut emissions + heat + Bitcoin) ✓ C. Higher emissions D. No measurable benefit _Explanation:_ Capturing biogas from farms or landfills cuts powerful greenhouse emissions while delivering heat and Bitcoin — a triple climate benefit.

**Q73. What is the typical lead time for ordering new ASIC miners?** A. 1–2 weeks B. 1–2 months C. 12–18 months in advance ✓ D. 3–5 years _Explanation:_ The typical cycle involves ordering new miners 12–18 months in advance, with manufacturers using pre-order funds for R&D.

**Q74. During 2018, why did many operations keep running unprofitable equipment?** A. To avoid taxes B. To accumulate Bitcoin at low prices ✓ C. Legal requirements D. Free electricity _Explanation:_ In 2018 many operations lost money daily but continued mining to accumulate Bitcoin at low prices, sometimes because new hardware was delayed.

### Section 7 — Stratum V2 Mining Protocol (4.1)

**Q75. The total set of possible hash outputs equals what?** A. 2^32 B. 2^128 C. 2^256 ✓ D. 10^82 _Explanation:_ The hash output space is 2²⁵⁶ — astronomically large; for perspective, the universe has an estimated 10⁸² atoms.

**Q76. At ~100 TH/s, how quickly do modern devices exhaust the nonce space?** A. They never exhaust it B. Almost instantly (the ~4 billion values) ✓ C. Once per day D. Once per block only _Explanation:_ Modern devices at ~100 terahashes/sec quickly exhaust the ~4 billion possible nonce values, requiring other header fields to be varied.

**Q77. To give thousands of devices unique work, miners modify the Merkle root by changing what?** A. The prev-hash B. The coinbase transaction ✓ C. The timestamp D. The version _Explanation:_ The most practical approach modifies the coinbase transaction, which changes the Merkle root and thus each device's header.

**Q78. How large is the coinbase "extranonce" field that carries no semantic meaning?** A. Up to 4 bytes B. Up to 32 bytes C. Up to 96 bytes ✓ D. Up to 256 bytes _Explanation:_ The coinbase contains an extranonce field of up to 96 bytes with no semantic meaning, divisible between pools and miners.

**Q79. How is the extranonce typically divided?** A. Miners take all of it B. Pools reserve the first four bytes for miner identification; miners modify the rest ✓ C. Pools take all of it D. It is split 50/50 by length _Explanation:_ Pools typically reserve the first four bytes for miner identification while letting miners modify the remaining bytes, ensuring unique block headers per device.

**Q80. What is the most important limitation of Stratum V1?** A. It is too fast B. It centralizes transaction selection entirely within pools, creating censorship risk ✓ C. It uses binary encoding D. It lacks payouts _Explanation:_ Stratum V1 centralizes transaction selection in pools — miners only poll for templates and cannot influence content — undermining decentralization.

**Q81. Stratum V2 emerged from whose 2018 research paper?** A. Satoshi Nakamoto's whitepaper B. Matt Corallo's "BetterHash" ✓ C. Adam Back's Hashcash D. Sergio Lerner's Patoshi analysis _Explanation:_ Stratum V2 grew out of Matt Corallo's 2018 "BetterHash" paper and subsequent collaboration with Braiins.

**Q82. Which Stratum V2 sub-protocol lets miners select their own transactions?** A. Template Distribution Protocol B. Mining Protocol C. Job Declaration Protocol ✓ D. Payout Protocol _Explanation:_ The Job Declaration Protocol — Stratum V2's most revolutionary feature — enables miners to choose their own transactions rather than accept pool-dictated choices.

**Q83. How does Stratum V2 encode messages, improving efficiency over V1?** A. JSON text B. Binary formats with length-prefixed framing ✓ C. XML D. Plain CSV _Explanation:_ Stratum V2 uses binary encoding rather than JSON, with unique message-type IDs and length-prefixed framing for efficient, reliable parsing.

### Section 8 — Beyond Protocol Wars (4.2)

**Q84. Since early 2024, roughly how many addresses capture everything from the blockchain, and how concentrated are rewards?** A. ~900 addresses; 50% to ten pools B. ~90 addresses; ~90% of rewards to about five pools ✓ C. ~9 addresses; all rewards to one pool D. ~9,000 addresses; evenly spread _Explanation:_ Since early 2024, about 90 addresses capture blockchain output, with roughly 90% of block rewards flowing to just five major pools — many secretly operated by the same entities.

**Q85. How does Ocean restore transparency compared to traditional pools?** A. It hides templates until after discovery B. It shows templates before mining begins ✓ C. It pays only in Lightning D. It bans transaction selection _Explanation:_ Unlike pools that reveal blocks only after discovery, Ocean shows templates before mining, letting participants decide whether they support the transaction policies.

**Q86. Which is one of Ocean's offered block template options?** A. A subsidy-free template B. A "data-free" template excluding arbitrary data ✓ C. A miner-less template D. A double-reward template _Explanation:_ Ocean offers options including Bitcoin Core's default, an "all-disrespected" version accepting certain privacy transactions, and a data-free template excluding arbitrary data.

**Q87. What does the Datum protocol let miners do?** A. Skip running nodes B. Run their own nodes, source transactions, and build independent templates ✓ C. Avoid sharing rewards D. Mine without electricity _Explanation:_ With Datum, miners run their own nodes, source transactions directly, and construct independent templates while still sharing pooled rewards.

**Q88. What does FPPS (Full Pay Per Share) guarantee?** A. Payment only when the pool finds a block B. Regular payments based on hashrate regardless of whether the pool finds blocks ✓ C. A fixed BTC price D. Zero fees _Explanation:_ FPPS pays miners by hashrate regardless of actual block discoveries, functioning as insurance that smooths Bitcoin's natural mining variance.

**Q89. Why has FPPS become increasingly problematic?** A. Block subsidies rose B. Income shifted from predictable subsidies to highly variable transaction fees ✓ C. Difficulty stopped adjusting D. Pools disappeared _Explanation:_ As subsidies halved and fees became significant and unpredictable (congestion, spam, token launches), the predictability that made FPPS feasible disappeared, forcing providers to take large margins.

**Q90. In Ocean's analysis, how did Ocean miners fare versus FPPS counterparts even during bad luck?** A. 10% worse B. More than 10% above FPPS pool counterparts ✓ C. Exactly equal D. 50% worse _Explanation:_ Even including three empty blocks and dry spells, Ocean miners earned more than 10% above FPPS counterparts, suggesting FPPS insurance's true cost exceeds advertised fees.

**Q91. In Ocean's share marketplace, what do buyers obtain by paying upfront?** A. Mining hardware B. The right to receive future block rewards when those shares win ✓ C. Pool ownership D. Voting rights _Explanation:_ Miners sell shares to buyers who pay upfront for the right to future block rewards when those shares win — giving miners immediate cash flow.

### Section 9 — Decentralizing Bitcoin Mining (4.3)

**Q92. What is the primary reason mining pools exist?** A. To increase difficulty B. To reduce payout variance ✓ C. To manufacture ASICs D. To set Bitcoin's price _Explanation:_ Pools exist mainly to reduce payout variance, turning irregular large rewards into smaller, steadier income aligned with each miner's contribution.

**Q93. What were P2Pool's two fatal flaws?** A. High fees and slow internet B. Linear share-chain race conditions (orphaned shares) and coinbase-based scalability limits ✓ C. No proof-of-work and no nodes D. Closed source and no payouts _Explanation:_ P2Pool's linear share chain orphaned some valid shares (no compensation), and paying everyone through the coinbase transaction was capped by block-size limits.

**Q94. How does Braidpool fix P2Pool's orphan problem?** A. By raising fees B. By replacing the linear share chain with a Directed Acyclic Graph (DAG) of shares ✓ C. By using a central database D. By removing proof-of-work _Explanation:_ Braidpool's DAG lets multiple shares reference the same parent, eliminating race conditions so all valid shares are compensated regardless of position.

**Q95. What cryptographic mechanism does Braidpool use for payouts?** A. Simple multisig B. Threshold signatures (Distributed Key Generation + Threshold Signature Schemes) ✓ C. Single private keys D. Hash time-locked contracts only _Explanation:_ Braidpool uses Distributed Key Generation to create shared public keys and Threshold Signature Schemes so subsets can sign without any single party controlling the private key.

**Q96. In Braidpool, what discourages misbehavior in the payout construction?** A. Fines B. Misbehavior lets a single miner claim the entire block reward ✓ C. Account bans D. Reduced hash rate _Explanation:_ Coinbase pays a threshold key with timeout fallback to designated miners; because misbehavior results in a single miner claiming the whole reward, honest behavior is incentivized.

**Q97. What does Radpool introduce between miners and the consensus layer?** A. Central exchanges B. Mining Service Providers (MSPs) ✓ C. Government regulators D. Hardware vendors _Explanation:_ Radpool introduces MSPs as intermediaries in a two-tier structure, so not every miner must run a full node; miners connect via familiar Stratum interfaces.

**Q98. How does Radpool prevent Sybil attacks?** A. KYC verification B. Participation rights earned through proof-of-work proportional to hash rate ✓ C. Membership fees D. Invitation only _Explanation:_ Influence reflects actual mining power because participation rights are earned through proof-of-work proportional to contributed hash rate, preventing Sybil attacks.

**Q99. What is Radpool's most innovative feature?** A. Free electricity B. Integration of Discreet Log Contracts (DLCs) for decentralized reward futures ✓ C. JSON encoding D. Air cooling _Explanation:_ Radpool integrates Discreet Log Contracts, enabling decentralized futures markets where MSPs can offer FPPS contracts that absorb variance, settled atomically and trustlessly.

**Q100. What shared challenge do Braidpool and Radpool face?** A. Lack of electricity B. Threshold signatures and distributed consensus under adversarial conditions, plus scaling ✓ C. No interest from miners D. Excessive centralization by design _Explanation:_ Both face complex implementation challenges around threshold signatures and distributed consensus in adversarial networks; scaling to hundreds of global participants is an open research problem.