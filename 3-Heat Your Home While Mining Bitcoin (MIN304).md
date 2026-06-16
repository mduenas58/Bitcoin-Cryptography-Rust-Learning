# Heat Your Home While Mining Bitcoin (MIN304) — Study Guide & Quiz

**Course:** Heat your home while mining bitcoins · **Professor:** Jim · **Level:** Advanced · **Duration:** 6 hours · **Course ID:** MIN304

**Project:** Attakai — repurposing a used Antminer S9 into a quiet, connected home Bitcoin heater.

This document has two parts:

1. **Concept Overview** — the main ideas of every chapter, condensed for revision and mastery.
2. **100-Question Quiz** — multiple-choice questions with the correct answer and an explanation for each.

---

# Part 1 — Concept Overview by Chapter

## Section 1 — Introduction

### 1.1 Course Overview

The course is built around **Attakai**, a hands-on project that turns a used **Antminer S9** into a home Bitcoin heater. It combines theory (how mining works, the industry, economics, geopolitics) with practice (sourcing hardware, flashing **BraiinsOS+**, networking, replacing fans, joining a pool, optimizing). Guides are by Ajelex, Jim and Rogzy on the Découvre Bitcoin platform. Core objectives: understand mining fundamentals, source a used S9 safely, build the DIY heater, and configure BraiinsOS+ to join a pool.

## Section 2 — Mining: Operation, Industry and Challenges

### 2.1 Explanation of Mining

- **Puzzle analogy:** Mining is hard to solve but easy to verify. The first miner to solve the puzzle broadcasts the solution; the network verifies it, the block is added to the **Timechain**, and the miner is rewarded.
- **Reward:** Started at 50 BTC per block (~every 10 minutes), **halves every 210,000 blocks (~4 years)**, was **6.25 BTC** in 2023. Reward = newly created bitcoins **+ transaction fees** (a fee auction for limited block space).
- **Hashing:** Mining means finding a valid, **irreversible hash** (SHA‑256). Manual computation is infeasible, so machines are used.
- **Hardware evolution:** **CPU → GPU → FPGA → ASIC.** ASICs do one calculation (SHA‑256) extremely efficiently. A typical S9 does ~14 TH/s; the whole network ~300 ExaHash/s (≈380 EH/s in later chapters).
- **Difficulty adjustment:** Every **2016 blocks** the network retargets difficulty to keep ~10‑minute blocks. Example: China's 2021 ban dropped network hashrate ~50%, and difficulty adjusted down to restore 10‑minute blocks — proving the mechanism's resilience.
- **Machine evolution:** S9 (2016) is old but still circulates second‑hand (~€100–200); S19 (2020) ~€3,000; newer S19 J / S19 XP add efficiency and liquid cooling. Future efficiency gains are expected to shrink as technology matures.

### 2.2 The Mining Industry

- **Mining pools:** Groups of miners combining hashpower to find blocks more often and share rewards proportionally (e.g., 1% of pool power → 1% of the 6.25 BTC). Pools usually charge ~2% commission.
- **Software:** As important as hardware. **Bitmain** makes the S9; pools like **Braiins Pool** hold ~5% of network hashrate. **BraiinsOS+** replaces stock firmware and can raise efficiency ~25%.
- **Regulation & electricity:** High European/French electricity prices and regulation discourage mining; miners chase cheap power, often in emerging countries or energy‑surplus regions. **Texas** (independent grid, surpluses) is a major hub.
- **Energy management:** Miners are a **flexible demand source** that can consume "orphaned"/surplus electricity (e.g., new dams before grid lines are ready, household solar), helping fund infrastructure and **stabilize grids** by adjusting demand rather than supply.
- **Centralization:** Large players (e.g., **Foundry**) dominate, risking transaction **censorship** and **51% attacks**. Countermeasures: **home mining**, **Stratum V2** (lets miners choose transactions), **open‑sourcing** mining software, and **geographic/actor diversification**.

### 2.3 Nuances of the Mining Industry

- **Principle of Attakai:** Place miners in buildings (homes, schools, hospitals, saunas, pools) and **reuse their heat**, distributing hashrate while doing something useful. Born from two friends' home‑mining experiment; obstacles (noise, no wired option) solved with **quieter fans** and a **Wi‑Fi adapter**.
- **Limits of decentralization:** Heat reuse works (a hall could be heated by 3–4 S19s at ~3000 W each). For any device, **1 kW electricity = 1 kW heat** — but the miner _also_ earns BTC. Long‑term scalability remains an open question.
- **Why BTC rewards:** Bitcoin has a fixed cap of **21 million**. Rewarding miners with new coins fairly distributes supply and pays for security; fees pay for transaction approval. By ~2032 reward < 1 BTC; by **2140** no new coins — miners live on **fees only**. The **Lightning Network** could reduce fees, raising questions about future miner income.
- **What belongs in a block:** Block space is **scarce and valuable**; Lightning channel opens/closes still settle on the base layer. The community debates "spam" vs. legitimate use; supply and demand will price block space.

### 2.4 Bitcoin Mining in the Bitcoin Protocol

- **Block Size Wars:** Showed miners do **not** hold ultimate power. Balance among **miners** (build blocks), **nodes** (verify/validate, can reject bad blocks), and **users** (choose which chain to use) preserves integrity.
- **Power of miners:** Satoshi's game theory aligns incentives so honest behavior is rewarded. Threats: **states** attacking mining, **hardware production centralized in China**. Responses: Intel making US mining chips, Block's open‑source **MDK**. Bitcoin's mission = **censorship‑resistant value exchange**, which is why **Proof of Stake is rejected**.
- **PoW vs PoS:** **PoW** is the **physical link** between the real world and Bitcoin — production needs real energy, anchoring the network and resisting capture. **PoS** lets large holders keep disproportionate power, reproducing existing wealth inequality and weakening decentralization.

### 2.5 Bitcoin Price and Hashrate — a Correlation?

- **Hashrate, price, profitability:** Bull markets spike machine orders (Avalon, Bitmain); delivery lag means machines ordered in a bull market arrive in a bear market (low price, high hashrate asymmetry). Judge Bitcoin's health by **cost (hashrate/electricity)**, not just price; cost is generally proportional to price.
- **Hashrate & reward:** Mining sets a rough **floor price** (miners would sell at a loss below it). Profitability calculators give a balanced view, though markets can be irrational.
- **Profit vs network:** Mining for profit risks centralization and environmental impact; mining for the network strengthens resilience but may be unprofitable. **Attakai** answers this by making home mining accessible, decentralizing, and turning waste heat into value.

