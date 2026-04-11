# Module 8 – Python for DevOps

## Why Python for DevOps?
- Glue language: connects APIs, CLIs, and services
- Rich ecosystem: boto3, paramiko, requests, fabric, PyYAML
- Used in Ansible modules, Terraform providers, and most cloud SDKs

## Key Libraries
| Library       | Use Case                                     |
|---------------|----------------------------------------------|
| `os` / `sys`  | OS interaction, args, environment vars       |
| `subprocess`  | Run shell commands from Python               |
| `pathlib`     | Modern file path manipulation                |
| `requests`    | HTTP API calls                               |
| `boto3`       | AWS SDK                                      |
| `paramiko`    | SSH connections                              |
| `PyYAML`      | Parse and write YAML                         |
| `rich`        | Beautiful terminal output                    |
| `click`       | Build CLI tools                              |

## DevOps Patterns

```python
import subprocess, sys

def run(cmd: list[str]) -> str:
    """Run a shell command and return stdout, raise on failure."""
    result = subprocess.run(cmd, capture_output=True, text=True, check=True)
    return result.stdout.strip()

# Environment variables (never hardcode secrets)
import os
db_password = os.environ["DB_PASSWORD"]

# YAML parsing
import yaml
with open("config.yaml") as f:
    config = yaml.safe_load(f)
```
