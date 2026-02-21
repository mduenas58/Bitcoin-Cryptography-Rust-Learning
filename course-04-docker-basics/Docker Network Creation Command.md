## Result of the Docker Network Creation Command

The command:
```bash
docker network create --driver bridge --subnet 182.18.0.0/24 --gateway 182.18.0.1 wp-mysql-network
```

### **Successful Output:**
If successful, Docker will return the **network ID** (a long hexadecimal string), for example:
```
a3f2d8e9b1c54a7f8d3e2b1c5a7f8d9e
```

### **What This Command Does:**

1. **Creates a custom bridge network** named `wp-mysql-network`
2. **Configures the subnet** as `182.18.0.0/24` (256 IP addresses from 182.18.0.0 to 182.18.0.255)
3. **Sets the gateway** to `182.18.0.1`
4. **Uses the bridge driver** (default for container-to-container communication on same host)

### **Verification Commands:**

```bash
# List all networks to confirm creation
docker network ls

# Expected output includes:
NETWORK ID     NAME                DRIVER    SCOPE
...            wp-mysql-network     bridge    local

# Inspect the network details
docker network inspect wp-mysql-network
```

### **Inspect Output Example:**
```json
[
    {
        "Name": "wp-mysql-network",
        "Id": "a3f2d8e9b1c54a7f8d3e2b1c5a7f8d9e",
        "Created": "2026-02-21T10:30:45.123456789Z",
        "Scope": "local",
        "Driver": "bridge",
        "EnableIPv6": false,
        "IPAM": {
            "Driver": "default",
            "Options": {},
            "Config": [
                {
                    "Subnet": "182.18.0.0/24",
                    "Gateway": "182.18.0.1"
                }
            ]
        },
        "Internal": false,
        "Attachable": false,
        "Ingress": false,
        "ConfigFrom": {
            "Network": ""
        },
        "ConfigOnly": false,
        "Containers": {},
        "Options": {},
        "Labels": {}
    }
]
```

### **Purpose of This Network:**
This network is specifically designed for:
- **WordPress and MySQL containers** to communicate securely
- **Isolated environment** for your web application stack
- **Predictable IP addressing** with the custom subnet

### **Using the Network:**

```bash
# Run MySQL container connected to this network
docker run -d \
  --name mysql-db \
  --network wp-mysql-network \
  -e MYSQL_ROOT_PASSWORD=rootpassword \
  -e MYSQL_DATABASE=wordpress \
  mysql:8.0

# Run WordPress container connected to the same network
docker run -d \
  --name wordpress-app \
  --network wp-mysql-network \
  -p 8080:80 \
  -e WORDPRESS_DB_HOST=mysql-db \
  -e WORDPRESS_DB_USER=root \
  -e WORDPRESS_DB_PASSWORD=rootpassword \
  -e WORDPRESS_DB_NAME=wordpress \
  wordpress:latest
```

### **Network Configuration Details:**
- **Subnet:** `182.18.0.0/24` (Range: 182.18.0.0 - 182.18.0.255)
- **Gateway:** `182.18.0.1` (host's interface on this network)
- **Available IPs for containers:** 182.18.0.2 to 182.18.0.254
- **Broadcast address:** 182.18.0.255

### **Troubleshooting if Command Fails:**

| Error | Solution |
|-------|----------|
| `Error response from daemon: network with name wp-mysql-network already exists` | Use a different name or remove existing: `docker network rm wp-mysql-network` |
| `Error response from daemon: Pool overlaps with other one on this address space` | The subnet conflicts with an existing network. Choose a different subnet |
| `Error response from daemon: invalid network subnet` | The subnet format is incorrect. Ensure it follows CIDR notation (e.g., 182.18.0.0/24) |