# Web UI 聊天卡死排查指南

## 症状

在 Web UI (hermes-web-ui) 聊天框输入消息后，无任何响应反馈，像死机一样。
消息似乎发送成功（服务端日志有记录），但浏览器不显示 AI 回复。

## 架构简述

```
浏览器 ←Socket.IO→ Web UI Node.js (:8648) 
  ←Agent Bridge(IPC)→ Hermes Agent
  ←upstream HTTP→ Gateway API Server (:8642)
```

Web UI 的 `chat-run-socket` 通过 Socket.IO 接收浏览器的消息，
通过内部 `Agent Bridge`（IPC socket）或 `upstream`（API Server）发送给 Hermes，
响应以 `response.output_text.delta` 事件流式返回浏览器。

## 诊断步骤

### 1. 检查后端是否正常

```bash
# API Server
curl http://127.0.0.1:8642/health          # 应返回 200

# API Server 带 key（host=0.0.0.0 时必须）
curl -H "Authorization: Bearer <API_SERVER_KEY>" http://127.0.0.1:8642/v1/models

# Web UI 自身
curl http://127.0.0.1:8648                  # 应返回 200

# Gateway
hermes gateway status
```

### 2. 检查 Web UI 日志

```bash
tail -100 ~/.hermes-web-ui/logs/server.log
```

关键信号：
- `resumed session X (working: false, messages: N)` — 加载了会话
- `upstream response event: response.created` — 上游收到请求 ✅
- `flushResponseRunToDb: flushed 1 messages` — 响应已写入 DB ✅
- `socket X resumed session Y (working: false, messages: N)` — 反复重连

如果看到 `upstream response event: response.completed` 且 `flushResponseRunToDb`，
说明**后端通讯正常**，问题在前端 Socket.IO 推送。

### 3. 检查 API Server 401 问题

```bash
# 无 key 时非 health 端点返回 401
curl http://127.0.0.1:8642/v1/models
# {"error": {"message": "Invalid API key", ...}} → 401

# 需带上 key
curl -H "Authorization: Bearer <key>" http://127.0.0.1:8642/v1/models
```

### 4. 检查 Agent Bridge

```bash
ls -la /tmp/hermes-agent-bridge.sock  # IPC socket 是否存在
ps aux | grep hermes_bridge           # Agent Bridge 进程是否在运行
```

## 修复方案

### 方案 A：清除旧会话数据（最有效）

```bash
# 1. 停止 Web UI
/home/yanxin/.npm-global/bin/hermes-web-ui stop

# 2. 清空 session 数据库（删除旧卡壳会话）
rm -f ~/.hermes-web-ui/hermes-web-ui.db*

# 3. 重启 Web UI
/home/yanxin/.npm-global/bin/hermes-web-ui start

# 4. 浏览器硬刷新（Ctrl+F5），用新令牌重新登录
grep "Auth enabled" ~/.hermes-web-ui/logs/server.log | tail -1
```

### 方案 B：重启整个 Web UI 进程

```bash
# 1. 杀旧进程
/home/yanxin/.npm-global/bin/hermes-web-ui stop
sleep 3

# 2. 后台启动
# 使用 terminal(background=true) 或
nohup /home/yanxin/.npm-global/bin/hermes-web-ui start > /dev/null 2>&1 &

# 3. 验证
sleep 8
curl -s -o /dev/null -w "%{http_code}" http://127.0.0.1:8648
```

## 预防

- 避免长时间使用同一个 Web UI 会话（会话累积过多消息后容易出问题）
- 定期清空 session DB 或开新会话
- 如果 Web UI 内嵌 gateway 启动失败，确保主 gateway 正在运行
