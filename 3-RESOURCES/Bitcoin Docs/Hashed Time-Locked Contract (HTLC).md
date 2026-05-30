A **Hashed Time-Locked Contract (HTLC)** is a conditional payment mechanism used in the Lightning Network to enable secure, trustless, and atomic payments across multiple payment channels. It ensures that a payment either completes fully (successfully reaching the recipient) or fails entirely without any partial loss of funds.

## Key Components

HTLCs combine two types of cryptographic locks:

1. **Hashlock** – The payment is locked using a cryptographic hash of a secret (preimage). Only the party who knows the original secret (the preimage) can claim the funds.

2. **Timelock** – An absolute or relative time constraint. If the secret is not revealed before the deadline, the funds are returned to the sender (or previous hop).

## How an HTLC Works in a Multi-Hop Payment

Suppose **Alice** wants to pay **Bob** via intermediate nodes **Carol** and **Dave**:

1. **Bob generates a secret R** and sends its hash `H = hash(R)` to Alice (out of band).

2. **Alice creates an HTLC** with Bob’s hash `H` to Carol on their channel:  
   *"Carol can claim X satoshis if she provides the preimage of H within 48 hours; otherwise the funds return to Alice."*

3. **Carol creates an HTLC** with the same hash `H` to Dave on their channel, but with a shorter timelock (e.g., 24 hours).

4. **Dave creates an HTLC** with `H` to Bob, with an even shorter timelock (e.g., 12 hours).

5. **Bob reveals the secret R** to Dave to claim the final HTLC.

6. **Dave uses the same secret R** to claim Carol’s HTLC.

7. **Carol uses R** to claim Alice’s HTLC.

Once the secret propagates back, every participant gets paid. If Bob never reveals R, all HTLCs time out and funds are refunded.

## Why HTLCs Are Essential

- **Atomicity** – The whole multi-hop payment either succeeds (secret revealed) or fails (all timelocks expire). No middleman can steal funds.
- **Trustless routing** – Nodes do not need to trust each other; the smart contract enforces behavior.
- **Channel balance management** – HTLCs are temporarily committed in channel states, adjusting balances only upon success.
- **Scalability** – Enables off-chain payments across a network of channels without a central hub.

## Relation to Lightning Channel States

Each HTLC is part of the commitment transaction of a payment channel. When an HTLC is active:
- The sending side’s balance is reduced by the HTLC amount.
- The receiving side’s balance is increased only after the secret is revealed.
- If a node tries to cheat by broadcasting an old state without a settled HTLC, the revocation mechanism (as in your previous question) penalizes them.

## Security Properties

- **No partial completion** – Without the preimage, the HTLC is unclaimable.
- **Timelock enforcement** – Absolute timelocks (CLTV) or relative timelocks (CSV) prevent indefinite locking of funds.
- **Collision resistance** – The hash function (SHA-256) ensures preimages are infeasible to guess.

In summary, HTLCs are the fundamental building block that turns a set of bidirectional payment channels into a decentralized, censorship-resistant routing network for instant, low-fee Bitcoin transactions.