# Hermes Desktop JSON-RPC end-to-end probe

Use when Desktop reports “提示词发送失败”, “网关断开”, or “代理 1 个失败” while Dashboard/Gateway ports look healthy.

## Key lesson

Do **not** stop at these checks:

- `curl /api/status` returns `200`
- WebSocket handshake returns `101 Switching Protocols`
- `model.options` returns a response
- CLI `hermes chat -q` returns `OK`

Those prove only partial health. Desktop can still fail at the actual TUI Gateway protocol path.

## Required verification shape

A real Desktop-path probe must run this sequence over `/api/ws`:

1. Fetch Dashboard HTML and extract `__HERMES_SESSION_TOKEN__`.
2. Connect `wss://<host>/api/ws?token=<token>`.
3. Receive `gateway.ready` event.
4. Send JSON-RPC `session.create`.
5. Capture returned `session_id`.
6. Send JSON-RPC `prompt.submit` with that `session_id`.
7. Observe stream frames, especially `message.delta` / `message.complete`.

If this sequence returns model text, the server-side Desktop path is working. Remaining failures are usually Desktop client local state/cache/version/backend-address configuration, not Gateway/Dashboard service health.

## Minimal frame sequence

```json
{"jsonrpc":"2.0","id":1,"method":"session.create","params":{"cols":120,"close_on_disconnect":false}}
```

Then:

```json
{"jsonrpc":"2.0","id":2,"method":"prompt.submit","params":{"session_id":"<sid>","text":"只回答 OK"}}
```

Expected frames:

- `{"type":"gateway.ready", ...}` immediately after connect
- `{"id":1,"result":{"session_id":"..."}}`
- `{"id":2,"result":{"status":"streaming"}}`
- `message.delta` containing `OK`
- `message.complete`

## Diagnostic interpretation

| Probe result | Meaning | Next action |
|---|---|---|
| `/api/status` fails | Dashboard/serve problem | Restart or repair 9119 service/Funnel |
| WS handshake fails | network/token/Funnel problem | Check token, `tailscale serve`, `--host 0.0.0.0 --insecure` |
| `model.options` fails | TUI Gateway protocol problem | Inspect `tui_gateway.ws` and `errors.log` |
| `session.create` succeeds but `prompt.submit` fails | agent/session/model path problem | Inspect `tui_gateway.server`, model config, MCP startup, session DB |
| Full probe returns `OK` but Desktop fails | Desktop local state/cache/version/backend config | Fully quit Desktop, clear local connection state, try LAN URL `http://192.168.1.42:9119`, or reinstall/update Desktop |

## Log signatures

Useful errors:

```text
WARNING tui_gateway.ws: ws send failed ... WebSocketDisconnect
WARNING tui_gateway.ws: ws response send failed ... method=model.options
ERROR tui_gateway.ws: ws ready frame send failed
```

These mean the server accepted the socket but the client disconnected while the server was sending. If the full JSON-RPC probe succeeds from another client, treat it as a Desktop-client-side issue.

## Related pitfalls

- `hermes-dashboard.service` may auto-start a random-token Dashboard and occupy `9119`; verify the real port owner with `ss -tlnp` and inspect `/proc/$PID/environ` for `HERMES_DASHBOARD_SESSION_TOKEN` before blaming Desktop.
- Comparing the static SPA HTML token to a fixed token file can mislead; prefer functional verification (`session.create` + `prompt.submit`) over token string comparisons.
- A watchdog that only checks `200`/`101` can keep the service alive but still miss Desktop-specific send failures.
