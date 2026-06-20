---
title: "Overview of available applications"
source: "https://planb.academy/en/courses/3cd9cb94-82e8-417a-9c5a-02afc2589426/understanding-ibd-and-the-peer-discovery-process-175ac9d1-ea23-45d9-9918-d3e7352435cd"
author:
published:
created: 2026-04-21
description: "Umbrel offers an extensive application store. As you'll see, there are many tools related to Bitcoin, but also a wide variety of applications in very different fields: self-hosting solutions for servi..."
tags:
  - "clippings"
---
CourseOverviewDiplomaCredits

[Course](https://planb.academy/courses/3cd9cb94-82e8-417a-9c5a-02afc2589426/175ac9d1-ea23-45d9-9918-d3e7352435cd) [Overview](https://planb.academy/courses/3cd9cb94-82e8-417a-9c5a-02afc2589426/overview) [Diploma](https://planb.academy/courses/3cd9cb94-82e8-417a-9c5a-02afc2589426/retake-exam) [Credits](https://planb.academy/courses/3cd9cb94-82e8-417a-9c5a-02afc2589426/credits)

- IBD milestones
- AssumeValid
- AssumeUTXO
- Peer discovery: How does your node find the Bitcoin network?

Your Bitcoin node starts up without any prior knowledge of transaction history. Initially, it's just a computer running software (Bitcoin Core or similar). To become a fully synchronized and operational Bitcoin node, it must locally reconstruct the state of the ledger by checking all blocks published since the Genesis block (block 0, published by Satoshi Nakamoto on January 3, 2009). This step is called **IBD (*Initial Block Download*)**.

IBD consists of downloading and verifying each block and transaction individually, applying the consensus rules, to build its own version of the Blockchain. The aim is not simply to retrieve a copy of unverified data, but to arrive at the same conclusion completely independently, as the honest majority of the network.

### IBD milestones

Synchronization begins with the ***headers-first*** step. Your node requests the sequence of block headers from several peers and, for each of them, verifies proof of work, difficulty adjustment, syntax, as well as timestamp and version number rules. In short, it ensures that each header received complies with the consensus rules.

As a reminder, a Bitcoin block consists of an 80-byte header and a list of transactions. The block's fingerprint is obtained by applying a double SHA-256 hash to this header, which contains 6 fields:

- version
- hash of previous block
- Merkle root of transactions
- timestamp (greater than the median time of the previous 11 blocks)
- difficulty target
- Nonce

Transactions are committed to a Merkle tree. This is a structure that summarizes a large set of data (in this case, all the transactions in the block) by aggregating their hashes progressively two by two down to a single "root", thus proving that an element belongs to the set (and detecting any modification). In this way, any modification to a transaction also modifies the root of the Merkle tree and therefore the block header's fingerprint. SegWit has introduced a separate additional commitment for the witness (signatures), placed in the coinbase.

This ***headers-first*** step enables the node to identify the branch with the most work (regardless of its number of blocks), which is the branch on which Bitcoin nodes synchronize. Once this branch has been identified, the node downloads the contents of the blocks in parallel from several connections, then validates each transaction: format, validity of scripts (except `assumevalid=1`), amounts, and absence of double spending. With each successful check, the current state of unspent coins (UTXO set) is updated in the `chainstate/` database: spent outputs are removed, while new valid outputs are added.

Mempool, on the other hand, only comes into play when approaching the tip of the chain: as long as the node remains late, it has no pending transactions to store.

Once the IBD is complete, the node enters its normal phase: it validates new blocks as they are published, maintains its Mempool with pending transactions according to its relay rules, relays transactions and blocks, and manages any chain reorganizations.

### AssumeValid

Bitcoin Core incorporates a mechanism designed to reduce the time needed before a node is fully operational, while retaining the essence of the autonomous verification principle: AssumeValid.

The `assumevalid` parameter is based on a past reference block, the hash of which is integrated into each software version. During IBD, if your node finds that this block is indeed on the branch with the most work, it can ignore script verification for all transactions prior to this point.

All other rules (block structure, proof of work, size limits, transaction amounts, UTXOs, etc.) remain fully verified. Only the calculation of scripts prior to this reference block is ignored. The performance gain is significant on the IBD, as signature verification accounts for a major portion of the CPU load. Beyond this reference block, verification returns to its normal state.

You can force full validation of all scripts by disabling this mechanism, at the cost of a much longer IBD, using the `assumevalid=0` parameter in the `Bitcoin.conf` file.

### AssumeUTXO

`assumeutxo` is another existing parameter, but unlike `assumevalid`, it is not activated by default. This mechanism enables the software to load a snapshot of the UTXO set, along with its metadata, and provisionally consider it as a reference state, after verifying that the headers indeed lead to the Blockchain with the most work.

The node thus quickly becomes operational for common uses (RPC, connecting wallets, etc.), while simultaneously launching the complete, verified reconstruction of its own UTXO set in the background. Once this stage is complete, the initial snapshot is replaced by the locally reconstructed state. This approach separates fast node provision from full verification, without compromising the latter.

### Peer discovery: How does your node find the Bitcoin network?

When a node starts up for the first time, it doesn't yet know any peers. However, it must find other Bitcoin nodes on the Internet to request headers, then blocks, in order to complete its IBD. To initiate these connections, Bitcoin Core follows a prioritized logic.

When the node restarts after having already been used, Core first attempts to reconnect to outgoing peers registered before the shutdown, information stored in the `anchors.dat` file. Then, it consults its IP address book **`peers.dat`**, which stores the list of previously encountered peers, in order to reconnect to them. This is simply a local file, updated and kept by Core. On the other hand, for a new node that has just been launched, these 2 files are empty, since it has never yet communicated with other Bitcoin nodes.

In this case, the software queries ***DNS seeds***. These are [servers maintained by recognized ecosystem developers](https://github.com/Bitcoin/Bitcoin/blob/master/src/kernel/chainparams.cpp), which return a list of IP addresses of presumed active nodes. These addresses enable the new node to initiate its first connections and request the necessary data from the IBD. Here is the list of *DNS seeds* active to date (August 2025):

- Pieter Wuille: `seed.Bitcoin.sipa.be.`
- Matt Corallo: `dnsseed.bluematt.me.`
- Luke Dashjr: `dnsseed.Bitcoin.dashjr-list-of-P2P-nodes.us.`
- Jonas Schnelli: `seed.Bitcoin.jonasschnelli.ch.`
- Peter Todd: `seed.btc.petertodd.net.`
- Sjors Provoost: `seed.Bitcoin.sprovoost.nl.`
- Stephan Oeste: `dnsseed.emzy.de.`
- Jason Maurice: `seed.Bitcoin.wiz.biz.`
- Ava Chow: `seed.Mainnet.achownodes.xyz.`

In the vast majority of cases, the *DNS seeds* step is sufficient to establish the first connections with other nodes. If, exceptionally, these servers fail to respond within 60 seconds, the node switches to another method: [a static list of over 1,000 addresses](https://github.com/Bitcoin/Bitcoin/blob/master/src/chainparamsseeds.h) of *seed nodes* is built into Bitcoin Core's code and regularly updated. If the first two methods of obtaining IP addresses fail, this last solution establishes an initial connection, from which the node can then request new IP addresses.

As a last resort, you can manually supply IP addresses via the `peers.dat` file to force specific connections.

Once bootstrapped, the internal address manager diversifies the sources (separate autonomous networks, clearnet, and Tor, as well as various geographical areas) to reduce the risk of topological isolation. The node establishes these outgoing connections (connections it selects itself, and which are therefore more secure).

If your node is listening on an open port (by default, 8333), it accepts incoming connections. These reinforce the overall resilience of the network by providing a point of contact for new nodes, without bringing any particular benefit to your own IBD. If your node runs on Tor, the logic remains the same, but the addresses used are `.onion` services.

Quiz

Quiz

btc2025.2

What mechanism can be used to load a snapshot of the UTXO set to make a node quickly usable?