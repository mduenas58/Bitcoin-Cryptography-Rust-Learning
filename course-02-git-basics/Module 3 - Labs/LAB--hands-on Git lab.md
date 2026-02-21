Below is a **comprehensive, hands-on Git lab** built around a realistic DevOps scenario:

> Two developers collaborating on a Node.js website using modern Git workflows, pull requests, branching strategy, CI, and conflict resolution.

This lab simulates real-world team collaboration and is portfolio-ready.

---

# 🧪 Git Collaboration Lab

## Scenario: Two Developers Building a Node.js Website

### 👥 Team

- Developer A → Feature development (UI + routes)
    
- Developer B → Backend logic + API integration
    

### 🏗 Project

A simple Node.js Express website with:

- Home page
    
- About page
    
- API endpoint (`/api/status`)
    
- Basic logging middleware
    

---

# 🎯 Learning Objectives

By the end of this lab, you will have practiced:

- Git branching strategy
    
- Feature branches
    
- Pull requests
    
- Merge conflicts
    
- Rebasing vs merging
    
- Code review workflow
    
- Git hooks
    
- CI integration
    
- Tagging & release versioning
    

---

# 🛠 Environment Setup

## Prerequisites

- Git installed
    
- Node.js 18+
    
- GitHub account
    
- Code editor
    

---

# 📁 Phase 1 — Project Initialization (Developer A)

## Step 1: Create Repository

```bash
mkdir node-website
cd node-website
git init
```

Initialize Node project:

```bash
npm init -y
npm install express
```

Create structure:

```
node-website/
 ├── app.js
 ├── routes/
 ├── package.json
 └── .gitignore
```

`.gitignore`:

```
node_modules/
.env
```

Minimal `app.js`:

```js
const express = require('express');
const app = express();

app.get('/', (req, res) => {
  res.send('Welcome to the website');
});

app.listen(3000, () => {
  console.log('Server running on port 3000');
});
```

Commit:

```bash
git add .
git commit -m "Initial Node.js Express setup"
```

---

## Step 2: Create Remote Repository

Push to GitHub:

```bash
git remote add origin <repo-url>
git branch -M main
git push -u origin main
```

---

# 🌿 Phase 2 — Branching Strategy

Use a simplified Git Flow:

- `main` → production-ready
    
- `develop` → integration branch
    
- `feature/*` → feature branches
    

Create develop:

```bash
git checkout -b develop
git push -u origin develop
```

---

# 👨‍💻 Phase 3 — Parallel Development

---

# 🔹 Developer A Task

Create feature branch:

```bash
git checkout -b feature/about-page develop
```

Add:

```js
app.get('/about', (req, res) => {
  res.send('About page');
});
```

Commit:

```bash
git commit -am "Add about route"
```

Push:

```bash
git push -u origin feature/about-page
```

Open Pull Request → merge into `develop`.

---

# 🔹 Developer B Task

Developer B clones repo:

```bash
git clone <repo-url>
cd node-website
git checkout develop
```

Create feature branch:

```bash
git checkout -b feature/status-api
```

Add:

```js
app.get('/api/status', (req, res) => {
  res.json({ status: 'OK' });
});
```

Commit & push.

Open Pull Request → merge into `develop`.

---

# ⚠️ Phase 4 — Merge Conflict Simulation

Now both developers modify the same section.

Both edit `/` route message:

Developer A changes:

```js
res.send('Welcome to our platform');
```

Developer B changes:

```js
res.send('Welcome to version 2');
```

When merging into `develop`, conflict occurs.

---

## Resolving Conflict

Git shows:

```
<<<<<<< HEAD
Welcome to our platform
=======
Welcome to version 2
>>>>>>> feature/status-api
```

Team agrees final message:

```js
res.send('Welcome to our platform v2');
```

Resolve:

```bash
git add app.js
git commit
git push
```

Lesson:  
Conflict resolution requires communication, not just commands.

---

# 🔄 Phase 5 — Rebasing Workflow (Advanced)

Developer B rebases feature branch:

```bash
git checkout feature/status-api
git rebase develop
```

Resolve conflicts during rebase if needed.

Push with force (safe version):

```bash
git push --force-with-lease
```

Discussion:

- Rebase keeps history linear
    
- Merge preserves historical branch context
    

DevOps teams must understand both.

