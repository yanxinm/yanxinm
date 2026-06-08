# Hermes Web UI Dashboard — Startup & Troubleshooting

## Quick Start

```bash
# Start Web UI (port 8648)
hermes-web-ui start

# Start Gateway (port 8642, enables WeChat/Feishu etc.)
hermes gateway run        # foreground
nohup hermes gateway run > ~/.hermes/logs/gateway.log 2>&1 &   # background
```

## Status Checks

```bash
hermes-web-ui status          # "✔ hermes-web-ui is running"
hermes gateway status         # "✔ Gateway is running (PID: XXX)"
ps aux | grep -E 'hermes.*gateway|hermes-web-ui' | grep -v grep
```

## ⚠️ Two Different Interfaces

**Important:** There are two separate web interfaces that users often confuse:

| Name | Command | Port | Type |
|------|---------|------|------|
| **Hermes Dashboard** | `hermes dashboard` | **9119** (default) | Built-in web dashboard for config, API keys, sessions |
| **Hermes Web UI** | `hermes-web-ui` | **8648** (default) | npm-installed modern web interface |

If a user says "打开 9119 打不开", they likely mean `hermes dashboard`. If they say "Web UI 打不开", they mean `hermes-web-ui`.

### Starting Hermes Dashboard (port 9119)

```bash
# Check status
hermes dashboard --status

# Start (blocks foreground)
hermes dashboard --port 9119 --host 127.0.0.1

# Start in background (for terminal-based use)
nohup hermes dashboard --port 9119 --host 127.0.0.1 > /dev/null 2>&1 &

# Start in background, no browser popup (recommended for autostart)
nohup hermes dashboard --port 9119 --host 127.0.0.1 --no-open > /dev/null 2>&1 &

# Stop
hermes dashboard --stop

# With TUI mode (embedded chat tab)
hermes dashboard --port 9119 --tui
```

### Starting Hermes Web UI (port 8648)

```bash
hermes-web-ui start          # daemonizes automatically
hermes-web-ui stop
hermes-web-ui status
```

## Symptom → Root Cause Mapping

| User says/symptom | Likely root cause | Fix |
|---|---|---|
| "微信没通" / "WeChat not working" | Gateway not running | `hermes gateway run` |
| "9119 打不开" | `hermes dashboard` not running | `hermes dashboard --port 9119` (may need background mode) |
| "8648 打不开" | `hermes-web-ui` not running | `hermes-web-ui start` |
| "dashboard 打不开" (ambiguous) | Check which one — try both | Check with `ss -tlnp \| grep -E '9119\|8648'` |
| "hermes dashbord" (typo) | User wants web UI | Start web UI + open browser |
| "gateway 重新启动有问题" | api_server binding 0.0.0.0 without API_SERVER_KEY | Set `API_SERVER_KEY` in `.env` or change bind to `127.0.0.1` (see gateway-recovery.md) |
| Web UI shows login but no response | Gateway API server (:8642) down | Start gateway |
| Gateway running, Web UI running, WeChat still dead | Check gateway logs for weixin errors | `tail -30 ~/.hermes/logs/gateway.log` |

## Autostart (WSL + Windows Task Scheduler)

When WSL uses `init` (not systemd), auto-start all three services via a single Task Scheduler batch:

```batch
@echo off
echo Starting Hermes Web UI (no auth)...
wsl.exe -d Ubuntu -u yanxin bash -lc "AUTH_DISABLED=1 /home/yanxin/.npm-global/bin/hermes-web-ui start"

echo Starting Hermes Dashboard (9119)...
wsl.exe -d Ubuntu -u yanxin bash -lc "nohup hermes dashboard --port 9119 --host 127.0.0.1 --no-open > /dev/null 2>&1 &"

echo Starting Hermes Gateway...
wsl.exe -d Ubuntu -u yanxin bash -lc "cd /home/yanxin/Hermes-Agent && source venv/bin/activate && hermes gateway run --replace"
```

**Key points:**
- **Order matters:** web-ui (daemonizes) → dashboard (nohup background) → gateway (foreground, blocks)
- **`--no-open`** on dashboard prevents a browser popup at every login
- **`AUTH_DISABLED=1`** on web-ui skips token login (only safe on localhost)
- The gateway's `--replace` flag ensures only one gateway process runs

**Set up in Task Scheduler:**
1. Save as `C:\Tools\hermes-gateway-start.bat`
2. Create task: Trigger = "At logon", Delay = 30s, Action = start the .bat
3. Run with highest privileges so WSL can start services properly

## Port Map

| Service | Port | Default URL |
|---------|------|-------------|
| Hermes Dashboard (built-in) | 9119 | http://localhost:9119 |
| Hermes Web UI (npm) | 8648 | http://localhost:8648 |
| Gateway API Server | 8642 | http://127.0.0.1:8642 |

## Logs

```bash
# Gateway logs
tail -50 ~/.hermes/logs/gateway.log

# Web UI logs
tail -50 ~/.hermes-web-ui/server.log
```

## Common Pitfalls

- **`hermes gateway restart` kills the new gateway** — `hermes gateway restart` runs in foreground. If the terminal tool times out (30s default), SIGTERM kills the newly-started child process. Gateway stops entirely. **Fix:** Use `terminal(background=true)` with `hermes gateway run`, wait 15s, then verify with `hermes gateway status`.
- **Web UI login prompts for token** — the token is printed when `hermes-web-ui start` runs. Look for `?token=...` in the output. If lost, restart web-ui to regenerate.
- **Web UI logo/image broken (Hermes logo shows as placeholder)** — the npm package (`hermes-web-ui`) is missing `/logo.png` that the React app references (`<img alt="Hermes" src="/logo.png">`). The server falls back to serving `index.html` as a 200, so the browser shows a broken image. Fix:
  ```bash
  cp ~/Hermes-Agent/website/static/img/logo.png \
     ~/.npm-global/lib/node_modules/hermes-web-ui/dist/client/logo.png
  hermes-web-ui restart
  ```
  The logo is at `Hermes-Agent/website/static/img/logo.png` (1772x1799 PNG, ~1.3MB).
- **Gateway starts but WeChat doesn't connect** — iLink QR-code expired or network issue. Check gateway log for `[Weixin]` connection lines.
- **Both services running but user says "微信没通"** — gateway was started AFTER a previous session, user's chat hadn't tried yet. Just verify log has `✓ weixin connected`.
