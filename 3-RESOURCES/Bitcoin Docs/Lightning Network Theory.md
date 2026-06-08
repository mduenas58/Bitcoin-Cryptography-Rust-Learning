# Lightning Network Theory — A Technical Study Companion

## Overall explanation of the subject

The **Lightning Network (LN)** is a _layer-2_ protocol built on top of Bitcoin that enables fast, cheap, high-volume payments without recording every transaction on the blockchain. Bitcoin's base layer is secure and decentralized but deliberately throughput-limited (roughly a handful of transactions per second, ~10-minute blocks). Lightning solves this by letting two parties open a **payment channel** — a single on-chain funding transaction that locks bitcoin into a 2-of-2 multisig — and then exchange a virtually unlimited number of _off-chain_ updates that re-apportion that locked balance. Only two transactions ever need to touch the blockchain: the one that opens the channel and the one that closes it. Everything in between is a sequence of cryptographically signed promises that either party can enforce on-chain if needed.

The genius of Lightning is twofold. First, **commitment transactions** plus a **revocation (penalty) mechanism** make off-chain balance updates _trustless_: if your counterparty tries to cheat by broadcasting an old, more-favorable-to-them channel state, you can take _all_ the channel funds as a penalty. Second, **Hashed Time-Locked Contracts (HTLCs)** let payments be routed _across multiple channels_ through intermediaries who never get custody of the funds — a payment from Alice to Carol can hop through Bob without Bob being able to steal it. Chained HTLCs turn isolated channels into a connected _network_ over which payments find a path the way packets find a route on the internet.

This curriculum builds that understanding from the ground up: first the Bitcoin primitives Lightning depends on (UTXOs, transactions, multisig, timelocks), then the channel lifecycle (open → update → close, with the revocation machinery that keeps it honest), then the network layer (HTLCs, routing, onion encryption, gossip), and finally the practical tooling (invoices, LNURL, keysend, liquidity management). The throughline to keep in mind: **Lightning is a system of pre-signed Bitcoin transactions held in reserve**; its safety always reduces to "what can each party broadcast on-chain, and who wins if they do?" Master that question and the whole protocol becomes legible.

For each chapter below you will find a comprehensive technical explanation, a curated and ordered resource list (beginner → master), and five questions graded from foundational to expert.

Canonical primary sources referenced throughout:

- **BOLTs** (Basis of Lightning Technology specs): `github.com/lightning/bolts` — BOLT 1–11 are the authoritative protocol definition.
- **Mastering the Lightning Network** by Antonopoulos, Osuntokun & Pickhardt (free on GitHub: `github.com/lnbook/lnbook`).
- The original **Lightning Network paper** (Poon & Dryja, 2016).
- Implementation docs: **LND** (lightning.engineering), **Core Lightning / CLN** (corelightning.org), **Eclair** (ACINQ), **LDK** (lightningdevkit.org).
- **River**, **Voltage**, and **Bitcoin Optech** technical write-ups.

---

## 1 — Introduction

### 1.1 — Course Overview

**Comprehensive explanation.** This opening chapter sets the conceptual frame: Lightning is not a separate coin or a sidechain, but a _protocol layer_ whose security ultimately derives from the ability to settle on Bitcoin's base chain at any time. The key reframing for newcomers is that a Lightning balance is not "coins inside Lightning" — it is _your share of a Bitcoin UTXO that two parties have agreed on but not yet broadcast_. The course will move from Bitcoin fundamentals upward through channels, the network, and tooling. Establishing the right mental model now — **off-chain promises backed by enforceable on-chain transactions** — prevents the most common misconceptions (that Lightning is custodial, or that funds "leave" the blockchain). It also previews the central tension Lightning manages: trust-minimization versus the convenience of instant payments, resolved through clever transaction construction rather than trusted third parties.

**Resources.**

- _Mastering the Lightning Network_, Ch. 1 ("Introduction") and Ch. 2 ("Getting Started") — the ideal conceptual on-ramp.
- The Lightning Network whitepaper (Poon–Dryja, 2016) — read the abstract and intro now, the full paper later.
- lightning.network — official overview and FAQ.
- Bitcoin Optech "Lightning Network" topic index (`bitcoinops.org/en/topics/`).
- River Learn "What is the Lightning Network?" — clean beginner explainer.

**Questions.**

