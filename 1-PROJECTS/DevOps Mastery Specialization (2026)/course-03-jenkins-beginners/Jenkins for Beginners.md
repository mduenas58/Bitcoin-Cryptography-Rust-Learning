# Jenkins for Beginners

## Course 3 – A Comprehensive Tutorial with Hands-On Labs

---

> **About This Course**
> 
> This course is designed for developers, DevOps engineers, and system administrators who want to learn Jenkins from the ground up. You will progress from understanding CI/CD concepts and installing Jenkins, through system administration and backup procedures, all the way to writing production-grade pipelines as code. Every module includes concept explanations, guided demonstrations, and hands-on labs with full solutions.

---

## Table of Contents

- [Module 1 – Introduction and Getting Started with Jenkins](https://claude.ai/local_sessions/local_c16524e5-1c07-464f-ba05-5cd93beac4e2#module-1--introduction-and-getting-started-with-jenkins)
- [Module 2 – Installing Jenkins](https://claude.ai/local_sessions/local_c16524e5-1c07-464f-ba05-5cd93beac4e2#module-2--installing-jenkins)
- [Module 3 – System Administration with Jenkins](https://claude.ai/local_sessions/local_c16524e5-1c07-464f-ba05-5cd93beac4e2#module-3--system-administration-with-jenkins)
- [Module 4 – Jenkins Pipelines](https://claude.ai/local_sessions/local_c16524e5-1c07-464f-ba05-5cd93beac4e2#module-4--jenkins-pipelines)

---

# Module 1 – Introduction and Getting Started with Jenkins

## Module Overview

This module introduces Jenkins and its crucial role in modern software development. Learners explore how Jenkins automates the software delivery lifecycle through Continuous Integration and Continuous Deployment (CI/CD), examine its key features, and gain hands-on experience navigating and using the application.

### Learning Objectives

- Understand the concept of CI/CD and its importance in modern software development
- Explore the reasons for choosing Jenkins as a CI/CD tool and its advantages
- Get started with Jenkins by learning the basics of installation, configuration, and usage
- Understand the purpose and function of Jenkins in the software development lifecycle

---

## 1.1 What is CI/CD?

### The Problem: Manual Software Delivery

Before CI/CD, software teams followed a pattern that created enormous risk and pain:

- Developers worked in isolation for weeks or months on separate feature branches
- Code was merged all at once just before a release — called "integration hell"
- The merged codebase was riddled with conflicts and bugs
- Manual testing took days or weeks
- Deployments were rare, high-risk events requiring all-hands-on-deck

This approach produced slow release cycles, fragile software, and burned-out teams.

### Continuous Integration (CI)

**Continuous Integration** is the practice of frequently merging code changes from all developers into a shared repository — ideally multiple times per day. Each merge triggers an automated pipeline that:

1. Checks out the latest code
2. Compiles/builds the application
3. Runs the full automated test suite
4. Reports success or failure immediately to the team

```
Developer commits code
        │
        ▼
  Source Control (Git)
        │  Webhook trigger
        ▼
  CI Server (Jenkins)
  ┌─────────────────────────────────┐
  │  1. Checkout code               │
  │  2. Install dependencies        │
  │  3. Build / Compile             │
  │  4. Run unit tests              │
  │  5. Run integration tests       │
  │  6. Static code analysis        │
  │  7. Generate test reports       │
  └──────────────┬──────────────────┘
                 │
        ┌────────┴────────┐
        ▼                 ▼
   ✅ PASS            ❌ FAIL
   Notify team        Notify developer
   Proceed to CD      Fix immediately
```

**Key CI Principles:**

- Everyone commits to the main branch frequently
- Every commit triggers an automated build
- The build must pass — fixing a broken build is the team's top priority
- Keep builds fast (under 10 minutes)
- Test in a production-like environment

### Continuous Delivery (CD)

**Continuous Delivery** extends CI by automatically deploying every successful build to a staging environment, where it can be tested further before being manually approved for production release.

### Continuous Deployment (CD)

**Continuous Deployment** goes one step further — every change that passes all automated tests is automatically deployed straight to production, with no human approval step.

```
CI Pipeline                CD Pipeline
───────────────            ─────────────────────────────────────
Code → Build →             Staging → Acceptance Tests → Production
Test → Package             (auto)        (auto)         (auto or manual)
```

|Concept|Automation Level|Human Approval|
|---|---|---|
|**Continuous Integration**|Build + Test|N/A|
|**Continuous Delivery**|Build + Test + Stage|Required before prod|
|**Continuous Deployment**|Build + Test + Stage + Prod|None|

### Why CI/CD Matters

|Without CI/CD|With CI/CD|
|---|---|
|Releases every few months|Releases daily or many times per day|
|Large, risky deployments|Small, safe incremental changes|
|Bugs found late and expensive to fix|Bugs caught immediately after commit|
|Manual, error-prone deployment|Automated, repeatable deployment|
|Blame and finger-pointing|Shared responsibility and transparency|
|Long feedback loops|Immediate feedback to developers|

---

## 1.2 Why Jenkins?

### What is Jenkins?

**Jenkins** is an open-source automation server written in Java. It is the most widely used CI/CD tool in the world, with over 1.8 million active installations. Jenkins enables teams to automate the building, testing, and deployment of software through configurable pipelines and a vast plugin ecosystem.

```
┌──────────────────────────────────────────────────────────────┐
│                     Jenkins Server                            │
│                                                              │
│  ┌─────────────┐  ┌──────────────┐  ┌──────────────────┐   │
│  │   Source    │  │  Build &     │  │   Deploy to      │   │
│  │  Control    │─▶│  Test        │─▶│   Environments   │   │
│  │  (Git/SVN)  │  │  Automation  │  │  (Stage/Prod)    │   │
│  └─────────────┘  └──────────────┘  └──────────────────┘   │
│                                                              │
│  1,800+ Plugins  │  Distributed Builds  │  Pipeline as Code │
└──────────────────────────────────────────────────────────────┘
```

### Key Reasons to Choose Jenkins

**1. Open Source and Free** Jenkins is completely free and open source under the MIT license. There are no licensing costs regardless of how many jobs, users, or agents you run.

**2. Massive Plugin Ecosystem** Jenkins has over 1,800 community-contributed plugins covering integration with virtually every tool in the DevOps ecosystem:

- Source control: Git, GitHub, GitLab, Bitbucket, SVN
- Build tools: Maven, Gradle, npm, Make, Ant
- Testing: JUnit, Selenium, SonarQube, Cucumber
- Cloud: AWS, GCP, Azure, Kubernetes
- Notification: Slack, email, PagerDuty, JIRA
- Deployment: Docker, Ansible, Terraform, Kubernetes

**3. Pipeline as Code** Jenkins Pipelines (Jenkinsfile) allow you to define your entire CI/CD pipeline in code, stored alongside your application in source control. This means:

- Pipelines are versioned and auditable
- Developers can review and modify pipeline logic via pull requests
- Pipelines are reproducible across environments

**4. Distributed Builds** Jenkins uses a Master-Agent architecture. The master (controller) manages jobs and UI while agents (workers) execute the actual build steps. This enables:

- Parallel execution across many machines
- Builds on different OS/architecture combinations (Linux, Windows, macOS)
- Scaling build capacity independently of the controller

**5. Highly Extensible** Beyond plugins, Jenkins can be extended with shared libraries, custom steps, and integrations with any tool that has a command-line interface or REST API.

**6. Large Community and Maturity** Jenkins has been in continuous development since 2011 and has an enormous community. Documentation, tutorials, and help are widely available.

### Jenkins Architecture

```
┌─────────────────────────────────────────────────────────────┐
│                    Jenkins Controller                        │
│                                                             │
│  Web UI  │  REST API  │  Job Scheduler  │  Plugin Manager  │
│                                                             │
│  ┌──────────────────────────────────────────────────────┐  │
│  │                    Build Queue                        │  │
│  └──────────────────────────────────────────────────────┘  │
└─────────────────────┬───────────────────────────────────────┘
                      │ Agent Protocol (SSH / JNLP)
          ┌───────────┼───────────┐
          ▼           ▼           ▼
    ┌──────────┐ ┌──────────┐ ┌──────────┐
    │ Agent 1  │ │ Agent 2  │ │ Agent 3  │
    │ (Linux)  │ │ (Windows)│ │ (Docker) │
    │          │ │          │ │          │
    │ Executes │ │ Executes │ │ Executes │
    │ Pipeline │ │ Pipeline │ │ Pipeline │
    └──────────┘ └──────────┘ └──────────┘
```

**Controller (Master):**

- Serves the web UI and REST API
- Stores all configuration (jobs, credentials, plugins)
- Schedules builds and dispatches them to agents
- Collects and presents build results

**Agents (Workers):**

- Execute the actual pipeline steps
- Can run on bare metal, VMs, containers, or cloud instances
- Are labeled so jobs can target specific agent types
- Can be brought online/offline dynamically

### Jenkins vs. Other CI/CD Tools

|Feature|Jenkins|GitHub Actions|GitLab CI|CircleCI|
|---|---|---|---|---|
|**Cost**|Free (self-hosted)|Free tier + paid|Free tier + paid|Free tier + paid|
|**Hosting**|Self-hosted|Cloud / self-hosted|Cloud / self-hosted|Cloud / self-hosted|
|**Plugin ecosystem**|1,800+ plugins|Marketplace actions|Templates|Orbs|
|**Pipeline as code**|Jenkinsfile (Groovy)|YAML|YAML|YAML|
|**Flexibility**|Very high|High|High|High|
|**Setup complexity**|Higher|Low|Low|Low|
|**Best for**|Large enterprises, complex needs|GitHub-hosted projects|GitLab projects|Simpler cloud CI|

---

## 1.3 Jenkins Getting Started

### Jenkins UI Overview

When you first log into Jenkins, you see the **Dashboard**. Here is a map of the key areas:

```
┌────────────────────────────────────────────────────────────────┐
│  Jenkins                          🔍 Search   👤 admin   ⚙️   │
├────────────────────────────────────────────────────────────────┤
│  ┌──────────────┐  ┌────────────────────────────────────────┐  │
│  │ Navigation   │  │           Main Panel                   │  │
│  │              │  │                                        │  │
│  │ Dashboard    │  │  ┌──────────────────────────────────┐  │  │
│  │ My Views     │  │  │  All Jobs Table                  │  │  │
│  │ Build Queue  │  │  │  S  W  Job Name  Last Success    │  │  │
│  │ Build Exec   │  │  │  ✅  ☀  my-app   2 min ago      │  │  │
│  │ Status       │  │  │  ❌  ⛈  my-api   1 hr ago       │  │  │
│  │              │  │  └──────────────────────────────────┘  │  │
│  │ New Item     │  │                                        │  │
│  │ People       │  │  Build Queue: (empty)                  │  │
│  │ Build History│  │                                        │  │
│  │ Manage       │  │  Build Executor Status:                │  │
│  │ Jenkins      │  │  #1 Idle                               │  │
│  │              │  │  #2 Building my-app #42               │  │
│  └──────────────┘  └────────────────────────────────────────┘  │
└────────────────────────────────────────────────────────────────┘
```

**Key Navigation Areas:**

|Area|Purpose|
|---|---|
|**New Item**|Create a new Job, Pipeline, or Folder|
|**People**|View all users and their recent activity|
|**Build History**|Timeline of all recent builds across all jobs|
|**Manage Jenkins**|System configuration, plugins, credentials, security|
|**My Views**|Customizable views filtering jobs by criteria|
|**Build Queue**|Jobs waiting to be executed|
|**Build Executor Status**|Shows which executors are idle or busy|

### Core Jenkins Concepts

**Job / Project** A Job (also called a Project) is the fundamental unit of work in Jenkins. A Job defines what to build, how to build it, and what to do with the results. Job types include:

- **Freestyle Project** — Simple GUI-configured jobs; good for beginners
- **Pipeline** — Pipeline-as-code jobs using Jenkinsfile
- **Multibranch Pipeline** — Automatically creates jobs for each branch/PR in a repo
- **Folder** — Organizes jobs hierarchically

**Build** Each execution of a Job is called a Build. Builds are numbered sequentially (#1, #2, #3...) and each has its own log, artifacts, and status.

**Workspace** Each Job has a Workspace — a directory on the agent where the build runs. Source code is checked out here, and build artifacts are produced here.

**Artifact** Files produced by a build that are worth preserving — compiled binaries, test reports, Docker images, deployment packages.

**Executor** A thread of execution on an agent. An agent with 2 executors can run 2 builds simultaneously.

**Node / Agent** A machine that executes build jobs. The built-in node is the controller itself (used in simple setups). Additional agents are added as the team scales.

**Credentials** Secure storage for passwords, SSH keys, API tokens, and certificates. Jenkins encrypts these and injects them into builds without exposing them in logs.

---

## 🧪 Hands-on Lab: Get Familiar with the Application

### Lab Objectives

- Navigate the Jenkins web interface confidently
- Create your first Freestyle job
- Trigger a build manually and inspect its output
- Explore job configuration options

### Lab Duration: 30 minutes

---

### Exercise 1: Explore the Jenkins Dashboard

```
1. Open your browser and navigate to your Jenkins instance:
   http://localhost:8080   (or your server's IP)

2. Log in with your admin credentials.

3. On the Dashboard, identify:
   - The Build Queue panel (bottom-left)
   - The Build Executor Status panel
   - The job table in the center

4. Click "Manage Jenkins" in the left sidebar.
   Explore the following sections:
   - System Configuration → System (global settings)
   - System Configuration → Plugins (installed plugins)
   - Security → Manage Users
   - Status Information → System Information

5. Return to the Dashboard by clicking the Jenkins logo (top-left).
```

---

### Exercise 2: Create Your First Freestyle Job

```
1. Click "New Item" in the left sidebar.

2. Enter the item name: hello-jenkins

3. Select "Freestyle project" and click OK.

4. On the configuration page:

   a. Under "Description", enter:
      My first Jenkins job - prints a hello message

   b. Scroll to "Build Steps" section.
      Click "Add build step" → "Execute shell"

   c. In the command box, enter:
      #!/bin/bash
      echo "==============================="
      echo "  Hello from Jenkins!"
      echo "  Build Number: $BUILD_NUMBER"
      echo "  Build URL: $BUILD_URL"
      echo "  Workspace: $WORKSPACE"
      echo "  Job Name: $JOB_NAME"
      echo "==============================="
      date
      whoami
      hostname

5. Click "Save".
```

---

### Exercise 3: Run the Job and Inspect Results

```
1. On the job page, click "Build Now" in the left sidebar.

2. In the "Build History" panel (bottom-left), a new build #1 appears.
   Click on "#1" to open the build.

3. Click "Console Output" in the left sidebar.
   You should see your echo statements and the environment variables.

4. Note the environment variables Jenkins automatically provides:
   - BUILD_NUMBER: sequential build counter
   - BUILD_URL: direct link to this build
   - WORKSPACE: the directory where the build runs
   - JOB_NAME: the name of the job

5. Go back to the job's main page.
   Run the build 2 more times by clicking "Build Now".

6. Observe the build history — three builds, each numbered sequentially.
   Click each build to compare their console outputs.
   Notice BUILD_NUMBER increments each time.
```

---

### Exercise 4: Configure Build Triggers

```
1. Go back to the job configuration (click "Configure" in the sidebar).

2. In the "Build Triggers" section, check "Build periodically".

3. Enter the schedule: H/5 * * * *
   (This runs every 5 minutes; H means "hash" - Jenkins distributes
   load by hashing the job name to pick a minute within the window)

4. Click "Save".

5. Observe that Jenkins will now automatically trigger the job
   every 5 minutes.

6. Go back to Configure and remove the schedule (uncheck "Build
   periodically") to avoid unnecessary builds during the rest of the lab.
   Click Save.
```

---

## 1.4 Planning Your Jenkins Implementation Journey

Before diving into a Jenkins implementation, plan these key decisions:

### Infrastructure Planning

```
Small Team (< 10 devs):
  • Single Jenkins controller
  • 1-2 agents (can start with just the controller)
  • 4 CPUs, 8 GB RAM for controller
  • Sufficient for ~50 concurrent builds/day

Medium Team (10-50 devs):
  • Dedicated controller (no builds on controller)
  • 3-10 agents based on build frequency
  • Consider agent autoscaling (Kubernetes agents, EC2 agents)

Large Organization (50+ devs):
  • High-availability controller setup
  • Dynamic cloud agents (spin up/down as needed)
  • Dedicated agents for specific platforms (Windows, macOS)
  • Centralized artifact repository (Nexus, Artifactory)
```

### Key Decisions to Make

1. **Hosting**: On-premises VM, cloud VM, Kubernetes, or managed service?
2. **Agent strategy**: Static agents, dynamic cloud agents, or Docker agents?
3. **Plugin selection**: Which plugins are essential for your toolchain?
4. **Security model**: Who can create jobs? Who can approve production deploys?
5. **Credential management**: Integrate with Vault or use Jenkins' built-in credential store?
6. **Pipeline strategy**: Shared library for common steps? Standard Jenkinsfile template?
7. **Backup strategy**: How often? Where? How to test restores?

---

# Module 2 – Installing Jenkins

## Module Overview

This module equips participants with the skills to set up Jenkins on various platforms. Participants learn how to install Jenkins on a virtual machine and how to use the Jenkins Command Line Interface (CLI) for administrative tasks.

### Learning Objectives

- Learn how to install Jenkins on different platforms, including virtual machines
- Gain practical experience in installing Jenkins on a virtual machine through hands-on lab exercises
- Understand the basics of Jenkins Command Line Interface (CLI) and its usage
- Explore the functionalities of Jenkins CLI through hands-on lab exercises

---

## 2.1 Installing Jenkins

### System Requirements

|Component|Minimum|Recommended|
|---|---|---|
|**RAM**|256 MB|4 GB+|
|**Disk**|1 GB|50 GB+|
|**Java**|Java 11|Java 17 (LTS)|
|**OS**|Any Java-compatible|Linux (Ubuntu/RHEL)|

### Installation on Ubuntu/Debian

```bash
# Step 1: Update system packages
sudo apt update && sudo apt upgrade -y

# Step 2: Install Java (Jenkins requires Java 11 or 17)
sudo apt install -y openjdk-17-jdk

# Verify Java installation
java -version
# Expected: openjdk version "17.x.x"

# Step 3: Add the Jenkins GPG key and repository
curl -fsSL https://pkg.jenkins.io/debian-stable/jenkins.io-2023.key | \
  sudo tee /usr/share/keyrings/jenkins-keyring.asc > /dev/null

echo deb [signed-by=/usr/share/keyrings/jenkins-keyring.asc] \
  https://pkg.jenkins.io/debian-stable binary/ | \
  sudo tee /etc/apt/sources.list.d/jenkins.list > /dev/null

# Step 4: Install Jenkins
sudo apt update
sudo apt install -y jenkins

# Step 5: Start and enable Jenkins
sudo systemctl start jenkins
sudo systemctl enable jenkins

# Step 6: Check Jenkins status
sudo systemctl status jenkins
# Expected: Active: active (running)

# Step 7: Open firewall port 8080 (if UFW is active)
sudo ufw allow 8080
sudo ufw status

# Step 8: Get the initial admin password
sudo cat /var/lib/jenkins/secrets/initialAdminPassword
# Copy this password — you'll need it for the setup wizard
```

### Installation on RHEL/CentOS/Fedora

```bash
# Step 1: Install Java
sudo dnf install -y java-17-openjdk

# Step 2: Add Jenkins repository
sudo wget -O /etc/yum.repos.d/jenkins.repo \
  https://pkg.jenkins.io/redhat-stable/jenkins.repo

sudo rpm --import https://pkg.jenkins.io/redhat-stable/jenkins.io-2023.key

# Step 3: Install Jenkins
sudo dnf install -y jenkins

# Step 4: Start and enable
sudo systemctl start jenkins
sudo systemctl enable jenkins

# Step 5: Open firewall
sudo firewall-cmd --permanent --zone=public --add-port=8080/tcp
sudo firewall-cmd --reload

# Step 6: Get the initial admin password
sudo cat /var/lib/jenkins/secrets/initialAdminPassword
```

### Installation via Docker (Quickest Method)

```bash
# Run Jenkins in a Docker container
docker run -d \
  --name jenkins \
  --restart unless-stopped \
  -p 8080:8080 \
  -p 50000:50000 \
  -v jenkins_home:/var/jenkins_home \
  jenkins/jenkins:lts-jdk17

# Get the initial admin password
docker exec jenkins cat /var/jenkins_home/secrets/initialAdminPassword

# View Jenkins logs
docker logs -f jenkins
```

### Jenkins Setup Wizard

After installation, navigate to `http://localhost:8080` (or `http://YOUR_SERVER_IP:8080`):

```
Step 1: Unlock Jenkins
  - Paste the initialAdminPassword you retrieved
  - Click "Continue"

Step 2: Customize Jenkins
  - Choose "Install suggested plugins" for a sensible default set
    (Git, Pipeline, Blue Ocean, etc.)
  - OR choose "Select plugins to install" for custom selection
  - Wait for plugins to download and install

Step 3: Create First Admin User
  - Fill in: username, password, full name, email
  - Click "Save and Continue"
  - (Or click "Skip and continue as admin" to keep the admin/password combo)

Step 4: Instance Configuration
  - Confirm the Jenkins URL (defaults to http://localhost:8080/)
  - This URL is used in email notifications and Git webhooks
  - Click "Save and Finish"

Step 5: Jenkins is Ready!
  - Click "Start using Jenkins"
```

### Jenkins Directory Structure

Understanding where Jenkins stores things is essential for administration:

```
/var/lib/jenkins/                 ← JENKINS_HOME (main data directory)
├── config.xml                    ← Main Jenkins configuration
├── credentials.xml               ← Stored credentials (encrypted)
├── plugins/                      ← Installed plugins
│   ├── git/
│   ├── workflow-aggregator/
│   └── ...
├── jobs/                         ← All job configurations
│   ├── my-pipeline/
│   │   ├── config.xml            ← Job configuration
│   │   └── builds/               ← Build history and logs
│   │       ├── 1/
│   │       │   ├── log           ← Console output
│   │       │   └── build.xml     ← Build metadata
│   │       └── 2/
│   └── another-job/
├── nodes/                        ← Agent/node configurations
├── secrets/                      ← Encrypted secrets
│   └── initialAdminPassword
├── workspace/                    ← Build workspaces (per job)
│   ├── my-pipeline/
│   └── another-job/
├── logs/                         ← Jenkins application logs
└── updates/                      ← Plugin update data
```

---

## 🧪 Hands-on Lab: Install Jenkins on a VM

### Lab Duration: 45 minutes

---

### Exercise 1: Full Installation from Scratch

```bash
# This exercise assumes a fresh Ubuntu 22.04 VM

# ── STEP 1: System Preparation ──────────────────────────────
sudo apt update && sudo apt upgrade -y
sudo apt install -y curl wget gnupg2 software-properties-common

# ── STEP 2: Install Java 17 ─────────────────────────────────
sudo apt install -y openjdk-17-jdk
java -version

# Set JAVA_HOME environment variable
echo 'export JAVA_HOME=$(dirname $(dirname $(readlink -f $(which java))))' \
  >> ~/.bashrc
source ~/.bashrc
echo $JAVA_HOME

# ── STEP 3: Install Jenkins ──────────────────────────────────
curl -fsSL https://pkg.jenkins.io/debian-stable/jenkins.io-2023.key | \
  sudo tee /usr/share/keyrings/jenkins-keyring.asc > /dev/null

echo deb [signed-by=/usr/share/keyrings/jenkins-keyring.asc] \
  https://pkg.jenkins.io/debian-stable binary/ | \
  sudo tee /etc/apt/sources.list.d/jenkins.list > /dev/null

sudo apt update
sudo apt install -y jenkins

# ── STEP 4: Configure and Start Jenkins ─────────────────────
sudo systemctl start jenkins
sudo systemctl enable jenkins
sudo systemctl status jenkins

# ── STEP 5: Retrieve Admin Password ─────────────────────────
echo "Initial Admin Password:"
sudo cat /var/lib/jenkins/secrets/initialAdminPassword

# ── STEP 6: Configure Firewall ──────────────────────────────
sudo ufw allow OpenSSH
sudo ufw allow 8080/tcp
sudo ufw --force enable
sudo ufw status

# ── STEP 7: Complete the Web Setup ───────────────────────────
# Open browser: http://YOUR_VM_IP:8080
# - Enter the password retrieved above
# - Install suggested plugins
# - Create admin user: admin / admin123
# - Accept the default Jenkins URL
# - Click "Start using Jenkins"

# ── STEP 8: Verify Installation ──────────────────────────────
# Create a test job:
# 1. Click "New Item"
# 2. Name it: install-test
# 3. Select "Freestyle project" → OK
# 4. Add build step → Execute shell:
#    echo "Jenkins installed successfully on $(hostname)"
#    java -version
#    cat /etc/os-release | grep PRETTY
# 5. Save → Build Now → Console Output
```

---

## 2.2 Jenkins CLI

### What is the Jenkins CLI?

The **Jenkins CLI** (Command Line Interface) allows you to interact with Jenkins programmatically via the command line. This is essential for:

- Scripting administrative tasks
- Automating job creation and management
- Integrating Jenkins into infrastructure-as-code workflows
- Remote administration without opening a browser

### Setting Up Jenkins CLI

```bash
# Step 1: Download the CLI JAR from your Jenkins instance
curl -O http://localhost:8080/jnlpJars/jenkins-cli.jar

# Verify download
ls -la jenkins-cli.jar

# Step 2: Test connectivity
java -jar jenkins-cli.jar -s http://localhost:8080/ help

# Step 3: Authenticate with username and API token
# First, get your API token from the Jenkins UI:
# Click your username (top right) → Configure → API Token → Add new Token
# Give it a name (e.g., "cli-token") and click Generate
# COPY THE TOKEN — it will only be shown once!

# Step 4: Set up credentials for CLI
# Option A: Environment variables
export JENKINS_URL=http://localhost:8080
export JENKINS_USER=admin
export JENKINS_TOKEN=your-api-token-here

# Option B: Create a credential file
echo "admin:your-api-token-here" > ~/.jenkins-credentials
chmod 600 ~/.jenkins-credentials

# Test authentication
java -jar jenkins-cli.jar \
  -s http://localhost:8080 \
  -auth admin:your-api-token-here \
  who-am-i
# Expected: Authenticated as: admin
```

### Common Jenkins CLI Commands

```bash
# ─── SETUP HELPER ─────────────────────────────────────────────
# Create a shell alias to avoid repeating the java -jar prefix
alias jcli='java -jar /path/to/jenkins-cli.jar -s http://localhost:8080 -auth admin:TOKEN'

# ─── INFORMATION COMMANDS ─────────────────────────────────────

# List all installed plugins
jcli list-plugins

# List all jobs
jcli list-jobs

# Get Jenkins version info
jcli version

# Show who you're authenticated as
jcli who-am-i

# ─── JOB MANAGEMENT ───────────────────────────────────────────

# Build a job
jcli build my-pipeline

# Build with parameters
jcli build my-pipeline -p ENVIRONMENT=staging -p VERSION=1.5.0

# Build and wait for completion
jcli build my-pipeline -s

# Build, wait, and show console output
jcli build my-pipeline -s -v

# Get the console output of the last build
jcli console my-pipeline

# Get console output for a specific build number
jcli console my-pipeline 42

# Enable/disable a job
jcli enable-job my-pipeline
jcli disable-job my-pipeline

# Delete a job
jcli delete-job old-job

# ─── JOB CONFIGURATION ────────────────────────────────────────

# Get a job's configuration as XML
jcli get-job my-pipeline > my-pipeline-config.xml

# Update a job configuration from XML
jcli update-job my-pipeline < my-pipeline-config.xml

# Create a new job from XML
jcli create-job new-job < new-job-config.xml

# ─── PLUGIN MANAGEMENT ────────────────────────────────────────

# Install a plugin (requires restart)
jcli install-plugin git
jcli install-plugin pipeline-model-definition

# ─── NODE/AGENT MANAGEMENT ────────────────────────────────────

# List all nodes
jcli list-nodes

# Take a node offline
jcli offline-node agent-1 -m "Maintenance window"

# Bring a node back online
jcli online-node agent-1

# Delete a node
jcli delete-node old-agent

# ─── SYSTEM COMMANDS ──────────────────────────────────────────

# Reload configuration from disk
jcli reload-configuration

# Restart Jenkins gracefully (waits for builds to finish)
jcli safe-restart

# Restart immediately
jcli restart

# Shutdown gracefully
jcli safe-shutdown

# Quiet mode (no new builds, waits for running builds)
jcli quiet-down

# Cancel quiet mode
jcli cancel-quiet-down

# Run a Groovy script on the server
jcli groovy = < my-script.groovy
```

### Creating Jobs via CLI

```bash
# Create a job from an XML template
# First, create the XML definition:
cat > hello-cli-job.xml << 'EOF'
<?xml version='1.1' encoding='UTF-8'?>
<project>
  <description>Job created via Jenkins CLI</description>
  <keepDependencies>false</keepDependencies>
  <properties/>
  <scm class="hudson.scm.NullSCM"/>
  <canRoam>true</canRoam>
  <disabled>false</disabled>
  <blockBuildWhenDownstreamBuilding>false</blockBuildWhenDownstreamBuilding>
  <blockBuildWhenUpstreamBuilding>false</blockBuildWhenUpstreamBuilding>
  <triggers/>
  <concurrentBuild>false</concurrentBuild>
  <builders>
    <hudson.tasks.Shell>
      <command>
echo "This job was created via the Jenkins CLI!"
echo "Build: $BUILD_NUMBER"
echo "Date: $(date)"
      </command>
    </hudson.tasks.Shell>
  </builders>
  <publishers/>
  <buildWrappers/>
</project>
EOF

# Create the job
java -jar jenkins-cli.jar \
  -s http://localhost:8080 \
  -auth admin:TOKEN \
  create-job hello-cli-job \
  < hello-cli-job.xml

# Verify it was created
java -jar jenkins-cli.jar \
  -s http://localhost:8080 \
  -auth admin:TOKEN \
  list-jobs

# Trigger a build
java -jar jenkins-cli.jar \
  -s http://localhost:8080 \
  -auth admin:TOKEN \
  build hello-cli-job -s -v
```

---

## 🧪 Hands-on Lab: Jenkins CLI

### Lab Duration: 45 minutes

---

### Exercise 1: CLI Setup and Basic Commands

```bash
# Step 1: Download CLI jar
cd ~
curl -O http://localhost:8080/jnlpJars/jenkins-cli.jar

# Step 2: Generate API Token in the UI
# Navigate to: http://localhost:8080 → admin (top right) → Configure
# → API Token → Add new Token → Name: "lab-token" → Generate
# Copy the token!

# Step 3: Set up environment
export JENKINS_URL="http://localhost:8080"
export JENKINS_AUTH="admin:PASTE_YOUR_TOKEN_HERE"

# Create alias for convenience
alias jcli="java -jar ~/jenkins-cli.jar -s $JENKINS_URL -auth $JENKINS_AUTH"

# Step 4: Test basic commands
jcli who-am-i
jcli version
jcli list-jobs
jcli list-plugins | head -20

# Step 5: List nodes
jcli list-nodes
```

---

### Exercise 2: Job Management via CLI

```bash
# Step 1: Create a job via CLI
cat > lab-cli-job.xml << 'EOF'
<?xml version='1.1' encoding='UTF-8'?>
<project>
  <description>Jenkins CLI Lab Job</description>
  <keepDependencies>false</keepDependencies>
  <properties/>
  <scm class="hudson.scm.NullSCM"/>
  <canRoam>true</canRoam>
  <disabled>false</disabled>
  <triggers/>
  <concurrentBuild>false</concurrentBuild>
  <builders>
    <hudson.tasks.Shell>
      <command>
#!/bin/bash
echo "=== CLI Job Execution ==="
echo "Job: $JOB_NAME"
echo "Build: $BUILD_NUMBER"
echo "Node: $NODE_NAME"
echo "Workspace: $WORKSPACE"
echo "Timestamp: $(date -u +%Y-%m-%dT%H:%M:%SZ)"
echo "========================="
      </command>
    </hudson.tasks.Shell>
  </builders>
  <publishers/>
  <buildWrappers/>
</project>
EOF

jcli create-job lab-cli-job < lab-cli-job.xml
echo "Job created."

# Step 2: Verify the job appears in the list
jcli list-jobs | grep lab-cli-job

# Step 3: Build the job and view output
jcli build lab-cli-job -s -v

# Step 4: Get console output of the last build
jcli console lab-cli-job

# Step 5: Disable and re-enable the job
jcli disable-job lab-cli-job
echo "Job disabled."
jcli list-jobs   # Note the job is now disabled

jcli enable-job lab-cli-job
echo "Job re-enabled."

# Step 6: Export the job config
jcli get-job lab-cli-job > exported-config.xml
cat exported-config.xml

# Step 7: Clean up
jcli delete-job lab-cli-job
echo "Job deleted."
jcli list-jobs | grep lab-cli-job || echo "Confirmed: job was deleted."

# Clean up files
rm lab-cli-job.xml exported-config.xml
```

---

### Graded Assessment: Jenkins Prerequisites

**Review Questions:**

1. What is the key difference between Continuous Delivery and Continuous Deployment?
2. Which file stores Jenkins' main system configuration?
3. What command would you use to perform a graceful Jenkins restart that waits for running builds to finish?
4. What is the purpose of the `initialAdminPassword` file?
5. Which directory contains all Jenkins job configurations and build history?
6. What does the `-s` flag do when used with `jcli build my-job -s`?

**Practical Task:** Using only the Jenkins CLI, create a job called `assessment-job`, trigger it, retrieve its console output, and then delete it. Document every command used.

---

# Module 3 – System Administration with Jenkins

## Module Overview

This module equips participants with essential skills for effectively administering Jenkins instances, including managing configurations, performing backup and restoration procedures, and ensuring data integrity and continuity.

### Learning Objectives

- Develop skills in administering Jenkins and managing its configuration
- Understand the importance of backup and restoration procedures for Jenkins instances
- Learn how to backup Jenkins configurations and data
- Gain proficiency in restoring Jenkins configurations and data from backups

---

## 3.1 Administering Jenkins

### Global System Configuration

The **Manage Jenkins → System** page contains critical global settings:

```
System Settings (Manage Jenkins → System):
├── System Message          → Banner shown on the dashboard
├── # of executors          → How many concurrent builds on the controller
├── Labels                  → Labels for this controller node
├── Jenkins URL             → External URL (critical for webhooks and emails)
├── System Admin e-mail     → From address for email notifications
├── Git configuration       → Global git user.name and user.email
├── Environment variables   → Global env vars available to all jobs
└── Tool locations          → Paths to JDK, Maven, Git, etc.
```

### Managing Plugins

Plugins extend Jenkins' core functionality. Plugin management is critical:

```
Manage Jenkins → Plugins:

├── Updates tab     → Plugins with available updates (update regularly!)
├── Available tab   → Browse and install new plugins
├── Installed tab   → Currently installed plugins
└── Advanced tab    → Upload plugin (.hpi/.jpi) file, update site URL
```

```bash
# View installed plugins via CLI
java -jar jenkins-cli.jar -s http://localhost:8080 -auth admin:TOKEN \
  list-plugins | sort

# Install plugins via CLI (useful for automation)
java -jar jenkins-cli.jar -s http://localhost:8080 -auth admin:TOKEN \
  install-plugin git pipeline-model-definition blueocean

# Essential plugins to install:
# - git                       → Git integration
# - workflow-aggregator       → Pipeline (included in Pipelines)
# - pipeline-model-definition → Declarative Pipeline syntax
# - blueocean                 → Modern Pipeline UI
# - credentials-binding       → Inject credentials into builds
# - ssh-credentials           → SSH key credential type
# - timestamper               → Add timestamps to console output
# - ansicolor                 → Colorize console output
# - slack                     → Slack notifications
# - email-ext                 → Extended email notifications
```

### Managing Users and Security

```
Manage Jenkins → Security:

1. Security Realm (Authentication):
   - Jenkins' own user database (default, stores users in Jenkins)
   - LDAP (integrate with Active Directory or LDAP server)
   - GitHub OAuth (log in with GitHub accounts)
   - SAML 2.0 (enterprise SSO)

2. Authorization (Who can do what):
   - Anyone can do anything (NEVER use in production)
   - Logged-in users can do anything (slightly better)
   - Matrix-based security (granular per-user/per-group permissions)
   - Project-based Matrix Authorization (per-job permissions)
   - Role-based Authorization Strategy (role-based access control)
```

**Setting up Matrix-Based Security:**

```
Manage Jenkins → Security → Authorization → Matrix-based security

Recommended permission matrix:
┌──────────────────────┬─────────┬─────────┬─────────┬──────────┐
│ Permission           │ anon    │ dev     │ devlead │ admin    │
├──────────────────────┼─────────┼─────────┼─────────┼──────────┤
│ Overall/Read         │ ❌      │ ✅      │ ✅      │ ✅       │
│ Job/Build            │ ❌      │ ✅      │ ✅      │ ✅       │
│ Job/Cancel           │ ❌      │ ✅ own  │ ✅      │ ✅       │
│ Job/Read             │ ❌      │ ✅      │ ✅      │ ✅       │
│ Job/Create           │ ❌      │ ❌      │ ✅      │ ✅       │
│ Job/Configure        │ ❌      │ ❌      │ ✅      │ ✅       │
│ Job/Delete           │ ❌      │ ❌      │ ❌      │ ✅       │
│ Manage Jenkins       │ ❌      │ ❌      │ ❌      │ ✅       │
└──────────────────────┴─────────┴─────────┴─────────┴──────────┘
```

### Managing Credentials

Credentials are stored encrypted in Jenkins and injected into builds:

```
Manage Jenkins → Credentials → System → Global credentials → Add Credentials

Credential Types:
- Username with password   → For HTTP authentication (Docker Hub, Nexus, etc.)
- SSH Username with key    → For Git SSH authentication, server access
- Secret text              → API tokens, single passwords
- Secret file              → Certificate files, config files
- Certificate (PKCS#12)    → SSL/TLS client certificates
```

```groovy
// Using credentials in a Jenkinsfile:

// Method 1: withCredentials binding
withCredentials([usernamePassword(
    credentialsId: 'dockerhub-creds',
    usernameVariable: 'DOCKER_USER',
    passwordVariable: 'DOCKER_PASS'
)]) {
    sh 'docker login -u $DOCKER_USER -p $DOCKER_PASS'
}

// Method 2: SSH key
withCredentials([sshUserPrivateKey(
    credentialsId: 'deploy-key',
    keyFileVariable: 'SSH_KEY'
)]) {
    sh 'ssh -i $SSH_KEY user@server "deploy.sh"'
}

// Method 3: Secret text
withCredentials([string(
    credentialsId: 'slack-webhook-url',
    variable: 'SLACK_URL'
)]) {
    sh 'curl -X POST $SLACK_URL -d \'{"text": "Build complete!"}\''
}
```

### Managing Agents/Nodes

```
Manage Jenkins → Nodes → New Node

Node Types:
- Permanent Agent   → Always-on server (SSH or JNLP connection)
- Cloud Agent       → Dynamically provisioned (AWS EC2, Kubernetes, Docker)

SSH Agent Configuration:
  - Host: agent-server-ip
  - Credentials: SSH key stored in Jenkins credentials
  - Host Key Verification: Known hosts file or non-verifying (dev only)
  - Labels: linux docker maven (used to target jobs to this agent)
  - # of Executors: 2-4 (parallel builds per agent)
  - Remote root directory: /var/jenkins
```

---

## 3.2 Backup and Restoring Jenkins

### Why Backup Jenkins?

Jenkins stores critical data:

- All job configurations (what pipelines run and how)
- Build history and console logs
- Plugin configurations
- User accounts and credentials
- System settings

Losing this data means recreating all your CI/CD infrastructure from scratch — potentially weeks of work. A tested backup strategy is non-negotiable.

### What to Back Up

```
CRITICAL (must backup):
  /var/lib/jenkins/config.xml              ← System configuration
  /var/lib/jenkins/credentials.xml         ← Encrypted credentials
  /var/lib/jenkins/jobs/*/config.xml        ← All job configurations
  /var/lib/jenkins/plugins/*.jpi|*.hpi      ← Installed plugins

IMPORTANT (back up if disk space allows):
  /var/lib/jenkins/jobs/*/builds/           ← Build history and logs
  /var/lib/jenkins/nodes/                   ← Agent configurations
  /var/lib/jenkins/users/                   ← User accounts

SKIP (regenerable, large):
  /var/lib/jenkins/workspace/               ← Can be recreated on next build
  /var/lib/jenkins/caches/                  ← Cache data
  /var/lib/jenkins/logs/                    ← Application logs
```

### Backup Methods

#### Method 1: ThinBackup Plugin (Recommended GUI Method)

```
1. Install the "ThinBackup" plugin:
   Manage Jenkins → Plugins → Available → Search "ThinBackup" → Install

2. Configure ThinBackup:
   Manage Jenkins → ThinBackup → Settings:
   - Backup directory: /var/lib/jenkins-backups
   - Full backup schedule: H 2 * * 0  (Weekly, Sunday 2am)
   - Differential backup schedule: H 2 * * 1-6  (Daily, Mon-Sat 2am)
   - Max # of backups: 10
   - Check: "Back up build results"
   - Check: "Back up 'userContent' folder"
   - Click "Save"

3. Run a manual backup:
   Manage Jenkins → ThinBackup → Backup Now

4. Verify backup files:
   ls -la /var/lib/jenkins-backups/
```

#### Method 2: Filesystem Backup Script (Recommended for Automation)

```bash
#!/bin/bash
# jenkins-backup.sh — Comprehensive Jenkins backup script

# ── Configuration ──────────────────────────────────────────────
JENKINS_HOME="/var/lib/jenkins"
BACKUP_DIR="/backups/jenkins"
BACKUP_RETENTION_DAYS=30
TIMESTAMP=$(date +%Y%m%d_%H%M%S)
BACKUP_FILE="${BACKUP_DIR}/jenkins_backup_${TIMESTAMP}.tar.gz"
LOG_FILE="/var/log/jenkins-backup.log"

# ── Functions ───────────────────────────────────────────────────
log() {
    echo "[$(date '+%Y-%m-%d %H:%M:%S')] $1" | tee -a "$LOG_FILE"
}

# ── Main Backup Logic ───────────────────────────────────────────
log "Starting Jenkins backup..."

# Create backup directory if it doesn't exist
mkdir -p "$BACKUP_DIR"

# Optional: Put Jenkins in quiet mode (pauses new builds)
# java -jar /usr/local/bin/jenkins-cli.jar \
#   -s http://localhost:8080 -auth admin:TOKEN quiet-down

# Create the backup archive (excluding workspaces, caches, and logs)
tar -czf "$BACKUP_FILE" \
  --exclude="${JENKINS_HOME}/workspace" \
  --exclude="${JENKINS_HOME}/caches" \
  --exclude="${JENKINS_HOME}/logs" \
  --exclude="${JENKINS_HOME}/*.log" \
  "$JENKINS_HOME" 2>> "$LOG_FILE"

BACKUP_STATUS=$?

# Optional: Cancel quiet mode
# java -jar /usr/local/bin/jenkins-cli.jar \
#   -s http://localhost:8080 -auth admin:TOKEN cancel-quiet-down

if [ $BACKUP_STATUS -eq 0 ]; then
    BACKUP_SIZE=$(du -sh "$BACKUP_FILE" | cut -f1)
    log "Backup successful: $BACKUP_FILE (Size: $BACKUP_SIZE)"
else
    log "ERROR: Backup failed with exit code $BACKUP_STATUS"
    exit 1
fi

# ── Rotate Old Backups ──────────────────────────────────────────
log "Removing backups older than ${BACKUP_RETENTION_DAYS} days..."
find "$BACKUP_DIR" -name "jenkins_backup_*.tar.gz" \
  -mtime +$BACKUP_RETENTION_DAYS -delete
log "Old backup rotation complete."

# ── Verify Backup ───────────────────────────────────────────────
log "Verifying backup integrity..."
if tar -tzf "$BACKUP_FILE" > /dev/null 2>&1; then
    log "Backup integrity check: PASSED"
else
    log "ERROR: Backup integrity check FAILED"
    exit 1
fi

# ── List Current Backups ────────────────────────────────────────
log "Current backups:"
ls -lh "$BACKUP_DIR" >> "$LOG_FILE"

log "Backup process complete."
```

```bash
# Install the script
sudo cp jenkins-backup.sh /usr/local/bin/jenkins-backup.sh
sudo chmod +x /usr/local/bin/jenkins-backup.sh

# Schedule with cron (daily at 2 AM)
echo "0 2 * * * root /usr/local/bin/jenkins-backup.sh" | \
  sudo tee /etc/cron.d/jenkins-backup

# Test the backup manually
sudo /usr/local/bin/jenkins-backup.sh
```

#### Method 3: Configuration-Only Backup (Lightweight)

```bash
#!/bin/bash
# jenkins-config-backup.sh — Back up only configurations (no build history)

JENKINS_HOME="/var/lib/jenkins"
BACKUP_DIR="/backups/jenkins-config"
TIMESTAMP=$(date +%Y%m%d_%H%M%S)

mkdir -p "$BACKUP_DIR"

# Backup only job configs (not build history)
tar -czf "${BACKUP_DIR}/configs_${TIMESTAMP}.tar.gz" \
  "${JENKINS_HOME}/config.xml" \
  "${JENKINS_HOME}/credentials.xml" \
  "${JENKINS_HOME}/users/" \
  "${JENKINS_HOME}/nodes/" \
  $(find "${JENKINS_HOME}/jobs" -name "config.xml") \
  2>/dev/null

echo "Config backup complete: ${BACKUP_DIR}/configs_${TIMESTAMP}.tar.gz"
```

### Restoring Jenkins

#### Full Restore from Filesystem Backup

```bash
#!/bin/bash
# jenkins-restore.sh — Restore Jenkins from a backup

BACKUP_FILE="$1"   # Pass backup file as argument
JENKINS_HOME="/var/lib/jenkins"

if [ -z "$BACKUP_FILE" ]; then
    echo "Usage: $0 /path/to/jenkins_backup_TIMESTAMP.tar.gz"
    exit 1
fi

if [ ! -f "$BACKUP_FILE" ]; then
    echo "Error: Backup file not found: $BACKUP_FILE"
    exit 1
fi

echo "=== Jenkins Restore Procedure ==="
echo "Backup file: $BACKUP_FILE"
echo "WARNING: This will overwrite all current Jenkins data!"
read -p "Are you sure you want to continue? (yes/no): " confirm

if [ "$confirm" != "yes" ]; then
    echo "Restore cancelled."
    exit 0
fi

# Step 1: Stop Jenkins
echo "[1/5] Stopping Jenkins service..."
sudo systemctl stop jenkins

# Step 2: Backup current state (safety net)
SAFETY_BACKUP="/tmp/jenkins_pre_restore_$(date +%Y%m%d_%H%M%S).tar.gz"
echo "[2/5] Creating safety backup of current state: $SAFETY_BACKUP"
sudo tar -czf "$SAFETY_BACKUP" "$JENKINS_HOME" 2>/dev/null
echo "Safety backup created: $SAFETY_BACKUP"

# Step 3: Clear Jenkins home
echo "[3/5] Clearing Jenkins home directory..."
sudo rm -rf "${JENKINS_HOME:?}"/*

# Step 4: Extract backup
echo "[4/5] Extracting backup..."
sudo tar -xzf "$BACKUP_FILE" -C / 2>/dev/null || \
sudo tar -xzf "$BACKUP_FILE" -C "$JENKINS_HOME" --strip-components=3

# Step 5: Fix ownership and restart
echo "[5/5] Fixing ownership and starting Jenkins..."
sudo chown -R jenkins:jenkins "$JENKINS_HOME"
sudo systemctl start jenkins

echo "=== Restore Complete ==="
echo "Jenkins is starting. Access it at http://localhost:8080"
echo "It may take 1-2 minutes to fully initialize."
```

```bash
# Make executable and run
sudo chmod +x jenkins-restore.sh

# Restore from a specific backup
sudo ./jenkins-restore.sh /backups/jenkins/jenkins_backup_20240115_020000.tar.gz
```

#### Restore via ThinBackup Plugin

```
1. Install ThinBackup if restoring to a fresh Jenkins instance
2. Navigate to: Manage Jenkins → ThinBackup → Restore
3. Select the backup set to restore from (by date)
4. Click "Restore"
5. Jenkins will restart automatically
```

---

## 🧪 Hands-on Lab: Backup and Restore Jenkins

### Lab Duration: 60 minutes

---

### Exercise 1: Create Several Jobs to Protect

```bash
# Using the CLI, create a few jobs that we'll back up and restore

JENKINS_URL="http://localhost:8080"
AUTH="admin:YOUR_TOKEN"

# Create Job 1: webapp-build
cat > job1.xml << 'EOF'
<?xml version='1.1' encoding='UTF-8'?>
<project>
  <description>Web Application Build Pipeline</description>
  <builders>
    <hudson.tasks.Shell>
      <command>
echo "Building web application version $BUILD_NUMBER"
echo "Running unit tests..."
echo "All tests passed!"
      </command>
    </hudson.tasks.Shell>
  </builders>
</project>
EOF
java -jar jenkins-cli.jar -s $JENKINS_URL -auth $AUTH \
  create-job webapp-build < job1.xml

# Create Job 2: api-tests
cat > job2.xml << 'EOF'
<?xml version='1.1' encoding='UTF-8'?>
<project>
  <description>API Integration Tests</description>
  <builders>
    <hudson.tasks.Shell>
      <command>
echo "Running API integration test suite..."
echo "Testing /api/users endpoint..."
echo "Testing /api/products endpoint..."
echo "All API tests passed!"
      </command>
    </hudson.tasks.Shell>
  </builders>
</project>
EOF
java -jar jenkins-cli.jar -s $JENKINS_URL -auth $AUTH \
  create-job api-tests < job2.xml

# Build each job once to create some history
java -jar jenkins-cli.jar -s $JENKINS_URL -auth $AUTH build webapp-build -s
java -jar jenkins-cli.jar -s $JENKINS_URL -auth $AUTH build api-tests -s

# Verify jobs exist
java -jar jenkins-cli.jar -s $JENKINS_URL -auth $AUTH list-jobs

# Clean up temp files
rm job1.xml job2.xml
```

---

### Exercise 2: Perform a Manual Backup

```bash
# Step 1: Create the backup directory
sudo mkdir -p /backups/jenkins
sudo chown jenkins:jenkins /backups/jenkins

# Step 2: Perform a full backup
TIMESTAMP=$(date +%Y%m%d_%H%M%S)
BACKUP_FILE="/backups/jenkins/backup_${TIMESTAMP}.tar.gz"

sudo tar -czf "$BACKUP_FILE" \
  --exclude=/var/lib/jenkins/workspace \
  --exclude=/var/lib/jenkins/caches \
  /var/lib/jenkins 2>/dev/null

# Step 3: Verify the backup
echo "Backup file:"
ls -lh "$BACKUP_FILE"

echo "Backup contents (top-level):"
sudo tar -tzf "$BACKUP_FILE" | grep -E "^[^/]+/[^/]+/?$" | head -30

echo "Job configs included:"
sudo tar -tzf "$BACKUP_FILE" | grep "config.xml" | head -20

# Step 4: Record the backup path for later
echo "BACKUP_FILE=$BACKUP_FILE" > /tmp/lab-backup-info.txt
cat /tmp/lab-backup-info.txt
```

---

### Exercise 3: Simulate Disaster and Restore

```bash
# Step 1: Read the backup file path saved earlier
source /tmp/lab-backup-info.txt
echo "Will restore from: $BACKUP_FILE"

# Step 2: "Accidentally" delete one of our jobs
java -jar jenkins-cli.jar -s http://localhost:8080 -auth admin:TOKEN \
  delete-job webapp-build

# Confirm it's gone
java -jar jenkins-cli.jar -s http://localhost:8080 -auth admin:TOKEN \
  list-jobs
# webapp-build should be absent

# Step 3: Stop Jenkins for restoration
sudo systemctl stop jenkins

# Step 4: Restore from backup
sudo rm -rf /var/lib/jenkins/jobs/webapp-build   # Ensure it's fully gone
sudo tar -xzf "$BACKUP_FILE" \
  --strip-components=3 \
  -C /var/lib/jenkins \
  var/lib/jenkins/jobs/webapp-build/
sudo chown -R jenkins:jenkins /var/lib/jenkins/jobs/webapp-build/

# Step 5: Restart Jenkins
sudo systemctl start jenkins

# Wait for startup
echo "Waiting for Jenkins to start..."
until curl -s http://localhost:8080/login > /dev/null; do
  sleep 5
  echo "Still starting..."
done
echo "Jenkins is up!"

# Step 6: Verify restoration
sleep 10   # Give Jenkins a moment to fully load
java -jar jenkins-cli.jar -s http://localhost:8080 -auth admin:TOKEN \
  list-jobs
# webapp-build should be back!

# Step 7: Build the restored job to confirm it works
java -jar jenkins-cli.jar -s http://localhost:8080 -auth admin:TOKEN \
  build webapp-build -s -v

echo "Restore exercise complete!"
```

---

### Graded Assessment: System Administration with Jenkins

**Review Questions:**

1. List three types of data that are critical to include in a Jenkins backup.
2. What is the difference between the ThinBackup plugin's "full backup" and "differential backup" options?
3. Why should the Jenkins workspace directory typically be excluded from backups?
4. What command stops Jenkins gracefully while allowing running builds to finish?
5. After restoring Jenkins files, what ownership command must be run and why?

**Practical Task:** Create a cron-scheduled backup script that backs up only Jenkins job configuration files (not build history), retains the last 14 backups, and writes a log entry for each run. Test the script and provide its output.

---

# Module 4 – Jenkins Pipelines

## Module Overview

This module focuses on Jenkins Pipelines as code, guiding participants through building various types of pipelines — from simple examples to full multi-stage CI/CD pipelines. Participants learn about Jenkinsfile and gain practical experience building pipelines for real-world deployment scenarios.

### Learning Objectives

- Understand and learn how to build a Jenkinsfile to define and execute pipelines
- Gain practical experience in running sample pipelines and building multistage pipelines
- Develop skills in building Continuous Integration (CI) and Continuous Deployment (CD) pipelines using Jenkins
- Understand the process of deploying a full pipeline including testing, staging, and production stages

---

## 4.1 What is a Jenkinsfile?

### Pipelines as Code

A **Jenkinsfile** is a text file written in Groovy-based DSL that defines a Jenkins pipeline. It lives in the root of your source code repository alongside your application code. This means:

- **Versioned**: Your pipeline history is in Git alongside your code
- **Reviewable**: Pipeline changes go through pull requests and code review
- **Reproducible**: The same Jenkinsfile produces the same pipeline on any Jenkins instance
- **Portable**: Move between Jenkins instances by simply pointing to the same repository

### Two Pipeline Syntaxes

Jenkins supports two distinct pipeline syntaxes:

#### Declarative Pipeline (Recommended)

The newer, more structured syntax with predefined sections. Easier to read and write:

```groovy
pipeline {                          // Required: outer wrapper
    agent any                       // Where to run

    stages {                        // Collection of stages
        stage('Build') {            // Individual stage
            steps {                 // Steps within the stage
                echo 'Building...'
            }
        }
    }
}
```

#### Scripted Pipeline (Legacy)

The older, more flexible syntax based on pure Groovy. More powerful but harder to maintain:

```groovy
node {                              // Run on any available agent
    stage('Build') {
        echo 'Building...'
    }
    stage('Test') {
        echo 'Testing...'
    }
}
```

**Use Declarative** for all new pipelines. It provides better structure, built-in error handling, and is the actively developed syntax.

### Declarative Pipeline Structure

```groovy
pipeline {
    // ── AGENT ──────────────────────────────────────────────
    // Defines where the pipeline (or individual stages) run
    agent any                    // Any available agent
    // agent none                // No global agent; each stage defines its own
    // agent { label 'linux' }   // Agent with label 'linux'
    // agent { docker 'maven:3' }// Run inside a Docker container

    // ── OPTIONS ─────────────────────────────────────────────
    options {
        timeout(time: 1, unit: 'HOURS')      // Fail if pipeline exceeds 1hr
        retry(3)                             // Retry whole pipeline up to 3x
        timestamps()                         // Prepend timestamps to log
        buildDiscarder(logRotator(           // Keep only last 10 builds
            numToKeepStr: '10'
        ))
        disableConcurrentBuilds()            // Only 1 build at a time
    }

    // ── TRIGGERS ────────────────────────────────────────────
    triggers {
        cron('H 4 * * 1-5')                 // Scheduled: weekdays at 4am
        pollSCM('H/5 * * * *')              // Poll SCM every 5 min
        githubPush()                         // GitHub webhook trigger
    }

    // ── PARAMETERS ──────────────────────────────────────────
    parameters {
        string(name: 'VERSION',
               defaultValue: '1.0.0',
               description: 'Application version to deploy')
        choice(name: 'ENVIRONMENT',
               choices: ['dev', 'staging', 'production'],
               description: 'Target deployment environment')
        booleanParam(name: 'RUN_INTEGRATION_TESTS',
                     defaultValue: true,
                     description: 'Run integration tests?')
    }

    // ── ENVIRONMENT ─────────────────────────────────────────
    environment {
        APP_NAME = 'my-application'
        DOCKER_REGISTRY = 'registry.example.com'
        // Inject a Jenkins credential as env var:
        DEPLOY_KEY = credentials('deploy-ssh-key')
        // Construct variable from other variables:
        IMAGE_TAG = "${DOCKER_REGISTRY}/${APP_NAME}:${params.VERSION}"
    }

    // ── TOOLS ───────────────────────────────────────────────
    tools {
        maven 'Maven-3.9'        // Uses tool configured in Manage Jenkins → Tools
        jdk 'JDK-17'
        nodejs 'NodeJS-18'
    }

    // ── STAGES ──────────────────────────────────────────────
    stages {
        stage('Checkout') {
            steps {
                checkout scm     // Check out source code from configured SCM
            }
        }

        stage('Build') {
            steps {
                sh 'mvn clean package -DskipTests'
            }
        }

        stage('Test') {
            parallel {           // Run sub-stages in parallel
                stage('Unit Tests') {
                    steps { sh 'mvn test' }
                }
                stage('Lint') {
                    steps { sh 'mvn checkstyle:check' }
                }
            }
        }

        stage('Deploy to Staging') {
            when {               // Conditional execution
                branch 'main'   // Only run on main branch
            }
            steps {
                echo "Deploying version ${params.VERSION}..."
            }
        }
    }

    // ── POST ────────────────────────────────────────────────
    post {
        always {
            junit '**/target/surefire-reports/*.xml'  // Publish test results
            archiveArtifacts artifacts: 'target/*.jar', fingerprint: true
        }
        success {
            echo 'Pipeline succeeded!'
            // slackSend(color: 'good', message: "Build passed: ${env.JOB_NAME}")
        }
        failure {
            echo 'Pipeline failed!'
            // mail to: 'team@example.com', subject: 'BUILD FAILED'
        }
        unstable {
            echo 'Build unstable (test failures)'
        }
        changed {
            echo 'Build status changed from previous run'
        }
    }
}
```

---

## 4.2 Build a Jenkinsfile

### Creating a Pipeline Job

```
1. Jenkins Dashboard → New Item
2. Enter name: my-first-pipeline
3. Select "Pipeline" → OK
4. On the configuration page, scroll to "Pipeline" section
5. Definition: "Pipeline script" (for inline Jenkinsfile)
   OR
   "Pipeline script from SCM" (reads Jenkinsfile from your Git repo — preferred!)
6. If using SCM:
   - SCM: Git
   - Repository URL: https://github.com/your-org/your-repo.git
   - Credentials: (select Git credential)
   - Branch: */main
   - Script Path: Jenkinsfile    (relative path in repo)
7. Click Save
```

### Your First Jenkinsfile

```groovy
// Jenkinsfile — your first pipeline
pipeline {
    agent any

    stages {
        stage('Hello') {
            steps {
                echo 'Hello, Jenkins Pipeline!'
                echo "Build number: ${env.BUILD_NUMBER}"
                echo "Build URL: ${env.BUILD_URL}"
                sh 'echo "Running on: $(hostname)"'
                sh 'echo "Date: $(date)"'
            }
        }
    }

    post {
        always {
            echo 'This always runs, regardless of success or failure.'
        }
    }
}
```

---

## 4.3 Run a Sample Pipeline

### Sample Pipeline with Multiple Steps

```groovy
// Jenkinsfile — sample pipeline demonstrating common patterns
pipeline {
    agent any

    environment {
        APP_NAME = 'sample-app'
        VERSION  = '1.0.0'
    }

    stages {
        stage('Preparation') {
            steps {
                echo "Preparing build environment for ${APP_NAME} v${VERSION}"

                // Multi-line shell script
                sh '''
                    echo "Checking tool versions:"
                    java -version || echo "Java not found"
                    git --version
                    echo "Workspace: $WORKSPACE"
                    echo "Available disk space:"
                    df -h $WORKSPACE
                '''
            }
        }

        stage('Source') {
            steps {
                // Simulate checking out source code
                sh '''
                    mkdir -p src/main/java
                    cat > src/main/java/App.java << "JAVA"
public class App {
    public static void main(String[] args) {
        System.out.println("Hello from Sample App!");
    }
}
JAVA
                    echo "Source code prepared."
                    cat src/main/java/App.java
                '''
            }
        }

        stage('Build') {
            steps {
                echo 'Simulating application build...'
                sh '''
                    mkdir -p target
                    echo "Compiled classes" > target/App.class
                    echo "Build artifact: target/App.class"
                    ls -la target/
                '''
            }
        }

        stage('Test') {
            steps {
                echo 'Running tests...'
                sh '''
                    mkdir -p test-results
                    cat > test-results/TEST-sample.xml << "XML"
<?xml version="1.0" encoding="UTF-8"?>
<testsuite name="SampleTests" tests="3" failures="0" errors="0" time="0.5">
  <testcase name="testHello" time="0.1"/>
  <testcase name="testVersion" time="0.2"/>
  <testcase name="testStartup" time="0.2"/>
</testsuite>
XML
                    echo "All 3 tests passed."
                '''
            }
            post {
                always {
                    junit 'test-results/TEST-*.xml'
                }
            }
        }

        stage('Package') {
            steps {
                sh '''
                    echo "Creating deployment package..."
                    tar -czf target/${APP_NAME}-${VERSION}.tar.gz target/App.class
                    echo "Package created: target/${APP_NAME}-${VERSION}.tar.gz"
                    ls -lh target/*.tar.gz
                '''
                archiveArtifacts artifacts: 'target/*.tar.gz', fingerprint: true
            }
        }

        stage('Report') {
            steps {
                echo 'Build summary:'
                sh '''
                    echo "Application: $APP_NAME"
                    echo "Version: $VERSION"
                    echo "Build: $BUILD_NUMBER"
                    echo "Status: SUCCESS"
                '''
            }
        }
    }

    post {
        success {
            echo "✅ Pipeline completed successfully for ${env.APP_NAME} v${env.VERSION}"
        }
        failure {
            echo "❌ Pipeline failed for ${env.APP_NAME} v${env.VERSION}"
        }
        always {
            // Clean up workspace to avoid disk space issues
            cleanWs()
        }
    }
}
```

---

## 4.4 Build a Multistage Pipeline

### Multistage Pipeline with Parallel Execution

```groovy
// Jenkinsfile — multistage pipeline with parallel testing
pipeline {
    agent any

    options {
        timeout(time: 30, unit: 'MINUTES')
        buildDiscarder(logRotator(numToKeepStr: '15'))
        timestamps()
    }

    environment {
        APP_NAME    = 'my-webapp'
        DOCKER_REPO = 'mycompany'
    }

    stages {
        stage('Checkout') {
            steps {
                checkout scm
                script {
                    // Capture the Git commit hash for tagging
                    env.GIT_COMMIT_SHORT = sh(
                        script: 'git rev-parse --short HEAD 2>/dev/null || echo "unknown"',
                        returnStdout: true
                    ).trim()
                    echo "Building commit: ${env.GIT_COMMIT_SHORT}"
                }
            }
        }

        stage('Build') {
            steps {
                echo "Building ${APP_NAME}..."
                sh 'mkdir -p build && echo "build artifact" > build/app.jar'
            }
        }

        stage('Quality Gates') {
            // Run all quality checks in parallel to save time
            parallel {
                stage('Unit Tests') {
                    steps {
                        echo 'Running unit tests...'
                        sh '''
                            mkdir -p test-results
                            cat > test-results/unit-tests.xml << "EOF"
<?xml version="1.0"?>
<testsuite name="UnitTests" tests="10" failures="0" errors="0">
  <testcase name="test1"/><testcase name="test2"/>
  <testcase name="test3"/><testcase name="test4"/>
  <testcase name="test5"/><testcase name="test6"/>
  <testcase name="test7"/><testcase name="test8"/>
  <testcase name="test9"/><testcase name="test10"/>
</testsuite>
EOF
                            echo "Unit tests: 10/10 passed"
                        '''
                    }
                    post {
                        always {
                            junit 'test-results/unit-tests.xml'
                        }
                    }
                }

                stage('Security Scan') {
                    steps {
                        echo 'Running security vulnerability scan...'
                        sh '''
                            echo "Scanning dependencies for CVEs..."
                            sleep 2
                            echo "Security scan complete: 0 critical vulnerabilities found"
                        '''
                    }
                }

                stage('Code Coverage') {
                    steps {
                        echo 'Calculating code coverage...'
                        sh '''
                            echo "Code coverage: 87% (threshold: 80%)"
                            echo "Coverage check: PASSED"
                        '''
                    }
                }

                stage('Static Analysis') {
                    steps {
                        echo 'Running static code analysis...'
                        sh '''
                            echo "Analyzing code quality..."
                            echo "Code smells: 2 (acceptable)"
                            echo "Static analysis: PASSED"
                        '''
                    }
                }
            }
        }

        stage('Docker Build') {
            steps {
                echo "Building Docker image: ${DOCKER_REPO}/${APP_NAME}:${GIT_COMMIT_SHORT}"
                sh '''
                    echo "FROM nginx:alpine" > Dockerfile
                    echo "COPY build/ /usr/share/nginx/html/" >> Dockerfile
                    echo "Docker build simulation: SUCCESS"
                    echo "Image: $DOCKER_REPO/$APP_NAME:$GIT_COMMIT_SHORT"
                '''
            }
        }

        stage('Integration Tests') {
            steps {
                echo 'Running integration tests against Docker image...'
                sh '''
                    echo "Starting test containers..."
                    echo "Running integration test suite..."
                    sleep 2
                    echo "Integration tests: 25/25 passed"
                '''
            }
        }

        stage('Push to Registry') {
            when {
                anyOf {
                    branch 'main'
                    branch 'release/*'
                }
            }
            steps {
                echo "Pushing image to registry..."
                sh "echo 'docker push ${DOCKER_REPO}/${APP_NAME}:${GIT_COMMIT_SHORT}'"
                sh "echo 'docker push ${DOCKER_REPO}/${APP_NAME}:latest'"
            }
        }
    }

    post {
        always {
            echo "Pipeline finished. Build: ${env.BUILD_NUMBER}"
            cleanWs()
        }
    }
}
```

---

## 4.5 Build a CI Pipeline

A **Continuous Integration pipeline** automatically validates every code commit by building and testing the application.

```groovy
// Jenkinsfile.ci — CI Pipeline for a Python Flask Application
pipeline {
    agent any

    options {
        timeout(time: 20, unit: 'MINUTES')
        buildDiscarder(logRotator(numToKeepStr: '20'))
        timestamps()
        disableConcurrentBuilds()
    }

    triggers {
        // Trigger on any push to the repository
        // (requires GitHub/GitLab webhook configured)
        pollSCM('H/2 * * * *')   // Poll every 2 min as fallback
    }

    environment {
        PYTHON_VERSION = '3.11'
        APP_PORT       = '5000'
        VENV_PATH      = "${WORKSPACE}/.venv"
    }

    stages {
        stage('Checkout') {
            steps {
                checkout scm
                sh 'git log --oneline -5'   // Show recent commits
            }
        }

        stage('Setup') {
            steps {
                sh '''
                    python3 --version
                    python3 -m venv .venv
                    . .venv/bin/activate
                    pip install --upgrade pip
                    pip install flask pytest pytest-cov flake8 bandit 2>/dev/null || \
                      echo "Install simulation - no requirements.txt found"
                    echo "Environment setup complete"
                '''
            }
        }

        stage('Lint & Style') {
            steps {
                sh '''
                    echo "=== Running flake8 linter ==="
                    echo "flake8 . --max-line-length=120 --exclude=.venv"
                    echo "Linting: No issues found."
                '''
            }
        }

        stage('Security Audit') {
            steps {
                sh '''
                    echo "=== Running Bandit Security Audit ==="
                    echo "bandit -r . --exclude .venv -l"
                    echo "Security audit: No high-severity issues found."
                '''
            }
        }

        stage('Unit Tests') {
            steps {
                sh '''
                    echo "=== Running Unit Tests ==="

                    # Create a sample test result XML (simulating pytest output)
                    mkdir -p test-results
                    cat > test-results/junit.xml << "XML"
<?xml version="1.0" encoding="utf-8"?>
<testsuites>
  <testsuite name="pytest" tests="12" errors="0" failures="0" time="1.234">
    <testcase classname="tests.test_app" name="test_home_returns_200" time="0.015"/>
    <testcase classname="tests.test_app" name="test_api_endpoint_json" time="0.012"/>
    <testcase classname="tests.test_app" name="test_health_check" time="0.008"/>
    <testcase classname="tests.test_app" name="test_invalid_route_404" time="0.009"/>
    <testcase classname="tests.test_models" name="test_user_creation" time="0.025"/>
    <testcase classname="tests.test_models" name="test_user_validation" time="0.018"/>
    <testcase classname="tests.test_models" name="test_password_hash" time="0.031"/>
    <testcase classname="tests.test_services" name="test_email_service" time="0.055"/>
    <testcase classname="tests.test_services" name="test_notification_service" time="0.042"/>
    <testcase classname="tests.test_services" name="test_cache_service" time="0.038"/>
    <testcase classname="tests.test_integration" name="test_db_connection" time="0.089"/>
    <testcase classname="tests.test_integration" name="test_full_request_cycle" time="0.112"/>
  </testsuite>
</testsuites>
XML
                    echo "Tests passed: 12/12"
                '''
            }
            post {
                always {
                    junit 'test-results/junit.xml'
                }
            }
        }

        stage('Code Coverage') {
            steps {
                sh '''
                    echo "=== Code Coverage Report ==="
                    echo "Statements:  92%"
                    echo "Branches:    85%"
                    echo "Functions:   94%"
                    echo "Lines:       92%"
                    echo ""
                    echo "Minimum threshold: 80% — PASSED ✅"
                '''
            }
        }

        stage('Build Artifact') {
            steps {
                sh '''
                    echo "=== Building deployable artifact ==="
                    mkdir -p dist
                    VERSION=$(git describe --tags --always 2>/dev/null || echo "1.0.0-ci")
                    echo "Building version: $VERSION"
                    tar -czf dist/flask-app-${BUILD_NUMBER}.tar.gz \
                      --exclude='.venv' \
                      --exclude='dist' \
                      --exclude='.git' \
                      --exclude='__pycache__' \
                      . 2>/dev/null || tar -czf dist/flask-app-${BUILD_NUMBER}.tar.gz .
                    echo "Artifact created: dist/flask-app-${BUILD_NUMBER}.tar.gz"
                    ls -lh dist/
                '''
                archiveArtifacts artifacts: 'dist/*.tar.gz', fingerprint: true
            }
        }

        stage('Docker Build & Push') {
            steps {
                script {
                    def imageTag = "${env.BUILD_NUMBER}"
                    echo "Building Docker image with tag: ${imageTag}"
                    sh """
                        echo 'FROM python:3.11-slim' > Dockerfile.ci
                        echo 'WORKDIR /app' >> Dockerfile.ci
                        echo 'COPY dist/ .' >> Dockerfile.ci
                        echo 'CMD ["python", "app.py"]' >> Dockerfile.ci
                        echo "docker build -t flask-app:${imageTag} -f Dockerfile.ci ."
                        echo "Docker build simulation successful."
                        echo "Image: flask-app:${imageTag}"
                    """
                }
            }
        }
    }

    post {
        success {
            echo """
✅ CI Pipeline PASSED
============================
Job:     ${env.JOB_NAME}
Build:   #${env.BUILD_NUMBER}
Branch:  ${env.GIT_BRANCH ?: 'unknown'}
Time:    ${currentBuild.durationString}
============================
"""
        }

        failure {
            echo """
❌ CI Pipeline FAILED
============================
Job:     ${env.JOB_NAME}
Build:   #${env.BUILD_NUMBER}
Branch:  ${env.GIT_BRANCH ?: 'unknown'}
============================
"""
        }

        always {
            cleanWs(cleanWhenSuccess: true, cleanWhenFailure: false)
        }
    }
}
```

---

## 4.6 Building a CD Pipeline and Full Pipeline Deployment

### What a CD Pipeline Adds to CI

A **Continuous Deployment pipeline** takes the validated build artifact from CI and deploys it through multiple environments — automatically to lower environments and with approval gates for production.

```
CI Pipeline                         CD Pipeline
─────────────────────              ─────────────────────────────────────────
  Checkout                           Deploy to Dev (automatic)
  → Build                                │
  → Lint/Scan                           ▼ Integration Tests
  → Test                             Deploy to Staging (automatic)
  → Package                              │
  → Docker Build/Push                   ▼ Acceptance Tests
  ─────────────────                  Manual Approval Gate 👤
       ↓ artifact                         │
       ↓                                 ▼
       └──────────────────────────▶  Deploy to Production
                                         │
                                        ▼ Smoke Tests
                                     Monitor & Verify
```

### Full CD Pipeline: Deploy to Dev → Staging → Production

```groovy
// Jenkinsfile.cd — Full CD Pipeline
pipeline {
    agent any

    parameters {
        string(
            name: 'IMAGE_TAG',
            defaultValue: '',
            description: 'Docker image tag to deploy (leave blank to use latest)'
        )
        choice(
            name: 'START_FROM',
            choices: ['dev', 'staging', 'production'],
            description: 'Start deployment from this environment'
        )
    }

    options {
        timeout(time: 60, unit: 'MINUTES')
        buildDiscarder(logRotator(numToKeepStr: '20'))
        timestamps()
    }

    environment {
        APP_NAME     = 'my-webapp'
        DOCKER_REPO  = 'mycompany'
        IMAGE_TAG    = "${params.IMAGE_TAG ?: env.BUILD_NUMBER}"
        FULL_IMAGE   = "${DOCKER_REPO}/${APP_NAME}:${IMAGE_TAG}"

        // Credentials injected from Jenkins credential store
        // DEV_SERVER_KEY    = credentials('dev-deploy-key')
        // STAGING_SERVER_KEY = credentials('staging-deploy-key')
        // PROD_SERVER_KEY   = credentials('prod-deploy-key')
    }

    stages {

        // ── STAGE: Dev Deployment ────────────────────────────
        stage('Deploy to Dev') {
            when {
                anyOf {
                    expression { params.START_FROM == 'dev' }
                    expression { currentBuild.number == 1 }
                }
            }
            environment {
                DEPLOY_ENV   = 'dev'
                DEPLOY_HOST  = 'dev.internal.example.com'
                APP_PORT     = '8080'
                REPLICAS     = '1'
            }
            steps {
                echo "🚀 Deploying ${FULL_IMAGE} to ${DEPLOY_ENV}..."

                sh '''
                    echo "=== Deployment: $DEPLOY_ENV ==="
                    echo "Image: $FULL_IMAGE"
                    echo "Host: $DEPLOY_HOST"
                    echo "Port: $APP_PORT"
                    echo "Replicas: $REPLICAS"
                    echo ""

                    # Simulate deployment steps
                    echo "[1/4] Pulling image..."
                    echo "  docker pull $FULL_IMAGE"

                    echo "[2/4] Stopping old container..."
                    echo "  docker stop ${APP_NAME}-dev 2>/dev/null || true"
                    echo "  docker rm ${APP_NAME}-dev 2>/dev/null || true"

                    echo "[3/4] Starting new container..."
                    echo "  docker run -d --name ${APP_NAME}-dev -p ${APP_PORT}:80 $FULL_IMAGE"

                    echo "[4/4] Deployment complete."
                    echo "  URL: http://$DEPLOY_HOST:$APP_PORT"
                '''
            }
            post {
                success {
                    echo "✅ Dev deployment successful."
                }
                failure {
                    echo "❌ Dev deployment failed. Stopping pipeline."
                }
            }
        }

        // ── STAGE: Dev Smoke Tests ───────────────────────────
        stage('Dev Smoke Tests') {
            when {
                expression { params.START_FROM in ['dev'] }
            }
            steps {
                echo "🧪 Running smoke tests on Dev..."
                sh '''
                    echo "Testing health endpoint..."
                    echo "  curl -f http://dev.internal.example.com:8080/health"
                    echo "  HTTP 200 OK"

                    echo "Testing API response..."
                    echo "  curl -f http://dev.internal.example.com:8080/api/version"
                    echo "  {\"version\": \"$IMAGE_TAG\", \"status\": \"ok\"}"

                    echo "Smoke tests: PASSED ✅"
                '''
            }
        }

        // ── STAGE: Staging Deployment ────────────────────────
        stage('Deploy to Staging') {
            when {
                expression { params.START_FROM in ['dev', 'staging'] }
            }
            environment {
                DEPLOY_ENV  = 'staging'
                DEPLOY_HOST = 'staging.example.com'
                APP_PORT    = '80'
                REPLICAS    = '2'
            }
            steps {
                echo "🚀 Deploying ${FULL_IMAGE} to ${DEPLOY_ENV}..."

                sh '''
                    echo "=== Deployment: $DEPLOY_ENV ==="
                    echo "Image: $FULL_IMAGE"
                    echo "Host: $DEPLOY_HOST"
                    echo "Replicas: $REPLICAS"

                    echo "[1/5] Pulling image on staging servers..."
                    echo "[2/5] Running database migrations..."
                    echo "  Migrations: 2 applied, 0 pending"
                    echo "[3/5] Rolling deployment: updating replica 1/2..."
                    echo "[4/5] Rolling deployment: updating replica 2/2..."
                    echo "[5/5] Updating load balancer..."

                    echo "Staging deployment complete."
                    echo "URL: https://$DEPLOY_HOST"
                '''
            }
        }

        // ── STAGE: Staging Acceptance Tests ─────────────────
        stage('Staging Acceptance Tests') {
            when {
                expression { params.START_FROM in ['dev', 'staging'] }
            }
            parallel {
                stage('API Tests') {
                    steps {
                        sh '''
                            echo "Running API acceptance test suite..."
                            echo "Tests: 45 passed, 0 failed"
                            echo "API tests: PASSED ✅"
                        '''
                    }
                }
                stage('UI Tests') {
                    steps {
                        sh '''
                            echo "Running Selenium UI test suite..."
                            echo "Browser tests: 18 passed, 0 failed"
                            echo "UI tests: PASSED ✅"
                        '''
                    }
                }
                stage('Performance Tests') {
                    steps {
                        sh '''
                            echo "Running performance baseline tests..."
                            echo "Avg response time: 42ms (threshold: 200ms)"
                            echo "Throughput: 850 req/sec (threshold: 500 req/sec)"
                            echo "Performance tests: PASSED ✅"
                        '''
                    }
                }
            }
        }

        // ── STAGE: Production Approval Gate ──────────────────
        stage('Production Approval') {
            when {
                anyOf {
                    expression { params.START_FROM in ['dev', 'staging'] }
                    expression { params.START_FROM == 'production' }
                }
            }
            steps {
                script {
                    def deployApproval = input(
                        message: "Deploy ${FULL_IMAGE} to PRODUCTION?",
                        ok: 'Deploy to Production',
                        parameters: [
                            string(
                                name: 'APPROVER_NOTES',
                                defaultValue: '',
                                description: 'Optional: notes for the deployment log'
                            )
                        ],
                        submitter: 'release-managers,admin',
                        submitterParameter: 'APPROVED_BY'
                    )

                    echo "✅ Production deployment approved."
                    echo "Approved by: ${deployApproval}"
                }
            }
        }

        // ── STAGE: Production Deployment ─────────────────────
        stage('Deploy to Production') {
            environment {
                DEPLOY_ENV  = 'production'
                DEPLOY_HOST = 'www.example.com'
                APP_PORT    = '443'
                REPLICAS    = '5'
            }
            steps {
                echo "🚀 DEPLOYING TO PRODUCTION: ${FULL_IMAGE}"

                sh '''
                    echo "=== PRODUCTION DEPLOYMENT ==="
                    echo "Image: $FULL_IMAGE"
                    echo "Replicas: $REPLICAS"
                    echo "Strategy: Rolling (1 at a time)"

                    for i in 1 2 3 4 5; do
                        echo "  Updating pod $i of $REPLICAS..."
                        echo "  Health check pod $i: OK"
                    done

                    echo ""
                    echo "Production deployment complete!"
                    echo "URL: https://$DEPLOY_HOST"
                '''
            }
        }

        // ── STAGE: Production Smoke Tests ────────────────────
        stage('Production Smoke Tests') {
            steps {
                sh '''
                    echo "=== Production Smoke Tests ==="
                    echo "Testing https://www.example.com/health..."
                    echo "  HTTP 200 OK ✅"
                    echo "Testing https://www.example.com/api/version..."
                    echo "  {\"version\": \"$IMAGE_TAG\"} ✅"
                    echo "Testing SSL certificate validity..."
                    echo "  Certificate valid for 89 more days ✅"
                    echo ""
                    echo "All smoke tests passed! ✅"
                '''
            }
        }

        // ── STAGE: Tag Production Release ────────────────────
        stage('Tag Release') {
            steps {
                sh '''
                    echo "Creating production release tag..."
                    echo "git tag -a release-${IMAGE_TAG} -m 'Production release ${IMAGE_TAG}'"
                    echo "git push origin release-${IMAGE_TAG}"
                    echo "Release tagged: release-${IMAGE_TAG} ✅"
                '''
            }
        }
    }

    post {
        success {
            echo """
🎉 FULL CD PIPELINE SUCCEEDED
================================
App:     ${env.APP_NAME}
Image:   ${env.FULL_IMAGE}
Build:   #${env.BUILD_NUMBER}
Duration: ${currentBuild.durationString}
================================
"""
        }

        failure {
            echo """
🚨 CD PIPELINE FAILED
================================
App:     ${env.APP_NAME}
Build:   #${env.BUILD_NUMBER}
Stage:   ${env.STAGE_NAME ?: 'unknown'}
================================
"""
        }

        aborted {
            echo "⚠️ Pipeline was manually aborted."
        }

        always {
            cleanWs()
        }
    }
}
```

---

## 🧪 Hands-on Lab: Building a CD Pipeline

### Lab Objectives

- Create a working multistage CD pipeline with a real Jenkinsfile
- Understand stage-based flow control with `when` directives
- Implement parallel test execution
- Add an approval gate for production deployments
- Work with pipeline parameters and environment variables

### Lab Duration: 90 minutes

---

### Exercise 1: Create the CI Stage

```groovy
// Save this as Jenkinsfile in a new Jenkins Pipeline job
// Job name: lab-cd-pipeline

pipeline {
    agent any

    parameters {
        choice(
            name: 'DEPLOY_TO',
            choices: ['dev', 'staging', 'skip'],
            description: 'Automatically deploy to this environment after CI'
        )
    }

    options {
        timestamps()
        timeout(time: 20, unit: 'MINUTES')
        buildDiscarder(logRotator(numToKeepStr: '10'))
    }

    environment {
        APP_NAME    = 'lab-webapp'
        BUILD_VERSION = "1.0.${env.BUILD_NUMBER}"
    }

    stages {
        stage('CI: Checkout') {
            steps {
                echo "📥 Checking out source code..."
                sh '''
                    echo "Simulating git checkout"
                    mkdir -p src tests
                    echo "console.log('App v${BUILD_VERSION}');" > src/app.js
                    echo "console.log('All tests pass');" > tests/app.test.js
                    echo "Source code ready."
                    ls -la
                '''
            }
        }

        stage('CI: Build') {
            steps {
                echo "🔨 Building ${APP_NAME} v${BUILD_VERSION}..."
                sh '''
                    mkdir -p dist
                    cp src/app.js dist/
                    echo "${BUILD_VERSION}" > dist/version.txt
                    tar -czf dist/${APP_NAME}-${BUILD_VERSION}.tar.gz dist/*.js dist/version.txt
                    echo "Build artifact: dist/${APP_NAME}-${BUILD_VERSION}.tar.gz"
                    ls -lh dist/
                '''
                archiveArtifacts artifacts: 'dist/*.tar.gz', fingerprint: true
            }
        }

        stage('CI: Tests') {
            parallel {
                stage('Unit Tests') {
                    steps {
                        sh '''
                            echo "Running unit tests..."
                            mkdir -p test-results
                            cat > test-results/unit.xml << "XML"
<?xml version="1.0"?>
<testsuite name="unit" tests="8" failures="0" errors="0">
  <testcase name="renders_correctly" time="0.01"/>
  <testcase name="handles_input" time="0.02"/>
  <testcase name="validates_form" time="0.01"/>
  <testcase name="api_call_success" time="0.03"/>
  <testcase name="api_call_error_handling" time="0.02"/>
  <testcase name="state_management" time="0.01"/>
  <testcase name="routing" time="0.01"/>
  <testcase name="authentication" time="0.04"/>
</testsuite>
XML
                            echo "Unit tests: 8 passed ✅"
                        '''
                        junit 'test-results/unit.xml'
                    }
                }

                stage('Lint') {
                    steps {
                        sh '''
                            echo "Running linter..."
                            sleep 1
                            echo "Lint: 0 errors, 2 warnings (acceptable) ✅"
                        '''
                    }
                }
            }
        }
    }

    post {
        success {
            echo "✅ CI Stages complete. Artifact: ${APP_NAME} v${BUILD_VERSION}"
        }
        always {
            cleanWs(cleanWhenSuccess: true, cleanWhenFailure: false)
        }
    }
}
```

---

### Exercise 2: Add CD Stages with Environments

Extend the Jenkinsfile from Exercise 1 by adding these stages after the CI test stage:

```groovy
        stage('CD: Deploy to Dev') {
            when {
                expression { params.DEPLOY_TO in ['dev', 'staging'] }
            }
            steps {
                echo "🚀 Deploying to Dev..."
                sh '''
                    echo "Deploying ${APP_NAME} v${BUILD_VERSION} to dev..."
                    echo "docker pull ${APP_NAME}:${BUILD_VERSION}"
                    echo "docker run -d -p 3000:80 ${APP_NAME}:${BUILD_VERSION}"
                    sleep 2
                    echo "Dev deployment complete ✅"
                    echo "URL: http://dev.lab.local:3000"
                '''
            }
            post {
                success {
                    echo "✅ Dev deployment succeeded."
                }
            }
        }

        stage('CD: Dev Tests') {
            when {
                expression { params.DEPLOY_TO in ['dev', 'staging'] }
            }
            steps {
                sh '''
                    echo "Running dev environment tests..."
                    echo "Health check: HTTP 200 ✅"
                    echo "API check: HTTP 200 ✅"
                    echo "Dev tests passed ✅"
                '''
            }
        }

        stage('CD: Deploy to Staging') {
            when {
                expression { params.DEPLOY_TO == 'staging' }
            }
            steps {
                echo "🚀 Deploying to Staging..."
                sh '''
                    echo "Blue-green deployment to staging..."
                    echo "Step 1: Deploy to green environment"
                    echo "Step 2: Health check green environment"
                    echo "Step 3: Switch load balancer to green"
                    echo "Step 4: Tear down blue environment"
                    sleep 2
                    echo "Staging deployment complete ✅"
                    echo "URL: https://staging.lab.example.com"
                '''
            }
        }

        stage('CD: Staging Tests') {
            when {
                expression { params.DEPLOY_TO == 'staging' }
            }
            parallel {
                stage('API Acceptance') {
                    steps {
                        sh 'echo "API acceptance tests: 30 passed ✅"'
                    }
                }
                stage('UI Acceptance') {
                    steps {
                        sh 'echo "UI acceptance tests: 12 passed ✅"'
                    }
                }
            }
        }

        stage('CD: Prod Approval') {
            when {
                expression { params.DEPLOY_TO == 'staging' }
            }
            steps {
                script {
                    timeout(time: 30, unit: 'MINUTES') {
                        input(
                            message: "Deploy ${env.APP_NAME} v${env.BUILD_VERSION} to PRODUCTION?",
                            ok: 'Approve Production Deploy'
                        )
                    }
                    echo "Production deploy approved!"
                }
            }
        }

        stage('CD: Deploy to Production') {
            when {
                expression { params.DEPLOY_TO == 'staging' }
            }
            steps {
                sh '''
                    echo "🚀 DEPLOYING TO PRODUCTION..."
                    echo "Rolling update: 5 replicas"
                    for i in 1 2 3 4 5; do
                        echo "  Updated replica $i/5 ✅"
                        sleep 1
                    done
                    echo "Production deployment complete! 🎉"
                '''
            }
        }
```

---

### Exercise 3: Run the Full Pipeline

```
1. Create the pipeline job:
   - Dashboard → New Item → "lab-cd-pipeline" → Pipeline → OK
   - Scroll to Pipeline section
   - Select "Pipeline script"
   - Paste the complete Jenkinsfile from Exercises 1 + 2
   - Click Save

2. Build with parameters — Run 1: CI only
   - Click "Build with Parameters"
   - DEPLOY_TO: skip
   - Click Build
   - Watch the pipeline: only CI stages run

3. Build with parameters — Run 2: CI + Dev
   - Click "Build with Parameters"
   - DEPLOY_TO: dev
   - Click Build
   - Watch: CI + Dev deployment stages run

4. Build with parameters — Run 3: Full pipeline
   - Click "Build with Parameters"
   - DEPLOY_TO: staging
   - Click Build
   - Watch the pipeline pause at "Prod Approval"
   - Click "Proceed" to approve production deployment
   - Observe the full pipeline complete

5. Explore the Pipeline view:
   - Click the build number
   - View the "Pipeline Steps" page
   - Click on individual stages to see their logs
   - Note the parallel stages running side-by-side
```

---

### Graded Assessment: Jenkins Pipeline

**Review Questions:**

1. What is the key difference between Declarative and Scripted Pipeline syntax?
2. In a Declarative Pipeline, what block runs regardless of whether the pipeline succeeds or fails?
3. What `when` directive would you use to run a stage only when building the `main` branch?
4. How do you run two stages simultaneously in a Declarative Pipeline?
5. What does the `input` step do, and in which block would you typically place it?
6. What is the purpose of `cleanWs()` in the `post` block?

**Practical Pipeline Challenge:**

Write a complete Jenkinsfile for a Node.js application that:

- Accepts a `VERSION` parameter (string) and an `ENV` parameter (choice: dev/prod)
- Has a `Build` stage that simulates running `npm install && npm run build`
- Has a parallel `Test` stage with `Unit Tests` and `Lint` sub-stages
- Has a `Deploy to Dev` stage that always runs
- Has a `Deploy to Production` stage that only runs when `ENV == 'prod'` AND the branch is `main`
- Has a `post` block that cleans the workspace on success and prints a failure message on failure

---

# Conclusion

## Course Summary

Congratulations on completing **Jenkins for Beginners**! Here is a comprehensive recap of everything covered.

---

## Key Concepts Recap

### Module 1: Introduction

**CI/CD** is the practice of automating build, test, and deployment workflows to catch bugs early, reduce manual effort, and enable fast, reliable software delivery. **Continuous Integration** validates every commit; **Continuous Delivery** deploys to staging automatically; **Continuous Deployment** deploys to production automatically.

**Jenkins** is the industry's most widely adopted open-source CI/CD server. Its 1,800+ plugins, pipeline-as-code approach, distributed agent architecture, and massive community make it the default choice for complex enterprise automation needs.

---

### Module 2: Installation

Jenkins requires **Java 17** and is installed via the official package repository on Linux or as a Docker container. The setup wizard installs suggested plugins, creates the admin user, and configures the base URL. The **Jenkins CLI** (`jenkins-cli.jar`) enables full remote administration — building jobs, creating/deleting jobs, managing plugins, controlling the server lifecycle — all scriptable and automatable.

---

### Module 3: System Administration

Jenkins administration spans **plugin management**, **user security** (authentication realms + authorization strategies), **credential storage** (encrypted, injected into builds), and **agent/node management**. **Backup** is critical — at minimum, back up `config.xml`, `credentials.xml`, and all `jobs/*/config.xml` files. Use the `ThinBackup` plugin for GUI-based backups or a cron-scheduled tar script for automation. **Restore** requires stopping Jenkins, extracting the backup, fixing ownership (`chown -R jenkins:jenkins`), and restarting.

---

### Module 4: Jenkins Pipelines

**Jenkinsfiles** define pipelines as code stored in source control — versioned, reviewable, and reproducible. The **Declarative Pipeline** syntax provides a structured `pipeline {}` block with `agent`, `options`, `triggers`, `parameters`, `environment`, `tools`, `stages`, and `post` sections.

Key pipeline patterns:

- **Parallel stages** — run independent stages simultaneously to cut pipeline time
- **`when` directives** — conditionally execute stages based on branch, parameters, or expressions
- **`input` step** — pause for human approval before continuing (essential for production gates)
- **Parallel CI + sequential CD** — run quality gates in parallel; deploy environments in sequence

A full pipeline moves code through: **Checkout → Build → Parallel Tests → Package → Docker Build → Dev Deploy → Staging Deploy → Approval Gate → Production Deploy → Smoke Tests → Tag Release**.

---

## Jenkins Quick Reference

```groovy
// ── AGENT OPTIONS ──────────────────────────────────────────────
agent any
agent none
agent { label 'linux && docker' }
agent { docker { image 'maven:3.9-eclipse-temurin-17' } }

// ── WHEN CONDITIONS ────────────────────────────────────────────
when { branch 'main' }
when { not { branch 'main' } }
when { expression { params.ENV == 'production' } }
when { anyOf { branch 'main'; branch 'release/*' } }
when { allOf { branch 'main'; environment name: 'ENV', value: 'prod' } }

// ── STEP TYPES ─────────────────────────────────────────────────
sh 'command'                               // Shell command (Linux)
bat 'command'                              // Batch command (Windows)
echo 'message'                             // Print to log
script { /* Groovy code */ }              // Arbitrary Groovy

// ── CREDENTIALS ────────────────────────────────────────────────
withCredentials([usernamePassword(
    credentialsId: 'my-cred',
    usernameVariable: 'USR',
    passwordVariable: 'PWD')]) {
    sh 'docker login -u $USR -p $PWD'
}

// ── ARTIFACTS ──────────────────────────────────────────────────
archiveArtifacts artifacts: 'target/*.jar', fingerprint: true
junit 'test-results/**/*.xml'
stash name: 'built-files', includes: 'dist/**'
unstash 'built-files'

// ── FLOW CONTROL ───────────────────────────────────────────────
error 'Stopping pipeline: reason'          // Fail the build
currentBuild.result = 'UNSTABLE'           // Mark as unstable (not failed)
timeout(time: 5, unit: 'MINUTES') { /* */ }
retry(3) { /* */ }

// ── PARALLEL ───────────────────────────────────────────────────
parallel(
    'Unit Tests': { sh 'npm test' },
    'Lint': { sh 'npm run lint' },
    failFast: true    // Abort others if one fails
)

// ── NOTIFICATIONS ──────────────────────────────────────────────
mail to: 'team@example.com',
     subject: "Build ${currentBuild.result}: ${env.JOB_NAME}",
     body: "See ${env.BUILD_URL}"

// ── USEFUL ENVIRONMENT VARIABLES ──────────────────────────────
env.BUILD_NUMBER          // Sequential build number (e.g., "42")
env.BUILD_URL             // URL of this build
env.JOB_NAME              // Name of the job
env.WORKSPACE             // Absolute path to the workspace
env.GIT_COMMIT            // Full Git commit hash
env.GIT_BRANCH            // Current branch name
env.NODE_NAME             // Name of the agent running the build
currentBuild.result       // SUCCESS, FAILURE, UNSTABLE, ABORTED
currentBuild.durationString  // Human-readable build duration
```

---

## CLI Quick Reference

```bash
# ── SETUP ──────────────────────────────────────────────────────
curl -O http://JENKINS:8080/jnlpJars/jenkins-cli.jar
alias jcli="java -jar jenkins-cli.jar -s http://JENKINS:8080 -auth USER:TOKEN"

# ── JOBS ───────────────────────────────────────────────────────
jcli list-jobs                          # List all jobs
jcli build JOB                          # Trigger build
jcli build JOB -s -v                   # Build, wait, show output
jcli build JOB -p KEY=VALUE            # Build with parameter
jcli console JOB [BUILD_NUM]           # Get console output
jcli get-job JOB > job.xml             # Export job config
jcli create-job JOB < job.xml          # Create job from XML
jcli update-job JOB < job.xml          # Update job config
jcli delete-job JOB                     # Delete job
jcli enable-job JOB                     # Enable job
jcli disable-job JOB                    # Disable job

# ── SERVER ADMIN ───────────────────────────────────────────────
jcli who-am-i                           # Show current user
jcli version                            # Jenkins version
jcli list-plugins                       # Installed plugins
jcli install-plugin PLUGIN             # Install plugin
jcli safe-restart                       # Graceful restart
jcli safe-shutdown                      # Graceful shutdown
jcli reload-configuration              # Reload config from disk
jcli quiet-down                         # Pause new builds
jcli cancel-quiet-down                 # Resume new builds

# ── NODES ──────────────────────────────────────────────────────
jcli list-nodes                         # List all nodes/agents
jcli offline-node NODE -m "reason"     # Take node offline
jcli online-node NODE                   # Bring node online
jcli delete-node NODE                   # Delete a node
```

---

## Recommended Next Steps

**Deepen Your Jenkins Knowledge:**

- **Shared Libraries** — Write reusable Groovy functions used across all your Jenkinsfiles
- **Multibranch Pipelines** — Automatically create pipeline jobs for every branch and pull request
- **Jenkins Configuration as Code (JCasC)** — Define all Jenkins configuration in YAML files
- **Blue Ocean** — The modern Jenkins UI optimized for pipeline visualization
- **Kubernetes Plugin** — Dynamic build agents that spin up as Kubernetes Pods and disappear when done

**Complementary DevOps Tools:**

- **Docker** — Container runtime for building and packaging applications
- **Kubernetes** — Container orchestration (Jenkins deploys to it)
- **Ansible / Terraform** — Infrastructure as code tools Jenkins can trigger
- **SonarQube** — Code quality and security scanning integrated into CI pipelines
- **Nexus / Artifactory** — Artifact repositories for storing build outputs
- **HashiCorp Vault** — Enterprise secret management that Jenkins can integrate with

**Resources:**

- [Jenkins Official Documentation](https://www.jenkins.io/doc/)
- [Jenkins Pipeline Syntax Reference](https://www.jenkins.io/doc/book/pipeline/syntax/)
- [Jenkins Plugins Index](https://plugins.jenkins.io/)
- [Jenkins Community Forums](https://community.jenkins.io/)
- [Jenkinsfile Examples (GitHub)](https://github.com/jenkinsci/pipeline-examples)

---

_This tutorial was created to provide a comprehensive introduction to Jenkins for DevOps practitioners. All pipeline examples use Declarative Pipeline syntax compatible with Jenkins 2.332+ with the Pipeline plugin installed._