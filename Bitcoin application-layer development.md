This 40-hour plan applies the 80/20 rule to Bitcoin Development. The 20% of concepts that yield 80% of your capabilities are: **The UTXO model, Hierarchical Deterministic (HD) wallets, SegWit transaction construction, Bitcoin Script basics, and PSBTs (Partially Signed Bitcoin Transactions).**

We will skip writing C++ consensus code, mining algorithms, and deep P2P networking. We will focus entirely on **application-layer development** (building wallets, creating transactions, reading the chain) using JavaScript/TypeScript, as it offers the fastest feedback loop and most widely used libraries.

### **The 80/20 Bitcoin Dev Resource Stack**
1. **Book:** *Mastering Bitcoin* (2nd Edition) by Andreas Antonopoulos. (Read Chapters 4, 5, 6, and 7 only. The rest is context).
2. **Library:** `bitcoinjs-lib` (The industry standard for JS transaction building).
3. **API/Indexer:** Mempool.space Open API & Blockstream Esplora (How you talk to the network without running a node).
4. **Visualizer:** Bitcoin Script Debugger (bitcoinscript.com).
5. **Reference:** Bitcoin Optech (bitcoinops.org) - for understanding modern best practices.

---

### **Phase 1: Cryptographic Keys & Identity (Sessions 1-3)**

**Session 1: Elliptic Curve Cryptography (Secp256k1) for Devs**
*The 80/20: You don't need the math. You need to know how a private key maps to a public key using a specific curve, and how to use libraries to do it.*
* **Min 0-30:** Public/private key pairs. Why Bitcoin uses `secp256k1`. Compressed vs. Uncompressed public keys (and why we only use compressed now).
* **Min 30-75:** **Resource:** Read *Mastering Bitcoin* Ch 4. Use an online tool (like learnmeabitcoin.com) to generate a private key and derive the public key.
* **Min 75-105:** **Code:** Use the `secp256k1` or `tiny-secp256k1` npm package in Node.js to generate a random private key and derive its compressed public key. Log both.
* **Min 105-120 (15-min Review):** *Feynman Prompt:* Why is it impossible to derive the private key from the public key? What is the difference between a 33-byte and a 65-byte public key?

**Session 2: HD Wallets & BIP32 (The Tree of Keys)**
*The 80/20: Modern wallets don't generate random keys; they derive them from a single seed in a tree structure.*
* **Min 0-30:** The problem with random keys (backups become impossible). Enter Hierarchical Deterministic wallets. Parent/Child keys. Extended Public Keys (xpubs) and Extended Private Keys (xprivs).
* **Min 30-75:** **Resource:** Read BIP-32 specification (just the summary and derivation path concepts). Watch "BIP32 Explained" by BTC Sessions.
* **Min 75-105:** **Code:** Install `bip32` and `tiny-secp256k1`. Take your private key from Session 1, create a root xpriv/xpub, and derive a child key at path `m/0/0`.
* **Min 105-120 (15-min Review):** *Feynman Prompt:* If I give you an xpub (Extended Public Key), what can you do? What can you *not* do?

**Session 3: Mnemonics & Derivation Paths (BIP39/BIP44)**
*The 80/20: How humans interact with HD wallets (12/24 words) and how those words map to standard wallet structures.*
* **Min 0-30:** BIP-39: Entropy to Mnemonics. Passwords/Passphrases (the "25th word"). BIP-44: Standard paths (`m/44'/0'/0'/0/0` for Legacy, `m/84'/0'/0'/0/0` for Native SegWit).
* **Min 30-75:** **Resource:** Read BIP-39 and BIP-44 summaries. Use Ian Coleman's BIP39 tool (offline) to generate a mnemonic and see the derived addresses.
* **Min 75-105:** **Code:** Install `bip39`. Generate a 12-word mnemonic. Convert it to a seed. Feed that seed into your BIP32 code from Session 2 to derive the first 5 receive addresses.
* **Min 105-120 (15-min Review):** *Feynman Prompt:* If someone gets my 12-word seed phrase, do they need my passphrase to steal my funds? If I lose the seed phrase but keep the passphrase, are my funds safe?