---

# 🧪 Phase 6 — Git Hooks (Quality Control)

Add pre-commit hook:

`.git/hooks/pre-commit`

```bash
#!/bin/sh
npm test
```

Make executable:

```bash
chmod +x .git/hooks/pre-commit
```

Now commits fail if tests fail.

---

# 🤖 Phase 7 — CI Integration

Add GitHub Actions workflow:

`.github/workflows/ci.yml`

```yaml
name: Node CI

on:
  push:
    branches: [develop]
  pull_request:
    branches: [develop]

jobs:
  build:
    runs-on: ubuntu-latest

    steps:
      - uses: actions/checkout@v3
      - uses: actions/setup-node@v4
        with:
          node-version: 18
      - run: npm install
      - run: npm test
```

Now:

- Every PR runs tests
    
- Broken code cannot merge safely
    

---

# 🏷 Phase 8 — Release Management

Merge `develop` into `main`:

```bash
git checkout main
git merge develop
```

Tag release:

```bash
git tag -a v1.0.0 -m "First stable release"
git push origin v1.0.0
```

Production branch is now stable.

---

# 🔐 Phase 9 — Hotfix Scenario

Critical bug found in production.

Create hotfix branch from main:

```bash
git checkout -b hotfix/fix-home-message main
```

Fix issue.

Merge into:

- main
    
- develop
    

Tag:

```bash
git tag -a v1.0.1 -m "Hotfix release"
```

---

# 📊 Phase 10 — DevOps Best Practices Reflection

This lab demonstrates:

- Branching models
    
- Parallel collaboration
    
- Pull requests
    
- Conflict resolution
    
- Rebasing vs merging
    
- CI enforcement
    
- Tagging strategy
    
- Production hotfix workflow
    

---

# 🧠 Advanced Extensions (Optional)

Add:

- Conventional commit messages
    
- Commit linting
    
- Semantic versioning automation
    
- Dockerfile
    
- Podman deployment on **Fedora Linux**
    
- Protected branches on GitHub
    
- Required PR reviews
    
- Codeowners file
    

---

# 📦 Portfolio Enhancement

Turn this into a repo:

`git-collaboration-lab-node`

Include:

- README with diagrams
    
- Conflict screenshots
    
- Rebase example
    
- CI badge
    
- Branch strategy explanation
    

This signals strong Git + DevOps fundamentals.

---

If you'd like next, I can:

- Turn this into a downloadable workshop-style curriculum
    
- Add a Kubernetes deployment layer
    
- Or create a “Git disaster recovery” advanced lab
    

What level are you aiming for — junior DevOps, mid-level, or platform engineer?

---

Below is a **workshop-style curriculum** you can turn into a downloadable PDF, internal training doc, or GitHub workshop repository.

It’s designed specifically for a **junior DevOps audience**, with structured labs, timing, instructor notes, checkpoints, and deliverables.

No fluff — this mirrors how real teams collaborate.

---

# 🧑‍💻 Workshop Title

# Git Collaboration & CI Fundamentals for Junior DevOps Engineers

### Scenario: Two Developers Building a Node.js Website

---

# 🎯 Workshop Overview

## Duration Options

- 1-Day Intensive (6–7 hours)
    
- 2 Half-Day Sessions
    
- Self-paced (1 week)
    

## Target Audience

Junior DevOps engineers who:

- Know basic Git commands
    
- Understand basic Node.js
    
- Want real-world workflow experience
    

---

# 📦 Learning Outcomes

By the end of this workshop, participants will:

- Implement a professional branching strategy
    
- Handle merge conflicts confidently
    
- Understand rebase vs merge
    
- Work with pull requests
    
- Integrate CI using GitHub Actions
    
- Perform release tagging
    
- Execute a hotfix workflow
    
- Understand Git from a DevOps perspective
    

---

# 🛠 Technical Stack

- Git
    
- GitHub
    
- Node.js 18+
    
- Express
    
- GitHub Actions
    
- Linux environment (recommended: **Fedora Linux**)
    

---

# 📚 Module 1 — Project Setup (45 minutes)

## Objective

Initialize a real Node.js project and push to GitHub.

---

## Exercise 1.1 — Initialize Project

Create:

```bash
mkdir node-devops-lab
cd node-devops-lab
git init
npm init -y
npm install express
```

