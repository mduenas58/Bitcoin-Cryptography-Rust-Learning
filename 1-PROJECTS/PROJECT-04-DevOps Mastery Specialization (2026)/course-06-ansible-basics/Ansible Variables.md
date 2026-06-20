## Ansible Variables — A Deeper Explanation with Examples

---

### What Are Variables and Why Do They Matter?

In any programming or scripting context, a variable is simply a named container that holds a value. The power of variables comes from the fact that you write your logic _once_, and the variable fills in whatever value is appropriate at runtime.

In Ansible's case, imagine you manage 200 web servers. Each one has a different IP address, a different hostname, maybe a different admin username. Without variables, you'd need 200 separate playbooks — one per server. With variables, you write **one** playbook and let variables supply the differences. That's the entire point.

---

### Where Variables Come From

Ansible lets you define variables in several places, each with a different scope and purpose.

**1. In the Inventory File**

This is the most common starting point. When you list your hosts, you can attach variables directly to them:

```ini
# inventory.ini

[web_servers]
web1 ansible_host=192.168.1.10 ansible_user=admin ansible_ssh_pass=secret123
web2 ansible_host=192.168.1.11 ansible_user=deploy ansible_ssh_pass=pass456
web3 ansible_host=192.168.1.12 ansible_user=admin ansible_ssh_pass=secret789
```

Here, `ansible_host`, `ansible_user`, and `ansible_ssh_pass` are built-in Ansible variables. When Ansible processes `web1`, it uses `192.168.1.10` to connect; when it processes `web2`, it uses `192.168.1.11` — same playbook, different values automatically.

**2. Directly Inside a Playbook**

You can define variables right inside the playbook using the `vars` block:

```yaml
# playbook.yml
- name: Configure DNS on all servers
  hosts: all
  vars:
    dns_server: "8.8.8.8"
    dns_search_domain: "example.com"

  tasks:
    - name: Add DNS entry to resolv.conf
      lineinfile:
        path: /etc/resolv.conf
        line: "nameserver {{ dns_server }}"
```

Notice `{{ dns_server }}` — that's Jinja2 templating syntax (more on that below). When Ansible runs this task, it replaces `{{ dns_server }}` with `8.8.8.8`. If you later want to switch DNS providers, you change the variable in one place at the top, not buried in every task.

**3. In a Separate Host Variable File (Best Practice)**

For real-world use, the cleanest approach is to store variables for each host in their own dedicated file. Ansible looks for these automatically in a folder called `host_vars/`:

```
project/
├── inventory.ini
├── playbook.yml
└── host_vars/
    ├── web1.yml
    ├── web2.yml
    └── web3.yml
```

Each file is named after the host it belongs to:

```yaml
# host_vars/web1.yml
dns_server: "8.8.8.8"
http_port: 80
max_connections: 200
admin_email: "ops@web1.example.com"
```

```yaml
# host_vars/web2.yml
dns_server: "1.1.1.1"
http_port: 8080
max_connections: 500
admin_email: "ops@web2.example.com"
```

When Ansible runs the playbook against `web1`, it reads `host_vars/web1.yml` and uses those values. When it runs against `web2`, it picks up `host_vars/web2.yml` automatically. The playbook itself never needs to change.

---

### A Practical Before/After Example

Here's a playbook with everything **hard-coded** (bad practice):

```yaml
- name: Apply firewall rules
  hosts: web1
  tasks:
    - name: Allow HTTP
      firewalld:
        port: 80/tcp
        state: enabled

    - name: Set max connections
      sysctl:
        name: net.core.somaxconn
        value: 200

    - name: Notify admin
      mail:
        to: ops@web1.example.com
        subject: "Firewall updated"
```

If another team member wants to reuse this for `web2` with port `8080`, max connections `500`, and a different email, they have to dig through the playbook and edit every value manually — and risk breaking something.

Here's the same playbook **with variables** (good practice):

```yaml
# playbook.yml
- name: Apply firewall rules
  hosts: all
  tasks:
    - name: Allow HTTP
      firewalld:
        port: "{{ http_port }}/tcp"
        state: enabled

    - name: Set max connections
      sysctl:
        name: net.core.somaxconn
        value: "{{ max_connections }}"

    - name: Notify admin
      mail:
        to: "{{ admin_email }}"
        subject: "Firewall updated on {{ inventory_hostname }}"
```

Now `host_vars/web1.yml` and `host_vars/web2.yml` (shown above) supply the right values for each server. The playbook is completely reusable with zero modifications.

---

### Jinja2 Templating — The `{{ }}` Syntax

The double-curly-brace syntax `{{ variable_name }}` is called **Jinja2 templating**. Jinja2 is a templating engine that Ansible uses to evaluate expressions before executing tasks.

**Rule 1 — Variable at the start of a value: wrap in quotes**

```yaml
# CORRECT — quotes required when the value starts with {{ }}
port: "{{ http_port }}"
path: "{{ base_dir }}/config"
```

Without quotes, YAML tries to parse `{{ http_port }}` as a dictionary and throws a syntax error.

**Rule 2 — Variable embedded mid-string: quotes optional but recommended**

```yaml
# Both of these work fine
message: "Server {{ inventory_hostname }} is ready"
message:  Server {{ inventory_hostname }} is ready
```

Because the string doesn't start with `{{`, YAML parses it as plain text and Ansible handles the substitution. Quotes are still a good habit for clarity.

**Rule 3 — You can use expressions, not just variable names**

```yaml
vars:
  max_conn: 200

tasks:
  - name: Set double the max connections
    sysctl:
      value: "{{ max_conn * 2 }}"       # Results in 400

  - name: Uppercase the hostname
    debug:
      msg: "{{ inventory_hostname | upper }}"   # Jinja2 filter
```

---

### Variable Precedence (Quick Reference)

Ansible has a strict order when the same variable is defined in multiple places. Higher on this list wins:

|Priority|Source|
|---|---|
|Highest|Extra vars (`-e` on command line)|
|↑|Task-level `vars`|
|↑|Playbook-level `vars`|
|↑|`host_vars/` files|
|↑|Inventory file variables|
|Lowest|Role defaults|

So if `dns_server` is set to `8.8.8.8` in `host_vars/web1.yml` but you run the playbook with `-e "dns_server=1.1.1.1"`, the command-line value wins.

---

### Summary

Variables in Ansible are the mechanism that makes a single playbook work across hundreds of different servers. Define them in inventory files for quick setups, in `vars:` blocks for playbook-specific values, and in `host_vars/` files for organized, per-host configuration. Access them anywhere with `{{ variable_name }}` using Jinja2 templating, and remember to quote values that start with `{{`. The payoff is a codebase where your logic (the playbook) and your data (the variables) are cleanly separated — making it far easier to reuse, maintain, and hand off to teammates.