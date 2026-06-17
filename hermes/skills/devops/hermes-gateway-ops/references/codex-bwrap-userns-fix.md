# Codex 沙箱权限修复

## 症状

Codex CLI 启动时显示警告：
```
⚠ Needs access to create user namespaces
```

实际使用时报：
```
INIT {"success": false, "error": {"code": "unknown_command", "message": "Unknown command."}}
stream disconnected before completion: No available accounts
```

## 诊断

```bash
# 测试 bubblewrap 能否创建沙箱
bwrap --ro-bind / / /bin/true 2>&1
# 输出: bwrap: setting up uid map: Permission denied

# 检查 AppArmor 限制
cat /proc/sys/kernel/apparmor_restrict_unprivileged_userns
# 输出: 1  ← 限制已启用
```

## 修复

```bash
# 立即生效
sudo sysctl -w kernel.apparmor_restrict_unprivileged_userns=0

# 持久化
echo 'kernel.apparmor_restrict_unprivileged_userns=0' | sudo tee /etc/sysctl.d/99-codex.conf

# 验证
cat /proc/sys/kernel/apparmor_restrict_unprivileged_userns  # → 0
bwrap --ro-bind / / /bin/true 2>&1  # → bwrap OK
```

## 注意

Ubuntu 22.04+ 默认为安全启用此限制。在 headless 服务器上不存在 GTK/显示问题（与 echobird 崩溃无关）。

## OAuth 认证（headless 环境）

Codex 依赖 echobird 本地中继做 OAuth 认证。无头环境重新认证方法：

```bash
# 用 API key 重新认证
python3 -c "import json; print(json.load(open('$HOME/.codex/auth.json'))['OPENAI_API_KEY'])" | codex login --with-api-key
```
