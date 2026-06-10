---
name: home-assistant-deployment
description: Deploy and manage Home Assistant on M710q Ubuntu base via Docker, with Tailscale Funnel exposure and Hermes integration.
version: 1.0.0
---

## Overview

Deploy Home Assistant in Docker on the M710q base machine (Ubuntu 22.04, i5-6600T, 15GB RAM), expose it via Tailscale Funnel for remote access, and connect it to Hermes Agent for AI-driven smart home control.

## Trigger

When the user wants to:
- Install or update Home Assistant on the base machine
- Add custom integrations (HACS or manual)
- Configure Tailscale Funnel for HA remote access
- Connect HA to Hermes Agent via HASS_TOKEN
- Troubleshoot HA deployment issues on M710q

## Prerequisites

- Docker installed (`docker.io` from Ubuntu repos is sufficient, v29.1.3+)
- Docker Compose v2 (comes with `docker-compose-v2` package)
- Tailscale connected with Funnel enabled
- `miao` user in `docker` group (`sudo usermod -aG docker $USER`)

## Step 1: Deploy HA via Docker Compose

```yaml
# /home/miao/docker/ha/docker-compose.yml
services:
  homeassistant:
    container_name: homeassistant
    image: ghcr.io/home-assistant/home-assistant:stable
    network_mode: host
    restart: unless-stopped
    volumes:
      - /home/miao/docker/ha/config:/config
      - /etc/localtime:/etc/localtime:ro
    environment:
      - TZ=Asia/Shanghai
```

Key decisions:
- `network_mode: host` — required for device discovery (mDNS, UPnP) on LAN
- No `devices:` section unless USB dongles (Zigbee/Z-Wave) are present
- Config volume at `/home/miao/docker/ha/config/` — created with `root` ownership by Docker

Commands:
```bash
mkdir -p /home/miao/docker/ha
# create docker-compose.yml above
sg docker -c "docker compose -f /home/miao/docker/ha/docker-compose.yml up -d"
```

## Step 2: Install HACS

The official `wget -O - https://get.hacs.xyz | bash` script often fails to detect the config dir. Manual install:

```bash
HACS_VERSION=$(curl -s https://api.github.com/repos/hacs/integration/releases/latest | grep '"tag_name"' | head -1 | sed 's/.*"tag_name": "\(.*\)".*/\1/')
wget -q "https://github.com/hacs/integration/releases/download/${HACS_VERSION}/hacs.zip" -O /tmp/hacs.zip
sudo mkdir -p /home/miao/docker/ha/config/custom_components/hacs
sudo unzip -qo /tmp/hacs.zip -d /home/miao/docker/ha/config/custom_components/hacs
# Restart HA
sg docker -c "docker restart homeassistant"
```

User then activates HACS in UI: Settings → Devices & Services → Add Integration → search "HACS" → GitHub OAuth.

## Step 3: Tailscale Funnel Exposure

### HA reverse proxy config (REQUIRED for Funnel)

Add to `/home/miao/docker/ha/config/configuration.yaml`:
```yaml
http:
  use_x_forwarded_for: true
  trusted_proxies:
    - 127.0.0.1
```

Use `docker exec homeassistant` to write files when sudo is unavailable:
```bash
sg docker -c "docker exec homeassistant sh -c 'echo \"...\" >> /config/configuration.yaml'"
```

### Funnel setup

**CRITICAL**: HA must be at root `/` — sub-paths (`/ha`) cause 400 Bad Request because HA uses absolute URLs.

```bash
# Reset first
sudo tailscale funnel --https=443 off
# HA at root
sudo tailscale funnel --bg --https=443 --set-path=/ http://localhost:8123
# Hermes Dashboard at /dash
sudo tailscale funnel --bg --https=443 --set-path=/dash http://127.0.0.1:9119
```

### Funnel Pitfalls

| Issue | Cause | Fix |
|-------|-------|-----|
| 400 Bad Request on `/ha` sub-path | HA doesn't support sub-path proxying | HA must be at root `/` |
| ERR_CONNECTION_TIMED_OUT from laptop | MagicDNS resolves ts.net → Tailscale IP; port 443 blocked | Use `http://100.86.13.11:8123` via Tailscale direct |
| Funnel reverts after HA restart | Funnel config is persistent but may need reset | Re-run funnel commands |
| Port 8443 blocked | Non-standard port blocked by client firewall/ISP | Use standard 443 |

