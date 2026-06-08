# send_message 假阳性陷阱（2026-05-24 会话记录）

## 现象

执行 `send_message` 后返回：
```json
{"success": true, "message_id": "hermes-weixin-xxx", "mirrored": true}
```

但微信端**实际未收到任何消息**。

## 根因

Gateway 进程早已崩溃（PID 已不存在），但 `send_message` 工具仍返回 `success=true`。

**为什么？** 可能原因：
- send_message 通过 Unix socket 或 HTTP 连接到 Gateway 的过期文件描述符
- 连接失败后工具返回了进程内部缓存/默认值而非真实结果
- Gateway API server (8642) 可能仍残留僵尸响应

## 完整验证流程

这是最可靠的"三层验证法"：

```python
# 第1层 — 确认 Gateway 进程存活
# shell: hermes gateway status
# → "✓ Gateway is running (PID: XXX)" 是必要条件

# 第2层 — 发送测试消息
# shell: send_message target=weixin:USER message="test"
# → success=true 是必要条件但不是充分条件

# 第3层 — 确认送达日志
# shell: tail -5 ~/.hermes/logs/gateway.log | grep 'Sending response'
# → "[Weixin] Sending response (N chars) to USER_ID" 是唯一确认
```

**重要：第2层的 success 不能替代第3层。三步必须全部执行，缺一不可。**

## 检测 Gateway 实际存活的方法

```bash
# 方法1：CLI 命令
hermes gateway status

# 方法2：检查进程
ps aux | grep 'hermes gateway' | grep -v grep

# 方法3：检查日志新鲜度
tail -1 ~/.hermes/logs/gateway.log
# 时间戳应在最近几分钟内

# 方法4：检查端口场景
ss -tlnp | grep -E '8420|8648|9119'
# Gateway 本身不暴露 HTTP 端口，但其他服务在以下端口
# TDAI Memory: 8420
# Web UI: 8648
# Dashboard: 9119
```

## 教训

- 永远不要仅凭 `send_message` 的返回值判断消息送达
- Gateway 可能在上秒 running、下秒 dead
- 日志中的 `Sending response` 条目是唯一的金标准
