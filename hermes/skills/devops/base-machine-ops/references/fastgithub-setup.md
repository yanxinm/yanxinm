# FastGithub 部署记录

## 版本选择

| 版本 | 来源 | 状态 | 说明 |
|------|------|------|------|
| v2.1.5 | creazyboyone/fastgithub (GitHub) | ❌ 崩溃 | `ProductionVersion.Parse` 抛出 `IndexOutOfRangeException`，核心转储 |
| v2.1.4-repaired | XingYuan55/FastGithub (Gitee) | ✅ 可用 | 修复了 Linux 启动后异常停止的问题 |

## 崩溃根因

v2.1.5 的 `ProductionVersion.Parse(string productionVersion)` 在解析程序集版本时越界：
```
System.TypeInitializationException: The type initializer for 'FastGithub.ProductionVersion' threw an exception.
 ---> System.IndexOutOfRangeException: Index was outside the bounds of the array.
   at FastGithub.ProductionVersion.Parse(String productionVersion)
```

v2.1.4 正常启动后输出：
```
FastGithub启动完成，当前版本为v2.1.4
```

## 代理行为

启动后：
- HTTP 代理端口：`127.0.0.1:38457`
- dnscrypt-proxy 会一起启动（失败不影响 HTTP 代理功能）
- CA 证书自动生成在 `~/fastgithub/cacert/`
- 首次启动有短暂延迟（~1s），之后所有 GitHub 请求自动走代理

## systemd 问题

v2.1.4 的 `fastgithub start` 命令会安装 systemd 服务，但 `ExecStart` 进程在 systemd 下核心转储（服务端启动后立即 ABRT）。在 shell 前台/后台运行正常。

建议用 cron @reboot + nohup 替代 systemd。

## Git 代理配置

```bash
git config --global http.proxy http://127.0.0.1:38457
git config --global https.proxy http://127.0.0.1:38457
git config --global http.sslverify false
```

## Desktop 远程后端（办公室网络）

办公室网络特性：
- Funnel URL 浏览器可达，Desktop WebSocket 404
- Tailscale 直连 IP `http://100.86.13.11:9119` 可替代 Funnel
- Funnel 映射 Dashboard(9119)，不是 WebSocket 端点，Desktop 连接失败
