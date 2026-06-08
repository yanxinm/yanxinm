# Hermes Services Watchdog

Cron-based auto-restart for TDAI Gateway and Hermes Gateway processes.

## Problem: TDAI Gateway EPIPE Crash

TDAI Gateway (port 8420) connects to the Hermes Agent IPC bridge at `/tmp/hermes-agent-bridge.sock`. When the bridge restarts (e.g., due to config changes, process recycle), the TDAI Gateway's stale socket connection triggers an unhandled `Error: write EPIPE` — the Node.js process crashes with no auto-recovery.

**Symptoms:**
- WeChat/iLink channel goes silent
- `ss -tlnp | grep 8420` shows nothing listening
- `/tmp/tdai-gw.log` ends with:
  ```
  node:events:485
        throw er; // Unhandled 'error' event
  Error: write EPIPE
      at Socket._writeGeneric (node:net:971:11)
  ```
- Hermes Gateway may also be down (check `ps aux | grep "hermes gateway"`)

## Solution: Watchdog Script

Script at `~/.hermes/scripts/watchdog.sh` — runs every 2 minutes via cron, checks both services, restarts silently.

See `scripts/watchdog.sh` in the hermes-agent skill for the full source.

## Registration

```bash
hermes cron create --schedule "every 2m" --name "服务守护" --script watchdog.sh --no-agent
```

## How It Works

Cron ticks every 2 min → runs watchdog.sh → checks port 8420 + Gateway process
- Both up → silent exit, no output
- Something down → log line + restart → stdout delivered to user

## Logs

- Watchdog: `/tmp/hermes-watchdog.log`
- TDAI runtime: `/tmp/tdai-gw.log`
- Gateway runtime: `~/.hermes/logs/gateway.log`

## Manual Recovery

```bash
cd ~/.memory-tencentdb && nohup node --import tsx/esm node_modules/@tencentdb-agent-memory/memory-tencentdb/src/gateway/server.ts >> /tmp/tdai-gw.log 2>&1 &
cd ~/Hermes-Agent && source venv/bin/activate && nohup hermes gateway run --replace >> ~/.hermes/logs/gateway.log 2>&1 &
sleep 10 && ss -tlnp | grep 8420 && pgrep -f "hermes gateway run"
```