### 2.6 Sovereignty and Regulation

- **Sovereignty before profit:** If mining a BTC costs more than buying it, buying is wiser — unless mining gives unique value (e.g., winter heating). Adage: **"Not your hashrate, not your reward"** — cloud mining and remote machines carry breakdown, power, and scam risks.
- **Virgin bitcoins:** Freshly mined, **no transaction history**, often **non‑KYC** (many pools require no ID). Valued by institutions as "clean" and less likely to be rejected by regulators/exchanges.
- **Is mining banned in Europe?** Not currently, but conceivable (China precedent). Best defense is **truthful education** against misleading anti‑mining campaigns (e.g., Greenpeace); broader hashrate distribution strengthens the European community.

## Section 3 — Home Mining and Heat Reuse

### 3.1 Attakai — Making Home Mining Possible and Accessible!

- **Attakai** means "the ideal temperature" in Japanese; initiative by @ajelexBTC and @jimzap21 with Découvre Bitcoin.
- **Why reuse ASIC heat:** Any electric heater gives **1 kW heat per 1 kW electricity** (Joule effect); newer radiators aren't more efficient, just more even. A miner produces the same heat **plus a BTC reward**, so heating with a miner beats a plain radiator regardless of BTC/electricity prices. (Satoshi, 2010: mining is cheapest where heat is needed.)
- **Radiator/server idea fails** because computing demand isn't tied to heating demand and bandwidth is limited; miners, by contrast, can be **switched on/off anytime** without harming the network.
- **Added value for Bitcoin:** Distributing miners across many homes **decentralizes hashrate**, making state seizure and 51% censorship harder. Out of the box a miner is unfit for home use (too noisy, no adjustment) — fixed via **hardware + software** mods. Bonus: KYC‑free sats as cashback on your heating bill.

### 3.2 Buying Guide for a Used ASIC

- **Antminer S9** (Bitmain, May 2016): ~1400 W, ~13.5 TH/s. Outdated but cheap, plentiful spare parts, ideal for modding. Buy P2P (eBay, LeBonCoin); variations (i, j) don't change the guide. France Feb 2023: ~€100–200.
- **Parts:** 3 hashboards, 1 control board (SD slot, Ethernet, connectors — the "brain"), 3 data cables, power supply (220 V), 2× 120 mm fans, a male C13 cable.
- **Verification ("Don't trust, verify"):** Power it on, check all hashboards work, test Ethernet/web login (IP like 192.168.x.x found via router), default credentials **root/root** (reset if they fail), check fans, expect noise/dust. Optionally disassemble to inspect hashboards. Partner **21energy** sells tested, cleaned S9s pre‑installed with BraiinsOS+ (code "decouvre" = 10% off).

### 3.3 Guide for Purchasing Hardware Modifications for the S9

- **Goal:** Turn a loud, bulky miner into a silent, connected heater (handyman skills; electrical risk — take precautions).
- **Main fans:** Replace stock fans with **Noctua NF‑A14 iPPC‑2000 PWM** (12 V), ~1200 W heat, ~31 dB; needs **140 mm→120 mm adapters** + 140 mm grilles.
- **PSU fan:** Replace with **Noctua NF‑A6x25 PWM** (12 V); needs **connector adapters** (×2).
- **Networking:** **Vonets VAP11G‑300** Wi‑Fi/Ethernet bridge (no subnet); can be powered from the PSU with a female 5.5×2.1 mm jack.
- **Optional:** **ANTELA 16A smart plug** (SmartLife app) for remote on/off and power monitoring.
- **Shopping list:** 2× 140→120 mm adapters, 2× NF‑A14 iPPC‑2000 PWM, 2× 140 mm grilles, 1× NF‑A6x25 PWM, electrician's "sugar" 2.5 mm², Vonets VAP11G‑300, optional ANTELA plug.

## Section 4 — Modifying the Software of an Antminer S9

### 4.1 Setting up a Vonets Wi‑Fi/Ethernet Bridge

A bridge takes the router's Wi‑Fi and feeds it to the miner over Ethernet. Power via USB; connect to the **VONETS_** network (password **12345678**); log in **admin/admin**; use **Wizard**; pick your network (**2.4 GHz only**); enter the source Wi‑Fi password (tick "Disable Hotspot" if not extending Wi‑Fi); **Apply** then **Reboot**. Once it appears as "VONETS.COM", connect its Ethernet to the ASIC and power the ASIC — it now works as if wired.

### 4.2 Resetting an Antminer S9

Reset to factory settings **2–10 minutes after startup**: press **Reset for 5 seconds**, release. It restores within ~4 minutes and restarts automatically (no need to power off). Needed when default credentials fail or BOS toolbox can't detect a password‑protected miner.

### 4.3 Installing BraiinsOS+ on an Antminer S9

Stock firmware is limited; **BraiinsOS+** (from the first Bitcoin mining pool) adds features like power adjustment. Easiest method = **BOS Toolbox**: power on and connect the miner, download BOS Toolbox (Windows/Linux), run **bos-toolbox.bat**. Use the **Scan** tab (e.g., range `192.168.1.0/24`) to find the miner's IP (note: a password blocks detection → reset). Then **Install** tab → enter IP → **Start**. After reboot, open the IP in a browser; login **root** with **no password**.

### 4.4 Configure BraiinsOS+

Log in via the device's local IP (root / no password). The **Dashboard** shows real‑time **temperature, hashrate, and status** graphs, plus real hashrate, average chip temperature, **efficiency in W/TH**, power consumption, **fan speed (% and RPM)**, per‑hashboard temperature/voltage/frequency, active **Pools**, and **Tuner Status**. Other areas: **Configuration**, **System**, and **Quick actions**.

## Section 5 — Modification of the Fans

### 5.1 Replace the Power Supply Fan

**Prerequisite:** BraiinsOS+ (or other power‑reducing firmware) must already be installed, because quieter fans dissipate less heat. **Materials:** 1× Noctua NF‑A6x25 PWM, 2.5 mm² electrician's sugar. **Safety:** unplug the miner. Steps: remove 6 side screws, open case, remove plastic cover; unscrew old fan and peel its glue carefully. The new fan's connector differs (3 wires incl. an unused **yellow** speed wire) — use an adapter, or splice with sugar: strip the new fan's sheath ~1 cm, join **black‑black and red‑red**, cut the yellow flush, optionally tape. Install the new fan + grille respecting the **airflow arrow pointing into the case**. Optionally power the Vonets bridge from the 12 V output via a 5.5 mm jack (only if electrically skilled — else use a USB charger). Replace cover over the case and re‑screw.

