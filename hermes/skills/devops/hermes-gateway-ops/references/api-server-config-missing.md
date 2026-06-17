# API Server 0.0.0.0 配置丢失/回退诊断

## 症状

- `ss -tlnp` 显示 `127.0.0.1:8642` 而非 `0.0.0.0:8642`
- 笔记本 Tailscale IP 访问 `http://100.x.x.x:8642/health` 超时
- Dashboard 显示"网关启动失败"
- Web UI 能打开但 API 不通

## 诊断步骤

```bash
# 1. 确认当前绑定
ss -tlnp | grep 8642
# 期望: 0.0.0.0:8642
# 实际: 127.0.0.1:8642 ← 问题

# 2. 检查哪个 profile 在用
hermes config path
# 输出当前活跃 profile 的 config.yaml 路径

# 3. 检查 default profile 是否有 api_server 段
grep -A5 'api_server' ~/.hermes/config.yaml
# 如果没有输出 → 完全缺失！

# 4. 检查其他 profile
grep -A5 'api_server' ~/.hermes/profiles/*/config.yaml
# 可能发现只有 jike/profile 有配置
```

## 根因

两种可能：

### A. `hermes config set` 写到错误 profile
```bash
# 当前活跃 profile = jike
hermes config set platforms.api_server.extra.host 0.0.0.0
# 写入 ~/.hermes/profiles/jike/config.yaml ❌

# Gateway 读取的是 ~/.hermes/config.yaml（default）
# → default 中无 api_server 配置 → 回退到 127.0.0.1
```

修复：
```bash
hermes -p default config set platforms.api_server.extra.host 0.0.0.0
```

### B. Default config 完全缺失 platforms.api_server 段
`hermes config set` 无法创建嵌套段结构。此时需直接编辑 config.yaml：

```bash
# 在 plugins: 前插入
sed -i '/^plugins:/i\
platforms:\
  api_server:\
    extra:\
      host: 0.0.0.0\
      port: 8642\
    key: hermes-fix-2026' ~/.hermes/config.yaml
```

## 修复后验证

```bash
# 重启 Gateway
kill $(pgrep -f "hermes gateway run")  # systemd 自动拉起
sleep 15

# 确认绑定
ss -tlnp | grep 8642  # → 0.0.0.0:8642 ✅

# Tailscale 验证
curl -s http://100.x.x.x:8642/health  # → {"status":"ok"}
```

## 预防

自检脚本增加端口绑定地址检测（不仅是端口是否监听）：
```bash
ss -tlnp | grep 8642 | grep -q '0.0.0.0' || echo "WARNING: API bound to localhost only"
```
