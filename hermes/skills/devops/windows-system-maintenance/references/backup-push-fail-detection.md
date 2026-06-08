# 备份 Push 失败检测模式

## 问题

GitHub Action / secret-scanning / 网络问题可能导致 `git push` 失败。如果脚本用 `|| true` 静默吞掉错误，用户以为备份成功，实际已中断数日。

## 正确模式（兼容 `set -euo pipefail`）

```bash
# ❌ 错误：吞掉 push 失败
git push origin main 2>&1 | grep -v "^remote:" || true

# ✅ 正确：捕获退出码
PUSH_OUT=$(git push origin main 2>&1) && PUSH_EXIT=0 || PUSH_EXIT=$?

if [ "$PUSH_EXIT" -ne 0 ]; then
    ERROR_MSG=$(echo "$PUSH_OUT" | grep -v "^remote:" | grep -v "^$" | head -5)
    echo "ERROR — push 失败"
    echo "$ERROR_MSG"
    exit 1
fi

echo "OK ($(du -sh ... | cut -f1))"
```

## 为什么 `set -e` 下要用 `&&/||` 模式

`set -e` 在命令返回非零时立即退出脚本。以下写法会提前退出：

```bash
PUSH_EXIT=0
PUSH_OUT=$(git push origin main 2>&1)   # 如果失败，set -e 会在这里杀死脚本
PUSH_EXIT=$?                             # 这行永远不会执行
```

`&& CMD || CMD2` 模式被 shell 识别为「条件执行」，不影响 `set -e`：

```bash
PUSH_OUT=$(cmd) && EXIT=0 || EXIT=$?   # ✅ set -e 允许这种写法
```

## 常见失败原因

| 原因 | 错误特征 |
|------|---------|
| GitHub Push Protection | `remote: error: GH013: Repository rule violations` + secret 路径 |
| 网络断连 | `ssh: connect to host github.com port 22: Connection timed out` |
| 认证过期 | `git@github.com: Permission denied (publickey)` |
| SSH 慢连接 | 长时间无输出后超时（可加 `GIT_SSH_COMMAND="ssh -o ConnectTimeout=10"`） |

## Push Protection 修复步骤

1. 从报错信息中找到触发扫描的文件路径和密钥
2. 删除源文件中的密钥原文（改为「见 .env 配置」）
3. 重新执行备份（生成干净 commit）
4. 如果旧 commit 仍在历史中 → `git reset --hard <last-good-commit>` → 重新备份 → 正常 push。**不可直接 force push**，因为 GitHub 拒绝包含密钥的整个历史