1. _(Foundational)_ In one sentence, what layer does Lightning occupy and what is its relationship to the Bitcoin base chain?
2. _(Core)_ Why is a Lightning balance better described as "a share of an unbroadcast UTXO" than as "coins stored on Lightning"?
3. _(Applied)_ Name the only two transactions that _must_ hit the blockchain in a normal channel lifecycle, and what each accomplishes.
4. _(Analytical)_ What problem with Bitcoin's base layer (throughput, fees, latency) does Lightning specifically target, and what does it deliberately _not_ try to replace?
5. _(Mastery)_ Articulate the core trust model: under what conditions is Lightning trustless, and what residual assumptions (online-ness, fee markets, watchtowers) does that trustlessness depend on?

---

## 2 — The Fundamentals

### 2.1 — Understanding the Lightning Network

**Comprehensive explanation.** This chapter develops the network-level intuition before the cryptographic detail. Channels are edges; nodes are vertices; payments traverse paths of channels. Crucially, two parties who have no direct channel can still pay each other if a _path_ of sufficiently funded channels connects them. The chapter introduces capacity vs. **liquidity directionality** (a channel's balance can be lopsided, so it may route in one direction but not the other), the role of **routing nodes**, and the difference between _public_ (announced in gossip) and _private/unannounced_ channels. It also frames the properties Lightning aims for: instant settlement, sub-cent fees, and privacy via source-routed onion payments. The mental leap is from "a channel between two people" to "a mesh of channels over which value flows."

**Resources.**

- _Mastering the Lightning Network_, Ch. 1 & 12 ("Lightning Network Architecture").
- learnmeabitcoin or River Learn network-topology explainers.
- BOLT 7 ("P2P Node and Channel Discovery") — how the network graph is built.
- Visualizations: `amboss.space`, `1ml.com`, `mempool.space/lightning` — explore real topology.
- Pickhardt & Richter, "Optimally Reliable & Cheap Payment Flows" (paper) for advanced network-flow framing.

**Questions.**

1. _(Foundational)_ What are the "nodes" and "edges" of the Lightning graph?
2. _(Core)_ Distinguish a channel's total _capacity_ from its directional _liquidity_, and why the distinction matters for routing.
3. _(Applied)_ How can Alice pay Carol if they share no direct channel? What must be true of the intervening channels?
4. _(Analytical)_ Compare public (announced) and unannounced channels in terms of routing usefulness and privacy.
5. _(Mastery)_ Why is Lightning routing fundamentally a _liquidity flow_ problem rather than a shortest-path problem, and what does that imply for large-payment reliability?

### 2.2 — Bitcoin, Addresses, UTXO, and Transactions

**Comprehensive explanation.** Lightning is unintelligible without the Bitcoin primitives it manipulates. This chapter covers the **UTXO model** (Bitcoin state is a set of unspent transaction outputs, each locked by a script), **transaction structure** (inputs reference and spend prior outputs; outputs create new ones; the difference is the fee), **scriptPubKey/witness** (the locking conditions), **multisig** (n-of-m, specifically the 2-of-2 that funds a channel), and **timelocks** — both absolute (`nLockTime`, `OP_CHECKLOCKTIMEVERIFY`) and relative (`nSequence`, `OP_CHECKSEQUENCEVERIFY` / CSV from BIP-68/112). These timelocks are the backbone of channel safety: revocation windows and HTLC timeouts are all enforced by them. SegWit (BIP-141) is also essential, because it fixed transaction malleability — without that fix, the pre-signed-transaction design of channels would be unsafe.

**Resources.**

- _Mastering Bitcoin_ (3rd ed.), Ch. 6 ("Transactions") and Ch. 7 ("Advanced Transactions and Scripting") — multisig, CLTV, CSV.
- _Mastering the Lightning Network_, Ch. 2 appendix on Bitcoin fundamentals.
- BIP-65 (CLTV), BIP-68/112/113 (relative timelocks, CSV), BIP-141 (SegWit).
- learnmeabitcoin.com — "Transaction", "Multisig", "Timelocks", "SegWit" pages.
- _Programming Bitcoin_ (Jimmy Song), Ch. 5–8 for hands-on transaction construction.

**Questions.**

1. _(Foundational)_ What is a UTXO, and what makes an output "spent"?
2. _(Core)_ Describe the structure of a Bitcoin transaction and how the fee is implicitly defined.
3. _(Applied)_ What is a 2-of-2 multisig, and why is it the natural construct for a two-party payment channel?
4. _(Analytical)_ Contrast absolute (CLTV) and relative (CSV) timelocks. Give a Lightning use case for each.
5. _(Mastery)_ Explain why transaction malleability would break the channel design, and precisely how SegWit's separation of the witness from the txid solves it.

---

## 3 — Opening and Closing Channels

### 3.1 — Channel Opening

**Comprehensive explanation.** Opening a channel means creating a **funding transaction** that pays into a 2-of-2 multisig output controlled by both parties. The critical safety subtlety: before the funding transaction is _broadcast_, the parties first exchange signatures for an initial **commitment transaction** that can spend the funding output back to them. This ordering guarantees neither party can lock the other's money with no way out. The chapter covers the BOLT 2 opening handshake (`open_channel`, `accept_channel`, `funding_created`, `funding_signed`, `channel_ready`), the confirmation depth before the channel is usable, and **dual-funding** (BOLT-level interactive tx construction) where both parties contribute inputs. It also introduces channel parameters: capacity, push amount, reserve requirements, `to_self_delay`, and dust limits.

**Resources.**

- BOLT 2 ("Peer Protocol for Channel Management") — the opening message flow.
- _Mastering the Lightning Network_, Ch. 9 ("Channel Operation and Payment Forwarding") and Ch. 10.
- LND / CLN docs on `openchannel`, funding confirmation, and `minconf`.
- Bitcoin Optech "Dual funding" and "v2 channel establishment" topics.
- The Lightning paper §"Funding" for the original construction.

**Questions.**

1. _(Foundational)_ What kind of output does a funding transaction create, and who controls it?
2. _(Core)_ Why must the parties exchange the first commitment transaction's signatures _before_ the funding transaction is broadcast?
3. _(Applied)_ Walk through the BOLT 2 opening message sequence from `open_channel` to `channel_ready`.
4. _(Analytical)_ What are channel _reserve_ and `to_self_delay`, and what attacks or risks do they mitigate?
5. _(Mastery)_ Explain how dual/interactive funding changes the trust and liquidity dynamics versus single-funder channels, and the new attack surface it introduces.

### 3.2 — Commitment Transaction

**Comprehensive explanation.** The **commitment transaction** is the heart of a channel: at every channel state, each party holds a (differently constructed) commitment transaction that spends the funding output to reflect the _current_ balance split. It is pre-signed by the counterparty so either side can unilaterally close by broadcasting it. The asymmetry is deliberate: my commitment pays _me_ via a delayed (`to_self_delay` via CSV) output and pays _you_ immediately, while your commitment mirrors that — the delay on one's own output is what gives the counterparty time to penalize a revoked state. The chapter covers the `to_local` and `to_remote` outputs, how HTLC outputs are added, dust handling, and fee/anchor-output mechanics (anchor channels, BOLT-3) that let commitment fees be bumped via CPFP after the fact.

**Resources.**

- BOLT 3 ("Bitcoin Transaction and Script Formats") — exact commitment & HTLC scripts.
- _Mastering the Lightning Network_, Ch. 9 & Appendix on commitment transactions.
- The Lightning paper §"Commitment Transactions."
- Bitcoin Optech "Anchor outputs" topic — fee bumping for commitments.
- LND `lncli` "pendingchannels"/"closedchannels" and CLN equivalents to inspect real commitment states.

**Questions.**

1. _(Foundational)_ What balance does a commitment transaction encode, and who signs it?
2. _(Core)_ Why are the two parties' commitment transactions _asymmetric_, and which output carries the CSV delay?
3. _(Applied)_ What are the `to_local` and `to_remote` outputs, and how does each party's commitment treat them differently?
4. _(Analytical)_ Why are anchor outputs needed, and how do they decouple the commitment fee from the fee paid at broadcast time?
5. _(Mastery)_ Trace exactly how the `to_local` output script is constructed so that the owner can claim it only after a delay, while the counterparty can claim it _immediately_ with a revocation secret.

### 3.3 — Revocation Key

**Comprehensive explanation.** Revocation is what makes off-chain updates safe. When the channel advances to a new state, each party **reveals the revocation secret** of the _previous_ state to the other. That secret lets the counterparty immediately sweep the _entire_ channel balance if the cheater ever broadcasts the now-revoked commitment. The chapter explains the construction: revocation public keys are derived by combining each party's `revocation_basepoint` with a per-commitment point, so that knowledge of the per-commitment _secret_ (revealed on update) yields the revocation _private_ key. It covers the **per-commitment secret** derivation (a shift-register/hash-chain so an entire history can be stored compactly, per BOLT 3), the **penalty (justice) transaction**, and why this "asymmetric punishment" — broadcast an old state and lose everything — deters cheating without any trusted party. Watchtowers, which watch for revoked broadcasts on your behalf while you're offline, are introduced here.

**Resources.**

- BOLT 3 §"Per-commitment Secret Requirements" and §"Key Derivation."
- _Mastering the Lightning Network_, Ch. 9 — revocation and the penalty mechanism.
- The Lightning paper §"Revocable Delivery / Breach Remedy."
- BOLT 13 / watchtower docs (LND watchtower, CLN `teos`) — outsourced revocation.
- rusty Russell / ACINQ blog posts on per-commitment secret storage.

**Questions.**

1. _(Foundational)_ What does a party reveal when the channel moves to a new state, and why?
2. _(Core)_ How does revealing the per-commitment secret let your counterparty punish you for broadcasting an old state?
3. _(Applied)_ Describe the penalty (justice) transaction: what does it spend, and how much can the honest party claim?
4. _(Analytical)_ Explain how the per-commitment secrets are derived so that an entire channel history can be reconstructed/stored from a compact seed.
5. _(Mastery)_ Derive how the revocation private key is reconstructed from the revocation basepoint secret and the revealed per-commitment secret, and why neither party alone can compute it in advance.

### 3.4 — Channel Closure

**Comprehensive explanation.** Channels close in three modes. **Mutual (cooperative) close**: both parties agree, negotiate a fee, and co-sign a clean closing transaction that pays each their current balance immediately with no timelocks — cheapest and fastest. **Unilateral (force) close**: one party broadcasts their latest commitment transaction; their own funds are subject to the `to_self_delay` CSV, and any in-flight HTLCs resolve via their timeout/ success paths. **Breach/penalty close**: a party broadcasts a _revoked_ commitment and the honest counterparty (or their watchtower) sweeps everything via the justice transaction. The chapter covers the BOLT 2 `shutdown`/`closing_signed` flow, fee negotiation, how pending HTLCs are handled at close, and the implications for capital lockup and timing.

**Resources.**

- BOLT 2 §"Channel Close" (`shutdown`, `closing_signed`) and BOLT 5 ("Recommendations for On-chain Transaction Handling").
- _Mastering the Lightning Network_, Ch. 9 — closing scenarios.
- LND/CLN docs on `closechannel` (cooperative vs force) and sweeping outputs.
- Bitcoin Optech "Channel close" and "anchor/CPFP fee bumping" discussions.
- mempool.space examples of real force-close and penalty transactions.

**Questions.**

1. _(Foundational)_ Name the three ways a channel can close.
2. _(Core)_ Why is a mutual close cheaper and faster than a force close?
3. _(Applied)_ In a force close, why are the broadcaster's own funds delayed while the counterparty's are immediately spendable?
4. _(Analytical)_ How are in-flight HTLCs resolved when a channel is force-closed, via their timeout and success branches?
5. _(Mastery)_ Compare the on-chain footprint, fee exposure, and security outcome of all three close types, and explain when a rational node prefers each.

---

## 4 — A Liquidity Network

### 4.1 — Lightning Network

**Comprehensive explanation.** This chapter elevates from single channels to the **routed network**. A payment is _source-routed_: the sender computes the full path and constructs an **onion** (BOLT 4, Sphinx construction) so each hop learns only its predecessor and successor, never the ultimate origin or destination. Forwarding nodes earn **routing fees** (a base fee plus a proportional `fee_rate`), advertised via gossip (BOLT 7) along with `cltv_expiry_delta` and channel policies. The chapter ties together how the network graph is discovered (`channel_announcement`, `channel_update`, `node_announcement`), how senders pick paths, and how privacy is preserved by onion routing. It frames the network as a liquidity fabric whose reliability depends on where balances sit, not just on connectivity.

**Resources.**

- BOLT 4 ("Onion Routing Protocol") and BOLT 7 ("P2P Node and Channel Discovery").
- _Mastering the Lightning Network_, Ch. 10 ("Onion Routing") and Ch. 12 ("Path Finding").
- The Sphinx paper (Danezis & Goldberg) — onion-routing foundations.
- Amboss / LnRouter analytics for fee and routing policy data.
- Pickhardt–Richter payment-flow papers for advanced multi-path routing.

**Questions.**

1. _(Foundational)_ What does "source routing" mean, and who computes the path?
2. _(Core)_ What does each forwarding hop learn and _not_ learn from the onion packet?
3. _(Applied)_ How is a routing fee structured (base + proportional), and where is the policy advertised?
4. _(Analytical)_ Why does `cltv_expiry_delta` decrease along the route, and what risk would a too-small delta create for an intermediary?
5. _(Mastery)_ Explain the Sphinx onion construction: fixed packet size, per-hop shared-secret derivation (ECDH), and HMAC integrity — and how these defeat traffic analysis.

### 4.2 — HTLC — Hashed Time-Locked Contract

**Comprehensive explanation.** The HTLC is the contract that makes _trustless routing_ possible. It locks funds with two escape paths: the recipient can claim by revealing a **preimage** `r` such that `H(r) = payment_hash` (the success path), or the sender reclaims after a **timeout** (CLTV, the timeout path). Across a route, every hop's HTLC is locked to the _same_ payment hash, so when the final recipient reveals the preimage to claim their incoming HTLC, each upstream hop in turn uses that revealed preimage to claim _its_ incoming HTLC. This atomicity means either the whole payment settles or it all unwinds — no intermediary can be left out of pocket. The chapter covers HTLC scripts (BOLT 3), the offered/received HTLC distinction, dust HTLCs, the layered (decreasing) timelocks that guarantee each hop has time to react, and the resulting **payment forwarding** state machine (`update_add_htlc`, `update_fulfill_htlc`, `update_fail_htlc`, `commitment_signed`, `revoke_and_ack`). It also notes the privacy upgrade of **PTLCs** (point timelocked contracts, enabled by Schnorr/Taproot) that replace hash correlation with point correlation.

**Resources.**

- BOLT 2 §"Adding/Removing HTLCs" and BOLT 3 §"HTLC Outputs."
- _Mastering the Lightning Network_, Ch. 8 ("Routing on a Network of Payment Channels") and the HTLC sections of Ch. 9.
- The Lightning paper §"Hashed Timelock Contracts."
- Bitcoin Optech "PTLCs" and "Point Time-Locked Contracts" topics.
- AJ Towns / ACINQ write-ups on PTLCs and the limitations of hash-based HTLCs.

**Questions.**

1. _(Foundational)_ What are the two ways an HTLC can be resolved, and what condition unlocks each?
2. _(Core)_ Why is the _same_ payment hash used at every hop along a route?
3. _(Applied)_ Walk through how the preimage propagates backward to settle every HTLC on a 3-hop path once the recipient claims.
4. _(Analytical)_ Why must the CLTV timeouts _decrease_ from sender toward recipient, and what failure occurs if an intermediary's delta is set too low?
5. _(Mastery)_ Compare HTLCs and PTLCs: how do PTLCs (via adaptor signatures on Schnorr) eliminate the payment-hash correlation that links hops, improving privacy and enabling stuckless payments?

### 4.3 — Finding Your Way

**Comprehensive explanation.** Pathfinding is the sender's problem of choosing a route that is _cheap, reliable, and likely to succeed_ given only partial knowledge — the sender knows channel _capacities_ from gossip but not the actual _balance split_ of any channel it doesn't own. This chapter covers route construction as a constrained optimization: minimize fees and CLTV risk while maximizing success probability, often modeled probabilistically (a channel of capacity C is more likely to forward amount a when a ≪ C). It introduces **multi-path payments (MPP / AMP)** that split a payment across several routes to move larger amounts than any single channel's liquidity allows, **trampoline routing** for light clients that can't hold the full graph, and the role of **failure feedback** (onion error messages) in iterative retry. It connects back to 2.1's framing: routing is a liquidity-flow problem, and the most robust approaches (Pickhardt–Richter min-cost flow) treat it as such.

**Resources.**

- _Mastering the Lightning Network_, Ch. 12 ("Path Finding and Payment Delivery").
- BOLT 4 §"Returning Errors" — onion failure messages that drive retries.
- Pickhardt & Richter, "Optimally Reliable & Cheap Payment Flows on the Lightning Network" — the definitive advanced treatment.
- BOLT proposals / Optech on MPP, AMP, and trampoline routing.
- LND/CLN/Eclair pathfinding source and docs (mission control, apriori/bimodal models).

**Questions.**

1. _(Foundational)_ What information about other channels does a sender have, and what is it missing?
2. _(Core)_ What three objectives does a good route balance?
3. _(Applied)_ How do multi-path payments let a node send more than any single channel's local balance permits?
4. _(Analytical)_ Why is success probability modeled as a function of amount relative to channel capacity, and how does failure feedback refine future attempts?
5. _(Mastery)_ Frame pathfinding as a min-cost flow problem (Pickhardt–Richter): what is the cost function, what are the constraints, and why does this outperform naive shortest-path Dijkstra approaches for large payments?

---

## 5 — The Tools of the Lightning Network

### 5.1 — Invoice, LNURL, and Keysend

**Comprehensive explanation.** This chapter covers the _payment request_ surface. A **BOLT 11 invoice** is a bech32-encoded string carrying the payment hash, amount, expiry, a description (or its hash), routing _hints_ for private channels, and a signature over it all by the recipient's node key (so the payer can recover the destination pubkey). **Keysend** (spontaneous payments) flips the normal flow: the _sender_ generates the preimage and ships it inside the onion's TLV payload so the recipient can claim without a prior invoice. **LNURL** is a set of higher-layer conventions (lnurl-pay, lnurl-withdraw, lnurl-auth, lnurl-channel) that wrap Lightning interactions in simple HTTP(S) callbacks and QR codes, enabling reusable payment links, static QR codes, and authentication. **Lightning Addresses** (`user@domain`) are a human-readable layer over lnurl-pay. The newer **BOLT 12 "offers"** improves on BOLT 11 with reusable, static, more private payment requests negotiated over the Lightning network itself.

**Resources.**

- BOLT 11 ("Invoice Protocol") and BOLT 12 ("Offers") — the spec for both invoice systems.
- _Mastering the Lightning Network_, Ch. 6 ("Lightning Payment Requests") and Ch. 15 appendix.
- LNURL specifications (`github.com/lnurl/luds`) and the Lightning Address spec (`lightningaddress.com`).
- LND `addinvoice`/`sendpayment --keysend`, CLN `invoice`/`keysend` docs.
- Bitcoin Optech "BOLT12 offers" and "Lightning Address" coverage.

**Questions.**

1. _(Foundational)_ What core fields does a BOLT 11 invoice contain, and what does its signature let the payer recover?
2. _(Core)_ How does keysend differ from a normal invoice-based payment in terms of who generates the preimage?
3. _(Applied)_ What is LNURL-pay, and how does a Lightning Address resolve to an actual invoice behind the scenes?
4. _(Analytical)_ What privacy and reusability limitations of BOLT 11 invoices does BOLT 12 (offers) address, and how?
5. _(Mastery)_ Design the end-to-end flow when a user pays a Lightning Address: the HTTP callback, the lnurl-pay response, invoice generation, and the payment — and identify the trust assumptions introduced by the domain/server.

### 5.2 — Managing Your Liquidity

**Comprehensive explanation.** Liquidity management is the operational craft of running a node. A channel's **outbound** liquidity (your local balance) lets you _send_; its **inbound** liquidity (remote balance) lets you _receive_. New nodes typically have outbound-only liquidity and must _acquire inbound_ to get paid. Techniques covered: **channel balancing** via circular **rebalancing** (paying yourself around a loop to shift liquidity), **submarine swaps / Loop** (swapping on-chain ↔ off-chain to refill or drain channels without closing them), **liquidity ads / marketplaces** (Lightning Pool, magma) to buy inbound capacity, and **splicing** (BOLT-level resizing of a channel without closing it). It also covers fee policy as a liquidity tool (raising fees on depleted directions), reserve/dust constraints, and the capital-efficiency trade-offs node operators constantly balance.

**Resources.**

- _Mastering the Lightning Network_, Ch. 9 (forwarding economics) and operational appendices.
- Lightning Labs **Loop** docs (submarine swaps) and **Pool** docs (liquidity marketplace).
- Bitcoin Optech "Splicing", "Submarine swaps", and "Liquidity advertisements" topics.
- Node-management guides: Voltage, Amboss Magma, lightningnetwork.plus (swaps/loops).
- Boltz / submarine-swap protocol docs for the cross-layer mechanics.

**Questions.**

1. _(Foundational)_ Distinguish inbound from outbound liquidity, and which one you need to _receive_ a payment.
2. _(Core)_ Why does a brand-new node usually struggle to receive payments, and what is the general remedy?
3. _(Applied)_ Explain circular rebalancing: what does paying yourself around a loop accomplish for channel balances?
4. _(Analytical)_ How does a submarine swap move liquidity between on-chain and off-chain without closing a channel, and what makes it trust-minimized?
5. _(Mastery)_ Compare splicing, swaps, and opening/closing channels as ways to adjust capacity — in terms of on-chain cost, downtime, capital efficiency, and trust — and recommend when to use each.

---

## 6 — Go Further

### 6.1 — Course Summary

**Comprehensive explanation.** The closing chapter synthesizes the whole stack and points toward the frontier. The unifying lens: **every Lightning safety property reduces to a question about pre-signed Bitcoin transactions and who can broadcast what, when.** Channels are 2-of-2 multisigs; commitments encode state; revocation punishes cheating; HTLCs make routing atomic; onion routing preserves privacy; pathfinding navigates hidden liquidity; tooling makes it usable. From here the path to mastery runs through running a node, reading the BOLTs end-to-end, and tracking active research: **Taproot channels and PTLCs** (privacy and efficiency), **BOLT 12 offers**, **splicing**, **channel factories** and **eltoo / `SIGHASH_ANYPREVOUT`** (simpler, non-punitive state updates), **trampoline routing**, and **async/offline receive**. The chapter encourages moving from theory to practice: operate a real node, force a test close on signet/regtest, and inspect the on-chain transactions to see the abstractions made concrete.

**Resources.**

- _Mastering the Lightning Network_ — full read, then the appendices on the protocol state machine.
- The complete **BOLT 1–11 (+12)** specs — the authoritative endgame reference.
- Bitcoin Optech newsletter (ongoing) — tracks eltoo, PTLCs, Taproot channels, splicing.
- Research: eltoo paper (Decker, Russell, Osuntokun), Taproot channel proposals, channel factories paper.
- Hands-on: Polar (regtest GUI), signet, LND/CLN/Eclair/LDK — run and break a node.

**Questions.**

1. _(Foundational)_ Summarize the channel lifecycle in one sentence per stage: open, update, close.
2. _(Core)_ How do revocation (intra-channel) and HTLCs (inter-channel) each provide trustlessness at their respective layers?
3. _(Applied)_ Pick one tool (invoice, swap, rebalance) and explain how it relies on the primitives from chapters 2–4.
4. _(Analytical)_ What problem does **eltoo / `SIGHASH_ANYPREVOUT`** aim to solve relative to the current penalty-based update scheme, and what is the trade-off?
5. _(Mastery)_ Make the case for how **Taproot channels + PTLCs + BOLT 12** together improve Lightning's privacy, efficiency, and UX, and identify the remaining open problems (e.g., offline receive, liquidity, watchtower trust) that research still targets.

---

## How to use this guide for mastery

Three passes per chapter. **First pass:** read the explanation and a beginner resource; answer questions 1–2. **Second pass:** read the relevant BOLT and the matching _Mastering the Lightning Network_ chapter; answer questions 3–4. **Third pass — true mastery:** spin up a regtest/signet node (Polar, LND, or CLN), reproduce the chapter's mechanism (open a channel, force a close, route a payment, trigger a penalty), inspect the resulting on-chain transactions, then answer question 5 and teach it to someone else. The single highest-leverage activity in the entire curriculum is running a node and deliberately forcing each close type while watching the blockchain — it turns every abstraction in this guide into something you have seen settle on-chain.

---

_Primary sources: the BOLT specifications (github.com/lightning/bolts), Mastering the Lightning Network (Antonopoulos, Osuntokun, Pickhardt), the Lightning Network paper (Poon–Dryja), the LND/CLN/Eclair/LDK implementation docs, and Bitcoin Optech._