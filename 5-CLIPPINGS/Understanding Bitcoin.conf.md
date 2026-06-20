---
title: "Overview of available applications"
source: "https://planb.academy/en/courses/3cd9cb94-82e8-417a-9c5a-02afc2589426/understanding-bitcoinconf-c54a629a-ddb1-41cb-9a88-21dfd9be50ca"
author:
published:
created: 2026-04-23
description: "Umbrel offers an extensive application store. As you'll see, there are many tools related to Bitcoin, but also a wide variety of applications in very different fields: self-hosting solutions for servi..."
tags:
  - "clippings"
---
CourseOverviewDiplomaCredits

[Course](https://planb.academy/courses/3cd9cb94-82e8-417a-9c5a-02afc2589426/b420bd9d-7e2a-4984-bc70-2b732a94c8ce) [Overview](https://planb.academy/courses/3cd9cb94-82e8-417a-9c5a-02afc2589426/overview) [Diploma](https://planb.academy/courses/3cd9cb94-82e8-417a-9c5a-02afc2589426/retake-exam) [Credits](https://planb.academy/courses/3cd9cb94-82e8-417a-9c5a-02afc2589426/credits)

The `Bitcoin.conf` file is the main Interface configuration file for Bitcoin Core. It allows you to adjust the behavior and parameters of your node without having to recompile its source code or make command-line modifications. In concrete terms, it's a plain text file structured in key-value pairs, meaning that each line of the file references a specific parameter (the key) and its associated value, which can be modified to adjust that parameter.

Network, transaction relay, performance, indexing, logging, and RPC access parameters can be defined in the `Bitcoin.conf`. However, this configuration file never modifies the protocol's consensus rules: it only sets the node's local policy (relaying rules), the way it connects, indexes, and exposes services.

### Location and priority

By default, `Bitcoin.conf` resides in the Bitcoin Core data directory. This is the famous directory we mentioned in the previous chapter. However, this file is not automatically created by Bitcoin Core, except in certain environments, such as Umbrel. If it doesn't already exist, you'll have to generate it yourself by simply creating a file named `Bitcoin.conf`, then opening it in a text editor to make your modifications.

The parameters defined in the `Bitcoin.conf` can be overridden by 2 layers:

- `settings.json` (written dynamically by Interface graphics or some RPC),
- and options modified via command lines.

Note that any modification to `Bitcoin.conf` requires a node restart to take effect.

### Format and structure

The format of the `Bitcoin.conf` is therefore very simple: one line per option, in the form `option=value`. Unnecessary spaces and blank lines are ignored, and code comments begin with `#`.

Almost all Boolean options can be disabled with a `no` prefix. For example, `listen=0` and `nolisten=1` are equivalent depending on the version.

To segment the configuration by network, you can use sections: `[main]`, `[test]` (testnet3), `[testnet4]`, `[bookmark]`, `[regtest]`. Alternatively, you can prefix the option name with `regtest.maxmempool=100`.

### What Bitcoin.conf can and cannot do

As explained above, consensus rules are obviously not configurable in `Bitcoin.conf`, as this could create a Hard Fork. On the other hand, many other aspects are configurable. There are 3 useful classes to keep in mind:

- Purely local parameters. These affect only your node: cache size (`dbcache`), pruned mode (`prune`), optional indexes... They influence your machine's performance, but not the network.
- Relay and Mempool policies. These decide what your node accepts, retains, and relays before confirmation: minimum fee threshold (`minrelaytxfee`), Mempool size and retention time (`maxmempool`, `mempoolexpiry`), transaction replacement (RBF)... These rules are not part of the consensus, so two different nodes can have different policies and still be fully compatible. On the other hand, these parameters will have an influence on the Bitcoin network (as explained in the first part, notably with percolation theory).
- Network connectivity. These options determine how your node finds peers, listens, traverses a NAT, uses Tor or a proxy, or limits its bandwidth. They shape your topology, but do not alter the relaying of transactions.

Understanding this separation is crucial: if a transaction doesn't adhere to the consensus rules, your node will reject it in any case. But a stricter local policy may refuse to relay a transaction that is valid in the consensus sense.

### Network and topology

First of all, it's important to clearly distinguish between the 2 types of connection a Bitcoin node can have:

- Outgoing connections, which are initiated by our node to another node;
- Incoming connections, initiated by another node to ours.

These two types of connection are perfectly capable of exchanging the same data in both directions; it's not a question of limiting the direction of flow, but only of a difference in the initiator of the connection. From our node's point of view, outgoing connections are generally considered safer, since we initiate them and choose precisely which node to connect to, making it unlikely that the connection is malicious. By default, Bitcoin Core maintains 10 outgoing connections (8 " *full-relay* " + 2 " *block-relay-only* ").

A full node adds more value to the network by accepting incoming connections. The `listen=1` parameter enables listening on the default port 8333 of the network in question, enabling these incoming connections to be received on the clearnet. For this to work, this port must also be open on your router. If it isn't, your node will continue to work with outgoing connections only, which will have no impact on your personal use of Bitcoin. The choice of whether to allow incoming connections is yours; there is no "best choice."

If you prefer not to open a port on your router, but still accept incoming connections, you can activate the `listenonion=1` parameter. This will achieve the same result, but only through the Tor network rather than clearnet.

On the network level, we also have:

- `addnode`: adds a friendly peer to contact in addition to the usual discovery (can be specified several times).
- `connect`: strictly restricts connections to the provided address (can be specified multiple times). Core will not connect to any other node;
- `seednode`: is used only to fill in the book-address when connecting to a node, then disconnects.
- `maxconnections`: defines the global ceiling for incoming + outgoing connections. By default, this parameter is set to 125, meaning that your node will never accept more than 125 connections.
- `maxuploadtarget`: caps the upload to limit bandwidth over a rolling 24-hour window. This cap does not sacrifice the propagation of essential recent elements;
- `onlynet`: limits outgoing connections to selected networks only (`ipv4`, `ipv6`, `onion`, `i2p`, `cjdns`). For example, if you want your node to connect to the Bitcoin network only via Tor, you can enable the `onlynet=onion` parameter and disable incoming connections (or only allow connections via Tor as well).
- `dnsseed`: allows or disallows *DNS seeds* to request peers when your local address pool is low (default: `1`, unless `-connect` or `-maxconnections=0`).
- `forcednsseed`: forces *DNS seeds* to be requested at startup, even if you already have addresses in stock (default: `0`).
- `fixedseeds`: Allow use of *seed nodes* (hardcoded address list) if *DNS seeds* fail or are disabled (default: `1`).
- `dns`: Authorizes DNS resolutions in general (e.g., for `-addnode` / `-seednode` / `-connect`).

By default, your node communicates over clearnet, Tor, and I2P. This means that the peers it connects with on the clearnet can see your public IP address, and your ISP will likely be able to detect that you're running a Bitcoin node (although P2P Transport V2 makes it more difficult for an ISP to eavesdrop). This isn't necessarily a problem, but if you want to avoid any leakage of this information, you can connect your node exclusively via the Tor network.

To be fully Tor-enabled, you need to force Bitcoin Core to use only this network and to create a hidden service for incoming connections (if you want to enable them). In the `Bitcoin.conf`, you need to add this configuration:

- `onlynet=onion`,
- `proxy=127.0.0.1:9050`,
- `listenonion=1`,
- `torcontrol=127.0.0.1:9051`,
- `proxyrandomize=1`,
- `listen=1`,
- `bind=127.0.0.1`,
- `upnp=0`,
- `natpmp=0`.

All your P2P connections go through Tor. Your node receives a `.onion` address for incoming connections, so no ports need to be opened on the router. Your ISP only sees Tor traffic, and your peers are unaware of your actual public IP address.

To avoid DNS resolution in the clear, you can add `dnsseed=0` and `dns=0` to your configuration. You'll then need to manually provide `.onion` peers via `seednode=` or `addnode=`, as discovery of new nodes will be difficult otherwise.

Obviously, if you're a beginner, I'd advise you to leave all these network settings alone for the time being. The default configuration is often sufficient.

### Mempool and relay policy

#### Basic parameters

Here are the basic parameters you can modify on your `Bitcoin.conf` concerning the management of your Mempool and the relaying of unconfirmed transactions:

- `maxmempool=<n>`: Limits the maximum size of the local Mempool to `<n>` megabytes (default: `300`). When the limit is reached, your node dynamically raises its effective fee threshold and prioritizes the least profitable transactions (based on the fee rate, not the absolute value) to stay below the limit. You can leave this setting as the default. Increasing it can be useful if you're mining solo, or if you want to get a more accurate view of mempool congestion and improve fee estimation. Conversely, reducing it will save RAM and, to a lesser extent, other system resources.
- `mempoolexpiry=<n>`: Maximum retention time for unconfirmed transactions in Mempool (in hours, default: `336`). After this time, transactions are removed even if space remains available.
- `persistmempool=1`: Saves a snapshot of the Mempool at standstill and reloads it on reboot (default: `1`). This speeds up recovery after reboot, avoiding the need to relearn the state via the network.
- `maxorphantx=<n>`: Maximum number of orphan transactions retained (dependent inputs from UTXOs not yet seen in the UTXO set, default: `100`). Beyond this threshold, the oldest transactions are deleted to avoid uncontrolled growth of the cache.
- `blocksonly=1`: Disables the acceptance and relay of unconfirmed transactions received from peers (except for special permissions). The node only downloads and announces blocks. Locally created transactions can still be broadcast (to use your node with your wallet software). This greatly reduces bandwidth and RAM requirements at the cost of reduced relay usefulness and total unawareness of the mempool.
- `minrelaytxfee=<n>`: Minimum fee rate (in BTC/kvB) below which transactions are not accepted in the node's Mempool and not relayed to peers (default: `0.00001` = 1 sat/vB). The higher this value, the more aggressively your node filters low-cost transactions.
- `mempoolfullrbf=1`: Accept RBF transactions even without explicit RBF signaling in the replaced transaction. With this " *full-RBF* " policy, a transaction offering a higher fee rate can replace another in Mempool if the other replacement conditions are met.

As a reminder, RBF is a transactional mechanism that enables the sender to replace a transaction with one that has higher fees in order to speed up confirmation. If a transaction with too low a fee remains blocked, the sender can use *Replace-by-fee* to increase the fee and prioritize their replacement transaction in mempools and with miners.

#### Advanced and specific settings

Here are the advanced settings for Mempool and relay policy. If you're a beginner, you shouldn't need to modify these settings:

- `datacarrier=1`: Allows the relay and (if mining via the node) inclusion of transactions carrying non-financial data via an `OP_RETURN` output (default: `1`). Disabling this parameter slightly reduces the surface for non-financial data spam at the cost of lower compatibility with certain uses. In all cases, you must accept mined `OP_RETURN`.
- `datacarriersize=<n>`: Maximum size (in bytes) of the `OP_RETURN` that the node relays (default: `83`). Lowering this value restricts the payloads transported via `OP_RETURN`. Note that this limit will be removed by default in a future version of Bitcoin Core.
- `bytespersigop=<n>`: Parameter which converts signature transactions into equivalent bytes for relay limit evaluation (default: `20`). This will influence the acceptance of `sigops` rich transactions according to local policy rules.
- `permitbaremultisig=1`: Allows relaying of *bare-Multisig* P2MS transactions (default: `1`). This is the oldest script template for establishing multisignature conditions on a UTXO (invented in 2011 by Gavin Andresen).
- `whitelistrelay=1`: Automatically grants relay permission to whitelisted incoming peers (default: `1`). These peers have their transactions accepted by the relay even if your node is not in general relay mode.
- `whitelistforcerelay=1`: Assigns " *forcerelay* " permission to whitelisted peers with default permissions (default: `0`). The node then relays their transactions even if they are already present in Mempool, thus bypassing anti-redundancy mechanisms.
- `whitebind=<[permissions@]addr>` / `whitelist=<[permissions@]CIDR>`: Binds an Interface or address range and assigns fine-grained permissions to the corresponding peers: `relay`, `forcerelay`, `Mempool` (Mempool content request), `noban`, `download`, `addr`, `bloomfilter`. This can be useful for granting privileged treatment to trusted peers (such as gateways, LANs, and internal services).
- `peerbloomfilters=1`: Enables support for Bloom filters (BIP37) to serve filtered blocks/transactions to lightweight clients (default: `0`). Note that this increases the load on your resources.
- `peerblockfilters=1`: Serves compact BIP157 (*Neutrino*) filters to peers (default: `0`).
- `blockreconstructionextratxn=<n>`: Additional number of transactions retained in memory to rebuild compact blocks (default: `100`). Improves the success of reconstructions during compact synchronizations, at the cost of a little memory.

As a reminder, all these relay rules have no impact on the validity of transactions included in a valid block. They serve to adjust your contribution to the relay, protect your resources, and make your node predictable in constrained environments, but never allow you to refuse blocks that respect the consensus rules.

### wallets

You can also adjust the way your wallets are managed in the `Bitcoin.conf` file. If you're not using wallet directly in Core, but rather external management software such as Sparrow or Liana, these parameters will be of little importance:

- `addresstype=<legacy|p2sh-segwit|bech32|bech32m>`: Defines the format of addresses generated by the wallet for receiving.
- `changetype=<legacy|P2SH-SegWit|bech32|bech32m>`: Force change address format (remainder of an input on a single payment).
- `wallet=<path>`: Loads an existing wallet at startup (can be repeated to load multiple wallets).
- `walletdir=<dir>`: Directory containing wallets (default: `<datadir>/wallets` if it exists, otherwise `<datadir>`). This can be useful if you wish to store wallets on a dedicated or encrypted volume.
- `walletbroadcast=1`: Automatically broadcasts transactions created by loaded wallets (default: `1`). Set to `0` if you wish to manage broadcasting via another channel.
- `walletrbf=1`: Enables RBF opt-in to signal RBF on all transactions (default: `1`). Allows you to increase fees later in the event of a blocked transaction.
- `txconfirmtarget=<n>`: Confirmation target for the transaction (in number of blocks, default: `6`). The wallet will automatically set the fee for the transaction to be confirmed within this number of blocks.
- `paytxfee=<amt>`: Fixed fee rate (BTC/kvB) applied to wallet transactions. Avoid in general: use adaptive estimation via `txconfirmtarget`.
- `fallbackfee=<amt>`: Fallback fee rate (BTC/kvB) used if the estimator lacks data (default: `0.00`). Setting it to 0 completely disables the fallback.
- `mintxfee=<amt>`: Minimum threshold (BTC/kvB) for wallet to create transactions (default: `0.00001`). Wallet will refuse to build a transaction below this threshold.
- `maxtxfee=<amt>`: Absolute cap on total fees for a wallet transaction (default: `0.10` BTC). Protects against abnormally high fees that would unnecessarily destroy bitcoins.
- `avoidpartialspends=1`: Selects UTXOs by address clusters to avoid partial spending.
- `spendzeroconfchange=1`: Allows an unconfirmed change UTXO to be reused as an entry in a new transaction (default: `1`).
- `consolidatefeerate=<amt>`: Maximum rate (BTC/kvB) beyond which wallet avoids adding more inputs than necessary to consolidate. This allows consolidations of small UTXO into larger ones at low prices, and reduces costs when costs are high.
- `maxapsfee=<n>`: Budget for additional charges (BTC, absolute value) that the wallet agrees to pay to activate the " *avoid partial spends* " option.
- `discardfee=<amt>`: Rate (BTC/kvB) indicating your tolerance to throw away the change by adding it to the fee. Outputs that would cost more than a third of their value at this rate are dropped.
- `keypool=<n>`: Size of pre-generated address pool (default: `1000`). Values that are too small increase the risk of incomplete restores.
- `disablewallet=1`: Starts Bitcoin Core without the wallet subsystem and disables associated RPCs. Reduces the attack surface and footprint if the node is only used for validation/release.

### Storage, indexing, and performance

The configuration file also allows you to adjust the parameters related to your machine. This can be particularly relevant if you have limited resources, or, on the contrary, a large amount of available capacity:

- `datadir=<dir>`: Sets Bitcoin Core's main data directory.
- `blocksdir=<dir>`: Decouples the location of the blocks files (`blocks/blk*.dat` and `blocks/rev*.dat`) from the `datadir`. This can be useful for placing the blocks archive on a different volume, while keeping the state base (`chainstate/`) on a faster medium, for example.
- `dbcache=<n>`: Allocates `<n>` MiB to the database cache (*LevelDB*) used by the block index and `chainstate` (default: `450`). The higher the value, the faster the IBD and current validation, at the cost of higher RAM consumption.
- `prune=<n>`: Enables pruning of block files and sets a disk space target in MiB (default: `0` = disabled; `1` = manual pruning via RPC; `>=550` = automatic pruning below target). Incompatible with `txindex=1`. The node remains a fully validating node, but can no longer provide the old history. This option is particularly useful if your disk space is limited, for example, when installing a node on your home computer.
- `txindex=1`: Builds and maintains a global index of confirmed transactions. Essential for certain queries (`getrawtransaction` outside the wallet) and for exploration purposes, but significantly increases disk usage. Incompatible with pruned mode.
- `assumevalid=<hex>`: Indicates a block that is assumed to be valid, allowing you to skip script checks for its ancestors (set `0` to check everything). See the previous chapter for more information.
- `reindex=1`: Reconstructs block indexes and state (`chainstate`) from `blk*.dat` files on disk. Also rebuilds optional active indexes. This is a time-consuming operation to use to repair a corrupted database or cleanly activate/deactivate heavy indexes.
- `reindex-chainstate=1`: Rebuilds only the `chainstate` from the current block index. Preferred when block files are healthy.
- `blockfilterindex=<type>`: Maintains indexes of compact block filters (e.g., `basic`) used by thin clients (BIP157/158) and some RPCs. Disabled by default (`0`). Consumes additional disk space and indexing time.
- `coinstatsindex=1`: Maintains a UTXO set statistics index operated by the `gettxoutsetinfo` call. Useful for audits and metrics, eliminating the need for costly recalculation. Disabled by default.
- `loadblock=<file>`: Imports blocks at startup from an external `blk*.dat` file. Used to preload history from an offline source (local copy, external media) to speed up initialization.
- `par=<n>`: Sets the number of script verification threads (from `-10` to `15`, `0` = auto, `<0` = leaves this number of cores free). Allows you to adjust CPU parallelism during validation. Auto mode is suitable in most cases.
- `debuglogfile=<file>`: Specifies the location of the `debug.log` log.
- `shrinkdebugfile=1`: Reduces the size of `debug.log` at startup (default: `1` when `-debug` is not active).
- `settings=<file>`: Path to dynamic settings file `settings.json`.

### RPC access and operational safety

Finally, the `Bitcoin.conf` file also allows you to configure the access parameters for your node. Be cautious with these settings, especially if you're just starting out: avoid changing them without a thorough understanding of the implications, as this could introduce vulnerabilities.

- `server=1`: Activates the JSON-RPC server. Essential if you're driving `bitcoind` via `bitcoin-cli` or a third-party application. Disable (`0`) on a purely validating node that doesn't expose any API, or already uses an Electrum server.
- `rpcbind=<addr>[:port]`: RPC server listening address/port. By default, listening is done locally only (`127.0.0.1` and `::1`). This parameter is ignored if `rpcallowip` is not also defined. Use it to explicitly restrict Interface.
- `rpcport=<port>`: RPC port (default: `8332` on Mainnet, `18332` on Testnet, `38332` on bookmark, `18443` on regtest).
- `rpcallowip=<ip|cidr>`: Allows RPC clients from a given IP or subnet (can be repeated). Use in conjunction with `rpcbind` to expose the API only to a trusted segment (LAN/VPN).
- `rpcauth=<USERNAME>:<SALT>$<Hash>`: Recommended RPC authentication method (hashed password). Allows multiple entries and avoids storing a secret in clear text.
- `rpccookiefile=<path>`: Path to authentication cookie (default: `.cookie` file under `datadir/`). This is used for local access by the same user without managing persistent passwords. For example, you can use it to connect the Liana wallet to your Bitcoin Core on the same machine.
- `rpcuser=<user>` / `rpcpassword=<pw>`: Classic RPC authentication with plaintext password. Avoid using this in favor of `rpcauth` or a cookie.
- `rpcthreads=<n>`: Number of threads to serve RPC calls (default: `4`). Increase it if you have high call peaks on the monitoring/external tool side.
- `rpcwhitelist=<USERNAME>:<rpc1>,<rpc2>,...`: Whitelist of authorized APIs. Reduces the attack surface by restricting accessible methods.
- `rpcwhitelistdefault=1|0`: Default whitelist behavior: if enabled and a whitelist is used, unlisted calls are refused. This can also force a default empty set (no calls allowed) as long as nothing is explicitly listed.
- `rest=1`: Enable public REST API (disabled by default). To be exposed only on a trusted network (same caution as with JSON-RPC).
- `conf=<file>`: Specifies, on the command line only, a read-only configuration file. Useful for freezing an execution profile (immutable) on the ops side.
- `includeconf=<file>`: Loads an additional configuration file (path relative to `datadir/`). Allows separation of roles: common base + sensitive local overload.
- `daemon=1` / `daemonwait=1`: Starts `bitcoind` in the background and, with `daemonwait`, waits for initialization to finish before handing over. This facilitates integration with supervisors (systemd, runit).
- `pid=<file>`: Location of PID file.
- `sandbox=<log-and-abort|abort>`: Enables experimental syscalls sandboxing: only expected syscalls are allowed.
- `startupnotify=<cmd>` / `shutdownnotify=<cmd>`: Executes a command at startup or shutdown.
- `alertnotify=<cmd>`: Triggers a command on receipt of an alert.
- `blocknotify=<cmd>`: Executes a command for each new block.
- `debug=<category>|1` / `debugexclude=<category>`: Enables/disables detailed log categories (e.g. `net`, `Mempool`, `RPC`, `validation`...).
- `logips=1`: Logs IP addresses.
- `logsourcelocations=1` / `logthreadnames=1` / `logtimestamps=1`: Adds source locations, thread names, and precise timestamps to logs, respectively.
- `printtoconsole=1`: Sends traces/debugs to the console (*stdout*).
- `help-debug=1`: Displays debug option help and quits.
- `uacomment=<cmt>`: Adds a comment to User-Agent P2P.

We've now finished listing most of the configuration parameters. This `Bitcoin.conf` file thus constitutes the real dashboard of your node: it defines network configuration, Mempool management, disk and memory usage, indexing, and general administration. If you'd like to learn more about this file and create one tailored to your needs, I recommend using [Jameson Lopp's generator](https://jlopp.github.io/Bitcoin-core-config-generator/).

We've reached the conclusion of this BTC 202 course, which will have enabled you not only to understand the basics of how nodes work and how they interact within the system, but also to set up your own. You're now a sovereign Bitcoiner, with your own self-custody wallet, broadcasting your transactions via your own node. Congratulations!

You can now move on to the final part of the course, where you'll be able to evaluate BTC 202, then take your diploma to check that you've mastered all the concepts covered.

Several paths are now open to you. The next logical step is to set up your own Lightning node, in order to be fully independent for your off-chain transactions. This is precisely the topic of another course on Plan ₿ Academy:

Quiz

Quiz

btc2025.4

What is the default number of outgoing connections a Bitcoin Core node maintains?