# Web UI Chat Fails with 401 "Invalid API key"

## Symptom

- Web UI (port 8648) loads, you can log in, see the chat window, type messages
- Messages appear in the session history but **agent never responds**
- Browser console (F12) shows:
  ```
  Socket.IO run stream error: Upstream 401: {"error": {"message": "Invalid API key", "type": "invalid_request_error", "code": "invalid_api_key"}}
  ```
- Gateway IS running (`hermes gateway status` shows ✓)
- Health check passes: `curl http://127.0.0.1:8642/health` → `{"status": "ok"}`
- But other endpoints fail: `curl http://127.0.0.1:8642/v1/models` → 401

## Root Cause

The hermes-web-ui chat window proxies requests through the **external Gateway API server** (port 8642), NOT through the internal agent bridge (IPC socket). 

The Gateway config has:
```yaml
platforms:
  api_server:
    extra:
      host: 0.0.0.0    # network-accessible → requires auth
      port: 8642
    key: ''             # empty string → fails auth check despite bypass code
```

The `key` field at `platforms.api_server.key` is read by the API server constructor as `extra.get("key", os.getenv("API_SERVER_KEY", ""))`. Since `key` sits outside the `extra` dict, the lookup falls through to the env var, which is also unset, yielding empty string `""`. Despite `if not self._api_key: return None` in `_check_auth()`, the server returns 401 on non-health endpoints when bound to `0.0.0.0`.

## Diagnostic Steps

```bash
# 1. Check which services are running
hermes gateway status
ss -tlnp | grep -E '8642|8648|9119'

# 2. Test health endpoint (will pass even when broken)
curl -s http://127.0.0.1:8642/health

# 3. Test any auth-required endpoint (this is the key test)
curl -s -w "\nHTTP: %{http_code}" http://127.0.0.1:8642/v1/models

# 4. If step 3 returns 200, auth is fine — look elsewhere
#    If step 3 returns 401, API_SERVER_KEY is misconfigured

# 5. Verify config
grep -A6 'api_server:' ~/.hermes/config.yaml | head -10
grep API_SERVER_KEY ~/.hermes/.env || echo "API_SERVER_KEY not set"
```

## Debugging the API Server (Source-Level)

If the config looks correct but the API server still returns 401, the source code being executed may differ from what you see in the file. **Python `.pyc` caching is a known trap** — stale bytecode persists even after editing the source.

### Trap: Stale `__pycache__`/`.pyc` caches

When debugging `gateway/platforms/api_server.py`, the import system may use a pre-compiled `.pyc` from a previous run. This causes your edits (including debug prints) to have zero effect:

```bash
# Clear ALL __pycache__ before restarting the gateway
find ~/Hermes-Agent/gateway -name '__pycache__' -type d -exec rm -rf {} +

# Verify your edit is actually in the module
cd ~/Hermes-Agent && source venv/bin/activate
python3 -c "
import gateway.platforms.api_server as m
import inspect
# Check whether your debug print is present in the loaded source
src = inspect.getsource(m.APIServerAdapter._check_auth)
print('Debug marker present?' , 'YOUR_MARKER' in src)
print('Loaded from:', m.__file__)
"
```

### Technique: Instrument the source with file writes

Rather than relying on `logging.warning()` (which may not route to `gateway.log` during early init), use direct file I/O to trace runtime values:

```python
# Add to the method being debugged:
with open("/tmp/hermes_dbg.log", "a") as _f:
    _f.write("DBG _check_auth: _api_key=%r, not _api_key=%s\n" % (self._api_key, not self._api_key))
```

Then read the file after a test request:

```bash
cat /tmp/hermes_dbg.log
```

Remember to **remove the debug code** and **clear `__pycache__`** once debugging is done.

## Fix

**Option A: Set an API_SERVER_KEY (recommended for 0.0.0.0 bindings)**
```bash
echo "API_SERVER_KEY=$(openssl rand -hex 32)" >> ~/.hermes/.env
hermes gateway restart
```

**Option B: Change host to 127.0.0.1 (no key needed, local-only)**
```bash
hermes config set platforms.api_server.extra.host 127.0.0.1
hermes gateway restart
```

After fixing, verify:
```bash
curl -s http://127.0.0.1:8642/v1/models    # should return 200
```

## Architecture Context

```
Browser ←port 8648→ hermes-web-ui (Node.js)
                         ├── agent bridge (IPC socket) — terminal, kanban, file browser
                         └── proxy → Gateway API Server :8642 — MAIN CHAT
                                         └── AIAgent (full tool access, memory, etc.)
```

The IPC agent bridge creates AIAgent instances but the Web UI's chat-run-socket does NOT use it for chat — it proxies through the external Gateway's API Server. This means:
- Gateway down? → Web UI chat breaks (even though bridge is "ready")
- Gateway API server returns 401? → Web UI chat breaks
- Gateway API server working? → Web UI chat works

The internal agent bridge handles terminal, kanban, and non-chat WebSocket connections.
