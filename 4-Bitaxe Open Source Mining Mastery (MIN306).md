# Bitaxe Open Source Mining Mastery (MIN306) — Study Guide & Quiz

**Course:** Bitaxe Open Source Mining Mastery · **Professor:** wantclue · **Level:** Advanced · **Duration:** 8 hours · **Course ID:** MIN306

**Goal:** Master the complete Bitaxe ecosystem — from hardware assembly to advanced customization and performance optimization.

This document has two parts:

1. **Concept Overview** — the main ideas of every chapter, condensed for revision and mastery.
2. **100-Question Quiz** — multiple-choice questions, each with the correct answer marked **(✓)** and an explanation.

---

# Part 1 — Concept Overview by Chapter

## Section 1 — Introduction

### 1.1 Course Overview

MIN306 is a journey into building, understanding, and optimizing **open-source Bitaxe mining hardware**. Bitaxe is a paradigm shift that breaks the monopoly of proprietary ASIC makers by providing fully open-source designs, firmware, and software. The six core areas are: **Understanding Bitaxe** (origins, values, what it is), **Software and Operations** (AxeOS), **Community and Collaboration** (open-source contribution, Public Pool, Umbrel), **Hardware Assembly and Troubleshooting** (tools, soldering, debugging), **Advanced Customization** (PCB modification, factory files, web flasher, ordering PCBs), and **Performance Optimization** (benchmarking, overclocking). No prior mining experience is required, but basic electronics and GitHub familiarity help. Course objectives: understand the philosophy of open-source mining, build Bitaxe devices, configure/optimize AxeOS and Public Pool, and implement overclocking and benchmarking.

## Section 2 — Understanding Bitaxe

### 2.1 The History

- **Origin:** Founder **Skot** discovered Bitcoin (~$20/coin) at a college party via someone buying on the Silk Road. At university he experimented with **open-source FPGA bitstreams** for mining (goal: mine enough for an office pizza).
- **Solar vision:** While building **solar-powered gateways in Africa**, he realized mining ASICs are low-voltage DC devices that pair perfectly with solar panels — but ASIC mining had become **proprietary/closed-source**, a gap that frustrated him.
- **Reverse engineering:** With **no Bitmain documentation**, Skot examined chips under microscopes, measured pin pitches with calipers, and scanned footprints. The first two "day miner" prototypes failed from wrong footprints.
- **Breakthrough:** The **third iteration (May 2022)** worked — a **two-chip design using BM1387 chips harvested from Antminer S9 units**. The name "Bitaxe" evokes a pickaxe for Bitcoin. ASICs run at very low voltages (~0.6 V) at high current; firmware had to run directly on an **ESP32** (no external CGMiner computer).
- **Community:** Early forum/social posts met skepticism. **SirVapesAlot** founded the **Open Source Miners United (OSMU)** Discord. **johnny9** solved firmware; **Ben** built the **AxeOS dashboard**, manufacturing, and **Public Pool**. OSMU mentors newcomers into contributors.
- **Vision:** Produce **one million 1-TH miners = one exahash** of distributed power, decentralizing mining against government/regulatory capture. Home mining has near-zero infrastructure cost (plug into existing outlets). Goal is also **educational**, bringing people into Bitcoin's mining process.

### 2.2 What is the Bitaxe?

- **Bitaxe Max** (first gen): **BM1397** chip (from Bitmain S17 series); **~300–400 GH/s**; educational/experimental.
- **Bitaxe Ultra:** **BM1366** chip (from S19 series); improved efficiency; required power/thermal/control changes.
- **Microcontroller:** Every Bitaxe uses an **ESP microcontroller** running OSMU software, communicating with the ASIC via serial traces etched on the PCB. It handles power management, temperature monitoring, and a display showing temperature, hash rate, IP, etc.
- **Power & safety:** Strict **5 V** requirement; consumes **~5–25 W** depending on frequency/voltage. Wrong voltage can permanently damage the device. Frequency/voltage/power/hashrate are interrelated.
- **Solo mining focus:** Bitaxe targets **solo mining** — statistically unlikely to find a block, but educational and good for decentralization.
- **Evolution:** Updates focus on **manufacturability** (e.g., micro-USB → **USB-C**), not forced obsolescence. Philosophy: **"if it hashes, it hashes."**

### 2.3 Where Can I Learn More?

- **Bitaxe.org:** Central hub with curated, verified links to all ecosystem resources.
- **GitHub repos:** Hardware design files (incl. **building.md** manufacturing instructions) and **ESP-Miner** (all firmware code/docs, pre-compiled binaries or build-from-source, Raspberry Pi integration).
- **Bitaxe Web Flasher:** Browser-based firmware flashing for Ultra (various port versions) and Max; supports updates or USB factory resets.
- **Community:** **Discord** (real-time, channels for solar, pools, specific devices like Ultra/Hex/Supra, firmware, releases, help; verification on join; paid subscriber tier) and the **OSMU wiki (osmu.wiki)** — structured, searchable, community-editable via GitHub, with PDF setup guides.
- **Bitaxe legit list:** Curated, **non-affiliate** list of trustworthy vendors, noting who contributes back to OSMU; protects against scams like unauthorized pre-orders.

## Section 3 — Software and Operations

### 3.1 What is AxeOS?

- **AxeOS** is the firmware + browser-based web interface for Bitaxe; access it via the device's **IP address**.
- **Four core metrics:** **Hash rate**, **shares** (valid solutions submitted), **efficiency** (hashrate ÷ power), and **best difficulty** (highest-difficulty share ever found — survives reboots/updates, resets only on factory flash).
- **Monitoring:** Live hash rate graph (more accurate over time), power section (consumption, input voltage with warnings, requested ASIC voltage), temperature (with offsets), frequency/voltage (measured at the ASIC), and connection status (stratum URL/port/user, quick links to public pool web UI).
- **Swarm:** Manage **multiple devices** from one dashboard by adding IPs; do pool changes, restarts, frequency adjustments, and monitoring across devices at once.
- **Settings:** Wi-Fi (single-word names recommended), stratum URL (no protocol/port), stratum user (BTC address for solo, or username for pools, with worker IDs), optional stratum password. **Hardware tuning defaults: 485 MHz / 1200 mV.**
- **Maintenance:** In-interface firmware updates (accepts **esp-miner.bin** and **www.bin**), live logs (ASIC model, uptime, Wi-Fi, memory, nonce/difficulty/submission detail), screen orientation, fan polarity inversion, automatic or manual fan control. **All changes require save + restart.**

## Section 4 — Community and Collaboration

### 4.1 Open-Source Contribution Overview