Create minimal Express server.

---

## Exercise 1.2 — First Commit

Add `.gitignore`:

```
node_modules/
.env
```

Commit:

```bash
git add .
git commit -m "Initial Express setup"
```

Push to GitHub.

---

### ✅ Checkpoint

- Repo exists remotely
    
- `main` branch pushed
    
- Server runs locally
    

---

# 🌿 Module 2 — Branching Strategy (60 minutes)

## Objective

Introduce team collaboration workflow.

---

## Instructor Explanation

Introduce simple Git Flow:

- `main` → production
    
- `develop` → integration
    
- `feature/*` → features
    
- `hotfix/*` → production fixes
    

---

## Exercise 2.1 — Create develop branch

```bash
git checkout -b develop
git push -u origin develop
```

---

## Exercise 2.2 — Feature Branch Creation

Developer A:

```
feature/about-page
```

Developer B:

```
feature/status-api
```

Participants work in pairs.

---

### ✅ Checkpoint

Both features exist as PRs.

---

# 🤝 Module 3 — Pull Requests & Code Review (60 minutes)

## Objective

Simulate real collaboration.

---

Each participant:

- Opens a Pull Request
    
- Reviews partner’s PR
    
- Leaves comments
    
- Requests change
    
- Approves
    

---

## Instructor Discussion

Cover:

- Why PRs matter
    
- Why direct pushes to main are dangerous
    
- Importance of review culture
    

---

### ✅ Checkpoint

Features merged into `develop`.

---

# ⚠️ Module 4 — Merge Conflict Simulation (60 minutes)

## Objective

Build confidence in resolving conflicts.

---

Both developers modify same route.

When merging → conflict appears.

Participants:

- Inspect conflict markers
    
- Discuss resolution
    
- Resolve manually
    
- Commit resolution
    

---

## Instructor Emphasis

Conflict resolution is:

- Communication
    
- Context awareness
    
- Not panic-driven
    

---

### ✅ Checkpoint

Conflict resolved successfully.

---

# 🔄 Module 5 — Rebase vs Merge (Advanced Junior Topic) (45 minutes)

## Objective

Understand clean history vs contextual history.

---

Participants:

```bash
git checkout feature/status-api
git rebase develop
```

Discuss:

- When to use rebase
    
- When to avoid it
    
- Why force push must be careful
    

Command:

```bash
git push --force-with-lease
```

---

### ✅ Checkpoint

Participants understand difference conceptually.

---

# 🤖 Module 6 — CI Integration (90 minutes)

## Objective

Introduce DevOps mindset.

---

Create:

`.github/workflows/ci.yml`

Include:

- Node setup
    
- Install
    
- Test (add simple test)
    

Add basic test example:

```js
if (1 + 1 !== 2) {
  throw new Error("Math broken");
}
```

Push → observe CI pipeline run.

---

## Instructor Discussion

Explain:

- Why CI protects develop
    
- How pipelines prevent broken merges
    
- Cultural shift from manual testing
    

---

### ✅ Checkpoint

CI runs successfully on pull request.

---

# 🏷 Module 7 — Release Management (45 minutes)

## Objective

Simulate production release.

---

Merge develop → main.

Tag release:

```bash
git tag -a v1.0.0 -m "First release"
git push origin v1.0.0
```

Explain semantic versioning.

---

### ✅ Checkpoint

Tag visible in GitHub releases.

---

# 🚑 Module 8 — Hotfix Scenario (45 minutes)

## Objective

Simulate production emergency.

---

Bug found in main.

Create:

```bash
git checkout -b hotfix/fix-issue main
```

Fix → merge into:

- main
    
- develop
    

Tag:

```bash
git tag -a v1.0.1 -m "Hotfix"
```

---

### ✅ Checkpoint

Participants understand production-safe fixes.

---

# 📊 Module 9 — DevOps Reflection & Architecture (30 minutes)

Participants document:

- Branching model
    
- CI flow
    
- Release workflow
    
- Hotfix strategy
    
- What went wrong
    
- What improved collaboration
    

---

# 🧠 Optional Advanced Extensions

If time allows:

- Protect branches in GitHub
    
- Require PR reviews
    
- Add Dockerfile
    
- Deploy with Podman on Fedora
    
- Add linting
    
- Implement commit message standard
    
