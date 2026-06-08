# WSL Gateway Auto-Start on Windows Boot

Hermes Gateway needs to run as a background process to handle WeChat, Feishu, and other messaging platforms. On WSL, systemd user services don't work reliably (the user bus isn't accessible), so the recommended approach is using **Windows Task Scheduler** (more reliable than the Startup folder — runs with configurable delay, highest privileges, survives reboots better).

## Recommended Approach: Windows Task Scheduler

### Step 1: Create a wrapper batch file on the Windows side

Create a `.bat` file in a stable Windows path (e.g. `C:\Tools\`). This avoids quoting issues with `&&` inside the schtasks command.

```batch
@echo off
wsl.exe -d Ubuntu -u <wsl_username> bash -lc "cd /home/<wsl_username>/Hermes-Agent && source venv/bin/activate && hermes gateway run --replace"
```

Path: `C:\Tools\hermes-gateway-start.bat`

### Step 2: Create the scheduled task

From within WSL, use PowerShell to create the task. This avoids UNC path issues with `cmd.exe /c` (WSL's CWD is a UNC path like `\\wsl.localhost\Ubuntu\home\...`, which `cmd.exe` doesn't support):

```powershell
powershell.exe -Command "schtasks /create /tn 'Hermes Gateway' /tr 'C:\Tools\hermes-gateway-start.bat' /sc onlogon /delay 0000:30 /rl highest /f"
```

Or run `schtasks` directly in a Windows terminal (CMD or PowerShell) as Administrator.

### Task properties

| Property | Value |
|----------|-------|
| Task name | `Hermes Gateway` |
| Trigger | At logon (any user) |
| Delay | 30 seconds (allow WSL to fully initialize) |
| Run with | Highest privileges |
| Action | Run `C:\Tools\hermes-gateway-start.bat` |
| Runs as | The Windows user |

### Alternative: Windows Startup Folder

If Task Scheduler isn't available, use the Startup folder:

1. Create `%APPDATA%\Microsoft\Windows\Start Menu\Programs\Startup\启动Hermes.bat`
2. Write the same `wsl.exe -d Ubuntu ...` command from above
3. The `.bat` will run on user login

Pitfall: the `.bat` briefly flashes a console window. To hide it, use a `.vbs` wrapper:
```vbs
Set WshShell = CreateObject("WScript.Shell")
WshShell.Run "wsl -d Ubuntu -u yanxin bash -lc '...'", 0, False
```

## Checking gateway state

```bash
# 1. Check gateway process is running
ps aux | grep "gateway run"

# 2. Check gateway state JSON (shows platform connection status)
cat ~/.hermes/gateway_state.json
# Fields: gateway_state ("running"/"draining"/"stopped"),
#         per-platform state ("connected"/"disconnected"),
#         PID, timestamps

# 3. Check gateway logs
cat ~/.hermes/logs/gateway.log | tail -30
```

A healthy gateway shows:
```json
{"gateway_state":"running","platforms":{"feishu":{"state":"connected"},"weixin":{"state":"connected"},"api_server":{"state":"connected"}}}
```

## Pitfalls

### Quoting nightmare with schtasks

Running `schtasks /create /tr "..."` directly with a wsl command containing `&&` is extremely fragile. **The `&&` is interpreted by cmd.exe/PowerShell as a command separator**, splitting your argument in half and causing `'Invalid syntax: Missing required option 'sc''`. Always use a wrapper batch file on the Windows filesystem instead of inline commands.

### UNC path issue in WSL

When running `cmd.exe /c` from within WSL, the current working directory is a UNC path (e.g. `\\wsl.localhost\Ubuntu\home\yanxin`). `cmd.exe` prints `"UNC paths are not supported. Defaulting to Windows directory."` and may behave unexpectedly. Use `powershell.exe -Command` instead, or `cd /d C:\` in the batch file.

### File permissions across WSL/Windows boundary

Writing to `C:\Users\<user>\AppData\...` from WSL file tools (`write_file`, `patch`) may fail with "Permission denied" even though the path has `rwxrwxrwx` permissions. Use terminal commands with shell redirection instead, or create the file on the Windows side.

### WSL distro name encoding

`wsl -l -q` may output UTF-16 (seen as `U\u0000b\u0000u\u0000n\u0000t\u0000u` in terminal). The actual name is likely "Ubuntu". Verify: `wsl -l -q > /tmp/distro.txt` then `cat /tmp/distro.txt`.

### Windows username discovery

Find the Windows username by listing `/mnt/c/Users/` and excluding well-known entries (All Users, Default, Public, desktop.ini). The WSL username is typically different from the Windows username.

### General (applies to both approaches)

- **`--replace` flag**: Always use it — it kills any existing gateway instance before starting, avoiding port conflicts.
- **Working directory**: Must be `~/Hermes-Agent` (or wherever Hermes is installed), because the venv activation depends on relative paths.
- **Venv activation**: Must source `venv/bin/activate` so `hermes` is on PATH.
- **Removing the old Startup folder entry**: If switching from Startup folder to Task Scheduler, delete the old `.bat` file to avoid duplicate gateway launches.
