# Git Basics for DevOps — Course 2

### A Comprehensive Tutorial with Hands-On Labs

---

## Table of Contents

- [Module 1 – Git Introduction](https://claude.ai/local_sessions/local_c16524e5-1c07-464f-ba05-5cd93beac4e2#module-1--git-introduction)
    - [Git Fundamentals](https://claude.ai/local_sessions/local_c16524e5-1c07-464f-ba05-5cd93beac4e2#git-fundamentals)
    - [Installing Git](https://claude.ai/local_sessions/local_c16524e5-1c07-464f-ba05-5cd93beac4e2#installing-git)
    - [Local and Remote Repositories](https://claude.ai/local_sessions/local_c16524e5-1c07-464f-ba05-5cd93beac4e2#local-and-remote-repositories)
    - [Initializing a Git Repository](https://claude.ai/local_sessions/local_c16524e5-1c07-464f-ba05-5cd93beac4e2#initializing-a-git-repository)
    - [Git Log](https://claude.ai/local_sessions/local_c16524e5-1c07-464f-ba05-5cd93beac4e2#git-log)
    - [Git Workflow: From Init to Commit](https://claude.ai/local_sessions/local_c16524e5-1c07-464f-ba05-5cd93beac4e2#git-workflow-from-init-to-commit)
    - [Git Branches](https://claude.ai/local_sessions/local_c16524e5-1c07-464f-ba05-5cd93beac4e2#git-branches)
    - [Merging Branches](https://claude.ai/local_sessions/local_c16524e5-1c07-464f-ba05-5cd93beac4e2#merging-branches)
    - [Module 1 Assessment](https://claude.ai/local_sessions/local_c16524e5-1c07-464f-ba05-5cd93beac4e2#module-1-assessment)
- [Module 2 – Initialize Remote Repositories](https://claude.ai/local_sessions/local_c16524e5-1c07-464f-ba05-5cd93beac4e2#module-2--initialize-remote-repositories)
    - [Remote Repositories](https://claude.ai/local_sessions/local_c16524e5-1c07-464f-ba05-5cd93beac4e2#remote-repositories)
    - [Pushing to Remote Repositories](https://claude.ai/local_sessions/local_c16524e5-1c07-464f-ba05-5cd93beac4e2#pushing-to-remote-repositories)
    - [Cloning Remote Repositories](https://claude.ai/local_sessions/local_c16524e5-1c07-464f-ba05-5cd93beac4e2#cloning-remote-repositories)
    - [Pull Requests](https://claude.ai/local_sessions/local_c16524e5-1c07-464f-ba05-5cd93beac4e2#pull-requests)
    - [Fetching and Pulling](https://claude.ai/local_sessions/local_c16524e5-1c07-464f-ba05-5cd93beac4e2#fetching-and-pulling)
    - [Merge Conflicts](https://claude.ai/local_sessions/local_c16524e5-1c07-464f-ba05-5cd93beac4e2#merge-conflicts)
    - [Forking](https://claude.ai/local_sessions/local_c16524e5-1c07-464f-ba05-5cd93beac4e2#forking)
    - [Module 2 Assessment](https://claude.ai/local_sessions/local_c16524e5-1c07-464f-ba05-5cd93beac4e2#module-2-assessment)
- [Quick Reference Card](https://claude.ai/local_sessions/local_c16524e5-1c07-464f-ba05-5cd93beac4e2#quick-reference-card)

---

# Module 1 – Git Introduction

## Learning Objectives

By the end of this module you will be able to:

- Understand Git fundamentals and why version control matters
- Install Git on your system and perform initial configuration
- Initialize and configure local repositories
- Understand the difference between local and remote repositories
- Navigate commit history with `git log`
- Master the Git workflow from `init` to `commit`
- Understand branches and their purpose in version control
- Create, switch, and merge branches

---

## Git Fundamentals

### What Is Version Control?

Version control is a system that records changes to files over time, allowing you to recall specific versions later. Without version control, developers face a number of painful problems:

- Overwriting a colleague's changes when two people edit the same file
- No way to roll back a breaking change
- Uncertainty about what changed between versions and who changed it
- Difficulty collaborating across teams and geographies

A **Version Control System (VCS)** solves all of these problems by tracking every modification to every file in a project.

### Types of Version Control Systems

```
Centralized VCS (CVCS)          Distributed VCS (DVCS)
────────────────────────        ──────────────────────────────
      Central Server                   Remote Repository
           │                               │
     ┌─────┴─────┐               ┌─────────┴─────────┐
   Dev A       Dev B           Dev A               Dev B
  (checkout)  (checkout)    (full local copy)  (full local copy)
```

**Centralized VCS** (e.g., SVN, CVS): A single central repository holds all versions. Developers check out files and check them back in. A server failure can halt all work.

**Distributed VCS** (e.g., Git, Mercurial): Every developer has a complete local copy of the entire repository including full history. Work continues even when offline. This is Git's model.

### What Is Git?

Git is a free, open-source **Distributed Version Control System** created by Linus Torvalds in 2005 to manage the Linux kernel source code. It is now the world's most widely used VCS.

Key properties of Git:

|Property|Description|
|---|---|
|**Distributed**|Every clone is a full repository with complete history|
|**Fast**|Most operations are local, no network round-trips needed|
|**Integrity**|Every object is checksummed with SHA-1 before storage|
|**Non-linear**|Powerful branching and merging support|
|**Free/Open Source**|Licensed under the GNU GPL v2|

### Git's Three States

Every file in a Git project lives in one of three states:

```
 ┌─────────────┐     git add     ┌─────────────┐    git commit   ┌─────────────┐
 │  Working    │ ──────────────► │   Staging   │ ──────────────► │ Repository  │
 │  Directory  │                 │     Area    │                 │  (.git dir) │
 └─────────────┘                 └─────────────┘                 └─────────────┘
   Modified files               Files staged for              Committed snapshots
   (untracked or                 next commit                   (permanent history)
    modified)
```

- **Working Directory**: Where you edit files. Changes here are not yet tracked.
- **Staging Area (Index)**: A preparation zone. You explicitly choose which changes go into the next commit.
- **Repository (.git directory)**: The permanent, compressed object database that stores your history.

### The Commit Object

A Git commit is a snapshot, not a diff. Each commit stores:

- A pointer to a **tree object** (directory snapshot)
- Pointers to **parent commit(s)**
- **Author** and **committer** metadata (name, email, timestamp)
- A **commit message**
- A **SHA-1 hash** that uniquely identifies it

```
commit a3f8c1d
Author: Alice <alice@example.com>
Date:   Mon Apr 01 09:15:00 2026 +0000

    Add user authentication module

tree   b4e2a09   ← directory snapshot
parent 9c1d73f   ← previous commit
```

---

## Installing Git

### Lab: Install Git

**Objective**: Install Git on your operating system and verify the installation.

**Estimated time**: 10 minutes

---

#### Linux (Debian/Ubuntu)

```bash
# Update package index
sudo apt update

# Install Git
sudo apt install -y git

# Verify installation
git --version
# Expected output: git version 2.x.x
```

#### Linux (RHEL/CentOS/Fedora)

```bash
# RHEL 8 / CentOS 8 / Fedora
sudo dnf install -y git

# RHEL 7 / CentOS 7
sudo yum install -y git

# Verify
git --version
```

#### macOS

```bash
# Option 1: Install Xcode Command Line Tools (includes Git)
xcode-select --install

# Option 2: Install via Homebrew
brew install git

# Verify
git --version
```

#### Windows

1. Download the installer from https://git-scm.com/download/win
2. Run the `.exe` and accept defaults (or customize as needed)
3. Open **Git Bash** and verify:

```bash
git --version
```

---

### Initial Configuration

Before using Git, you must tell it who you are. This information is embedded in every commit you make.

```bash
# Set your name (used in commit metadata)
git config --global user.name "Your Name"

# Set your email (used in commit metadata)
git config --global user.email "you@example.com"

# Set your preferred editor (used for commit messages)
git config --global core.editor vim       # or nano, code, etc.

# Set default branch name to 'main'
git config --global init.defaultBranch main

# Enable colored output
git config --global color.ui auto

# Set line ending handling (Linux/macOS)
git config --global core.autocrlf input

# Set line ending handling (Windows)
git config --global core.autocrlf true
```

### Configuration Scopes

Git has three levels of configuration, each overriding the previous:

```
┌──────────────┬──────────────────────────────────┬─────────────────────────────────┐
│ Scope        │ File Location                    │ Flag                            │
├──────────────┼──────────────────────────────────┼─────────────────────────────────┤
│ System       │ /etc/gitconfig                   │ --system                        │
│ Global       │ ~/.gitconfig  or ~/.config/git/  │ --global  (per user)            │
│ Local        │ .git/config  (in the repo)       │ --local   (per project)         │
└──────────────┴──────────────────────────────────┴─────────────────────────────────┘
```

```bash
# View all configuration and where each setting comes from
git config --list --show-origin

# View a specific setting
git config user.name

# Edit global config directly
git config --global --edit
```

---

## Local and Remote Repositories

### The Two Worlds of Git

```
  LOCAL                                         REMOTE
 ─────────────────────────────────             ─────────────────
  Working     Staging    .git/                  GitHub / GitLab /
  Directory    Area     (local repo)             Bitbucket / etc.
     │           │          │                          │
     │  git add  │          │                          │
     │──────────►│          │                          │
     │           │git commit│                          │
     │           │─────────►│                          │
     │           │          │    git push              │
     │           │          │─────────────────────────►│
     │           │          │    git fetch/pull        │
     │           │          │◄─────────────────────────│
```

- A **local repository** lives on your machine inside a `.git/` directory. All `git add`, `git commit`, and `git log` operations work entirely locally — no network required.
- A **remote repository** is a copy of your repository hosted on a server (GitHub, GitLab, Bitbucket, a private server, etc.). It enables collaboration: you `push` your commits up and `pull` or `fetch` others' commits down.

You can have multiple remotes. The default remote is conventionally named `origin`.

---

## Initializing a Git Repository

### Demo: Initialize a Git Repository

Two ways to start a Git project:

**Method 1 — `git init` (start fresh)**

```bash
# Create a new project directory
mkdir my-devops-project
cd my-devops-project

# Initialize an empty Git repository
git init

# Git creates a hidden .git/ directory — this IS the repository
ls -la
# drwxr-xr-x  .git/
# (your project files go here)

# Inspect the .git/ directory structure
ls .git/
# HEAD        branches/   config      description
# hooks/      info/       objects/    refs/
```

**Method 2 — `git clone` (copy an existing remote repo)**

```bash
# Clone creates a local copy of a remote repository
git clone https://github.com/example/repo.git

# Clone into a custom directory name
git clone https://github.com/example/repo.git my-local-name

# Clone a specific branch
git clone --branch develop https://github.com/example/repo.git
```

### Lab: Initialize a Git Repository

**Objective**: Create a new project, initialize Git, make your first commit, and explore the `.git` directory structure.

**Estimated time**: 15 minutes

---

**Step 1 – Create the project**

```bash
mkdir git-lab-project
cd git-lab-project
git init
```

Expected output:

```
Initialized empty Git repository in /home/user/git-lab-project/.git/
```

**Step 2 – Check repository status**

```bash
git status
```

Expected output:

```
On branch main

No commits yet

nothing to commit (create/copy files and use "git commit")
```

**Step 3 – Create your first file**

```bash
cat > README.md << 'EOF'
# My DevOps Project

A hands-on Git learning project.

## Goals
- Learn Git fundamentals
- Practice branching and merging
- Collaborate with remote repositories
EOF
```

**Step 4 – Check status again**

```bash
git status
```

Output:

```
On branch main

No commits yet

Untracked files:
  (use "git add <file>..." to include in what will be committed)
        README.md

nothing added to commit but untracked files present
```

**Step 5 – Stage the file**

```bash
# Stage a specific file
git add README.md

# Or stage all files in the directory
git add .

git status
```

Output:

```
On branch main

No commits yet

Changes to be committed:
  (use "git rm --cached <file>..." to unstage)
        new file:   README.md
```

**Step 6 – Make your first commit**

```bash
git commit -m "Initial commit: add README"
```

Output:

```
[main (root-commit) a1b2c3d] Initial commit: add README
 1 file changed, 10 insertions(+)
 create mode 100644 README.md
```

**Step 7 – Explore the .git directory**

```bash
# View the HEAD pointer
cat .git/HEAD
# ref: refs/heads/main

# View your commit object
git cat-file -p HEAD

# View the tree (directory snapshot)
git ls-tree HEAD
```

**Step 8 – Create more files and practice the workflow**

```bash
mkdir src
cat > src/app.py << 'EOF'
#!/usr/bin/env python3

def main():
    print("Hello, DevOps!")

if __name__ == "__main__":
    main()
EOF

cat > .gitignore << 'EOF'
# Python
__pycache__/
*.pyc
*.pyo
.venv/
venv/

# OS
.DS_Store
Thumbs.db
EOF

git add .
git commit -m "Add Python app and .gitignore"
```

---

## Git Log

`git log` is your window into the history of the repository. It shows commits in reverse chronological order (newest first).

### Basic Usage

```bash
# Full log (default format)
git log

# Output:
# commit a1b2c3d4e5f6... (HEAD -> main)
# Author: Alice <alice@example.com>
# Date:   Mon Apr 01 09:15:00 2026 +0000
#
#     Add user authentication module
#
# commit 9c1d73f2a8b1...
# Author: Alice <alice@example.com>
# Date:   Sun Mar 31 16:30:00 2026 +0000
#
#     Initial commit: add README
```

### Useful Flags

```bash
# Compact one-line format
git log --oneline

# Show branch/tag decorations as a graph
git log --oneline --graph --decorate --all

# Limit number of commits shown
git log -5

# Show commits by a specific author
git log --author="Alice"

# Show commits containing a keyword in the message
git log --grep="authentication"

# Show commits that changed a specific file
git log -- src/app.py

# Show commits between two dates
git log --after="2026-01-01" --before="2026-04-01"

# Show the diff (patch) for each commit
git log -p

# Show a summary of changed files per commit
git log --stat

# Custom format
git log --pretty=format:"%h | %an | %ar | %s"
# a1b2c3d | Alice | 2 hours ago | Add authentication module
```

### Lab: Git Log

**Objective**: Build up a realistic commit history and practice inspecting it with various `git log` options.

**Estimated time**: 15 minutes

---

**Step 1 – Add several commits to your project**

```bash
# In git-lab-project from the previous lab

# Commit 3
cat > src/config.py << 'EOF'
DATABASE_URL = "postgresql://localhost/myapp"
DEBUG = False
SECRET_KEY = "change-me-in-production"
EOF
git add .
git commit -m "Add application configuration"

# Commit 4
cat >> README.md << 'EOF'

## Setup
1. Install dependencies: `pip install -r requirements.txt`
2. Configure database in `src/config.py`
3. Run: `python src/app.py`
EOF
git add .
git commit -m "Update README with setup instructions"

# Commit 5
cat > requirements.txt << 'EOF'
flask==3.0.0
psycopg2-binary==2.9.9
python-dotenv==1.0.0
EOF
git add .
git commit -m "Add requirements.txt with Flask dependencies"
```

**Step 2 – Explore the log**

```bash
# Basic log
git log

# One-line compact view
git log --oneline

# Graph view (useful once you have branches)
git log --oneline --graph --decorate --all

# Show who changed what
git log --stat

# Show changes inline
git log -p --follow src/app.py
```

**Step 3 – Inspect a specific commit**

```bash
# Pick a commit hash from your log output
git show a1b2c3d    # replace with your actual hash

# Show only the changed files
git show --name-only a1b2c3d

# Show the diff for a specific file in a commit
git show HEAD:src/config.py
```

**Step 4 – Search the history**

```bash
# Find all commits that touched requirements.txt
git log --follow -- requirements.txt

# Find commits with "config" in the message
git log --grep="config" --oneline

# Compare two commits
git diff HEAD~2 HEAD
```

---

## Git Workflow: From Init to Commit

### The Complete Daily Workflow

```
┌─────────────────────────────────────────────────────────────────────┐
│  DAILY GIT WORKFLOW                                                  │
│                                                                      │
│  1. git status         → What's changed?                            │
│  2. git diff           → What exactly changed line-by-line?         │
│  3. git add <files>    → Stage specific changes                     │
│  4. git diff --staged  → Review what's about to be committed        │
│  5. git commit -m "…"  → Snapshot staged changes                   │
│  6. git log --oneline  → Confirm the commit is in history           │
└─────────────────────────────────────────────────────────────────────┘
```

### Useful Workflow Commands

```bash
# See what has changed (tracked files)
git diff

# See what's staged (about to be committed)
git diff --staged

# Unstage a file (keep working directory changes)
git restore --staged src/app.py

# Discard working directory changes for a file (DESTRUCTIVE)
git restore src/app.py

# Add and commit in one step (only for already-tracked files)
git commit -am "Quick fix for typo"

# Amend the most recent commit (before pushing!)
git commit --amend -m "Better commit message"

# Undo the last commit, keep changes staged
git reset --soft HEAD~1

# Undo the last commit, keep changes unstaged
git reset HEAD~1

# See what .gitignore is ignoring
git status --ignored
```

### Writing Good Commit Messages

A commit message has two parts: a **subject line** and an optional **body**.

```
feat: add OAuth2 login support

Implement Google OAuth2 authentication using the authlib library.
Users can now sign in with their Google accounts in addition to
email/password. The existing session management is preserved.

Resolves: #142
```

**Rules for great commit messages:**

1. Subject line: 50 characters or fewer
2. Capitalize the subject line
3. Do not end the subject line with a period
4. Use the imperative mood: "Add feature" not "Added feature"
5. Separate subject from body with a blank line
6. Body: wrap at 72 characters
7. Explain _what_ and _why_, not _how_

**Common prefixes (Conventional Commits)**:

|Prefix|Meaning|
|---|---|
|`feat:`|A new feature|
|`fix:`|A bug fix|
|`docs:`|Documentation changes only|
|`style:`|Formatting, missing semicolons, etc.|
|`refactor:`|Code change that is not a fix or feature|
|`test:`|Adding or correcting tests|
|`chore:`|Build process, tooling changes|
|`ci:`|CI configuration changes|

---

## Git Branches

### What Is a Branch?

A branch in Git is simply a **lightweight movable pointer to a commit**. The default branch is `main` (or `master` in older repositories). When you make a commit on a branch, the branch pointer automatically advances to the new commit.

```
Before branching:

  main
    │
    ▼
A ← B ← C
        ▲
       HEAD


After creating 'feature/login':

  main   feature/login
    │          │
    ▼          ▼
A ← B ← C ← D ← E
                  ▲
                 HEAD
```

`HEAD` is a special pointer that tracks which branch you're currently on. When you commit, HEAD (and the current branch pointer) advance together.

### Why Branch?

Branches enable you to:

- **Isolate features**: Work on a new feature without touching stable code
- **Experiment safely**: Try risky changes; if they fail, delete the branch
- **Enable parallel work**: Multiple developers work simultaneously on different features
- **Support release workflows**: Maintain separate branches for development, staging, and production

### Branch Commands

```bash
# List all local branches (* marks the current branch)
git branch

# List all branches including remote-tracking branches
git branch -a

# List remote branches only
git branch -r

# Create a new branch (does NOT switch to it)
git branch feature/user-auth

# Create a new branch AND switch to it
git checkout -b feature/user-auth

# Modern equivalent (Git 2.23+)
git switch -c feature/user-auth

# Switch to an existing branch
git checkout main
# or
git switch main

# Rename a branch
git branch -m old-name new-name

# Delete a branch (safe: prevents deletion if unmerged)
git branch -d feature/user-auth

# Force-delete a branch (even if unmerged)
git branch -D feature/user-auth

# See the last commit on each branch
git branch -v
```

### Lab: Branches – Checkout, Push Branch

**Objective**: Create branches, switch between them, make changes on each, and push a branch to a remote repository.

**Estimated time**: 20 minutes

---

**Step 1 – Verify your starting point**

```bash
cd git-lab-project
git log --oneline
git branch
# * main
```

**Step 2 – Create and switch to a feature branch**

```bash
git switch -c feature/add-logging

# Verify you are now on the feature branch
git branch
# * feature/add-logging
#   main
```

**Step 3 – Make changes on the feature branch**

```bash
cat > src/logger.py << 'EOF'
import logging
import sys

def get_logger(name: str) -> logging.Logger:
    """Configure and return a named logger."""
    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)

    handler = logging.StreamHandler(sys.stdout)
    handler.setLevel(logging.DEBUG)

    formatter = logging.Formatter(
        '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    )
    handler.setFormatter(formatter)

    if not logger.handlers:
        logger.addHandler(handler)

    return logger
EOF

git add src/logger.py
git commit -m "feat: add centralized logging module"
```

**Step 4 – Update the main app on this branch**

```bash
cat > src/app.py << 'EOF'
#!/usr/bin/env python3
from logger import get_logger

logger = get_logger(__name__)

def main():
    logger.info("Application starting up")
    print("Hello, DevOps!")
    logger.info("Application finished")

if __name__ == "__main__":
    main()
EOF

git add src/app.py
git commit -m "feat: integrate logger into main application"
```

**Step 5 – Switch back to main and verify isolation**

```bash
git switch main

# The main branch does NOT have logger.py
ls src/
# app.py  config.py

# app.py on main still has the original content
cat src/app.py
```

**Step 6 – Create a second branch from main**

```bash
git switch -c fix/config-typo

cat > src/config.py << 'EOF'
import os

DATABASE_URL = os.getenv("DATABASE_URL", "postgresql://localhost/myapp")
DEBUG = os.getenv("DEBUG", "false").lower() == "true"
SECRET_KEY = os.getenv("SECRET_KEY", "change-me-in-production")
EOF

git add src/config.py
git commit -m "fix: load config values from environment variables"
```

**Step 7 – Review your branch structure**

```bash
git log --oneline --graph --decorate --all

# Output example:
# * a1b2c3d (HEAD -> fix/config-typo) fix: load config from environment
# | * f4e5d6c (feature/add-logging) feat: integrate logger
# | * b7c8d9e feat: add centralized logging module
# |/
# * 9a0b1c2 (main) Add requirements.txt with Flask dependencies
# * ...
```

**Step 8 – Push a branch to a remote (if you have one configured)**

```bash
# If you have a remote repository (e.g., on GitHub):
git remote add origin https://github.com/your-username/git-lab-project.git

# Push the feature branch
git push -u origin feature/add-logging

# The -u flag sets the upstream tracking reference.
# Future pushes only need: git push
```

---

## Merging Branches

### What Is Merging?

Merging takes the work from one branch and integrates it into another. The branch you merge _into_ is called the **target** (or base) branch. The branch you merge _from_ is called the **source** (or topic) branch.

### Types of Merges

**Fast-Forward Merge**

When the target branch has not diverged from the source, Git simply moves the target branch pointer forward. No merge commit is created.

```
Before:
  main: A ← B
               \
  feature:      C ← D

After fast-forward merge of feature into main:
  main: A ← B ← C ← D
  (no merge commit; main pointer simply advanced)
```

```bash
git switch main
git merge feature/my-feature
# Fast-forward
```

**Three-Way Merge (Recursive)**

When both branches have diverged, Git finds the common ancestor and performs a three-way merge, creating a new **merge commit**.

```
Before:
  main:    A ← B ← C
                     \
  feature:  A ← B ← D ← E

After three-way merge:
  main:    A ← B ← C ← F  (F is the merge commit)
                    ↗
                   D ← E
```

```bash
git switch main
git merge feature/my-feature
# Merge made by the 'recursive' strategy.
# A merge commit is created automatically.
```

**Squash Merge**

Collapse all commits from the source branch into a single commit on the target branch. Keeps main history clean.

```bash
git switch main
git merge --squash feature/my-feature
git commit -m "feat: add user authentication (squashed)"
```

**No-Fast-Forward (--no-ff)**

Force a merge commit even when a fast-forward is possible. Useful for preserving branch history.

```bash
git switch main
git merge --no-ff feature/my-feature -m "Merge feature/my-feature into main"
```

### Lab: Merging Branches

**Objective**: Perform a fast-forward merge and a three-way merge, then inspect the resulting history.

**Estimated time**: 20 minutes

---

**Step 1 – Start from the project you built earlier**

```bash
cd git-lab-project
git log --oneline --graph --decorate --all
```

**Step 2 – Fast-forward merge the bugfix branch into main**

```bash
git switch main

# The fix/config-typo branch diverged directly from main with one commit
# This will be a fast-forward merge
git merge fix/config-typo

# Verify: main now contains the config fix
cat src/config.py
```

Expected output:

```
Updating 9a0b1c2..a1b2c3d
Fast-forward
 src/config.py | 7 +++++--
 1 file changed, 5 insertions(+), 2 deletions(-)
```

**Step 3 – Add a new commit to main to force a three-way merge**

```bash
cat > Makefile << 'EOF'
.PHONY: run test install clean

install:
	pip install -r requirements.txt

run:
	python src/app.py

test:
	python -m pytest tests/

clean:
	find . -type f -name "*.pyc" -delete
	find . -type d -name "__pycache__" -exec rm -rf {} +
EOF

git add Makefile
git commit -m "chore: add Makefile for common tasks"
```

**Step 4 – Three-way merge the feature branch**

```bash
# main has a new commit that feature/add-logging doesn't have
# This will create a merge commit
git merge feature/add-logging --no-ff -m "Merge feature/add-logging into main"
```

Output:

```
Merge made by the 'ort' strategy.
 src/app.py    | 5 ++++-
 src/logger.py | 24 ++++++++++++++++++++++++
 2 files changed, 28 insertions(+), 1 deletion(-)
 create mode 100644 src/logger.py
```

**Step 5 – Inspect the merge commit**

```bash
git log --oneline --graph --decorate --all

# Output:
# *   d9e0f1a (HEAD -> main) Merge feature/add-logging into main
# |\
# | * f4e5d6c (feature/add-logging) feat: integrate logger
# | * b7c8d9e feat: add centralized logging module
# * | c2d3e4f chore: add Makefile for common tasks
# * | a1b2c3d fix: load config from environment variables
# |/
# * 9a0b1c2 Add requirements.txt with Flask dependencies
# ...

# Inspect the merge commit
git show HEAD
```

**Step 6 – Clean up merged branches**

```bash
# Delete branches that have been fully merged into main
git branch -d feature/add-logging
git branch -d fix/config-typo

# Confirm cleanup
git branch
# * main
```

**Step 7 – Practice with a conflict scenario**

```bash
# Create two branches that edit the same line
git switch -c branch-a
echo "# Branch A was here" >> README.md
git add README.md
git commit -m "Branch A: update README"

git switch main
git switch -c branch-b
echo "# Branch B was here" >> README.md
git add README.md
git commit -m "Branch B: update README"

git switch main
git merge branch-a
git merge branch-b
# CONFLICT (content): Merge conflict in README.md
# You'll resolve this in Module 2's Merge Conflicts section
git merge --abort   # abort for now; we'll handle conflicts in Module 2
```

---

## Module 1 Assessment

### Knowledge Check

**Question 1**: What are Git's three states? Describe what happens to a file in each state.

**Question 2**: What is the difference between `git fetch` and `git pull`? (Hint: we'll cover this fully in Module 2 — use your intuition.)

**Question 3**: You made two commits and realized the second commit message has a typo. What command fixes it, and when is it safe to use?

**Question 4**: Draw the commit graph (ASCII art) for the following sequence of operations:

```
git init
git commit -m "A"
git commit -m "B"
git switch -c feature
git commit -m "C"
git switch main
git commit -m "D"
git merge feature
```

**Question 5**: What is the difference between `git branch -d` and `git branch -D`? When would you use each?

**Question 6**: Explain why Git uses SHA-1 hashes for commit IDs. What problem does this solve?

**Question 7**: You have changes in your working directory that you don't want to commit yet, but you need to switch to another branch urgently. Name two approaches to handle this safely.

### Practical Exercises

**Exercise 1**: Create a repository called `devops-pipeline`, add a `.gitignore` for Python, make 5 commits with meaningful messages following Conventional Commits format, and display the history in a custom `git log` format showing hash, author, relative date, and subject.

**Exercise 2**: Create two branches (`feature/ci` and `feature/cd`) from main. Add two commits to each. Merge them both into main using `--no-ff`. Produce the graph view showing all three branches.

**Exercise 3**: Using `git log` flags, answer these questions about a repository: (a) How many commits touched `README.md`? (b) Who made the most commits? (c) What changed in the third commit?

---

# Module 2 – Initialize Remote Repositories

## Learning Objectives

By the end of this module you will be able to:

- Initialize and connect to remote repositories
- Push changes to a remote repository
- Clone a remote repository to create a local working copy
- Understand and create pull requests for collaborative workflows
- Fetch and pull changes from remote repositories
- Resolve merge conflicts
- Fork a repository to contribute to open-source projects

---

## Remote Repositories

### Understanding Remotes

A **remote** is a version of your project hosted on a network (GitHub, GitLab, Bitbucket, a self-hosted server, etc.). Remotes allow:

- **Backup**: Your history is preserved on a server
- **Collaboration**: Multiple developers share a common reference point
- **Deployment**: CI/CD pipelines pull from remotes to build and deploy
- **Open Source**: Anyone can fork, contribute, and submit pull requests

### Remote Management Commands

```bash
# List configured remotes (name and URL)
git remote -v

# Add a remote named 'origin'
git remote add origin https://github.com/username/repo.git

# Add an SSH remote
git remote add origin git@github.com:username/repo.git

# Change the URL of an existing remote
git remote set-url origin https://github.com/username/new-repo.git

# Rename a remote
git remote rename origin upstream

# Remove a remote
git remote remove upstream

# Inspect a remote (shows tracked branches and fetch/push URLs)
git remote show origin
```

### Setting Up GitHub (or GitLab)

**HTTPS Authentication (Personal Access Token)**

```bash
# GitHub no longer accepts password authentication.
# Generate a Personal Access Token (PAT) at:
# GitHub → Settings → Developer settings → Personal access tokens

# When prompted for a password, use your PAT instead
git clone https://github.com/username/repo.git
# Username: your-github-username
# Password: ghp_xxxxxxxxxxxxxxxxxxxx  ← your PAT
```

**SSH Authentication (Recommended)**

```bash
# Step 1: Generate an SSH key pair
ssh-keygen -t ed25519 -C "you@example.com"
# Press Enter to accept the default location (~/.ssh/id_ed25519)
# Enter a passphrase (recommended)

# Step 2: Start the SSH agent and add your key
eval "$(ssh-agent -s)"
ssh-add ~/.ssh/id_ed25519

# Step 3: Copy the public key
cat ~/.ssh/id_ed25519.pub
# Paste this into GitHub → Settings → SSH and GPG keys → New SSH key

# Step 4: Test the connection
ssh -T git@github.com
# Hi username! You've successfully authenticated.

# Step 5: Use SSH URL for cloning/remotes
git remote add origin git@github.com:username/repo.git
```

---

## Pushing to Remote Repositories

### The Push Command

`git push` uploads your local commits to a remote repository.

```bash
# Push the current branch to its upstream remote
git push

# Push a specific branch to origin
git push origin main

# Push and set the upstream tracking reference (-u)
git push -u origin feature/my-feature

# Push all local branches
git push --all origin

# Push tags to remote
git push --tags

# Delete a remote branch
git push origin --delete feature/old-branch
# or shorthand:
git push origin :feature/old-branch

# Force push (DANGEROUS — rewrites remote history)
git push --force origin main

# Safer force push (fails if remote was updated by someone else)
git push --force-with-lease origin main
```

### Understanding Upstream Tracking

When you use `-u` (or `--set-upstream`), Git remembers the relationship between your local branch and the remote branch. After this, `git push` and `git pull` work without arguments.

```bash
# First push: set the upstream
git push -u origin feature/my-feature

# Subsequent pushes (no need to specify branch)
git push

# View upstream tracking info
git branch -vv
# * feature/my-feature a1b2c3d [origin/feature/my-feature] Add feature
#   main               9c1d73f [origin/main] Initial commit
```

### Lab: Remote Repositories

**Objective**: Initialize a remote repository on GitHub, connect it to your local repository, and push your commits.

**Estimated time**: 20 minutes

**Prerequisites**: A GitHub account and either a PAT or SSH key configured.

---

**Step 1 – Create a repository on GitHub**

1. Go to https://github.com and sign in
2. Click the **+** icon → **New repository**
3. Repository name: `git-lab-project`
4. Description: `Git learning project`
5. Visibility: **Public** (or Private)
6. **Do NOT** initialize with README, .gitignore, or license (we already have these locally)
7. Click **Create repository**

**Step 2 – Connect your local repository**

```bash
cd git-lab-project

# Add the remote (use SSH URL if you have SSH keys set up)
git remote add origin git@github.com:YOUR_USERNAME/git-lab-project.git

# Verify
git remote -v
# origin  git@github.com:YOUR_USERNAME/git-lab-project.git (fetch)
# origin  git@github.com:YOUR_USERNAME/git-lab-project.git (push)
```

**Step 3 – Push your main branch**

```bash
git push -u origin main

# Output:
# Enumerating objects: 18, done.
# Counting objects: 100% (18/18), done.
# Delta compression using up to 8 threads
# Compressing objects: 100% (12/12), done.
# Writing objects: 100% (18/18), 2.45 KiB | 2.45 MiB/s, done.
# Total 18 (delta 3), reused 0 (delta 0)
# To github.com:YOUR_USERNAME/git-lab-project.git
#  * [new branch]      main -> main
# Branch 'main' set up to track remote branch 'main' from 'origin'.
```

**Step 4 – Make a new commit and push**

```bash
cat > CONTRIBUTING.md << 'EOF'
# Contributing Guide

Thank you for considering contributing to this project!

## How to Contribute

1. Fork the repository
2. Create a feature branch: `git switch -c feature/your-feature`
3. Commit your changes: `git commit -m "feat: add your feature"`
4. Push to your fork: `git push origin feature/your-feature`
5. Open a Pull Request
EOF

git add CONTRIBUTING.md
git commit -m "docs: add contributing guide"
git push
```

**Step 5 – Verify on GitHub**

Open your browser and navigate to `https://github.com/YOUR_USERNAME/git-lab-project`. You should see all your files and commit history.

---

## Cloning Remote Repositories

### What Is Cloning?

`git clone` creates a full local copy of a remote repository. It:

1. Creates a new directory (named after the repository, unless overridden)
2. Initializes a `.git/` directory inside it
3. Downloads all commits, branches, and tags
4. Checks out the default branch (usually `main`)
5. Automatically configures `origin` pointing to the source URL

```bash
# Basic clone
git clone https://github.com/username/repo.git

# Clone into a specific directory
git clone https://github.com/username/repo.git my-project

# Clone a specific branch
git clone --branch develop https://github.com/username/repo.git

# Shallow clone (only the latest N commits — faster for large repos)
git clone --depth 1 https://github.com/username/repo.git

# Clone including all submodules
git clone --recurse-submodules https://github.com/username/repo.git

# Mirror clone (for backups — includes all refs)
git clone --mirror https://github.com/username/repo.git
```

### Lab: Cloning Remote Repositories

**Objective**: Clone a public repository, explore its structure, and contribute a change.

**Estimated time**: 15 minutes

---

**Step 1 – Clone a public repository**

```bash
# Move to a parent directory
cd ~

# Clone the official Git documentation repository (small, educational)
git clone https://github.com/git/git.git --depth 5

# Or clone a simpler example repo
git clone https://github.com/octocat/Hello-World.git
cd Hello-World
```

**Step 2 – Explore the cloned repository**

```bash
# See the remote configuration set automatically
git remote -v
# origin  https://github.com/octocat/Hello-World.git (fetch)
# origin  https://github.com/octocat/Hello-World.git (push)

# View all branches (including remote-tracking branches)
git branch -a

# View the commit history
git log --oneline -10
```

**Step 3 – Clone your own repository into a second location (simulating a second developer)**

```bash
cd ~
git clone git@github.com:YOUR_USERNAME/git-lab-project.git git-lab-project-colleague
cd git-lab-project-colleague

ls -la
git log --oneline
```

**Step 4 – Simulate a colleague's commit**

```bash
# In git-lab-project-colleague:
cat > CHANGELOG.md << 'EOF'
# Changelog

## [Unreleased]
### Added
- Centralized logging module
- Environment-based configuration
- Contributing guide
EOF

git add CHANGELOG.md
git commit -m "docs: add CHANGELOG file"
git push origin main
```

**Step 5 – Pull the colleague's changes into your original clone**

```bash
cd ~/git-lab-project
git pull
# You should now see CHANGELOG.md here too
ls
```

---

## Pull Requests

### What Is a Pull Request?

A **Pull Request (PR)** — called a **Merge Request (MR)** in GitLab — is a proposal to merge changes from one branch into another. Pull Requests are a collaboration tool, not a Git feature. They live in the hosting platform (GitHub, GitLab, Bitbucket).

A Pull Request enables:

- **Code review**: Teammates review your changes before they land in the main branch
- **Discussion**: Comments on specific lines, questions, suggestions
- **CI/CD gate**: Automated tests must pass before merging
- **Audit trail**: A permanent record of what changed, why, and who approved it

### Pull Request Workflow

```
  Developer Fork / Branch              Main Repository
  ─────────────────────────           ─────────────────────
  1. Fork (or create branch)
  2. git switch -c feature/X
  3. Make commits
  4. git push origin feature/X
  5. Open Pull Request ──────────────► PR appears on repo
                                       Reviewers notified
                                       CI runs tests
                                       ◄─── Comments / requests
  6. Address review feedback
  7. git push (more commits)
  8. ◄─── Approved ──────────────────  Reviewer approves
  9.                                   Merge PR (squash/merge/rebase)
 10.                                   Branch deleted
 11. git switch main && git pull       Feature now in main
```

### Lab: Pull Requests

**Objective**: Create a feature branch, push it, and open a Pull Request on GitHub.

**Estimated time**: 20 minutes

---

**Step 1 – Create a new feature branch**

```bash
cd ~/git-lab-project
git switch main
git pull  # ensure you're up to date

git switch -c feature/add-tests
```

**Step 2 – Add a test file**

```bash
mkdir tests
cat > tests/test_app.py << 'EOF'
import unittest
import sys
import os

# Add the src directory to the path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))


class TestApplication(unittest.TestCase):

    def test_import_succeeds(self):
        """Test that the application module can be imported."""
        try:
            import app
            imported = True
        except ImportError:
            imported = False
        self.assertTrue(imported)

    def test_config_has_required_keys(self):
        """Test that configuration module defines required settings."""
        import config
        self.assertTrue(hasattr(config, 'DATABASE_URL'))
        self.assertTrue(hasattr(config, 'DEBUG'))
        self.assertTrue(hasattr(config, 'SECRET_KEY'))


if __name__ == '__main__':
    unittest.main()
EOF

git add tests/test_app.py
git commit -m "test: add basic unit tests for app and config"
```

**Step 3 – Add a test step to the Makefile**

```bash
cat > Makefile << 'EOF'
.PHONY: run test install clean lint

install:
	pip install -r requirements.txt

run:
	python src/app.py

test:
	python -m pytest tests/ -v

lint:
	flake8 src/ tests/

clean:
	find . -type f -name "*.pyc" -delete
	find . -type d -name "__pycache__" -exec rm -rf {} +
EOF

git add Makefile
git commit -m "chore: add lint and test targets to Makefile"
```

**Step 4 – Push the feature branch**

```bash
git push -u origin feature/add-tests
```

**Step 5 – Open a Pull Request on GitHub**

1. Navigate to your repository on GitHub
2. GitHub will show a banner: **"feature/add-tests had recent pushes"** → Click **Compare & pull request**
3. Fill in the Pull Request form:
    - **Title**: `feat: add unit tests for app and config modules`
    - **Description**:
        
        ```
        ## Summary- Add basic unit tests covering app import and config attribute checks- Update Makefile with `lint` and improved `test` targets## Testing- [x] `make test` passes locally- [x] `make lint` shows no errors## Related IssuesCloses #1
        ```
        
4. Click **Create pull request**

**Step 6 – Review and merge (self-review for this lab)**

1. Click the **Files changed** tab to review the diff
2. Click **Review changes** → **Approve** → **Submit review**
3. Click **Merge pull request** → **Confirm merge**
4. Click **Delete branch**

**Step 7 – Sync your local main branch**

```bash
git switch main
git pull

# Confirm the test files are now on main
ls tests/
git log --oneline -5
```

---

## Fetching and Pulling

### The Difference Between Fetch and Pull

```
git fetch                          git pull
──────────────────                 ─────────────────────────────
Downloads remote changes           Downloads remote changes
Does NOT update your               AND automatically merges them
working files                      into your current branch

Safe to run anytime.               Can cause merge conflicts.
Lets you inspect before merging.   Equivalent to:
                                   git fetch + git merge
```

### `git fetch`

```bash
# Fetch all changes from origin (all branches)
git fetch origin

# Fetch a specific branch
git fetch origin main

# Fetch from all configured remotes
git fetch --all

# Fetch and prune deleted remote branches
git fetch --prune

# After fetching, inspect what changed
git log main..origin/main --oneline
git diff main origin/main
```

### `git pull`

```bash
# Pull (fetch + merge) from tracked upstream
git pull

# Pull from a specific remote and branch
git pull origin main

# Pull using rebase instead of merge (keeps linear history)
git pull --rebase

# Configure pull to always rebase
git config --global pull.rebase true

# Pull and prune deleted remote branches
git pull --prune
```

### Understanding Remote-Tracking Branches

When you fetch, Git stores the remote's state as **remote-tracking branches** (e.g., `origin/main`). These are local read-only references to the last known state of the remote.

```bash
# List all branches including remote-tracking
git branch -a
# * main
#   remotes/origin/HEAD -> origin/main
#   remotes/origin/main
#   remotes/origin/feature/add-tests

# Compare local main with remote main
git log main..origin/main --oneline
# If empty: you're up to date
# If commits shown: remote is ahead of you

# Compare remote main with local main
git log origin/main..main --oneline
# If commits shown: you're ahead of remote (need to push)
```

### Lab: Fetching and Pulling

**Objective**: Simulate a team environment where changes happen on the remote, and practice fetching and pulling safely.

**Estimated time**: 15 minutes

---

**Step 1 – Simulate a remote change using your second clone**

```bash
cd ~/git-lab-project-colleague

git switch main
git pull

cat > docs/architecture.md << 'EOF'
# Architecture Overview

## Components

- **src/app.py**: Main application entry point
- **src/config.py**: Environment-based configuration
- **src/logger.py**: Centralized logging
- **tests/**: Unit test suite

## Environment Variables

| Variable | Default | Description |
|---|---|---|
| DATABASE_URL | postgresql://localhost/myapp | Database connection string |
| DEBUG | false | Enable debug mode |
| SECRET_KEY | change-me-in-production | Application secret |
EOF

mkdir docs
mv docs/architecture.md docs/
git add docs/
git commit -m "docs: add architecture overview"
git push origin main
```

**Step 2 – Back in your main clone, fetch (don't pull yet)**

```bash
cd ~/git-lab-project

# Fetch without merging
git fetch origin

# Inspect what arrived
git log main..origin/main --oneline
# a1b2c3d docs: add architecture overview

# See the actual diff
git diff main origin/main
```

**Step 3 – Review, then merge**

```bash
# You're satisfied with the changes — merge them
git merge origin/main

# Or do both in one step next time:
git pull

ls docs/
```

**Step 4 – Practice rebase-based pull**

```bash
# Make a local commit before pulling
echo "# Local note" >> README.md
git commit -am "docs: local README update"

# Now a remote commit arrives (simulate)
# (switch to colleague clone, make a commit, push, then come back)

# Pull with rebase — replays your commit on top of remote changes
git pull --rebase origin main
```

---

## Merge Conflicts

### What Is a Merge Conflict?

A **merge conflict** occurs when two branches make different changes to the same line(s) of the same file, and Git cannot determine which version to keep automatically. Git pauses the merge and asks you to resolve the conflict manually.

### Anatomy of a Conflict Marker

```
<<<<<<< HEAD
This is the content from your current branch (HEAD)
=======
This is the content from the branch being merged in
>>>>>>> feature/other-branch
```

- Everything between `<<<<<<< HEAD` and `=======` is your version
- Everything between `=======` and `>>>>>>> branch-name` is the incoming version
- You must decide which to keep (or combine both), then remove all conflict markers

### Resolving Conflicts Step by Step

```bash
# 1. Start the merge (conflict occurs)
git merge feature/other-branch
# CONFLICT (content): Merge conflict in src/app.py
# Automatic merge failed; fix conflicts and then commit the result.

# 2. See which files have conflicts
git status
# Both modified: src/app.py

# 3. Open the file and resolve
vim src/app.py   # or use your editor of choice

# 4. Stage the resolved file
git add src/app.py

# 5. Complete the merge
git commit
# Git pre-fills the commit message: "Merge branch 'feature/other-branch'"
```

### Tools for Conflict Resolution

```bash
# Use Git's built-in merge tool
git mergetool

# Configure a specific merge tool
git config --global merge.tool vimdiff
git config --global merge.tool vscode

# VS Code settings for merge tool
git config --global mergetool.vscode.cmd 'code --wait $MERGED'

# Accept "ours" for all conflicts (keep current branch entirely)
git checkout --ours src/app.py
git add src/app.py

# Accept "theirs" for all conflicts (accept incoming entirely)
git checkout --theirs src/app.py
git add src/app.py

# Abort the merge and return to the pre-merge state
git merge --abort
```

### Lab: Merge Conflicts

**Objective**: Deliberately create and then resolve a merge conflict.

**Estimated time**: 20 minutes

---

**Step 1 – Set up two conflicting branches**

```bash
cd ~/git-lab-project
git switch main

# Create branch-a and edit the app title
git switch -c conflict-branch-a

cat > src/app.py << 'EOF'
#!/usr/bin/env python3
"""
DevOps Application - Branch A Version
Enhanced with health checks.
"""
from logger import get_logger

logger = get_logger(__name__)

def health_check():
    return {"status": "healthy", "version": "1.0.0"}

def main():
    logger.info("Application starting up - Branch A")
    print("Hello, DevOps! (Branch A)")
    logger.info("Health check: %s", health_check())

if __name__ == "__main__":
    main()
EOF

git add src/app.py
git commit -m "feat: add health check endpoint (branch A)"
```

**Step 2 – Create a conflicting change on a second branch**

```bash
git switch main

git switch -c conflict-branch-b

cat > src/app.py << 'EOF'
#!/usr/bin/env python3
"""
DevOps Application - Branch B Version
Enhanced with metrics.
"""
from logger import get_logger

logger = get_logger(__name__)

def get_metrics():
    return {"requests": 0, "errors": 0, "uptime": 0}

def main():
    logger.info("Application starting up - Branch B")
    print("Hello, DevOps! (Branch B)")
    logger.info("Metrics: %s", get_metrics())

if __name__ == "__main__":
    main()
EOF

git add src/app.py
git commit -m "feat: add metrics collection (branch B)"
```

**Step 3 – Merge branch-a into main (no conflict)**

```bash
git switch main
git merge conflict-branch-a
# Fast-forward or clean merge
```

**Step 4 – Attempt to merge branch-b (conflict!)**

```bash
git merge conflict-branch-b
# CONFLICT (content): Merge conflict in src/app.py
# Automatic merge failed; fix conflicts and then commit the result.

git status
# On branch main
# You have unmerged paths.
#   (fix conflicts and run "git commit")
#   (use "git merge --abort" to abort the merge)
#
# Unmerged paths:
#   (use "git add <file>..." to mark resolution)
#         both modified:   src/app.py
```

**Step 5 – View the conflict markers**

```bash
cat src/app.py

# Output will show conflict markers:
# <<<<<<< HEAD
# ... Branch A's version ...
# =======
# ... Branch B's version ...
# >>>>>>> conflict-branch-b
```

**Step 6 – Resolve the conflict manually**

Open `src/app.py` in your editor and create a merged version that includes both health check and metrics:

```bash
cat > src/app.py << 'EOF'
#!/usr/bin/env python3
"""
DevOps Application
Enhanced with health checks and metrics.
"""
from logger import get_logger

logger = get_logger(__name__)

def health_check():
    return {"status": "healthy", "version": "1.0.0"}

def get_metrics():
    return {"requests": 0, "errors": 0, "uptime": 0}

def main():
    logger.info("Application starting up")
    print("Hello, DevOps!")
    logger.info("Health check: %s", health_check())
    logger.info("Metrics: %s", get_metrics())

if __name__ == "__main__":
    main()
EOF
```

**Step 7 – Stage the resolution and complete the merge**

```bash
git add src/app.py

git status
# All conflicts fixed but you are still merging.
# (use "git commit" to conclude merge)

git commit
# Git opens your editor with a pre-filled message.
# Save and close to complete the merge.
```

**Step 8 – Verify and clean up**

```bash
git log --oneline --graph --decorate
cat src/app.py   # confirm both functions are present

# Clean up
git branch -d conflict-branch-a
git branch -d conflict-branch-b
git push origin main
```

---

## Forking

### What Is a Fork?

A **fork** is a server-side copy of a repository under your own account. Forking is the standard workflow for contributing to open-source projects where you don't have write access to the original repository.

```
  Original Repository (upstream)        Your Fork (origin)
  ──────────────────────────────        ──────────────────────────
  github.com/linux/linux                github.com/yourname/linux
         │                                      │
         │  Click "Fork" on GitHub             │
         │ ────────────────────────────────────►│
         │                                      │
         │                              git clone (local copy)
         │                                      │
         │                                      ▼
         │                               Your local machine
         │                               (git remote: origin = your fork)
         │
         ◄── Pull Request ── push to your fork ──
```

**Terminology:**

- **upstream**: The original repository you forked from
- **origin**: Your personal fork on GitHub

### Fork Workflow

```bash
# Step 1: Fork on GitHub (click the Fork button)

# Step 2: Clone YOUR fork locally
git clone git@github.com:YOUR_USERNAME/original-repo.git
cd original-repo

# Step 3: Add the original as 'upstream'
git remote add upstream git@github.com:ORIGINAL_OWNER/original-repo.git

# Verify
git remote -v
# origin    git@github.com:YOUR_USERNAME/original-repo.git (fetch)
# origin    git@github.com:YOUR_USERNAME/original-repo.git (push)
# upstream  git@github.com:ORIGINAL_OWNER/original-repo.git (fetch)
# upstream  git@github.com:ORIGINAL_OWNER/original-repo.git (push)

# Step 4: Create a feature branch
git switch -c fix/documentation-typo

# Step 5: Make and commit changes
# ...
git commit -m "fix: correct typo in installation docs"

# Step 6: Push to YOUR fork
git push origin fix/documentation-typo

# Step 7: Open a Pull Request from your fork to the upstream repo
# (GitHub → Compare & pull request → choose upstream:main as base)
```

### Keeping Your Fork Up To Date

The original repository (upstream) will receive new commits from other contributors. You need to sync your fork regularly.

```bash
# Fetch all branches from upstream
git fetch upstream

# Switch to your main branch
git switch main

# Merge upstream changes into your local main
git merge upstream/main

# Push the updated main to your fork
git push origin main

# Or do fetch + merge in one step using pull
git pull upstream main
git push origin main
```

### Lab: Fork

**Objective**: Fork a public repository, clone your fork, add the upstream remote, make a change, and simulate submitting a contribution.

**Estimated time**: 20 minutes

---

**Step 1 – Fork a repository on GitHub**

1. Navigate to a public repository (e.g., `https://github.com/octocat/Spoon-Knife`)
2. Click the **Fork** button in the top-right corner
3. Select your account as the destination
4. GitHub creates a copy at `https://github.com/YOUR_USERNAME/Spoon-Knife`

**Step 2 – Clone your fork**

```bash
cd ~
git clone git@github.com:YOUR_USERNAME/Spoon-Knife.git
cd Spoon-Knife
```

**Step 3 – Add the upstream remote**

```bash
git remote add upstream https://github.com/octocat/Spoon-Knife.git

git remote -v
# origin    git@github.com:YOUR_USERNAME/Spoon-Knife.git (fetch)
# origin    git@github.com:YOUR_USERNAME/Spoon-Knife.git (push)
# upstream  https://github.com/octocat/Spoon-Knife.git (fetch)
# upstream  https://github.com/octocat/Spoon-Knife.git (push)
```

**Step 4 – Sync with upstream**

```bash
git fetch upstream
git switch main
git merge upstream/main
git push origin main
```

**Step 5 – Make a contribution on a feature branch**

```bash
git switch -c docs/improve-readme

cat >> README.md << 'EOF'

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines.

## License

This project is for demonstration purposes.
EOF

git add README.md
git commit -m "docs: add contributing and license sections to README"
git push origin docs/improve-readme
```

**Step 6 – Open a Pull Request to the upstream (on GitHub)**

1. Navigate to the original repository `github.com/octocat/Spoon-Knife`
2. GitHub may show a banner for your recently pushed branch → Click **Compare & pull request**
3. Verify:
    - **Base repository**: `octocat/Spoon-Knife` → `main`
    - **Head repository**: `YOUR_USERNAME/Spoon-Knife` → `docs/improve-readme`
4. Write a meaningful PR description and submit

> **Note**: The `octocat/Spoon-Knife` repository is a practice repository. Submitted PRs there are never actually merged — it's safe to practice.

**Step 7 – Practice the full fork sync cycle**

```bash
# After time passes and upstream gets new commits:
git fetch upstream

# See what's new
git log main..upstream/main --oneline

# Sync
git switch main
git rebase upstream/main
git push origin main --force-with-lease  # force needed after rebase
```

---

## Module 2 Assessment

### Knowledge Check

**Question 1**: What is the difference between `git clone` and `git fork`? Which is a Git command and which is a GitHub feature?

**Question 2**: Explain the difference between `origin` and `upstream` in a fork-based workflow.

**Question 3**: What does `git fetch --prune` do? When would you use it?

**Question 4**: You ran `git pull` and got a merge conflict. Walk through the exact steps to resolve it and complete the pull.

**Question 5**: Your colleague has pushed 5 commits to the remote `main` branch. You also have 3 local commits that haven't been pushed yet. What happens when you run `git pull --rebase`? Draw the resulting commit graph.

**Question 6**: What is the risk of `git push --force`? What safer alternative should you use instead and why?

**Question 7**: Describe a Pull Request review checklist. What at minimum should a reviewer check before approving?

### Practical Exercises

**Exercise 1**: Fork any public repository on GitHub. Clone your fork. Create two branches: one that adds a `.editorconfig` file and one that adds a `SECURITY.md` file. Push both branches and create Pull Requests for each. Include a meaningful PR description for both.

**Exercise 2**: Simulate a team conflict. In `git-lab-project`, have "colleague" (your second clone) modify line 5 of `README.md` and push. You also modify line 5 locally. Pull and resolve the conflict using the merge strategy that preserves both changes as separate sentences.

**Exercise 3**: Set up a complete fork workflow for an open-source Python project:

- Fork the repository
- Clone your fork
- Configure upstream
- Create a feature branch
- Make a meaningful code improvement or documentation fix
- Push to your fork
- Open a PR with a professional description including: summary, motivation, testing instructions, and screenshots (if applicable)

---

# Quick Reference Card

## Essential Commands

```bash
# ─── Setup ───────────────────────────────────────────────────
git config --global user.name "Your Name"
git config --global user.email "you@example.com"

# ─── Start a Repo ────────────────────────────────────────────
git init                          # Initialize new local repo
git clone <url>                   # Clone a remote repo

# ─── Daily Workflow ──────────────────────────────────────────
git status                        # Check working tree state
git diff                          # Show unstaged changes
git diff --staged                 # Show staged changes
git add <file>                    # Stage specific file
git add .                         # Stage all changes
git commit -m "message"           # Commit staged changes
git commit -am "message"          # Stage tracked files + commit

# ─── Undoing Changes ─────────────────────────────────────────
git restore <file>                # Discard working dir changes
git restore --staged <file>       # Unstage a file
git commit --amend                # Fix last commit (before push!)
git reset HEAD~1                  # Undo last commit, keep changes
git reset --hard HEAD~1           # Undo last commit, discard changes

# ─── Branching ───────────────────────────────────────────────
git branch                        # List local branches
git branch -a                     # List all branches
git switch -c <branch>            # Create and switch
git switch <branch>               # Switch to branch
git branch -d <branch>            # Delete (safe)
git branch -D <branch>            # Force delete

# ─── Merging ─────────────────────────────────────────────────
git merge <branch>                # Merge into current branch
git merge --no-ff <branch>        # Force merge commit
git merge --squash <branch>       # Squash all commits into one
git merge --abort                 # Cancel in-progress merge

# ─── Remote Repositories ────────────────────────────────────
git remote -v                     # List remotes
git remote add origin <url>       # Add remote
git push -u origin <branch>       # Push + set upstream
git push                          # Push to tracked upstream
git push origin --delete <branch> # Delete remote branch

# ─── Fetch and Pull ──────────────────────────────────────────
git fetch origin                  # Download remote changes
git fetch --all --prune           # Fetch all, prune deleted
git pull                          # Fetch + merge
git pull --rebase                 # Fetch + rebase

# ─── Inspection ──────────────────────────────────────────────
git log --oneline --graph --all   # Visual branch history
git log --stat                    # Files changed per commit
git log -p                        # Full diffs per commit
git show <hash>                   # Inspect a commit
git diff <branch1>..<branch2>     # Compare branches

# ─── Fork Workflow ───────────────────────────────────────────
git remote add upstream <url>     # Add original repo as upstream
git fetch upstream                # Get upstream changes
git merge upstream/main           # Sync local with upstream
git push origin main              # Push sync to your fork
```

## Conflict Resolution Cheat Sheet

```
1. git status                  ← See conflicted files
2. Edit file, remove markers   ← <<<<<<< = ======= >>>>>>>
3. git add <resolved-file>     ← Mark as resolved
4. git commit                  ← Complete the merge
```

## Branch Naming Conventions

|Pattern|Example|Use for|
|---|---|---|
|`feature/`|`feature/user-auth`|New features|
|`fix/`|`fix/login-crash`|Bug fixes|
|`hotfix/`|`hotfix/security-patch`|Urgent production fixes|
|`docs/`|`docs/api-reference`|Documentation updates|
|`chore/`|`chore/update-deps`|Tooling, maintenance|
|`ci/`|`ci/add-lint-step`|CI/CD changes|
|`release/`|`release/v2.1.0`|Release preparation|

## Git Workflow Models

|Workflow|Best For|Key Branches|
|---|---|---|
|**GitHub Flow**|Web apps, continuous delivery|`main` + feature branches|
|**Git Flow**|Scheduled releases|`main`, `develop`, `feature/*`, `release/*`, `hotfix/*`|
|**Trunk-Based**|High-frequency CI/CD|Single `main` with short-lived branches|
|**Forking Workflow**|Open source contributions|upstream `main` + personal forks|

---

_End of Git Basics for DevOps — Course 2_

> **Next in the series**: Course 3 – Jenkins for Beginners covers CI/CD automation that builds on the Git workflows you've mastered here.