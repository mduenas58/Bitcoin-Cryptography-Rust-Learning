## Ansible Variable Precedence & Registered Variables — A Deeper Explanation

---

### Part 1 — Variable Precedence

#### What Is Precedence and Why Does It Matter?

When you define the same variable in multiple places — inventory, playbook, command line — Ansible needs a rule to decide which value wins. That rule is called **variable precedence**. Think of it as a chain of authority: the higher up the chain a variable is defined, the more it overrides everything below it.

This is actually very useful. It means you can set a sensible default at the group level, let individual hosts override it when they need something different, and still have the ability to force a specific value at runtime via the command line — all without touching your playbooks.

---

#### The Layered Example

Let's build this up step by step using a realistic scenario: configuring a DNS server across a fleet of web servers.

**Step 1 — Group Variable (lowest of these four)**

```ini
# inventory.ini

[web_servers]
web1 ansible_host=192.168.1.10
web2 ansible_host=192.168.1.11
web3 ansible_host=192.168.1.12

[web_servers:vars]
dns_server=8.8.8.8     # Group variable — applies to ALL hosts in web_servers
```

When Ansible processes this inventory, it creates a mental model like this:

```
web1 → dns_server = 8.8.8.8  (inherited from group)
web2 → dns_server = 8.8.8.8  (inherited from group)
web3 → dns_server = 8.8.8.8  (inherited from group)
```

Each host gets its own copy of the group variable. They don't share one reference — they each hold the value independently, which is why host-level overrides work cleanly.

**Step 2 — Host Variable overrides the group**

Now suppose `web2` needs a different DNS server — maybe it's in a different network segment:

```ini
[web_servers]
web1 ansible_host=192.168.1.10
web2 ansible_host=192.168.1.11 dns_server=1.1.1.1   # ← host-level override
web3 ansible_host=192.168.1.12

[web_servers:vars]
dns_server=8.8.8.8
```

Ansible's resolution now looks like this:

```
web1 → dns_server = 8.8.8.8  (from group)
web2 → dns_server = 1.1.1.1  ← host variable wins over group variable
web3 → dns_server = 8.8.8.8  (from group)
```

The host-level definition wins because **host variables always take precedence over group variables**. The rule makes intuitive sense: a specific host's config should override a generic group default.

**Step 3 — Play variable overrides the host**

Now say your playbook also defines the variable:

```yaml
# configure_dns.yml
- name: Configure DNS
  hosts: web_servers
  vars:
    dns_server: "9.9.9.9"     # ← play-level variable

  tasks:
    - name: Set DNS in resolv.conf
      lineinfile:
        path: /etc/resolv.conf
        line: "nameserver {{ dns_server }}"
```

Now every host — including `web2` — gets `9.9.9.9`, because the play-level variable overrides both the group and host variables. The resolution becomes:

```
web1 → dns_server = 9.9.9.9  (play variable wins)
web2 → dns_server = 9.9.9.9  (play variable wins, overrides host variable too)
web3 → dns_server = 9.9.9.9  (play variable wins)
```

This is useful when you're testing a new DNS server across your whole fleet temporarily, without changing the inventory.

**Step 4 — Extra vars: the ultimate override**

Finally, you can pass a variable directly on the command line using `-e` (or `--extra-vars`). This has the absolute highest precedence and overrides everything — group vars, host vars, play vars, role defaults, everything:

```bash
ansible-playbook configure_dns.yml -e "dns_server=208.67.222.222"
```

Result:

```
web1 → dns_server = 208.67.222.222  (extra var wins over everything)
web2 → dns_server = 208.67.222.222  (extra var wins over everything)
web3 → dns_server = 208.67.222.222  (extra var wins over everything)
```

This is extremely powerful for one-off overrides, emergency changes, or CI/CD pipelines where you inject environment-specific values at deploy time without touching any files.

---

#### The Full Precedence Ladder (Simplified)

From **lowest to highest** priority — a higher entry always beats anything below it:

|Priority|Variable Source|
|---|---|
|1 (lowest)|Role defaults (`roles/myrole/defaults/main.yml`)|
|2|Inventory group variables|
|3|Inventory host variables|
|4|Playbook group vars files (`group_vars/`)|
|5|Playbook host vars files (`host_vars/`)|
|6|Play-level `vars:` block|
|7|Task-level `vars:` block|
|8|`set_fact` / `register`|
|9 (highest)|Extra vars (`-e` on the command line)|

The practical takeaway: **defaults go low, specifics go high**. Set broad defaults at the group or role level, let individual hosts override as needed, and use `-e` only for emergency or one-time overrides.

---

### Part 2 — Registered Variables

#### The Problem They Solve

Ansible tasks are normally fire-and-forget — a task runs, does its job, and that's it. But sometimes the output of one task is the input for the next. Registered variables are how Ansible captures the result of a task and makes it available to subsequent tasks.

