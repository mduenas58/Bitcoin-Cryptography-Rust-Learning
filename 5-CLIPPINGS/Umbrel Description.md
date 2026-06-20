---
title: "Overview of available applications"
source: "https://planb.academy/en/courses/3cd9cb94-82e8-417a-9c5a-02afc2589426/overview-of-available-applications-2a5ccfbe-0b17-44c9-863c-b7e8cb4b4594"
author:
published:
created: 2026-04-19
description: "Umbrel offers an extensive application store. As you'll see, there are many tools related to Bitcoin, but also a wide variety of applications in very different fields: self-hosting solutions for servi..."
tags:
  - "clippings"
---
CourseOverviewDiplomaCredits

[Course](https://planb.academy/courses/3cd9cb94-82e8-417a-9c5a-02afc2589426/2a5ccfbe-0b17-44c9-863c-b7e8cb4b4594) [Overview](https://planb.academy/courses/3cd9cb94-82e8-417a-9c5a-02afc2589426/overview) [Diploma](https://planb.academy/courses/3cd9cb94-82e8-417a-9c5a-02afc2589426/retake-exam) [Credits](https://planb.academy/courses/3cd9cb94-82e8-417a-9c5a-02afc2589426/credits)

Umbrel offers an extensive application store. As you'll see, there are many tools related to Bitcoin, but also a wide variety of applications in very different fields: self-hosting solutions for services and files, productivity applications, more general financial tools, media management, network security and administration, development, artificial intelligence, social networking, and even home automation.

In this BTC 202 course, we'll be concentrating exclusively on Bitcoin-related applications. However, feel free to explore the rest of the catalog for tools that may be of use to you.

Of course, it would be impossible to list all the Bitcoin applications here. In this chapter, I'd like to introduce you to the essential tools that will facilitate and enrich your daily use of Bitcoin.

### Mempool.space

In the daily use of Bitcoin, if there's one tool that's truly indispensable, it's the block explorer. Whether accessible online or installed locally, it transforms Blockchain's raw data into a structured, clear, and easy-to-read format. It also features a search engine that allows users to quickly locate a specific block, transaction, or address.

In concrete terms, the explorer lets you estimate the fees required for your transaction to be included in a block, then track its progress: find out whether it is likely to be included in the near future, depending on the fee market, and finally confirm that it has indeed been included in a block. It also offers the possibility of analyzing your past transactions and consulting their history. In short, it's the bitcoiner's Swiss Army Knife.

As mentioned previously, an explorer can be hosted online on a website or run locally on your machine. A major disadvantage of online services is that they can compromise your privacy. Without VPN or Tor, the server hosting the explorer can link your IP address to the transactions you're viewing, which can provide an ideal entry point for chain analysis.

What's more, your Internet Service Provider (ISP) may know that you're viewing a particular transaction via the block explorer site. This also raises a question of trust: you must rely on the online service to provide you with accurate information about your transactions, without being able to verify its veracity yourself.

That's why it's always best to use your own local block explorer. This way, no data related to your search activity will leak out, since all queries are processed directly on a machine you control, without passing through the Internet. What's more, a local explorer relies on data from your own Bitcoin node, which you have validated yourself, according to your own rules, and which you can trust.

Umbrel offers several block explorers:

- Mempool.Space
- Bitfeed
- BTC RPC Explorer

I'm particularly fond of Mempool.Space, which I've installed on my node. Please note: to use most block explorers on Umbrel, an address indexer is required. You therefore need the Bitcoin Node (or Bitcoin Knots) application, which has a 100% synchronized blockchain, as well as an indexer such as Electrs or Fulcrum, which is also 100% synchronized.

Once the application is installed, simply open it to access your own explorer.

To learn more about using the Mempool.Space explorer, I recommend this comprehensive tutorial:

[![mempool-space](https://planb.academy/cdn/tutorials/privacy/mempool-space/assets/logo.webp?c=f9da2097c70a2bfee9bbdac6d7a026585314d182&w=160)](https://planb.academy/tutorials/privacy/explorer/mempool-space-f3e468a1-92f1-43ce-b2e4-c3298fa0e02f)

[Mempool](https://planb.academy/tutorials/privacy/explorer/mempool-space-f3e468a1-92f1-43ce-b2e4-c3298fa0e02f)

### Lightning Node

Now that you have your own Bitcoin node, you can also set up your own Lightning node to carry out off-chain transactions, without relying on a third-party infrastructure.

Umbrel offers a number of applications to help you get your Lightning node up and running. You can already choose between two main implementations:

- LND, via the *Lightning Node* application;
- Core Lightning.

[![umbrel-lnd](https://planb.academy/cdn/tutorials/node/umbrel-lnd/assets/logo.webp?c=e7bf15095f117cc67977d227e292bc2e7887dbcd&w=160)](https://planb.academy/tutorials/node/lightning-network/umbrel-lnd-b12e0b5b-12ff-45f1-978e-62f4b4a8ba16)

[Umbrel LND](https://planb.academy/tutorials/node/lightning-network/umbrel-lnd-b12e0b5b-12ff-45f1-978e-62f4b4a8ba16)

You can then administer your node from the main Interface, or, for even greater functionality and advanced options, install *Ride The Lightning* or *ThunderHub*. These tools will provide you with a much more comprehensive web-based interface management system for your node.

[![ride-the-lightning](https://planb.academy/cdn/resources/projects/ride-the-lightning/assets/logo.webp?c=3fb8a2f1e1b5f20f586f71432b8afa43cf2778f7&w=160)](https://planb.academy/tutorials/node/lightning-network/ride-the-lightning-ca007688-0653-490c-8349-81d330d744b5)

[Ride The Lightning (RTL)](https://planb.academy/tutorials/node/lightning-network/ride-the-lightning-ca007688-0653-490c-8349-81d330d744b5)

[![thunderhub](https://planb.academy/cdn/tutorials/node/thunderhub/assets/logo.webp?c=74a4a3a621bf57d742036d717321cd03f42def92&w=160)](https://planb.academy/tutorials/node/lightning-network/thunderhub-16909a39-2484-408e-a118-4e34e249bb9a)

[ThunderHub](https://planb.academy/tutorials/node/lightning-network/thunderhub-16909a39-2484-408e-a118-4e34e249bb9a)

Finally, I recommend the *Lightning Network+* application, which allows you to find peers with whom to open channels, enabling both outgoing and incoming cash transactions.

Thanks to Umbrel, managing a personal Lightning node is simplified, but it nonetheless remains relatively complex. This is why I recommend that you take the LNP 202 course, which is the logical continuation of the BTC 202 course, and in which I guide you step by step through the setup and management of your Lightning node on Umbrel.

### Tailscale

Another application I particularly like on Umbrel is Tailscale. It's a VPN application designed to simplify the creation of secure networks between multiple devices, wherever they may be in the world. Unlike traditional VPNs, which rely on centralized servers, Tailscale utilizes the WireGuard protocol to establish end-to-end encrypted connections between your various machines. This means you can deploy a working VPN in just a few minutes, without the need for complicated network configurations.

On Umbrel, Tailscale installation connects your Bitcoin node to your own virtual private network. Once configured, your node obtains a private Tailscale IP address, accessible only from other devices connected to the same Tailscale network (such as computers, smartphones, and tablets). This connection is end-to-end encrypted and does not pass through an unprotected public network, significantly enhancing security compared to an unencrypted connection.

- You can administer the Interface Umbrel or access the applications linked to your node (such as Mempool, Ride The Lightning, ThunderHub...) from anywhere, as if you were on the same local network, without exposing ports on the Internet and without going through Tor, which is very slow;
- You can connect to your Electrum server (Electrs or Fulcrum) or directly to Bitcoin Core via your VPN, bypassing Tor. This provides a secure connection, comparable to using Tor, but with much higher speed and reduced latency. In short, you retain the privacy and security benefits of Tor while enjoying the speed of a Clearnet connection. For an On-Chain wallet, this gain may seem marginal, but if you're planning to set up your own Lightning node at a later date, the difference is considerable. Indeed, making payments via your node on the move on Tor is extremely slow due to the numerous exchanges required, whereas with Tailscale, it works perfectly.
- No need to configure NAT rules, open ports, or set up a conventional VPN server. Once the application is installed on Umbrel and your devices, the network is automatically established.

Tailscale on Umbrel is therefore a very interesting solution if you want to access your node from anywhere in the world in a secure, high-performance, and easy-to-configure way, without sacrificing privacy or security.

To install and configure Tailscale on your Umbrel, see this tutorial, section 4: " *Using Tailscale on Umbrel* ":

[![tailscale](https://planb.academy/cdn/tutorials/computer-security/tailscale/assets/logo.webp?c=c5c764c02b784c73c9261cc832a6a97a592b8faf&w=160)](https://planb.academy/tutorials/computer-security/communication/tailscale-9acbd7de-04d9-40f6-ab80-35f0dfedb632)

[Tailscale](https://planb.academy/tutorials/computer-security/communication/tailscale-9acbd7de-04d9-40f6-ab80-35f0dfedb632)

### Nostr

Nostr, an acronym for " *Notes and Other Stuff Transmitted by Relays* ", is an open, decentralized protocol designed to enable messages to be published and exchanged on the Internet without depending on a centralized platform. Each user has a pair of cryptographic keys: the public key (`npub`), which serves as an identifier, and the private key (`nsec`), which is used to sign messages and guarantee their authenticity.

Messages are transmitted via a network of independent relays. This distributed architecture makes Nostr resistant to censorship: no single server controls access or distribution, and a user can connect to as many relays as they wish.

This protocol is very popular within the Bitcoin community because, like Bitcoin, Nostr addresses issues of digital sovereignty and data control. Its creator, Fiatjaf, is a developer already recognized in the ecosystem for his numerous contributions.

With your Umbrel, you can optimize your use of Nostr. By installing the ***Nostr Relay*** application, you can host your own private relay directly on your machine, ensuring that all your posts and interactions on Nostr are saved locally and can't be lost through deletion by public relays.

Nostr clients ***noStrudel*** or ***Snort*** are also available on Umbrel. Thanks to these applications, you can publish, read, search for profiles, and interact with the Nostr ecosystem directly from the Interface web on your Umbrel.

Finally, there is the ***Nostr wallet Connect*** application on Umbrel, which allows native Lightning payments within Nostr. Specifically, you can link your future Lightning node to your Nostr clients to send micro-payments, called " *zaps* ", to reward content or interact in a monetized way, without going through a third-party service. These payments are sent directly from your personal node via your channels.

To find out how to use all these applications, I recommend you take a look at this complete tutorial:

[![umbrel-nostr](https://planb.academy/cdn/resources/projects/umbrel/assets/logo.webp?c=0a3d6a79c6727d6dfaa5605f6c73427ab321df7d&w=160)](https://planb.academy/tutorials/node/others/umbrel-nostr-7ae147e8-f5cd-46e1-861b-17c2ea1e08fd)

[Umbrel Nostr](https://planb.academy/tutorials/node/others/umbrel-nostr-7ae147e8-f5cd-46e1-861b-17c2ea1e08fd)

### BTCPay Server

BTCPay Server is a free, open-source payment processor that enables you to accept payments via Bitcoin and Lightning Network without intermediaries, while retaining self-custody of funds.

BTCPay Server's architecture is based on a Bitcoin node and, for Lightning, on a compatible implementation (LND, Core Lightning...), making it one of the only totally non-custodial PoS solutions. It's also the most comprehensive software for tracking and accounting.

If you own a business and would like to accept bitcoin payments directly via your Umbrel node, the BTCPay Server application is ideal for you. To find out more on this subject, I recommend you consult the following resources:

- The BIZ 101 course on using Bitcoin in your business:
- The POS 305 course on using BTCPay Server:
- The BTCPay Server tutorial:

[![btcpay-server](https://planb.academy/cdn/resources/projects/btcpay-serveur/assets/logo.webp?c=0a8505e27c3f1ea91e5bb5396b73a77ce8aa6932&w=160)](https://planb.academy/tutorials/business/point-of-sale/btcpay-server-928eb01e-824b-4b57-a3e8-8727633beddc)

[BTCPay Server](https://planb.academy/tutorials/business/point-of-sale/btcpay-server-928eb01e-824b-4b57-a3e8-8727633beddc)

Quiz

Quiz

btc2024.3

Which Umbrel application lets you manage your Lightning node with an advanced Interface?