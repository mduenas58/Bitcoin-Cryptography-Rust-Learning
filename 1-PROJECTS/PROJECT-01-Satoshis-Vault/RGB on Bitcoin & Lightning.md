# Exercises: RGB on Bitcoin & Lightning

Three exercises per topic, each followed by a short explanation of what the exercise is testing and the key ideas a correct answer should surface.

---

## 1. What is RGB programming in Bitcoin?

**Exercise 1.1 — Define and differentiate.** In your own words, define RGB and contrast it with an on-chain token standard such as ERC-20 on Ethereum. Focus on where state lives, who validates it, and what the base chain records.

_Explanation:_ This tests the core mental model. A good answer identifies RGB as a client-side validated, off-chain smart-contract and asset layer anchored to Bitcoin via UTXO commitments, rather than a protocol where every node re-executes every transfer. The Bitcoin base layer only sees opaque commitments, not asset data.

**Exercise 1.2 — Client-side validation.** Explain what "client-side validation" means and list two scalability properties it gives RGB that on-chain token systems do not have.

_Explanation:_ The exercise targets the principle that only the sender and receiver of a transfer need to validate the history of the asset they hold. Expected properties include: the Bitcoin chain does not grow with asset activity, and privacy improves because transfer data is never broadcast publicly.

**Exercise 1.3 — Single-use seals.** Describe the "single-use seal" abstraction and explain how a Bitcoin UTXO enforces it in RGB.

_Explanation:_ A good answer shows that an RGB seal is "closed" by spending the UTXO it is bound to, and Bitcoin's consensus guarantees a UTXO can only be spent once — giving RGB its double-spend resistance without needing its own consensus.

---

## 2. Deep Dive: How RGB's Technical Core Works

**Exercise 2.1 — Schema vs. contract.** Explain the relationship between an RGB Schema and an RGB Contract. Give one example of something defined at the schema level and one defined at the contract level.

_Explanation:_ Tests understanding that a schema is a reusable template (types, state, allowed transitions — e.g. the NIA/CFA schema for fungible assets) and a contract is a specific instance (e.g. the issuance of a specific token with its ticker, supply, and genesis state).

**Exercise 2.2 — Trace a state transition.** Walk through a transfer of an RGB asset from Alice to Bob, naming each artifact produced: state transition, witness transaction, commitment (tapret/opret), and consignment.

_Explanation:_ The learner should show that Alice builds a state transition, commits its hash into a Bitcoin witness tx that spends the seal UTXO, and hands Bob a consignment file containing the history Bob must validate client-side before accepting.

**Exercise 2.3 — Why AluVM?** Describe AluVM and explain why RGB chose a register-based, deterministic, non-Turing-complete VM instead of something like the EVM.

_Explanation:_ Expected points: determinism and bounded execution are critical when every holder must re-validate history independently; AluVM allows formal reasoning about contract behavior and avoids gas-style accounting since there is no shared global execution.

---

## 3. Lightning Network integration for RGB assets

**Exercise 3.1 — RGB state in a commitment tx.** Explain how RGB state is attached to a Lightning commitment transaction and how the channel's "two balances" are extended to cover an RGB asset.

_Explanation:_ The answer should describe that the funding output doubles as an RGB seal and each commitment tx carries a tapret/opret commitment encoding the current asset split between the two channel parties, validated client-side by both peers.

**Exercise 3.2 — HTLC vs. RGB-HTLC.** Contrast a standard BTC HTLC with an RGB-HTLC. What does the hash-locked output commit to, and what changes about settlement?

_Explanation:_ Tests the insight that the HTLC still lives in Bitcoin script (same hash/time locks), but the associated RGB state transition moves the asset amount on the preimage reveal, so the commitment carries both sat-denominated and asset-denominated balances.

**Exercise 3.3 — Routing considerations.** Discuss two liquidity or trust challenges specific to routing an RGB-asset payment across multiple Lightning hops.

_Explanation:_ Expected issues: every hop must support the same asset (asset-aware routing, not just sat-liquidity); each intermediate node must hold inbound and outbound liquidity in that specific asset; privacy of the asset ID across the route; and fee semantics when fees are paid in sats but volume is in the asset.

---

## 4. Steps to set up a Lightning node that supports RGB assets

**Exercise 4.1 — Prerequisites.** List the prerequisites for running `rgb-lightning-node` (RLN) — Bitcoin Core (`bitcoind`), an Electrum server such as `electrs`, and the Rust toolchain — and explain what each is used for.

_Explanation:_ `bitcoind` provides the base-layer node and chain data; `electrs` provides fast address/UTXO indexing the wallet layer needs; the Rust toolchain compiles RLN (which is LDK-based). The learner should tie each dependency to a concrete function of the node.

**Exercise 4.2 — First-run bring-up.** Describe the sequence to initialize an RLN node from a clean state: generating a mnemonic via `init`, unlocking the node via `unlock`, and funding the on-chain wallet. Explain what each step establishes.

_Explanation:_ Tests the operational flow — `init` creates the encrypted seed, `unlock` decrypts it into memory so the node can sign, and on-chain funding is required because opening an RGB Lightning channel still requires a Bitcoin funding transaction.

**Exercise 4.3 — Network selection trade-offs.** Configure RLN for regtest, testnet, and mainnet respectively (naming the relevant flags/config keys), and list one trade-off of each.

_Explanation:_ Expected: regtest gives instant, free blocks but is a local sandbox; testnet is public but coins are worthless and peers are sparse; mainnet is real but asset issuance and channel funds carry real cost. Candidates should map each to the corresponding `--network` / bitcoind config.

---

## 5. API commands for opening a Lightning channel with an RGB asset

**Exercise 5.1 — Issue an asset.** Write the RLN API call that issues a new NIA (Normal Inflatable Asset) with ticker `DEMO`, name `Demo Token`, precision `0`, and a supply of `1000`. Identify the field that will later be referenced as `asset_id`.

_Explanation:_ Exercises the `issueassetnia` endpoint and the fact that the returned `asset_id` (a contract ID) is what downstream calls — transfers, channel opens — must reference.

**Exercise 5.2 — Open the channel.** Construct the `openchannel` request body to open a channel to a peer `<pubkey>@<host>:<port>` carrying `100` units of the asset from Exercise 5.1, with a `capacity_sat` large enough to satisfy the dust and reserve requirements. Explain each parameter: `peer_pubkey_and_addr`, `capacity_sat`, `push_msat`, `asset_id`, `asset_amount`.

_Explanation:_ Tests familiarity with RLN's channel-open schema. Key insight: `capacity_sat` is the BTC channel capacity (sats still back the channel), while `asset_id` + `asset_amount` attach the RGB asset side; `push_msat` is optional initial sats to the counterparty.

**Exercise 5.3 — Send and verify.** After the channel is active, write the calls to (a) generate an RGB-enabled invoice on the receiving side (`lninvoice`) for `10` units of the asset, (b) pay it from the sending side (`sendpayment`), and (c) confirm the new balances on both peers (`assetbalance` / `listchannels`).

_Explanation:_ This covers the full round-trip: invoice generation with asset metadata, routed payment, and post-payment reconciliation. A good answer notes that `assetbalance` reports spendable vs. channel-locked asset balance and `listchannels` exposes per-channel asset allocation.

---

_Note:_ RGB tooling (RLN, rgb-cli, LDK integration) evolves quickly; exact flag names and endpoints should be verified against the version installed on your system before running the commands above.