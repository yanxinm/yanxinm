# Gateway 崩溃模式与检测（2026-05-24 会话记录）

## 症状

检查时发现：
- `hermes gateway status` 返回 `✓ Gateway is running (PID: 39)`
- 但 `ps aux` 确认 PID 39 已不存在
- `send_message` 返回 `success=true`，但消息未实际送达
- gateway.log 最后时间戳停滞在数分钟前（00:09:19）
- Web UI (8648) 和 Dashboard (9119) 端口无监听

## 根因推测

Gateway 在 00:09 启动后约 20 秒内完成了 3 个平台连接，随后在 00:09:19 左右崩溃。
exit-diag.log 无错误信息 — 崩溃可能发生在 Python 日志刷盘前。

## 检测方法

```bash
# 1. 检查进程实际存活
hermes gateway status
ps aux | grep 'hermes gateway' | grep -v grep

# 2. 检查日志最后时间戳
tail -1 ~/.hermes/logs/gateway.log

# 3. 检查所有关键端口
ss -tlnp | grep -E '8420|8648|9119'

# 4. 验证 send_message 实际送达
send_message target=weixin:USER_ID message="test"
sleep 5
tail -5 ~/.hermes/logs/gateway.log | grep 'Sending response'
```

## 小窍门

- `send_message` 返回 `success=true` + `mirrored=true` 并不意味着消息已发到微信/飞书
- 唯一的确认方式是 gateway.log 中出现 `[Weixin] Sending response` 条目
- Gateway 重启后需要等 15-20 秒让所有平台完成 WebSocket 握手
