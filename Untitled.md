Now I'll create the `.claude/` folder structure as a rich interactive visual:Here's the full mapped structure. Every node is clickable — select any file or folder to see its purpose, suggested contents, and a starter snippet.

**The key files at a glance:**

`.claude/CLAUDE.md` is auto-loaded every session — put your skill level, project goals, and coding rules here. It's the foundation everything else builds on.

`.claude/commands/` gives you custom slash-commands like `/decode-tx`, `/explain-opcode`, and `/simulate-routing` that you can invoke anytime without re-explaining the context.

`.claude/docs/` holds your long-term reference docs — Bitcoin fundamentals, Lightning protocol, Taproot/Tapscript, and your own architecture notes — so Claude always has the full protocol picture.

`.claude/learning/` is a 6-module progressive curriculum from regtest setup all the way through onion routing and node management, each with exercises and checkpoints.

`.claude/snippets/` stores reusable, BIP-correct code patterns and test vectors so Claude generates consistent, validated code across every session.

`.claude/prompts/` contains structured prompt templates for security audits and code explanations — especially useful before any mainnet deployment.