### 5.2 Replacing the Main Fans

**Prerequisite & safety:** same as 5.1 (BraiinsOS+ installed; unplug first). **Materials:** 2× 140→120 mm 3D adapters, 2× Noctua NF‑A14 iPPC‑2000 PWM, 2× 140 mm grilles. Steps: disconnect/unscrew old fans; trim the new connectors' plastic tabs to fit; attach the 3D adapters with the old fan screws (don't over‑tighten — risk of touching a capacitor); mount fans with the supplied screws, **airflow arrows running Ethernet‑port side → opposite side**; connect fans and attach grilles (2 opposite‑corner screws each). Secure case and PSU with cable ties; connect the Vonets bridge to the Ethernet port and its power. Result: a much quieter miner.

## Section 6 — DIY Heating Configuration

### 6.1 Joining a Mining Pool

A pool is like a **farming cooperative** — pooled hashes reduce income variance. Solo mining an S9 is a near‑hopeless lottery (~1 in 24,777,849 per block, ~1 in 172,068 per day, ~471 years on average), though rare solo wins happen. **Reward models:** Braiins Pool's **Score** rewards long uptime (bad for an on/off heater) and has a high **100,000 sat** on‑chain minimum. Better for heating: **PPS** (pay per valid share) and **FPPS** (shares + transaction fees). Recommended: **Linecoin Pool (FPPS)** — rich dashboard, Paynym/BIP‑47 privacy, Telegram bot, app automations, BTC‑only, but 100,000 sat minimum; and **Nicehash (PPS)** — Lightning withdrawals, 2,000 sat minimum, but routes hashrate to the most profitable chain (may not aid Bitcoin's hashrate). Configure by creating a pool account, copying the **Stratum address + username** into BraiinsOS+ (password can be left empty).

### 6.2 Optimizing the Performance of Your Antminer S9

**Overclocking/underclocking/autotuning** all adjust hashboard frequencies. **Overclocking** raises frequency/hashrate; **underclocking** lowers it, cutting heat → lower fan speed → **less noise** (ideal for home). BraiinsOS+ supports all three. History: **AsicBoost** (2018) cut costs ~13%; **autotuning** goes further by tuning **each chip individually** (chips vary; makers set one conservative frequency for all), giving higher **hash/watt**. Manufacturers avoid it because customers want predictable, uniform performance and it's costly to develop. BraiinsOS+ autotuning can improve performance **up to ~20%**.

## Section 7 — Final Section

**7.1 Reviews & Ratings**, **7.2 Final exam**, **7.3 Conclusion.** The course closes by inviting learners to build their Attakai, mine their first KYC‑free sats while heating their space, and contribute to Bitcoin's decentralization.

---

# Part 2 — 100-Question Quiz

Each question lists four options; the correct answer is marked **(✓)** and followed by an **Explanation**.

### Section 1 — Introduction

**Q1. What is the central DIY project the MIN304 course is built around?**

- A. Building an ASIC chip from scratch
- B. Attakai — turning a used Antminer S9 into a home Bitcoin heater **(✓)**
- C. Mining altcoins with a GPU rig
- D. Running a cloud-mining business

**Explanation:** The whole course centers on Attakai, repurposing a used S9 into a quiet, connected home heater that mines Bitcoin.

**Q2. Which of these is NOT a stated learning objective of the course?**

- A. Understand Bitcoin mining fundamentals
- B. Source a used Antminer S9 safely
- C. Configure BraiinsOS+ and join a mining pool
- D. Design a new Proof of Stake blockchain **(✓)**

**Explanation:** The objectives are mining fundamentals, safe S9 sourcing, building the heater, and configuring BraiinsOS+ to join a pool. Designing PoS is not among them.

**Q3. According to the course structure, what does Section 2 mainly cover?**

- A. Replacing fans
- ==B. The technical functioning, industry, economics, and geopolitics of Bitcoin mining **(✓)**==
- C. Installing BraiinsOS+
- D. Joining a mining pool

**Explanation:** Section 2 gives a comprehensive understanding of mining: how it works, its role in the protocol, and its economic and geopolitical implications.

### Section 2.1 — Explanation of Mining

**Q4. Which analogy is used to explain mining?**

- A. A lock and key
- ==B. A puzzle: hard to solve, easy to verify **(✓)**==
- C. A relay race
- D. A spreadsheet

**Explanation:** Mining is compared to a puzzle — complex to solve but easy for the network to verify once a solution is presented.

**Q5. What is the main tool miners use in the Bitcoin network today?**

- A. ASICs **(✓)**
- B. CPUs
- C. FPGAs
- D. GPUs

**Explanation:** Miners now exclusively use ASICs dedicated to SHA‑256, optimized for maximum attempts at minimum energy.

**Q6. What was the initial block reward when Bitcoin launched?**

- A. 6.25 BTC
- B. 12.5 BTC
- C. 50 BTC **(✓)**
- D. 25 BTC

**Explanation:** The reward began at 50 bitcoins per block (about every ten minutes).

**Q7. How often does the block reward halving occur?**

- A. Every 2016 blocks
- B. Every 210,000 blocks, roughly every four years **(✓)**
- C. Every year
- D. Every 100,000 blocks

**Explanation:** The reward halves every 210,000 blocks, approximately every four years.

**Q8. The current mining reward (as of the course, 2023) consists of what?**

- A. The creation of new bitcoins only
- B. The creation of new bitcoins and transaction fees **(✓)**
- C. Transaction fees only
- D. New bitcoins plus a bonus for the fastest miner

**Explanation:** The reward is twofold: newly created bitcoins (6.25 BTC in 2023) plus the transaction fees of included transactions.

**Q9. How do transaction fees behave in Bitcoin?**

- A. They are fixed by the protocol
- B. They function like an auction where users bid to be included in the next block **(✓)**
- C. They are set by mining pools
- D. They are paid by miners to users

**Explanation:** Fees act as an auction — users indicate how much they will pay to have a transaction included; miners pick the most profitable ones.

**Q10. The hash produced in mining is best described as:**

