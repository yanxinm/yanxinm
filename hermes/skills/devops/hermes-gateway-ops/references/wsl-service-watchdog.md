# WSL Service Watchdog Reference

## TDAI Gateway EPIPE Crash — Root Cause

### Symptom
WeChat/Feishu channels go offline. Gateway logs show:
```
Error: write EPIPE
    at Socket._writeGeneric (node:net:971:11)
Emitted 'error' event on Socket instance at:
    at Socket.onerror (node:internal/streams/readable:1026:14)
    at emitErrorNT (node:internal/streams/destroy:170:8)
```

### Cause Chain
1. Hermes Agent bridge IPC socket (`/tmp/hermes-agent-bridge.sock`) gets recreated
   - Triggered by: config changes, gateway restart, new session launch
2. TDAI Gateway (Node.js) holds a stale file descriptor to the OLD socket
3. Next write to the stale socket → EPIPE → unhandled error → process crash
4. Port 8420 stops listening → WeChat/Feishu offline

### Why TDAI Gateway Is Vulnerable
- Node.js `console.debug()` writes to the IPC socket synchronously
- No `'error'` event handler on the socket
- Hermes Agent bridge can restart independently (config change, session spawn)
- No reconnection logic in the gateway

### The Watchdog Fix
A cron-based health check (every 2 minutes) that:
1. Checks `ss -tlnp | grep ':8420 '` — if silent, restart
2. Checks `pgrep -f 'hermes gateway run'` — if missing, restart
3. Exits silently when healthy

## CLIProxyAPI Setup Notes

### Installation via ghproxy (China-friendly)
```bash
# Download from GitHub Releases via ghproxy mirror
curl -sL "https://ghproxy.net/https://github.com/router-for-me/CLIProxyAPI/releases/download/v7.1.17/CLIProxyAPI_7.1.17_linux_amd64.tar.gz" -o cliproxyapi.tar.gz
tar xzf cliproxyapi.tar.gz
cp cli-proxy-api ~/.local/bin/
chmod +x ~/.local/bin/cli-proxy-api
```

### Configuration
```yaml
# ~/.cli-proxy-api/config.yaml
host: "127.0.0.1"
port: 8317
auth-dir: "~/.cli-proxy-api"
api-keys:
  - "sk-test-key"
```

### OAuth Login (Gemini/Codex/Claude)
```bash
cli-proxy-api -login -no-browser -config ~/.cli-proxy-api/config.yaml
```
The `-no-browser` flag prints a URL to stdout instead of opening a browser (needed in WSL). User opens the URL in Windows browser, completes OAuth, pastes the code back.

### Models Available Through CLIProxyAPI
After OAuth login, available models include Gemini 2.5 Pro, Gemini 2.5 Flash, GPT-5 Codex, Claude Sonnet 4, etc. — whatever the user's subscription covers.

## Provider Diagnostics Quick Reference

### NVIDIA NIM
- Endpoint: `https://integrate.api.nvidia.com/v1`
- Not all listed models are accessible — test with a known-good model first
- Verified working: `meta/llama-3.1-8b-instruct`, `google/gemma-2-2b-it`
- 404 with "Function not found for account" = key lacks access to that model
- List available models: `curl -s <base_url>/v1/models -H "Authorization: Bearer <key>"`
- Model `01-ai/yi-large` → 404 (no access)

### apikey.fun (Relay)
- Endpoints: `https://api.apikey.fun/v1` (general) / `https://slb.apikey.fun/v1` (专线直连)
- Has ~22 models including: gpt-5.5, gpt-5.4, gpt-4o (vision), gpt-image-2, gpt-image-1.5
- Latency: 1.8-7s per request (relay overhead to OpenAI US servers)
- Vision test: `gpt-4o` works with base64 image input
- Image generation: `gpt-image-2` works (returned 1.6MB, response_format: b64_json)
- Image generation timeout: needs ~120s for first run
- Cold start after idle: ~6-7s first request
- Default relay is slower than dedicated line (`slb.apikey.fun`)

### Doubao Seedream (Ark/火山引擎)
- Endpoint: `https://ark.cn-beijing.volces.com/api/v3`
- Image generation models: `doubao-seedream-4-5-251128`, `doubao-seedream-5-0-260128`
- Minimum output size: 3,686,400 pixels (1920×1920)
- Minimum input size for img2img: same (auto-resize in script)
- API key from `~/.hermes/.env` → `ARK_IMAGE_API_KEY`
- Text model: `doubao-seed-1-6-vision-250815` (also handles vision)
- Text backup: `doubao-seed-2-0-pro-260215`

### Hermes Gateway Logs
- Gateway log: `/home/yanxin/.hermes/logs/gateway.log`
- TDAI Gateway log: `/tmp/tdai-gw.log`
- Watchdog log: `/tmp/hermes-watchdog.log`
- Gateway state: `/home/yanxin/.hermes/gateway_state.json` (JSON with platform status)
