**By adding entries to the `/etc/hosts` file**

This is the correct answer because the `/etc/hosts` file is the **original, DNS-independent method** for hostname resolution on Linux/Unix systems.

---

## Why This Works: The Resolution Order

Linux uses **Name Service Switch (NSS)** configured in `/etc/nsswitch.conf`:
```bash
$ grep hosts /etc/nsswitch.conf
hosts: files dns
```

This means:
1. **`files`** → Check `/etc/hosts` first
2. **`dns`** → Then query DNS if not found

**No DNS required.** No network connectivity needed.

---

## Practical Implementation

### Basic `/etc/hosts` Entry
```bash
# Format: IP_ADDRESS    CANONICAL_HOSTNAME    [ALIASES...]
127.0.0.1       localhost
192.168.1.10    db-server.internal    db
192.168.1.20    app-server.internal   app
```

### Testing Without DNS
```bash
# Ping using hosts file resolution
$ ping db-server.internal
PING db-server.internal (192.168.1.10) 56(84) bytes of data.

# SSH using alias
$ ssh app
Last login: from 192.168.1.20
```

---

## Why The Other Options Are Wrong

| Option | Why It's Incorrect |
|--------|---------------------|
| **Static IPs** | IP addressing is separate from **name resolution**. Static IPs don't map names to addresses. |
| **Third-party tool** | Unnecessary. `/etc/hosts` is built-in, standard, works offline. |
| **`/etc/resolv.conf`** | **This configures DNS!** Contains nameserver IPs. Requires DNS to function. |

---

## DevOps Context: When `/etc/hosts` Still Matters

### 1. **Local Development Environments**
```bash
# Prevent accidental external traffic
127.0.0.1 api.stripe.com
127.0.0.1 graph.facebook.com
```

### 2. **Air-Gapped/Offline Systems**
No DNS server available. Entire network resolves via `/etc/hosts` or internal DNS.

### 3. **Kubernetes/Container Hosts**
```bash
# Pods use /etc/hosts for local entries
kubectl exec pod -- cat /etc/hosts
# Kubernetes injects pod name, service entries here
```

### 4. **Emergency Overrides**
```bash
# Force a specific host to resolve locally
# Even if DNS says something else
192.168.1.50   production-api.company.com
```

### 5. **Blocking Malware/Hosts Files**
```bash
# /etc/hosts as a blocklist
0.0.0.0 tracking-server.com
0.0.0.0 ad.doubleclick.net
```

---

## The Critical `/etc/hosts` Mistake

**Don't remove the `127.0.0.1 localhost` entry!**
```bash
# BROKEN - many tools assume localhost resolves
# 127.0.0.1 localhost   # Deleted by mistake

# Now 'localhost' goes to DNS, fails offline
$ ping localhost
ping: localhost: Name or service not known
```

---

## Summary

**`/etc/hosts` is the DNS-independent, offline-capable, zero-configuration hostname resolution method.** It predates DNS, survives alongside it, and remains essential for:
- Local development isolation
- Offline/air-gapped environments
- Emergency overrides
- Container networking
- Malware blocking

The other options either:
- **Don't resolve names** (static IPs)
- **Require DNS** (`resolv.conf`)
- **Add unnecessary complexity** (third-party tools)