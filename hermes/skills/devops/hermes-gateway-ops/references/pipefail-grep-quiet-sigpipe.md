# `set -o pipefail` + `grep -q` 导致 SIGPIPE 反向判断

## 问题

在 `set -o pipefail` 的 shell 脚本中：

```bash
set -o pipefail
if journalctl -u myservice | grep -q 'pattern'; then
    echo "FOUND"
else
    echo "NOT FOUND"  # ← 明明有匹配却走这里
fi
```

输出 `NOT FOUND`，但实际上日志中存在匹配行。

## 根因

1. `grep -q` 找到第一个匹配后**立即退出**
2. grep 退出关闭管道 → `journalctl` 收到 **SIGPIPE** (信号 13)
3. `set -o pipefail` 下，pipeline 的退出码取**最后一个失败进程**的退出码
4. journalctl 退出码 = 128 + 13 = **141**（非零）
5. `if` 把 141 当作 false → 走 else 分支

```bash
# 验证
set -o pipefail
echo "match" | grep -q match
echo $?  # 0 — 没问题（echo 不触发 SIGPIPE）

journalctl -u someservice | grep -q 'pattern'
echo $?  # 141 — journalctl 被 SIGPIPE
```

## 修复

三种方式：

```bash
# 方式 A：拆 pipeline（推荐 — 最清晰）
matches=$(journalctl -u myservice | grep 'pattern')
if [ -n "$matches" ]; then ...

# 方式 B：避免 -q，用 head 吸收 SIGPIPE
if journalctl -u myservice | grep 'pattern' | head -1 | grep -q .; then ...

# 方式 C：关闭 pipefail（粗暴）
set +o pipefail
```

## 实战案例

2026-06-13：健康检查脚本 v4 中飞书检测：
```bash
# ❌ 原始（SIGPIPE 反转）
if journalctl -u hermes-gateway --since "6 hours ago" | grep -q '\[Lark\].*connected'; then

# ✅ 修复
if journalctl -u hermes-gateway --since "6 hours ago" | grep '\[Lark\].*connected' | head -1 | grep -q .; then
```

明明 journal 中有 2 条 `[Lark] ... connected` 日志，却报"无最近连接日志"。
