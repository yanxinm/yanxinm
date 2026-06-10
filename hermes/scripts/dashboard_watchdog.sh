#!/usr/bin/env bash
set -euo pipefail
LOG="$HOME/.hermes/logs/dashboard-watchdog.log"
TOKEN_FILE="$HOME/.hermes/dashboard_session_token"
DASHBOARD_BIN="$HOME/.hermes/hermes-agent/venv/bin/hermes"
URL_LOCAL="http://127.0.0.1:9119/api/status"
URL_PUBLIC="https://miao-thinkcentre-m710q-n080.tail589fe7.ts.net/api/status"
mkdir -p "$HOME/.hermes/logs"
if [[ ! -s "$TOKEN_FILE" ]]; then
  umask 077
  python3 - <<'PY' > "$TOKEN_FILE"
import secrets
print(secrets.token_urlsafe(32))
PY
fi
chmod 600 "$TOKEN_FILE"
log(){ printf '[%s] %s\n' "$(date '+%F %T')" "$*" >> "$LOG"; }
healthy_http(){ curl --max-time 4 -fsS "$URL_LOCAL" >/dev/null 2>&1; }
healthy_ws(){
python3 - <<'PY' >/dev/null 2>&1
import re, urllib.request, socket, ssl, base64, os, sys
host='miao-thinkcentre-m710q-n080.tail589fe7.ts.net'
try:
    html=urllib.request.urlopen('https://'+host+'/', timeout=5).read().decode('utf-8','ignore')
    m=re.search(r"__HERMES_SESSION_TOKEN__\s*=\s*['\"]([^'\"]+)", html)
    if not m: raise RuntimeError('no token')
    token=m.group(1)
    key=base64.b64encode(os.urandom(16)).decode()
    sock=socket.create_connection((host,443), timeout=5)
    ssock=ssl.create_default_context().wrap_socket(sock, server_hostname=host)
    req=(f"GET /api/ws?token={token} HTTP/1.1\r\nHost: {host}\r\nUpgrade: websocket\r\nConnection: Upgrade\r\nSec-WebSocket-Key: {key}\r\nSec-WebSocket-Version: 13\r\nOrigin: https://{host}\r\n\r\n")
    ssock.sendall(req.encode())
    first=ssock.recv(200).decode(errors='ignore').split('\r\n')[0]
    ssock.close()
    sys.exit(0 if '101 Switching Protocols' in first else 1)
except Exception:
    sys.exit(1)
PY
}
restart_dashboard(){
  local pids
  pids=$(pgrep -f "hermes dashboard --port 9119" || true)
  if [[ -n "$pids" ]]; then
    log "restart: killing dashboard pids: $pids"
    kill $pids 2>/dev/null || true
    sleep 3
    pids=$(pgrep -f "hermes dashboard --port 9119" || true)
    [[ -n "$pids" ]] && kill -9 $pids 2>/dev/null || true
  fi
  log "restart: starting dashboard"
  nohup env HERMES_DASHBOARD_SESSION_TOKEN="$(cat "$TOKEN_FILE")" "$DASHBOARD_BIN" dashboard --port 9119 --host 0.0.0.0 --insecure --no-open --skip-build >> "$HOME/.hermes/logs/dashboard-watchdog-dashboard.log" 2>&1 &
}
if healthy_http && healthy_ws; then
  log "ok"
  exit 0
fi
log "unhealthy: http_or_ws_failed"
restart_dashboard
sleep 6
if healthy_http && healthy_ws; then
  log "recovered"
  exit 0
fi
log "still_unhealthy"
exit 1
