
Here is the content converted into a `BTC-introduction.md` file, ready for download or further editing.

```markdown
# Introduction
## Bitcoin Core and protocol implementations

### What you will learn:
- A historic implementation that has become a benchmark
- Current distribution of implementations
- Internal operation of Bitcoin Core
- Other Bitcoin implementations
- The power of Core developers

The Bitcoin protocol is not software: it is a set of tacit rules shared between network users. It defines transaction validity conditions, money creation mechanisms, block format, proof-of-work conditions, and many other specifications. To interact with this protocol, users must run software that implements these rules: this is known as an **implementation of Bitcoin**.

An implementation is therefore node software: a program capable of interfacing with other machines on the Bitcoin network, downloading, verifying, storing, and propagating blocks and transactions, and locally enforcing consensus and relay rules. Each implementation is a concrete interpretation of the protocol, written in a given programming language, with its own architecture, performance, and ergonomics. Each implementation will also have its own development organization, with its own division of responsibilities.

Among these implementations, one dominates by far: **Bitcoin Core**.

![Bitcoin Core](https://via.placeholder.com/800x400?text=Bitcoin+Core+Image)

---

## A historic implementation that has become a benchmark

**Bitcoin Core** is the reference software for the Bitcoin protocol. It is derived from the original code written by Satoshi Nakamoto in 2008-2009, and is a direct continuation of it. Initially known as "Bitcoin", then "Bitcoin QT" (due to the addition of a graphical interface via the Qt library), it was renamed "Bitcoin Core" in 2014 to clearly differentiate the software from the network. Since version 0.5, it has been distributed with two components: `bitcoin-qt` (the graphical interface) and `bitcoind` (the command-line interface).

In theory, Bitcoin Core does not represent the Bitcoin protocol; rather, it is just one implementation among many. It is, however, distinguished by its massive adoption, its age, the robustness of its code, and the rigor of its development process. Consequently, in practice, the rules applied by Bitcoin Core are *de facto* those of the Bitcoin protocol: users, developers, miners, and ecosystem services refer to it almost exclusively.

---

## Current distribution of implementations

According to data collected in August 2025 by Luke Dashjr (a well-known developer in the ecosystem), the distribution of implementations among the network's public nodes is as follows:

- **Bitcoin Core:** 87.3% of nodes
- **Bitcoin Knots:** 12.5%
- **Other cumulative implementations:** 0.2% (btcsuite, Bcoin, BTCD...)

![Node Distribution](https://via.placeholder.com/600x300?text=Node+Distribution+Chart)

In other words, around 9 out of 10 public nodes are running Bitcoin Core. The rest of the network relies on more marginal clients (although Knots' share has risen sharply in recent months, not least in the wake of debates over the `OP_RETURN` size limit). These alternative implementations are often maintained by a single person or a small team.

> **Note:** These figures are still estimates, however, as they are based primarily on listening nodes, i.e., nodes accepting incoming connections (with port 8333 open). Non-listening nodes are much more complex to count, since it's impossible to connect to them directly: you have to wait for the initiative to come from them, in the form of an outgoing connection. Luke Dashjr's site claims to be trying to count these non-listening nodes too, but it remains impossible to obtain perfectly accurate data about them, and the updating of these statistics inevitably lags behind reality.

---

## Internal operation of Bitcoin Core

Bitcoin Core is software written in **C++**. It is also an open-source project maintained by a community of developers who are either volunteers or funded by various entities (often companies within the ecosystem that have an interest in ensuring that Core development proceeds favorably). The code is hosted on GitHub, and development follows a rigorous model:

1.  Contributors submit proposals in the form of **pull requests (PR)**. In principle, anyone can propose a change, but it must be tested, documented, and go through a peer review process.
2.  The **maintainers** have the right to approve and merge PRs. They are the ones who guarantee the coherence and stability of the project. In July 2025, there are five of them: Hennadii Stepanov, Michael Ford, Andrew Chow, Gloria Zhao, and Ryan Ofsky.
3.  There has been **no principal maintainer** since February 2023. This role was initially held by Satoshi Nakamoto at the launch of Bitcoin, then by Gavin Andresen following Nakamoto's departure in early 2011, and finally by Wladimir J. Van Der Laan from 2014 to 2023.

![Core Development](https://via.placeholder.com/800x400?text=Bitcoin+Core+Development)

The development of Bitcoin Core follows a meritocratic logic: new contributors are encouraged to review and test the code before proposing any changes themselves. Decisions are based on technical consensus, and major modifications (particularly in areas of consensus) require upstream discussions on public channels, such as mailing lists or PR review clubs.

---

## Other Bitcoin implementations

Although marginal in terms of adoption, other clients do exist. The main one is **Bitcoin Knots**, developed by Luke Dashjr, a fork of Bitcoin Core that incorporates additional options and a more conservative approach to development. These include tighter restrictions on transaction formats.

![Bitcoin Knots](https://via.placeholder.com/600x300?text=Bitcoin+Knots)

We can also mention:

- **Libbitcoin:** a modular C++ library developed by Amir Taaki and maintained by Eric Voskuil;
- **Bcoin:** a JavaScript implementation, no longer actively maintained;
- **BTCD/btcsuite:** an implementation in Go.

These projects contribute to the diversity of the ecosystem, but their adoption remains very limited, making it difficult for Bitcoin Core to evolve independently.

---

## The power of Core developers

You might think that Bitcoin Core developers have direct control over Bitcoin, but this is not the case. They can't impose a change to the protocol. Their role is to **propose code**. It is up to each user, via their node, to decide whether or not to use this code.

This means that if a change in Bitcoin Core does not meet consensus, it can be ignored by the nodes, either by not updating Bitcoin Core or by simply changing the implementation. Conversely, if a feature desired by users is blocked in the Core development process, it is always possible to switch to another implementation or fork the project.

As we'll discuss later in this course, it's the nodes, according to their **economic weight** (i.e., the merchants), that confer utility on a version of the protocol (and therefore on the corresponding currency), by accepting units that respect its rules. The real power of governance over Bitcoin, therefore, lies with these merchants, not the developers.
```

You can save the content above as `BTC-introduction.md`. The placeholder images (via.placeholder.com) are included as examples—replace them with actual paths or URLs as needed.