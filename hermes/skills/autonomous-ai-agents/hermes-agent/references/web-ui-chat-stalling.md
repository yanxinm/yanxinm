# Web UI 聊天会话停滞（有响应但浏览器不显示）

## 症状

用户在 Web UI 浏览器中发消息后：
- 无任何输出/响应，页面像死机一样
- 后端日志显示消息已被接收并处理完成（`upstream response event: response.completed` + `flushResponseRunToDb`）
- 数据库中的消息计数更新了（messages: 68 → 70）
- 但浏览器前端不显示内容

## 根因

Web UI (v0.5.28) 的 SQLite 数据库存储了会话历史。当 Web UI 进程异常终止后重启（例如 Gateway 被 OOM 杀死、手动 `kill`），**旧会话数据仍然保留在数据库中**。

浏览器端 Socket.IO 连接时会自动恢复（resume）旧会话，但该会话的状态是 `working: false`（已完成），导致：

1. Socket.IO 将浏览器连接到旧会话而非新会话
2. 新消息虽被上游处理并回写到 DB，但前端的 Socket.IO 事件推送失败
3. 浏览器不断重复 re-resume 同一会话（`socket resumed session X (working: false, messages: N)`）

## 诊断流程

```bash
# 1. 看 Web UI 服务端日志 — 是否收到并处理了上游响应
tail -20 ~/.hermes-web-ui/logs/server.log | grep -E "upstream|flushResponseRunToDb|loaded session"

# 2. 看是否有同一 session 被反复 resumne
grep "resumed session" ~/.hermes-web-ui/logs/server.log | tail -5
# 正常情况：不同浏览器会话应有不同 session ID
# 异常情况：不同 socket 始终 resume 同一个旧 session ID

# 3. 看 API Server 是否可用
curl -s -w "\nHTTP %{http_code}" http://127.0.0.1:8642/v1/models
# 如果返回 401 → API Server 需要认证（见 gateway-recovery.md）
```

## 修复

### 方案 A：清除旧会话数据库（推荐 — 100% 有效）

```bash
# 1. 停掉 Web UI
/home/yanxin/.npm-global/bin/hermes-web-ui stop

# 2. 确认端口释放
ss -tlnp | grep 8648 || echo "已释放"

# 3. 删除 SQLite 数据库文件
rm -f ~/.hermes-web-ui/hermes-web-ui.db*

# 4. 重启 Web UI（后台模式）
# 使用 terminal(background=true)
terminal(background=true, command="/home/yanxin/.npm-global/bin/hermes-web-ui start")
sleep 10
curl -s -o /dev/null -w "HTTP %{http_code}" http://127.0.0.1:8648

# 5. 浏览器打开 http://127.0.0.1:8648，用新令牌登录
grep "Auth enabled" ~/.hermes-web-ui/logs/server.log | tail -1
```

### 方案 B：在 Web UI 中点"新建会话"

点击 Web UI 页面左上角的 **"+ New Chat"** 或 **"新建会话"** 按钮，创建一个全新的会话再发消息。有时有效，但如果旧会话在 DB 中被浏览器缓存的 socket 持续 resume，则需方案 A。

### 方案 C：清除数据库后添加 API key 到启动参数

如果 Web UI 需要连接 Gateway 的 API Server 进行认证，确保 API key 已正确设置：

```bash
# 验证 API Server 带 key 是否能通
curl -s -H "Authorization: Bearer $API_SERVER_KEY" http://127.0.0.1:8642/v1/models
# 预期: HTTP 200 + model list
```

## 预防

- Web UI 启用了认证令牌（`Auth enabled — token: <token>`），每次重启后令牌不变（由 DB 持久化），无需重新登录
- 定期清理 Web UI 的会话数据库可以避免数据堆积导致的前后端不同步问题
- 正常关闭（`hermes-web-ui stop` / SIGTERM）不会导致会话数据损坏，但 `kill -9` 可能导致 SQLite WAL 不一致
- **Gateway 端口冲突规避**：Web UI v0.5.28 启动时会主动扫描已有 Gateway 进程（`Scanning profiles for running gateways...` → `default: running (PID: X, port: 8642)`），如果发现 Gateway 已在运行，**跳过启动内嵌 Gateway**，直接连接已有的。因此先启动 Gateway 再启动 Web UI 是安全的。如果先启动 Web UI（启动了自己的内嵌 Gateway），再启动外部 Gateway，会导致端口 8642 绑定冲突。推荐启动顺序：Gateway → Web UI。

## 相关日志路径

| 文件 | 用途 |
|------|------|
| `~/.hermes-web-ui/logs/server.log` | Web UI 主进程日志（Socket.IO、upstream 通讯） |
| `~/.hermes-web-ui/logs/bridge.log` | Agent Bridge 日志（IPC 通讯） |
| `~/.hermes-web-ui/hermes-web-ui.db*` | SQLite 会话数据库（含 WAL 文件） |
| `~/.hermes/logs/gateway.log` | Gateway 日志（API Server 请求） |