- **GitHub** is a cloud platform hosting projects using **Git** (distributed version control) for collaboration: tracking changes, merging, versioning, and contributing to projects like OSMU's **BitX**.
- **Interface:** Top bar = Code, Issues, Pull Requests, Discussions, Actions, Projects, Security, Insights. **Watch** (notifications), **Fork** (personal copy), **Star** (endorsement). The **About** section shows description and license — BitX is "open source ASIC Bitcoin miner hardware" under **GPL 3.0**.
- **Branches:** Copies/variants of the codebase. **master** = default stable; other branches hold variants (e.g., Ultra v2, Super 401 using the **S21 ASIC**); may be "X commits ahead/behind."
- **Issues:** For **real technical problems/bugs** (with reproduction steps), **not** general questions — those go to **Discussions** (or Discord). Some issues lead to hardware improvements (e.g., added mounting holes).
- **Pull requests (PRs):** Mechanism for outside contributors to propose changes (fork → change → PR → review → merge). **Tags** mark version milestones; **releases** are formal distributions with notes.

### 4.2 Open-Source Contribution Hands-on

- **Fork:** Your personal copy ("forked from …"); operates independently but tracks the upstream ("X commits behind/ahead"); use **Sync fork** to pull upstream changes.
- **Dev environment:** **Visual Studio Code** as IDE; install/authenticate the **Git extension** (GitHub icon in sidebar → clone, branch, sync without command line). For ESP32 projects, install the **ESP-IDF extension** (**version 5.1.3** recommended in this chapter).
- **Making changes:** Clone (ZIP or VS Code) for a local copy. Firmware projects use **C** (core), **TypeScript** (UI), **Java** (utilities). **Cardinal rules: never publish untested code; never commit secrets** (passwords, API tokens).
- **Pull requests:** Sync first to avoid conflicts; write a clear description (problem, solution, impact); request expert reviewers; expect iteration. **Rejection isn't failure** — it's part of the iterative process.

### 4.3 What's Public-Pool?

- **Public Pool** is a fully **open-source solo Bitcoin mining pool**: you keep **100% of the block reward** (currently **3.125 BTC + fees**) when _you personally_ find a block — but you still bear solo variance.
- **Zero fees** vs. traditional pools' 1–3%. Solo mining = full reward but extreme variance (months/years); pooled mining = steady, shared income. Public Pool gives solo economics with shared infrastructure and transparency.
- **Open source:** Full codebase + separate UI repo on GitHub; runnable in **Docker**; connect with **Stratum details + your BTC address** as username (optional worker name after a dot).
- **Community/sustainability:** Shows total connected hashrate (**~1–2 PH/s in 2024, ~40 PH/s Nov 2025**); stars mark fully open-source hardware. Funded by an **affiliate program** — code **"SOLO"** gives equipment discounts; **50%** of affiliate earnings fund operations, **50%** rewards top monthly difficulty shares.
- **Decentralization:** Public Pool is a **stepping stone** toward running **your own pool** (the highest decentralization), and a learning platform for it.

### 4.4 How to Install Public-Pool on Umbrel

- **Hardware:** A **mini PC** (recommended **Intel N100**, **≥1 TB NVMe**, sufficient RAM) — NVMe is critical for syncing/storing the full **Bitcoin node**.
- **Software:** Linux base + **Umbrel** node-management platform (web UI, app store) handles Bitcoin Core install/sync/maintenance, abstracting complexity.
- **Install:** Umbrel **app store → search "public pool" → install** (a few clicks). It auto-configures the connection to the Bitcoin node (validates txs, builds block templates, distributes work). UI is reachable on the local network.
- **Connect miners:** Point the miner's pool settings to your **local IP + assigned port**. Consider local DNS quirks; **port forwarding** enables external access but adds security risk.

## Section 5 — Hardware Assembly and Troubleshooting

### 5.1 What Tools to Use?

- **Hand tools:** Quality **tweezers** (straight-tip for most parts, bent-tip for tiny ones; e.g., iFixit kits), **scissors**, and **electrical tape** (insulation).
- **Solder paste:** Apply via small **non-sharp syringes** for control. Use quality paste — **ChipQuik TS391SNL50** is recommended; cheap pastes with low melting points cause joints to re-flow and components to shift.
- **Cleanup/repair:** **Desoldering rig** (heated vacuum) + **flux** (solid/liquid) to clear bridges and restore flow; a small **spoon tool** for flux; **isopropanol + brush** (old toothbrush) for cleaning flux residue.
- **Specialized:** **Stencils** (consistent paste on fine-pitch ICs/ASICs), **thermal paste/grease** (heat transfer), and a **hot air rework station** — budget units (~$30–50) work at **~355 °C** with auto temp reduction in the holder, but higher-end gear is more reliable.

### 5.2 Fix Solder Issues

- **Orientation:** MOSFETs **Q1/Q2** have a **dot marker** and four pins (one large pad, three small unconnected to it). Always verify orientation against the board's pads before soldering — wrong orientation causes hard-to-diagnose faults.
- **Solder bridges:** Common near fine-pitch parts like **U10**; remove with **desoldering wick** (copper braid) + heat, holding the board in a PCB holder/clamp. Prevent with correct paste amounts.
- **Critical component U9 (buck converter):** Converts **5 V → 1.2 V** for the ASIC; has five small connections and tends to fail. Too little paste = no conversion; too much = bridges. A bridged U9 emits **high-frequency noise**. Reflow/add paste (flows via **capillary action**); if no 1.2 V output, add paste and reinstall.
- **Heat management:** Crystal oscillator **Y1** and **U1** are heat-sensitive — solder at **350 °C**, minimize time. For the ASIC, use stencils for even paste; press only on **labeled edges**, never the central die. **U8** has many pins (some internally connected — bridges there are harmless); straighten bent leads patiently.

### 5.3 How to Debug Your Bitaxe Using AxeOS

- **Power consumption** is the first indicator: normal **Ultra/Supra ≈ 10–17 W**. **Below ~3 W** signals a fundamental ASIC/circuitry fault.
- **ASIC voltage readings:** Understand **measured vs requested** voltage. **1.2 V measured + <3 W** = ASIC soldering problem or dead ASIC (inspect die for cracks). **Low power + very low requested voltage (e.g., 100 mV / 0.5 V)** = inadequate supply, usually a **U9 buck converter** problem.
- **Logs:** "**ASIC results**" entries confirm the chip is powered, working, and communicating; their absence narrows the fault to components/connections.
- **Systematic order:** Document power + voltage, correlate with logs. For U9 issues, inspect/resolder; verify **1.2 V at ASIC pins with a multimeter**; if voltage is present but ASIC dead with no visible damage → **replace the ASIC**; if still failing → check **U2** (which drives the ASIC) last.

### 5.4 How to Debug Using USB?

- Provides **direct serial access** to internal logs via the **ESP-IDF** framework — captures data lost on reboots, unlike web interfaces. Needs **VS Code + ESP-IDF**; works on variants with a USB port (e.g., **Ultra 204**).
- **Setup:** Connect USB, run **`idf.py monitor`**; it scans COM ports (COM3, COM4, COM16…) to establish UART with the ESP32; manual port selection if auto fails.
- **Normal boot:** ESP-IDF version → "**Welcome to the Bitaxe. Hack the planet**" → ASIC frequency, model, board version → I2C init, **ASIC voltage 1.2 V**, GPIO, Wi-Fi, DHCP/IP → "**detected one ASIC chip**." Operational tasks: stratum API, main task, ASIC task; pool connect, difficulty, job queue, nonces, submits.
- **Failures:** I2C errors like **DS4432U** "**ESP_ERROR_CHECK failed**" with timeouts (points to **U10** voltage/display) — logs name the source file (e.g., **main_ds4432u.c**), function, and core. **EMC2101** (temp/fan) has its own signatures. Repeated error→reboot cycles and **audible noise** indicate soldering bridges/bad joints. Missing ASIC results = ESP32↔ASIC communication failure (power, traces, components). Document patterns before seeking community help.