---

### **Phase 2: The Ledger & Transactions (Sessions 4-7)**

**Session 4: The UTXO Model (The hardest mental shift)**
*The 80/20: Bitcoin has no accounts or balances. It only has unspent transaction outputs (UTXOs). Understanding this is 50% of Bitcoin dev.*
* **Min 0-45:** UTXOs explained. Analogy: Cash in a drawer vs. Bank account balance. Inputs consume UTXOs; Outputs create new UTXOs. Transaction fees = Sum(Inputs) - Sum(Outputs).
* **Min 45-105:** **Resource:** Read *Mastering Bitcoin* Ch 5 & 6. Go to Mempool.space, click on a random transaction, and visually trace which UTXOs were consumed and which were created.
* **Min 105-120 (15-min Review):** *Feynman Prompt:* I have 1 BTC in my wallet. I send 0.2 BTC to Alice. How many UTXOs did I likely consume? How many new UTXOs were created? (Hint: Think about change).

**Session 5: Address Formats (P2PKH, P2SH, P2WPKH, P2TR)**
*The 80/20: Addresses are just human-readable wrappers around locking scripts. Native SegWit (bech32) is the current standard.*
* **Min 0-45:** Evolution of addresses: 
  * Legacy (P2PKH): Starts with `1`. Inefficient.
  * Nested SegWit (P2SH-P2WPKH): Starts with `3`. Backward compatible hack.
  * Native SegWit (P2WPKH): Starts with `bc1q`. The 80/20 standard. Cheaper fees.
  * Taproot (P2TR): Starts with `bc1p`. Privacy & efficiency upgrades.
* **Min 45-105:** **Resource:** Read *Mastering Bitcoin* Ch 5 (Address formats). Use `bitcoinjs-lib` to take a public key and generate a P2WPKH (Native SegWit) address.
* **Min 105-120 (15-min Review):** *Feynman Prompt:* Why should a new wallet application *only* generate `bc1q` (Native SegWit) addresses by default today?

**Session 6: Raw Transaction Anatomy**
*The 80/20: Peeling back the hex. Understanding Version, Locktime, Inputs (TxID, Vout, ScriptSig/Witness), and Outputs (Value, ScriptPubKey).*
* **Min 0-45:** Transaction structure. TxID vs. Wtxid (SegWit difference). Block headers vs. Transaction data.
* **Min 45-105:** **Resource:** Find a transaction on a block explorer. Copy its raw hex. Paste it into a transaction decoder (like bitcoindeck.com). Map every byte to the Version, Inputs, Outputs, and Locktime fields.
* **Min 105-120 (15-min Review):** *Feynman Prompt:* Where is the actual "sender address" stored inside a raw Bitcoin transaction? (Trick question: It isn't. It's implied by the inputs).

**Session 7: Fee Calculation & RBF (Replace-by-Fee)**
*The 80/20: If you mess up fees, your transaction is stuck forever. You must know how to calculate sat/vByte and implement RBF.*
* **Min 0-30:** Virtual Bytes (vBytes) vs. Weight units (WU). Why SegWit transactions get a "discount" on fees.
* **Min 30-75:** How to estimate fees using the Mempool.space API (`/api/v1/fees/recommended`). 
* **Min 75-105:** **Resource:** Read Bitcoin Optech article on RBF. Look at a transaction on mempool.space that has an "RBF" flag. 
* **Min 105-120 (15-min Review):** *Feynman Prompt:* A transaction is 250 vBytes. The economy fee is 20 sat/vByte. What is the total fee in sats? If you underpay, how does RBF fix it?

---

### **Phase 3: Bitcoin Script (Sessions 8-10)**

