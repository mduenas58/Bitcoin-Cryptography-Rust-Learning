A comprehensive list of all `bitcoin-cli` commands would be quite lengthy, so this guide focuses on the most essential and commonly used commands. These are organized by category to help you quickly find what you need.

`bitcoin-cli` connects to a running `bitcoind` daemon via RPC to query blockchain data, manage wallets, and perform transactions. For a complete and authoritative list of all available commands, you can run `bitcoin-cli help` on your own node.

### 💻 General Commands
| Command | Description | Example |
| :--- | :--- | :--- |
| `help` | Lists all commands or provides detailed help for a specific command. | `bitcoin-cli help`<br>`bitcoin-cli help getblockchaininfo` |
| `stop` | Shuts down the Bitcoin Core server gracefully. | `bitcoin-cli stop` |
| `uptime` | Returns the total number of seconds the server has been running. | `bitcoin-cli uptime` |

### ⛓️ Blockchain Information
| Command             | Description                                                                      | Example                                                                                 |
| :------------------ | :------------------------------------------------------------------------------- | :-------------------------------------------------------------------------------------- |
| `getblockchaininfo` | Returns an object containing various state info regarding blockchain processing. | `bitcoin-cli getblockchaininfo`                                                         |
| `getblockcount`     | Returns the number of blocks in the longest blockchain.                          | `bitcoin-cli getblockcount`                                                             |
| `getblockhash`      | Returns the hash of the block at the specified block height.                     | `bitcoin-cli getblockhash 1000`                                                         |
| `getblock`          | Returns detailed block information for the given block hash.                     | `bitcoin-cli getblock 000000000019d6689c085ae165831e934ff763ae46a2a6c172b3f1b60a8ce26f` |
| `getdifficulty`     | Returns the proof-of-work difficulty as a multiple of the minimum difficulty.    | `bitcoin-cli getdifficulty`                                                             |
| `gettxoutsetinfo`   | Returns statistics about the unspent transaction output (UTXO) set.              | `bitcoin-cli gettxoutsetinfo`                                                           |

### 👛 Wallet Management
| Command | Description | Example |
| :--- | :--- | :--- |
| `getwalletinfo` | Returns an object containing information about the wallet. | `bitcoin-cli getwalletinfo` |
| `getbalance` | Returns the wallet's total available balance. | `bitcoin-cli getbalance` |
| `listtransactions` | Returns up to the most recent transactions from the wallet. | `bitcoin-cli listtransactions` |
| `getnewaddress` | Generates a new Bitcoin address for receiving payments. | `bitcoin-cli getnewaddress` |
| `sendtoaddress` | Sends an amount of Bitcoin to a given address. | `bitcoin-cli sendtoaddress "bc1q..." 0.01` |
| `listunspent` | Returns an array of unspent transaction outputs (UTXOs) controlled by the wallet. | `bitcoin-cli listunspent` |
| `dumpprivkey` | Reveals the private key corresponding to a given address. | `bitcoin-cli dumpprivkey "bc1q..."` |
| `dumpwallet` | Dumps all wallet keys into a specified file. | `bitcoin-cli dumpwallet "backup.txt"` |
| `backupwallet` | Safely copies the wallet.dat file to a specified destination. | `bitcoin-cli backupwallet "/path/to/backup/wallet.dat"` |

### 💰 Transaction Handling
| Command | Description | Example |
| :--- | :--- | :--- |
| `gettransaction` | Returns detailed information about an in-wallet transaction. | `bitcoin-cli gettransaction "txid"` |
| `createrawtransaction` | Creates a raw, unsigned transaction from specified inputs and outputs. | `bitcoin-cli createrawtransaction '[{"txid":"...","vout":0}]' '{"address":0.01}'` |
| `signrawtransactionwithwallet` | Signs the inputs of a raw transaction using keys from the wallet. | `bitcoin-cli signrawtransactionwithwallet "raw_hex"` |
| `sendrawtransaction` | Submits a raw transaction (signed) to the network for propagation. | `bitcoin-cli sendrawtransaction "signed_hex"` |

### ⛏️ Mining Commands
These commands are primarily used on test networks or private chains (`-regtest`).

| Command | Description | Example |
| :--- | :--- | :--- |
| `generate` | Generates one or more blocks instantly (e.g., for regression testing). | `bitcoin-cli -regtest generate 1` |
| `generatetoaddress` | Mines blocks immediately to a specified address. | `bitcoin-cli generatetoaddress 1 "bcrt1q..."` |
| `getmininginfo` | Returns a JSON object containing mining-related information. | `bitcoin-cli getmininginfo` |
| `getblocktemplate` | Returns data needed to construct a block to work on. | `bitcoin-cli getblocktemplate` |

### 🌐 Network & P2P
| Command | Description | Example |
| :--- | :--- | :--- |
| `getnetworkinfo` | Returns information about the node's connection to the network. | `bitcoin-cli getnetworkinfo` |
| `getpeerinfo` | Returns data about each connected network node. | `bitcoin-cli getpeerinfo` |
| `ping` | Sends a ping to all connected peers to measure latency. | `bitcoin-cli ping` |
| `addnode` | Attempts to add or remove a peer node (e.g., add, remove, onetry). | `bitcoin-cli addnode "1.2.3.4" "add"` |
| `setnetworkactive` | Disables or enables all P2P network activity. | `bitcoin-cli setnetworkactive false` |

A best practice is to use `-named` before the command, allowing you to specify arguments by name (`key=value`). This approach is more explicit and less error-prone than relying on positional arguments. For more advanced scripting, you can also use `-stdin` to read sensitive arguments (like passphrases) securely from standard input.