#### Basic Example

```yaml
- name: Read and display /etc/hosts
  hosts: web1
  tasks:

    - name: Read the contents of /etc/hosts
      shell: cat /etc/hosts
      register: hosts_file_result        # ← capture output into this variable

    - name: Print the contents to screen
      debug:
        var: hosts_file_result           # ← use the captured output
```

When this runs, `hosts_file_result` holds a rich dictionary of information about what happened during the shell command. The raw output looks something like this:

```json
{
  "cmd": "cat /etc/hosts",
  "rc": 0,
  "start": "2026-03-08 10:00:01.234567",
  "end": "2026-03-08 10:00:01.256789",
  "delta": "0:00:00.022222",
  "stdout": "127.0.0.1   localhost\n192.168.1.10   web1",
  "stderr": "",
  "stdout_lines": ["127.0.0.1   localhost", "192.168.1.10   web1"],
  "stderr_lines": [],
  "changed": true,
  "failed": false
}
```

#### Accessing Specific Fields

Rather than printing the entire object, you access individual fields using dot notation:

```yaml
tasks:
  - name: Run a command
    shell: cat /etc/hosts
    register: result

  - name: Print just the file contents
    debug:
      msg: "{{ result.stdout }}"       # just the command output

  - name: Print line by line
    debug:
      msg: "{{ result.stdout_lines }}" # output as a list of lines

  - name: Print the return code
    debug:
      msg: "Return code was: {{ result.rc }}"

  - name: Print execution time
    debug:
      msg: "Took {{ result.delta }} to complete"
```

#### Using the Return Code for Conditional Logic

The `rc` (return code) field is particularly powerful. By convention, `rc: 0` means success, anything else means failure. You can use this to make decisions:

```yaml
tasks:
  - name: Check if nginx is running
    shell: systemctl is-active nginx
    register: nginx_status
    ignore_errors: true           # don't fail the play if nginx is down

  - name: Start nginx if it's not running
    service:
      name: nginx
      state: started
    when: nginx_status.rc != 0   # only run this task if nginx wasn't active
```

Without `register`, there would be no way to make that second task conditional on the first task's result.

#### A More Complete Real-World Example

```yaml
- name: Deploy application
  hosts: app_servers
  tasks:

    - name: Check current app version
      shell: cat /opt/myapp/version.txt
      register: current_version
      ignore_errors: true

    - name: Show current version
      debug:
        msg: "Current version is: {{ current_version.stdout }}"
      when: current_version.rc == 0

    - name: Warn if version file is missing
      debug:
        msg: "No version file found — this may be a fresh install"
      when: current_version.rc != 0

    - name: Run deployment script
      shell: /opt/deploy.sh
      register: deploy_result

    - name: Show deployment log
      debug:
        msg: "{{ deploy_result.stdout_lines }}"

    - name: Check for errors in deployment
      fail:
        msg: "Deployment failed! Stderr: {{ deploy_result.stderr }}"
      when: deploy_result.rc != 0
```

This playbook reads the current version, makes conditional decisions based on whether that succeeded, runs a deploy, and then checks whether the deploy itself succeeded — all using registered variables to pass information between steps.

---

#### Variable Scope for Registered Variables

Registered variables live at the **host scope** for the duration of the entire playbook run. This means two important things:

**First**, they survive across multiple plays in the same playbook file:

```yaml
# Play 1
- name: Gather information
  hosts: web_servers
  tasks:
    - name: Get server uptime
      shell: uptime -p
      register: uptime_result

# Play 2 — runs after Play 1, but result is still accessible
- name: Generate report
  hosts: web_servers
  tasks:
    - name: Print uptime from previous play
      debug:
        msg: "{{ uptime_result.stdout }}"   # still works!
```

**Second**, each host has its own independent copy of the variable. If you run a task against 10 hosts and register the result, `result.stdout` for `web1` holds `web1`'s output, and `result.stdout` for `web2` holds `web2`'s output. They don't interfere with each other.

---

#### The Quick Alternative: the `-v` Flag

If you just want to see what a task returned without writing a debug task, run your playbook with `-v` (verbose):

```bash
ansible-playbook my_playbook.yml -v
```

This prints the return values of every task directly to the terminal. Use `-vv` or `-vvv` for progressively more detail. It's great for quick debugging without modifying the playbook itself.

---

### Summary

Variable precedence gives you a clean hierarchy: broad defaults at the group/role level, specific overrides at the host level, in-playbook control at the play level, and the command-line `-e` flag as the emergency override that beats everything. Registered variables then let you chain tasks together by capturing output and referencing it downstream — accessing specific fields like `.stdout`, `.rc`, `.stderr`, and `.stdout_lines` to make your playbooks dynamic and context-aware.