**Session 8: Script Basics & The Stack**
*The 80/20: Bitcoin Script is a simple, purposefully non-Turing-complete language. You just need to understand the stack (push/push/OP_ADD/equal).*
* **Min 0-45:** Forth-like stack execution. No loops. Basic opcodes: `OP_DUP`, `OP_HASH160`, `OP_EQUALVERIFY`, `OP_CHECKSIG`.
* **Min 45-105:** **Resource:** Go to bitcoinscript.com. Type `OP_DUP OP_HASH160 <pubKeyHash> OP_EQUALVERIFY OP_CHECKSIG`. Push a dummy signature and public key onto the stack and click "Run" to see it pass.
* **Min 105-120 (15-min Review):** *Feynman Prompt:* Why did Satoshi make Bitcoin Script intentionally incapable of loops (Turing incomplete)?

**Session 9: P2WPKH Under the Hood (Locking & Unlocking)**
*The 80/20: Stripping away the address abstraction to see exactly how a standard Native SegWit transaction locks and unlocks funds.*
* **Min 0-45:** Locking Script (ScriptPubKey) for P2WPKH: `OP_0 <20-byte-hash>`. Unlocking (Witness): `<Signature> <PublicKey>`. 
* **Min 30-75:** The execution flow: Hash the public key $\rightarrow$ check if it matches the hash in the script $\rightarrow$ check if the signature is valid for that public key.
* **Min 75-105:** **Resource:** Read *Mastering Bitcoin* Ch 6 (SegWit section). Trace the P2WPKH execution on the script debugger.
* **Min 105-120 (15-min Review):** *Feynman Prompt:* In Legacy transactions, the signature went in the `ScriptSig`. In SegWit, where does it go, and why did this fix the transaction malleability bug?

**Session 10: Multisig & Timelocks (Intro)**
*The 80/20: You will inevitably need to build 2-of-3 wallets or time-locked transactions. Understand the opcodes, but know you'll use libraries to build them.*
* **Min 0-45:** `OP_CHECKMULTISIG`. Bare multisig vs. P2WSH (Pay-to-Witness-Script-Hash). Timelocks: `CSV` (CheckSequenceVerify) for relative time, `CLTV` (CheckLockTimeVerify) for absolute time.
* **Min 45-105:** **Resource:** Read Bitcoin Optech summaries on P2WSH and Timelocks. Look up a P2WSH transaction on a block explorer and look at its "Witness Script" (the redeem script).
* **Min 105-120 (15-min Review):** *Feynman Prompt:* If I want to create a vault where funds can *only* be spent after 1 year, which opcode do I put in the script?

---

### **Phase 4: Modern Transaction Building (Sessions 11-14)**

