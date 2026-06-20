---
title: "Overview of available applications"
source: "https://planb.academy/en/courses/3cd9cb94-82e8-417a-9c5a-02afc2589426/anatomy-of-your-bitcoin-node-b420bd9d-7e2a-4984-bc70-2b732a94c8ce"
author:
published:
created: 2026-04-22
description: "Umbrel offers an extensive application store. As you'll see, there are many tools related to Bitcoin, but also a wide variety of applications in very different fields: self-hosting solutions for servi..."
tags:
  - "clippings"
---
CourseOverviewDiplomaCredits

[Course](https://planb.academy/courses/3cd9cb94-82e8-417a-9c5a-02afc2589426/b420bd9d-7e2a-4984-bc70-2b732a94c8ce) [Overview](https://planb.academy/courses/3cd9cb94-82e8-417a-9c5a-02afc2589426/overview) [Diploma](https://planb.academy/courses/3cd9cb94-82e8-417a-9c5a-02afc2589426/retake-exam) [Credits](https://planb.academy/courses/3cd9cb94-82e8-417a-9c5a-02afc2589426/credits)

- Where are the node's data actually located?
- The blocks
- UTXO set (chainstate)
- The Mempool
- Auxiliary files and databases
- The validation path for a new block

When your node has completed its initial synchronization, it stores several complementary data sets locally, enabling it to validate blocks and transactions, serve network peers, and restart quickly while maintaining its state. 3 main bricks are essential on a node:

- the **blocks** of the blockchain stored on disk,
- the **UTXO set** maintained in a key-value database,
- and the **Mempool** is stored in RAM and periodically serialized.

Additionally, several auxiliary files (peers, fee estimates, exclusion lists, wallets, etc.) complete the picture. Let's discover the role of all these files.

### Where are the node's data actually located?

By default, Bitcoin Core saves its data in a specific working directory. Under GNU/Linux, this is usually in `~/.Bitcoin/`, under Windows in `%APPDATA%\Bitcoin/`, and under macOS in `~/Library/Application Support/Bitcoin/`. If you're using a packaged solution (e.g., within a node distribution), this directory may be mounted elsewhere, but its structure remains the same. The important sub-folders and files described below are still located here.

### The blocks

Blockchain is, therefore, a collection of blocks. A full node stores these blocks as sequential flat files and maintains a parallel index for quick retrieval. When needed (reorganization, wallet rescan, peer service), this data is re-read as is.

**Note:** A reorganization, or resynchronization, is a phenomenon in which the Blockchain undergoes a modification of its structure due to the existence of competing blocks at the same height. This happens when a portion of the blockchain is replaced by another chain with a greater amount of accumulated work. These resynchronizations are a natural part of Bitcoin's operation, where different miners can find new blocks almost simultaneously, thereby splitting the Bitcoin network in two. In such cases, the network may temporarily split into competing chains. Eventually, as one of these chains accumulates more work, the other chains are abandoned by the nodes, and their blocks become known as "obsolete blocks" or "orphan blocks." This process of replacing one chain with another is called resynchronization.

#### Blk\*.dat files (raw block data)

Received and validated blocks are written to sequential containers named `blkNNNNN.dat`, stored in the `blocks/` folder. Each file is filled in sequence until it reaches a maximum size of 128 MiB, at which point Core opens the next file. Inside, each block is serialized in network format, preceded by a magic identifier and a length. This organization enables fast writing to disk and facilitates block service to synchronize peers.

In pruned mode, the node retains only a recent window of these files to limit the disk footprint. It deletes the oldest `blk*.dat` containers as soon as the configured space target is reached, while retaining sufficient history to remain consistent with the best-known chain. The index and UTXO set remain normal, enabling the next transactions and blocks to be validated.

#### Rev\*.dat files (cancellation data)

In order to be able to go back in time during a reorganization, Core saves, in parallel with each `blk` file, a `revNNNNN.dat` file in `blocks/`. This file contains the information needed to undo the effect of a block on the UTXO set: for each output consumed by the block, the previous state of the corresponding UTXO is stored (amount, script, height...). In the event of a block abort, the node can quickly reconstitute the previous state without having to rescan the entire chain.

#### Block index (blocks/index)

Searching for a block directly in the flat files would be too time-consuming. Core therefore maintains a LevelDB database in `blocks/index/` which lists, for each known block, metadata such as Hash, height, validation status, `blk` file, and offset where it is located. When a peer requests a block, or when an internal component needs to access a specific block, this index provides quick access. Without this index, too many operations would be required.

#### Optional indexes (indexes/)

Some indexes are optional and disabled by default, as they increase the disk footprint:

- `indexes/txindex/`, which we've already mentioned, provides a transaction → location mapping table, making it possible to retrieve any confirmed transaction without knowing the block that contains it. This is useful for off-wallet `getrawtransaction` type RPC queries, but is quite expensive.
- indexes/blockfilter/\` which can contain compact block filters (BIP157/158) for thin clients. These structures accelerate client-side verification at the expense of additional storage on the indexer node.

### UTXO set (chainstate)

The UTXO (*Unspent Transaction Output*) model is the accounting representation of Bitcoin: each unspent output is an available "coin" that can be used as an input for a future transaction.

The totality of all these parts at a given moment T constitutes the UTXO set: a large list of all the parts now available. It's this state that the node consults to decide whether a transaction spends legitimate units not already used in a previous transaction (to avoid double-spending).

The UTXO set is stored in the `chainstate/` folder as a compact LevelDB database. Each part associates a key derived from the Hash of the transaction and the output index with a value containing: the amount, the `scriptPubKey` lock, the height of the creation block, and a coinbase indicator.

The node maintains a memory cache above LevelDB to absorb frequent read and write operations. The `dbcache` parameter can be used to modify the size of this cache: the larger it is, the more memory access the IBD and current validation benefit from, at the cost of higher RAM consumption. When a new block is found by a miner, the node deletes from the UTXO set the outputs spent (or consumed) by the transactions included in the block and adds the newly created outputs.

Theoretically, we could validate a transaction by rescanning the block history to check that an output has never been spent. In practice, however, this would be far too time-consuming, as the entire Blockchain would have to be scanned for each new transaction. The UTXO set, therefore, provides the minimum view required to prove locally and in a reasonable amount of time the absence of double-spending.

Note that the UTXO set is often at the heart of concerns about Bitcoin's decentralization, as its size naturally increases rapidly. This is partly due to the rising price of Bitcoin, which encourages fragmentation of parts, and partly to the growing adoption of the system: the more users there are, the greater the demand for UTXOs.

The growth of the UTXO set also stems from the structure of simple payment transactions on Bitcoin. Indeed, when you make a payment, you consume a single UTXO as input and create two new UTXOs as output (one for the payment and the other for the change that comes back to the payer). Finally, a chain analysis heuristic, called CIOH (*Common Input Ownership Heuristic*), provides a further incentive to avoid coin consolidation.

Since a portion of it must be kept in RAM to verify transactions in a reasonable time, the UTXO set may gradually render the operation of a full node too costly. To solve this problem, a few proposals already exist, notably Utreexo.

### The Mempool

The mempool is the local set of valid transactions that have been received but not yet confirmed. As a reminder, a "confirmed transaction" is one that has been included in a valid block. Each node maintains its own Mempool, which may differ from that of other nodes in the network depending on:

- the size allocated to the Mempool via the `maxmempool` parameter: a node with a larger Mempool will be able to hold more transactions than a node with a smaller Mempool (unless the latter becomes empty);
- mempool rules: they form a subset of the node’s relay rules and define the characteristics that an unconfirmed transaction must meet to be accepted into the mempool;
- transaction percolation: due to various factors, a given transaction may have been distributed to one part of the network, but not yet reached another.

It is important to note that node mempools have no consensus value. Bitcoin works perfectly even if each node has a different Mempool. Ultimately, the authoritative blocks are always those added to the Blockchain. For example, even if a node initially rejects a given transaction in its Mempool (valid according to the consensus rules), it will be obliged to accept it if it is eventually included in a block with a valid proof of work. If it failed to do so and rejected this block, even though it complied with the consensus rules, it would trigger a Hard Fork, i.e., the creation of a new, separate Bitcoin on which it would be alone.

#### Memory policy and management

When a transaction is received, Core applies a series of checks against consensus rules (syntax, valid scripts, no double spending, etc.) and Mempool rules, which are a local policy (RBF, minimum charge thresholds, data limit in `OP_RETURN`, etc.). If the transaction adheres to these rules, it is stored in memory.

The size of the Mempool is limited by the `maxmempool` parameter in the `Bitcoin.conf` file (more on this in the next chapter). By default, the limit is 300 MB. When it's full, the node dynamically raises its minimum charge threshold and expels the least profitable transactions first (i.e., it retains transactions that should be mined first). Transactions that are too old can also expire after a configured delay.

#### Mempool persistence on disk

To speed up restarts, Core periodically serializes the state of the Mempool in the `Mempool.dat` file when the node is shut down. In addition to the actual Mempool, which remains in memory, Core stores this `Mempool.dat` file on disk. The next time the node is launched, it reloads this snapshot and deletes anything that is no longer valid for the current Blockchain.

### Auxiliary files and databases

Several other files at the same level as `blocks/`, `chainstate/`, and `indexes/` participate in the proper functioning of the:

- `peers.dat` keeps an IP address book of potential peers, fed by initial DNS discovery, network exchanges, and manual additions. When the node starts up, it can draw on this file to establish outgoing connections.
- When the node is switched off, `anchors.dat` saves the addresses of outgoing peers, so that you can try to contact them again quickly the next time you start up.
- `banlist.json` contains local bans decided by the operator or by the node (repeated invalid behavior), in order to prevent the node from reconnecting or accepting connections from these specific peers.
- `fee_estimates.dat` stores time horizon statistics on observed confirmations, used by the fee estimator to propose fee rates consistent with the delay objectives chosen when creating a transaction.
- `bitcoin.conf` contains your node’s configuration parameters. It is in this file that the relay rules can be adjusted. I will discuss this in more detail in the next chapter;
- `settings.json` contains additional parameters to `Bitcoin.conf`.
- `debug.log` is the diagnostic text log, which can be used to understand node activity in the event of a bug.
- `bitcoind.pid` records the process ID during execution, allowing other applications or scripts to easily identify Bitcoind (*Bitcoin Daemon*) and interact with it if necessary. It is created when the node starts and deleted when it stops;
- `ip_asn.map` is an IP → ASN mapping table (standalone system) used for bucketing and peer diversification (`-asmap` option).
- `onion_v3_private_key` stores the private key of the Tor v3 service when the `-listenonion` option is enabled, in order to keep a stable onion address between reboots.
- `i2p_private_key` stores the I2P private key when `-i2psam=` is used, to make outgoing and possibly incoming connections on I2P.
- `.cookie` contains an ephemeral RPC authentication token (created at startup, deleted at shutdown) when cookie authentication is used. This can be used, for example, to connect wallet software.
- `.lock` is the data directory lock, which prevents multiple instances from writing to the same datadir simultaneously.
- `guisettings.ini.bak` is the automatic saving of GUI settings (*Bitcoin Qt*) when the `-resetguisettings` option is used.

As we saw in the first parts of this BTC 202 course, Bitcoin Core is both Bitcoin node software and wallet. However, it's not necessarily the solution I'd recommend for managing your wallets, as its Interface remains basic and its functionalities are limited compared with modern software such as Sparrow or Liana. Core also includes files for managing your wallets:

- `wallets/` is the default directory that hosts one or more wallets;
- `wallets/<name>/wallet.dat` is the SQLite database of the wallet (keys, descriptors, transaction metadata, etc.);
- `wallets/<name>/wallet.dat-journal` is the SQLite rollback journal.

To summarize, here is the Bitcoin Core file structure:

```
~/.bitcoin/
├── bitcoin.conf
├── blocks/
│   ├── blk00000.dat
│   ├── blk00001.dat
│   ├── rev00000.dat
│   ├── rev00001.dat
│   └── index/
├── chainstate/
├── indexes/
│   ├── txindex/
│   ├── blockfilter/
│   │   └── basic/
│   │       ├── db/
│   │       └── fltrNNNNN.dat
│   └── coinstats/
│       └── db/
├── wallets/
│   └── <wallet_name>/
│       ├── wallet.dat
│       └── wallet.dat-journal
├── peers.dat
├── anchors.dat
├── banlist.json
├── mempool.dat
├── fee_estimates.dat
├── bitcoind.pid
├── debug.log
├── ip_asn.map
├── onion_v3_private_key
├── i2p_private_key
├── settings.json
├── guisettings.ini.bak
├── .cookie
└── .lock
```

### The validation path for a new block

On receipt of a new block, your node checks the proof of work and, more generally, compliance with the consensus rules. If all is well, it applies the changes transaction by transaction to its UTXO set: it checks that each entry spends existing UTXOs with a valid script, deletes these UTXOs, and adds the new exits. If everything is valid, the changes are committed to `chainstate/`.

In parallel, undo data is written to `rev*.dat` and metadata to the `blocks/index/` index. The block is then serialized to the correct `blk*.dat` file. In the event of a reorganization, the node reads `rev*.dat` in reverse to cleanly disconnect the abandoned blocks, restore the UTXO set, and then connect the blocks of the new best chain.

Quiz

Quiz

btc2025.3

What is the maximum size of a blkNNNNN.dat file before a new file is created?