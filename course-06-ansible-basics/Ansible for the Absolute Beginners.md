# Ansible for the Absolute Beginners

## A Comprehensive Tutorial with Hands-On Labs

---

> **About This Course**
> 
> This tutorial is designed for IT professionals, system administrators, and developers who are new to Ansible. By the end of this course, you will have the practical skills to automate infrastructure provisioning, configuration management, and application deployment using Ansible. Each module builds on the previous one, and hands-on labs reinforce every concept with real-world exercises.

---

## Table of Contents

- [Module 1 – Introduction and Ansible Inventory](https://claude.ai/local_sessions/local_c16524e5-1c07-464f-ba05-5cd93beac4e2#module-1--introduction-and-ansible-inventory)
- [Module 2 – Ansible Variables](https://claude.ai/local_sessions/local_c16524e5-1c07-464f-ba05-5cd93beac4e2#module-2--ansible-variables)
- [Module 3 – Ansible Concepts](https://claude.ai/local_sessions/local_c16524e5-1c07-464f-ba05-5cd93beac4e2#module-3--ansible-concepts)
- [Module 4 – Advanced Ansible Techniques](https://claude.ai/local_sessions/local_c16524e5-1c07-464f-ba05-5cd93beac4e2#module-4--advanced-ansible-techniques)

---

# Module 1 – Introduction and Ansible Inventory

## Module Overview

This module gives participants a practical foundation in Ansible and the essentials of managing infrastructure with inventories. You'll start with Ansible's purpose and advantages in IT automation, then set up a local lab environment and install Ansible. Through interactive labs, you'll get comfortable with YAML syntax and learn how to define and organize hosts in Ansible inventories.

### Learning Objectives

- Gain proficiency in working with Ansible Inventory
- Understand the concept and importance of Ansible inventory in managing nodes
- Gain an understanding of Ansible and its significance in IT automation
- Learn how to set up an Ansible local environment using VirtualBox
- Acquire skills in installing Ansible on a local machine
- Understand YAML syntax and its importance in Ansible configurations

---

## 1.1 Ansible Introduction

### What is Ansible?

Ansible is an open-source IT automation tool developed by Red Hat. It enables you to automate repetitive IT tasks such as:

- **Configuration Management** – Ensuring servers are configured correctly and consistently
- **Application Deployment** – Deploying applications across many servers simultaneously
- **Orchestration** – Coordinating complex multi-tier workflows
- **Provisioning** – Setting up cloud infrastructure, virtual machines, and containers

### Why Ansible?

Ansible stands out from other automation tools for several key reasons:

|Feature|Description|
|---|---|
|**Agentless**|No software needs to be installed on managed nodes; Ansible uses SSH (Linux) or WinRM (Windows)|
|**Simple YAML Syntax**|Playbooks are written in human-readable YAML, lowering the barrier to entry|
|**Idempotent**|Running a playbook multiple times produces the same result; safe to re-run|
|**Large Module Library**|Thousands of built-in modules cover nearly every infrastructure task|
|**Extensible**|Write custom modules in Python when built-in modules don't cover your needs|
|**Community & Support**|Backed by Red Hat with a massive open-source community (Ansible Galaxy)|

### How Ansible Works

Ansible follows a **push-based** model:

```
┌─────────────────────────────────────────────────────────────────┐
│                      Control Node                               │
│   ┌──────────┐   ┌──────────────┐   ┌──────────────────────┐  │
│   │Inventory │   │  Playbooks   │   │  Ansible Engine       │  │
│   │(hosts)   │ + │  (YAML)      │ → │  (executes tasks)     │  │
│   └──────────┘   └──────────────┘   └──────────┬───────────┘  │
└─────────────────────────────────────────────────┼───────────────┘
                                                  │ SSH / WinRM
                            ┌─────────────────────┼──────────────┐
                            │                     │              │
                      ┌─────▼──────┐    ┌─────────▼──┐   ┌──────▼─────┐
                      │ web01      │    │ db01        │   │ app01      │
                      │ (Managed)  │    │ (Managed)   │   │ (Managed)  │
                      └────────────┘    └─────────────┘   └────────────┘
```

1. You write a **Playbook** describing the desired state
2. Ansible reads the **Inventory** to know which hosts to target
3. Ansible connects via **SSH** and pushes/executes tasks
4. No persistent agent runs on managed nodes

### Key Ansible Components

- **Control Node** – The machine where Ansible is installed and run from
- **Managed Nodes** – The servers Ansible manages (also called "hosts")
- **Inventory** – A list of managed nodes
- **Playbook** – A YAML file describing automation tasks
- **Module** – A unit of work (e.g., install a package, create a file, restart a service)
- **Task** – A single call to a module within a playbook
- **Role** – A reusable, organized collection of tasks, variables, and templates

---

## 1.2 Demo: Setup Ansible Local Environment Using VirtualBox

### Prerequisites

Before setting up the lab environment, ensure you have:

- A host machine with at least **8 GB RAM** and **40 GB** free disk space
- **VirtualBox** installed (version 6.1 or later)
- Internet access for downloading ISOs and packages

### Step 1: Download and Install VirtualBox

1. Visit [https://www.virtualbox.org/wiki/Downloads](https://www.virtualbox.org/wiki/Downloads)
2. Download the installer for your operating system (Windows, macOS, or Linux)
3. Run the installer and accept the default settings
4. Install the **VirtualBox Extension Pack** for USB 2.0/3.0 support

### Step 2: Create the Control Node VM

1. Open VirtualBox and click **New**
2. Configure the VM:
    - **Name**: `ansible-control`
    - **Type**: Linux
    - **Version**: Ubuntu (64-bit)
    - **RAM**: 2048 MB (2 GB)
    - **Disk**: 20 GB (dynamically allocated)
3. Download Ubuntu Server 22.04 LTS ISO from [https://ubuntu.com/download/server](https://ubuntu.com/download/server)
4. Attach the ISO and complete the OS installation

### Step 3: Create Managed Node VMs

Repeat the VM creation process for two managed nodes:

|VM Name|RAM|Disk|Purpose|
|---|---|---|---|
|`node01`|1024 MB|10 GB|Managed node 1 (web server)|
|`node02`|1024 MB|10 GB|Managed node 2 (database server)|

### Step 4: Configure Networking

Set all three VMs to use a **Host-Only Network** so they can communicate:

1. In VirtualBox, go to **File → Host Network Manager**
2. Create a new host-only network (e.g., `192.168.56.0/24`)
3. For each VM: **Settings → Network → Adapter 2 → Host-Only Adapter**

### Step 5: Configure SSH Key-Based Authentication

On the control node, generate an SSH key pair and copy the public key to each managed node:

```bash
# On ansible-control
ssh-keygen -t rsa -b 4096 -C "ansible@control"
# Press Enter to accept defaults

# Copy public key to each managed node
ssh-copy-id ansible@192.168.56.101  # node01
ssh-copy-id ansible@192.168.56.102  # node02

# Test SSH connectivity
ssh ansible@192.168.56.101 "hostname"
ssh ansible@192.168.56.102 "hostname"
```

### Step 6: Configure /etc/hosts (Optional but Recommended)

```bash
# On ansible-control, edit /etc/hosts
sudo nano /etc/hosts

# Add these lines:
192.168.56.101  node01
192.168.56.102  node02
```

---

## 1.3 Demo: Install Ansible

### Installing Ansible on Ubuntu/Debian

```bash
# Update the package index
sudo apt update

# Install software-properties-common
sudo apt install -y software-properties-common

# Add the Ansible PPA repository
sudo add-apt-repository --yes --update ppa:ansible/ansible

# Install Ansible
sudo apt install -y ansible

# Verify installation
ansible --version
```

Expected output:

```
ansible [core 2.16.x]
  config file = /etc/ansible/ansible.cfg
  configured module search path = ['/home/user/.ansible/plugins/modules', ...]
  ansible python module location = /usr/lib/python3/dist-packages/ansible
  ...
  python version = 3.10.x
```

### Installing Ansible on RHEL/CentOS/Fedora

```bash
# For RHEL/CentOS 8+
sudo dnf install -y epel-release
sudo dnf install -y ansible

# For Fedora
sudo dnf install -y ansible

# Verify installation
ansible --version
```

### Installing Ansible via pip (Any Platform)

```bash
# Install pip if not present
sudo apt install -y python3-pip   # Ubuntu/Debian

# Install Ansible via pip
pip3 install ansible

# Verify installation
ansible --version
```

### Ansible Configuration File

Ansible looks for its configuration file in the following order:

1. `ANSIBLE_CONFIG` environment variable
2. `./ansible.cfg` (current directory)
3. `~/.ansible.cfg` (home directory)
4. `/etc/ansible/ansible.cfg` (global default)

The default configuration file at `/etc/ansible/ansible.cfg` contains many settings. Key settings include:

```ini
[defaults]
inventory      = /etc/ansible/hosts    # Default inventory location
remote_user    = ansible               # Default SSH user
host_key_checking = False             # Disable SSH host key checking (useful in labs)
log_path       = /var/log/ansible.log  # Log file location

[privilege_escalation]
become         = True                  # Enable privilege escalation by default
become_method  = sudo                  # Use sudo for privilege escalation
```

### Test Your First Ansible Command

```bash
# Ping all hosts (connectivity test)
ansible all -m ping

# Expected output:
# node01 | SUCCESS => {
#     "changed": false,
#     "ping": "pong"
# }
# node02 | SUCCESS => {
#     "changed": false,
#     "ping": "pong"
# }
```

---

## 1.4 Understanding YAML

YAML (YAML Ain't Markup Language) is the language used to write Ansible playbooks and configuration files. It is designed to be human-readable and easy to write.

### YAML Basics

#### Key-Value Pairs

```yaml
# Simple key-value pairs
name: John Doe
age: 30
city: New York
active: true
```

#### Lists (Sequences)

```yaml
# List with hyphens
fruits:
  - apple
  - banana
  - cherry

# Inline list
colors: [red, green, blue]
```

#### Dictionaries (Mappings)

```yaml
# Dictionary (nested key-value pairs)
person:
  name: Jane Doe
  age: 25
  email: jane@example.com

# Inline dictionary
coordinates: {x: 10, y: 20}
```

#### Multi-line Strings

```yaml
# Literal block (preserves newlines) - use |
message: |
  This is line one.
  This is line two.
  This is line three.

# Folded block (folds newlines into spaces) - use >
description: >
  This long text will be
  folded into a single line.
```

#### Comments

```yaml
# This is a YAML comment
name: example  # Inline comment
```

#### Data Types

```yaml
# String
hostname: "web-server-01"
os: Ubuntu

# Integer
port: 8080
max_connections: 100

# Float
version: 2.5

# Boolean
enabled: true
debug: false

# Null
value: null
empty: ~

# List of dictionaries
users:
  - name: alice
    role: admin
    active: true
  - name: bob
    role: developer
    active: false
```

### YAML in Ansible Context

Here is how YAML maps to an Ansible playbook structure:

```yaml
---
# Three dashes indicate the start of a YAML document
- name: My first playbook       # String value
  hosts: webservers             # String value
  become: true                  # Boolean value
  vars:                         # Dictionary
    http_port: 80               # Integer value
    app_name: myapp             # String value

  tasks:                        # List of dictionaries
    - name: Install Apache      # First task (dictionary)
      apt:                      # Module name
        name: apache2           # Module parameter
        state: present          # Module parameter

    - name: Start Apache        # Second task
      service:
        name: apache2
        state: started
        enabled: true
```

### Common YAML Pitfalls

```yaml
# ❌ Wrong: Tabs are NOT allowed in YAML (use spaces only)
name:	value       # This uses a tab - will cause error

# ✅ Correct: Use spaces for indentation
name: value

# ❌ Wrong: Inconsistent indentation
tasks:
  - name: task1
      module:         # Extra indentation - will cause error
        param: value

# ✅ Correct: Consistent 2-space indentation
tasks:
  - name: task1
    module:
      param: value

# ❌ Wrong: Missing space after colon
name:value            # Will be treated as a string, not key-value

# ✅ Correct: Space after colon
name: value
```

---

## 🧪 Hands-on Lab: YAML

### Lab Objectives

- Practice writing valid YAML structures
- Identify and fix common YAML errors
- Understand YAML data types and structures in the context of Ansible

### Lab Duration: 30 minutes

---

### Exercise 1: Create a Valid YAML File

Create a file named `server_config.yaml` that describes a web server configuration using all YAML data types.

**Requirements:**

- Server name and IP address (strings)
- Port number (integer)
- SSL enabled flag (boolean)
- List of installed packages
- Dictionary of environment variables

**Solution:**

```yaml
---
server:
  name: "web-prod-01"
  ip_address: 192.168.1.100
  port: 443
  ssl_enabled: true
  max_connections: 1000
  owner: null

packages:
  - nginx
  - python3
  - certbot
  - ufw

environment_variables:
  APP_ENV: production
  DEBUG: "false"
  LOG_LEVEL: info
  DB_HOST: db-prod-01

description: >
  This is the primary production
  web server running nginx with SSL.

startup_script: |
  #!/bin/bash
  systemctl start nginx
  systemctl enable nginx
```

**Validate with Python:**

```bash
python3 -c "import yaml; yaml.safe_load(open('server_config.yaml')); print('YAML is valid!')"
```

---

### Exercise 2: Fix the Broken YAML

The following YAML contains several errors. Identify and fix them all.

**Broken YAML:**

```yaml
---
- name: Broken Playbook
hosts: all
  become:true
  vars:
    http_port:80
    packages:
    - nginx
    - php
  tasks:
  	- name: Install packages
      apt:
        name: {{ packages }}
        state:present
```

**Fixed YAML:**

```yaml
---
- name: Broken Playbook
  hosts: all          # Fixed: added 2-space indentation
  become: true        # Fixed: added space after colon
  vars:
    http_port: 80     # Fixed: added space after colon
    packages:
      - nginx         # Fixed: added proper indentation
      - php
  tasks:
    - name: Install packages    # Fixed: replaced tab with spaces
      apt:
        name: "{{ packages }}"  # Fixed: quoted Jinja2 template
        state: present          # Fixed: added space after colon
```

---

### Exercise 3: Write a Server Inventory in YAML Format

Create a YAML file representing an infrastructure inventory with 3 web servers, 2 database servers, and a load balancer. Include IP addresses, ports, and roles for each.

**Solution:**

```yaml
---
infrastructure:
  load_balancers:
    - name: lb01
      ip: 10.0.0.10
      port: 80
      role: load_balancer
      active: true

  web_servers:
    - name: web01
      ip: 10.0.1.10
      port: 8080
      role: web
      active: true
    - name: web02
      ip: 10.0.1.11
      port: 8080
      role: web
      active: true
    - name: web03
      ip: 10.0.1.12
      port: 8080
      role: web
      active: false

  database_servers:
    - name: db01
      ip: 10.0.2.10
      port: 5432
      role: primary
      active: true
    - name: db02
      ip: 10.0.2.11
      port: 5432
      role: replica
      active: true
```

---

## 1.5 Ansible Inventory

### What is an Ansible Inventory?

The **inventory** is Ansible's source of truth about the nodes it manages. It tells Ansible:

- **Which hosts** to manage
- **How to connect** to those hosts
- **How to group** hosts for targeted task execution

Without an inventory, Ansible has no targets to work with.

### Default Inventory Location

By default, Ansible reads from `/etc/ansible/hosts`. You can override this with:

```bash
# Using -i flag
ansible-playbook -i /path/to/inventory playbook.yml

# Using environment variable
export ANSIBLE_INVENTORY=/path/to/inventory

# In ansible.cfg
[defaults]
inventory = /path/to/inventory
```

---

## 1.6 Inventory Formats

Ansible supports two primary inventory formats: **INI** and **YAML**.

### INI Format

The INI format is the traditional and most widely used format. It is simple and easy to read.

```ini
# /etc/ansible/hosts (INI format)

# Ungrouped hosts (no group)
192.168.56.10
mail.example.com

# [group_name] defines a group
[webservers]
web01.example.com
web02.example.com
192.168.56.101

[dbservers]
db01.example.com  ansible_port=5432
db02.example.com

# Host with connection variables
[special]
jumpbox01  ansible_host=192.168.56.200  ansible_user=admin  ansible_port=2222
```

### YAML Format

The YAML format is more explicit and supports complex data structures. It is preferred for larger, more complex inventories.

```yaml
# inventory.yaml (YAML format)
all:
  hosts:
    mail.example.com:
    192.168.56.10:
  children:
    webservers:
      hosts:
        web01.example.com:
        web02.example.com:
        192.168.56.101:
    dbservers:
      hosts:
        db01.example.com:
          ansible_port: 5432
        db02.example.com:
    special:
      hosts:
        jumpbox01:
          ansible_host: 192.168.56.200
          ansible_user: admin
          ansible_port: 2222
```

### Inventory Variables

You can define variables directly in the inventory to customize behavior per host or group.

#### Host Variables (in INI)

```ini
[webservers]
web01  ansible_host=192.168.56.101  http_port=80  max_clients=200
web02  ansible_host=192.168.56.102  http_port=8080 max_clients=100
```

#### Group Variables (in INI)

```ini
[webservers]
web01
web02

[webservers:vars]
ansible_user=deploy
http_port=80
document_root=/var/www/html
```

#### Inventory Variable Files

For cleaner inventories, use separate variable files:

```
inventory/
├── hosts.ini          # Main inventory file
├── group_vars/
│   ├── all.yaml       # Variables for ALL hosts
│   ├── webservers.yaml
│   └── dbservers.yaml
└── host_vars/
    ├── web01.yaml     # Variables specific to web01
    └── db01.yaml
```

**`group_vars/webservers.yaml`:**

```yaml
---
http_port: 80
document_root: /var/www/html
ansible_user: deploy
max_clients: 200
```

**`host_vars/web01.yaml`:**

```yaml
---
http_port: 443
ssl_enabled: true
ssl_cert_path: /etc/ssl/certs/web01.crt
```

### Common Inventory Parameters

|Parameter|Description|Example|
|---|---|---|
|`ansible_host`|The actual IP or hostname to connect to|`ansible_host=192.168.1.10`|
|`ansible_port`|SSH port (default: 22)|`ansible_port=2222`|
|`ansible_user`|SSH user to connect as|`ansible_user=ubuntu`|
|`ansible_password`|SSH password (prefer SSH keys)|`ansible_password=secret`|
|`ansible_ssh_private_key_file`|Path to SSH private key|`ansible_ssh_private_key_file=~/.ssh/id_rsa`|
|`ansible_become`|Enable privilege escalation|`ansible_become=true`|
|`ansible_become_user`|User to escalate to|`ansible_become_user=root`|
|`ansible_python_interpreter`|Python interpreter path|`ansible_python_interpreter=/usr/bin/python3`|
|`ansible_connection`|Connection type|`ansible_connection=local` or `ssh`|

### Dynamic Inventory

For cloud environments, Ansible supports **dynamic inventory** through plugins that query APIs:

```bash
# AWS EC2 dynamic inventory
ansible-inventory -i aws_ec2.yaml --list

# Example aws_ec2.yaml plugin config:
# plugin: amazon.aws.aws_ec2
# regions:
#   - us-east-1
# filters:
#   instance-state-name: running
```

### Viewing Your Inventory

```bash
# List all hosts in inventory
ansible-inventory -i inventory.ini --list

# Show inventory as a graph
ansible-inventory -i inventory.ini --graph

# Example graph output:
# @all:
#   |--@webservers:
#   |  |--web01
#   |  |--web02
#   |--@dbservers:
#   |  |--db01
#   |  |--db02
#   |--@ungrouped:
#      |--mail.example.com
```

---

## 🧪 Hands-on Lab: Inventory

### Lab Objectives

- Create and validate an Ansible inventory file
- Work with both INI and YAML inventory formats
- Define host and group variables
- Use inventory groups to target specific hosts

### Lab Duration: 45 minutes

---

### Exercise 1: Create a Basic INI Inventory

Create a file named `inventory.ini` that represents the following infrastructure:

- **Load Balancer**: `lb01` at `192.168.56.100`
- **Web Servers**: `web01` at `192.168.56.101`, `web02` at `192.168.56.102`
- **Database Servers**: `db01` at `192.168.56.103`, `db02` at `192.168.56.104`
- All servers connect via user `ansible` with sudo enabled

**Solution:**

```ini
# inventory.ini

[loadbalancers]
lb01  ansible_host=192.168.56.100

[webservers]
web01  ansible_host=192.168.56.101
web02  ansible_host=192.168.56.102

[dbservers]
db01  ansible_host=192.168.56.103
db02  ansible_host=192.168.56.104

[all:vars]
ansible_user=ansible
ansible_become=true
ansible_become_method=sudo
ansible_ssh_private_key_file=~/.ssh/id_rsa
```

**Test the inventory:**

```bash
# List all hosts
ansible all -i inventory.ini --list-hosts

# Ping web servers only
ansible webservers -i inventory.ini -m ping

# Run command on db servers
ansible dbservers -i inventory.ini -m command -a "hostname"
```

---

### Exercise 2: Convert to YAML Inventory

Convert the INI inventory from Exercise 1 to YAML format.

**Solution:**

```yaml
# inventory.yaml
all:
  vars:
    ansible_user: ansible
    ansible_become: true
    ansible_become_method: sudo
    ansible_ssh_private_key_file: ~/.ssh/id_rsa

  children:
    loadbalancers:
      hosts:
        lb01:
          ansible_host: 192.168.56.100

    webservers:
      hosts:
        web01:
          ansible_host: 192.168.56.101
        web02:
          ansible_host: 192.168.56.102

    dbservers:
      hosts:
        db01:
          ansible_host: 192.168.56.103
        db02:
          ansible_host: 192.168.56.104
```

**Verify:**

```bash
ansible-inventory -i inventory.yaml --graph
ansible all -i inventory.yaml --list-hosts
```

---

### Exercise 3: Add Group-Specific Variables

Create `group_vars` directory with variables for each group:

```bash
mkdir -p group_vars host_vars
```

**`group_vars/webservers.yaml`:**

```yaml
---
http_port: 80
document_root: /var/www/html
nginx_worker_processes: auto
```

**`group_vars/dbservers.yaml`:**

```yaml
---
db_port: 5432
db_name: appdb
db_user: appuser
max_connections: 100
```

**`host_vars/db01.yaml`:**

```yaml
---
# db01 is the primary, so it gets extra settings
db_role: primary
db_sync_mode: synchronous
```

**Test that variables are accessible:**

```bash
# Show all variables for a specific host
ansible-inventory -i inventory.yaml --host db01
```

---

## 1.7 Grouping and Parent-Child Relationships

### Why Group Hosts?

Grouping allows you to:

- Target specific subsets of servers with tasks
- Apply variables to multiple hosts at once
- Create logical organization of your infrastructure

### Parent-Child Group Relationships

Ansible supports **nested groups** (parent-child relationships) where a parent group contains child groups. This is also called **group of groups**.

#### INI Format - Parent-Child

```ini
[webservers_us]
web-us-01
web-us-02

[webservers_eu]
web-eu-01
web-eu-02

[webservers_apac]
web-apac-01

# Parent group containing child groups
# Use :children suffix
[webservers:children]
webservers_us
webservers_eu
webservers_apac

[dbservers]
db01
db02

# All production servers
[production:children]
webservers
dbservers

# Group-level variables apply to all children
[production:vars]
environment=production
log_level=warning
```

#### YAML Format - Parent-Child

```yaml
all:
  children:
    production:
      children:
        webservers:
          children:
            webservers_us:
              hosts:
                web-us-01:
                web-us-02:
            webservers_eu:
              hosts:
                web-eu-01:
                web-eu-02:
            webservers_apac:
              hosts:
                web-apac-01:
        dbservers:
          hosts:
            db01:
            db02:
      vars:
        environment: production
        log_level: warning

    staging:
      children:
        webservers_staging:
          hosts:
            web-stage-01:
        dbservers_staging:
          hosts:
            db-stage-01:
      vars:
        environment: staging
        log_level: debug
```

### The `all` Group

Every Ansible inventory has two implicit groups:

- `all` – Contains every host in the inventory
- `ungrouped` – Contains hosts that don't belong to any other group

```bash
# Target all hosts
ansible all -m ping

# Target only ungrouped hosts
ansible ungrouped -m ping
```

### Best Practices for Inventory Organization

```
project/
├── ansible.cfg
├── inventory/
│   ├── production/
│   │   ├── hosts.yaml          # Production inventory
│   │   ├── group_vars/
│   │   │   ├── all.yaml
│   │   │   ├── webservers.yaml
│   │   │   └── dbservers.yaml
│   │   └── host_vars/
│   │       ├── web01.yaml
│   │       └── db01.yaml
│   └── staging/
│       ├── hosts.yaml          # Staging inventory
│       ├── group_vars/
│       └── host_vars/
├── playbooks/
└── roles/
```

### Targeting Patterns

```bash
# Target all hosts
ansible all -m ping

# Target a specific group
ansible webservers -m ping

# Target a specific host
ansible web01 -m ping

# Target multiple groups
ansible webservers:dbservers -m ping

# Target all except a group (negation)
ansible 'all:!dbservers' -m ping

# Target intersection of two groups
ansible 'webservers:&production' -m ping

# Wildcard patterns
ansible 'web*' -m ping

# Limit to first N hosts in a group
ansible webservers -m ping --limit 'webservers[0]'
```

---

# Module 2 – Ansible Variables

## Module Overview

"Ansible Variables" explores variable management in Ansible playbooks, covering types, scoping, and precedence. Participants learn to register variables, understand scoping rules, and leverage magic variables for insights about the environment.

### Learning Objectives

- Understand Variable scoping and Variable precedence
- Gain proficiency in working with Ansible Variables
- Explore Ansible variables and their significance in managing system configurations

---

## 2.1 Ansible Variables

### What are Variables in Ansible?

Variables in Ansible allow you to manage differences between systems, environments, and configurations without duplicating code. Instead of hardcoding values, you use variables that can be defined in many places and referenced throughout your playbooks.

### Variable Naming Rules

```yaml
# ✅ Valid variable names
http_port: 80
server_name: web01
max_connections: 200
ssl_enabled: true

# ❌ Invalid variable names
# Cannot start with a number
1st_server: web01

# Cannot use hyphens (use underscores instead)
http-port: 80

# Cannot use Python keywords
class: production
```

### Defining Variables in Playbooks

```yaml
---
- name: Web Server Setup
  hosts: webservers
  vars:
    http_port: 80
    document_root: /var/www/html
    server_name: "{{ inventory_hostname }}"

  tasks:
    - name: Display the configured port
      debug:
        msg: "Web server is listening on port {{ http_port }}"

    - name: Create document root
      file:
        path: "{{ document_root }}"
        state: directory
        mode: '0755'
```

### Variable Files (vars_files)

```yaml
---
- name: Web Server Setup
  hosts: webservers
  vars_files:
    - vars/common.yaml
    - vars/webserver.yaml

  tasks:
    - name: Install web packages
      apt:
        name: "{{ web_packages }}"
        state: present
```

**`vars/webserver.yaml`:**

```yaml
---
http_port: 80
https_port: 443
document_root: /var/www/html
web_packages:
  - nginx
  - php-fpm
  - php-mysql
```

### Referencing Variables

Variables are referenced using **Jinja2** template syntax: `{{ variable_name }}`

```yaml
tasks:
  - name: Configure nginx
    template:
      src: nginx.conf.j2
      dest: /etc/nginx/nginx.conf

  - name: Display message
    debug:
      msg: "Server {{ server_name }} is running on port {{ http_port }}"

  - name: Use variable in a condition
    apt:
      name: nginx
      state: "{{ 'present' if install_nginx else 'absent' }}"
```

---

## 2.2 Variable Types

### String Variables

```yaml
vars:
  server_name: "web01"
  env: production
  message: "Hello, World!"
  multiline: |
    Line one
    Line two
```

### Number Variables

```yaml
vars:
  http_port: 80
  max_retries: 3
  timeout: 30.5
```

### Boolean Variables

```yaml
vars:
  ssl_enabled: true
  debug_mode: false
  install_dependencies: yes   # 'yes' and 'no' are also valid
```

### List Variables

```yaml
vars:
  packages:
    - nginx
    - php-fpm
    - mysql-client

  ports:
    - 80
    - 443
    - 8080
```

Accessing list items:

```yaml
tasks:
  - name: Show first package
    debug:
      msg: "First package: {{ packages[0] }}"

  - name: Show last port
    debug:
      msg: "Last port: {{ ports[-1] }}"
```

### Dictionary Variables

```yaml
vars:
  database:
    host: db01
    port: 5432
    name: appdb
    user: appuser
    password: "{{ vault_db_password }}"

  nginx_config:
    worker_processes: auto
    worker_connections: 1024
    keepalive_timeout: 65
```

Accessing dictionary values:

```yaml
tasks:
  - name: Show DB host (dot notation)
    debug:
      msg: "DB Host: {{ database.host }}"

  - name: Show DB port (bracket notation)
    debug:
      msg: "DB Port: {{ database['port'] }}"
```

### Combining Variables

```yaml
vars:
  base_dir: /opt/myapp
  config_dir: "{{ base_dir }}/config"
  log_dir: "{{ base_dir }}/logs"
  db_url: "postgresql://{{ db_user }}:{{ db_pass }}@{{ db_host }}:{{ db_port }}/{{ db_name }}"
```

---

## 2.3 Registering Variables and Variable Precedence

### Registering Variables

The `register` keyword captures the output of a task into a variable for use in subsequent tasks.

```yaml
---
- name: Check and use task output
  hosts: all
  tasks:
    - name: Get current date
      command: date
      register: current_date_output

    - name: Display the captured date
      debug:
        msg: "Current date is: {{ current_date_output.stdout }}"

    - name: Check if a file exists
      stat:
        path: /etc/nginx/nginx.conf
      register: nginx_conf

    - name: Show file status
      debug:
        msg: "Nginx config exists: {{ nginx_conf.stat.exists }}"

    - name: Only proceed if config exists
      debug:
        msg: "Config file size: {{ nginx_conf.stat.size }} bytes"
      when: nginx_conf.stat.exists
```

### Registered Variable Structure

```yaml
tasks:
  - name: Run a shell command
    shell: "ls /var/www"
    register: ls_output

  # The register variable typically contains:
  - debug:
      var: ls_output
  # Output structure:
  # {
  #   "changed": true,
  #   "cmd": "ls /var/www",
  #   "rc": 0,                  # Return code (0 = success)
  #   "stdout": "html\nlogs",   # Standard output
  #   "stderr": "",             # Standard error
  #   "stdout_lines": ["html", "logs"]  # Output as list
  # }
```

### Variable Precedence

Ansible applies variables in a specific order, with **higher numbers overriding lower numbers**. The full precedence order (lowest to highest):

|Priority|Variable Source|
|---|---|
|1|Command line values (`-e` / `--extra-vars`)|
|2|Role defaults (`roles/x/defaults/main.yaml`)|
|3|Inventory file or script group `vars`|
|4|Inventory `group_vars/all`|
|5|Playbook `group_vars/all`|
|6|Inventory `group_vars/*`|
|7|Playbook `group_vars/*`|
|8|Inventory file or script host `vars`|
|9|Inventory `host_vars/*`|
|10|Playbook `host_vars/*`|
|11|Host facts / cached `set_facts`|
|12|Play `vars`|
|13|Play `vars_prompt`|
|14|Play `vars_files`|
|15|Role `vars` (`roles/x/vars/main.yaml`)|
|16|Block `vars` (only for tasks in block)|
|17|Task `vars` (only for the task)|
|18|`include_vars`|
|19|`set_facts` / registered variables|
|20|Role (and include_role) params|
|21|`include` params|
|**22**|**Extra vars (`-e`)** ← **Always wins**|

**Key Rule:** Extra vars (`-e`) always have the highest precedence.

```bash
# Extra vars always override everything
ansible-playbook playbook.yml -e "http_port=9090 env=testing"
```

---

## 2.4 Variable Scoping

### Scope Levels

Variables in Ansible have three scope levels:

#### 1. Global Scope

Variables available to all plays, hosts, and tasks:

- Extra vars (`-e`)
- Variables defined in `ansible.cfg`

#### 2. Play Scope

Variables available to all tasks within a play:

- `vars:` in a play
- `vars_files:` in a play
- `group_vars/` and `host_vars/`

```yaml
---
- name: Play 1
  hosts: webservers
  vars:
    my_var: "I exist in Play 1"    # Only available in Play 1
  tasks:
    - debug:
        msg: "{{ my_var }}"        # Works

- name: Play 2
  hosts: dbservers
  tasks:
    - debug:
        msg: "{{ my_var }}"        # ERROR: my_var not defined here
```

#### 3. Host Scope

Variables tied to a specific host:

- Facts gathered by `setup` module
- `host_vars/`
- Variables set with `set_fact`

```yaml
tasks:
  - name: Set a host-scoped variable
    set_fact:
      my_custom_fact: "This host's custom value"

  - name: Use the host-scoped variable
    debug:
      msg: "{{ my_custom_fact }}"
```

### Scope Example

```yaml
---
- name: Demonstrating Variable Scope
  hosts: all
  vars:
    play_var: "I am play-scoped"

  tasks:
    - name: Set a host-specific variable
      set_fact:
        host_var: "I am host-scoped for {{ inventory_hostname }}"

    - name: Show play-scoped variable
      debug:
        msg: "Play var: {{ play_var }}"

    - name: Show host-scoped variable
      debug:
        msg: "Host var: {{ host_var }}"

- name: Second Play - play_var is gone, host_var persists
  hosts: all
  tasks:
    - name: This will fail - play_var is out of scope
      debug:
        msg: "{{ play_var }}"        # UndefinedError
      ignore_errors: true

    - name: This works - host_var persists across plays
      debug:
        msg: "{{ host_var }}"        # Works!
```

---

## 2.5 Magic Variables

Magic variables are special variables automatically set by Ansible. They provide information about the current play, hosts, and environment. You cannot set them yourself, but you can read them.

### Commonly Used Magic Variables

#### `inventory_hostname`

The name of the current host as defined in the inventory:

```yaml
tasks:
  - name: Show current host name
    debug:
      msg: "Managing host: {{ inventory_hostname }}"

  - name: Create host-specific config
    template:
      src: config.j2
      dest: "/etc/myapp/{{ inventory_hostname }}.conf"
```

#### `ansible_host`

The actual IP or hostname used to connect:

```yaml
tasks:
  - name: Show connection address
    debug:
      msg: "Connecting to: {{ ansible_host }}"
```

#### `groups`

A dictionary of all groups and their hosts:

```yaml
tasks:
  - name: List all web servers
    debug:
      msg: "Web servers: {{ groups['webservers'] }}"

  - name: Check if host is in a group
    debug:
      msg: "This host is a web server"
    when: inventory_hostname in groups['webservers']
```

#### `hostvars`

A dictionary of all variables for all hosts:

```yaml
tasks:
  - name: Get another host's IP
    debug:
      msg: "db01's IP is: {{ hostvars['db01']['ansible_host'] }}"

  - name: Collect all web server IPs
    debug:
      msg: "{{ groups['webservers'] | map('extract', hostvars, 'ansible_host') | list }}"
```

#### `inventory_dir` and `inventory_file`

Path information about the inventory:

```yaml
tasks:
  - name: Show inventory location
    debug:
      msg: "Inventory is at: {{ inventory_dir }}"
```

#### `ansible_play_hosts`

List of all hosts in the current play:

```yaml
tasks:
  - name: Show all hosts in this play
    debug:
      msg: "Play hosts: {{ ansible_play_hosts }}"
```

#### `ansible_facts`

All facts gathered about the current host:

```yaml
tasks:
  - name: Show OS information
    debug:
      msg: "OS: {{ ansible_facts['distribution'] }} {{ ansible_facts['distribution_version'] }}"

  - name: Show memory
    debug:
      msg: "Total RAM: {{ ansible_facts['memtotal_mb'] }} MB"

  - name: Show all network interfaces
    debug:
      msg: "Interfaces: {{ ansible_facts['interfaces'] }}"
```

### Full List of Useful Magic Variables

|Variable|Description|
|---|---|
|`inventory_hostname`|Current host's inventory name|
|`inventory_hostname_short`|Short hostname (before first dot)|
|`ansible_host`|Actual connection hostname/IP|
|`groups`|Dictionary of all groups and their hosts|
|`group_names`|List of groups the current host belongs to|
|`hostvars`|Dictionary of all variables for all hosts|
|`ansible_play_hosts`|All active hosts in current play|
|`ansible_play_batch`|Hosts in current serial batch|
|`inventory_dir`|Directory of the inventory file|
|`inventory_file`|Path to the inventory file|
|`playbook_dir`|Directory of the current playbook|
|`role_name`|Name of the current role (if in a role)|
|`ansible_check_mode`|True if running in check mode|
|`ansible_diff_mode`|True if running in diff mode|
|`ansible_version`|Dictionary with Ansible version info|

---

## 🧪 Hands-on Lab: Variables

### Lab Objectives

- Define and use different types of variables
- Register task output as variables
- Understand and demonstrate variable precedence
- Work with magic variables

### Lab Duration: 45 minutes

---

### Exercise 1: Define and Use Variables

Create `playbook_vars.yaml` that:

- Defines string, number, boolean, list, and dictionary variables
- Uses each type in a meaningful task

**Solution:**

```yaml
---
- name: Variable Types Lab
  hosts: localhost
  connection: local
  gather_facts: false

  vars:
    # String
    app_name: "MyWebApp"
    app_version: "2.5.0"

    # Numbers
    http_port: 8080
    max_workers: 4

    # Boolean
    ssl_enabled: true
    debug_mode: false

    # List
    required_packages:
      - nginx
      - python3
      - git

    # Dictionary
    database:
      host: "db.internal"
      port: 5432
      name: "webapp_db"
      user: "appuser"

  tasks:
    - name: Display application info
      debug:
        msg: "Starting {{ app_name }} v{{ app_version }} on port {{ http_port }}"

    - name: Show SSL status
      debug:
        msg: "SSL is {{ 'enabled' if ssl_enabled else 'disabled' }}"

    - name: List all packages to install
      debug:
        msg: "Installing: {{ required_packages | join(', ') }}"

    - name: Show database connection string
      debug:
        msg: "postgresql://{{ database.user }}@{{ database.host }}:{{ database.port }}/{{ database.name }}"

    - name: Show max workers (computed)
      debug:
        msg: "Max connections = workers × 25 = {{ max_workers * 25 }}"
```

```bash
ansible-playbook playbook_vars.yaml
```

---

### Exercise 2: Register Variables

Create `register_lab.yaml` that checks system information and acts based on results:

**Solution:**

```yaml
---
- name: Register Variables Lab
  hosts: all
  gather_facts: true

  tasks:
    - name: Check current disk usage
      command: df -h /
      register: disk_output

    - name: Display raw output
      debug:
        var: disk_output.stdout

    - name: Get list of running services
      shell: systemctl list-units --type=service --state=running --no-pager | head -5
      register: running_services

    - name: Display running services
      debug:
        msg: "Running services:\n{{ running_services.stdout }}"

    - name: Check if nginx is installed
      command: which nginx
      register: nginx_check
      ignore_errors: true

    - name: Report nginx status
      debug:
        msg: "{{ 'Nginx is installed at: ' + nginx_check.stdout if nginx_check.rc == 0 else 'Nginx is NOT installed' }}"

    - name: Get uptime
      command: uptime -p
      register: system_uptime

    - name: Display uptime
      debug:
        msg: "System {{ inventory_hostname }} has been up {{ system_uptime.stdout }}"
```

---

### Exercise 3: Magic Variables

Create `magic_vars_lab.yaml` to explore magic variables:

**Solution:**

```yaml
---
- name: Magic Variables Lab
  hosts: all
  gather_facts: true

  tasks:
    - name: Show inventory hostname
      debug:
        msg: "Inventory name: {{ inventory_hostname }}"

    - name: Show all groups this host belongs to
      debug:
        msg: "{{ inventory_hostname }} is in groups: {{ group_names | join(', ') }}"

    - name: Show all web servers in inventory
      debug:
        msg: "All web servers: {{ groups.get('webservers', ['none defined']) }}"

    - name: Show OS distribution
      debug:
        msg: "OS: {{ ansible_distribution }} {{ ansible_distribution_version }}"

    - name: Show CPU information
      debug:
        msg: "CPUs: {{ ansible_processor_vcpus }}, Architecture: {{ ansible_architecture }}"

    - name: Show memory
      debug:
        msg: "RAM: {{ (ansible_memtotal_mb / 1024) | round(1) }} GB"

    - name: Show primary IP address
      debug:
        msg: "Primary IP: {{ ansible_default_ipv4.address }}"

    - name: Show all play hosts
      debug:
        msg: "All hosts in this play: {{ ansible_play_hosts }}"
      run_once: true
```

---

# Module 3 – Ansible Concepts

## Module Overview

The "Ansible Concepts" module provides participants with foundational knowledge of essential Ansible components. Participants learn about Ansible playbooks, modules, and how they work together to automate infrastructure tasks.

### Learning Objectives

- Gain proficiency in working with Ansible playbooks for orchestrating tasks
- Learn about Ansible modules and their role in executing tasks on managed nodes

---

## 3.1 Ansible Playbooks

### What is a Playbook?

A **playbook** is a YAML file containing one or more **plays**. Each play maps a set of **tasks** to a group of **hosts**. Playbooks are the primary way to automate complex, multi-step processes with Ansible.

```
Playbook (YAML file)
└── Play 1 (targets hosts group A)
│   ├── Task 1 (uses module X)
│   ├── Task 2 (uses module Y)
│   └── Task 3 (uses module Z)
└── Play 2 (targets hosts group B)
    ├── Task 1
    └── Task 2
```

### Playbook Structure

```yaml
---
# Playbook: site.yaml
# The --- marks the beginning of a YAML document

- name: Configure Web Servers        # Play name (human-readable)
  hosts: webservers                  # Target hosts or groups
  become: true                       # Escalate privileges (sudo)
  gather_facts: true                 # Collect host facts (default: true)
  serial: 2                          # Process 2 hosts at a time (rolling update)

  vars:                              # Play-level variables
    http_port: 80
    document_root: /var/www/html

  vars_files:                        # External variable files
    - vars/secrets.yaml

  pre_tasks:                         # Tasks that run BEFORE roles
    - name: Update apt cache
      apt:
        update_cache: true
        cache_valid_time: 3600

  roles:                             # Roles to apply
    - common
    - nginx

  tasks:                             # Main task list
    - name: Ensure nginx is running
      service:
        name: nginx
        state: started
        enabled: true

    - name: Deploy application config
      template:
        src: app.conf.j2
        dest: "{{ document_root }}/app.conf"
      notify: Restart Nginx          # Trigger handler if changed

  post_tasks:                        # Tasks that run AFTER roles
    - name: Verify nginx is responding
      uri:
        url: "http://{{ ansible_host }}"
        status_code: 200

  handlers:                          # Tasks triggered by 'notify'
    - name: Restart Nginx
      service:
        name: nginx
        state: restarted
```

### Handlers

Handlers are special tasks that only run when **notified** by another task. They run once at the end of a play, regardless of how many times they were notified.

```yaml
tasks:
  - name: Deploy nginx config
    template:
      src: nginx.conf.j2
      dest: /etc/nginx/nginx.conf
    notify:
      - Reload Nginx
      - Send Slack Notification

  - name: Deploy SSL certificate
    copy:
      src: ssl/server.crt
      dest: /etc/ssl/certs/server.crt
    notify: Reload Nginx             # Same handler - runs only once

handlers:
  - name: Reload Nginx
    service:
      name: nginx
      state: reloaded

  - name: Send Slack Notification
    uri:
      url: "{{ slack_webhook_url }}"
      method: POST
      body_format: json
      body:
        text: "Nginx was updated on {{ inventory_hostname }}"
```

### Running Playbooks

```bash
# Run a playbook
ansible-playbook site.yaml

# Run against a specific inventory
ansible-playbook -i inventory/production site.yaml

# Limit to specific hosts
ansible-playbook site.yaml --limit webservers

# Run in check mode (dry run - no changes made)
ansible-playbook site.yaml --check

# Run in diff mode (shows what would change)
ansible-playbook site.yaml --diff

# Run both check and diff
ansible-playbook site.yaml --check --diff

# Start from a specific task
ansible-playbook site.yaml --start-at-task "Deploy application config"

# Run only tasks with specific tags
ansible-playbook site.yaml --tags "nginx,config"

# Skip specific tags
ansible-playbook site.yaml --skip-tags "notifications"

# Override variables at command line
ansible-playbook site.yaml -e "http_port=8080 env=staging"

# Verbose output
ansible-playbook site.yaml -v      # basic verbose
ansible-playbook site.yaml -vvv    # very verbose (for debugging)

# Run playbook in parallel
ansible-playbook site.yaml --forks=20
```

### Task Control: tags, when, and ignore_errors

```yaml
tasks:
  - name: Install development tools
    apt:
      name: "{{ item }}"
      state: present
    loop:
      - vim
      - git
      - htop
    tags:
      - dev_tools
      - packages

  - name: Run only on Ubuntu
    apt:
      name: nginx
      state: present
    when: ansible_distribution == "Ubuntu"

  - name: Attempt to remove old service (may not exist)
    service:
      name: old-service
      state: stopped
    ignore_errors: true

  - name: Task with error handling
    block:
      - name: Risky task
        command: /opt/scripts/deploy.sh
    rescue:
      - name: Handle failure
        debug:
          msg: "Deployment failed, rolling back..."
    always:
      - name: Always send notification
        debug:
          msg: "Deployment attempt completed"
```

---

## 🧪 Hands-on Lab: Playbooks

### Lab Objectives

- Write a complete, multi-play Ansible playbook
- Use handlers, tags, and conditionals
- Run playbooks with various flags

### Lab Duration: 60 minutes

---

### Exercise 1: First Playbook – System Setup

Create `setup_webserver.yaml` that sets up a web server:

**Solution:**

```yaml
---
- name: Web Server Setup
  hosts: webservers
  become: true
  gather_facts: true

  vars:
    http_port: 80
    document_root: /var/www/html
    server_admin: admin@example.com

  pre_tasks:
    - name: Update package cache
      apt:
        update_cache: true
        cache_valid_time: 3600
      when: ansible_os_family == "Debian"

  tasks:
    - name: Install Nginx
      apt:
        name: nginx
        state: present
      tags: [nginx, packages]
      notify: Start Nginx

    - name: Create document root
      file:
        path: "{{ document_root }}"
        state: directory
        owner: www-data
        group: www-data
        mode: '0755'
      tags: [nginx, config]

    - name: Deploy index page
      copy:
        content: |
          <!DOCTYPE html>
          <html>
            <head><title>{{ inventory_hostname }}</title></head>
            <body>
              <h1>Welcome to {{ inventory_hostname }}</h1>
              <p>Server configured by Ansible</p>
            </body>
          </html>
        dest: "{{ document_root }}/index.html"
        owner: www-data
        group: www-data
        mode: '0644'
      tags: [nginx, content]

    - name: Configure firewall for HTTP
      ufw:
        rule: allow
        port: "{{ http_port }}"
        proto: tcp
      tags: [firewall]
      when: ansible_os_family == "Debian"

  post_tasks:
    - name: Verify web server is running
      uri:
        url: "http://{{ ansible_host }}"
        status_code: 200
      delegate_to: localhost
      become: false
      tags: [verify]

  handlers:
    - name: Start Nginx
      service:
        name: nginx
        state: started
        enabled: true

    - name: Reload Nginx
      service:
        name: nginx
        state: reloaded
```

```bash
# Test run (dry run)
ansible-playbook setup_webserver.yaml --check --diff

# Run only nginx-tagged tasks
ansible-playbook setup_webserver.yaml --tags nginx

# Run the full playbook
ansible-playbook setup_webserver.yaml
```

---

### Exercise 2: Multi-Play Playbook

Create `site.yaml` that configures both web and database servers:

**Solution:**

```yaml
---
# Play 1: Common setup for all servers
- name: Common Configuration
  hosts: all
  become: true

  tasks:
    - name: Set timezone to UTC
      timezone:
        name: UTC

    - name: Install common utilities
      apt:
        name:
          - curl
          - wget
          - vim
          - htop
          - net-tools
        state: present
        update_cache: true
      when: ansible_os_family == "Debian"

    - name: Create ansible management user
      user:
        name: ansible
        groups: sudo
        shell: /bin/bash
        create_home: true

# Play 2: Web server configuration
- name: Configure Web Servers
  hosts: webservers
  become: true

  vars:
    http_port: 80

  tasks:
    - name: Install and configure nginx
      apt:
        name: nginx
        state: present

    - name: Ensure nginx is running
      service:
        name: nginx
        state: started
        enabled: true

# Play 3: Database server configuration
- name: Configure Database Servers
  hosts: dbservers
  become: true

  tasks:
    - name: Install PostgreSQL
      apt:
        name:
          - postgresql
          - postgresql-contrib
          - python3-psycopg2
        state: present

    - name: Ensure PostgreSQL is running
      service:
        name: postgresql
        state: started
        enabled: true
```

---

## 3.2 Ansible Modules

### What is a Module?

A **module** is a discrete unit of work that Ansible executes on managed nodes. Modules are the building blocks of tasks. Ansible ships with **thousands of built-in modules** covering almost every common IT task.

```yaml
tasks:
  - name: Using the 'apt' module to install a package
    apt:              # ← This is the module name
      name: nginx     # ← These are module parameters
      state: present
```

### Module Categories

#### Package Management

```yaml
# Install packages (Ubuntu/Debian)
- name: Install nginx
  apt:
    name: nginx
    state: present   # present, absent, latest
    update_cache: true

# Install packages (RHEL/CentOS)
- name: Install nginx
  yum:
    name: nginx
    state: present

# Universal package manager (works cross-platform)
- name: Install nginx (cross-platform)
  package:
    name: nginx
    state: present

# Install Python packages
- name: Install Flask
  pip:
    name: flask
    version: "2.3.0"
    state: present
```

#### File Operations

```yaml
# Create/manage files and directories
- name: Create a directory
  file:
    path: /opt/myapp/logs
    state: directory
    owner: www-data
    group: www-data
    mode: '0755'
    recurse: true

# Copy a file to managed hosts
- name: Copy config file
  copy:
    src: files/nginx.conf
    dest: /etc/nginx/nginx.conf
    owner: root
    group: root
    mode: '0644'
    backup: true      # Back up existing file

# Render a Jinja2 template
- name: Deploy config from template
  template:
    src: templates/app.conf.j2
    dest: /etc/myapp/app.conf
    owner: root
    mode: '0640'

# Create a symbolic link
- name: Create symlink
  file:
    src: /opt/myapp/current
    dest: /opt/myapp/latest
    state: link

# Delete a file
- name: Remove old log file
  file:
    path: /tmp/old.log
    state: absent

# Modify a single line in a file
- name: Set max connections in config
  lineinfile:
    path: /etc/mysql/mysql.conf
    regexp: '^max_connections'
    line: 'max_connections = 500'
    backup: true

# Add a block of text to a file
- name: Add server block to nginx
  blockinfile:
    path: /etc/nginx/sites-enabled/default
    block: |
      location /api {
          proxy_pass http://localhost:3000;
      }
    marker: "# {mark} ANSIBLE MANAGED BLOCK"
```

#### Service Management

```yaml
# Manage system services
- name: Start and enable nginx
  service:
    name: nginx
    state: started    # started, stopped, restarted, reloaded
    enabled: true     # Enable at boot

# Manage systemd specifically
- name: Reload systemd daemon
  systemd:
    daemon_reload: true

- name: Start a user service
  systemd:
    name: myapp
    state: started
    enabled: true
    scope: user
```

#### User and Group Management

```yaml
# Manage users
- name: Create a user
  user:
    name: deploy
    uid: 1500
    group: www-data
    groups:
      - sudo
      - docker
    shell: /bin/bash
    home: /home/deploy
    create_home: true
    comment: "Deployment User"
    password: "{{ 'mysecret' | password_hash('sha512') }}"
    state: present

# Manage SSH authorized keys
- name: Add SSH key for deploy user
  authorized_key:
    user: deploy
    state: present
    key: "{{ lookup('file', '~/.ssh/id_rsa.pub') }}"

# Manage groups
- name: Create a group
  group:
    name: webteam
    gid: 2000
    state: present
```

#### Command and Shell Execution

```yaml
# Run a command (no shell features)
- name: Check Java version
  command: java -version
  register: java_version
  changed_when: false   # This command never changes state

# Run a shell command (supports pipes, redirects, etc.)
- name: Get disk usage
  shell: df -h | grep /dev/sda1 | awk '{print $5}'
  register: disk_usage

# Run a command only if file doesn't exist
- name: Initialize database
  command: /opt/app/init_db.sh
  args:
    creates: /var/lib/myapp/db_initialized   # Skip if this exists
```

#### Network and HTTP

```yaml
# Make HTTP requests
- name: Check if API is responding
  uri:
    url: https://api.example.com/health
    method: GET
    status_code: 200
    timeout: 30
  register: api_response

- name: POST data to API
  uri:
    url: https://api.example.com/register
    method: POST
    body_format: json
    body:
      hostname: "{{ inventory_hostname }}"
      ip: "{{ ansible_host }}"
    headers:
      Authorization: "Bearer {{ api_token }}"
    status_code: 201

# Download files
- name: Download application tarball
  get_url:
    url: "https://releases.example.com/app-{{ version }}.tar.gz"
    dest: /tmp/app.tar.gz
    checksum: "sha256:{{ app_checksum }}"
    mode: '0644'
```

#### Debug and Utility

```yaml
# Debug - print variables or messages
- name: Show a variable
  debug:
    var: my_variable

- name: Show a message
  debug:
    msg: "The value is {{ my_variable }}"

- name: Show multiple facts
  debug:
    msg:
      - "OS: {{ ansible_distribution }}"
      - "IP: {{ ansible_default_ipv4.address }}"

# Set facts during play
- name: Compute derived value
  set_fact:
    db_url: "postgresql://{{ db_user }}@{{ db_host }}/{{ db_name }}"

# Pause for a moment or for input
- name: Wait 30 seconds for service to start
  pause:
    seconds: 30

- name: Confirm before proceeding
  pause:
    prompt: "Ready to deploy to production? (Ctrl+C to abort)"

# Wait for a condition
- name: Wait for port 8080 to be open
  wait_for:
    host: "{{ ansible_host }}"
    port: 8080
    delay: 5
    timeout: 120
    state: started

# Gather facts
- name: Gather facts about target hosts
  setup:
    gather_subset:
      - network
      - hardware
```

### Using the `ansible-doc` Command

```bash
# Get documentation for any module
ansible-doc apt
ansible-doc service
ansible-doc template

# List all available modules
ansible-doc -l

# Search modules by keyword
ansible-doc -l | grep docker

# Get short description
ansible-doc -s apt
```

---

## 🧪 Hands-on Lab: Modules

### Lab Objectives

- Use a variety of Ansible modules in playbooks
- Understand module parameters and return values
- Combine multiple modules in a practical workflow

### Lab Duration: 60 minutes

---

### Exercise 1: File and Package Modules

Create `file_package_lab.yaml` that demonstrates file and package management:

**Solution:**

```yaml
---
- name: File and Package Modules Lab
  hosts: all
  become: true
  gather_facts: true

  vars:
    app_dir: /opt/weblab
    app_user: weblab
    packages:
      - nginx
      - curl
      - htop

  tasks:
    - name: Create application user
      user:
        name: "{{ app_user }}"
        shell: /bin/bash
        create_home: true
        state: present

    - name: Install required packages
      apt:
        name: "{{ packages }}"
        state: present
        update_cache: true
      when: ansible_os_family == "Debian"

    - name: Create application directory structure
      file:
        path: "{{ item }}"
        state: directory
        owner: "{{ app_user }}"
        group: "{{ app_user }}"
        mode: '0755'
      loop:
        - "{{ app_dir }}"
        - "{{ app_dir }}/logs"
        - "{{ app_dir }}/config"
        - "{{ app_dir }}/data"

    - name: Create application config file
      copy:
        content: |
          # Application Configuration
          # Generated by Ansible on {{ ansible_date_time.iso8601 }}
          APP_NAME=WebLab
          APP_PORT=8080
          LOG_DIR={{ app_dir }}/logs
          DATA_DIR={{ app_dir }}/data
        dest: "{{ app_dir }}/config/app.conf"
        owner: "{{ app_user }}"
        group: "{{ app_user }}"
        mode: '0640'

    - name: Check if app was initialized before
      stat:
        path: "{{ app_dir }}/.initialized"
      register: init_check

    - name: Initialize application (first time only)
      copy:
        content: "Initialized on {{ ansible_date_time.iso8601 }}"
        dest: "{{ app_dir }}/.initialized"
        owner: "{{ app_user }}"
        mode: '0644'
      when: not init_check.stat.exists

    - name: Get app directory info
      stat:
        path: "{{ app_dir }}"
      register: app_dir_stat

    - name: Report directory details
      debug:
        msg:
          - "App dir exists: {{ app_dir_stat.stat.exists }}"
          - "App dir size: {{ app_dir_stat.stat.size }} bytes"
          - "App dir owner: {{ app_dir_stat.stat.pw_name }}"
```

---

### Exercise 2: Service and Command Modules

Create `service_command_lab.yaml`:

**Solution:**

```yaml
---
- name: Service and Command Modules Lab
  hosts: all
  become: true
  gather_facts: true

  tasks:
    - name: Install nginx
      apt:
        name: nginx
        state: present
        update_cache: true

    - name: Ensure nginx is started and enabled
      service:
        name: nginx
        state: started
        enabled: true

    - name: Check nginx status via command
      command: systemctl is-active nginx
      register: nginx_status
      changed_when: false

    - name: Display nginx status
      debug:
        msg: "Nginx is: {{ nginx_status.stdout }}"

    - name: Get nginx version
      command: nginx -v
      register: nginx_version
      changed_when: false

    - name: Display nginx version
      debug:
        msg: "{{ nginx_version.stderr }}"   # nginx -v outputs to stderr

    - name: Check listening ports
      shell: ss -tlnp | grep nginx
      register: nginx_ports
      changed_when: false
      ignore_errors: true

    - name: Display listening ports
      debug:
        msg: "Nginx ports:\n{{ nginx_ports.stdout }}"
      when: nginx_ports.rc == 0

    - name: Test nginx configuration
      command: nginx -t
      register: nginx_test
      changed_when: false

    - name: Report config test result
      debug:
        msg: "Config test: {{ 'PASSED' if nginx_test.rc == 0 else 'FAILED' }}"

    - name: Wait for nginx to be accessible
      wait_for:
        host: "{{ ansible_default_ipv4.address }}"
        port: 80
        timeout: 30
        state: started

    - name: Verify HTTP response
      uri:
        url: "http://{{ ansible_default_ipv4.address }}"
        status_code: 200
        return_content: true
      register: http_response
      delegate_to: localhost
      become: false

    - name: Show HTTP response summary
      debug:
        msg: "HTTP {{ http_response.status }}: {{ http_response.content_length }} bytes received"
      delegate_to: localhost
      become: false
```

---

# Module 4 – Advanced Ansible Techniques

## Module Overview

The "Advanced Ansible Techniques" module focuses on advanced Ansible concepts for enhancing playbook flexibility and efficiency: conditionals, loops, and roles.

### Learning Objectives

- Understand how to use conditionals in Ansible playbooks to control task execution
- Gain proficiency in implementing loops to iterate over lists of items
- Learn about Ansible roles and their significance in organizing and reusing playbook logic

---

## 4.1 Ansible Conditionals

### The `when` Statement

The `when` statement allows tasks to run only when specific conditions are met. It uses **Jinja2 expressions** that evaluate to `true` or `false`.

```yaml
tasks:
  - name: Install on Debian
    apt:
      name: nginx
      state: present
    when: ansible_os_family == "Debian"

  - name: Install on RedHat
    yum:
      name: nginx
      state: present
    when: ansible_os_family == "RedHat"
```

### Conditional Operators

```yaml
tasks:
  # Equality check
  - name: Task for Ubuntu 22.04 only
    debug:
      msg: "Running on Ubuntu 22.04"
    when: ansible_distribution == "Ubuntu" and ansible_distribution_version == "22.04"

  # Not equal
  - name: Task for non-production
    debug:
      msg: "Not production!"
    when: env != "production"

  # Greater/less than
  - name: Task if memory > 4 GB
    debug:
      msg: "Enough memory available"
    when: ansible_memtotal_mb > 4096

  # 'in' operator - check if value is in a list
  - name: Task for specific distributions
    debug:
      msg: "Supported distribution"
    when: ansible_distribution in ["Ubuntu", "Debian", "CentOS"]

  # 'not in' operator
  - name: Task for non-test environments
    debug:
      msg: "Non-test environment"
    when: env not in ["test", "staging"]

  # Check if variable is defined
  - name: Use optional variable
    debug:
      msg: "Custom port: {{ custom_port }}"
    when: custom_port is defined

  # Check if variable is undefined
  - name: Use default when not defined
    set_fact:
      custom_port: 80
    when: custom_port is not defined

  # Check if variable is truthy/falsy
  - name: Task when flag is true
    debug:
      msg: "SSL is enabled"
    when: ssl_enabled

  # Check if a task succeeded/failed (using registered vars)
  - name: Check if file exists
    stat:
      path: /opt/myapp/config.yaml
    register: config_file

  - name: Create default config if missing
    copy:
      content: "# Default config\n"
      dest: /opt/myapp/config.yaml
    when: not config_file.stat.exists

  # Check return code
  - name: Run command that might fail
    command: service old-daemon status
    register: daemon_status
    ignore_errors: true

  - name: Start old daemon if stopped
    command: service old-daemon start
    when: daemon_status.rc != 0
```

### Multiple Conditions

```yaml
tasks:
  # AND - all conditions must be true (using 'and')
  - name: Install dev tools in dev environment on Ubuntu
    apt:
      name: vim
      state: present
    when:
      - env == "development"           # Condition 1
      - ansible_os_family == "Debian"  # Condition 2 (implicit AND)

  # OR - at least one condition must be true
  - name: Install on Ubuntu or Debian
    apt:
      name: nginx
      state: present
    when: ansible_distribution == "Ubuntu" or ansible_distribution == "Debian"

  # Complex combinations
  - name: Complex conditional
    debug:
      msg: "Complex condition met"
    when: >
      (env == "production" and ssl_enabled)
      or
      (env == "staging" and debug_mode is defined)
```

### Conditionals with Loops

```yaml
vars:
  users:
    - name: alice
      active: true
    - name: bob
      active: false
    - name: charlie
      active: true

tasks:
  - name: Create only active users
    user:
      name: "{{ item.name }}"
      state: present
    loop: "{{ users }}"
    when: item.active
```

### Conditionals Based on Facts

```yaml
tasks:
  - name: Configure memory settings based on available RAM
    lineinfile:
      path: /etc/myapp/app.conf
      regexp: '^MAX_MEMORY='
      line: "MAX_MEMORY={{ '4G' if ansible_memtotal_mb > 8192 else '2G' if ansible_memtotal_mb > 4096 else '1G' }}"

  - name: Use newer features only on supported OS versions
    command: /opt/app/enable-feature-x
    when:
      - ansible_distribution == "Ubuntu"
      - ansible_distribution_major_version | int >= 20

  - name: Skip virtual machines for certain tasks
    debug:
      msg: "Running on bare metal"
    when: ansible_virtualization_type == "NA"
```

---

## 🧪 Hands-on Lab: Conditionals

### Lab Objectives

- Use `when` statements to control task execution
- Combine multiple conditions with `and` and `or`
- Use registered variables in conditionals

### Lab Duration: 45 minutes

---

### Exercise 1: OS-Based Conditionals

Create `os_conditional_lab.yaml` that handles both Debian and RedHat families:

**Solution:**

```yaml
---
- name: OS-Based Conditionals Lab
  hosts: all
  become: true
  gather_facts: true

  vars:
    web_service: nginx
    config_dir: /etc/nginx

  tasks:
    - name: Display OS information
      debug:
        msg: "Running on {{ ansible_distribution }} {{ ansible_distribution_version }}"

    - name: Install nginx on Debian/Ubuntu
      apt:
        name: nginx
        state: present
        update_cache: true
      when: ansible_os_family == "Debian"

    - name: Install nginx on RHEL/CentOS
      yum:
        name: nginx
        state: present
      when: ansible_os_family == "RedHat"

    - name: Configure firewall on Ubuntu (using ufw)
      ufw:
        rule: allow
        port: "80"
        proto: tcp
      when:
        - ansible_distribution == "Ubuntu"
        - ansible_distribution_major_version | int >= 18

    - name: Configure firewall on CentOS (using firewalld)
      firewalld:
        service: http
        permanent: true
        state: enabled
      when: ansible_distribution == "CentOS"

    - name: Check if nginx config exists
      stat:
        path: "{{ config_dir }}/nginx.conf"
      register: nginx_conf_check

    - name: Report config file status
      debug:
        msg: "Nginx config {{ 'exists' if nginx_conf_check.stat.exists else 'does NOT exist' }}"

    - name: Run only if config file exists
      command: nginx -t
      when: nginx_conf_check.stat.exists
      register: config_test
      changed_when: false

    - name: Start nginx if config is valid
      service:
        name: nginx
        state: started
        enabled: true
      when:
        - nginx_conf_check.stat.exists
        - config_test.rc == 0
```

---

### Exercise 2: Environment-Based Conditionals

Create `env_conditional_lab.yaml` that behaves differently for dev/staging/production:

**Solution:**

```yaml
---
- name: Environment-Based Conditionals Lab
  hosts: all
  become: true
  gather_facts: true

  vars:
    environment: "{{ env | default('development') }}"

  tasks:
    - name: Display current environment
      debug:
        msg: "Deploying to: {{ environment }}"

    - name: Install debug tools (development only)
      apt:
        name:
          - gdb
          - strace
          - ltrace
        state: present
      when:
        - environment == "development"
        - ansible_os_family == "Debian"

    - name: Enable debug logging (non-production)
      lineinfile:
        path: /etc/myapp/app.conf
        regexp: '^LOG_LEVEL='
        line: 'LOG_LEVEL=DEBUG'
        create: true
      when: environment in ["development", "staging"]

    - name: Enable production logging
      lineinfile:
        path: /etc/myapp/app.conf
        regexp: '^LOG_LEVEL='
        line: 'LOG_LEVEL=WARNING'
        create: true
      when: environment == "production"

    - name: Set max connections based on environment
      set_fact:
        max_connections: "{{ 10 if environment == 'development' else 100 if environment == 'staging' else 1000 }}"

    - name: Display max connections
      debug:
        msg: "Max connections for {{ environment }}: {{ max_connections }}"

    - name: Require confirmation before production changes
      pause:
        prompt: "You are deploying to PRODUCTION. Press Enter to continue or Ctrl+C to abort"
      when:
        - environment == "production"
        - not ansible_check_mode
```

Run with different environments:

```bash
# Development (default)
ansible-playbook env_conditional_lab.yaml

# Staging
ansible-playbook env_conditional_lab.yaml -e "env=staging"

# Production (with confirmation)
ansible-playbook env_conditional_lab.yaml -e "env=production"
```

---

## 4.2 Ansible Loops

### The `loop` Keyword

Loops allow you to repeat a task for multiple items, eliminating the need to write the same task multiple times. The `loop` keyword is the modern way to iterate in Ansible.

```yaml
# Without loop (repetitive)
tasks:
  - name: Install nginx
    apt:
      name: nginx
      state: present

  - name: Install git
    apt:
      name: git
      state: present

  - name: Install curl
    apt:
      name: curl
      state: present

# With loop (clean and efficient)
tasks:
  - name: Install packages
    apt:
      name: "{{ item }}"
      state: present
    loop:
      - nginx
      - git
      - curl
```

### Loop with Simple Lists

```yaml
tasks:
  # Loop over strings
  - name: Create directories
    file:
      path: "/opt/myapp/{{ item }}"
      state: directory
      mode: '0755'
    loop:
      - logs
      - config
      - data
      - tmp

  # Loop over numbers
  - name: Create numbered files
    file:
      path: "/tmp/file{{ item }}.txt"
      state: touch
    loop:
      - 1
      - 2
      - 3
```

### Loop with Dictionaries

```yaml
tasks:
  - name: Create users with specific settings
    user:
      name: "{{ item.name }}"
      uid: "{{ item.uid }}"
      groups: "{{ item.groups }}"
      shell: "{{ item.shell | default('/bin/bash') }}"
    loop:
      - name: alice
        uid: 1001
        groups: sudo
      - name: bob
        uid: 1002
        groups: www-data
        shell: /bin/sh
      - name: charlie
        uid: 1003
        groups: docker

  - name: Configure multiple vhosts
    template:
      src: vhost.conf.j2
      dest: "/etc/nginx/sites-enabled/{{ item.name }}.conf"
    loop:
      - name: site1
        domain: site1.example.com
        port: 80
      - name: site2
        domain: site2.example.com
        port: 8080
    notify: Reload Nginx
```

### Loop Variables

Within a loop, special variables are available:

```yaml
tasks:
  - name: Loop with index
    debug:
      msg: "Item {{ ansible_loop.index }}/{{ ansible_loop.length }}: {{ item }}"
    loop:
      - apple
      - banana
      - cherry
    loop_control:
      index_var: my_index      # Create a custom index variable
      label: "{{ item }}"      # Control what's shown in output

  - name: Loop with 0-based index
    debug:
      msg: "Index {{ my_idx }}: {{ item }}"
    loop: [a, b, c]
    loop_control:
      index_var: my_idx
```

### Loop Filters and Transformations

```yaml
vars:
  servers:
    - web01
    - web02
    - db01

tasks:
  # Loop over a variable list
  - name: Ping all servers
    command: ping -c1 "{{ item }}"
    loop: "{{ servers }}"

  # Loop over range of numbers
  - name: Create numbered configs
    copy:
      content: "# Config {{ item }}"
      dest: "/etc/app/config{{ item }}.conf"
    loop: "{{ range(1, 6) | list }}"    # [1, 2, 3, 4, 5]

  # Loop with zip (multiple lists together)
  - name: Map names to IPs
    debug:
      msg: "{{ item.0 }} → {{ item.1 }}"
    with_together:
      - [web01, web02, db01]
      - [10.0.1.1, 10.0.1.2, 10.0.2.1]
```

### Nested Loops

```yaml
tasks:
  - name: Create user home directories with subdirectories
    file:
      path: "/home/{{ item.0 }}/{{ item.1 }}"
      state: directory
    with_nested:
      - [alice, bob]
      - [documents, downloads, projects]
```

### Loop with `register`

```yaml
tasks:
  - name: Check multiple services
    service_facts:

  - name: Check service status
    command: systemctl is-active "{{ item }}"
    register: service_results
    loop:
      - nginx
      - postgresql
      - redis
    ignore_errors: true

  - name: Report service statuses
    debug:
      msg: "{{ item.item }}: {{ item.stdout }}"
    loop: "{{ service_results.results }}"
```

### Loop Performance Tips

```yaml
# ✅ Better: Install multiple packages in one task
- name: Install packages (efficient)
  apt:
    name: "{{ packages }}"    # Pass a list directly to apt
    state: present
  vars:
    packages:
      - nginx
      - git
      - curl

# ⚠️ Less efficient: Loop calls apt once per package
- name: Install packages (less efficient)
  apt:
    name: "{{ item }}"
    state: present
  loop: [nginx, git, curl]
```

---

## 🧪 Hands-on Lab: Loops

### Lab Objectives

- Use loops to iterate over simple lists and dictionaries
- Work with loop control variables
- Combine loops with conditionals

### Lab Duration: 45 minutes

---

### Exercise 1: Basic Loops

Create `basic_loops_lab.yaml`:

**Solution:**

```yaml
---
- name: Basic Loops Lab
  hosts: localhost
  connection: local
  gather_facts: false

  vars:
    packages_to_install:
      - nginx
      - git
      - curl
      - htop

    directories:
      - /tmp/lab/logs
      - /tmp/lab/config
      - /tmp/lab/data
      - /tmp/lab/backup

    users:
      - name: webmaster
        role: admin
        active: true
      - name: developer
        role: dev
        active: true
      - name: testuser
        role: tester
        active: false

  tasks:
    - name: Show all packages that would be installed
      debug:
        msg: "Would install: {{ item }}"
      loop: "{{ packages_to_install }}"

    - name: Create lab directory structure
      file:
        path: "{{ item }}"
        state: directory
        mode: '0755'
      loop: "{{ directories }}"

    - name: Create config files for each directory
      copy:
        content: "# Config for {{ item | basename }}\ncreated_at: {{ ansible_date_time.iso8601 | default('unknown') }}\n"
        dest: "{{ item }}/settings.conf"
      loop: "{{ directories }}"

    - name: Display active users only
      debug:
        msg: "User {{ item.name }} ({{ item.role }}) is active"
      loop: "{{ users }}"
      when: item.active

    - name: Count items in loop
      debug:
        msg: "Processing {{ ansible_loop.index }} of {{ ansible_loop.length }}: {{ item }}"
      loop: "{{ packages_to_install }}"
      loop_control:
        label: "{{ item }}"
```

---

### Exercise 2: Loops with Dictionaries and Conditions

Create `dict_loops_lab.yaml`:

**Solution:**

```yaml
---
- name: Dictionary Loops Lab
  hosts: all
  become: true
  gather_facts: true

  vars:
    web_vhosts:
      - name: site-a
        domain: site-a.local
        port: 80
        enabled: true
        docroot: /var/www/site-a
      - name: site-b
        domain: site-b.local
        port: 8080
        enabled: true
        docroot: /var/www/site-b
      - name: site-c
        domain: site-c.local
        port: 80
        enabled: false
        docroot: /var/www/site-c

    system_users:
      - username: webmaster
        uid: 2001
        group: www-data
        authorized_key: "ssh-rsa AAAA..."
      - username: deploy
        uid: 2002
        group: deploy
        authorized_key: "ssh-rsa BBBB..."

  tasks:
    - name: Create document roots for enabled sites
      file:
        path: "{{ item.docroot }}"
        state: directory
        owner: www-data
        group: www-data
        mode: '0755'
      loop: "{{ web_vhosts }}"
      when: item.enabled

    - name: Deploy index page for each enabled site
      copy:
        content: |
          <!DOCTYPE html>
          <html>
            <body>
              <h1>{{ item.domain }}</h1>
              <p>Port: {{ item.port }}</p>
            </body>
          </html>
        dest: "{{ item.docroot }}/index.html"
        owner: www-data
        mode: '0644'
      loop: "{{ web_vhosts }}"
      when: item.enabled
      loop_control:
        label: "{{ item.name }}"

    - name: Create nginx config for each enabled site
      copy:
        content: |
          server {
              listen {{ item.port }};
              server_name {{ item.domain }};
              root {{ item.docroot }};
              index index.html;
          }
        dest: "/etc/nginx/sites-available/{{ item.name }}.conf"
      loop: "{{ web_vhosts }}"
      when: item.enabled
      notify: Reload Nginx

    - name: Report disabled sites
      debug:
        msg: "Site '{{ item.name }}' is disabled - skipping"
      loop: "{{ web_vhosts }}"
      when: not item.enabled

  handlers:
    - name: Reload Nginx
      service:
        name: nginx
        state: reloaded
```

---

## 4.3 Ansible Roles

### What is a Role?

A **role** is a structured way to organize and reuse Ansible automation. Roles break a playbook into a standardized directory structure, making complex automation manageable, shareable, and reusable.

Think of roles as **self-contained packages of automation** — like functions in programming.

### Why Use Roles?

- **Reusability**: Write once, use in many playbooks
- **Organization**: Clear structure makes large projects manageable
- **Shareability**: Share via Ansible Galaxy
- **Testability**: Roles can be tested independently
- **Separation of Concerns**: Each role handles one specific aspect (nginx, mysql, common, etc.)

### Role Directory Structure

```
roles/
└── nginx/                    # Role name
    ├── tasks/
    │   └── main.yaml         # Main task list (REQUIRED)
    ├── handlers/
    │   └── main.yaml         # Handlers triggered by tasks
    ├── templates/
    │   └── nginx.conf.j2     # Jinja2 templates
    ├── files/
    │   └── ssl/              # Static files to copy
    ├── vars/
    │   └── main.yaml         # Role variables (high precedence)
    ├── defaults/
    │   └── main.yaml         # Default variables (low precedence, overridable)
    ├── meta/
    │   └── main.yaml         # Role metadata, dependencies
    ├── library/
    │   └── my_module.py      # Custom modules
    └── README.md             # Documentation
```

### Creating a Role

```bash
# Use ansible-galaxy to create the skeleton
ansible-galaxy role init nginx

# This creates:
# nginx/
# ├── tasks/main.yml
# ├── handlers/main.yml
# ├── templates/
# ├── files/
# ├── vars/main.yml
# ├── defaults/main.yml
# ├── meta/main.yml
# └── README.md
```

### Building a Complete Role

Let's build a complete `nginx` role:

**`roles/nginx/defaults/main.yaml`** (overridable defaults):

```yaml
---
nginx_port: 80
nginx_user: www-data
nginx_document_root: /var/www/html
nginx_worker_processes: auto
nginx_worker_connections: 1024
nginx_server_name: "{{ inventory_hostname }}"
nginx_packages:
  - nginx
```

**`roles/nginx/vars/main.yaml`** (high-priority, non-overridable):

```yaml
---
nginx_config_dir: /etc/nginx
nginx_sites_dir: /etc/nginx/sites-enabled
nginx_log_dir: /var/log/nginx
```

**`roles/nginx/tasks/main.yaml`**:

```yaml
---
- name: Install nginx packages
  apt:
    name: "{{ nginx_packages }}"
    state: present
    update_cache: true
  when: ansible_os_family == "Debian"
  tags: [nginx, packages]

- name: Create document root
  file:
    path: "{{ nginx_document_root }}"
    state: directory
    owner: "{{ nginx_user }}"
    group: "{{ nginx_user }}"
    mode: '0755'
  tags: [nginx, config]

- name: Deploy nginx main config
  template:
    src: nginx.conf.j2
    dest: "{{ nginx_config_dir }}/nginx.conf"
    owner: root
    group: root
    mode: '0644'
    validate: 'nginx -t -c %s'
  notify: Reload Nginx
  tags: [nginx, config]

- name: Deploy default site config
  template:
    src: default-site.conf.j2
    dest: "{{ nginx_sites_dir }}/default"
    owner: root
    mode: '0644'
  notify: Reload Nginx
  tags: [nginx, config]

- name: Deploy default index page
  template:
    src: index.html.j2
    dest: "{{ nginx_document_root }}/index.html"
    owner: "{{ nginx_user }}"
    mode: '0644'
  tags: [nginx, content]

- name: Start and enable nginx
  service:
    name: nginx
    state: started
    enabled: true
  tags: [nginx, service]
```

**`roles/nginx/handlers/main.yaml`**:

```yaml
---
- name: Reload Nginx
  service:
    name: nginx
    state: reloaded

- name: Restart Nginx
  service:
    name: nginx
    state: restarted
```

**`roles/nginx/templates/nginx.conf.j2`**:

```nginx
# {{ ansible_managed }}
user {{ nginx_user }};
worker_processes {{ nginx_worker_processes }};
pid /run/nginx.pid;

events {
    worker_connections {{ nginx_worker_connections }};
}

http {
    sendfile on;
    tcp_nopush on;
    types_hash_max_size 2048;
    include /etc/nginx/mime.types;
    default_type application/octet-stream;
    access_log {{ nginx_log_dir }}/access.log;
    error_log {{ nginx_log_dir }}/error.log;
    gzip on;
    include /etc/nginx/conf.d/*.conf;
    include /etc/nginx/sites-enabled/*;
}
```

**`roles/nginx/templates/default-site.conf.j2`**:

```nginx
server {
    listen {{ nginx_port }} default_server;
    server_name {{ nginx_server_name }};
    root {{ nginx_document_root }};
    index index.html index.htm;

    location / {
        try_files $uri $uri/ =404;
    }
}
```

**`roles/nginx/templates/index.html.j2`**:

```html
<!DOCTYPE html>
<html>
<head>
    <title>{{ nginx_server_name }}</title>
</head>
<body>
    <h1>Welcome to {{ nginx_server_name }}</h1>
    <p>Managed by Ansible | Role: nginx</p>
    <p>OS: {{ ansible_distribution }} {{ ansible_distribution_version }}</p>
</body>
</html>
```

**`roles/nginx/meta/main.yaml`**:

```yaml
---
galaxy_info:
  author: your_name
  description: Install and configure Nginx
  license: MIT
  min_ansible_version: "2.12"
  platforms:
    - name: Ubuntu
      versions:
        - "20.04"
        - "22.04"
  galaxy_tags:
    - nginx
    - web
    - linux

dependencies:
  - role: common    # This role depends on the 'common' role
```

### Using Roles in Playbooks

```yaml
---
# site.yaml
- name: Configure Web Servers
  hosts: webservers
  become: true

  roles:
    # Simple role reference
    - common

    # Role with variable overrides
    - role: nginx
      vars:
        nginx_port: 8080
        nginx_server_name: "myapp.example.com"
        nginx_document_root: /opt/myapp/public

    # Another role
    - role: certbot
      when: ssl_enabled | bool

  tasks:
    # Tasks here run AFTER roles
    - name: Verify web server
      uri:
        url: "http://localhost"
        status_code: 200
```

### Role Search Paths

Ansible looks for roles in these locations (in order):

1. `./roles/` (relative to playbook)
2. `~/.ansible/roles`
3. `/etc/ansible/roles`
4. `/usr/share/ansible/roles`
5. Paths in `roles_path` in `ansible.cfg`

```ini
# ansible.cfg
[defaults]
roles_path = ./roles:~/.ansible/roles:/etc/ansible/roles
```

### Ansible Galaxy – Finding and Installing Roles

[Ansible Galaxy](https://galaxy.ansible.com/) is a public repository for sharing Ansible roles.

```bash
# Search for roles
ansible-galaxy search nginx

# Install a role
ansible-galaxy install geerlingguy.nginx

# Install a specific version
ansible-galaxy install geerlingguy.nginx,3.2.0

# Install from a requirements file
ansible-galaxy install -r requirements.yaml

# List installed roles
ansible-galaxy list

# Remove a role
ansible-galaxy remove geerlingguy.nginx
```

**`requirements.yaml`** (declaring role dependencies):

```yaml
---
roles:
  - name: geerlingguy.nginx
    version: "3.2.0"

  - name: geerlingguy.mysql
    version: "4.0.0"

  - src: https://github.com/custom/role.git
    scm: git
    version: main
    name: custom_role

collections:
  - name: community.general
    version: ">=5.0.0"

  - name: amazon.aws
    version: ">=3.0.0"
```

### Project Structure with Roles

A well-organized Ansible project using roles:

```
my-ansible-project/
├── ansible.cfg
├── inventory/
│   ├── production/
│   │   ├── hosts.yaml
│   │   ├── group_vars/
│   │   │   ├── all.yaml
│   │   │   ├── webservers.yaml
│   │   │   └── dbservers.yaml
│   │   └── host_vars/
│   └── staging/
│       ├── hosts.yaml
│       └── group_vars/
├── playbooks/
│   ├── site.yaml          # Master playbook
│   ├── webservers.yaml    # Web server playbook
│   └── dbservers.yaml     # Database server playbook
├── roles/
│   ├── common/            # Common base configuration
│   ├── nginx/             # Nginx web server role
│   ├── postgresql/        # PostgreSQL database role
│   └── myapp/             # Application deployment role
├── requirements.yaml      # External role/collection dependencies
└── README.md
```

### Role Best Practices

1. **One role, one purpose**: Each role should do one thing well
2. **Use defaults**: Put overridable variables in `defaults/main.yaml`
3. **Document with README**: Always include a README.md with usage examples
4. **Use tags**: Tag tasks so they can be selectively run
5. **Make roles idempotent**: Running a role multiple times should produce the same result
6. **Test your roles**: Use Molecule for role testing
7. **Handle multiple OS families**: Use conditionals to support different distributions

---

## 🧪 Hands-on Lab: Roles

### Lab Objectives

- Create a complete Ansible role from scratch
- Use the role in a playbook
- Override role default variables
- Install and use a role from Ansible Galaxy

### Lab Duration: 90 minutes

---

### Exercise 1: Build the `common` Role

This role will set up baseline configuration applied to all servers.

```bash
# Create the role structure
ansible-galaxy role init roles/common
```

**`roles/common/defaults/main.yaml`:**

```yaml
---
common_timezone: UTC
common_ntp_servers:
  - 0.pool.ntp.org
  - 1.pool.ntp.org
common_packages:
  - curl
  - wget
  - vim
  - htop
  - git
  - net-tools
  - unzip
common_sysctl_settings:
  - name: net.ipv4.ip_forward
    value: "0"
  - name: net.core.somaxconn
    value: "1024"
```

**`roles/common/tasks/main.yaml`:**

```yaml
---
- name: Install common packages
  apt:
    name: "{{ common_packages }}"
    state: present
    update_cache: true
  when: ansible_os_family == "Debian"
  tags: [common, packages]

- name: Set timezone
  timezone:
    name: "{{ common_timezone }}"
  tags: [common, timezone]

- name: Apply sysctl settings
  sysctl:
    name: "{{ item.name }}"
    value: "{{ item.value }}"
    state: present
    reload: true
  loop: "{{ common_sysctl_settings }}"
  tags: [common, sysctl]

- name: Ensure SSH service is running
  service:
    name: ssh
    state: started
    enabled: true
  when: ansible_os_family == "Debian"
  tags: [common, ssh]

- name: Configure vim as default editor
  alternatives:
    name: editor
    path: /usr/bin/vim.basic
  ignore_errors: true
  tags: [common, config]
```

**`roles/common/meta/main.yaml`:**

```yaml
---
galaxy_info:
  author: ansible_student
  description: Common baseline configuration for all servers
  license: MIT
  min_ansible_version: "2.12"
  platforms:
    - name: Ubuntu
      versions: ["20.04", "22.04"]

dependencies: []
```

---

### Exercise 2: Build the `webserver` Role

```bash
ansible-galaxy role init roles/webserver
```

**`roles/webserver/defaults/main.yaml`:**

```yaml
---
webserver_port: 80
webserver_user: www-data
webserver_document_root: /var/www/html
webserver_server_name: "{{ inventory_hostname }}"
webserver_index_content: |
  <html>
    <body>
      <h1>{{ webserver_server_name }}</h1>
      <p>Deployed by Ansible</p>
    </body>
  </html>
```

**`roles/webserver/tasks/main.yaml`:**

```yaml
---
- name: Install Nginx
  apt:
    name: nginx
    state: present
  tags: [webserver, packages]

- name: Create document root
  file:
    path: "{{ webserver_document_root }}"
    state: directory
    owner: "{{ webserver_user }}"
    group: "{{ webserver_user }}"
    mode: '0755'
  tags: [webserver, config]

- name: Deploy index page
  copy:
    content: "{{ webserver_index_content }}"
    dest: "{{ webserver_document_root }}/index.html"
    owner: "{{ webserver_user }}"
    mode: '0644'
  tags: [webserver, content]

- name: Configure nginx site
  template:
    src: site.conf.j2
    dest: /etc/nginx/sites-enabled/default
  notify: Restart Nginx
  tags: [webserver, config]

- name: Start and enable nginx
  service:
    name: nginx
    state: started
    enabled: true
  tags: [webserver, service]
```

**`roles/webserver/handlers/main.yaml`:**

```yaml
---
- name: Restart Nginx
  service:
    name: nginx
    state: restarted

- name: Reload Nginx
  service:
    name: nginx
    state: reloaded
```

**`roles/webserver/templates/site.conf.j2`:**

```nginx
# Ansible managed - do not edit manually
server {
    listen {{ webserver_port }};
    server_name {{ webserver_server_name }};
    root {{ webserver_document_root }};
    index index.html;

    access_log /var/log/nginx/{{ webserver_server_name }}-access.log;
    error_log /var/log/nginx/{{ webserver_server_name }}-error.log;

    location / {
        try_files $uri $uri/ =404;
    }
}
```

---

### Exercise 3: Use Roles in a Playbook

Create `site.yaml` that uses both roles:

**Solution:**

```yaml
---
# Apply common role to ALL servers
- name: Common Configuration
  hosts: all
  become: true

  roles:
    - role: common
      vars:
        common_timezone: America/New_York
        common_packages:
          - curl
          - wget
          - vim
          - git
          - htop
          - ntp

# Apply webserver role to web servers
- name: Web Server Configuration
  hosts: webservers
  become: true

  roles:
    - role: webserver
      vars:
        webserver_port: 80
        webserver_server_name: "{{ inventory_hostname }}.example.com"
        webserver_index_content: |
          <!DOCTYPE html>
          <html>
          <head><title>{{ inventory_hostname }}</title></head>
          <body>
            <h1>{{ inventory_hostname }}</h1>
            <p>Environment: {{ env | default('production') }}</p>
            <p>OS: {{ ansible_distribution }} {{ ansible_distribution_version }}</p>
          </body>
          </html>

  post_tasks:
    - name: Verify web server responds
      uri:
        url: "http://{{ ansible_host }}"
        status_code: 200
      delegate_to: localhost
      become: false
```

Run the complete site playbook:

```bash
# Syntax check
ansible-playbook site.yaml --syntax-check

# Dry run
ansible-playbook site.yaml --check --diff

# Run only common role tasks
ansible-playbook site.yaml --tags common

# Run only webserver tasks on specific hosts
ansible-playbook site.yaml --tags webserver --limit web01

# Full run
ansible-playbook site.yaml
```

---

### Exercise 4: Install a Community Role from Galaxy

```bash
# Create requirements.yaml
cat > requirements.yaml << 'EOF'
---
roles:
  - name: geerlingguy.security
    version: "2.2.0"
EOF

# Install the role
ansible-galaxy install -r requirements.yaml

# Use it in a playbook
cat > security_playbook.yaml << 'EOF'
---
- name: Security Hardening
  hosts: all
  become: true

  vars:
    security_ssh_password_authentication: "no"
    security_ssh_permit_root_login: "no"
    security_autoupdate_enabled: true
    security_fail2ban_enabled: true

  roles:
    - geerlingguy.security
EOF

# Run the playbook
ansible-playbook security_playbook.yaml --check
```

---

# Conclusion and Next Steps

## Course Summary

Congratulations on completing **Ansible for the Absolute Beginners**! Here is a summary of what you have learned:

**Module 1 – Introduction and Inventory**

- What Ansible is and how it works
- Setting up a local VirtualBox lab environment
- Installing Ansible on various platforms
- Writing valid YAML syntax
- Creating and managing inventory files in INI and YAML formats
- Building group hierarchies and parent-child relationships

**Module 2 – Variables**

- Defining variables (strings, numbers, booleans, lists, dictionaries)
- Registering task output as variables
- Understanding variable precedence (22 levels)
- Scoping variables at global, play, and host levels
- Using magic variables like `hostvars`, `groups`, `inventory_hostname`

**Module 3 – Concepts**

- Writing complete Ansible playbooks with multiple plays
- Using handlers, tags, and error handling
- Working with Ansible's module library (apt, yum, file, service, user, copy, template, uri, command, shell, debug)

**Module 4 – Advanced Techniques**

- Controlling task execution with `when` conditionals
- Using loops to iterate over lists and dictionaries
- Building and using Ansible roles
- Organizing projects with proper directory structures
- Using Ansible Galaxy for community roles

## Recommended Next Steps

1. **Practice daily**: Automate a real task in your environment with Ansible
2. **Learn Ansible Vault**: Encrypt sensitive variables like passwords and API keys
3. **Explore Molecule**: Test your roles in isolated environments
4. **Study AWX/Ansible Tower**: Enterprise Ansible with a web UI and RBAC
5. **Contribute to Galaxy**: Share your roles with the community
6. **Learn Collections**: The modern way to package and distribute Ansible content
7. **Study advanced topics**:
    - Ansible callbacks and plugins
    - Custom modules in Python
    - Dynamic inventory scripts
    - Delegation and local actions
    - Ansible with cloud providers (AWS, Azure, GCP)

## Quick Reference Card

```bash
# Essential Commands
ansible all -m ping                          # Connectivity test
ansible all -m setup                         # Gather facts
ansible-inventory --list                     # Show inventory
ansible-inventory --graph                    # Show inventory tree
ansible-playbook site.yaml                   # Run a playbook
ansible-playbook site.yaml --check           # Dry run
ansible-playbook site.yaml --diff            # Show changes
ansible-playbook site.yaml --limit web01     # Limit to host
ansible-playbook site.yaml --tags nginx      # Run tagged tasks
ansible-playbook site.yaml -e "env=prod"     # Extra vars
ansible-doc apt                              # Module documentation
ansible-galaxy role init myrole              # Create role skeleton
ansible-galaxy install -r requirements.yaml  # Install roles
ansible-vault encrypt secrets.yaml           # Encrypt a file
ansible-vault edit secrets.yaml              # Edit encrypted file
```

---

_This tutorial was created to provide a comprehensive introduction to Ansible for beginners. All examples are based on Ansible Core 2.12+ and have been tested on Ubuntu 22.04._