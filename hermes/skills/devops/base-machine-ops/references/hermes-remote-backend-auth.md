# Hermes Remote Backend — 认证架构

## 中间件链（web_server.py）

请求穿过 Python Dashboard 时会依次经过：

```
1. host_header_middleware (line 325)
   → 检查 Host header 是否匹配 bound_host
   → 0.0.0.0 绑定接受任何 Host；127.0.0.1 只接受 localhost

2. _dashboard_auth_gate (line 364)
   → OAuth gate，仅当 auth_required=True 时激活
   → auth_required = should_require_auth(host, allow_public)
   → loopback bind: False; non-loopback + --insecure: False; non-loopback without --insecure: True

3. auth_middleware (line 370)
   → Session token 校验
   → 当 auth_required=True 时 SKIP（由 OAuth gate 接管）
   → 当 auth_required=False 时，检查 /api/ 路由的 X-Hermes-Session-Token 或 Authorization: Bearer
```

## Session Token

```python
# web_server.py line 183
_SESSION_TOKEN = os.environ.get("HERMES_DASHBOARD_SESSION_TOKEN") or secrets.token_urlsafe(32)
```

两种传法：
- `X-Hermes-Session-Token: <token>`
- `Authorization: Bearer <token>`

Token 注入到 Dashboard HTML（SPA 自动获取），但通过 Node SPA 代理时会丢失。

## 为什么 Funnel → Node(8648) → Python(9119) 返回 401

Node SPA server (`hermes-web-ui/dist/server/index.js`) 作为反向代理时不转发 `X-Hermes-Session-Token` 请求头。
因此即使 Funnel URL 能访问 SPA 页面，API 调用也会被 `auth_middleware` 拒绝。

## 解决方案：Funnel 直连 Python Dashboard

```
Funnel → 127.0.0.1:9119 (Python Dashboard, --insecure --host 0.0.0.0)
```

- `--host 0.0.0.0` 使 `host_header_middleware` 接受 Funnel 的 Host header
- `--insecure` 使 `should_require_auth` 返回 False
- `HERMES_DASHBOARD_SESSION_TOKEN` 固化 token
- Desktop 客户端通过 `X-Hermes-Session-Token` header 认证
