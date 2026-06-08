---
name: tailscale
description: Tailscale VPN setup and management on headless Linux servers — install, auth, verify, and troubleshoot connectivity.
category: devops
---

# Tailscale Headless Setup

## Trigger
Use this skill when: connecting a headless Linux machine to Tailscale, authenticating without a browser, verifying tailnet connectivity, or troubleshooting Tailscale offline state.

## Quick Setup (Auth Key Method)

The browser-based auth (`tailscale up` → open link) **times out on headless machines** because the CLI waits for the browser flow to complete, which can't happen without a graphical session. Use auth keys instead.

### 1. Generate Auth Key
In Tailscale Admin Console: **Settings → Keys → Generate auth key**
URL: `https://login.tailscale.com/admin/settings/keys`

### 2. Connect with Auth Key
```bash
sudo tailscale up --auth-key=tskey-auth-<key> --accept-routes
```

### 3. Verify
```bash
tailscale status          # should show online
ping <other-machine-ip>   # test connectivity
```

## Pitfalls

- **`tailscale up` times out on headless**: The CLI waits for web auth flow completion. Without a browser on the machine, this always fails. Solution: always use `--auth-key`.
- **Auth key is consumed on first use**: If `tailscale up` with auth key succeeds but the machine later shows "Logged out", generate a new key — the old one is spent.
- **Permissions**: Requires `sudo` unless operator is configured (`sudo tailscale set --operator=$USER`).
- **After reboot**: `tailscale up` must run again (or configure as systemd service for auto-connect).

## Verification Checklist
- `tailscale status` — shows machine as online with IP
- `ping <tailscale-ip>` — zero packet loss
- Admin console shows green dot

## Systemd Auto-Start (Optional)
```bash
sudo systemctl enable --now tailscaled
```
Tailscale will reconnect automatically after reboot using the stored auth state.
