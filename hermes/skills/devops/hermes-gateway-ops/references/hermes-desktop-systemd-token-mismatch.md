# Hermes Desktop systemd Dashboard token mismatch

## Trigger

Use this reference when Hermes Desktop remote backend shows any of these symptoms:

- “提示词发送失败”
- “网关断开” during a running Desktop task
- “代理 1 个失败” while Dashboard/Gateway ports appear healthy
- `curl /api/status` returns 200 but Desktop still cannot send prompts

## Key distinction

Do not conflate these layers:

| Layer | Typical port | What it means |
|---|---:|---|
| Messaging Gateway | 8642 | WeChat/Feishu/API Server platform bridge |
| Dashboard backend | 9119 | Desktop remote backend + `/api/ws` WebSocket |
| Web UI | 8648 | Browser UI / Node server |
| TDAI Memory | 8420 | Memory gateway |

If Desktop says “gateway disconnected”, it often means **Dashboard WebSocket** failed, not that `hermes-gateway.service` died.

## Diagnostic sequence

```bash
# Services and ports
systemctl is-active hermes-dashboard hermes-gateway hermes-web-ui hermes-tdai 2>&1 || true
ss -tlnp 2>/dev/null | grep -E ':(8420|8642|8648|9119)\b' || true

# Endpoint liveness
curl --max-time 5 -sS -o /tmp/dash.json -w 'dashboard:%{http_code}\n' http://127.0.0.1:9119/api/status
curl --max-time 5 -sS -o /tmp/api.json -w 'api_server:%{http_code}\n' http://127.0.0.1:8642/health
curl --max-time 5 -sS -o /tmp/webui.json -w 'webui:%{http_code}\n' http://127.0.0.1:8648/health
curl --max-time 5 -sS -o /tmp/tdai.json -w 'tdai:%{http_code}\n' http://127.0.0.1:8420/health
```

Then test the actual Dashboard WebSocket upgrade. A 200 HTTP status alone is not sufficient.

```bash
python3 - <<'PY'
import re, urllib.request, socket, ssl, base64, os
host='miao-thinkcentre-m710q-n080.tail589fe7.ts.net'
html=urllib.request.urlopen('https://'+host+'/', timeout=8).read().decode('utf-8','ignore')
token=re.search(r"__HERMES_SESSION_TOKEN__\s*=\s*['\"]([^'\"]+)", html).group(1)
key=base64.b64encode(os.urandom(16)).decode()
sock=socket.create_connection((host,443), timeout=8)
ws=ssl.create_default_context().wrap_socket(sock, server_hostname=host)
ws.sendall((f"GET /api/ws?token={token} HTTP/1.1\r\nHost: {host}\r\nUpgrade: websocket\r\nConnection: Upgrade\r\nSec-WebSocket-Key: {key}\r\nSec-WebSocket-Version: 13\r\nOrigin: https://{host}\r\n\r\n").encode())
print(ws.recv(200).decode(errors='ignore').split('\r\n')[0])
ws.close()
PY
```

Expected:

```text
HTTP/1.1 101 Switching Protocols
```

## systemd token mismatch pattern

Root cause pattern seen on the M710q base:

1. `hermes-dashboard.service` is a system-level service under `/etc/systemd/system/`.
2. It auto-starts Dashboard on port 9119 without `HERMES_DASHBOARD_SESSION_TOKEN`.
3. Manual attempts to start a fixed-token Dashboard fail with `address already in use` because systemd already owns 9119.
4. Desktop remote backend can appear connected, but prompt sends fail or long tasks lose the WebSocket.

Check the port owner and environment:

```bash
PID=$(ss -tlnp 2>/dev/null | awk -F'pid=' '/:9119/{split($2,a,","); print a[1]; exit}')
echo "pid:$PID"
ps -p "$PID" -o pid,ppid,etime,cmd --no-headers
tr '\0' '\n' < /proc/$PID/environ 2>/dev/null | grep '^HERMES_DASHBOARD_SESSION_TOKEN=' || echo token_env_missing
systemctl status hermes-dashboard.service --no-pager -n 20
```

If `token_env_missing` and systemd owns the process, do not keep restarting Desktop. Fix the service ownership first.

## Recovery path

If sudo is available:

```bash
sudo systemctl stop hermes-dashboard.service
sudo systemctl disable hermes-dashboard.service
sudo systemctl daemon-reload
```

Then start Dashboard with a stable token:

```bash
TOKEN_FILE="$HOME/.hermes/dashboard_session_token"
if [ ! -s "$TOKEN_FILE" ]; then
  umask 077
  python3 - <<'PY' > "$TOKEN_FILE"
import secrets
print(secrets.token_urlsafe(32))
PY
fi
chmod 600 "$TOKEN_FILE"

bash -lc 'TOKEN=$(cat "$HOME/.hermes/dashboard_session_token"); export HERMES_DASHBOARD_SESSION_TOKEN="$TOKEN"; exec "$HOME/.hermes/hermes-agent/venv/bin/hermes" dashboard --port 9119 --host 0.0.0.0 --insecure --no-open --skip-build'
```

If the terminal tool starts it in background, verify:

```bash
curl --max-time 5 -sS -o /tmp/dash.json -w 'local:%{http_code}\n' http://127.0.0.1:9119/api/status
curl --max-time 8 -sS -o /tmp/dash_pub.json -w 'public:%{http_code}\n' https://miao-thinkcentre-m710q-n080.tail589fe7.ts.net/api/status
# Run WebSocket 101 probe above
hermes chat -Q -q '只输出 OK 两个字母，不要标点' --provider custom:apikey-fun -m gpt-5.5 --toolsets safe
```

## Watchdog pattern

A useful operational guard is a per-minute watchdog that checks both:

1. `http://127.0.0.1:9119/api/status` returns 200
2. Funnel `/api/ws` upgrades to `101 Switching Protocols`

If either fails, restart only the Dashboard process on 9119. Do not restart `hermes-gateway` unless WeChat/Feishu/API Server are actually impacted.

## Pitfalls

- `local:200` / `public:200` is not enough; validate `/api/ws` with `101`.
- `hermes-gateway.service active` does not prove Desktop backend health.
- `pgrep -f 'hermes dashboard --port 9119'` may match the diagnostic shell itself; prefer the PID from `ss -tlnp` for killing/checking the real port owner.
- If systemd owns 9119, manual fixed-token starts will fail with `EADDRINUSE`; disable/patch the service first.
- Do not assume a served root HTML token comparison alone is authoritative; the real acceptance test is a successful WebSocket upgrade and a model send.
- WeChat/iLink rate limiting can hide progress reports during debugging; keep replies compact and avoid spammy interim updates.