## Section 6 — Advanced Customization

### 6.1 Modify the PCB

- **KiCad** is the open-source PCB design/routing tool; place components and route traces. Fully open-source, ideal for learning from the complete Bitaxe design.
- **Setup:** Download the Bitaxe repo (GitHub ZIP) + install KiCad from the official site; open the **Bitaxe Ultra KiCad project file**. Use the **3D viewer** to understand layout.
- **Logo customization** (most accessible mod): use the **image converter** to turn an image into a footprint (size in **mm**); pick **high-contrast** images for the silkscreen; choose **front/back silkscreen** layer; manage **footprint libraries** and link them to the project.
- **Advanced exploration:** Layer management, **trace routing analysis** (e.g., power distribution), schematic-vs-layout relationships (thermal/signal-integrity placement), and **design rule checking** for electrical/manufacturing compatibility.

### 6.2 How to Create a Factory File?

- Factory files **embed configuration into the firmware binary**, removing manual setup — ideal for multi-device deployments. (Technical chapter; skimmable.)
- **Environment:** VS Code (ideally Linux) + **ESP-IDF**. Note: **5.1.3 caused build issues**; **use ESP-IDF 5.3 Beta 1** (Express install).
- **Config file:** Wi-Fi SSID/password (real, not "test"), private pool IP or public pool like **public-pool.io** + port, stratum user (**BTC address**), frequency/voltage/ASIC type. Examples: **BM1368** for Super, **BM1366** for Ultra; board port version e.g. **401** for newer revisions.
- **Build web UI first:** In the **AxeOS** subdir of the HTTP server, run **`npm install`** then **`npm run build`** (requires Node.js) — these assets embed into the ESP32 firmware before the main build.
- **Factory file creation:** Generate a config binary from **config.csv** with the **NVS partition generator** (`nvs-partition-gen.py`) → **config.binary** at address **0x6000**; combine with firmware via **merge scripts** (e.g., **merge-bin-with-config.sh** for config-inclusive factory files). Produces ready-to-flash, device-specific binaries.

### 6.3 How to Use the Bitaxe Web Flasher?

- **URL:** https://bitaxeorg.github.io/bitaxe-web-flasher/ . **Chrome** (or Chromium) required — **Brave and Firefox lack Web Serial API** support, so they fail.
- **Power:** **Version ≤204** runs on **USB power alone**; **version ≥205** needs **external power** plus USB or installation fails.
- **Bootloader mode:** **Press and hold the boot button before** connecting USB-C; connecting first results in normal operation, not flashing.
- **Four install options;** key distinction is **Factory vs Update.** **Factory** = complete erase + fresh install + self-test (wipes Wi-Fi, BTC address, settings — reconfigure from scratch); good for persistent issues. **Update** = preserves config, updates only firmware. During Update, **decline the "erase device?" prompt by clicking "Next"** — accepting erases the config file and can render the device non-functional (recoverable, but troublesome).

### 6.4 How to Create and Order the PCB?

- From KiCad design to physical board. The PCB editor shows components/connections (colored traces); the **3D viewer** previews the assembled board.
- **Gerber files** are the manufacturing standard (copper layers, solder mask, drill holes). In KiCad: PCB editor → **fabrication outputs** (Files menu) → typically "manufacturing files/gerbers"; **compress into a ZIP** for upload. Many repos (incl. Bitaxe) ship pre-generated files, but knowing how to regenerate matters for modifications.
- **Manufacturers:** **JLCPCB** and **PCBWay** are popular; keep default settings unless you have specific needs. Parameters: thickness, copper weight, surface finish, **minimum ~5 boards**. **Color** is purely aesthetic (green cheapest; blue/red/yellow/purple/black available).
- **Add-ons:** **Stencils** (precision-cut aluminum templates) greatly improve fine-pitch/ASIC paste application — combined top/bottom stencil is usually best. Full assembly services exist but many mining-specific components aren't readily available, so **manual assembly** is often more practical (and educational).

## Section 7 — Performance Optimization

### 7.1 Benchmark Your Bitaxe

- **Key metrics:** hashrate (**TH/s**), efficiency (**J/TH**), ASIC frequency (**MHz**), core voltage (**V**). A well-configured Bitaxe ≈ **1.1 TH/s, ~17 J/TH, 550 MHz, 1.14 V** measured. Higher frequency → more hashrate but more heat/power; balance is the goal.
- **Tool:** **Bitaxe Hashrate Benchmark**, a Python tool by **WhiteCookie**, enhanced by **mrv777**, under **GPLv3**. It systematically tests frequency/voltage combos while monitoring performance and temperature, prioritizing **safe operation** over max performance.
- **Process:** Takes **~30–40 minutes**, starting conservatively (**~1.15 V, 500 MHz**) and incrementing.
- **Install:** Needs **Python + Git** (optionally VS Code); clone repo, create a **virtual environment**, install dependencies from the requirements file.
- **Run & results:** Execute one Python command with the **Bitaxe's IP**; it logs each iteration (voltage, frequency, hashrate, input voltage, temps incl. buck converter). It backs off near the **66 °C** safety threshold. Output is **JSON ranking the top five configs** for max hashrate and for best efficiency. Command-line args allow custom starting voltage/frequency.

### 7.2 Overclock Your Bitaxe

- Overclocking raises frequency/voltage beyond factory specs → more heat and component stress, shortening lifespan; **adequate cooling is mandatory** (e.g., a **Bitaxe Gamma with a quality heatsink and fan**). Don't overclock devices with small heatsinks/weak fans.
- **Strategic heatsinks:** The **buck converter (TPS)** — small black part near the large coil on the back, converting **5 V → ~1.2 V** — is the main thermal bottleneck; add a small **adhesive heatsink** for headroom and efficiency. Additional heatsinks help high-current voltage-regulation areas on the front.
- **Cooling limits:** The **ESP32** needs no extra cooling — heatsinks there can interfere with the **Wi-Fi antenna**. The Bitaxe has **two fan headers but only one fan controller**, so two fans give conflicting RPM signals and unpredictable control.
- **Baseline:** Run stock for several hours; keep **ASIC < 60 °C** and **voltage regulator < 60 °C**. If stock already exceeds **65 °C ASIC / 70–80 °C regulator**, add cooling first. Increase frequency in steps, ~**30–60 min per step**.
- **Advanced (custom) settings:** Append **`?OC`** to the web UI URL to unlock manual frequency/voltage fields. Use **10–15 MHz increments**; some reach **~700 MHz at ~1.175 V** with heavy cooling. The voltage regulator tolerates up to **100 °C** without immediate damage, but heat reduces efficiency/longevity.

