# Hermes Full-Stack Health Check — Session Reference

## Complete Verification Session (2026-05-24)

This reference documents the actual commands and expected output patterns for a full-stack health check of the Hermes ecosystem.

## 1. Check Listening Ports

```bash
ss -tlnp | grep -E '8420|8648|9119'
```

Expected output (all running):
```
LISTEN 0      511         127.0.0.1:8420      0.0.0.0:*    users:(("MainThread",pid=58,fd=30))
LISTEN 0      511           0.0.0.0:8648      0.0.0.0:*    users:(("MainThread",pid=383,fd=28))
LISTEN 0      2048        127.0.0.1:9119      0.0.0.0:*    users:(("hermes",pid=300,fd=13))
```

Empty output means that service is not running.

## 2. Check Running Processes

```bash
ps aux | grep -E 'hermes gateway|hermes-web-ui|dashboard|memory-tencentdb' | grep -v grep
```

Expected:
```
yanxin  PID  ... python3 ... hermes gateway run --replace
yanxin  PID  ... node --import tsx/esm ... @tencentdb-agent-memory/memory-tencentdb/src/gateway/server.ts
yanxin  PID  ... hermes dashboard --port 9119 --host 127.0.0.1 --no-open
```

## 3. Check Gateway Status

```bash
hermes gateway status
```

Expected:
```
✓ Gateway is running (PID: X)
  (Running manually, not as a system service)
```

## 4. Check Platform Connections (Gateway Logs)

```bash
tail -5 ~/.hermes/logs/gateway.log | grep -E 'running with|connected'
```

Expected:
```
Gateway running with 3 platform(s)
```

Full connection sequence from a fresh start:
```
Connecting to api_server...
[Api_Server] API server listening on http://127.0.0.1:8642 (model: hermes-agent)
✓ api_server connected
Connecting to feishu...
[Feishu] Connected in websocket mode (feishu)
✓ feishu connected
Connecting to weixin...
[Weixin] Connected account=b4fc996d base=https://ilinkai.weixin.qq.com
✓ weixin connected
Gateway running with 3 platform(s)
```

## 5. Verify Messaging Channels End-to-End

### Step 1: List available targets

```
send_message action=list
```

Expected output:
```
Available messaging targets:

Feishu:
  feishu:oc_xxxxx (dm)

Weixin:
  weixin:o9cq801d0fsgKmInswETASzBSaSA@im.wechat (dm)

Bare platform name (e.g. "telegram") sends to home channel.
```

### Step 2: Send test messages

```python
send_message message="✅ 连通性测试 — 微信通道正常" target=weixin:o9cq...@im.wechat
send_message message="✅ 连通性测试 — 飞书通道正常" target=feishu:oc_xxxxx
```

Expected success:
```
{"success": true, "platform": "weixin", ... "mirrored": true}
{"success": true, "platform": "feishu", ... "mirrored": true}
```

## 6. Web UI & Dashboard Content Check

```bash
curl -s http://localhost:8648 | head -5
curl -s http://localhost:9119 | head -5
```

Both should return HTML starting with `<!doctype html>`.

## 7. Starting Services That Are Down

### Web UI (port 8648)
```bash
hermes-web-ui start 8648    # run in background
```

### Dashboard (port 9119)
```bash
hermes dashboard --port 9119 --host 127.0.0.1 --no-open   # run in background
```

### Hermes Gateway (auto-replaces existing)
```bash
hermes gateway run --replace
```

## Platform Credentials (stored in ~/.hermes/.env)

| Platform | Key Config Values |
|----------|------------------|
| WeChat | `WEIXIN_ACCOUNT_ID`, `WEIXIN_TOKEN`, `WEIXIN_BASE_URL` |
| Feishu | `FEISHU_APP_ID`, `FEISHU_APP_SECRET`, `FEISHU_DOMAIN=feishu`, `FEISHU_CONNECTION_MODE=websocket` |

## Common Issues

1. **Port 8648 and 9119 not listening** after a system restart — Web UI and Dashboard don't auto-start from the startup script (only Gateway + TDAI Gateway do). Manually start them.
2. **Port 8420 listening but Hermes Gateway process missing** — the TDAI Memory Gateway is independent. Check both: `ss` for port, `hermes gateway status` for process.
3. **send_message returns `mirrored: true`** — this means the message went through the current agent's channel AND was mirrored to the target platform. It's normal and indicates success.
