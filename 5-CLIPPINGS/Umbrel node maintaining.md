---
title: "Overview of available applications"
source: "https://planb.academy/en/courses/3cd9cb94-82e8-417a-9c5a-02afc2589426/maintaining-your-umbrel-node-06d77d09-bf24-4555-b2ba-c08bbda477c7"
author:
published:
created: 2026-04-19
description: "Umbrel offers an extensive application store. As you'll see, there are many tools related to Bitcoin, but also a wide variety of applications in very different fields: self-hosting solutions for servi..."
tags:
  - "clippings"
---
CourseOverviewDiplomaCredits

[Course](https://planb.academy/courses/3cd9cb94-82e8-417a-9c5a-02afc2589426/06d77d09-bf24-4555-b2ba-c08bbda477c7) [Overview](https://planb.academy/courses/3cd9cb94-82e8-417a-9c5a-02afc2589426/overview) [Diploma](https://planb.academy/courses/3cd9cb94-82e8-417a-9c5a-02afc2589426/retake-exam) [Credits](https://planb.academy/courses/3cd9cb94-82e8-417a-9c5a-02afc2589426/credits)

To kick off this final section, and before moving on to more advanced theory, I'd like to examine the best practices and concrete actions you can take once your Umbrel node is installed, synchronized, and correctly configured in this short chapter. How do you maintain it on a daily basis?

### Keeping equipment healthy

A reliable node starts with stable hardware. Ensure the machine housing your node is properly ventilated, dust-free, and installed in a dry environment, away from any sources of heat and humidity. Avoid cramming it into a confined space and opt for a well-ventilated location.

On Raspberry Pi and mini-PCs, dust eventually clogs the heatsinks, raising the temperature and leading to throttling (voluntary limitation of resource use), which in turn results in a drop in your node's efficiency. That's why I recommend cleaning the air intake and fan periodically, ideally every few months.

Ensure you use a high-quality power supply, as unstable voltage can lead to system corruption and even pose a fire hazard. Ideally, you should use the original power supply supplied by the manufacturer of your machine. Beware, too, of overheating due to the Joule effect on power strips: always respect the maximum permissible power and never connect several power strips in cascade.

I also recommend investing in a UPS. This protects your node from sudden shutdowns, enables Umbrel to shut down cleanly in the event of an outage, and ensures continuity of operation during micro outages or short-term failures.

On the storage side, keep an eye on progress: if the disk is approaching saturation, consider freeing up space (uninstall unused apps, adjust the indexer settings) or migrate to a larger SSD. The disadvantage of a full Bitcoin node is that its storage requirements increase continuously, as a new block is generated every 10 minutes and old blocks can't be deleted (unless the node is pruned). I therefore advise you to plan for a sufficiently large capacity when purchasing your hardware (2 TB minimum).

### Update

Node updates are important for three main reasons: first, security (vulnerability patches, network hardening, and DoS protection); second, compatibility (relay policy changes, format changes, and protocol upgrades); and third, reliability and performance (bug fixes, resource consumption, and other improvements). So check periodically that UmbrelOS and your apps are up to date:

- To update the system: Open the settings menu, then click on the " *Check for Update* " button next to the " *UmbrelOS* " parameter.
- To update applications: Go to the App Store. If any of your applications require updating, a button with a red bubble will appear in the top right-hand corner of the Interface. Simply click on it, then update each application.

Perform this operation regularly to keep your operating system and applications up to date.

### Backups

If you only use your Bitcoin node to validate and distribute your transactions, but your wallets are managed outside Umbrel (e.g., with a Hardware wallet and Sparrow wallet), there's nothing to back up directly to Umbrel. In this case, the essential backup remains that of the recovery phrase and Descriptor of your external wallet, and this applies whether you use your own node or not. So nothing changes from your previous configuration.

On the other hand, depending on the additional applications you use on Umbrel, further backups may be required. This is particularly the case if you operate a Lightning node on Umbrel. In this case, it is absolutely essential to back up the seed supplied when you installed your Lightning node. In addition to the seed, you need an up-to-date ***Static Channel Backup (SCB)*** to be able to restore your Lightning node in the event of a problem. SCB allows you to recover your funds by forcibly closing channels. If either the seed or the SCB is missing, it is impossible to restore a Lightning node.

Umbrel also offers the option of automatically and dynamically backing up this SCB on their servers, via Tor, to ensure that an up-to-date file is always available. In this case, only the seed is needed to restore the node.

We'll revisit these aspects in detail in the next LNP202 course.

### Day-to-day operational safety

In terms of security, use a long, unique, and random password for Interface Umbrel, and remember to activate two-factor authentication (2FA). For applications that offer both password and 2FA protection, always activate both and change the default passwords.

Never expose the dashboard to the Internet without using a secure gateway (such as a VPN, Tor, or local access only). Limit the number of applications you install, and regularly delete those you no longer need, to reduce the attack surface.

To deepen your knowledge of computer security in general, I highly recommend you check out this other free course:

### Diagnosis and self-help

In the event of a bug on your Umbrel, first generate a diagnostics bundle via the troubleshooting section of UmbrelOS or the application concerned, then cleanly restart the application. If necessary, also attempt a full system reboot.

If the problem persists, I recommend that you [join the Umbrel user community on their Discord](https://discord.gg/efNtFzqtdx). Begin by doing a search to determine if anyone has already encountered the same difficulty and found a solution. If not, you can post a message in the `general-support` channel. You can also use [the Umbrel forum](https://community.umbrel.com/).

These areas will enable you not only to follow security announcements and updates, but also to ask questions and, ultimately, to help other users. It's often in these exchanges that best practices are discovered.

With these simple habits, your Umbrel node will remain stable, safe, and useful, both for you and for the Bitcoin network.

Quiz

Quiz

btc2025.1

What are the three main benefits of regular OS and app updates?