# Gateway Systematic Recovery

Use this checklist when the gateway is down. Symptoms: WeChat/Feishu not responding, Web UI chat stall, platform connections silent.

## 1. Check Running Processes

```bash
# Are the key services alive?
ss -tlnp | grep -E "8420|8642|8648|9119"
```

| Port | Service | Notes |
|------|---------|-------|
| 8420 | TDAI Memory Gateway | Hermes memory (TencentDB) bridge |
| 8642 | Hermes API Server | Gateway's HTTP API endpoint (chat routes through this) |
| 8648 | hermes-web-ui | Web UI frontend |
| 9119 | hermes dashboard | Built-in dashboard |

## 2. Check Gateway Process

```bash
hermes gateway status
# Also check:
ps aux | grep 'hermes.*gateway' | grep -v grep
```

## 3. Check Logs

```bash
# Main gateway log
tail -50 ~/.hermes/logs/gateway.log
# OOM diagnosis
tail -10 ~/.hermes/logs/gateway-exit-diag.log 2>/dev/null
# TDAI gateway log
tail -30 /tmp/tdai-gw.log 2>/dev/null
```

## 4. Common Failure Modes

### TDAI Gateway crashed with EPIPE

**Symptom**: WeChat/iLink stops responding. `tdai-gw.log` shows:
```
Error: write EPIPE
    at Socket._writeGeneric (node:net:971:11)
```

**Root cause**: The TDAI gateway (Hermes memory bridge) lost connection to the Hermes agent bridge's IPC socket.

**Fix**:
```bash
# 1. Kill any stale TDAI process
pkill -f "tencentdb.*gateway/server" 2>/dev/null

# 2. Restart TDAI gateway
cd ~/.memory-tencentdb && nohup node --import tsx/esm \
  node_modules/@tencentdb-agent-memory/memory-tencentdb/src/gateway/server.ts \
  > /tmp/tdai-gw.log 2>&1 &

# 3. Wait for it to bind
sleep 5
ss -tlnp | grep 8420  # Should show listening

# 4. Restart Hermes gateway
hermes gateway run --replace
```

### Gateway process vanishes (OOM kill)

**Symptom**: Gateway log jumps from normal INFO directly to next startup without any ERROR/CRITICAL/traceback.

**Root cause**: Linux OOM killer terminated the process when total WSL memory was exhausted.

**Diagnosis**:
```bash
grep -i 'oom\|out of memory' /var/log/kern.log 2>/dev/null
# Or check gateway-exit-diag.log for:
# "gateway.exit_nonzero" with "sys_exc": "(None, None, None)"
tail -5 ~/.hermes/logs/gateway-exit-diag.log
```

**Fix**: See `references/wsl-oom-prevention.md`.

### `hermes gateway restart` kills new process (timeout)

**Symptom**: Gateway stops entirely after `hermes gateway restart` — old process killed but new one never finishes starting.

**Root cause**: `hermes gateway restart` starts the gateway in foreground. If startup takes >30s (terminal tool default timeout), the tool sends SIGTERM, killing the new gateway process.

**Fix**: Use `terminal(background=true)`:
```bash
terminal(command='hermes gateway run', background=true)
sleep 15
hermes gateway status
```

### Web UI chat not working (401)

**Symptom**: Web UI accepts messages, agent never responds. Browser console shows `Socket.IO Upstream 401`.

**Root cause**: `platforms.api_server.key` is empty with `host: 0.0.0.0`.

**Fix**: Set an API key or bind to localhost:
```bash
echo "API_SERVER_KEY=$(openssl rand -hex 32)" >> ~/.hermes/.env
# OR
hermes config set platforms.api_server.extra.host 127.0.0.1
```
Then restart gateway.
