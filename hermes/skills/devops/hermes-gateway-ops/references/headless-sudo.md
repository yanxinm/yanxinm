# Headless Sudo 配置

## 场景

无显示器 Linux 主机上，Hermes Agent 通过 terminal 工具执行需要 sudo 的命令（安装软件、重启服务等）。默认 sudo 要求交互式终端输入密码，而 Agent 运行在非交互环境中。

## 解决方案：SUDO_PASSWORD 环境变量

在 `~/.hermes/.env` 中设置 `SUDO_PASSWORD`，Hermes 的 terminal 工具会自动读取并注入 sudo 命令：

```bash
echo 'SUDO_PASSWORD=<your-password>' >> ~/.hermes/.env
```

**⚠️ 注意：** `sudo -S` 管道方式（`echo password | sudo -S cmd`）被 Hermes 的安全策略拦截。只有 `.env` 中的 `SUDO_PASSWORD` 会被 terminal 工具自动使用。

**⚠️ `.env` 受保护：** 直接 `echo >> .env` 需要用户审批。`hermes auth add` 是写入 `.env` 的更安全路径，但不支持 SUDO_PASSWORD（仅限 API key 类字段）。

## 验证

```bash
sudo apt update 2>&1 | tail -3
# 应该不需要密码直接执行
```

## 安全注意

- SUDO_PASSWORD 以明文存在 `.env` 中
- `.env` 文件权限为 600（仅 owner 可读写）
- 建议使用专门的服务账号而非主用户账号
- 生产环境可考虑配置 `NOPASSWD` sudoers 规则替代密码存储
