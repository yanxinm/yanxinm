# WSL 内存与 Swap 配置指南

## 问题

WSL2 默认无 swap，当内存耗尽时内核 OOM killer 随机杀进程。
常见的受害者包括：Hermes Gateway（进程消失无 traceback）、hindsight-api daemon。

## 解决方案：创建 `.wslconfig`

在 Windows 用户目录 `C:\Users\<用户名>\` 下创建 `.wslconfig` 文件。

### 基本配置（仅添加 swap）

```ini
[wsl2]
# 增加 swap 作为 OOM 安全垫
swap=4GB
```

### 高级配置（限制内存上限）

如果希望限制 WSL 最大内存使用量（例如防止 WSL 占用过多主机内存）：

```ini
[wsl2]
memory=6GB
swap=4GB
# localhostForwarding=true  # 默认已开启
```

### 生效方式

```powershell
# 在 Windows PowerShell 或 CMD 中执行
wsl --shutdown
# 重新启动 WSL（打开终端即可）
```

## 验证

重启 WSL 后：

```bash
# 查看 swap
swapon --show
# 预期输出：
# NAME       TYPE SIZE USED PRIO
# /swap/file file 4G   0B   -2

# 查看总内存
free -h
```

## 注意事项

- `.wslconfig` 仅作用于 WSL2，不影响 WSL1
- 重启 WSL 会终止所有 WSL 进程，包括 Hermes Gateway、Web UI 等
- 修改 `.wslconfig` 后必须 `wsl --shutdown` 再加 WSL 重启才能生效
- swap 文件路径默认在 `%USERPROFILE%\AppData\Local\Temp\` 下
- 可以通过 `swapFile=D:\wsl-swap.vhdx` 指定到 D 盘（避免 C 盘空间不足）