## Section 8 — Final Section

**8.1 Evaluate this course** and **8.2 Conclusion.** The course ends encouraging learners to build, optimize, and contribute to Bitaxe — putting the future of decentralized Bitcoin mining in their hands.

---

# Part 2 — 100-Question Quiz

Each question lists four options; the correct answer is marked **(✓)** and followed by an **Explanation**.

### Section 1 — Introduction

**Q1. What fundamental shift does the Bitaxe project represent in Bitcoin mining?**

- A. Moving mining to the cloud
- B. Breaking the monopoly of proprietary ASIC makers with fully open-source designs, firmware, and software **(✓)**
- C. Replacing ASICs with GPUs
- D. Eliminating the need for electricity

**Explanation:** Bitaxe provides fully open-source hardware, firmware, and software, breaking the closed-source monopoly of proprietary ASIC manufacturers.

**Q2. Which background knowledge does the course say is helpful (though not required)?**

- A. Professional mining experience
- B. Basic electronics and familiarity with GitHub **(✓)**
- C. A finance degree
- D. Chinese language skills

**Explanation:** No prior mining experience is required, but basic electronics knowledge and GitHub familiarity are helpful.

**Q3. Which is NOT one of the course's stated objectives?**

- A. Understand the philosophy of open-source mining hardware
- B. Build Bitaxe devices from scratch
- C. Configure and optimize AxeOS and Public Pool
- D. Launch a proprietary ASIC company **(✓)**

**Explanation:** Objectives are understanding the philosophy, building devices, configuring AxeOS/Public Pool, and implementing overclocking/benchmarking — not launching a proprietary company.

### Section 2.1 — The History

**Q4. Who is the founder of the Bitaxe project?**

- A. johnny9
- B. Skot **(✓)**
- C. SirVapesAlot
- D. wantclue

**Explanation:** Skot founded Bitaxe; his journey began after learning about Bitcoin at a college party.

**Q5. How did Skot first learn about Bitcoin?**

- A. From a TV advertisement
- B. At a college party, via someone purchasing on the Silk Road **(✓)**
- C. From a university lecture
- D. By mining it himself

**Explanation:** He first heard of Bitcoin (~$20/coin) at a college party through someone buying items on the Silk Road.

**Q6. What professional experience sparked the solar-mining idea?**

- ==A. Building solar-powered gateways for remote data collection in Africa **(✓)**==
- B. Working at Bitmain
- C. Designing electric cars
- D. Running a mining farm in Texas

**Explanation:** Working on solar-powered gateways in Africa, Skot realized low-voltage DC mining ASICs pair naturally with solar panels.

**Q7. What major obstacle did Skot face when reverse-engineering the ASIC chips?**

- A. The chips were too expensive
- ==B. A complete lack of documentation for Bitmain's chips **(✓)**==
- C. There were no ASICs available
- D. Government restrictions

**Explanation:** With no official datasheets, he examined chips under microscopes and measured pin pitches with calipers.

**Q8. When did the breakthrough working design appear, and what chips did it use?**

- ==A. May 2022, a two-chip design using BM1387 chips from Antminer S9 units **(✓)**==
- B. January 2020, BM1366 chips
- C. May 2022, BM1397 chips from the S17
- D. 2016, custom chips

**Explanation:** The third iteration in May 2022 worked — a two-chip design using BM1387 chips harvested from Antminer S9 units; this birthed the "Bitaxe" name.

**Q9. The Bitaxe name was inspired by what concept?**

- A. A computer mouse
- B. A pickaxe for Bitcoin mining **(✓)**
- C. A solar panel
- D. A microchip

**Explanation:** "Bitaxe" evokes a pickaxe for mining Bitcoin.

**Q10. Why did the firmware need to run on an ESP32 microcontroller?**

- A. To reduce cost only
- B. To create self-contained, deployable units without an external computer running software like CGMiner **(✓)**
- C. Because ASICs cannot mine alone
- D. To connect to the cloud

**Explanation:** Running mining software directly on the ESP32 made the units independent and deployable (e.g., under solar panels) without a separate computer.

**Q11. Who established the Open Source Miners United (OSMU) Discord server?**

- A. Skot
- B. SirVapesAlot **(✓)**
- C. Ben
- D. mrv777

**Explanation:** Community member SirVapesAlot recognized the potential and created the OSMU Discord, enabling collaboration.

**Q12. What did contributor Ben create, among other things?**

- A. The BM1397 chip
- B. The AxeOS dashboard, manufacturing capabilities, and Public Pool **(✓)**
- C. The Bitcoin protocol
- D. The Silk Road

**Explanation:** Ben built the AxeOS dashboard's front end, established manufacturing, and created Public Pool.

**Q13. What is Skot's ambitious long-term vision for distributed hash power?**

- A. One thousand miners totaling 1 PH/s
- B. One million 1-terahash miners creating one exahash of distributed power **(✓)**
- C. A single giant mining farm
- D. Replacing all industrial miners with GPUs

**Explanation:** Producing one million 1-TH miners would create an exahash of distributed mining power, advancing decentralization.

**Q14. Why is home mining economically attractive in this vision?**

- A. Governments subsidize it
- B. Infrastructure costs are essentially zero — devices plug into existing outlets and internet **(✓)**
- C. Electricity is free at home
- D. Home miners always find blocks

**Explanation:** Unlike industrial operations needing facilities and cooling, home miners use existing outlets and connections, so infrastructure cost is near zero.

### Section 2.2 — What is the Bitaxe?

**Q15. Which ASIC chip does the first-generation Bitaxe Max use?**

- A. BM1366 (from the S19 series)
- B. BM1397 (from the S17 series) **(✓)**
- C. BM1387 (from the S9)
- D. BM1368 (from the Super)

**Explanation:** The Bitaxe Max uses the BM1397 chip originally developed by Bitmain for the S17 mining series.

**Q16. What is the estimated hash rate of the Bitaxe Max?**

- A. 300 to 400 GH/s **(✓)**
- B. 1.1 TH/s
- C. 13.5 TH/s
- D. 40 PH/s

**Explanation:** The Bitaxe Max delivers roughly 300–400 gigahashes per second, positioning it as an educational/experimental platform.

**Q17. Which chip does the Bitaxe Ultra use?**

- A. BM1397
- B. BM1366 (from the S19 series) **(✓)**
- C. BM1387
- D. BM1397i

**Explanation:** The Bitaxe Ultra incorporates the more advanced BM1366 chip from Bitmain's S19 series.

**Q18. What type of microcontroller sits at the heart of every Bitaxe?**

- A. An Arduino Uno
- B. An ESP microcontroller running OSMU software **(✓)**
- C. A Raspberry Pi 4
- D. A BM1366 chip

**Explanation:** Every Bitaxe uses an ESP microcontroller, running OSMU-developed software, as the interface to the ASIC.

**Q19. What is the Bitaxe's strict power supply voltage requirement?**

- A. 12 volts
- B. 5 volts **(✓)**
- C. 1.2 volts
- D. 220 volts

