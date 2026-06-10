# Hermes Desktop over Tailscale/Funnel — Dashboard 可打开但提示词发送失败

## 适用场景

- 浏览器能打开 `https://<node>.<tailnet>.ts.net` 且是 Hermes Dashboard。
- Desktop 显示已连接，但发送提示词失败。
- 模型 CLI 实发正常，问题不在 provider。
- 用户在单位/家里/手机热点间切换网络后表现不同。

## 关键结论

Hermes Desktop/Chat 的“发送提示词”不是普通 HTTP 请求，而是 Dashboard 的 WebSocket 通道：

- HTTP 健康检查：`/api/status` → 期望 `200`
- 发送通道：`/api/ws?token=...` → 期望 WebSocket 握手 `101 Switching Protocols`

因此“网页能打开”只证明 HTTP 入口通，不能证明提示词能发送。

## 验收顺序

1. 确认 Funnel 根路径没有被 HA 或其他服务抢占：
   ```bash
   tailscale serve status
   curl -sS -o /tmp/hermes_status.json -w '%{http_code}\n' \
     https://miao-thinkcentre-m710q-n080.tail589fe7.ts.net/api/status
   ```
2. 确认模型本身能实发：
   ```bash
   /home/miao/.hermes/hermes-agent/venv/bin/hermes chat \
     -q '只回答 OK' --provider custom:apikey-fun -m gpt-5.5 --toolsets safe
   ```
3. 确认 WebSocket 握手：
   ```bash
   python3 - <<'PY'
   import re, urllib.request, socket, ssl, base64, os, urllib.parse
   host='miao-thinkcentre-m710q-n080.tail589fe7.ts.net'
   html=urllib.request.urlopen('https://'+host+'/', timeout=10).read().decode('utf-8','ignore')
   token=re.search(r'__HERMES_SESSION_TOKEN__\\s*=\\s*["\\']([^"\\']+)', html).group(1)
   key=base64.b64encode(os.urandom(16)).decode()
   raw=socket.create_connection((host,443),timeout=10)
   raw=ssl.create_default_context().wrap_socket(raw,server_hostname=host)
   path=f'/api/ws?token={urllib.parse.quote(token)}'
   req=f'GET {path} HTTP/1.1\\r\\nHost: {host}\\r\\nUpgrade: websocket\\r\\nConnection: Upgrade\\r\\nSec-WebSocket-Key: {key}\\r\\nSec-WebSocket-Version: 13\\r\\nOrigin: https://{host}\\r\\n\\r\\n'
   raw.sendall(req.encode())
   print(raw.recv(300).decode('latin1','ignore').splitlines()[0])
   raw.close()
   PY
   ```

## 判断规则

| 结果 | 判断 |
|---|---|
| `/api/status=200`，`/api/ws=101`，CLI 模型 OK | 基地端/Funnel/模型正常，问题在 Desktop 客户端缓存或本地网络拦 WebSocket |
| `/api/status=200`，`/api/ws` 非 101 | Dashboard WebSocket/token/Host-Origin 检查有问题 |
| 根页面显示 HA | Funnel 根路径被 HA 抢占或浏览器 Service Worker 缓存了旧 HA 前端 |
| 手机热点可用、单位网不可用 | 单位网络/代理/DPI 拦 WebSocket 或 Tailscale/MagicDNS 干扰 |

## 老缪基地的地址策略

长期默认给 Desktop 填 Funnel 根域名：

```text
https://miao-thinkcentre-m710q-n080.tail589fe7.ts.net
```

家里局域网排障时可临时用：

```text
http://192.168.1.42:9119
http://100.86.13.11:9119
```

不要把 Desktop 指向：

- `8642`：这是 Gateway API，不是 Desktop 用的 Dashboard。
- `8123` 或 `/ha`：这是 Home Assistant。

## 重要坑

- HA 不要再挂 Hermes 的 Funnel 根域名 `/`，否则 Desktop 和 HA 会互抢。
- 若浏览器仍显示 Home Assistant，但服务端 curl 根页面是 Hermes，多半是 HA Service Worker 缓存；先强刷/清缓存/无痕窗口，不要急着改路由。
- Dashboard 重启后 session token 会变化；Desktop 若复用旧窗口/旧缓存，可能继续发送失败。先完全退出 Desktop 后重开。