- A. Reversible and editable
- B. Irreversible, like potatoes turned into mashed potatoes **(✓)**
- C. Easily computed by hand
- D. Different on every network node

**Explanation:** A found hash is irreversible; the analogy of mashing potatoes illustrates a one‑way function.

**Q11. What is the correct historical order of mining hardware evolution?**

- A. ASIC → FPGA → GPU → CPU
- B. CPU → GPU → FPGA → ASIC **(✓)**
- C. GPU → CPU → ASIC → FPGA
- D. FPGA → CPU → GPU → ASIC

**Explanation:** Mining evolved from CPUs to GPUs, then FPGAs, which served as a platform for developing ASICs.

**Q12. What is the main advantage of ASICs for mining?**

- A. They perform many types of calculations
- B. They perform one specific calculation (SHA‑256) very efficiently **(✓)**
- C. They are cheaper than CPUs
- D. They never need cooling

**Explanation:** Unlike general‑purpose CPUs, ASICs are optimized to do one calculation — SHA‑256 — as efficiently as possible.

**Q13. Roughly what hashrate does a typical S9-class miner achieve?**

- ==A. 14 TH/s (14 trillion attempts per second) **(✓)**==
- B. 14 MH/s
- C. 14 GH/s
- D. 14 PH/s

**Explanation:** A typical miner reaches ~14 TeraHash per second — 14 trillion attempts each second.

**Q14. How often does the network adjust mining difficulty?**

- A. Every 10 minutes
- B. Every 2016 blocks **(✓)**
- C. Every 210,000 blocks
- D. Every day

**Explanation:** Difficulty is retargeted every 2016 blocks based on the average time taken to mine the previous blocks.

**Q15. What is the purpose of the difficulty adjustment mechanism?**

- A. To make mining progressively harder forever
- B. To keep the average block time around 10 minutes regardless of total hashpower **(✓)**
- C. To stop one miner mining consecutive blocks
- D. To reduce electricity use

**Explanation:** It keeps blocks coming roughly every 10 minutes no matter how many miners or how much computing power exists — hence "Timechain."

**Q16. What happened to global hashrate after China's 2021 mining ban, and how did Bitcoin respond?**

- A. Hashrate doubled; difficulty rose
- B. Hashrate dropped ~50%; difficulty adjusted down to restore ~10-minute blocks **(✓)**
- C. Nothing changed
- D. The network halted for weeks

**Explanation:** China's ban cut hashrate ~50%, and the difficulty adjustment reduced difficulty to keep block times near 10 minutes, demonstrating resilience.

**Q17. Why is the Bitcoin blockchain also called the "Timechain"?**

- A. Because blocks are timestamped by governments
- B. Because difficulty adjustment keeps blocks at a steady ~10-minute cadence over time **(✓)**
- C. Because transactions expire after a set time
- D. Because it tracks time zones

**Explanation:** The constant ~10-minute block interval, maintained by difficulty adjustment, gives the chain a reliable timing property.

**Q18. According to the course, what is the approximate second-hand price range of an Antminer S9 (France, early 2023)?**

- A. €100 to €200 **(✓)**
- B. €1,000 to €2,000
- C. €3,000
- D. Under €20

**Explanation:** The older S9 trades around €100–200 second-hand, versus ~€3,000 for a newer S19.

**Q19. Which newer model is cited as featuring a liquid cooling system for better efficiency?**

- A. Antminer S9i
- B. Antminer S19 XP **(✓)**
- C. Antminer S7
- D. Avalon 741

**Explanation:** The S19 XP is noted for a liquid cooling system enabling a significant efficiency improvement.

**Q20. What does the course predict about future mining-efficiency gains?**

- A. They will accelerate indefinitely
- B. They will likely shrink as the technology matures and nears a threshold **(✓)**
- C. They will stop entirely tomorrow
- D. They are irrelevant to the industry

**Explanation:** Innovation continues, but future efficiency gains are expected to be smaller as the sector matures.

### Section 2.2 — The Mining Industry

**Q21. What is a mining pool?**

- A. A reservoir of cooling water for ASICs
- B. A group of miners combining computing power to find blocks more often and share rewards **(✓)**
- C. A government registry of miners
- D. A type of mining software

**Explanation:** A pool pools hashpower so members find blocks more frequently and split rewards in proportion to contribution.

**Q22. If a pool finds a block worth 6.25 BTC and you contributed 1% of its power, what is your share?**

- A. 6.25 BTC
- B. 0.0625 BTC **(✓)**
- C. 0.625 BTC
- D. 1 BTC