**Explanation:** The Bitaxe operates on a strict 5-volt requirement; incorrect voltage can permanently damage the device.

**Q20. What is the typical power consumption range of a Bitaxe depending on configuration?**

- A. 5 to 25 watts **(✓)**
- B. 50 to 100 watts
- C. 1400 watts
- D. Under 1 watt

**Explanation:** Depending on frequency and voltage, a Bitaxe typically consumes between 5 and 25 watts.

**Q21. What kind of mining does the Bitaxe platform specifically target?**

- A. Pooled mining only
- B. Solo mining **(✓)**
- C. Cloud mining
- D. GPU mining

**Explanation:** Bitaxe targets solo mining — individuals attempting to solve blocks independently — for educational and decentralization purposes.

**Q22. Which connector change is cited as a production/usability improvement?**

- A. USB-C to micro-USB
- B. Micro-USB to USB-C **(✓)**
- C. HDMI to USB
- D. Ethernet to Wi-Fi

**Explanation:** The transition from micro-USB to USB-C reflects community-driven usability improvements.

**Q23. What philosophy reflects Bitaxe's focus on functionality over constant upgrades?**

- A. "Move fast and break things"
- B. "If it hashes, it hashes" **(✓)**
- C. "Don't trust, verify"
- D. "Not your keys, not your coins"

**Explanation:** The "if it hashes, it hashes" philosophy encourages maintaining and operating devices rather than chasing the newest version.

### Section 2.3 — Where Can I Learn More?

**Q24. What is the primary central hub for Bitaxe project information?**

- A. Bitaxe.org **(✓)**
- B. Reddit
- C. Twitter
- D. Bitmain.com

**Explanation:** Bitaxe.org is the central hub providing curated, verified links to all ecosystem resources.

**Q25. Which GitHub repository contains all the Bitaxe firmware code and documentation?**

- A. building.md
- B. ESP-Miner **(✓)**
- C. AxeOS-only
- D. KiCad-files

**Explanation:** The ESP-Miner repository is the central location for all firmware-related code and documentation.

**Q26. What is the purpose of the "Bitaxe legit list"?**

- A. To rank miners by hash rate
- B. To identify trustworthy vendors and avoid fraudulent sellers **(✓)**
- C. To list banned users
- D. To track block rewards

**Explanation:** The legit list curates verified vendors, notes who contributes back to OSMU, and protects against scams like unauthorized pre-orders.

**Q27. Where is structured, searchable, community-editable documentation found?**

- A. The OSMU wiki (osmu.wiki) **(✓)**
- B. The Discord chat history
- C. A printed manual
- D. The block explorer

**Explanation:** The osmu.wiki provides structured documentation, editable by the community via GitHub integration with a review process.

**Q28. The Bitaxe legit list emphasizes which kind of links to ensure unbiased recommendations?**

- A. Affiliate links
- B. Non-affiliate links **(✓)**
- C. Sponsored links
- D. Shortened links

**Explanation:** The list uses non-affiliate links so recommendations are based on legitimacy and community contribution, not financial incentives.

### Section 3.1 — What is AxeOS?

**Q29. How do you access the AxeOS dashboard?**

- A. Through a mobile app only
- B. By navigating to the Bitaxe device's IP address in a browser **(✓)**
- C. Via a USB cable only
- D. Through the Bitmain interface

**Explanation:** AxeOS is a browser-based interface reached at the device's IP address.

**Q30. Which four core metrics does the AxeOS dashboard present?**

- A. Price, volume, market cap, supply
- B. Hash rate, shares, efficiency, and best difficulty **(✓)**
- C. CPU, RAM, disk, network
- D. Voltage, current, resistance, power

**Explanation:** The dashboard's four key indicators are hash rate, shares submitted, efficiency, and best difficulty.

**Q31. What does the "best difficulty" indicator track, and when does it reset?**

- A. The average difficulty; resets daily
- B. The highest-difficulty share ever found; resets only on a complete factory flash **(✓)**
- C. The pool's difficulty; resets each block
- D. The network difficulty; never resets

**Explanation:** Best difficulty preserves the highest-difficulty share ever found, surviving reboots/updates and resetting only on a factory flash.

**Q32. What is the AxeOS Swarm feature for?**

- A. Mining multiple coins
- B. Managing multiple Bitaxe devices from a single dashboard by adding their IPs **(✓)**
- C. Increasing a single device's hashrate
- D. Connecting to multiple pools at once

**Explanation:** Swarm centralizes control of many devices — pool changes, restarts, frequency adjustments, monitoring — without juggling IP addresses.

**Q33. What are the default frequency and core voltage settings in AxeOS?**

- A. 550 MHz and 1150 mV
- B. 485 MHz and 1200 mV **(✓)**
- C. 700 MHz and 1175 mV
- D. 500 MHz and 1150 mV

**Explanation:** Defaults of 485 MHz frequency and 1200 mV core voltage provide stable operation for initial testing.

**Q34. Which two filenames does the AxeOS update interface accept?**

- A. firmware.hex and ui.zip
- B. esp-miner.bin and www.bin **(✓)**
- C. bitaxe.img and config.bin
- D. boot.bin and app.bin

**Explanation:** The update system accepts properly named files esp-miner.bin and www.bin to ensure compatibility.

**Q35. For the stratum user field, what do you enter for solo mining?**

- A. A pool username
- B. A Bitcoin address **(✓)**
- C. The device serial number
- D. Your Wi-Fi password

**Explanation:** The stratum user supports a Bitcoin address for solo mining (or a username for pool mining), with optional device identifiers.

### Section 4.1 — Open-Source Contribution Overview

**Q36. GitHub hosts projects using which underlying version control system?**

- A. SVN
- B. Git **(✓)**
- C. Mercurial
- D. Perforce

**Explanation:** GitHub is a cloud platform that hosts projects using Git, a distributed version control system.

**Q37. What does the "Fork" button do on a GitHub repository?**

- A. Deletes the repository
- B. Creates a personal copy of the repository under your account **(✓)**
- C. Stars the project
- D. Reports a bug

**Explanation:** Fork creates an independent personal copy that still maintains a connection to the original source.

**Q38. Under which license is the BitX project released?**

- A. MIT
- B. Apache 2.0
- C. GPL 3.0 **(✓)**
- D. BSD

**Explanation:** The About section identifies BitX as "open source ASIC Bitcoin miner hardware" under the GPL 3.0 license.

**Q39. What does a branch allow developers to do?**

- A. Permanently delete the master code
- B. Work on features/fixes/variants without affecting the primary development line **(✓)**
- C. Bill the project owner
- D. Encrypt the repository

**Explanation:** A branch is a copy/modified version of the codebase, letting developers work without disturbing the stable master branch.

**Q40. The Super 401 branch focuses on implementations using which ASIC chip?**

- A. BM1397
- B. BM1366
- C. The S21 ASIC **(✓)**
- D. BM1387

**Explanation:** The Super 401 branch focuses on the S21 ASIC chip for improved efficiency.

**Q41. The GitHub Issues section is specifically designed for what?**