- Add CODEOWNERS file
    

---

# 📦 Workshop Deliverables (Portfolio Ready)

Participants leave with:

- Fully working Node.js repo
    
- CI-enabled project
    
- Branching strategy documented
    
- Tagged release history
    
- Merge conflict experience
    
- Hotfix workflow experience
    

---

# 🎓 Evaluation Criteria (For Instructors)

Participants demonstrate ability to:

- Use feature branches properly
    
- Resolve conflicts confidently
    
- Explain merge vs rebase
    
- Configure CI workflow
    
- Perform release tagging
    
- Execute hotfix safely
    

---

# 🧩 Instructor Materials Section

You can package this workshop as:

- PDF curriculum
    
- Slide deck
    
- GitHub template repository
    
- Recorded demo
    
- Internal training program
    

---

# 🏁 Outcome for Junior DevOps

After this workshop, participants will:

- Think in workflows, not just commands
    
- Understand Git as infrastructure safety tool
    
- Respect CI as quality enforcement
    
- Recognize release discipline
    
- Be prepared for real DevOps team collaboration
    

---

If you’d like next, I can:

- Format this as a clean PDF-ready document structure
    
- Create a slide deck outline
    
- Add Kubernetes deployment extension
    
- Or build an instructor answer key
    

What format are you planning to distribute this in?

---

Excellent — this is what makes the workshop feel **real-world and production-grade**.

Below is a **professional GitHub lab repository structure** designed to pair with your Instructor Manual and simulate two developers collaborating on a Node.js web application with CI.

---

# 📦 Repository Name

```
nodejs-git-collaboration-lab
```

---

# 🌳 Full Repository Structure

```
nodejs-git-collaboration-lab/
│
├── README.md
├── CONTRIBUTING.md
├── CODEOWNERS
├── .gitignore
│
├── .github/
│   └── workflows/
│       └── ci.yml
│
├── app/
│   ├── package.json
│   ├── package-lock.json
│   ├── server.js
│   │
│   ├── routes/
│   │   └── users.js
│   │
│   ├── controllers/
│   │   └── userController.js
│   │
│   ├── services/
│   │   └── userService.js
│   │
│   └── tests/
│       └── user.test.js
│
├── docs/
│   ├── LAB_GUIDE.md
│   ├── BRANCHING_STRATEGY.md
│   ├── MERGE_CONFLICT_SCENARIOS.md
│   └── CI_PIPELINE_EXPLANATION.md
│
└── scripts/
    ├── setup.sh
    └── seed-data.js
```

---

# 📘 What Each Section Teaches

## 🔹 `app/`

Real Node.js service for hands-on Git workflows.

Use:

- Express server
    
- Jest tests
    
- Basic REST endpoint (`/users`)
    
- Simulated service layer
    

This allows:

- Feature branches
    
- Refactors
    
- Merge conflicts
    
- Broken CI scenarios
    
- Code review exercises
    

---

## 🔹 `.github/workflows/ci.yml`

Simulated professional CI pipeline:

- Runs on pull request
    
- Installs dependencies
    
- Runs tests
    
- Fails on lint/test errors
    
- Optionally builds Docker image
    

This reinforces:

- “Green pipeline before merge”
    
- DevOps mindset
    
- Automation as guardrails
    

---

## 🔹 `docs/` (Instructor Gold)

### LAB_GUIDE.md

Step-by-step exercises aligned with manual

### BRANCHING_STRATEGY.md

Explains:

- main
    
- develop
    