**Session 11: Building a Transaction Manually (P2WPKH)**
*The 80/20: Gluing it all together. Fetching UTXOs, building the transaction object, signing, and extracting the hex.*
* **Min 0-30:** The workflow: 1. Get UTXOs from API. 2. Create `PSBT` (or `TransactionBuilder`). 3. Add inputs. 4. Add outputs (recipient + change). 
* **Min 30-90:** **Code:** Use `bitcoinjs-lib`. Fetch a real UTXO from the Bitcoin Testnet (using Blockstream Testnet API). Build a transaction sending Testnet BTC to another address. Sign it with your private key.
* **Min 90-105:** Extract the raw hex. Broadcast it using the Blockstream `/api/tx` endpoint.
* **Min 105-120 (15-min Review):** *Feynman Prompt:* What happens if you forget to add a "change" output to a transaction? (Answer: The leftover sats become the miner's fee).

**Session 12: PSBTs (Partially Signed Bitcoin Transactions) - The Core Standard**
*The 80/20: PSBTs are how modern wallets (especially hardware wallets) interact. You will use PSBTs for 90% of complex workflows.*
* **Min 0-45:** Why PSBTs were created (BIP-174). Separating the *creation* of a transaction from the *signing* of a transaction. The structure of a PSBT (Global, Inputs, Outputs maps).
* **Min 45-105:** **Resource:** Read the BIP-174 GitHub summary. Use a PSBT decoder online. Take the signed transaction from Session 11, convert it to a PSBT format using `bitcoinjs-lib`, and inspect the base64 string.
* **Min 105-120 (15-min Review):** *Feynman Prompt:* Alice creates a transaction on an offline computer and puts it on a USB drive. Bob signs it on his hardware wallet. What data format makes this possible?

**Session 13: PSBTs in Practice: Air-gapped & Multisig Workflows**
*The 80/20: Passing PSBTs between different parties/devices.*
* **Min 0-30:** The workflow of a 2-of-3 multisig using PSBTs. Initiator creates PSBT $\rightarrow$ Signer 1 signs $\rightarrow$ Signer 2 signs $\rightarrow$ Finalizer combines and extracts hex.
* **Min 30-90:** **Code:** Use `bitcoinjs-lib` and `bip68` (for timelocks if feeling adventurous, otherwise stick to multisig). Create a 2-of-2 PSBT. Sign it with Key 1. Pass the base64 to a separate function and sign with Key 2. Finalize and broadcast to Testnet.
* **Min 90-105:** Debug any errors. PSBTs fail often due to missing global xpubs or incorrect sighash types. Learn to read the error logs.
* **Min 105-120 (15-min Review):** *Feynman Prompt:* Can a hardware wallet see the balance of the wallet just by looking at a PSBT it is asked to sign? Why or why not?

**Session 14: Taproot & P2TR (The New Paradigm)**
*The 80/20: Taproot makes complex scripts look exactly like standard single-signature transactions on the blockchain. You don't need to build complex Taproot scripts yet, but you *must* know how to send to them.*
* **Min 0-45:** Schnorr Signatures vs. ECDSA. Key path spending vs. Script path spending. How Taproot hides multisig conditions inside a single public key (MAST concept).
* **Min 45-105:** **Resource:** Read *Mastering Bitcoin* (update appendix on Taproot) or a high-level Taproot explainer by Bitcoin Optech. Generate a P2TR (bc1p) address using `bitcoinjs-lib`.
* **Min 105-120 (15-min Review):** *Feynman Prompt:* Why is a 5-of-5 multisig Taproot transaction cheaper on fees than a 5-of-5 Legacy multisig transaction?

---

### **Phase 5: Interfacing with the Ecosystem (Sessions 15-17)**

**Session 15: Indexers & APIs (Mempool & Esplora)**
*The 80/20: You rarely run your own node for app development. You use Indexers. Knowing their endpoints is critical.*
* **Min 0-30:** What an indexer does (parses the blockchain into a relational database). Blockstream Esplora vs. Mempool.space APIs.
* **Min 30-90:** **Code:** Write a Node.js script that takes a `bc1q` address and fetches: 1. Total balance. 2. List of UTXOs. 3. Transaction history. Do this using ONLY the Mempool.space REST API (`/api/address/:address`).
* **Min 90-105:** Error handling. What if the API is down? What if the address has 10,000 transactions (pagination)?
* **Min 105-120 (15-min Review):** *Feynman Prompt:* If an API returns a UTXO, how do you know it hasn't already been spent by the time you build your transaction? (Hint: Race conditions).

**Session 16: Webhooks & Real-time Tracking**
*The 80/20: E-commerce needs to know *instantly* when a payment is made. Polling APIs is bad; WebSockets/Webhooks are good.*
* **Min 0-45:** The problem with polling (rate limits, latency). Mempool.space WebSockets. Third-party services like Electrumx servers or paid APIs (like Chainalysis or mempool.space API alternatives).
* **Min 45-105:** **Code:** Connect to the Mempool.space WebSocket (`wss://mempool.space/api/v1/ws`). Subscribe to a specific Bitcoin address. Send Testnet BTC to that address and watch the terminal print the unconfirmed TXID in real-time.
* **Min 105-120 (15-min Review):** *Feynman Prompt:* Why shouldn't you consider a transaction "confirmed" just because you see it in the mempool via WebSocket?

**Session 17: Running Your Own Node (ElectrumX vs. Core)**
*The 80/20: For production apps, relying on a third-party API is a business risk. You need to know how to plug your app into your own infrastructure.*
* **Min 0-45:** Bitcoin Core (heavy, fully validating) vs. Electrum Server (ElectrumX/Fulcrum - lightweight, relies on Core, provides fast querying). 
* **Min 45-105:** **Resource:** Download and install Electrs or ElectrumX locally (or via Docker). Connect an Electrum client library (like `electrum-client` in JS) to your local server. Fetch a balance.
* **Min 105-120 (15-min Review):** *Feynman Prompt:* If you run an exchange and use a third-party API, what happens to your business if that API goes offline for 24 hours?

---

### **Phase 6: Capstone Application (Sessions 18-20)**

**Session 18: Capstone Build - The Backend (Node.js)**
*The 80/20: Building a simple, functional backend for a Bitcoin checkout system.*
* **Min 0-90:** **Code:** Build an Express.js server with two endpoints:
  1. `POST /generate-invoice`: Generates a new Testnet address (using HD derivation), returns the address and expected BTC amount.
  2. `POST /verify-payment`: Takes a TXID, fetches it from the API, verifies the amount sent matches the invoice, and checks if it has 1 confirmation.
* **Min 90-105:** Refactor the fee calculation to ensure you don't accidentally accept a transaction where the user underpaid fees (which could get stuck/dropped).
* **Min 105-120 (15-min Review):** *Feynman Prompt:* How does your backend keep track of which derivation index (`m/84'/0'/0'/0/X`) belongs to which invoice?

**Session 19: Capstone Build - The Transaction Assembler**
*The 80/20: Automating the UTXO selection and change address generation.*
* **Min 0-90:** **Code:** Add a `POST /sweep-wallet` endpoint to your server. It should: 1. Fetch ALL UTXOs for a given extended public key. 2. Calculate the total value. 3. Subtract a 10 sat/vByte fee. 4. Build a transaction sending everything to a single destination address. 5. Return the PSBT (unsigned).
* **Min 90-105:** Test edge cases. What if the UTXOs are dust (too small to even pay the fee)?
* **Min 105-120 (15-min Review):** *Feynman Prompt:* What is "dust," and why do wallets refuse to spend it?

**Session 20: Security, Best Practices, & Next Steps**
*The 80/20: How not to lose money or get hacked as a developer.*
* **Min 0-45:** Securing private keys in memory (zeroing out memory after use). Never log sensitive data. The dangers of entropy issues (Math.random() vs. crypto.randomBytes()). 
* **Min 45-90:** **Resource:** Read the Bitcoin Optech "Common Vulnerabilities" page. Review your Capstone code. Did you use `crypto.randomBytes`? Did you expose private keys in API responses? Did you handle change addresses correctly?
* **Min 90-105:** Mapping the next 80% (What to learn next if you want to go deeper: Lightning Network (LND/CLN), Miniscript, Bitcoin Core C++ development, DLCs).
* **Min 105-120 (15-min Review):** *Feynman Prompt:* You are auditing a junior dev's code. You see they stored the user's private key in a MongoDB database to "make signing faster on the backend." What do you tell them?

### **Post-Plan Golden Rules for Bitcoin Devs:**
1. **Never roll your own crypto:** Use `bitcoinjs-lib`. Do not manually concatenate hex strings to build scripts.
2. **Always verify on Testnet first:** Real BTC is immutable. Bugs cost real money.
3. **Treat UTXOs as cash:** If you lose the physical bill (delete the UTXO database), the money is gone. Backups are not optional.
4. **SegWit is mandatory:** Never build an application that creates P2PKH (`1...`) addresses. Always use Native SegWit (`bc1q...`) or Taproot (`bc1p...`).