- A. General questions and casual chat
- B. Legitimate technical problems and bugs, with reproduction details **(✓)**
- C. Buying and selling hardware
- D. Sharing memes

**Explanation:** Issues are for real technical problems and bugs; general questions belong in Discussions (or Discord).

**Q42. What is a pull request?**

- A. A request to download files
- B. A mechanism for contributors to propose changes for review and potential merging **(✓)**
- C. A way to delete a branch
- D. A donation request

**Explanation:** A PR submits a contributor's changes for maintainer review before integration into the main codebase.

**Q43. In version control, what do "tags" typically mark?**

- A. Spam comments
- B. Specific points/versions or milestones in the development timeline **(✓)**
- C. User profiles
- D. Pull request authors

**Explanation:** Tags mark specific points (often model numbers/hardware revisions), while releases are formal distributions with notes.

### Section 4.2 — Open-Source Contribution Hands-on

**Q44. What does the "Sync fork" button do?**

- A. Deletes your fork
- B. Pulls in the latest changes from the upstream original repository **(✓)**
- C. Pushes your changes to the original
- D. Creates a new branch

**Explanation:** Sync fork synchronizes your fork with the original by pulling the latest upstream changes.

**Q45. Which IDE is recommended for most open-source contributions in this course?**

- A. Eclipse
- B. Visual Studio Code **(✓)**
- C. Notepad
- D. Vim only

**Explanation:** Visual Studio Code is recommended, with the Git extension enabling GitHub integration from the IDE.

**Q46. For ESP32 projects, which extension is required (with version 5.1.3 recommended in this chapter)?**

- A. ESP-IDF **(✓)**
- B. PlatformIO
- C. Arduino Core
- D. CMake Tools

**Explanation:** The ESP-IDF extension is crucial for ESP32 projects; this chapter recommends version 5.1.3.

**Q47. Which language is typically used for the core firmware functionality?**

- A. Python
- B. C **(✓)**
- C. Ruby
- D. Go

**Explanation:** Firmware projects use C for core functionality, with TypeScript for UIs and Java for some utilities.

**Q48. What are the two cardinal rules of open-source contribution emphasized in the chapter?**

- A. Always use Linux and always fork
- B. Never publish untested code and never commit sensitive information **(✓)**
- C. Always squash commits and never branch
- D. Always request reviewers and never sync

**Explanation:** Never publish untested code (it can introduce bugs/vulnerabilities) and never commit secrets like passwords or API tokens.

**Q49. How should you view a rejected pull request, per the course?**

- A. As a personal failure
- B. As an opportunity to learn from feedback and refine the approach **(✓)**
- C. As a reason to quit
- D. As proof the project is broken

**Explanation:** Rejection is part of the iterative process; it's a chance to learn, refine, and propose better solutions.

### Section 4.3 — What's Public-Pool?

**Q50. What type of mining pool is Public Pool?**

- A. A proprietary pooled-mining service
- B. A fully open-source solo Bitcoin mining pool **(✓)**
- C. An altcoin pool
- D. A cloud-mining contract

**Explanation:** Public Pool is a fully open-source solo mining pool where individuals keep 100% of their block rewards.

**Q51. What is Public Pool's fee structure?**

- A. 2% flat
- B. 1–3% like traditional pools
- C. Zero fees **(✓)**
- D. 10% for solo miners

**Explanation:** Public Pool has a zero-fee structure; finders receive the complete block reward plus all transaction fees.

**Q52. What is the current full block reward referenced for solo mining?**

- A. 6.25 BTC + fees
- B. 3.125 BTC + fees **(✓)**
- C. 50 BTC + fees
- D. 12.5 BTC + fees

**Explanation:** The chapter states the current block reward is 3.125 BTC plus transaction fees.

**Q53. What is the main trade-off of solo mining (even via Public Pool)?**

- A. High fees
- B. Extreme reward variance — you're only paid when you personally find a block **(✓)**
- C. No transparency
- D. Loss of your Bitcoin address

**Explanation:** Solo mining means full rewards but extreme variance (months/years between blocks), unlike pooled mining's steady income.

**Q54. How is Public Pool's zero-fee operation funded?**

- A. Government grants
- B. An affiliate program — code "SOLO" gives discounts; 50% of affiliate earnings fund operations, 50% rewards top difficulty shares **(✓)**
- C. A 2% hidden fee
- D. Selling user data

**Explanation:** Partner vendors give discounts via code "SOLO"; half the affiliate earnings sustain the pool, half reward miners with the highest monthly difficulty shares.

**Q55. What does Public Pool represent in the path toward decentralization?**

- A. The final destination
- B. A stepping stone toward miners running their own pools **(✓)**
- C. A centralized authority
- D. A replacement for Bitcoin nodes

**Explanation:** Running your own pool is the highest decentralization; Public Pool is a transparent stepping stone and learning platform toward that.

**Q56. To connect to Public Pool, what do miners provide as the username?**

- A. Their email
- B. Their Bitcoin address (optionally with a worker name after a dot) **(✓)**
- C. A pool-assigned ID
- D. Their Wi-Fi SSID

**Explanation:** Miners configure Stratum details and use their Bitcoin address as the username, with an optional worker name after a dot.

### Section 4.4 — Installing Public-Pool on Umbrel

**Q57. What hardware is recommended for a home Public Pool setup?**

- A. A high-end gaming PC with a GPU
- B. A mini PC with an Intel N100 and at least 1 TB NVMe storage **(✓)**
- C. A Raspberry Pi Zero
- D. A smartphone

**Explanation:** The recommended config is a mini PC with an Intel N100 processor and ≥1 TB NVMe to hold the Bitcoin blockchain.

**Q58. Why is the 1 TB NVMe drive critical?**

- A. For storing mining rewards
- B. Because running the pool requires a fully synchronized Bitcoin node with fast read/write **(✓)**
- C. To cache web pages
- D. For video editing

**Explanation:** A mining pool needs a full Bitcoin node; the NVMe ensures fast read/write for blockchain sync and transaction processing.

**Q59. What role does Umbrel play?**

- A. It's a mining ASIC
- B. A node-management platform that handles Bitcoin Core install/sync/maintenance via a web UI and app store **(✓)**
- C. A cryptocurrency exchange
- D. A firmware flasher

**Explanation:** Umbrel abstracts node complexity, offering a web interface and app-store model to install services like Public Pool.

**Q60. How do you install Public Pool on Umbrel?**

- A. Compile it from source manually
- B. Through the Umbrel app store — search "public pool" and install with a few clicks **(✓)**
- C. By flashing firmware over USB
- D. It cannot be installed on Umbrel

**Explanation:** Installation is via the Umbrel app store: search "public pool," confirm, and the automated setup configures the node connection.

**Q61. To connect your miner to the home pool, what must you configure?**

- A. A new Bitcoin wallet
- B. The miner's pool settings to point to your local IP and the assigned port **(✓)**
- C. A cloud account
- D. A VPN on the ASIC

**Explanation:** You replace the default pool address with your local IP and the port assigned during installation to redirect mining to your infrastructure.

### Section 5.1 — What Tools to Use?

