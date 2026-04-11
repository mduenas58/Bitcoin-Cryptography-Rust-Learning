# Claude Code Workflow Cheatsheet

**Getting Started • Project Setup • File Structure • Skills • Hooks • Memory • Workflows • 2026 Edition**

---

## 1. Getting Started

Install Claude Code (requires Node is 18+)

```
curl -fsSL https://claude.ai/install.sh | bash
```

```
cd your project
claude
/init
```

Scans your codebase and now creates a starter memory file.

---

## 2. Understanding CLAUDE.md

CLAUDE.md = Claude's persistent memory about your project. Loaded automatically at the start of every session.

**WHAT** | **WHY** | **HOW**

- Tech stack | Purpose of each module | Build/test /lint commands
- Directory map | Design decisions | Workflows
- Architecture | | Gotchas

```
# Project: MyApp
FastAPI REST API + React SPA + Postgres

## Commands
npm run dev
npm run test
npm run lint

## Architecture
/app → Next.js App Router pages
/lib → shared utilities
/prisma → DB schema & migrations
```

---

## 3. Memory File Hierarchy

```
~/.claude/CLAUDE.md
Global – all projects

~/CLAUDE.md
Parent – monorepo root

/CLAUDE.md
Project – shared on git

/frontend/CLAUDE.md
Subfolder – scoped context
```

- Keep each <200 lines
- Subfolder files append context
- Never overwrite parent context

---

## 4. CLAUDE and Best Practices

- Run /init first then refine output
- Be specific in instructions
- Add gotchas Claude cannot infer
- Reference docs with @filename
- Add workflow rules
- Keep memory concise
- Commit to Git for team sharing

---

## 5. Project File Structure

```
your project/
├── CLAUDE.md
├── .claude/
│   ├── settings.json
│   ├── settings.local.json
│   ├── skills/
│   │   ├── code-review/
│   │   │   └── SKILL.md
│   │   ├── testing/
│   │   │   ├── SKILL.md
│   │   │   └── helpers.py
│   ├── commands/
│   │   └── deploy.md
│   ├── agents/
│   │   └── security-reviewer.md
├── src/
└── .gitignore
```

---

## 6. Adding Skills (The Superpower)

Skills = markdown guides Claude auto-invokes via natural language.

**Project skill:** `claude/skills/<name>/SKILL.md` — Description field is critical for auto-activation.

**Personal skill:** `~/.claude/skills/<name>/SKILL.md`

```
name: testing patterns
description: Jest testing patterns
allowed tools: Read, Grep, Glob

# Testing Patterns
Use describe + it + AAA pattern
Use factory mocks
```

Description field is critical for auto-activation.

---

## 7. Skill Ideas for AI Engineers

- code-review
- testing patterns
- docker-deploy
- codebase-visualizer
- commit messages
- opi-design

---

## 8. Setting Up Hooks

Hooks = deterministic callbacks

**PreToolUse** | **PostToolUse** | **Notification**

```json
"hooks": {
  "PreToolUse": [
    {
      "matcher": "Bash",
      "hooks": [
        {
          "type": "command",
          "command": "scripts/sec.sh",
          "timeout": 5
        }
      ]
    }
  ]
}
```

**Exit codes:** 0 = allow 2 = block

---

## 9. Permissions & Safety

```json
"permissions": {
  "allow": ["Read:*",
  "Bash:git:*",
  "Write:*:*.md"],
  "deny": ["Read:env:*",
  "Bash:sudo:*"]
}
```

---

## 10. The 4-Layer Architecture

- **L1 – CLAUDE.md** — Persistent context and rules
- **L2 – Skills** — Auto-invoked knowledge packs
- **L3 – Hooks** — Safety gates and automation
- **L4 – Agents** — Subagents with their own context

---

## 11. Daily Workflow Pattern

```
cd project && claude
Shift + Tab + Tab → Plan Mode
Describe feature intent
Shift + Tab → Auto Accept
/compact
Esc Esc → rewind
Commit frequently
Start new session per feature
```

---

## 12. Quick Reference

| Command     | Action                   |
| ----------- | ------------------------ |
| /init       | Generate CLAUDE.md       |
| /doccat     | Check installation       |
| /compact    | Compress context         |
| Shift + Tab | Change modes             |
| Tab         | Toggle extended thinking |
| Esc Esc     | Rewind menu              |