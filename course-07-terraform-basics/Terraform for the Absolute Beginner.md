# Terraform for the Absolute Beginner with Hands-on Labs

A comprehensive, hands-on tutorial covering Infrastructure as Code fundamentals, Terraform essentials, configuration management, state management, and advanced workflows.

---

## Table of Contents

1. [Module 1 – Introduction to Infrastructure as Code and Terraform Essentials](https://claude.ai/local_sessions/local_4e5327dd-b99f-4c21-b2ce-e233b861a37f#module-1--introduction-to-infrastructure-as-code-and-terraform-essentials)
2. [Module 2 – Introduction to Terraform Configuration](https://claude.ai/local_sessions/local_4e5327dd-b99f-4c21-b2ce-e233b861a37f#module-2--introduction-to-terraform-configuration)
3. [Module 3 – Understanding Terraform State Management](https://claude.ai/local_sessions/local_4e5327dd-b99f-4c21-b2ce-e233b861a37f#module-3--understanding-terraform-state-management)
4. [Module 4 – Working with Terraform](https://claude.ai/local_sessions/local_4e5327dd-b99f-4c21-b2ce-e233b861a37f#module-4--working-with-terraform)

---

## Course Overview

Welcome to **Terraform for the Absolute Beginner**! This course is designed for IT professionals, developers, and system administrators who want to learn how to manage infrastructure using code. By the end of this course, you will understand Infrastructure as Code principles, write Terraform configurations using HCL, manage providers, variables, state, and lifecycle rules, and confidently provision and destroy infrastructure resources.

**Prerequisites:** Basic familiarity with the command line and general understanding of cloud computing concepts. No prior Terraform or IaC experience is required.

**How to use this tutorial:** Each module contains conceptual explanations followed by hands-on labs. The labs use Terraform's `local` provider and file-based resources so you can practice without needing a cloud account. Where cloud-specific concepts are discussed, AWS examples are provided for illustration.

---

# Module 1 – Introduction to Infrastructure as Code and Terraform Essentials

This module introduces Infrastructure as Code (IaC) and explains how it addresses the limitations of traditional infrastructure management. You'll learn why Terraform is a widely used IaC tool, how it compares to other approaches, and when it's a good fit. You'll also set up your environment, write basic configurations in HashiCorp Configuration Language (HCL), and use core Terraform commands through hands-on labs.

### Learning Objectives

- Understand the principles and benefits of Infrastructure as Code (IaC) in modern IT environments.
- Identify the challenges associated with traditional IT infrastructure management and the need for automation.
- Explore the features and advantages of Terraform as an IaC tool.
- Install Terraform and set up the development environment effectively.
- Acquire proficiency in writing Terraform configurations using HashiCorp Configuration Language (HCL).
- Develop skills in managing infrastructure resources by updating and destroying them with Terraform commands.

---

## Introduction to Infrastructure as Code

### Course Introduction

Infrastructure as Code (IaC) is the practice of managing and provisioning computing infrastructure through machine-readable configuration files rather than through manual processes or interactive configuration tools. Instead of clicking through a cloud console or SSHing into servers to run commands, you write code that describes the desired state of your infrastructure, and a tool makes it so.

This approach brings the same rigor that software development applies to application code — version control, code review, testing, and automated deployment — to the infrastructure layer.

### Challenges with Traditional IT Infrastructure

Traditional infrastructure management relies on manual processes: administrators log into servers, click through cloud consoles, run ad-hoc scripts, and maintain handwritten runbooks. This approach creates several problems.

**Configuration drift** is one of the most insidious. When two servers that should be identical are configured manually, small differences inevitably creep in over time — a package updated here, a config file tweaked there. Eventually, the "identical" servers behave differently, and troubleshooting becomes a nightmare because nobody knows exactly what changed or when.

**Slow provisioning** is another major pain point. When a development team needs a new environment, they file a ticket, wait for an administrator to set it up, discover something is wrong, file another ticket, and wait again. What should take minutes takes days or weeks.

**Lack of reproducibility** means that rebuilding an environment after a disaster (or simply setting up a staging environment that matches production) becomes a heroic effort of archaeology — digging through logs, scripts, and tribal knowledge to reconstruct what exists.

**No audit trail** makes it difficult to answer fundamental questions: who changed what, when, and why? Manual changes leave no reliable record.

**Scaling challenges** compound all of these issues. Managing 5 servers manually is tedious but possible. Managing 500 or 5,000 the same way is simply untenable.

### Types of IaC Tools

IaC tools generally fall into three categories:

**Configuration Management Tools** — These tools manage the software and settings on existing servers. They install packages, manage services, edit configuration files, and enforce a desired state on machines that already exist. Examples include Ansible, Puppet, Chef, and SaltStack. They answer the question: "Given a server, how should it be configured?"

**Server Templating Tools** — These tools create pre-built images (templates) of servers with all software and configuration baked in. When you need a new server, you launch it from a template rather than configuring it from scratch. Examples include Docker (container images), Packer (machine images), and Vagrant (development environments). They answer the question: "What should a server look like from the start?"

**Infrastructure Provisioning Tools** — These tools create the infrastructure itself: virtual machines, networks, load balancers, databases, DNS entries, and everything else. Rather than configuring what runs on a server, they create (or destroy) the servers and the surrounding infrastructure. Examples include Terraform, AWS CloudFormation, Pulumi, and Google Cloud Deployment Manager. They answer the question: "What infrastructure should exist?"

Terraform falls firmly in the third category, though it can interact with configuration management and templating tools to provide end-to-end automation.

### Why Terraform?

Terraform has become one of the most popular IaC tools for several compelling reasons:

**Cloud-agnostic** — Terraform works with virtually every cloud provider (AWS, Azure, Google Cloud, Oracle Cloud, and many more) as well as on-premises solutions and SaaS platforms. A single tool and a single workflow can manage infrastructure across multiple providers.

**Declarative syntax** — You describe the desired end state ("I want 3 web servers behind a load balancer"), not the steps to get there ("create server 1, then create server 2, then create a load balancer, then attach them"). Terraform figures out the steps.

**Execution plans** — Before making any changes, Terraform shows you exactly what it plans to do. You can review the plan, catch mistakes, and approve before anything is modified. This is the `terraform plan` command, and it is one of Terraform's most valuable features.

**State management** — Terraform maintains a state file that maps your configuration to real-world resources. This allows it to determine what needs to change when you update your configuration and to detect drift from the desired state.

**Resource graph** — Terraform builds a dependency graph of all resources and creates or modifies them in the correct order, parallelizing where possible for speed.

**Open source and extensible** — Terraform's core is open source. Its provider ecosystem is vast and community-driven, meaning you can manage almost any service that has an API.

**HCL (HashiCorp Configuration Language)** — Terraform uses a purpose-built language that is human-readable, supports comments, and strikes a balance between the simplicity of JSON/YAML and the power of a full programming language.

### Putting IaC Concepts to Work

Let's contrast the traditional approach with IaC using a simple example.

**Traditional approach — provisioning a web server:**

1. Log into the cloud console.
2. Navigate to the compute section.
3. Click "Create Instance."
4. Select the operating system, instance size, network, and storage.
5. Click "Launch."
6. SSH into the server.
7. Run `apt update && apt install -y nginx`.
8. Edit the Nginx config file.
9. Start Nginx.
10. Hope you remember all these steps next time.

**IaC approach — the same task with Terraform:**

```hcl
# main.tf — Provision a web server
resource "aws_instance" "web_server" {
  ami           = "ami-0c55b159cbfafe1f0"
  instance_type = "t2.micro"

  user_data = <<-EOF
    #!/bin/bash
    apt update
    apt install -y nginx
    systemctl start nginx
  EOF

  tags = {
    Name = "WebServer"
  }
}
```

Run three commands:

```bash
terraform init      # Initialize the working directory
terraform plan      # Preview what will happen
terraform apply     # Create the infrastructure
```

The configuration is version-controlled, reviewable, repeatable, and self-documenting. Need 10 identical servers? Change one number. Need to tear it all down? Run `terraform destroy`.

---

## Introduction to Terraform Essentials

### Terraform Installation and Setup

#### Installing Terraform

**On macOS (using Homebrew):**

```bash
brew tap hashicorp/tap
brew install hashicorp/tap/terraform
```

**On Ubuntu/Debian Linux:**

```bash
sudo apt-get update && sudo apt-get install -y gnupg software-properties-common

# Add the HashiCorp GPG key
wget -O- https://apt.releases.hashicorp.com/gpg | \
  gpg --dearmor | \
  sudo tee /usr/share/keyrings/hashicorp-archive-keyring.gpg > /dev/null

# Add the official HashiCorp repository
echo "deb [signed-by=/usr/share/keyrings/hashicorp-archive-keyring.gpg] \
  https://apt.releases.hashicorp.com $(lsb_release -cs) main" | \
  sudo tee /etc/apt/sources.list.d/hashicorp.list

sudo apt-get update && sudo apt-get install terraform
```

**On Windows (using Chocolatey):**

```powershell
choco install terraform
```

**Manual installation (any platform):**

1. Visit [https://developer.hashicorp.com/terraform/downloads](https://developer.hashicorp.com/terraform/downloads).
2. Download the appropriate ZIP file for your operating system.
3. Extract the `terraform` binary.
4. Add it to your system's PATH.

#### Verifying the Installation

```bash
terraform version
```

You should see output like:

```
Terraform v1.9.x
on linux_amd64
```

#### Setting Up a Project Directory

Terraform operates on a directory of `.tf` files. Create a new directory for each project:

```bash
mkdir ~/terraform-labs
cd ~/terraform-labs
mkdir lab01-basics
cd lab01-basics
```

#### Recommended Editor

Use VS Code with the official HashiCorp Terraform extension for syntax highlighting, auto-completion, and formatting. Any text editor works, but the extension significantly improves the experience.

---

### Understanding HashiCorp Configuration Language (HCL)

HCL is the language Terraform uses for configuration files. It is designed to be both human-readable and machine-friendly.

#### HCL Basics — Blocks, Arguments, and Expressions

Every HCL configuration is built from **blocks**. A block has a type, zero or more labels, and a body enclosed in curly braces:

```hcl
block_type "label_1" "label_2" {
  argument_name = "argument_value"
}
```

The most important block types in Terraform are:

- `resource` — defines an infrastructure object to create
- `provider` — configures a provider plugin
- `variable` — declares an input variable
- `output` — declares an output value
- `data` — reads data from an external source
- `terraform` — configures Terraform behavior

#### Resource Blocks

The most common block type. A resource block declares a piece of infrastructure:

```hcl
resource "local_file" "hello" {
  filename = "/tmp/hello.txt"
  content  = "Hello, Terraform!"
}
```

Breaking this down:

- `resource` — the block type (we are declaring a resource)
- `"local_file"` — the resource type (from the `local` provider, creating a file)
- `"hello"` — the resource name (a local identifier you choose)
- `filename` and `content` — arguments (configuration for this resource)

The combination `local_file.hello` uniquely identifies this resource within your configuration.

#### Data Types in HCL

```hcl
# String
name = "terraform-lab"

# Number
count = 3

# Boolean
enabled = true

# List (ordered collection)
availability_zones = ["us-east-1a", "us-east-1b", "us-east-1c"]

# Map (key-value pairs)
tags = {
  Environment = "dev"
  Team        = "platform"
}

# Tuple (fixed-length, mixed-type list)
config = ["web", 8080, true]

# Object (structured type with named attributes)
server = {
  name  = "web-01"
  port  = 8080
  debug = false
}
```

#### Comments in HCL

```hcl
# This is a single-line comment

// This is also a single-line comment

/*
  This is a
  multi-line comment
*/
```

#### Strings and String Interpolation

```hcl
# Simple string
greeting = "Hello, World!"

# String interpolation
name = "Terraform"
message = "Welcome to ${name}!"

# Heredoc syntax for multi-line strings
user_data = <<-EOT
  #!/bin/bash
  echo "Hello from Terraform"
  apt update
  apt install -y nginx
EOT
```

---

### Update and Destroy Infrastructure

Terraform manages the full lifecycle of infrastructure: create, update, and destroy.

#### The Terraform Workflow

The core Terraform workflow consists of three stages:

**1. `terraform init`** — Initializes the working directory. Downloads provider plugins, sets up the backend, and prepares the directory for use. You run this once when starting a new configuration and again when you change providers or backend configuration.

```bash
terraform init
```

**2. `terraform plan`** — Creates an execution plan. Terraform reads your configuration, compares it to the current state, and shows what changes it would make. No actual changes are made.

```bash
terraform plan
```

The output uses symbols to indicate what will happen:

- `+` — resource will be **created**
- `-` — resource will be **destroyed**
- `~` — resource will be **updated in-place**
- `-/+` — resource will be **destroyed and recreated** (replaced)

**3. `terraform apply`** — Executes the plan. Terraform makes the changes to reach the desired state. It shows the plan first and asks for confirmation.

```bash
terraform apply
```

Type `yes` when prompted to confirm.

#### Updating Infrastructure

To update infrastructure, simply modify your `.tf` files and run `terraform apply` again. Terraform determines what changed and applies only the differences.

```hcl
# Before — original file
resource "local_file" "hello" {
  filename = "/tmp/hello.txt"
  content  = "Hello, Terraform!"
}
```

```hcl
# After — updated content
resource "local_file" "hello" {
  filename = "/tmp/hello.txt"
  content  = "Hello, Terraform! Updated content here."
}
```

```bash
terraform apply
```

Terraform detects the content change and updates (or recreates) the resource.

#### Destroying Infrastructure

To tear down everything managed by your configuration:

```bash
terraform destroy
```

This shows a plan of all resources to be destroyed and asks for confirmation. To destroy a specific resource:

```bash
terraform destroy -target=local_file.hello
```

#### The `terraform show` Command

View the current state of managed resources:

```bash
terraform show
```

#### The `terraform fmt` Command

Automatically format your configuration files to follow HCL style conventions:

```bash
terraform fmt
```

#### The `terraform validate` Command

Check your configuration for syntax errors and internal consistency:

```bash
terraform validate
```

---

### Hands-on Lab: HCL Basics

**Lab Goal:** Write your first Terraform configurations, run the core workflow, and practice creating, updating, and destroying resources using the `local` provider (no cloud account required).

---

**Exercise 1: Your First Terraform Configuration**

Create a project directory and your first configuration file.

```bash
mkdir -p ~/terraform-labs/lab01-hcl-basics
cd ~/terraform-labs/lab01-hcl-basics
```

Create a file called `main.tf`:

```hcl
# main.tf — Our first Terraform configuration

resource "local_file" "greeting" {
  filename = "${path.module}/greeting.txt"
  content  = "Hello, Terraform! This is my first resource."
}
```

Run the Terraform workflow:

```bash
# Step 1: Initialize the directory
terraform init
```

Expected output (abbreviated):

```
Initializing the backend...
Initializing provider plugins...
- Finding latest version of hashicorp/local...
- Installing hashicorp/local v2.5.1...
Terraform has been successfully initialized!
```

```bash
# Step 2: Preview the changes
terraform plan
```

Expected output (abbreviated):

```
Terraform will perform the following actions:

  # local_file.greeting will be created
  + resource "local_file" "greeting" {
      + content              = "Hello, Terraform! This is my first resource."
      + filename             = "./greeting.txt"
      + id                   = (known after apply)
      ...
    }

Plan: 1 to add, 0 to change, 0 to destroy.
```

```bash
# Step 3: Apply the configuration
terraform apply
```

Type `yes` when prompted. Verify the file was created:

```bash
cat greeting.txt
```

Output:

```
Hello, Terraform! This is my first resource.
```

---

**Exercise 2: Creating Multiple Resources**

Add more resources to `main.tf`:

```hcl
# main.tf — Multiple resources

resource "local_file" "greeting" {
  filename = "${path.module}/greeting.txt"
  content  = "Hello, Terraform! This is my first resource."
}

resource "local_file" "about" {
  filename = "${path.module}/about.txt"
  content  = "This file was created by Terraform.\nTerraform is an IaC tool by HashiCorp."
}

resource "local_file" "config" {
  filename = "${path.module}/config.json"
  content  = <<-EOT
    {
      "app_name": "terraform-lab",
      "version": "1.0.0",
      "debug": false
    }
  EOT
}
```

```bash
terraform apply
```

Terraform detects that `greeting.txt` already exists (no changes needed) and creates the two new files. Verify:

```bash
ls -la *.txt *.json
cat about.txt
cat config.json
```

---

**Exercise 3: Updating a Resource**

Modify the content of the `greeting` resource in `main.tf`:

```hcl
resource "local_file" "greeting" {
  filename = "${path.module}/greeting.txt"
  content  = "Hello, Terraform! This content has been updated."
}
```

```bash
terraform plan
```

Observe the output — Terraform shows that the `local_file.greeting` resource will be replaced (destroyed and recreated) because the `content` argument changed.

```bash
terraform apply
```

Type `yes`. Verify:

```bash
cat greeting.txt
```

Output:

```
Hello, Terraform! This content has been updated.
```

---

**Exercise 4: Destroying Specific Resources**

Destroy only the `config` resource:

```bash
terraform destroy -target=local_file.config
```

Verify `config.json` is gone but the other files remain:

```bash
ls *.txt *.json 2>/dev/null
```

---

**Exercise 5: Destroying All Resources**

Tear down everything:

```bash
terraform destroy
```

Type `yes`. All managed files are removed.

```bash
ls *.txt *.json 2>/dev/null
# No files remain
```

---

**Exercise 6: Formatting and Validation**

Create a file with intentionally poor formatting called `messy.tf`:

```hcl
resource "local_file" "messy" {
filename="${path.module}/messy.txt"
    content="This file has messy formatting."
}
```

Run the formatter:

```bash
terraform fmt
```

Output shows which files were modified:

```
messy.tf
```

View the corrected file — Terraform has aligned the `=` signs and fixed indentation:

```hcl
resource "local_file" "messy" {
  filename = "${path.module}/messy.txt"
  content  = "This file has messy formatting."
}
```

Validate the configuration:

```bash
terraform validate
```

Expected output:

```
Success! The configuration is valid.
```

Now introduce a deliberate error (reference a nonexistent variable):

```hcl
resource "local_file" "broken" {
  filename = "${path.module}/broken.txt"
  content  = var.undefined_variable
}
```

```bash
terraform validate
```

Expected output:

```
Error: Reference to undeclared input variable
...
```

Clean up by removing `messy.tf` and the broken resource before proceeding.

---

### Graded Assessment: Terraform Essentials

**Challenge 1:** Write a Terraform configuration that creates three files: `dev.txt`, `staging.txt`, and `prod.txt`. Each file should contain the name of the environment and a message like "This is the [environment] environment."

```hcl
resource "local_file" "dev" {
  filename = "${path.module}/dev.txt"
  content  = "This is the dev environment.\nAll debug logging is enabled."
}

resource "local_file" "staging" {
  filename = "${path.module}/staging.txt"
  content  = "This is the staging environment.\nMirrors production configuration."
}

resource "local_file" "prod" {
  filename = "${path.module}/prod.txt"
  content  = "This is the prod environment.\nHandle with care."
}
```

Run the full workflow:

```bash
terraform init
terraform plan
terraform apply
```

Verify all three files were created with the correct content.

**Challenge 2:** Modify the `dev.txt` content to include an additional line, then apply the change. Observe how Terraform handles the update. Afterwards, destroy only the `staging` file using a targeted destroy.

```bash
# After modifying the dev resource content:
terraform apply

# Destroy only staging:
terraform destroy -target=local_file.staging

# Verify dev.txt and prod.txt still exist:
terraform show
```

**Challenge 3:** Explain in your own words: What is the difference between `terraform plan` and `terraform apply`? Why is `terraform plan` valuable even though `terraform apply` also shows a plan before executing?

_Answer: `terraform plan` is a read-only operation that shows what changes Terraform would make without actually making them. It is valuable because it allows you to review changes safely, share the plan for code review or approval, and catch errors before they affect real infrastructure. `terraform apply` shows the same plan but then asks for confirmation to execute it. Separating plan from apply enables review workflows, CI/CD gates, and a safety net before any changes touch infrastructure._

---

# Module 2 – Introduction to Terraform Configuration

This module provides foundational knowledge and practical skills in working with Terraform configurations. You will learn how to use providers, organize configuration directories, work with input and output variables, define resource attributes and dependencies, and manage multiple providers.

### Learning Objectives

- Learn to utilize Terraform providers effectively for interacting with various cloud services and APIs.
- Understand the use of input variables and the variable block in Terraform configurations.
- Develop skills in managing resource attributes, dependencies, and output variables within Terraform configurations.

---

## Interacting with Terraform Providers

A **provider** is a plugin that Terraform uses to interact with a specific platform, service, or API. Providers are the bridge between your configuration and the real world.

### How Providers Work

When you declare a resource like `aws_instance` or `local_file`, the first part before the underscore (e.g., `aws`, `local`) identifies the provider. Terraform uses this to know which plugin to call.

Providers are downloaded during `terraform init` and cached in the `.terraform` directory.

### Declaring Providers

```hcl
# Explicit provider configuration
provider "aws" {
  region = "us-east-1"
}

# Provider with version constraint
terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 5.0"
    }
    local = {
      source  = "hashicorp/local"
      version = "~> 2.5"
    }
  }
}
```

### Provider Source Addresses

Every provider has a source address in the format `namespace/type`:

- `hashicorp/aws` — AWS provider by HashiCorp
- `hashicorp/local` — Local provider by HashiCorp
- `hashicorp/random` — Random provider for generating random values
- `hashicorp/tls` — TLS provider for generating certificates

### Common Providers

|Provider|Purpose|Example Resources|
|---|---|---|
|`hashicorp/local`|Local file operations|`local_file`, `local_sensitive_file`|
|`hashicorp/random`|Random value generation|`random_pet`, `random_integer`, `random_password`|
|`hashicorp/aws`|Amazon Web Services|`aws_instance`, `aws_s3_bucket`, `aws_vpc`|
|`hashicorp/azurerm`|Microsoft Azure|`azurerm_resource_group`, `azurerm_virtual_machine`|
|`hashicorp/google`|Google Cloud Platform|`google_compute_instance`, `google_storage_bucket`|
|`hashicorp/tls`|TLS certificates and keys|`tls_private_key`, `tls_self_signed_cert`|

### Provider Configuration Arguments

Each provider has its own set of configuration arguments. For example, the AWS provider needs a region and authentication credentials:

```hcl
provider "aws" {
  region     = "us-west-2"
  access_key = "YOUR_ACCESS_KEY"    # Not recommended — use env vars
  secret_key = "YOUR_SECRET_KEY"    # Not recommended — use env vars
}
```

Best practice is to use environment variables or shared credential files instead of hardcoding secrets:

```bash
export AWS_ACCESS_KEY_ID="YOUR_ACCESS_KEY"
export AWS_SECRET_ACCESS_KEY="YOUR_SECRET_KEY"
export AWS_DEFAULT_REGION="us-west-2"
```

---

### Hands-on Lab: Terraform Providers

**Lab Goal:** Practice working with multiple providers and understand how Terraform initializes and manages them.

---

**Exercise 1: Working with the Local Provider**

```bash
mkdir -p ~/terraform-labs/lab02-providers
cd ~/terraform-labs/lab02-providers
```

Create `main.tf`:

```hcl
terraform {
  required_providers {
    local = {
      source  = "hashicorp/local"
      version = "~> 2.5"
    }
  }
}

resource "local_file" "provider_demo" {
  filename = "${path.module}/provider-demo.txt"
  content  = "This file was created using the local provider."
}
```

```bash
terraform init
terraform apply -auto-approve
cat provider-demo.txt
```

Examine what `terraform init` created:

```bash
ls -la .terraform/providers/registry.terraform.io/hashicorp/local/
```

---

**Exercise 2: Using the Random Provider**

Update `main.tf` to also use the `random` provider:

```hcl
terraform {
  required_providers {
    local = {
      source  = "hashicorp/local"
      version = "~> 2.5"
    }
    random = {
      source  = "hashicorp/random"
      version = "~> 3.6"
    }
  }
}

resource "random_pet" "server_name" {
  length    = 3
  separator = "-"
}

resource "random_integer" "port" {
  min = 8000
  max = 9000
}

resource "local_file" "server_config" {
  filename = "${path.module}/server-config.txt"
  content  = <<-EOT
    Server Name: ${random_pet.server_name.id}
    Server Port: ${random_integer.port.result}
  EOT
}
```

```bash
terraform init      # Needed again because we added a new provider
terraform apply -auto-approve
cat server-config.txt
```

Each time you destroy and recreate, the random values will be different.

---

**Exercise 3: Examining Provider Plugins**

```bash
# List installed providers
terraform providers

# Show detailed provider requirements
terraform version
```

---

## Configuration Directory

A Terraform **configuration directory** is any directory containing `.tf` files. Terraform reads all `.tf` files in the directory and treats them as a single configuration. File names are conventional, not mandatory, but the community follows standard patterns.

### Recommended File Structure

```
my-project/
├── main.tf          # Primary resource definitions
├── variables.tf     # Input variable declarations
├── outputs.tf       # Output value declarations
├── providers.tf     # Provider configurations
├── terraform.tfvars # Variable values (not committed to version control if sensitive)
└── README.md        # Documentation
```

### How Terraform Reads Files

Terraform does not care about file names or the order of blocks within files. It reads all `.tf` files, builds a dependency graph, and processes them in the correct order.

This means these two approaches are equivalent:

**Single file approach:**

```hcl
# everything.tf
provider "local" {}

resource "local_file" "example" {
  filename = "${path.module}/example.txt"
  content  = "Hello"
}

output "file_path" {
  value = local_file.example.filename
}
```

**Multi-file approach:**

```hcl
# providers.tf
provider "local" {}
```

```hcl
# main.tf
resource "local_file" "example" {
  filename = "${path.module}/example.txt"
  content  = "Hello"
}
```

```hcl
# outputs.tf
output "file_path" {
  value = local_file.example.filename
}
```

The multi-file approach is preferred for anything beyond trivial configurations because it is easier to navigate and maintain.

---

## Managing Multiple Providers in Terraform

Terraform can use multiple providers in a single configuration — for example, managing AWS resources alongside local files, or even managing resources across multiple cloud providers.

### Multiple Provider Types

```hcl
terraform {
  required_providers {
    local = {
      source  = "hashicorp/local"
      version = "~> 2.5"
    }
    random = {
      source  = "hashicorp/random"
      version = "~> 3.6"
    }
    tls = {
      source  = "hashicorp/tls"
      version = "~> 4.0"
    }
  }
}
```

### Provider Aliases

When you need multiple instances of the same provider (e.g., two AWS regions), use aliases:

```hcl
provider "aws" {
  region = "us-east-1"
  alias  = "east"
}

provider "aws" {
  region = "us-west-2"
  alias  = "west"
}

resource "aws_instance" "east_server" {
  provider      = aws.east
  ami           = "ami-0c55b159cbfafe1f0"
  instance_type = "t2.micro"
}

resource "aws_instance" "west_server" {
  provider      = aws.west
  ami           = "ami-0a91cd140a1fc148a"
  instance_type = "t2.micro"
}
```

---

### Hands-on Lab: Multiple Providers

**Lab Goal:** Configure and use multiple providers in a single Terraform project.

---

**Exercise 1: Combining Local, Random, and TLS Providers**

```bash
mkdir -p ~/terraform-labs/lab03-multi-providers
cd ~/terraform-labs/lab03-multi-providers
```

Create `providers.tf`:

```hcl
terraform {
  required_providers {
    local = {
      source  = "hashicorp/local"
      version = "~> 2.5"
    }
    random = {
      source  = "hashicorp/random"
      version = "~> 3.6"
    }
    tls = {
      source  = "hashicorp/tls"
      version = "~> 4.0"
    }
  }
}
```

Create `main.tf`:

```hcl
# Generate a random project name
resource "random_pet" "project_name" {
  length = 2
}

# Generate a random password
resource "random_password" "db_password" {
  length  = 16
  special = true
}

# Generate a TLS private key
resource "tls_private_key" "ssh_key" {
  algorithm = "RSA"
  rsa_bits  = 4096
}

# Write the project configuration to a file
resource "local_file" "project_config" {
  filename = "${path.module}/project-config.txt"
  content  = <<-EOT
    Project Name: ${random_pet.project_name.id}
    Database Password Length: ${length(random_password.db_password.result)} characters
    SSH Key Algorithm: ${tls_private_key.ssh_key.algorithm}
    SSH Key Size: ${tls_private_key.ssh_key.rsa_bits} bits
  EOT
}

# Write the public key to a file
resource "local_file" "public_key" {
  filename = "${path.module}/ssh-key.pub"
  content  = tls_private_key.ssh_key.public_key_openssh
}
```

Create `outputs.tf`:

```hcl
output "project_name" {
  value = random_pet.project_name.id
}

output "public_key_file" {
  value = local_file.public_key.filename
}
```

```bash
terraform init
terraform apply -auto-approve

cat project-config.txt
cat ssh-key.pub
```

---

## Understanding Input Variables in Terraform

Input variables let you parameterize your configurations so that the same code can be reused with different values without modifying the `.tf` files.

### Declaring Variables

Variables are declared with `variable` blocks:

```hcl
variable "filename" {
  description = "The path of the file to create"
  type        = string
  default     = "default.txt"
}

variable "content" {
  description = "The content of the file"
  type        = string
}
```

### Using Variables

Reference variables with the `var.` prefix:

```hcl
resource "local_file" "example" {
  filename = "${path.module}/${var.filename}"
  content  = var.content
}
```

### Providing Variable Values

There are multiple ways to provide values for variables, in order of precedence (highest to lowest):

**1. Command-line flags:**

```bash
terraform apply -var="filename=hello.txt" -var="content=Hello!"
```

**2. Variable definition files (`.tfvars`):**

```hcl
# terraform.tfvars (automatically loaded)
filename = "hello.txt"
content  = "Hello from terraform.tfvars!"
```

```hcl
# dev.tfvars (manually specified)
filename = "dev-config.txt"
content  = "Development environment"
```

```bash
terraform apply -var-file="dev.tfvars"
```

**3. Environment variables:**

```bash
export TF_VAR_filename="hello.txt"
export TF_VAR_content="Hello from environment!"
terraform apply
```

**4. Default values** (defined in the variable block):

```hcl
variable "filename" {
  default = "default.txt"
}
```

**5. Interactive prompt** (if no value is provided and there's no default, Terraform asks):

```
var.content
  The content of the file

  Enter a value: _
```

---

### Understanding the Variable Block

The `variable` block supports several arguments:

```hcl
variable "instance_type" {
  description = "The EC2 instance type"      # Human-readable description
  type        = string                        # Type constraint
  default     = "t2.micro"                   # Default value (makes variable optional)
  sensitive   = false                        # Hide value from output if true

  validation {
    condition     = contains(["t2.micro", "t2.small", "t2.medium"], var.instance_type)
    error_message = "Instance type must be t2.micro, t2.small, or t2.medium."
  }
}
```

### Variable Types

```hcl
# String
variable "name" {
  type    = string
  default = "terraform-demo"
}

# Number
variable "port" {
  type    = number
  default = 8080
}

# Boolean
variable "enabled" {
  type    = bool
  default = true
}

# List of strings
variable "availability_zones" {
  type    = list(string)
  default = ["us-east-1a", "us-east-1b"]
}

# Map of strings
variable "tags" {
  type = map(string)
  default = {
    Environment = "dev"
    Team        = "platform"
  }
}

# Object (structured type)
variable "server_config" {
  type = object({
    name  = string
    port  = number
    debug = bool
  })
  default = {
    name  = "web-server"
    port  = 8080
    debug = false
  }
}

# Tuple (fixed-length, mixed types)
variable "example_tuple" {
  type    = tuple([string, number, bool])
  default = ["hello", 42, true]
}

# Set (unique, unordered strings)
variable "unique_names" {
  type    = set(string)
  default = ["alpha", "beta", "gamma"]
}
```

---

### Hands-on Lab: Variables

**Lab Goal:** Practice declaring and using different types of variables.

---

**Exercise 1: Basic String Variables**

```bash
mkdir -p ~/terraform-labs/lab04-variables
cd ~/terraform-labs/lab04-variables
```

Create `variables.tf`:

```hcl
variable "filename" {
  description = "Name of the file to create"
  type        = string
  default     = "default-output.txt"
}

variable "content" {
  description = "Content to write to the file"
  type        = string
  default     = "Default content from variable."
}

variable "file_permission" {
  description = "File permissions"
  type        = string
  default     = "0644"
}
```

Create `main.tf`:

```hcl
resource "local_file" "variable_demo" {
  filename        = "${path.module}/${var.filename}"
  content         = var.content
  file_permission = var.file_permission
}
```

```bash
terraform init

# Use default values
terraform apply -auto-approve
cat default-output.txt

# Override with command-line flags
terraform apply -auto-approve \
  -var="filename=custom.txt" \
  -var="content=Custom content via CLI!"

cat custom.txt
```

---

**Exercise 2: Using `.tfvars` Files**

Create `dev.tfvars`:

```hcl
filename = "dev-config.txt"
content  = "Development environment configuration.\nDebug mode: enabled."
```

Create `prod.tfvars`:

```hcl
filename = "prod-config.txt"
content  = "Production environment configuration.\nDebug mode: disabled."
```

```bash
# Apply with dev settings
terraform apply -auto-approve -var-file="dev.tfvars"
cat dev-config.txt

# Apply with prod settings
terraform apply -auto-approve -var-file="prod.tfvars"
cat prod-config.txt
```

---

**Exercise 3: Complex Variable Types**

Add to `variables.tf`:

```hcl
variable "project" {
  description = "Project configuration"
  type = object({
    name        = string
    environment = string
    version     = string
  })
  default = {
    name        = "terraform-lab"
    environment = "dev"
    version     = "1.0.0"
  }
}

variable "team_members" {
  description = "List of team members"
  type        = list(string)
  default     = ["Alice", "Bob", "Carol"]
}

variable "resource_tags" {
  description = "Tags to apply to resources"
  type        = map(string)
  default = {
    ManagedBy   = "Terraform"
    Environment = "lab"
  }
}
```

Add a new resource to `main.tf`:

```hcl
resource "local_file" "project_info" {
  filename = "${path.module}/project-info.txt"
  content  = <<-EOT
    Project: ${var.project.name}
    Environment: ${var.project.environment}
    Version: ${var.project.version}

    Team Members:
    %{for member in var.team_members~}
    - ${member}
    %{endfor~}

    Tags:
    %{for key, value in var.resource_tags~}
    ${key} = ${value}
    %{endfor~}
  EOT
}
```

```bash
terraform apply -auto-approve
cat project-info.txt
```

---

### Hands-on Lab: Using Variables in Terraform

**Lab Goal:** Practice variable precedence and validation.

---

**Exercise 1: Variable Precedence Demonstration**

Create `variables.tf`:

```hcl
variable "message" {
  description = "A greeting message"
  type        = string
  default     = "Hello from DEFAULT"
}
```

Create `main.tf`:

```hcl
resource "local_file" "message" {
  filename = "${path.module}/message.txt"
  content  = var.message
}

output "current_message" {
  value = var.message
}
```

Create `terraform.tfvars`:

```hcl
message = "Hello from TFVARS"
```

Test precedence:

```bash
terraform init

# Uses terraform.tfvars (overrides default)
terraform plan
# Shows: "Hello from TFVARS"

# CLI flag overrides terraform.tfvars
terraform plan -var='message=Hello from CLI'
# Shows: "Hello from CLI"

# Environment variable
export TF_VAR_message="Hello from ENV"
terraform plan
# Shows: "Hello from TFVARS" (tfvars overrides env)

# CLI still wins
terraform plan -var='message=Hello from CLI'
# Shows: "Hello from CLI"

unset TF_VAR_message
```

---

**Exercise 2: Variable Validation**

```hcl
variable "environment" {
  description = "Deployment environment"
  type        = string

  validation {
    condition     = contains(["dev", "staging", "prod"], var.environment)
    error_message = "Environment must be dev, staging, or prod."
  }
}

variable "port" {
  description = "Application port"
  type        = number

  validation {
    condition     = var.port >= 1024 && var.port <= 65535
    error_message = "Port must be between 1024 and 65535."
  }
}
```

```bash
# Valid values
terraform plan -var='environment=dev' -var='port=8080'

# Invalid environment
terraform plan -var='environment=test' -var='port=8080'
# Error: Environment must be dev, staging, or prod.

# Invalid port
terraform plan -var='environment=dev' -var='port=80'
# Error: Port must be between 1024 and 65535.
```

---

## Exploring Terraform Variables

### Local Values

**Locals** are named expressions that reduce repetition within a module:

```hcl
locals {
  project_name = "terraform-lab"
  environment  = "dev"
  common_tags = {
    Project     = local.project_name
    Environment = local.environment
    ManagedBy   = "Terraform"
  }
  full_name = "${local.project_name}-${local.environment}"
}

resource "local_file" "config" {
  filename = "${path.module}/${local.full_name}-config.txt"
  content  = "Project: ${local.project_name}\nEnvironment: ${local.environment}"
}
```

Reference locals with `local.` (singular, no `s`).

### Sensitive Variables

Mark variables as sensitive to prevent their values from appearing in logs and output:

```hcl
variable "db_password" {
  description = "Database password"
  type        = string
  sensitive   = true
}

output "password_status" {
  value     = "Password is ${length(var.db_password)} characters long"
  sensitive = false
}
```

---

### Hands-on Lab: Exploring Variables

**Exercise 1: Using Local Values**

```hcl
# locals.tf
locals {
  environments = {
    dev = {
      prefix  = "dev"
      debug   = "enabled"
      logging = "verbose"
    }
    prod = {
      prefix  = "prod"
      debug   = "disabled"
      logging = "error-only"
    }
  }
}
```

```hcl
# main.tf
variable "env" {
  type    = string
  default = "dev"
}

resource "local_file" "env_config" {
  filename = "${path.module}/${local.environments[var.env].prefix}-settings.txt"
  content  = <<-EOT
    Environment: ${var.env}
    Debug: ${local.environments[var.env].debug}
    Logging: ${local.environments[var.env].logging}
  EOT
}
```

```bash
terraform init
terraform apply -auto-approve
cat dev-settings.txt

terraform apply -auto-approve -var='env=prod'
cat prod-settings.txt
```

---

## Resource Attributes

Every resource in Terraform has **attributes** — properties that describe it. Some attributes are inputs you set (arguments), while others are computed by the provider after creation (read-only attributes).

### Referencing Resource Attributes

Use the syntax `resource_type.resource_name.attribute`:

```hcl
resource "local_file" "example" {
  filename = "${path.module}/example.txt"
  content  = "Hello, Terraform!"
}

# Reference attributes of the above resource
output "file_id" {
  value = local_file.example.id
}

output "file_path" {
  value = local_file.example.filename
}

output "content_md5" {
  value = local_file.example.content_md5
}
```

### Using Attributes Across Resources

One resource can reference attributes of another:

```hcl
resource "random_pet" "server" {
  length = 2
}

resource "local_file" "server_info" {
  filename = "${path.module}/${random_pet.server.id}.txt"
  content  = "Server name: ${random_pet.server.id}"
}
```

Here, `random_pet.server.id` is an attribute of the `random_pet.server` resource, and it is used in the `local_file.server_info` resource's arguments.

---

### Hands-on Lab: Resource Attributes

**Lab Goal:** Practice referencing resource attributes across resources.

---

**Exercise 1: Chain Resource Attributes**

```bash
mkdir -p ~/terraform-labs/lab05-attributes
cd ~/terraform-labs/lab05-attributes
```

Create `main.tf`:

```hcl
terraform {
  required_providers {
    local  = { source = "hashicorp/local" }
    random = { source = "hashicorp/random" }
  }
}

resource "random_pet" "project" {
  length    = 2
  separator = "-"
}

resource "random_integer" "id" {
  min = 1000
  max = 9999
}

resource "random_password" "secret" {
  length  = 24
  special = true
}

resource "local_file" "project_manifest" {
  filename = "${path.module}/manifest-${random_pet.project.id}.txt"
  content  = <<-EOT
    Project ID: ${random_pet.project.id}-${random_integer.id.result}
    Secret Key Length: ${length(random_password.secret.result)} characters
    Generated At: Terraform Apply
  EOT
}

output "project_id" {
  value = "${random_pet.project.id}-${random_integer.id.result}"
}

output "manifest_file" {
  value = local_file.project_manifest.filename
}

output "manifest_md5" {
  value = local_file.project_manifest.content_md5
}
```

```bash
terraform init
terraform apply -auto-approve
terraform output
```

---

## Resource Dependencies

Terraform automatically builds a **dependency graph** from attribute references. When resource B references an attribute of resource A, Terraform knows to create A first.

### Implicit Dependencies

Terraform detects these automatically when you reference one resource from another:

```hcl
resource "random_pet" "name" {
  length = 2
}

# Implicit dependency: this resource depends on random_pet.name
resource "local_file" "config" {
  filename = "${path.module}/config.txt"
  content  = "Server: ${random_pet.name.id}"
}
```

### Explicit Dependencies

Sometimes resources have dependencies that Terraform cannot detect from attribute references. Use `depends_on` for these:

```hcl
resource "local_file" "data" {
  filename = "${path.module}/data.txt"
  content  = "Important data"
}

resource "local_file" "backup" {
  filename   = "${path.module}/backup.txt"
  content    = "Backup created"
  depends_on = [local_file.data]    # Ensure data.txt is created first
}
```

### Viewing the Dependency Graph

```bash
terraform graph
```

This outputs a DOT-formatted graph. You can visualize it with Graphviz:

```bash
terraform graph | dot -Tpng > graph.png
```

---

### Hands-on Lab: Resource Dependencies

**Lab Goal:** Practice working with implicit and explicit dependencies.

---

**Exercise 1: Implicit Dependencies**

```bash
mkdir -p ~/terraform-labs/lab06-dependencies
cd ~/terraform-labs/lab06-dependencies
```

Create `main.tf`:

```hcl
terraform {
  required_providers {
    local  = { source = "hashicorp/local" }
    random = { source = "hashicorp/random" }
  }
}

# Step 1: Generate a random project name
resource "random_pet" "project" {
  length = 2
}

# Step 2: Generate a random password (implicitly depends on nothing)
resource "random_password" "db_pass" {
  length  = 16
  special = true
}

# Step 3: Create a config file (implicitly depends on both random resources)
resource "local_file" "db_config" {
  filename = "${path.module}/${random_pet.project.id}-db-config.txt"
  content  = <<-EOT
    Database Configuration
    =====================
    Project: ${random_pet.project.id}
    Password Length: ${length(random_password.db_pass.result)} chars
    Connection String: postgresql://admin:****@localhost:5432/${random_pet.project.id}
  EOT
}
```

```bash
terraform init
terraform apply -auto-approve

# View the dependency graph
terraform graph
```

---

**Exercise 2: Explicit Dependencies with `depends_on`**

Add to `main.tf`:

```hcl
# This resource has no attribute reference to db_config,
# but logically should be created after it.
resource "local_file" "deployment_log" {
  filename = "${path.module}/deployment-log.txt"
  content  = <<-EOT
    Deployment Log
    ==============
    Status: All configurations created successfully.
    Timestamp: Terraform Apply Complete
  EOT

  depends_on = [local_file.db_config]
}
```

```bash
terraform apply -auto-approve
terraform graph
```

Notice that `local_file.deployment_log` depends on `local_file.db_config` even though it doesn't reference any of its attributes.

---

## Output Variables

Output variables display information after `terraform apply` and make data available to other configurations or scripts.

### Declaring Outputs

```hcl
output "file_path" {
  description = "The path of the generated file"
  value       = local_file.example.filename
}

output "project_id" {
  description = "The generated project identifier"
  value       = random_pet.project.id
}

output "sensitive_data" {
  description = "A sensitive value"
  value       = random_password.secret.result
  sensitive   = true
}
```

### Viewing Outputs

```bash
# Show all outputs after apply
terraform output

# Show a specific output
terraform output project_id

# Show a sensitive output (revealed in plain text)
terraform output -raw sensitive_data

# JSON format (useful for scripting)
terraform output -json
```

---

### Hands-on Lab: Output Variables

**Lab Goal:** Practice defining and using output variables.

---

**Exercise 1: Comprehensive Outputs**

```bash
mkdir -p ~/terraform-labs/lab07-outputs
cd ~/terraform-labs/lab07-outputs
```

Create `main.tf`:

```hcl
terraform {
  required_providers {
    local    = { source = "hashicorp/local" }
    random   = { source = "hashicorp/random" }
  }
}

resource "random_pet" "app_name" {
  length = 2
}

resource "random_integer" "app_port" {
  min = 3000
  max = 9000
}

resource "random_password" "api_key" {
  length  = 32
  special = false
}

resource "local_file" "app_config" {
  filename = "${path.module}/app-config.json"
  content  = <<-EOT
    {
      "app_name": "${random_pet.app_name.id}",
      "port": ${random_integer.app_port.result},
      "api_key": "REDACTED"
    }
  EOT
}
```

Create `outputs.tf`:

```hcl
output "app_name" {
  description = "The generated application name"
  value       = random_pet.app_name.id
}

output "app_port" {
  description = "The assigned application port"
  value       = random_integer.app_port.result
}

output "api_key" {
  description = "The generated API key"
  value       = random_password.api_key.result
  sensitive   = true
}

output "config_file" {
  description = "Path to the generated config file"
  value       = local_file.app_config.filename
}

output "config_checksum" {
  description = "MD5 checksum of the config file"
  value       = local_file.app_config.content_md5
}

output "summary" {
  description = "Summary of all generated values"
  value       = "App '${random_pet.app_name.id}' running on port ${random_integer.app_port.result}"
}
```

```bash
terraform init
terraform apply -auto-approve

# View all outputs
terraform output

# View specific outputs
terraform output app_name
terraform output app_port

# View sensitive output
terraform output -raw api_key

# JSON output (for scripting)
terraform output -json
```

---

### Graded Assessment: Terraform Configuration

**Challenge 1:** Write a Terraform configuration that generates a random pet name, a random integer between 1 and 100, and creates a local file named `{pet_name}-{integer}.txt` containing a summary of the values. Define outputs for all generated values.

```hcl
terraform {
  required_providers {
    local  = { source = "hashicorp/local" }
    random = { source = "hashicorp/random" }
  }
}

resource "random_pet" "name" {
  length = 2
}

resource "random_integer" "number" {
  min = 1
  max = 100
}

resource "local_file" "summary" {
  filename = "${path.module}/${random_pet.name.id}-${random_integer.number.result}.txt"
  content  = <<-EOT
    Generated Resource Summary
    ==========================
    Pet Name: ${random_pet.name.id}
    Number:   ${random_integer.number.result}
    Filename: ${random_pet.name.id}-${random_integer.number.result}.txt
  EOT
}

output "pet_name" {
  value = random_pet.name.id
}

output "number" {
  value = random_integer.number.result
}

output "filename" {
  value = local_file.summary.filename
}
```

**Challenge 2:** Create a configuration with: a `variable` for environment (with validation to accept only "dev", "staging", "prod"), a `variable` for team name, `locals` that combine these into a naming prefix, and resources that use the prefix. Include `outputs` for all relevant information.

```hcl
variable "environment" {
  type = string
  validation {
    condition     = contains(["dev", "staging", "prod"], var.environment)
    error_message = "Must be dev, staging, or prod."
  }
}

variable "team_name" {
  type    = string
  default = "platform"
}

locals {
  prefix      = "${var.team_name}-${var.environment}"
  common_tags = "ManagedBy=Terraform, Environment=${var.environment}, Team=${var.team_name}"
}

resource "local_file" "config" {
  filename = "${path.module}/${local.prefix}-config.txt"
  content  = <<-EOT
    Environment: ${var.environment}
    Team:        ${var.team_name}
    Prefix:      ${local.prefix}
    Tags:        ${local.common_tags}
  EOT
}

output "prefix" {
  value = local.prefix
}

output "config_file" {
  value = local_file.config.filename
}
```

```bash
terraform init
terraform apply -var='environment=dev'
terraform apply -var='environment=prod' -var='team_name=backend'
```

---

# Module 3 – Understanding Terraform State Management

This module introduces the concept of Terraform state and its significance in managing infrastructure resources. You will learn about the purpose of state, explore its structure, and understand best practices for managing it effectively.

### Learning Objectives

- Explore the purpose of Terraform state and its role in tracking and managing resource states.
- Gain practical experience in working with Terraform state through hands-on labs.
- Learn about important considerations and best practices for managing Terraform state effectively.

---

## Introduction to Terraform State

When you run `terraform apply`, Terraform does not just create resources and forget about them. It records everything it created in a **state file** — by default, a JSON file named `terraform.tfstate` in your working directory.

The state file is Terraform's source of truth. It maps the resources defined in your configuration to the real-world objects that actually exist. Without state, Terraform would have no way to know what it has already created, what needs to change, and what should be destroyed.

### What the State File Contains

The state file (`terraform.tfstate`) is a JSON file that stores:

- The **version** of the state format.
- The **Terraform version** that last wrote to it.
- A list of every **resource** Terraform manages, including their type, name, provider, and all attribute values (including computed ones like IDs).
- A **serial number** that increments with each change (used for locking and detecting concurrent modifications).

Here is a simplified example:

```json
{
  "version": 4,
  "terraform_version": "1.9.0",
  "serial": 3,
  "resources": [
    {
      "type": "local_file",
      "name": "greeting",
      "provider": "provider[\"registry.terraform.io/hashicorp/local\"]",
      "instances": [
        {
          "attributes": {
            "content": "Hello, Terraform!",
            "filename": "./greeting.txt",
            "id": "a1b2c3d4..."
          }
        }
      ]
    }
  ]
}
```

---

## Purpose of State

Terraform state serves several critical purposes.

### 1. Mapping Configuration to Real Resources

Your configuration says: "I want a `local_file` called `greeting`." The state file records: "That `local_file.greeting` corresponds to the actual file at `/path/to/greeting.txt` with ID `abc123`."

Without this mapping, if you changed the content and ran `terraform apply`, Terraform wouldn't know that the file already exists — it might try to create a duplicate instead of updating the existing one.

### 2. Tracking Metadata

State stores metadata that Terraform needs for correct behavior, such as resource dependencies. While most dependencies are visible in the configuration, some only become clear at apply time. State preserves this information for future operations.

### 3. Performance Optimization

For large infrastructures, querying every cloud resource to determine current state would be extremely slow. Instead, Terraform reads from the cached state file and only queries the real infrastructure when refreshing state with `terraform refresh` (or during a `plan`/`apply`).

### 4. Syncing in a Team

When working in a team, the state file is the shared record of what currently exists. If Alice creates a VPC and Bob creates a subnet in it, both changes are recorded in the shared state. Without shared state, Bob wouldn't know the VPC exists.

### State Commands

```bash
# Show the current state in a human-readable format
terraform show

# List all resources in state
terraform state list

# Show detailed info about a specific resource
terraform state show local_file.greeting

# Move a resource to a different address (rename)
terraform state mv local_file.old_name local_file.new_name

# Remove a resource from state WITHOUT destroying it
terraform state rm local_file.example

# Pull remote state to a local file
terraform state pull > state.json

# Push a local state file to the remote backend
terraform state push state.json
```

---

### Hands-on Lab: Terraform State

**Lab Goal:** Explore the state file, understand its contents, and practice state management commands.

---

**Exercise 1: Examining the State File**

```bash
mkdir -p ~/terraform-labs/lab08-state
cd ~/terraform-labs/lab08-state
```

Create `main.tf`:

```hcl
terraform {
  required_providers {
    local  = { source = "hashicorp/local" }
    random = { source = "hashicorp/random" }
  }
}

resource "random_pet" "project" {
  length = 2
}

resource "local_file" "config" {
  filename = "${path.module}/config-${random_pet.project.id}.txt"
  content  = "Project: ${random_pet.project.id}\nStatus: Active"
}

resource "local_file" "readme" {
  filename = "${path.module}/README.txt"
  content  = "This project is managed by Terraform."
}
```

```bash
terraform init
terraform apply -auto-approve
```

Now examine the state:

```bash
# List all managed resources
terraform state list
```

Expected output:

```
local_file.config
local_file.readme
random_pet.project
```

```bash
# Show details of a specific resource
terraform state show random_pet.project
```

```bash
# Show details of the file resource
terraform state show local_file.config
```

```bash
# View the raw state file (it's JSON)
cat terraform.tfstate | python3 -m json.tool | head -50
```

---

**Exercise 2: Understanding State After Changes**

Modify the `readme` resource in `main.tf`:

```hcl
resource "local_file" "readme" {
  filename = "${path.module}/README.txt"
  content  = "This project is managed by Terraform.\nLast updated during state lab."
}
```

```bash
terraform plan
```

Observe that Terraform shows only the `readme` resource will change — it knows the exact current state and what needs to change.

```bash
terraform apply -auto-approve

# Check the backup state file
ls terraform.tfstate.backup

# Compare current and backup state
diff <(cat terraform.tfstate.backup | python3 -m json.tool) \
     <(cat terraform.tfstate | python3 -m json.tool) | head -30
```

---

**Exercise 3: Removing a Resource from State**

Sometimes you want Terraform to "forget" about a resource without destroying it. This is useful when migrating resources between configurations.

```bash
# The resource currently exists
terraform state list
cat README.txt

# Remove it from state (does NOT delete the file)
terraform state rm local_file.readme
```

```bash
# The resource is gone from state
terraform state list

# But the actual file still exists
cat README.txt
```

Now if you run `terraform plan`, Terraform will want to recreate the file because it is in the configuration but not in state:

```bash
terraform plan
```

Apply to bring state back in sync with configuration:

```bash
terraform apply -auto-approve
```

---

**Exercise 4: Using `terraform show` vs. `terraform state show`**

```bash
# terraform show — displays the entire state
terraform show

# terraform state show — displays a single resource
terraform state show local_file.config

# terraform state list — lists all resource addresses
terraform state list
```

---

## Terraform State Considerations

### Never Edit State Manually

The state file is a critical piece of infrastructure management. Editing it by hand is extremely risky — a single misplaced character can corrupt it and break your entire deployment. Always use `terraform state` commands to make changes.

### State Contains Sensitive Data

The state file may contain sensitive information in plain text: database passwords, API keys, private keys, and other secrets. This has important implications for how you store and share state.

### Remote State Backends

For team environments, store state in a remote backend instead of a local file. Remote backends provide locking (preventing concurrent modifications), encryption, versioning, and shared access.

Common remote backends:

- **Amazon S3** (with DynamoDB for locking)
- **Azure Blob Storage**
- **Google Cloud Storage**
- **HashiCorp Terraform Cloud / HCP Terraform**
- **Consul**

Example S3 backend configuration:

```hcl
terraform {
  backend "s3" {
    bucket         = "my-terraform-state"
    key            = "project/terraform.tfstate"
    region         = "us-east-1"
    dynamodb_table = "terraform-locks"
    encrypt        = true
  }
}
```

### State Locking

When using a remote backend that supports locking, Terraform acquires a lock before any operation that could write to state (`plan`, `apply`, `destroy`). This prevents two team members from making conflicting changes simultaneously.

If a lock is stuck (for example, after a crash), you can force-unlock it:

```bash
terraform force-unlock LOCK_ID
```

Use this with extreme caution — only when you are certain no other operation is running.

### State File Best Practices

1. **Use remote state** for any team or production work.
2. **Enable encryption** for state at rest.
3. **Enable versioning** on your state storage (S3 versioning, GCS versioning) so you can recover from corruption.
4. **Never commit `terraform.tfstate` to version control.** Add it to `.gitignore`.
5. **Use state locking** to prevent concurrent modifications.
6. **Limit access** to the state backend to authorized users only.

Example `.gitignore` for Terraform projects:

```
# Terraform state
*.tfstate
*.tfstate.backup
*.tfstate.lock.info

# Terraform plugins (downloaded during init)
.terraform/

# Sensitive variable files
*.tfvars
!example.tfvars

# OS files
.DS_Store
```

---

### Graded Assessment: Terraform State Management

**Challenge 1:** Answer the following questions:

1. What is the default filename for Terraform state? What format is it in?
    
    _Answer: `terraform.tfstate`, stored in JSON format in the current working directory._
    
2. What happens if you delete the state file and run `terraform apply`?
    
    _Answer: Terraform has no record of existing resources, so it attempts to create everything from scratch. This will either fail (if the resources already exist and conflict) or create duplicates. This is why state is critical and should be backed up._
    
3. Why should you never manually edit the state file?
    
    _Answer: The state file has a specific structure, serial numbers, and computed checksums. Manual edits can corrupt the file, cause Terraform to lose track of resources, or create inconsistencies between what Terraform believes exists and what actually exists. Use `terraform state` commands instead._
    
4. What is the purpose of state locking and which backends support it?
    
    _Answer: State locking prevents two users from running Terraform operations simultaneously, which could corrupt state. Backends that support locking include S3 (with DynamoDB), Azure Blob Storage, Google Cloud Storage, Terraform Cloud, and Consul._
    

**Challenge 2:** Create a Terraform configuration with three resources. Apply it, then practice the following state operations:

```bash
# Setup
mkdir -p ~/terraform-labs/lab-state-assessment
cd ~/terraform-labs/lab-state-assessment
```

```hcl
# main.tf
terraform {
  required_providers {
    local  = { source = "hashicorp/local" }
    random = { source = "hashicorp/random" }
  }
}

resource "random_pet" "app" {
  length = 2
}

resource "local_file" "config" {
  filename = "${path.module}/config.txt"
  content  = "App: ${random_pet.app.id}"
}

resource "local_file" "notes" {
  filename = "${path.module}/notes.txt"
  content  = "Deployment notes for ${random_pet.app.id}"
}
```

```bash
terraform init
terraform apply -auto-approve

# 1. List all resources in state
terraform state list

# 2. Show details of the config file resource
terraform state show local_file.config

# 3. Remove notes from state (without destroying the file)
terraform state rm local_file.notes

# 4. Verify it's gone from state but still on disk
terraform state list
cat notes.txt

# 5. Run plan to see what Terraform wants to do
terraform plan
# Terraform will want to recreate the notes file

# 6. Apply to bring state back in sync
terraform apply -auto-approve

# 7. Clean up
terraform destroy -auto-approve
```

---

# Module 4 – Working with Terraform

This module provides comprehensive knowledge and practical skills for effectively working with Terraform. You will master essential commands, understand mutable vs. immutable infrastructure, learn lifecycle rules, use data sources, explore meta-arguments, and work with version constraints.

### Learning Objectives

- Master essential Terraform commands for managing IaC resources.
- Understand the differences between mutable and immutable infrastructure.
- Learn about Terraform lifecycle rules and how to manage resource lifecycle effectively.
- Gain proficiency in using Terraform data sources to retrieve external information.
- Explore meta-arguments including `count` and `for_each` for dynamic resource creation.
- Understand version constraints and how to specify them in Terraform configurations.

---

## Terraform Commands

Here is a comprehensive reference for the most important Terraform commands.

### Core Workflow Commands

|Command|Purpose|
|---|---|
|`terraform init`|Initialize working directory, download providers|
|`terraform plan`|Preview changes without applying them|
|`terraform apply`|Apply changes to reach desired state|
|`terraform destroy`|Destroy all managed infrastructure|

### Inspection Commands

|Command|Purpose|
|---|---|
|`terraform show`|Show current state or a saved plan|
|`terraform state list`|List resources in state|
|`terraform state show <addr>`|Show a specific resource in state|
|`terraform output`|Show output values|
|`terraform graph`|Generate a dependency graph (DOT format)|
|`terraform providers`|Show providers required by configuration|

### Utility Commands

|Command|Purpose|
|---|---|
|`terraform fmt`|Format configuration files|
|`terraform validate`|Validate configuration syntax and consistency|
|`terraform console`|Interactive console for testing expressions|
|`terraform version`|Show Terraform version|
|`terraform workspace`|Manage workspaces|

### Advanced Commands

|Command|Purpose|
|---|---|
|`terraform import`|Import existing infrastructure into state|
|`terraform taint`|Mark a resource for recreation (deprecated — use `-replace`)|
|`terraform untaint`|Remove taint mark from a resource|
|`terraform refresh`|Update state to match real infrastructure|
|`terraform plan -replace=<addr>`|Plan with a specific resource marked for replacement|

### The `terraform console`

An interactive environment for testing HCL expressions:

```bash
terraform console
```

```
> 1 + 2
3
> "hello ${"world"}"
"hello world"
> max(5, 12, 9)
12
> length(["a", "b", "c"])
3
> upper("terraform")
"TERRAFORM"
> exit
```

### Common Flags

```bash
# Auto-approve (skip confirmation prompt)
terraform apply -auto-approve
terraform destroy -auto-approve

# Target a specific resource
terraform apply -target=local_file.config
terraform destroy -target=local_file.config

# Pass variable values
terraform apply -var="name=value"
terraform apply -var-file="custom.tfvars"

# Save a plan to a file
terraform plan -out=myplan.tfplan
terraform apply myplan.tfplan

# Refresh-only mode (update state without changing infrastructure)
terraform apply -refresh-only
```

---

### Hands-on Lab: Terraform Commands

**Lab Goal:** Practice using essential Terraform commands.

---

**Exercise 1: Exploring Commands**

```bash
mkdir -p ~/terraform-labs/lab09-commands
cd ~/terraform-labs/lab09-commands
```

Create `main.tf`:

```hcl
terraform {
  required_providers {
    local  = { source = "hashicorp/local" }
    random = { source = "hashicorp/random" }
  }
}

variable "prefix" {
  type    = string
  default = "lab"
}

resource "random_pet" "name" {
  prefix = var.prefix
  length = 2
}

resource "local_file" "output" {
  filename = "${path.module}/output.txt"
  content  = "Generated name: ${random_pet.name.id}"
}

output "name" {
  value = random_pet.name.id
}

output "file" {
  value = local_file.output.filename
}
```

```bash
# Initialize
terraform init

# Validate
terraform validate

# Format
terraform fmt

# Plan and save
terraform plan -out=lab.tfplan

# Apply from saved plan (no confirmation needed)
terraform apply lab.tfplan

# Inspect
terraform show
terraform state list
terraform output
terraform output -json

# Use the console
echo 'upper("terraform is fun")' | terraform console
echo 'length(["a", "b", "c", "d"])' | terraform console

# View the providers
terraform providers

# Generate a graph
terraform graph

# Destroy
terraform destroy -auto-approve
```

---

**Exercise 2: Targeted Operations**

Create `main.tf` with multiple resources:

```hcl
terraform {
  required_providers {
    local = { source = "hashicorp/local" }
  }
}

resource "local_file" "alpha" {
  filename = "${path.module}/alpha.txt"
  content  = "Alpha resource"
}

resource "local_file" "beta" {
  filename = "${path.module}/beta.txt"
  content  = "Beta resource"
}

resource "local_file" "gamma" {
  filename = "${path.module}/gamma.txt"
  content  = "Gamma resource"
}
```

```bash
terraform init

# Apply only alpha
terraform apply -target=local_file.alpha -auto-approve
terraform state list
# Only local_file.alpha exists in state

# Apply everything
terraform apply -auto-approve
terraform state list
# All three resources exist

# Destroy only beta
terraform destroy -target=local_file.beta -auto-approve
terraform state list
# alpha and gamma remain

# Clean up
terraform destroy -auto-approve
```

---

## Mutable vs Immutable Infrastructure

### Mutable Infrastructure

In the mutable model, you update existing servers in place. When you need a new software version, you SSH into the server and upgrade it. The server's identity persists, but its configuration changes over time.

Problems with this approach include configuration drift (each update might leave the server in a slightly different state), snowflake servers (servers that have been updated so many times they are unique and irreproducible), and difficult rollbacks (undoing an update is harder than rolling forward).

### Immutable Infrastructure

In the immutable model, you never modify existing infrastructure. Instead, you create new infrastructure with the desired configuration and destroy the old one. Need to upgrade? Build a new server with the new version, route traffic to it, and terminate the old server.

Benefits include reproducibility (every server is created from the same template), no configuration drift (servers are never modified), easy rollbacks (just route traffic back to the old server), and consistency (every server of a given version is identical).

### How Terraform Handles This

When you change a resource's configuration, Terraform decides whether to:

- **Update in-place** (`~`): The provider can modify the existing resource without replacing it (e.g., changing a tag on an AWS instance).
- **Replace** (`-/+`): The change requires destroying the old resource and creating a new one (e.g., changing the AMI of an AWS instance).

This decision is made by the provider, not by you. Some attributes support in-place updates; others force replacement. Terraform's plan output always shows you which approach will be used.

---

## Lifecycle Rules

Terraform provides lifecycle meta-arguments that let you customize how resources are created, updated, and destroyed.

### `create_before_destroy`

By default, when Terraform must replace a resource, it destroys the old one first, then creates the new one. This can cause downtime. With `create_before_destroy`, the new resource is created first:

```hcl
resource "local_file" "config" {
  filename = "${path.module}/config.txt"
  content  = "version 2"

  lifecycle {
    create_before_destroy = true
  }
}
```

### `prevent_destroy`

Prevents Terraform from destroying a resource. This is a safety net for critical resources like databases:

```hcl
resource "local_file" "critical_data" {
  filename = "${path.module}/critical.txt"
  content  = "Do not delete this!"

  lifecycle {
    prevent_destroy = true
  }
}
```

If you try to destroy this resource, Terraform will error:

```
Error: Instance cannot be destroyed
```

To actually destroy it, you must first remove the `prevent_destroy` rule from the configuration.

### `ignore_changes`

Tells Terraform to ignore changes to specific attributes, even if they differ between the configuration and the real resource:

```hcl
resource "local_file" "managed" {
  filename = "${path.module}/managed.txt"
  content  = "Initial content"

  lifecycle {
    ignore_changes = [content]    # Terraform won't update if content changes externally
  }
}
```

You can also use `ignore_changes = all` to ignore all attribute changes.

### `replace_triggered_by`

Forces a resource to be replaced when another resource changes:

```hcl
resource "random_pet" "trigger" {
  length = 2
}

resource "local_file" "dependent" {
  filename = "${path.module}/dependent.txt"
  content  = "Static content"

  lifecycle {
    replace_triggered_by = [random_pet.trigger.id]
  }
}
```

---

### Hands-on Lab: Lifecycle Rules

**Lab Goal:** Practice using lifecycle rules to control resource behavior.

---

**Exercise 1: `create_before_destroy`**

```bash
mkdir -p ~/terraform-labs/lab10-lifecycle
cd ~/terraform-labs/lab10-lifecycle
```

Create `main.tf`:

```hcl
terraform {
  required_providers {
    local = { source = "hashicorp/local" }
  }
}

resource "local_file" "web_config" {
  filename = "${path.module}/web-config.txt"
  content  = "Server configuration v1"

  lifecycle {
    create_before_destroy = true
  }
}
```

```bash
terraform init
terraform apply -auto-approve
cat web-config.txt
```

Now change the content:

```hcl
resource "local_file" "web_config" {
  filename = "${path.module}/web-config.txt"
  content  = "Server configuration v2"

  lifecycle {
    create_before_destroy = true
  }
}
```

```bash
terraform plan
# Observe: resource will be replaced, with create happening before destroy
terraform apply -auto-approve
```

---

**Exercise 2: `prevent_destroy`**

Add to `main.tf`:

```hcl
resource "local_file" "database_backup" {
  filename = "${path.module}/db-backup.txt"
  content  = "Critical database backup reference"

  lifecycle {
    prevent_destroy = true
  }
}
```

```bash
terraform apply -auto-approve

# Try to destroy everything
terraform destroy
# Error: local_file.database_backup has prevent_destroy set

# You can destroy other resources with targeting
terraform destroy -target=local_file.web_config -auto-approve
```

To clean up, remove `prevent_destroy = true` from the configuration, then destroy.

---

**Exercise 3: `ignore_changes`**

```hcl
resource "local_file" "user_data" {
  filename = "${path.module}/user-data.txt"
  content  = "Initial setup content"

  lifecycle {
    ignore_changes = [content]
  }
}
```

```bash
terraform apply -auto-approve
cat user-data.txt
```

Now change the content in `main.tf`:

```hcl
resource "local_file" "user_data" {
  filename = "${path.module}/user-data.txt"
  content  = "Updated content that should be ignored"

  lifecycle {
    ignore_changes = [content]
  }
}
```

```bash
terraform plan
# "No changes" — Terraform ignores the content change
```

---

## Data Sources

Data sources allow Terraform to **read** information from external sources without creating or managing anything. They are declared with `data` blocks.

### Syntax

```hcl
data "local_file" "existing" {
  filename = "${path.module}/existing-file.txt"
}

output "file_content" {
  value = data.local_file.existing.content
}
```

### How Data Sources Differ from Resources

- A `resource` block tells Terraform to **create and manage** an object.
- A `data` block tells Terraform to **read** information from an existing object.

Data sources are read during the planning phase and their values are available for use in resource configurations.

### Common Data Sources

```hcl
# Read an existing local file
data "local_file" "config" {
  filename = "/etc/hostname"
}

# Read AWS AMI information
data "aws_ami" "ubuntu" {
  most_recent = true
  owners      = ["099720109477"]   # Canonical

  filter {
    name   = "name"
    values = ["ubuntu/images/hvm-ssd/ubuntu-*-22.04-amd64-server-*"]
  }
}

# Use the AMI data in a resource
resource "aws_instance" "web" {
  ami           = data.aws_ami.ubuntu.id
  instance_type = "t2.micro"
}
```

---

### Hands-on Lab: Data Sources

**Lab Goal:** Practice using data sources to read existing information.

---

**Exercise 1: Reading an Existing File**

```bash
mkdir -p ~/terraform-labs/lab11-datasources
cd ~/terraform-labs/lab11-datasources

# Create a file that already exists (NOT managed by Terraform)
echo "This file was created manually, not by Terraform." > existing-data.txt
```

Create `main.tf`:

```hcl
terraform {
  required_providers {
    local = { source = "hashicorp/local" }
  }
}

# Read the existing file (data source — does NOT manage it)
data "local_file" "existing" {
  filename = "${path.module}/existing-data.txt"
}

# Create a new file using data from the existing one
resource "local_file" "copy" {
  filename = "${path.module}/copy-of-existing.txt"
  content  = <<-EOT
    --- Copy of Existing File ---
    Original content: ${data.local_file.existing.content}
    Original file size: ${length(data.local_file.existing.content)} characters
  EOT
}

output "original_content" {
  value = data.local_file.existing.content
}

output "original_content_base64" {
  value = data.local_file.existing.content_base64
}
```

```bash
terraform init
terraform apply -auto-approve

cat copy-of-existing.txt
terraform output
```

Notice that `terraform destroy` will remove `copy-of-existing.txt` (managed by Terraform) but will NOT touch `existing-data.txt` (only read by a data source).

---

**Exercise 2: Combining Data Sources with Conditions**

```bash
# Create two files to read
echo "Server A: Active" > server-a-status.txt
echo "Server B: Maintenance" > server-b-status.txt
```

```hcl
variable "active_server" {
  type    = string
  default = "a"
}

data "local_file" "server_a" {
  filename = "${path.module}/server-a-status.txt"
}

data "local_file" "server_b" {
  filename = "${path.module}/server-b-status.txt"
}

resource "local_file" "report" {
  filename = "${path.module}/status-report.txt"
  content  = <<-EOT
    Active Server: ${var.active_server}
    Server A Status: ${trimspace(data.local_file.server_a.content)}
    Server B Status: ${trimspace(data.local_file.server_b.content)}
    Primary: ${var.active_server == "a" ? trimspace(data.local_file.server_a.content) : trimspace(data.local_file.server_b.content)}
  EOT
}
```

```bash
terraform apply -auto-approve
cat status-report.txt

terraform apply -auto-approve -var='active_server=b'
cat status-report.txt
```

---

## Meta-Arguments

Meta-arguments are special arguments available to all resource types. They control Terraform's behavior rather than the resource's configuration.

---

## Count

The `count` meta-argument creates multiple instances of a resource:

```hcl
resource "local_file" "servers" {
  count = 3

  filename = "${path.module}/server-${count.index}.txt"
  content  = "Configuration for server ${count.index}"
}
```

This creates three files: `server-0.txt`, `server-1.txt`, and `server-2.txt`.

### Referencing Count Resources

Each instance is referenced by its index:

```hcl
output "first_server" {
  value = local_file.servers[0].filename
}

output "all_servers" {
  value = local_file.servers[*].filename    # Splat expression
}
```

### Conditional Resources with Count

Use `count` with a conditional to optionally create a resource:

```hcl
variable "create_backup" {
  type    = bool
  default = true
}

resource "local_file" "backup" {
  count = var.create_backup ? 1 : 0

  filename = "${path.module}/backup.txt"
  content  = "Backup data"
}
```

---

## for_each

The `for_each` meta-argument creates one instance for each item in a map or set. Unlike `count`, it uses meaningful keys instead of numeric indices.

### Using a Set

```hcl
resource "local_file" "environments" {
  for_each = toset(["dev", "staging", "prod"])

  filename = "${path.module}/${each.key}-config.txt"
  content  = "Configuration for ${each.key} environment"
}
```

### Using a Map

```hcl
variable "files" {
  type = map(string)
  default = {
    "readme"    = "This is the project README."
    "changelog" = "Version 1.0.0 - Initial release."
    "license"   = "MIT License"
  }
}

resource "local_file" "docs" {
  for_each = var.files

  filename = "${path.module}/${each.key}.txt"
  content  = each.value
}
```

### Referencing for_each Resources

```hcl
output "readme_file" {
  value = local_file.docs["readme"].filename
}

output "all_files" {
  value = { for k, v in local_file.docs : k => v.filename }
}
```

### Count vs. for_each

|Feature|`count`|`for_each`|
|---|---|---|
|Index type|Numeric (0, 1, 2...)|String keys|
|Removing middle item|Shifts all indices — can cause unnecessary destroys|Only the specific key is removed|
|Best for|Simple multiples of identical resources|Resources with unique identifiers|

In general, prefer `for_each` when each instance has a meaningful name or identity. Use `count` for simple "create N copies" scenarios.

---

### Hands-on Lab: Count and for_each

**Lab Goal:** Practice using `count` and `for_each` to create dynamic sets of resources.

---

**Exercise 1: Using Count**

```bash
mkdir -p ~/terraform-labs/lab12-meta-args
cd ~/terraform-labs/lab12-meta-args
```

Create `main.tf`:

```hcl
terraform {
  required_providers {
    local  = { source = "hashicorp/local" }
    random = { source = "hashicorp/random" }
  }
}

variable "server_count" {
  type    = number
  default = 4
}

resource "random_pet" "server_names" {
  count  = var.server_count
  length = 2
}

resource "local_file" "server_configs" {
  count = var.server_count

  filename = "${path.module}/server-${count.index}-${random_pet.server_names[count.index].id}.txt"
  content  = <<-EOT
    Server #${count.index}
    Name: ${random_pet.server_names[count.index].id}
    Port: ${8080 + count.index}
    Status: active
  EOT
}

output "server_names" {
  value = random_pet.server_names[*].id
}

output "config_files" {
  value = local_file.server_configs[*].filename
}
```

```bash
terraform init
terraform apply -auto-approve

terraform output server_names
ls server-*.txt
```

Change the count and observe:

```bash
terraform apply -auto-approve -var='server_count=2'
# Two servers are destroyed, two remain

terraform apply -auto-approve -var='server_count=6'
# Four new servers are created
```

---

**Exercise 2: Using for_each with a Set**

Create `for_each.tf`:

```hcl
variable "environments" {
  type    = set(string)
  default = ["dev", "staging", "production"]
}

resource "local_file" "env_configs" {
  for_each = var.environments

  filename = "${path.module}/env-${each.key}.txt"
  content  = <<-EOT
    Environment: ${each.key}
    Debug: ${each.key == "dev" ? "enabled" : "disabled"}
    Log Level: ${each.key == "production" ? "error" : "debug"}
  EOT
}

output "environment_files" {
  value = { for k, v in local_file.env_configs : k => v.filename }
}
```

```bash
terraform apply -auto-approve
cat env-dev.txt
cat env-production.txt
```

---

**Exercise 3: Using for_each with a Map**

Create `for_each_map.tf`:

```hcl
variable "users" {
  type = map(object({
    role  = string
    email = string
  }))
  default = {
    alice = {
      role  = "admin"
      email = "alice@example.com"
    }
    bob = {
      role  = "developer"
      email = "bob@example.com"
    }
    carol = {
      role  = "viewer"
      email = "carol@example.com"
    }
  }
}

resource "local_file" "user_profiles" {
  for_each = var.users

  filename = "${path.module}/user-${each.key}.txt"
  content  = <<-EOT
    Username: ${each.key}
    Role: ${each.value.role}
    Email: ${each.value.email}
    Access Level: ${each.value.role == "admin" ? "full" : each.value.role == "developer" ? "read-write" : "read-only"}
  EOT
}

output "user_files" {
  value = { for k, v in local_file.user_profiles : k => v.filename }
}
```

```bash
terraform apply -auto-approve

cat user-alice.txt
cat user-bob.txt
terraform output user_files
```

---

## Version Constraints

Version constraints ensure that your configuration uses compatible versions of Terraform and its providers. This prevents unexpected behavior when new versions are released.

### Provider Version Constraints

```hcl
terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 5.0"     # Any 5.x version (>= 5.0, < 6.0)
    }
    local = {
      source  = "hashicorp/local"
      version = ">= 2.5.0"   # Version 2.5.0 or higher
    }
  }
}
```

### Terraform Version Constraints

```hcl
terraform {
  required_version = ">= 1.8.0"    # Requires Terraform 1.8.0 or higher
}
```

### Version Constraint Syntax

|Operator|Meaning|Example|Matches|
|---|---|---|---|
|`= 1.0.0`|Exact version|`= 1.0.0`|Only 1.0.0|
|`!= 1.0.0`|Exclude version|`!= 1.0.0`|Any except 1.0.0|
|`> 1.0.0`|Greater than|`> 1.0.0`|1.0.1, 1.1.0, 2.0.0, ...|
|`>= 1.0.0`|Greater or equal|`>= 1.0.0`|1.0.0, 1.0.1, 1.1.0, ...|
|`< 2.0.0`|Less than|`< 2.0.0`|1.9.9, 1.0.0, 0.1.0, ...|
|`<= 2.0.0`|Less or equal|`<= 2.0.0`|2.0.0, 1.9.9, ...|
|`~> 1.0`|Pessimistic (minor)|`~> 1.0`|>= 1.0, < 2.0|
|`~> 1.0.4`|Pessimistic (patch)|`~> 1.0.4`|>= 1.0.4, < 1.1.0|

The `~>` operator (the "pessimistic constraint") is the most commonly used. It allows the rightmost component to increment but locks the others:

- `~> 5.0` means `>= 5.0.0, < 6.0.0` (allows minor and patch updates)
- `~> 5.1.0` means `>= 5.1.0, < 5.2.0` (allows only patch updates)

### Combining Constraints

```hcl
terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = ">= 5.0, < 5.50, != 5.25.0"
    }
  }
}
```

### The Dependency Lock File

When you run `terraform init`, Terraform creates a `.terraform.lock.hcl` file that records the exact provider versions selected. This ensures everyone on the team uses the same versions.

```bash
# After terraform init, examine the lock file
cat .terraform.lock.hcl
```

The lock file should be committed to version control. To update the locked versions:

```bash
terraform init -upgrade
```

---

### Hands-on Lab: Version Constraints

**Lab Goal:** Practice configuring and understanding version constraints.

---

**Exercise 1: Setting Up Version Constraints**

```bash
mkdir -p ~/terraform-labs/lab13-versions
cd ~/terraform-labs/lab13-versions
```

Create `main.tf`:

```hcl
terraform {
  required_version = ">= 1.5.0"

  required_providers {
    local = {
      source  = "hashicorp/local"
      version = "~> 2.5"
    }
    random = {
      source  = "hashicorp/random"
      version = ">= 3.5.0, < 4.0.0"
    }
  }
}

resource "random_pet" "demo" {
  length = 2
}

resource "local_file" "demo" {
  filename = "${path.module}/version-demo.txt"
  content  = "Pet: ${random_pet.demo.id}"
}
```

```bash
terraform init
```

Examine the lock file:

```bash
cat .terraform.lock.hcl
```

The lock file shows the exact versions installed and their hashes for integrity verification.

---

**Exercise 2: Understanding Constraint Behavior**

Try using a version that doesn't exist:

```hcl
terraform {
  required_providers {
    local = {
      source  = "hashicorp/local"
      version = "= 0.0.1"    # This version doesn't exist
    }
  }
}
```

```bash
terraform init
# Error: no available releases match the given constraints
```

Fix it back to a valid constraint and reinitialize:

```hcl
terraform {
  required_providers {
    local = {
      source  = "hashicorp/local"
      version = "~> 2.5"
    }
  }
}
```

```bash
terraform init
```

---

**Exercise 3: Upgrading Provider Versions**

```bash
# Show currently installed provider versions
terraform version

# Upgrade to latest versions within constraints
terraform init -upgrade

# Compare the lock file
cat .terraform.lock.hcl
```

---

### Graded Assessment: Terraform Configuration Essentials

**Challenge 1:** Write a Terraform configuration that uses `for_each` to create configuration files for a set of microservices. Each file should include the service name, port, and health check path.

```hcl
terraform {
  required_version = ">= 1.5.0"
  required_providers {
    local = {
      source  = "hashicorp/local"
      version = "~> 2.5"
    }
  }
}

variable "services" {
  type = map(object({
    port        = number
    health_path = string
  }))
  default = {
    "auth-service" = {
      port        = 8081
      health_path = "/auth/health"
    }
    "user-service" = {
      port        = 8082
      health_path = "/users/health"
    }
    "order-service" = {
      port        = 8083
      health_path = "/orders/health"
    }
    "notification-service" = {
      port        = 8084
      health_path = "/notifications/health"
    }
  }
}

resource "local_file" "service_configs" {
  for_each = var.services

  filename = "${path.module}/${each.key}-config.json"
  content  = <<-EOT
    {
      "service": "${each.key}",
      "port": ${each.value.port},
      "health_check": "${each.value.health_path}",
      "log_level": "info"
    }
  EOT
}

output "service_endpoints" {
  value = {
    for name, config in var.services :
    name => "http://localhost:${config.port}${config.health_path}"
  }
}
```

```bash
terraform init
terraform apply -auto-approve
terraform output service_endpoints
```

**Challenge 2:** Create a configuration that uses `count` to create a variable number of log files. Use a lifecycle rule to prevent destruction of the first log file. Add version constraints for all providers and the Terraform binary.

```hcl
terraform {
  required_version = "~> 1.5"
  required_providers {
    local = {
      source  = "hashicorp/local"
      version = "~> 2.5"
    }
  }
}

variable "log_count" {
  type    = number
  default = 3

  validation {
    condition     = var.log_count >= 1 && var.log_count <= 10
    error_message = "Log count must be between 1 and 10."
  }
}

resource "local_file" "primary_log" {
  filename = "${path.module}/log-0-primary.txt"
  content  = "Primary log file — creation timestamp: Terraform Apply"

  lifecycle {
    prevent_destroy = true
  }
}

resource "local_file" "additional_logs" {
  count = var.log_count - 1

  filename = "${path.module}/log-${count.index + 1}.txt"
  content  = "Log file #${count.index + 1}"

  lifecycle {
    create_before_destroy = true
  }
}

output "primary_log" {
  value = local_file.primary_log.filename
}

output "additional_logs" {
  value = local_file.additional_logs[*].filename
}
```

```bash
terraform init
terraform apply -auto-approve

# Try to destroy — should fail because of prevent_destroy
terraform destroy
# Error: primary_log cannot be destroyed

# Scale up logs
terraform apply -auto-approve -var='log_count=6'
```

**Challenge 3:** Write a configuration that combines data sources, variables, outputs, lifecycle rules, and `for_each`. The configuration should read an existing file, use its content as input to create environment-specific configuration files, and output a summary.

```hcl
terraform {
  required_version = ">= 1.5.0"
  required_providers {
    local  = { source = "hashicorp/local", version = "~> 2.5" }
    random = { source = "hashicorp/random", version = "~> 3.5" }
  }
}

# Assume this file exists with a project name
# echo "my-awesome-project" > project-name.txt
data "local_file" "project_name" {
  filename = "${path.module}/project-name.txt"
}

locals {
  project = trimspace(data.local_file.project_name.content)
}

variable "environments" {
  type = map(object({
    replicas  = number
    log_level = string
  }))
  default = {
    dev = {
      replicas  = 1
      log_level = "debug"
    }
    staging = {
      replicas  = 2
      log_level = "info"
    }
    prod = {
      replicas  = 3
      log_level = "error"
    }
  }
}

resource "random_password" "env_secrets" {
  for_each = var.environments
  length   = 32
  special  = false
}

resource "local_file" "env_configs" {
  for_each = var.environments

  filename = "${path.module}/${local.project}-${each.key}.txt"
  content  = <<-EOT
    Project: ${local.project}
    Environment: ${each.key}
    Replicas: ${each.value.replicas}
    Log Level: ${each.value.log_level}
    Secret Length: ${length(random_password.env_secrets[each.key].result)} chars
  EOT

  lifecycle {
    create_before_destroy = true
  }
}

output "project_name" {
  value = local.project
}

output "config_files" {
  value = { for k, v in local_file.env_configs : k => v.filename }
}
```

```bash
# Create the prerequisite file
echo "my-awesome-project" > project-name.txt

terraform init
terraform apply -auto-approve

cat my-awesome-project-dev.txt
cat my-awesome-project-prod.txt
terraform output config_files

terraform destroy -auto-approve
```

---

## Course Conclusion

Congratulations on completing **Terraform for the Absolute Beginner**! Here is a summary of what you have learned:

**Module 1 – IaC and Terraform Essentials:** You learned why Infrastructure as Code matters, how Terraform compares to other IaC tools, and the core workflow of `init`, `plan`, `apply`, and `destroy`. You wrote your first HCL configurations and managed the full lifecycle of local resources.

**Module 2 – Terraform Configuration:** You dove into providers, configuration directory structure, multiple providers, input variables (with types, defaults, and validation), local values, resource attributes, implicit and explicit dependencies, and output variables. You learned how to parameterize and organize configurations for reuse.

**Module 3 – State Management:** You explored the state file, understood its purpose in mapping configuration to real resources, practiced state commands (`state list`, `state show`, `state rm`), and learned best practices for remote state, locking, and security.

**Module 4 – Working with Terraform:** You mastered advanced commands, understood mutable vs. immutable infrastructure, used lifecycle rules (`create_before_destroy`, `prevent_destroy`, `ignore_changes`), worked with data sources, used `count` and `for_each` for dynamic resource creation, and configured version constraints for stability.

### Where to Go Next

Your Terraform journey has just begun. Here are recommended next steps:

- **Terraform Modules:** Package reusable configurations into modules for sharing and composition.
- **Remote Backends:** Set up S3, Azure Blob, or Terraform Cloud for team state management.
- **Terraform Cloud / HCP Terraform:** Explore managed state, remote runs, and policy enforcement.
- **Cloud Providers:** Apply what you've learned to AWS, Azure, or GCP resources.
- **Workspaces:** Manage multiple environments (dev, staging, prod) with workspaces.
- **Sentinel / OPA:** Policy as code for governance and compliance.
- **CI/CD Integration:** Automate Terraform in GitHub Actions, GitLab CI, or Jenkins pipelines.
- **Terraform Import:** Bring existing infrastructure under Terraform management.

Keep building, keep automating, and keep your infrastructure as code!

---

_End of Terraform for the Absolute Beginner Tutorial_