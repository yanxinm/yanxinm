# Gateway 升级后日志迁移到 systemd journal

## 症状

`hermes update` 执行后：
- `~/.hermes/logs/gateway.log` 时间戳停滞在升级前
- 新 Gateway 进程运行正常、端口正常，但日志不再更新
- 健康检查脚本读 `gateway.log` 发现"微信/飞书已断开"
- 实际微信/飞书正常连接并响应

## 根因

`hermes update` 后重启 Gateway，新进程将日志写入 **systemd journal** 而非文件。这是 systemd 管理进程时的默认行为——stdout/stderr 被 systemd 捕获进 journal。

## 验证

```bash
# 方法 1：journalctl 查看连接日志
journalctl -u hermes-gateway --no-pager --since "6 hours ago" | grep -E '\[Weixin\]|\[Lark\]'

# 方法 2：确认文件日志已停滞
tail -1 ~/.hermes/logs/gateway.log  # 时间戳停留在升级前
```

## 对健康检查的影响

旧版自检脚本依赖 `grep` 解析 `gateway.log` 文件内容。Gateway 升级后日志迁移，文件内容停滞，自检误报平台断开。

## 修复

健康检查脚本 v5 改为直接用 `journalctl` 查询：

```bash
# 飞书（journal 中标签为 [Lark] 而非 [Feishu]）
journalctl -u hermes-gateway --no-pager --since "6 hours ago" | grep '\[Lark\].*connected'

# 微信（journal 中无显式 Connected 日志，改用进程推断）
is_gateway_running
```

注意：`set -o pipefail` 与 `grep -q` 共用会触发 SIGPIPE 反转判断（见 `pipefail-grep-quiet-sigpipe.md`）。
