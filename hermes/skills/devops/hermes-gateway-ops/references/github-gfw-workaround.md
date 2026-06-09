# GitHub 被墙时的替代下载方案

## 问题

`git clone https://github.com/...` 超时 —— `github.com` 直连不通，但 `api.github.com` 和 `codeload.github.com` 通常可达。

## 诊断

```bash
# 检测连通性
curl -s -o /dev/null -w "%{http_code} %{time_total}s\n" --connect-timeout 10 https://github.com
curl -s -o /dev/null -w "%{http_code} %{time_total}s\n" --connect-timeout 10 https://api.github.com
# github.com 返回 000 → 被墙
# api.github.com 返回 200 → 可用
```

## 方案一：tarball 下载（推荐，无需登录）

```bash
# 通过 API 获取源码 tarball
curl -L --connect-timeout 30 -o repo.tar.gz \
  "https://api.github.com/repos/<owner>/<repo>/tarball/<branch>"

# 解压（tarball 包含 owner-repo-commit 前缀目录）
mkdir <repo> && tar -xzf repo.tar.gz -C <repo> --strip-components=1
```

网速较慢时（~100KB/s），大仓库用后台下载：
```bash
# terminal(background=true, notify_on_complete=true)
curl -L --connect-timeout 30 -o /tmp/repo.tar.gz \
  "https://api.github.com/repos/<owner>/<repo>/tarball/main"
```

完成后验证：
```bash
ls -lh /tmp/repo.tar.gz
tar -tzf /tmp/repo.tar.gz | head -5
```

## 方案二：git 全局代理（推荐，一劳永逸）

**最佳方案：`git insteadOf` 自动路由所有 GitHub 请求走镜像**，无需每次手动加前缀。

```bash
# 先测哪个镜像可用
for url in https://ghproxy.net https://ghproxy.com https://gh.con.sh; do
  echo -n "$url → "; curl -s -o /dev/null -w "%{http_code} %{time_total}s" --connect-timeout 5 "$url"; echo
done

# 配置全局代理（选可用的镜像）
git config --global url."https://ghproxy.net/https://github.com/".insteadOf "https://github.com/"
```

配置后所有 `git clone https://github.com/xxx` 自动变为 `git clone https://ghproxy.net/https://github.com/xxx`，包括 `hermes update` 等内部 git 操作。

验证：
```bash
git config --global --list | grep insteadOf
# 预期：url.https://ghproxy.net/https://github.com/.insteadof=https://github.com/
```

取消：
```bash
git config --global --unset url."https://ghproxy.net/https://github.com/".insteadOf
```

**可用镜像池（2026-06-08 实测）：**
| 镜像 | 状态 |
|------|------|
| ghproxy.net | ✅ 可用（200 OK, ~1.2s） |
| ghproxy.com | ❌ 超时（频繁故障） |
| gh.con.sh | ⚠️ 302 重定向 |
| mirror.ghproxy.com | ❌ 超时 |

## 方案三：传统 git 代理（HTTP proxy）

如果基地配置了 HTTP 代理：
```bash
git config --global http.proxy http://127.0.0.1:<port>
git config --global https.proxy http://127.0.0.1:<port>
```

取消代理：
```bash
git config --global --unset http.proxy
git config --global --unset https.proxy
```

## 方案四：镜像站直链（手动加前缀）

临时使用（不推荐长期手动操作）：

```bash
git clone https://ghproxy.net/https://github.com/<owner>/<repo>.git
```

> 推荐用方案二 `insteadOf`，一次配置永不再管。

## 陷阱

- `--depth 1` 浅克隆走的是 git 协议（github.com），同样被墙，不解决问题
- tarball 下载走 api.github.com，与 git clone 走不同域名
- 下载速度可能很慢（100KB/s 以下），大仓库需要 1-2 分钟
- tarball 不包含 .git 目录，无法做 git 操作

## Git Push 特别说明（2026-06-08 实测）

即使 `ghproxy.net` 的 HTTPS 代理对网页和 API 返回 200 OK，**git push 仍可能失败**：
- `git push` 使用 git smart HTTP 协议（`git-upload-pack`），与普通 HTTPS GET 走不同路径
- 即使 `insteadOf` 代理生效，fetch-pack 在传输数据包时会 `unexpected disconnect`
- SSH 端口 443（`ssh.github.com:443`）同样被 DPI 阻断

**灾备脚本应对：** 见 §十二 每日灾备——网络不通时自动退化为本地 tar 备份，不阻塞 cron。有网时 git push 自动恢复。
