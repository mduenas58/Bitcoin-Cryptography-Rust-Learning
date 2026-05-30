# The Self-Sovereign Bitcoiner's Handbook

_A practical, step-by-step guide to running your own Bitcoin and Lightning infrastructure._

---

## 1. Introduction to Self-Sovereignty

Bitcoin's promise is rooted in a simple but radical idea: **don't trust, verify**. When you rely on a third-party block explorer, a custodial exchange, or a public RPC endpoint, you are outsourcing the verification of monetary truth. That undermines the very property that makes Bitcoin valuable.

Running your own full node restores that property. Specifically:

- **Trustlessness** — Your node independently validates every block and transaction against the consensus rules. You no longer have to ask anyone whether a payment is real, whether coins exist, or whether the chain is valid. You compute the answer yourself.
- **Privacy** — When you query an external service for your balance or transactions, you leak data: which addresses belong to you, your IP, your spending patterns. A local node lets your wallet talk to your own infrastructure, dramatically shrinking your surveillance surface.
- **Censorship Resistance** — A node connects you directly to the peer-to-peer network. You broadcast your own transactions, so no intermediary can refuse to relay them.
- **Network Health** — Every additional honest node strengthens Bitcoin's decentralization and makes coercion of node operators harder at scale.

The rest of this guide walks through building that sovereign stack: Bitcoin Core for the base layer, Core Lightning for instant payments, and Specter Desktop with a hardware wallet for signing.

---

## 2. Bitcoin Core Installation & Setup