### Alternative: Direct Tailscale access

When Funnel is unreliable from the laptop, use Tailscale direct IP:
```
http://100.86.13.11:8123
```
This works when both machines are on the same tailnet and ufw allows port 8123.

## Step 4: Install Custom Integrations (China)

GitHub downloads often fail/timeout from China. **Always use ghproxy.net mirror**:

```bash
# Pattern 1: Direct download (small repos)
wget -q "https://ghproxy.net/https://github.com/OWNER/REPO/archive/refs/heads/BRANCH.zip" -O /tmp/component.zip
unzip -qo /tmp/component.zip -d /tmp/extract
dir=$(ls /tmp/extract | head -1)
sudo cp -r /tmp/extract/${dir}/custom_components/COMPONENT /home/miao/docker/ha/config/custom_components/

# Pattern 2: git clone (larger repos or when wget fails)
git clone --depth 1 "https://ghproxy.net/https://github.com/OWNER/REPO" /tmp/repo
sudo cp -r /tmp/repo/custom_components/COMPONENT /home/miao/docker/ha/config/custom_components/
```

Restart HA after all installations:
```bash
sg docker -c "docker restart homeassistant"
```

## Step 5: Connect Hermes Agent

1. In HA: Profile → Long-Lived Access Tokens → Create Token "Hermes Agent"
2. Add to `~/.hermes/.env`:
   ```
   HASS_TOKEN=<long-lived-token>
   HASS_URL=http://localhost:8123
   ```
3. Restart Hermes Gateway: `hermes gateway`

Hermes will auto-enable 4 HA tools: `ha_get_state`, `ha_call_service`, `ha_list_entities`, `ha_list_services`.

## Platform Integration Reference

| Platform | HA Integration | Install Method | Status |
|----------|---------------|---------------|--------|
| Xiaomi/Mi Home | Xiaomi Miot Auto (`hass-xiaomi-miot`) | HACS / manual | ✅ Active |
| Dreame | Dreame Vacuum (`Tasshack/dreame-vacuum`) | HACS / manual | ✅ Active, 2K+ stars |
| Midea | Midea AC LAN (`georgezhao2010/midea_ac_lan`) | HACS / manual | ⚠️ Version-dependent |
| Haier | Haier (`banto6/haier`) | HACS / manual | ⚠️ DMCA risks |
| Home Connect (晶御) | Built-in Home Connect | HA native | ✅ Auto-discovered |
| Treeow (树新风) | Treeow Home (`hlhk2017/treeow-homeassistant`) | Manual | Niche |
| Huawei Smart Life | **NOT SUPPORTED** | — | ❌ Closed protocol |

### Midea-specific notes
- `hasscc/meiju` is outdated — incompatible with HA 2026.6+ (`'HomeAssistant' object has no attribute 'helpers'`)
- `midea_ac_lan` v0.3.22 is the recommended version for HA 2026.x
- Both local (midea_ac_lan) and cloud (Midea Auto Cloud) options exist; prefer local

## Quick Health Checks

```bash
# HA local status
curl -s -o /dev/null -w "HTTP %{http_code}\n" http://localhost:8123/

# Container status
sg docker -c "docker ps --format '{{.Names}} {{.Status}}'"

# Funnel status
tailscale funnel status

# Config validation
sg docker -c "docker exec homeassistant cat -n /config/configuration.yaml"
```

## Pitfalls

1. **Config ownership**: Docker creates config files as `root`. Use `sudo` or `docker exec` to modify — `patch` tool will fail on root-owned files.
2. **HA 2026.6+ compatibility**: Very new HA versions break older custom integrations. Check integration's last update date before installing.
3. **Funnel + sub-paths**: HA does NOT work behind a path prefix. Always use root `/` for HA.
4. **MagicDNS interference**: Laptop's Tailscale MagicDNS resolves `*.ts.net` to Tailscale IPs, which may route Funnel traffic through Tailscale instead of public internet. Use direct Tailscale IP as fallback.
5. **ufw blocks**: New ports (8123, 443) must be explicitly allowed in ufw.
6. **No Bluetooth**: Ignore `habluetooth` errors — harmless when no BT hardware is available to the container.
