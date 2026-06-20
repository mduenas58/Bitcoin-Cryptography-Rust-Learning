---
title: "The Ultimate Guide to Umbrel Commands, SSH Access, and CLI Operations"
source: "https://www.danielbrummitt.com/p/the-ultimate-guide-to-umbrel-commands"
author:
  - "[[DANIEL BRUMMITT]]"
published: 2025-03-18
created: 2026-04-21
description: "Your one-stop resource for managing your Umbrel node like a pro"
tags:
  - "clippings"
---
### Your one-stop resource for managing your Umbrel node like a pro

## Introduction

If you're running an Umbrel node, knowing how to effectively use its command line interface can dramatically enhance your ability to manage, troubleshoot, and customize your setup. This comprehensive guide covers everything from basic commands to advanced CLI operations, giving you the power to take full control of your Umbrel node.

![The Ultimate Guide to Umbrel Commands, SSH Access, and CLI Operations](https://substackcdn.com/image/fetch/$s_!CvAH!,w_1456,c_limit,f_webp,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Ffd1ba8b1-b5ea-4849-a407-fbc714f6ea44_512x512.jpeg)

The Ultimate Guide to Umbrel Commands, SSH Access, and CLI Operations

## Getting Started with Basic Umbrel Commands

Umbrel provides a straightforward set of commands for daily management. These commands handle core functionality like installation, updates, and basic system control.

### Installation

To install Umbrel on a compatible device, simply run:

```markup
curl -L https://umbrel.sh | bash
```

This single command downloads and executes the Umbrel installation script, setting up everything you need to get started.

### Essential Control Commands

Once installed, these commands will be your go-to for basic operations:

```markup
# Start Umbrel
umbrel start

# Stop Umbrel
umbrel stop

# Restart Umbrel
umbrel restart
```

### Update Management

Keeping your node updated is critical for security and new features:

```markup
# Update Umbrel
umbrel update

# Check if updates are available
umbrel update check
```

### Status Monitoring

Need to know what's happening with your node?

```markup
# Check Umbrel status
umbrel status

# View logs for troubleshooting
umbrel logs
```

## Accessing Your Umbrel Node via SSH

SSH access gives you direct terminal access to your Umbrel device, enabling more powerful management options.

### Enabling SSH Access

1. Navigate to Settings > Advanced in the Umbrel web UI
2. Toggle the SSH access switch to enable it
3. Make note of the displayed SSH credentials

### Connecting to Your Node

```markup
# Connect using hostname (if mDNS is working on your network)
ssh umbrel@umbrel.local

# Connect using IP address (more reliable method)
ssh umbrel@192.168.x.x
```

### Default Credentials

- Username: `umbrel`
- Default password: `moneyprintergobrrr`

**Pro tip:** You'll likely be prompted to change this password on first login for security reasons.

## Advanced CLI Operations

For power users who want complete control, these advanced operations let you dive deeper into your Umbrel node's configuration.

### Docker Management

Since Umbrel runs its apps in Docker containers, knowing these commands is invaluable:

```markup
# List all running containers
docker ps

# View logs from a specific container
docker logs [container_name]

# Restart a problematic container
docker restart [container_name]
```

### File System Navigation

Knowing where key files are stored helps with customization and troubleshooting:

```markup
# Navigate to main Umbrel directory
cd ~/umbrel

# Check app data directories
cd ~/umbrel/app-data

# View Docker compose files for apps
cd ~/umbrel/apps
```

### Backup and Restore Operations

Protecting your data should be a priority:

```markup
# Create a manual backup
umbrel backup

# Restore from a previous backup
umbrel restore [backup_file]
```

### Advanced Troubleshooting

When things go wrong, these commands can help:

```markup
# Start Umbrel in debug mode
umbrel start --debug

# Reset Umbrel (caution: this will erase data)
umbrel reset

# Check disk usage
df -h
```

### App Management via CLI

Manage your apps without using the web interface:

```markup
# List all installed apps
umbrel app list

# Install a specific app
umbrel app install [app_name]

# Uninstall an app
umbrel app uninstall [app_name]
```

## Network Configuration and Testing

Network issues are common with self-hosted services. These commands help diagnose problems:

```markup
# Check network configuration
umbrel network info

# Test connectivity
ping umbrel.local
```

## Best Practices and Tips

1. **Regular Backups**: Schedule regular backups of your node, especially before updates or major changes.
2. **Update Frequently**: Security updates are important - check for updates at least once a month.
3. **Monitor Disk Space**: Blockchain data grows over time, so keep an eye on available storage.
4. **Use Strong Passwords**: Change the default SSH password immediately after enabling remote access.
5. **Check Logs First**: When troubleshooting, always check the logs before making changes.

## Common Troubleshooting Scenarios

- **Umbrel Won't Start**: Try checking logs with `umbrel logs` to identify the issue.
- **App Not Working**: Use `docker logs [container_name]` to see app-specific errors.
- **Web UI Inaccessible**: Verify network configuration and try accessing via IP address instead of hostname.
- **Disk Space Issues**: Use `df -h` to check available space and consider pruning blockchain data or removing unused apps.

## Conclusion

Mastering Umbrel's command line interface transforms you from a casual user to a node operator with complete control. While the web UI provides an excellent experience for everyday tasks, the CLI opens up possibilities for customization, automation, and advanced troubleshooting.

Whether you're running Bitcoin Core, Lightning Network, or any of the other fantastic apps available on Umbrel, these commands will help ensure your node runs smoothly and efficiently.

*Note: Commands may vary slightly between Umbrel versions. This guide is based on recent versions as of publication.*

---

*Do you have favorite Umbrel commands or CLI tricks not covered here? Share them in the comments below!*

---