- feature/*
    
- hotfix/*
    
- release/*
    

Can compare:

- Git Flow
    
- Trunk-Based Development
    

### MERGE_CONFLICT_SCENARIOS.md

Pre-scripted conflicts:

- Two developers editing same route
    
- JSON config conflict
    
- package.json dependency conflict
    

### CI_PIPELINE_EXPLANATION.md

Breakdown of:

- What each job does
    
- Why CI matters
    
- Common failures
    

---

## 🔹 `CONTRIBUTING.md`

Teaches:

- Branch naming conventions
    
- Commit message format
    
- PR requirements
    
- Required reviews
    
- Squash vs merge commit policy
    

This models professional engineering behavior.

---

## 🔹 `CODEOWNERS`

Simulates real-world DevOps practice:

```
* @devops-lead
/routes/ @backend-dev
/tests/ @qa-engineer
```

Students learn:

- Approval workflows
    
- Responsibility boundaries
    

---

# 🔬 Built-In Lab Scenarios

Here’s how you structure the workshop exercises inside the repo.

---

## 🧪 Lab 1 – Feature Branch Workflow

Developer A:

```
feature/add-user-validation
```

Developer B:

```
feature/add-logging
```

Students:

- Create branches
    
- Push
    
- Open PR
    
- Review
    
- Merge
    

---

## 🧪 Lab 2 – Merge Conflict Simulation

Both modify:

```
routes/users.js
```

Instructor triggers conflict.

Students:

- Fetch latest main
    
- Rebase or merge
    
- Resolve conflict
    
- Commit fix
    

---

## 🧪 Lab 3 – Broken CI

Introduce failing test in:

```
tests/user.test.js
```

Students:

- See red pipeline
    
- Diagnose locally
    
- Fix test or code
    
- Push fix
    

---

## 🧪 Lab 4 – Hotfix Workflow

Simulate production bug.

Create:

```
hotfix/fix-user-crash
```

Merge directly to main.

Discuss:

- Why hotfix branches exist
    
- Risk mitigation
    
- CI requirements
    

---

# 🧰 Sample CI File

Example `.github/workflows/ci.yml`:

```yaml
name: Node.js CI

on:
  pull_request:
    branches: [ main, develop ]

jobs:
  build:
    runs-on: ubuntu-latest

    steps:
    - uses: actions/checkout@v4

    - name: Setup Node
      uses: actions/setup-node@v4
      with:
        node-version: 20

    - run: npm install
      working-directory: app

    - run: npm test
      working-directory: app
```

---

# 🎯 Instructor Usage Plan

You can run this repo in 3 modes:

### Mode 1 – Single Repo Simulation

One repo, students use branches.

### Mode 2 – Fork + PR Model

Each student forks and submits PRs.

### Mode 3 – Organization Simulation

Create GitHub org:

```
devops-workshop-lab
```

Assign:

- Maintainers
    
- Reviewers
    
- Contributors
    

Simulates real company workflow.

---

# 🚀 Make It Portfolio-Ready

Add to README:

- Architecture diagram
    
- CI badge
    
- Workshop screenshots
    
- “What This Demonstrates” section
    

This turns it from a lab into:

👉 Recruiter-facing DevOps signal.

---

# 🧠 Want Me To Next:

- Generate the full `README.md` content?
    
- Generate all starter Node.js files?
    
- Generate merge-conflict-ready versions?
    
- Create a downloadable ZIP repo template?
    
- Or build a “Professional DevOps GitHub Organization Simulation Plan”?
    

Tell me your goal:  
🎓 Teaching  
💼 Portfolio  
🏢 Internal training  
🚀 Public DevOps bootcamp

---

Perfect — this README will position you as a **DevOps engineer who understands collaboration, CI, and production workflow**, not just Git commands.

Below is a **portfolio-optimized README.md** ready to drop into your repository.

---

# 📄 `README.md`

---

# Node.js Git Collaboration & CI Lab

A production-style Git collaboration simulation built on Node.js, designed to demonstrate real-world DevOps workflows including branching strategies, CI enforcement, merge conflict resolution, and pull request governance.

This project models how two developers collaborate on a shared codebase while maintaining quality and deployment integrity.

---

## 🚀 Project Overview

This lab simulates:

- Two developers building features in parallel
    
- Structured Git branching strategy
    
- Pull request review process
    
- Automated CI validation
    
- Merge conflict resolution
    
- Hotfix workflow simulation
    
- Code ownership enforcement
    

The application itself is a simple Express-based REST API, but the focus is on **process, automation, and engineering discipline**.

---

## 🏗 Architecture

- Node.js (Express)
    
- Modular service/controller structure
    
- Jest for testing
    
- GitHub Actions for CI
    
- Branch protection workflow
    
- Codeowners review model
    

---

## 🌿 Branching Strategy

This repository follows a structured branching model inspired by Git Flow.

### Permanent Branches

- `main` → Production-ready code
    
- `develop` → Integration branch for features
    

### Supporting Branches

- `feature/*`
    
- `hotfix/*`
    
- `release/*`
    

Example:

```
feature/add-user-validation
hotfix/fix-null-crash
```

This structure enforces controlled integration and reduces production risk.

---

## 🔄 Collaboration Workflow

1. Developer creates feature branch from `develop`
    
2. Code is committed with structured messages
    
3. Pull request opened
    
4. CI pipeline runs automatically
    
5. Code review required (CODEOWNERS enforced)
    
6. Merge after approval + green pipeline
    

This mirrors modern DevOps team workflows.

---

## 🧪 CI Pipeline

Automated via GitHub Actions:

- Install dependencies
    
- Run unit tests
    
- Fail on errors
    
- Enforce green builds before merge
    

Example workflow triggers:

- Pull Requests to `main`
    
- Pull Requests to `develop`
    

The pipeline ensures no broken code reaches integration branches.

---

## 🛠 Running Locally

### 1. Clone Repository

```bash
git clone https://github.com/YOUR_USERNAME/nodejs-git-collaboration-lab.git
cd nodejs-git-collaboration-lab/app
```

### 2. Install Dependencies

```bash
npm install
```

### 3. Run Application

```bash
node server.js
```

App runs on:

```
http://localhost:3000
```

### 4. Run Tests

```bash
npm test
```

---

## 🔍 What This Project Demonstrates

This repository is intentionally structured to showcase:

- Git workflow maturity
    
- Conflict resolution skills
    
- CI/CD integration
    
- DevOps mindset
    
- Secure merging practices
    
- Branch protection modeling
    
- Clean commit history discipline
    

It is less about building a complex application and more about demonstrating **engineering process integrity**.

---

## 🧠 DevOps Principles Modeled

- Infrastructure as Code mindset (CI as code)
    
- Shift-left testing
    
- Reproducibility
    
- Collaboration discipline
    
- Review-driven development
    
- Automation over manual validation
    

---

## 🧩 Merge Conflict Simulation

This lab includes structured conflict scenarios in:

```
routes/users.js
package.json
```

Developers must:

- Rebase or merge latest changes
    
- Resolve conflicts manually
    
- Validate via CI
    
- Maintain commit clarity
    

---

## 🚑 Hotfix Simulation

Production issue scenario:

```
hotfix/fix-user-crash
```

Workflow:

1. Branch from `main`
    
2. Fix bug
    
3. PR into `main`
    
4. Merge back into `develop`
    

This models real production emergency workflows.

---

## 📊 CI Badge

(After publishing)

```markdown
![CI](https://github.com/YOUR_USERNAME/nodejs-git-collaboration-lab/actions/workflows/ci.yml/badge.svg)
```

---

## 📁 Repository Structure

```
app/
docs/
.github/workflows/
scripts/
CONTRIBUTING.md
CODEOWNERS
```

---

## 🔐 Security & Governance

- Branch protections assumed
    
- Required pull request reviews
    
- CI must pass before merge
    
- No direct commits to `main`
    
- Code ownership enforced
    

---

## 📈 Professional Relevance

This project reflects real DevOps responsibilities:

- Managing collaborative codebases
    
- Preventing integration drift
    
- Maintaining pipeline integrity
    
- Resolving merge conflicts efficiently
    
- Protecting production branches
    

It demonstrates operational thinking beyond writing code.

---

## 👨‍💻 Author

Built as part of a structured DevOps skill progression focusing on:

- Linux fundamentals
    
- Git workflow mastery
    
- CI/CD pipeline engineering
    
- Secure collaboration patterns
    

---

## 🤝 Open to Collaboration

If you're building teams focused on DevOps engineering, platform reliability, or CI/CD systems, I’m always open to connect and discuss infrastructure automation and Linux-driven development workflows.

---

# Optional Enhancements (Recommended for Portfolio Impact)

Add:

- Architecture diagram (PNG in repo)
    
- Screenshot of passing CI pipeline
    
- Screenshot of resolved merge conflict
    
- Link to LinkedIn post discussing project
    
- Short demo video (Loom or similar)
    

---

If you'd like, I can next:

- Rewrite this to sound more senior-level
    
- Make it optimized for recruiter keyword scanning
    
- Add measurable metrics (even simulated)
    
- Or create a DevOps-focused GitHub profile README that ties all your projects together
    

What level are you positioning yourself for — Junior DevOps, Mid-level, or Platform Engineer track?