# Hermes Desktop Dashboard WebSocket stall recovery

## Symptom

Hermes Desktop is connected to the remote backend, then a long-running task reports the gateway disconnected or stops receiving responses. Messaging Gateway may still be healthy.

## Key distinction

Do not assume `hermes-gateway` died. Desktop remote mode primarily depends on the Python Dashboard WebSocket at `/api/ws` on port 9119. A stalled Dashboard can make Desktop say “gateway disconnected” while the messaging Gateway service remains active.

## Diagnosis sequence

```bash
# 1. Check the real messaging Gateway separately
systemctl is-active hermes-gateway 2>&1
pgrep -af 'hermes gateway'

# 2. Check Dashboard responsiveness with short timeout
curl --max-time 5 -sS -o /tmp/dash_status.json -w 'dash:%{http_code}\n' http://127.0.0.1:9119/api/status

# 3. Check port owner and active Desktop connections
ss -tlnp 2>/dev/null | grep ':9119' || true
ss -tnp 2>/dev/null | grep ':9119' | tail -20 || true

# 4. Confirm WebSocket handshake through Funnel
python3 - <<'PY'
import re, urllib.request, socket, ssl, base64, os
host='miao-thinkcentre-m710q-n080.tail589fe7.ts.net'
html=urllib.request.urlopen('https://'+host+'/', timeout=8).read().decode('utf-8','ignore')
token=re.search(r"__HERMES_SESSION_TOKEN__\s*=\s*['\"]([^'\"]+)", html).group(1)
key=base64.b64encode(os.urandom(16)).decode()
sock=socket.create_connection((host,443), timeout=8)
ctx=ssl.create_default_context(); ssock=ctx.wrap_socket(sock, server_hostname=host)
req=(f"GET /api/ws?token={token} HTTP/1.1\r\nHost: {host}\r\nUpgrade: websocket\r\nConnection: Upgrade\r\nSec-WebSocket-Key: {key}\r\nSec-WebSocket-Version: 13\r\nOrigin: https://{host}\r\n\r\n")
ssock.sendall(req.encode())
print(ssock.recv(200).decode(errors='ignore').split('\r\n')[0])
ssock.close()
PY
```

Expected healthy WebSocket result: `HTTP/1.1 101 Switching Protocols`.

## Recovery

If `hermes-gateway` is active but Dashboard `/api/status` times out or `/api/ws` fails:

```bash
PID=$(ss -tlnp 2>/dev/null | awk -F'pid=' '/:9119/{split($2,a,","); print a[1]; exit}')
echo "dashboard_pid:${PID:-none}"
[ -n "$PID" ] && kill "$PID" 2>/dev/null || true
sleep 3
# If SIGTERM does not release port, use SIGKILL only for the Dashboard PID.
ss -tlnp 2>/dev/null | grep ':9119' && [ -n "$PID" ] && kill -9 "$PID" 2>/dev/null || true
```

On the base machine, systemd/watchdog may auto-restart Dashboard. After recovery verify:

```bash
curl --max-time 5 -sS -o /tmp/dash_after.json -w 'local:%{http_code}\n' http://127.0.0.1:9119/api/status
curl --max-time 8 -sS -o /tmp/dash_public_after.json -w 'public:%{http_code}\n' https://miao-thinkcentre-m710q-n080.tail589fe7.ts.net/api/status
```

Then repeat the WebSocket handshake and one model smoke test:

```bash
/home/miao/.hermes/hermes-agent/venv/bin/hermes chat -Q -q '只输出 OK 两个字母，不要标点' --provider custom:apikey-fun -m gpt-5.5 --toolsets safe
```

## Hardening: add a Dashboard watchdog

If the user reports repeated “提示词发送失败” or “网关断开” after manual Dashboard restarts, do **not** keep telling them to reopen Desktop. Add a short-interval watchdog that checks both `/api/status` and `/api/ws`, then restarts only the 9119 Dashboard process when either fails.

Minimum watchdog behavior:

1. Keep a fixed `~/.hermes/dashboard_session_token` and launch Dashboard with `HERMES_DASHBOARD_SESSION_TOKEN=$(cat ~/.hermes/dashboard_session_token)` so Desktop does not keep inheriting fresh tokens after restarts.
2. Health check local HTTP: `curl --max-time 4 -fsS http://127.0.0.1:9119/api/status`.
3. Health check WebSocket through the same remote URL users configure in Desktop; expect `HTTP/1.1 101 Switching Protocols`.
4. On failure, kill only the PID listening on `:9119`, wait briefly, then `kill -9` only that Dashboard PID if it did not exit.
5. Restart Dashboard with `--host 0.0.0.0 --insecure --no-open --skip-build`.
6. Log to `~/.hermes/logs/dashboard-watchdog.log` and schedule every minute via user crontab.

Example crontab:

```bash
* * * * * /home/miao/.hermes/scripts/dashboard_watchdog.sh >/dev/null 2>&1
```

Verification after hardening must include all four:

| Check | Expected |
|---|---|
| Local Dashboard | `local:200` |
| Funnel Dashboard | `public:200` |
| WebSocket | `HTTP/1.1 101 Switching Protocols` |
| Model smoke test | `OK` |

## User-facing guidance

After a Dashboard WebSocket stall, tell the user to refresh/reopen Desktop. If the task session’s WebSocket already broke, advise starting a new Desktop conversation and re-sending the task rather than trusting the old stalled session.

If the user is frustrated by repeated failures, acknowledge the miss plainly and state the durable fix made (watchdog + exact verification). Avoid claiming “fixed” until the four verification checks above have passed.
