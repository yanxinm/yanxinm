# API Server 配置丢失诊断（2026-06-11 实战）

## 症状

- Dashboard 显示"网关启动失败"
- `ss -tlnp | grep 8642` 显示 `127.0.0.1:8642`（应该是 `0.0.0.0:8642`）
- 笔记本 Tailscale IP `http://100.x.x.x:8642/health` 超时
- 微信/飞书正常（Gateway 本身在跑，只是 API Server 绑定错误）

## 诊断路径

```bash
# 1. 查端口绑定
ss -tlnp | grep 8642
# 输出: 127.0.0.1:8642 → 绑定错误，应该是 0.0.0.0

# 2. 查当前活跃 profile（关键！）
hermes config path
# 输出: /home/miao/.hermes/profiles/jike/config.yaml
# → 活跃 profile 不是 default！

# 3. 查 default config 中 api_server 配置
grep -n 'api_server' /home/miao/.hermes/config.yaml
# 无输出 → 配置段完全缺失

# 4. 查其他 profile 的 config 作为参考
grep -A6 '^platforms:' /home/miao/.hermes/profiles/jike/config.yaml
# 有正确的 api_server 配置模板
```

## 根因链

```
活跃 profile = jike（通过 dashboard --open-profile jike 设置）
    ↓
hermes config set → 写入 jike 的 config.yaml
    ↓
Gateway 读的是 default config.yaml
    ↓
default config 中 platforms.api_server 段完全不存在
    ↓
Gateway 回退到默认值 127.0.0.1
```

## 修复

### 方法 A：用 hermes config set（需指定 profile）

```bash
hermes -p default config set platforms.api_server.extra.host 0.0.0.0
hermes -p default config set platforms.api_server.extra.port 8642
```

⚠️ 但如果 `platforms:` 段本身不存在，config set 可能不会创建它。用方法 B 更可靠。

### 方法 B：直接写入 config.yaml

```bash
sed -i '/^plugins:/i\
platforms:\
  api_server:\
    extra:\
      host: 0.0.0.0\
      port: 8642\
    key: hermes-fix-2026' /home/miao/.hermes/config.yaml
```

### 修复后重启

```bash
# 杀旧进程，systemd 自动拉起新进程（带新配置）
pkill -9 -f "hermes.*gateway run"
sleep 15
# 验证
ss -tlnp | grep 8642  # 应显示 0.0.0.0:8642
curl -s http://100.86.13.11:8642/health  # 应返回 200
```

## 预防

在自检脚本中增加绑定地址检测（不仅是端口是否监听）：

```bash
# 检查 8642 是否绑定到 0.0.0.0（而非 127.0.0.1）
if ss -tlnp | grep ':8642' | grep -q '0.0.0.0'; then
    echo "✅ API Server 绑定 0.0.0.0"
else
    echo "❌ API Server 绑定错误（127.0.0.1），远程不可达"
fi
```