[Bitcoin Core](https://bitcoincore.org/) is the reference implementation of the Bitcoin protocol. We will install it, verify its authenticity, and complete the initial blockchain download (IBD).

### 2.1 Hardware Requirements

Before you start, plan your hardware:

- **CPU:** Any modern x86-64 or ARM64 processor (Raspberry Pi 4/5 works for pruned nodes).
- **RAM:** 4 GB minimum, 8 GB recommended (more RAM speeds up IBD via larger `dbcache`).
- **Storage:** ~700 GB free on an SSD for a full archival node (May 2026), or ~10 GB for a pruned node. **Always use SSD** — HDDs make IBD painfully slow because of random-access UTXO writes.
- **Network:** Unmetered broadband; expect 300+ GB downloaded during IBD and ~20 GB/month afterward if you serve peers.

### 2.2 Installation

#### Linux (Ubuntu/Debian)

Download the binary tarball, signatures, and SHA256SUMS file from the official site:

```bash
cd ~
VERSION=27.0   # check bitcoincore.org for the latest stable
wget https://bitcoincore.org/bin/bitcoin-core-${VERSION}/bitcoin-${VERSION}-x86_64-linux-gnu.tar.gz
wget https://bitcoincore.org/bin/bitcoin-core-${VERSION}/SHA256SUMS
wget https://bitcoincore.org/bin/bitcoin-core-${VERSION}/SHA256SUMS.asc
```

**Verify the download.** This step is non-negotiable — never run an unverified Bitcoin binary.

```bash
# Import the Bitcoin Core release signing keys
git clone https://github.com/bitcoin-core/guix.sigs.git
gpg --import guix.sigs/builder-keys/*.gpg

# Verify signatures on the SHA256SUMS file
gpg --verify SHA256SUMS.asc SHA256SUMS

# Verify the tarball matches the signed checksum
sha256sum --ignore-missing --check SHA256SUMS
```

You should see `bitcoin-${VERSION}-x86_64-linux-gnu.tar.gz: OK` and at least several "Good signature" lines from independent builders. If anything fails, **stop and investigate**.

Extract and install:

```bash
tar -xvf bitcoin-${VERSION}-x86_64-linux-gnu.tar.gz
sudo install -m 0755 -o root -g root -t /usr/local/bin bitcoin-${VERSION}/bin/*
bitcoind --version
```

#### macOS

Download the `.tar.gz` for macOS from bitcoincore.org and verify it the same way (install GnuPG via Homebrew: `brew install gnupg`). Then:

```bash
tar -xvf bitcoin-27.0-arm64-apple-darwin.tar.gz
sudo cp -r bitcoin-27.0/bin/* /usr/local/bin/
```

Alternatively, use the signed `.dmg` and drag Bitcoin-Qt to `/Applications`. CLI tools live inside the bundle at `/Applications/Bitcoin-Qt.app/Contents/MacOS/`.

#### Windows

Download the signed installer (`bitcoin-27.0-win64-setup.exe`) and verify its SHA256 against `SHA256SUMS` using PowerShell:

```powershell
Get-FileHash .\bitcoin-27.0-win64-setup.exe -Algorithm SHA256
```

Compare the output against the matching line in `SHA256SUMS`. Run the installer; it places `bitcoin-qt.exe`, `bitcoind.exe`, and `bitcoin-cli.exe` in `C:\Program Files\Bitcoin\daemon`.

### 2.3 Data Directory Configuration

The default data directory is:

- Linux: `~/.bitcoin/`
- macOS: `~/Library/Application Support/Bitcoin/`
- Windows: `%APPDATA%\Bitcoin\`

If you are using an external SSD, point Bitcoin Core at it:

```bash
mkdir -p /mnt/btc-ssd/bitcoin
bitcoind -datadir=/mnt/btc-ssd/bitcoin -daemon
```

Or set `datadir=` permanently inside `bitcoin.conf` (see Section 6).

### 2.4 First Run & Initial Block Download

Start the daemon:

```bash
bitcoind -daemon
```

Tail the debug log to monitor progress:

```bash
tail -f ~/.bitcoin/debug.log
```

Check sync state:

```bash
bitcoin-cli getblockchaininfo | grep -E 'blocks|headers|verificationprogress'
```

IBD takes anywhere from **6 hours on a fast NVMe with 16 GB RAM** to **several days on modest hardware**. Bitcoin Core verifies every signature and script — this is the work that makes your node trustless. Don't shortcut it by importing a snapshot from an untrusted source.

### 2.5 Use Cases & Benefits

Once synced, your node becomes the foundation for:

- **Transaction validation** — Every wallet you connect now checks consensus rules locally.
- **Privacy-preserving wallets** — Tools like Specter Desktop, Sparrow, and Electrum (with Electrum Personal Server or `electrs`) can use your node as the only data source.
- **Hardware wallet workflow** — Hot signing software (Specter) talks to your node; cold signing happens on a Ledger, Coldcard, or Trezor.
- **Programmatic access** — `bitcoind` exposes a JSON-RPC interface; `bitcoin-cli` is its command-line wrapper.

---

## 3. Fundamental `bitcoin-cli` Commands

`bitcoin-cli` is your primary interface. Every command below assumes the daemon is running and synced.

### 3.1 Inspecting the Chain

```bash
bitcoin-cli getblockchaininfo
```

Returns chain state: current height, best block hash, verification progress, chain work, and pruning status. Use this to confirm IBD is complete (`verificationprogress` ≈ `1.0`).

### 3.2 Wallet Status

In modern Bitcoin Core (v0.21+), wallets are not loaded automatically. Create or load one first:

```bash
bitcoin-cli createwallet "sovereign"
bitcoin-cli -rpcwallet=sovereign getwalletinfo
```

`getwalletinfo` shows balance, transaction count, key pool size, and whether the wallet is descriptor-based (the modern default) or legacy.

### 3.3 Generating a Receiving Address

```bash
bitcoin-cli -rpcwallet=sovereign getnewaddress "savings" "bech32"
```

Address types you should understand:

- `bech32` — native SegWit (P2WPKH), starts with `bc1q`. Cheapest fees, broad support.
- `bech32m` — Taproot (P2TR), starts with `bc1p`. Best privacy and future-proofing.
- `legacy` — P2PKH, starts with `1`. Avoid unless required for compatibility.

### 3.4 Reviewing History

```bash
bitcoin-cli -rpcwallet=sovereign listtransactions "*" 25 0
```

This returns the last 25 transactions across all labels. Use `getreceivedbyaddress` for per-address totals.

### 3.5 Sending Bitcoin

```bash
bitcoin-cli -rpcwallet=sovereign sendtoaddress \
  "bc1q...recipient..." 0.0025 \
  "rent-may" "landlord" false true null "unset" null 2
```

The trailing arguments are positional: comment, comment-to, subtract-fee-from-amount, replaceable, conf-target, estimate-mode, avoid-reuse, **fee_rate (sat/vB)**. Naming the fee rate explicitly avoids surprise overpayments.

> **Warning:** `sendtoaddress` signs and broadcasts immediately. For large amounts, prefer the PSBT workflow (`walletcreatefundedpsbt` → sign on hardware wallet → `finalizepsbt` → `sendrawtransaction`). Section 5 shows how Specter handles this for you.

### 3.6 Useful Companions

- `bitcoin-cli help` — list every RPC.
- `bitcoin-cli help <command>` — full schema and examples.
- `bitcoin-cli getmempoolinfo` — current mempool state, useful for fee decisions.
- `bitcoin-cli estimatesmartfee 6` — fee rate for ~6 block confirmation.

---

## 4. Lightning Network: Core Lightning (CLN)

Core Lightning, formerly known as c-lightning, is Blockstream's implementation of the Lightning Network protocol. It is rock-solid, plugin-driven, and pairs naturally with Bitcoin Core.

### 4.1 Installation on Linux

Install build dependencies (Debian/Ubuntu):

```bash
sudo apt update
sudo apt install -y autoconf automake build-essential git libtool libsqlite3-dev \
  libgmp-dev libsqlite3-dev python3 python3-pip net-tools zlib1g-dev libsodium-dev \
  gettext libpq-dev protobuf-compiler
```

Clone, check out a release tag, and build:

```bash
git clone https://github.com/ElementsProject/lightning.git
cd lightning
git checkout v24.05    # confirm the latest stable release
./configure
make -j$(nproc)
sudo make install
lightningd --version
```

Always check out a **signed release tag** rather than `master`. Verify the tag with `git tag -v v24.05` against the maintainer's PGP key.

### 4.2 Configuring Bitcoin Core for Lightning

CLN talks to `bitcoind` over RPC. In your `bitcoin.conf`, ensure:

```conf
server=1
txindex=0           # CLN does not need txindex
rpcuser=lightning
rpcpassword=USE_A_LONG_RANDOM_STRING
rpcallowip=127.0.0.1
zmqpubrawblock=tcp://127.0.0.1:28332
zmqpubrawtx=tcp://127.0.0.1:28333
```

Restart `bitcoind`. **Better practice:** instead of `rpcpassword`, use `rpcauth=` with a hashed credential generated by Core's `share/rpcauth/rpcauth.py` script — that way the plaintext password never lives on disk.

### 4.3 The CLN `config` File

Create `~/.lightning/config`:

```conf
# ~/.lightning/config
network=bitcoin
alias=SovereignNode
rgb=ff9900
log-level=info
log-file=/home/satoshi/.lightning/cln.log

# Bitcoin RPC
bitcoin-rpcuser=lightning
bitcoin-rpcpassword=USE_A_LONG_RANDOM_STRING
bitcoin-rpcconnect=127.0.0.1
bitcoin-rpcport=8332

# Networking — Tor only (recommended)
addr=statictor:127.0.0.1:9051
proxy=127.0.0.1:9050
always-use-proxy=true

# Channel defaults
fee-base=1000
fee-per-satoshi=1
min-capacity-sat=100000

# Database safety
wallet=sqlite3:///home/satoshi/.lightning/bitcoin/lightningd.sqlite3
```

### 4.4 Starting `lightningd`

```bash
lightningd --daemon
tail -f ~/.lightning/cln.log
```

Once running, generate an on-chain address to fund the wallet:

```bash
lightning-cli newaddr bech32
```

Send a small amount of BTC to that address from your Bitcoin Core wallet — say 200,000 sats — and wait for at least 3 confirmations.

### 4.5 Opening Your First Channel

You need a peer's `nodeid@host:port`. Reputable starting peers can be found on `1ml.com` or `amboss.space`. Connect and open:

```bash
# Connect to the peer (no funds at risk yet)
lightning-cli connect 03abc...peerpubkey...@xyz.onion:9735

# Open a 100k-sat channel
lightning-cli fundchannel 03abc...peerpubkey... 100000
```

Monitor the channel:

```bash
lightning-cli listpeerchannels
lightning-cli listfunds
```

Channels become usable after 3 confirmations of the funding transaction (or 6 for larger amounts depending on `minimum-depth`).

### 4.6 Daily-Driver `lightning-cli` Commands

- `lightning-cli getinfo` — node ID, addresses, block height, peer count.
- `lightning-cli listpeerchannels` — channel state, balances, fees.
- `lightning-cli invoice <amount_msat> <label> <description>` — create a BOLT 11 invoice.
- `lightning-cli pay <bolt11>` — pay an invoice.
- `lightning-cli decode <bolt11>` — inspect an invoice before paying.
- `lightning-cli close <peerid>` — cooperative channel close.

---

## 5. Security & Hardware Integration

Self-hosting is only sovereign if it is also secure. A node that an attacker can compromise is worse than no node at all.

### 5.1 Node Security Best Practices

**Run as a non-root user.** Create a dedicated account, and never run `bitcoind` or `lightningd` as root:

```bash
sudo adduser --disabled-password --gecos "" satoshi
sudo usermod -aG sudo satoshi   # only if you want sudo; not required
sudo su - satoshi
```

Bitcoin Core and CLN should live entirely under that user.

**Configure a firewall.** UFW gives a clean default-deny posture:

```bash
sudo ufw default deny incoming
sudo ufw default allow outgoing
sudo ufw allow from 192.168.0.0/16 to any port 22 proto tcp   # SSH from LAN only
sudo ufw allow 9735/tcp                                         # Lightning (omit if Tor-only)
sudo ufw enable
sudo ufw status verbose
```

**Never expose the RPC port to the internet.** `bitcoind`'s RPC (8332) and CLN's RPC socket should only be reachable from `127.0.0.1` or a trusted LAN. Confirm with:

```bash
ss -tlnp | grep -E '8332|9735'
```

**Keep SSH locked down.** Disable password auth in `/etc/ssh/sshd_config` (`PasswordAuthentication no`, `PermitRootLogin no`), use ED25519 keys, and consider Fail2ban or a non-default port behind a VPN.

**Encrypt your wallet.** For Bitcoin Core: `bitcoin-cli encryptwallet "<long passphrase>"`. For CLN: use the `hsmtool encrypt` command on `hsm_secret`. Without encryption, anyone with file-level access can drain funds.

**Back up regularly.**

- Bitcoin Core: back up `wallet.dat` (legacy) or the descriptor wallet's `.sqlite` plus the descriptors themselves.
- CLN: back up `hsm_secret` (the seed). Use the `backup` plugin or `--wallet=postgres://...` for live replication of channel state. **Restoring an outdated channel database can cost you funds** because of Lightning's punishment mechanism — channel-state backups must be live, not nightly.

### 5.2 Specter Desktop + Ledger: A Sovereign Hot/Cold Setup

[Specter Desktop](https://specter.solutions/) is a coordinator that turns your Bitcoin Core node into the data source for hardware wallet workflows. Combined with a [Ledger](https://ledger.com/), you get an architecture where:

- **Private keys** never leave the Ledger.
- **Transaction construction and broadcast** happen via your own node.
- **Address derivation and balance lookups** never touch a third party.

#### Step 1 — Connect Specter to Bitcoin Core

Install Specter Desktop from the official release page and verify the GPG signature exactly as you did for Bitcoin Core. On first launch, Specter auto-detects a local node by reading `bitcoin.conf`. If it doesn't, configure manually:

```
RPC host: 127.0.0.1
RPC port: 8332
RPC user: <from bitcoin.conf>
RPC password: <from bitcoin.conf>
```

Specter will create a dedicated wallet inside Core and load it on demand.

#### Step 2 — Initialize the Ledger

On the Ledger device:

1. Set a PIN.
2. **Write down the 24-word recovery phrase on steel or paper, offline.** Never photograph it. Never type it into anything.
3. Install the Bitcoin app via Ledger Live, then close Ledger Live before using Specter (only one host app can hold the USB connection).

#### Step 3 — Add the Ledger to Specter

In Specter, go to **Devices → Add new device → Ledger**, plug in the device, unlock it, and open the Bitcoin app. Specter reads the device's xpubs over USB.

For each address type you intend to use (Native SegWit and Taproot are the modern defaults), Specter saves the corresponding xpub.

#### Step 4 — Create a Single-Sig Wallet

**Wallets → Add new wallet → Single signature**, select the Ledger, choose **Native SegWit** (or Taproot for new wallets), and confirm the derivation path matches what the Ledger displays. Specter will register the descriptor with Bitcoin Core, which then watches and indexes the addresses.

#### Step 5 — Receiving and Spending

- **Receive:** Specter generates an address; **always verify it on the Ledger screen** before sharing it. This defends against malicious malware on the host.
- **Send:** Specter builds a PSBT, sends it to the Ledger, the Ledger displays the recipient and amount on its trusted screen, you approve, the signed PSBT comes back, and Specter broadcasts via your Bitcoin Core node.

This pattern — **air-gapped key custody, locally-validated broadcast** — is the gold standard for a sovereign hot/cold setup. The "hot" half is your node; the "cold" half is the Ledger. Neither side alone can move your coins.

> **Tip:** For larger holdings, repeat the process with two or three hardware wallets from different vendors (e.g., Ledger + Coldcard + Trezor) and create a **multisig** wallet in Specter. This eliminates any single point of failure — including any single vendor's firmware.

---

## 6. Advanced Configurations

### 6.1 Pruned Node

Pruning lets you run a fully-validating node without storing the entire historical chain. The node still verifies every block during IBD; it just discards block data older than the prune target afterward.

In `bitcoin.conf`:

```conf
prune=10000     # keep ~10 GB of recent blocks (minimum 550)
```

Trade-offs:

- **You cannot serve historical blocks** to other peers (limits network contribution).
- **You cannot rescan deep history** for a freshly imported descriptor without re-downloading.
- **Lightning still works** — CLN only needs recent block data, ZMQ notifications, and the RPC interface.

For a Raspberry Pi setup, `prune=10000` plus a 256 GB SSD is plenty.

### 6.2 An Optimized `bitcoin.conf`

Drop the following into `~/.bitcoin/bitcoin.conf`. Tune the values to your hardware:

```conf
# === Core ===
server=1
daemon=1
txindex=0                   # set to 1 only if you run electrs / a block explorer

# === Performance ===
dbcache=4096                # MB of UTXO cache; set to ~50% of free RAM for IBD
par=0                       # auto-detect CPU cores for script verification
maxmempool=300              # MB; raise on high-traffic nodes
mempoolexpiry=72            # hours

# === Pruning (optional) ===
# prune=10000

# === Networking ===
listen=1
maxconnections=40
maxuploadtarget=5000        # MB/day; cap upstream so you don't saturate your link

# === Tor (recommended) ===
proxy=127.0.0.1:9050
listenonion=1
onlynet=onion               # remove this line if you also want clearnet peers
bind=127.0.0.1
discover=0

# === RPC ===
rpcbind=127.0.0.1
rpcallowip=127.0.0.1
# Use rpcauth (hashed) instead of rpcuser/rpcpassword in production:
rpcauth=lightning:abcd1234$0123456789abcdef...

# === ZMQ for Lightning / indexers ===
zmqpubrawblock=tcp://127.0.0.1:28332
zmqpubrawtx=tcp://127.0.0.1:28333
```

> **Tip:** During IBD, temporarily set `dbcache` very high (e.g., 8192 on a 16 GB machine) and `assumevalid` to a recent known-good block hash to accelerate sync. Lower `dbcache` once IBD finishes; the running node doesn't need it.

### 6.3 Lightning Networking: Tor and Inbound Liquidity

Two reasons you want Tor for Lightning:

1. **Privacy** — clearnet exposes your home IP to every peer you connect to.
2. **Connectivity** — Tor side-steps NAT and consumer-grade ISP port-blocking, so you don't need to forward `9735/tcp` on your router.

#### Install and Configure Tor

```bash
sudo apt install -y tor
sudo nano /etc/tor/torrc
```

Add (or uncomment) the following:

```conf
ControlPort 9051
CookieAuthentication 1
CookieAuthFileGroupReadable 1
SocksPort 9050
```

Add your Bitcoin/Lightning user to the `debian-tor` group so it can read the auth cookie:

```bash
sudo usermod -aG debian-tor satoshi
sudo systemctl restart tor
```

In `bitcoin.conf` (already shown above) and in CLN's `config` (from Section 4.3), the `proxy=127.0.0.1:9050` and `addr=statictor:127.0.0.1:9051` lines route everything through Tor. CLN's `statictor` directive gives you a **stable** `.onion` address across restarts — important so peers can keep finding you.

#### Clearnet (If You Insist)

If you want a clearnet Lightning endpoint for better routing throughput, forward `9735/tcp` from your router to your node, and add to CLN's config:

```conf
addr=0.0.0.0:9735
announce-addr=your.public.host:9735
```

Combine with Tor (`addr=statictor:...`) so peers can reach you either way. **Never** announce your residential public IP without considering the privacy implications.

#### Inbound Liquidity

A new Lightning node only has outbound capacity (you can pay, but not receive) until peers open channels back to you. Options:

- **Liquidity marketplaces** (Lightning Pool, Magma, LNRouter) — pay a small fee for inbound capacity.
- **Swaps** — use Loop Out / Boltz to send on-chain funds out of Lightning, freeing inbound space on your existing channels.
- **Reciprocal opens** — a peer you opened to may open back; community channels often arrange this.

---

## Closing Thoughts

Self-hosting Bitcoin infrastructure is a journey, not a one-time install. Maintain it the way you would any other security-critical system: keep software updated to signed releases, monitor logs (`debug.log`, `cln.log`), back up wallets and channel state, and test recovery on testnet or signet before you ever need to do it for real.

The minute your node finishes IBD and your hardware wallet first signs a PSBT through Specter, you've crossed a line: you no longer need anyone's permission to use Bitcoin. That is what self-sovereignty actually feels like.

**Verify, then trust yourself.**

---

### Quick Reference: Key Sources

- Bitcoin Core: https://bitcoincore.org
- Core Lightning: https://github.com/ElementsProject/lightning
- Specter Desktop: https://specter.solutions
- Ledger: https://ledger.com