**Explanation:** Rewards are proportional: 1% of 6.25 BTC = 0.0625 BTC (before the pool's commission).

**Q23. What commission do mining pools typically charge?**

- A. Around 2% **(✓)**
- B. Around 25%
- C. Around 50%
- D. Nothing

**Explanation:** Pools usually charge a small commission, around 2%, to cover operating costs.

**Q24. Approximately what share of global hashrate does Braiins Pool control, per the course?**

- A. ~5% **(✓)**
- B. ~51%
- C. ~25%
- D. ~80%

**Explanation:** Braiinspool is said to control approximately 5% of the global network hashrate.

**Q25. By roughly how much can BraiinsOS+ increase a machine's efficiency?**

- A. ~25% **(✓)**
- B. ~2%
- C. ~100%
- D. ~5%

**Explanation:** Replacing stock firmware with BraiinsOS+ can increase efficiency by about 25% — more hashrate for the same electricity.

**Q26. Which company manufactures the Antminer S9?**

- A. Intel
- B. Bitmain **(✓)**
- C. Foundry
- D. Nicehash

**Explanation:** Bitmain is the prolific manufacturer that developed the Antminer S9.

**Q27. Why do European/French locations generally not attract miners?**

- A. Lack of internet
- B. High electricity tariffs and regulation **(✓)**
- C. Too cold
- D. No ASIC availability

**Explanation:** High electricity costs and regulation in Europe make it unattractive; miners seek cheap power elsewhere.

**Q28. Why is Texas a major mining hub?**

- A. It has the cheapest ASICs
- B. Its independent grid often overproduces, creating cheap surplus electricity **(✓)**
- C. It mandates mining
- D. It has the coldest climate

**Explanation:** Texas's independent grid produces surplus power to avoid shortages; miners exploit that overproduction at very low rates.

**Q29. How can Bitcoin miners help stabilize power grids?**

- A. By selling surplus energy back to the grid
- B. By acting as a flexible demand buffer, adjusting demand rather than supply **(✓)**
- C. By storing energy in large batteries
- D. By generating their own electricity

**Explanation:** Miners can absorb surpluses and switch off when local demand rises, balancing grids by adjusting demand.

**Q30. What is "orphaned" electricity in the mining context?**

- A. Electricity stolen from the grid
- B. Wasted or untapped power, e.g., from a new dam before distribution lines are ready **(✓)**
- C. Electricity from decommissioned plants
- D. Power lost to ASIC inefficiency

**Explanation:** Miners act as flexible demand that consumes otherwise-wasted "orphaned" electricity, helping offset infrastructure costs.

**Q31. Which large player is named as dominating the market and raising centralization concerns?**

- A. Foundry **(✓)**
- B. Noctua
- C. Vonets
- D. EDF

**Explanation:** Foundry is cited as a large player whose dominance risks transaction censorship and centralization.

**Q32. A 51% attack occurs when an actor controls what?**

- A. More than 50% of all bitcoins
- B. More than 50% of the network's hashing power **(✓)**
- C. More than 50% of the nodes' bandwidth
- D. More than 50% of the mining pools' fees

**Explanation:** Controlling over 50% of hashing power lets an actor manipulate and potentially censor the network.

**Q33. Which protocol lets individual miners choose which transactions to include, improving censorship resistance?**

- A. Stratum V1
- B. Stratum V2 **(✓)**
- C. Lightning Network
- D. Proof of Stake

**Explanation:** Unlike its predecessor, Stratum V2 gives miners control over transaction selection, reducing pool influence.

**Q34. Which of the following is NOT listed as a strategy against mining centralization?**

- A. Home mining
- B. Open-sourcing mining software
- C. Diversifying actors and geography
- D. Switching Bitcoin to Proof of Stake **(✓)**

**Explanation:** The anti-centralization strategies are home mining, Stratum V2, open-sourcing software, and diversification — not PoS, which the community rejects.

### Section 2.3 — Nuances of the Mining Industry

**Q35. What is the principle of Attakai?**

- A. Using renewable energy only
- B. The productive reuse of heat generated by Bitcoin mining **(✓)**
- C. Advanced liquid cooling
- D. Low-energy hardware design

**Explanation:** Attakai places miners in buildings to reuse their heat, decentralizing hashrate while doing something useful.

**Q36. For every 1 kW of electricity, how much heat does both an electric radiator and a miner produce?**

- A. 1 kW of heat **(✓)**
- B. 0.5 kW
- C. 2 kW
- D. It depends on the device's efficiency

**Explanation:** Energy and heat are equivalent: 1 kW of electricity yields 1 kW of heat in either device. The miner just adds a BTC reward.

**Q37. According to the course, why is heating with a miner economically better than a plain electric radiator?**

- A. The miner uses less electricity
- B. The miner produces the same heat AND earns a bitcoin reward **(✓)**
- C. The miner produces more heat per kW
- D. The miner is silent by default

**Explanation:** Both produce identical heat per kW, but the miner additionally earns BTC — an extra economic incentive.

**Q38. What is Bitcoin's fixed supply cap?**

- A. 21 million **(✓)**
- B. 210,000
- C. 100 million
- D. Unlimited

**Explanation:** Bitcoin is capped at 21 million units; mining rewards are how new coins are fairly distributed.

**Q39. By approximately what year will no new bitcoins be created?**

- A. 2032
- B. 2140 **(✓)**
- C. 2100
- D. 2050

**Explanation:** By 2140 issuance ends; from then miners rely solely on transaction fees. (By ~2032 the reward drops below 1 BTC.)

**Q40. After issuance ends, what will miners rely on for compensation?**

- A. Block rewards
- B. Transaction fees only **(✓)**
- C. Government subsidies
- D. New coin creation

**Explanation:** Once no new bitcoins are minted, transaction fees become the miners' sole compensation.

**Q41. What concern does the Lightning Network raise for miners?**

- A. It increases block size
- B. It could significantly reduce transaction fees, affecting miner income **(✓)**
- C. It eliminates the need for nodes
- D. It speeds up mining

**Explanation:** By moving transactions off-chain cheaply, Lightning could lower fees and thus miners' future income.

**Q42. The base layer of Bitcoin, used to open/close Lightning channels, is often called the:**

- A. Consensus layer
- B. Settlement layer **(✓)**
- C. Transaction layer
- D. Security layer

**Explanation:** The base chain serves as the settlement layer on which Lightning channels open and close.

**Q43. How is Bitcoin block space best characterized?**

- A. Unlimited and cheap
- B. A scarce, valuable resource to be used wisely **(✓)**
- C. Controlled solely by miners
- D. Irrelevant to the network's future

**Explanation:** Block space is intrinsically limited; as Lightning grows, demand for it rises, making it increasingly valuable.

### Section 2.4 — Bitcoin Mining in the Bitcoin Protocol

**Q44. What did the Block Size Wars reveal about miners' power?**

- A. Miners hold ultimate control
- B. Miners do NOT hold ultimate power; nodes and users also wield power **(✓)**
- C. Only governments hold power
- D. Pools alone decide the rules

**Explanation:** The wars showed power is balanced among miners, nodes (verify/reject), and users (choose the chain).

**Q45. What is the role of nodes in the Bitcoin network?**

- A. They create and validate blocks
- B. They maintain integrity by verifying and validating transactions and blocks **(✓)**
- C. They only relay messages
- D. They set the price of Bitcoin

**Explanation:** Nodes verify and validate; a fraudulent block is rejected by nodes, censoring the offending miner.

**Q46. Which three groups share responsibility for the network's security?**

- A. Miners, nodes, and users **(✓)**
- B. Banks, governments, and exchanges
- C. Pools, manufacturers, and regulators
- D. Developers, investors, and traders

**Explanation:** Responsibility is shared among miners, nodes, and users; weakening any group raises centralization and attack risk.

**Q47. According to the course, why is the centralization of mining hardware production in China a risk?**

- A. It raises shipping costs
- B. It could enable export refusal or hashrate accumulation for a potential 51% attack **(✓)**
- C. It makes machines too cheap
- D. It improves efficiency too quickly

**Explanation:** Concentrated production means China could refuse exports or amass hashrate, threatening the network.

**Q48. Which initiatives aim to decentralize mining hardware production?**

- A. Intel producing chips in the US and Block's open-source MDK **(✓)**
- B. Banning all non-Chinese manufacturers
- C. Switching to GPUs
- D. Closing all mining farms

**Explanation:** Intel making US mining equipment and Block's open-source Mining Development Kit (MDK) help distribute production.

**Q49. Why is Proof of Work considered the "physical link" to the real world?**

- A. Because bitcoins are physical coins
- B. Because producing/validating blocks requires real, tangible energy **(✓)**
- C. Because miners must be physically present
- D. Because nodes run on paper

**Explanation:** PoW ties Bitcoin to physical reality — validation has a real energy cost, anchoring the network and resisting capture.

**Q50. What is a key limitation of Proof of Stake versus Proof of Work?**

- A. PoS is slower
- B. PoS gives disproportionate power to large existing holders, reflecting wealth inequality **(✓)**
- C. PoS requires more energy
- D. PoS cannot process transactions

**Explanation:** In PoS, those holding the most currency hold the most power, perpetuating concentration — unlike PoW where even small miners contribute.

**Q51. What is Bitcoin's fundamental mission, per the course?**

- A. To make transactions anonymous
- B. To replace all traditional currencies
- C. To be a censorship-resistant value exchange network **(✓)**
- D. To be the fastest payment system

**Explanation:** Bitcoin's core mission is censorship-resistant value exchange; the community strengthens distribution and anti-fragility.

**Q52. What does Satoshi's game theory achieve among network actors?**

- A. It forces everyone to cooperate by law
- B. It incentivizes each actor to act correctly, protecting their own and others' interests **(✓)**
- C. It rewards dishonest behavior
- D. It removes the need for miners

**Explanation:** The incentive design rewards honesty and reprimands bad behavior, reinforcing system security and stability.

**Q53. In the recap, how do miners "fortify" the Bitcoin network?**

- A. By holding bitcoins long-term
- B. By using electricity to compute Proof of Work, earning new BTC and fees **(✓)**
- C. By running the most nodes
- D. By setting transaction fees

**Explanation:** Miners spend electricity on PoW to secure the network against censorship, rewarded with new bitcoins and fees.

### Section 2.5 — Bitcoin Price and Hashrate

**Q54. Why can machines ordered in a bull market arrive during a bear market?**

- A. Shipping is always delayed a year
- B. Manufacturing/delivery lags create a mismatch between demand and availability **(✓)**
- C. Manufacturers hoard machines
- D. Miners cancel orders

**Explanation:** Production isn't instant, so a surge of bull-market orders may be delivered later when prices have fallen — high hashrate, low price.

**Q55. The course argues Bitcoin's health is better judged by what, rather than price alone?**

- A. Number of exchanges
- B. Its cost/hashrate (electricity required to run the network) **(✓)**
- C. Media coverage
- D. Number of wallets

**Explanation:** Focusing on cost (tied to hashrate and electricity) gives a more consistent view of stability than price alone.

**Q56. What does mining help establish for Bitcoin's price?**

- A. A ceiling price
- B. A fixed price
- C. A floor price below which miners would sell at a loss **(✓)**
- D. A guaranteed daily return

**Explanation:** Mining cost establishes a rough floor; below it, miners would be selling at a loss.

**Q57. What is the relationship between Bitcoin's production cost and its market price?**

- A. Inversely proportional
- B. Generally proportional **(✓)**
- C. Always equal
- D. Completely unrelated

**Explanation:** Cost is generally proportional to price, helping explain fluctuations and outlook.

**Q58. A downside of "mining for profit" highlighted in the course is:**

- A. It always loses money
- B. It can centralize hashpower and carry environmental impact **(✓)**
- C. It reduces the block reward
- D. It slows transactions

**Explanation:** If only big firms can afford top equipment, profit-seeking can centralize hashpower and raise environmental concerns.

**Q59. How does Attakai answer the "profit vs. network" debate?**

- A. By maximizing profit at all costs
- B. By making home mining accessible, decentralizing while turning waste heat into value **(✓)**
- C. By discouraging individual mining
- D. By centralizing in big farms

**Explanation:** Attakai isn't only about profit; it strengthens distribution and security while making mining accessible and reusing heat.

### Section 2.6 — Sovereignty and Regulation

**Q60. When is it generally wiser to buy Bitcoin directly rather than mine it?**

- A. Always
- B. When the cost to mine a BTC exceeds the cost to buy it **(✓)**
- C. When electricity is free
- D. Never

**Explanation:** If mining costs more than buying, direct purchase avoids the challenges and costs of mining — unless mining adds unique value.

**Q61. Which adage captures the risk of not controlling your own mining hardware?**

- A. "Not your keys, not your coins"
- B. "Not your hashrate, not your reward" **(✓)**
- C. "Trust the cloud"
- D. "Mine fast, sell faster"

**Explanation:** Echoing "not your keys, not your coins," the mining version warns that without control of your hashrate you can't rely on the reward.

**Q62. What are "virgin bitcoins"?**

- A. Coins held by founders
- B. Freshly mined coins with no transaction history, never spent **(✓)**
- C. Coins on the Lightning Network
- D. Stolen coins

**Explanation:** Virgin bitcoins are newly mined, history-free coins, often acquired without KYC, valued as "clean."

**Q63. Why are virgin bitcoins sought after by large institutions?**

- A. To avoid taxes
- B. To guarantee the legitimacy of their assets to regulators **(✓)**
- C. To use for illegal activity
- D. To sell at double price

**Explanation:** With no tainted history, virgin coins help institutions prove legitimacy to regulators and exchanges.

**Q64. What is the field of "cloud mining" especially known for, per the course?**

- A. Guaranteed profits
- B. A high number of scams due to investors' lack of understanding **(✓)**
- C. Government backing
- D. Free electricity

**Explanation:** Cloud mining is characterized by many scams, exploiting investors who don't understand mining.

**Q65. What does the course say is the best weapon against restrictive mining regulation?**

- A. Lobbying with money
- B. Truthful information and education **(✓)**
- C. Moving all mining underground
- D. Ignoring regulators

**Explanation:** Against misleading campaigns, accurate education of the public and decision-makers is the strongest defense.

**Q66. Is mining currently banned in Europe, according to the course?**

- A. Yes, fully banned
- B. No, but a ban is conceivable given the China precedent **(✓)**
- C. Yes, but only in France
- D. It is mandatory

**Explanation:** Mining isn't banned in Europe, but a ban is a conceivable scenario; wider hashrate distribution and education help guard against it.

### Section 3.1 — Attakai: Making Home Mining Possible

**Q67. What does "Attakai" mean, and where does the word come from?**

- A. "Cold mining" in Korean
- B. "The ideal temperature" in Japanese **(✓)**
- C. "Free energy" in Finnish
- D. "Hot coin" in Chinese

**Explanation:** Attakai means "the ideal temperature" in Japanese — fitting for a heat-reuse initiative.

**Q68. What did Satoshi Nakamoto (2010) suggest about where mining could become cost-free?**

- A. In tropical climates with air conditioning
- B. In cold climates where heating is electric, making mining heat free **(✓)**
- C. Only in data centers
- D. Where electricity is most expensive

**Explanation:** Satoshi noted mining should occur where it is cheapest — e.g., a cold place using electric heat, where the mining heat is essentially free.

**Q69. Why does the "radiator/server" concept struggle, unlike a Bitcoin miner?**

- A. Servers produce no heat
- B. Computing demand isn't tied to heating demand, and bandwidth is limited **(✓)**
- C. Servers are silent
- D. Servers can be turned off anytime

**Explanation:** A company's server needs don't match households' heating needs, and bandwidth limits prevent profitability — whereas a miner can be toggled freely.

**Q70. Why can a Bitcoin miner be switched on or off at any time without harming the network?**

- A. Because it stores blocks locally
- B. Because difficulty adjusts to total hashrate; any one miner is optional **(✓)**
- C. Because nodes replace it instantly
- D. Because it never actually mines

**Explanation:** The network self-adjusts difficulty to total hashrate, so a single miner can start or stop without affecting the network, unlike a server providing a live service.

**Q71. What causes an electronic board to generate heat (the "Joule effect")?**

- A. The act of calculating itself
- B. Electrical resistance of components causing losses as current flows **(✓)**
- C. Cooling fans
- D. Software bugs

**Explanation:** Boards don't "spend" energy to compute; current flowing through resistive components produces losses dissipated as heat — the Joule effect.

**Q72. How does distributing miners across many homes benefit Bitcoin?**

- A. It raises the price directly
- B. It decentralizes hashrate, making state seizure and censorship harder **(✓)**
- C. It lowers the block reward
- D. It speeds up confirmations

**Explanation:** Spreading hashrate across thousands or millions of households makes it very hard for any state to seize control.

**Q73. Out of the factory, why is a miner unsuitable as a home heater?**

- A. It produces no heat
- B. Excessive noise and lack of adjustment **(✓)**
- C. It uses no electricity
- D. It cannot connect to the internet

**Explanation:** Stock miners are too loud and not adjustable; hardware and software mods fix both, making them quiet and controllable like modern heaters.

### Section 3.2 — Buying Guide for a Used ASIC

**Q74. What are the S9's approximate stock specs?**

- A. ~1400 W and ~13.5 TH/s **(✓)**
- B. ~3000 W and ~100 TH/s
- C. ~500 W and ~5 TH/s
- D. ~220 W and ~1 TH/s

**Explanation:** The Antminer S9 (Bitmain, May 2016) consumes about 1400 W and produces about 13.5 TH/s.

**Q75. Which component is described as the "brain" of the ASIC?**

- A. A hashboard
- B. The control board (SD slot, Ethernet, connectors) **(✓)**
- C. The power supply
- D. The C13 cable

**Explanation:** The control board — with its SD card slot, Ethernet port, and connectors for hashboards and fans — is the brain of the machine.

**Q76. How many hashboards does a standard Antminer S9 contain?**

- A. 1
- B. 2
- C. 3 **(✓)**
- D. 6

**Explanation:** The S9 has 3 hashboards containing the hashing chips, connected by 3 data cables to the control board.

**Q77. What are the default S9 login credentials to check when buying?**

- A. admin / admin
- B. root / root **(✓)**
- C. user / 1234
- D. root / (none)

**Explanation:** On the stock Bitmain interface the defaults are username "root" and password "root"; if they fail, reset the machine.

**Q78. What single phrase summarizes the used-ASIC buying guide?**

- A. "Buy low, sell high"
- B. "Don't trust, verify" **(✓)**
- C. "Hashrate is king"
- D. "Cheaper is better"

**Explanation:** The guide's one-sentence summary is "Don't trust, verify" — confirm parts, function, connectivity, and credentials in person.

**Q79. What discount does the affiliate code "decouvre" give with partner 21energy?**

- A. 5%
- B. 10% **(✓)**
- C. 21%
- D. 50%

**Explanation:** The code "decouvre" gives a 10% discount on a tested, BraiinsOS+-preinstalled S9 from 21energy, supporting Attakai.

**Q80. How can you find an S9's local IP address?**

- A. It is printed on the case
- B. By checking connected devices in your internet router's interface (format 192.168.x.x) **(✓)**
- C. By calling Bitmain
- D. It is always 10.0.0.1

**Explanation:** Connect to the router's interface and look for connected devices; the miner's address looks like 192.168.x.x.

### Section 3.3 / 5 — Hardware Modifications and Fans

**Q81. Which fan is recommended to replace the S9's main fans?**

- A. Noctua NF-A6x25 PWM
- B. Noctua NF-A14 iPPC-2000 PWM (12V) **(✓)**
- C. Stock Bitmain 120mm fan
- D. Corsair LL140

**Explanation:** The team selected the 140mm Noctua NF-A14 iPPC-2000 PWM (12V) as the best compromise for the main fans.

**Q82. What adapter is needed to fit the 140mm main fans onto the S9?**

- A. A 120mm to 92mm adapter
- B. A 140mm to 120mm adapter **(✓)**
- C. A USB adapter
- D. No adapter is needed

**Explanation:** A 140mm→120mm adapter (a 3D-printed part) lets the larger 140mm fans mount on the S9.

**Q83. Which fan is recommended for the power supply?**

- A. Noctua NF-A14 iPPC-2000 PWM
- B. Noctua NF-A6x25 PWM **(✓)**
- C. Noctua NF-A12
- D. Stock PSU fan

**Explanation:** The smaller Noctua NF-A6x25 PWM (12V) replaces the noisy power-supply fan; connector adapters are needed.

**Q84. Which device is used to connect the S9 over Wi-Fi instead of Ethernet?**

- A. ANTELA smart plug
- B. Vonets VAP11G-300 Wi-Fi/Ethernet bridge **(✓)**
- C. A USB Wi-Fi dongle
- D. A powerline adapter

**Explanation:** The Vonets VAP11G-300 bridges the router's Wi-Fi to the miner via Ethernet without creating a subnet.

**Q85. On which Wi-Fi frequency does the Vonets bridge operate?**

- A. 5 GHz only
- B. 2.4 GHz only **(✓)**
- C. Both 2.4 and 5 GHz
- D. 6 GHz

**Explanation:** The Vonets bridge works only on the 2.4 GHz band, so you must select the router's 2.4 GHz network.

**Q86. Before installing quieter fans, what must already be done, and why?**

- A. Overclock the miner for more heat
- B. Install BraiinsOS+ (or power-reducing firmware), because quieter fans dissipate less heat **(✓)**
- C. Remove the hashboards
- D. Disconnect the power supply permanently

**Explanation:** Quieter fans cool less, so the machine must first be set to lower power via BraiinsOS+ to avoid overheating.

**Q87. When wiring a new Noctua fan via electrician's "sugar," what do you do with the yellow wire?**

- A. Connect it to the red wire
- B. Cut it flush — it is the unused speed-control wire **(✓)**
- C. Connect it to the black wire
- D. Connect it to the Ethernet port

**Explanation:** The yellow wire controls speed and isn't used here, so it's cut flush; only black-to-black and red-to-red are joined.

**Q88. Which way must a fan's airflow arrow point when installing the PSU fan?**

- A. Toward the outside of the case
- B. Toward the inside of the case **(✓)**
- C. Upward
- D. It doesn't matter

**Explanation:** The arrow indicates airflow direction; for the PSU fan it must point toward the inside of the case.

**Q89. When mounting the 3D adapters for the main fans, what risk does over-tightening pose?**

- A. Stripping the Ethernet port
- B. Deforming the part so a screw contacts a capacitor **(✓)**
- C. Cracking the hashboard
- D. Breaking the SD card

**Explanation:** Over-tightening can deform the 3D part and push a screw into contact with a capacitor — tighten only until flush.

### Section 4 — Software Setup

**Q90. What is BraiinsOS+ and who developed it?**

- A. A wallet app by Bitmain
- B. Third-party mining firmware from the first Bitcoin mining pool, replacing stock OS **(✓)**
- C. A node implementation by Block
- D. An exchange platform

**Explanation:** BraiinsOS+ is third-party firmware developed by the first Bitcoin mining pool; it replaces stock firmware and adds features like power adjustment.

**Q91. Which tool makes it easy to find a miner's IP and install BraiinsOS+?**

- A. BOS Toolbox **(✓)**
- B. SmartLife app
- C. Vonets Wizard
- D. Telegram bot

**Explanation:** The BOS Toolbox scans the network for the miner's IP and installs BraiinsOS+ directly to the device's memory.

**Q92. In BOS Toolbox, what IP range would you typically scan on a home network?**

- A. 10.0.0.0/8
- B. 192.168.1.0/24 **(✓)**
- C. 255.255.255.0
- D. 127.0.0.1/32

**Explanation:** Home networks usually use 192.168.1.1–192.168.1.255, entered as 192.168.1.0/24 in the scan field.

**Q93. After installing BraiinsOS+, what are the default login credentials?**

- A. root / root
- B. admin / admin
- C. root / (no password) **(✓)**
- D. user / braiins

**Explanation:** On BraiinsOS+, the default username is "root" with no password.

**Q94. How do you reset an Antminer S9 to factory settings?**

- A. Hold the power button for 30 seconds
- B. 2–10 minutes after startup, press Reset for 5 seconds and release **(✓)**
- C. Remove the SD card
- D. Unplug all hashboards

**Explanation:** Between 2 and 10 minutes after startup, press Reset for 5 seconds; it restores within ~4 minutes and restarts automatically.

**Q95. Which of these does the BraiinsOS+ Dashboard display?**

- A. Only the price of Bitcoin
- B. Real-time temperature, hashrate, status, efficiency (W/TH), power, and fan speeds **(✓)**
- C. The miner's purchase price
- D. The user's wallet balance

**Explanation:** The Dashboard shows real-time temperature/hashrate/status graphs plus efficiency in W/TH, power consumption, fan speeds, and per-hashboard data.

### Section 6 — Pools and Optimization

**Q96. A mining pool is compared to what kind of cooperative?**

- A. A farming cooperative pooling production to stabilize income **(✓)**
- B. A credit union
- C. A car-sharing club
- D. A housing co-op

**Explanation:** Like farmers pooling output to reduce variance and stabilize income, miners pool hashes for steadier rewards.

**Q97. Roughly how long would a single S9 take on average to mine a block solo?**

- A. About 1 year
- B. About 471 years **(✓)**
- C. About 10 minutes
- D. About 50 years

**Explanation:** At constant difficulty, a lone S9 would average ~471 years per block (~1 in 24,777,849 per block) — hence pools.

**Q98. Which reward model does the course prefer for an on/off heater, and why?**

- A. Score, because it rewards uptime
- B. PPS/FPPS, because each valid share is rewarded equally regardless of uptime **(✓)**
- C. Solo mining, for the full block reward
- D. Proof of Stake rewards

**Explanation:** Score rewards long uptime (bad for intermittent heating); PPS/FPPS pay per share, ideal for a miner toggled on briefly.

**Q99. Which two pools are recommended, and what models do they use?**

- A. Braiins Pool (Score) and Foundry (PPS)
- B. Linecoin Pool (FPPS) and Nicehash (PPS) **(✓)**
- C. Slush (Score) and AntPool (FPPS)
- D. Linecoin (PPS) and Braiins (FPPS)

**Explanation:** The course recommends Linecoin Pool (FPPS, BTC-only, rich features, 100k sat minimum) and Nicehash (PPS, Lightning withdrawals, 2k sat minimum).

**Q100. What does autotuning do, and what improvement can BraiinsOS+ achieve?**

- A. Sets one frequency for the whole machine; ~13% gain
- B. Optimizes frequency chip-by-chip for higher hash/watt; up to ~20% improvement **(✓)**
- C. Disables underperforming chips; ~50% gain
- D. Increases voltage uniformly; no measurable gain

**Explanation:** Autotuning tunes each chip's frequency individually (chips vary), raising hash-per-watt; BraiinsOS+ autotuning can improve performance up to ~20% (beyond AsicBoost's ~13%).