**Q62. Which solder paste is specifically recommended for Bitaxe/SMD work?**

- A. ChipQuik TS391SNL50 **(✓)**
- B. The cheapest available paste
- C. Lead-free generic paste
- D. Plumber's flux

**Explanation:** ChipQuik TS391SNL50 maintains proper consistency/melting characteristics, avoiding the re-flow problems of cheap pastes.

**Q63. What problem do cheap, low-melting-point solder pastes cause?**

- A. They never melt
- B. Previously soldered joints become fluid again when heating adjacent areas, displacing components **(✓)**
- C. They are toxic
- D. They increase hashrate

**Explanation:** Low-quality pastes re-liquefy nearby joints during work, leading to component displacement and poor connections.

**Q64. What is a desoldering rig?**

- A. A magnifying lamp
- B. A heated vacuum tool that removes excess solder and corrects bridges **(✓)**
- C. A type of tweezers
- D. A PCB holder

**Explanation:** A desoldering rig is essentially a heated vacuum tool; combined with flux it clears excess solder and bridged pins.

**Q65. What is used to clean flux residue from a board for a professional finish?**

- A. Water and soap
- B. Isopropanol alcohol with a dedicated brush (e.g., an old toothbrush) **(✓)**
- C. Acetone and a rag
- D. Compressed air only

**Explanation:** Isopropanol plus a brush removes flux residue and paste remnants, leaving a clean board that's easy to inspect.

**Q66. At roughly what temperature do budget hot air rework stations typically operate?**

- A. ~100 °C
- B. ~250 °C
- C. ~355 °C **(✓)**
- D. ~600 °C

**Explanation:** Entry-level stations typically operate effectively at about 355 °C with automatic temperature reduction when holstered.

### Section 5.2 — Fix Solder Issues

**Q67. Which components require careful orientation, marked by a small dot?**

- A. Resistors R1 and R2
- B. MOSFETs Q1 and Q2 **(✓)**
- C. Capacitors C1 and C2
- D. The ESP32

**Explanation:** MOSFETs Q1 and Q2 have a dot marker and a four-pin layout (one large pad, three small) that must match the board.

**Q68. What is the role of the buck converter U9, and what does it convert?**

- A. It boosts 1.2 V to 5 V
- B. It converts 5 volts down to 1.2 volts for the ASIC chip **(✓)**
- C. It regulates Wi-Fi signals
- D. It controls the fan

**Explanation:** U9 is a critical, failure-prone buck converter that steps 5 V down to the 1.2 V the ASIC needs.

**Q69. What audible clue indicates a U9 solder bridge issue?**

- A. A clicking sound
- B. High-frequency noise that differs from normal ASIC operation **(✓)**
- C. Complete silence
- D. A beeping alarm

**Explanation:** A bridged U9 produces distinctive high-frequency noise, an auditory diagnostic clue (if you can hear high frequencies).

**Q70. At what temperature should you solder heat-sensitive parts like the Y1 crystal oscillator and U1?**

- A. 350 °C, minimizing heat application time **(✓)**
- B. 450 °C for as long as needed
- C. 200 °C indefinitely
- D. 500 °C briefly

**Explanation:** Keep the iron at 350 °C and minimize time on these heat-sensitive components to prevent damage.

### Section 5.3 — Debug Your Bitaxe Using AxeOS

**Q71. What is the normal power consumption range for Bitaxe Ultra/Supra models?**

- A. 1 to 3 watts
- B. 10 to 17 watts **(✓)**
- C. 25 to 40 watts
- D. 50 to 100 watts

**Explanation:** Normal operation is roughly 10–17 watts; consumption far below this (especially under 3 W) signals a fundamental fault.

**Q72. An ASIC voltage of exactly 1.2 V combined with power below 3 W indicates what?**

- A. Normal operation
- B. A soldering problem with the ASIC or a completely failed ASIC **(✓)**
- C. A Wi-Fi failure
- D. A fan problem

**Explanation:** Power reaches the chip location (1.2 V present) but the chip isn't working — inspect the die for cracks; suspect bad soldering or a dead ASIC.

**Q73. Low power paired with a very low requested voltage (e.g., 100 mV or 0.5 V) points to which component?**

- A. The Wi-Fi antenna
- B. The U9 buck converter **(✓)**
- C. The ESP32
- D. The display

**Explanation:** This pattern indicates inadequate voltage supply, typically a problem with the U9 buck converter's voltage regulation.

**Q74. In the AxeOS logs, what confirms the ASIC is powered and actively working?**

- A. "Welcome to the Bitaxe" message
- B. The presence of "ASIC results" entries **(✓)**
- C. A green LED
- D. The IP address display

**Explanation:** "ASIC results" entries confirm the chip is powered, processing work, and communicating with the control system.

**Q75. In the troubleshooting sequence, which component is checked last if problems persist after ASIC replacement?**

- A. U9
- B. U10
- C. U2 (which drives the ASIC) **(✓)**
- D. Y1

**Explanation:** If issues remain after resoldering U9 and replacing the ASIC, U2 — which drives the ASIC chip — is the final element to address.

### Section 5.4 — Debug Using USB?

**Q76. Which command initiates the USB serial connection to the Bitaxe via ESP-IDF?**

- A. idf.py flash
- B. idf.py monitor **(✓)**
- C. npm run build
- D. git clone

**Explanation:** `idf.py monitor` scans COM ports to establish UART communication with the ESP32 and streams the logs.

**Q77. What message confirms successful firmware loading during boot?**

- A. "Hello World"
- B. "Welcome to the Bitaxe. Hack the planet" **(✓)**
- C. "Mining started"
- D. "ASIC results"

**Explanation:** The boot sequence shows ESP-IDF version info followed by the distinctive "Welcome to the Bitaxe. Hack the planet" message.

**Q78. For a single-chip device, which log message validates proper ASIC connection?**

- A. "detected one ASIC chip" **(✓)**
- B. "ASIC voltage 5V"
- C. "no chips found"
- D. "DHCP assigned"

**Explanation:** The crucial detection message "detected one ASIC chip" confirms the mining hardware is connected and communicating with the ESP32.

**Q79. A DS4432U "ESP_ERROR_CHECK failed" timeout error typically points to which component?**

- A. U2
- B. U10 (display communication / voltage regulation) **(✓)**
- C. The crystal Y1
- D. The fan header

**Explanation:** DS4432U I2C failures point to voltage regulation or soldering problems affecting U10, responsible for display communication.

**Q80. Which chip handles temperature and fan control, generating its own distinctive error signatures?**

- A. BM1366
- B. EMC2101 **(✓)**
- C. DS4432U
- D. ESP32

**Explanation:** The EMC2101 temperature and fan control chip produces distinctive log signatures that help identify failures.

**Q81. What is a key advantage of USB serial monitoring over web-based debugging?**

- A. It's faster to type
- B. Continuous log capture isn't lost during reboots/disconnections **(✓)**
- C. It requires no cable
- D. It increases hashrate

**Explanation:** Serial monitoring captures all diagnostic data even through reboots, unlike web interfaces that lose data on disconnection.

### Section 6.1 — Modify the PCB

**Q82. Which open-source software is used for PCB design and routing?**

- A. AutoCAD
- B. KiCad **(✓)**
- C. Photoshop
- D. Fusion 360

**Explanation:** KiCad is the open-source PCB design/routing tool; it lets users examine and modify the complete Bitaxe design.

**Q83. Which is the most accessible PCB modification for KiCad newcomers?**

- A. Re-routing power traces
- B. Customizing the logo via the image converter tool **(✓)**
- C. Changing the ASIC chip
- D. Redesigning the schematic

**Explanation:** Logo customization requires minimal technical knowledge and gives immediate visual results using the image converter.

**Q84. What type of source image works best for the silkscreen logo conversion?**

- A. Low-resolution images
- B. High-contrast designs **(✓)**
- C. Full-color photos
- D. Animated GIFs

**Explanation:** High-contrast designs translate well to the silkscreen printing process used in PCB manufacturing.

**Q85. What KiCad feature helps verify modifications keep electrical/manufacturing compatibility?**

- A. The 3D viewer only
- B. Design rule checking and verification tools **(✓)**
- C. The image converter
- D. The footprint editor

**Explanation:** KiCad's design rule checking prevents common errors and educates users about industry standards.

### Section 6.2 — How to Create a Factory File?

**Q86. What is the main benefit of a factory file?**

- A. It increases hashrate
- B. It embeds configuration directly into the firmware, removing manual setup **(✓)**
- C. It cools the ASIC
- D. It bypasses the bootloader

**Explanation:** Factory files embed settings into the binary, eliminating manual configuration — valuable for multi-device deployments.

**Q87. Which ESP-IDF version does this chapter recommend to avoid build issues?**

- A. 5.1.3
- B. 5.3 Beta 1 **(✓)**
- C. 4.4
- D. 6.0

**Explanation:** Version 5.1.3 caused build issues; 5.3 Beta 1 is recommended as it resolves them.

**Q88. Which commands build the AxeOS web interface before the firmware build?**

- A. git clone then git push
- B. npm install then npm run build **(✓)**
- C. idf.py monitor then idf.py flash
- D. make then make install

**Explanation:** In the AxeOS subdirectory, `npm install` installs dependencies and `npm run build` compiles the web assets embedded into the firmware.

**Q89. The NVS partition generator converts config.csv into a config.binary targeting which memory address?**

- A. 0x1000
- B. 0x6000 **(✓)**
- C. 0xFFFF
- D. 0x0000

**Explanation:** The nvs-partition-gen.py script generates config.binary targeting the 0x6000 memory address space.

**Q90. Which configuration corresponds to Super devices versus Ultra variants?**

- A. BM1366 for Super, BM1368 for Ultra
- B. BM1368 for Super, BM1366 for Ultra **(✓)**
- C. BM1397 for both
- D. BM1387 for Super, BM1397 for Ultra

**Explanation:** The repo provides BM1368 config for Super devices and BM1366 settings for Ultra variants.

### Section 6.3 — How to Use the Bitaxe Web Flasher?

**Q91. Which browser is required for the Bitaxe Web Flasher?**

- A. Firefox
- B. Chrome (or Chromium-based) — Brave and Firefox lack Web Serial API support **(✓)**
- C. Safari
- D. Internet Explorer

**Explanation:** The flasher relies on the Web Serial API; Chrome works fully, while Brave and Firefox lack the necessary support.

**Q92. Which Bitaxe versions require external power (not just USB) during flashing?**

- A. Version 204 and below
- B. Version 205 and above **(✓)**
- C. All versions
- D. No versions

**Explanation:** Devices at version 205+ need external power plus USB; versions ≤204 can flash on USB power alone.

**Q93. What is the correct procedure to enter bootloader mode?**

- A. Connect USB first, then press boot
- B. Press and hold the boot button before connecting the USB-C cable **(✓)**
- C. Hold boot for 30 seconds after boot-up
- D. Remove power, then press boot

**Explanation:** You must hold the boot button before plugging in USB-C; connecting first yields normal operation, not bootloader mode.

**Q94. During an Update installation, how should you respond to the "erase device?" prompt?**

- A. Accept it to be safe
- B. Decline it by clicking "Next" — accepting erases the config and can break the device **(✓)**
- C. Ignore the warning
- D. Restart the computer

**Explanation:** Accepting the erase during an Update removes the config file (potentially non-functional); decline by clicking "Next" to preserve settings.

**Q95. What does a Factory installation do compared to an Update?**

- A. Only changes the logo
- B. Completely erases firmware/config and reinstalls fresh with a self-test, wiping Wi-Fi and BTC address **(✓)**
- C. Preserves all user settings
- D. Updates only the web interface

**Explanation:** Factory installs erase everything (Wi-Fi, BTC address, settings) and reinstall like manufacturing, with self-test; Updates preserve config.

### Section 6.4 — How to Create and Order the PCB?

**Q96. Which file format is the industry standard for communicating PCB designs to manufacturers?**

- A. STL files
- B. Gerber files **(✓)**
- C. PDF files
- D. PNG files

**Explanation:** Gerber files contain copper layers, solder mask, and drill data; in KiCad they're generated via fabrication outputs and zipped for upload.

**Q97. Which two PCB manufacturers are named as popular choices?**

- A. TSMC and Intel
- B. JLCPCB and PCBWay **(✓)**
- C. Bitmain and Avalon
- D. Foxconn and Samsung

**Explanation:** JLCPCB and PCBWay are among the most popular options for hobbyists and professionals.

**Q98. What is true about PCB color choice?**

- A. It affects electrical performance
- B. It is purely aesthetic; green is most cost-effective **(✓)**
- C. Only green is available
- D. It changes the hashrate

**Explanation:** Color is purely aesthetic and doesn't affect electrical performance; green is traditional and cheapest.

### Section 7 — Performance Optimization

**Q99. What does the Bitaxe Hashrate Benchmark tool do, and who maintains it?**

- A. Mines blocks; built by Bitmain
- B. Systematically tests frequency/voltage combos for optimal settings; by WhiteCookie, enhanced by mrv777, under GPLv3 **(✓)**
- C. Overclocks automatically to 700 MHz; by Skot
- D. Flashes firmware; by JLCPCB

**Explanation:** This Python tool (WhiteCookie, enhanced by mrv777, GPLv3) takes ~30–40 min, prioritizes safety (backing off near 66 °C), and outputs JSON ranking the top five configs for hashrate and efficiency.

**Q100. How do you unlock custom frequency/voltage fields for advanced overclocking, and what increment is advised?**

- A. Hold the boot button; 100 MHz steps
- B. Append "?OC" to the device's web URL; use conservative 10–15 MHz increments **(✓)**
- C. Flash a factory file; 50 MHz steps
- D. Use the Swarm menu; 1 MHz steps

**Explanation:** Appending "?OC" to the web interface URL exposes manual frequency/voltage controls; advancing in 10–15 MHz steps prevents thermal spikes and allows stability testing (the voltage regulator tolerates up to ~100 °C but with reduced efficiency/longevity).