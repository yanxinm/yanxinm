# WSL OOM Prevention

Hermes Agent runs multiple memory-intensive processes inside WSL2. Without swap or memory limits, the Linux OOM killer can terminate the gateway, hindsight daemon, or other critical processes when RAM runs out.

## How OOM Manifests in Hermes

- **Gateway**: Last log entry is a routine message (cache eviction, idle sweep), then nothing. No traceback, no error. The process simply disappears.
- **hindsight-api**: Daemon process shows as `(defunct)` zombie or just gone. Subsequent memory operations fail silently or trigger a new daemon spawn.
- **Multiple gateway instances**: A failed `--replace` restart can leave two gateway processes alive simultaneously, doubling memory for several seconds — enough to trigger OOM if near the limit.

## Symptoms

- `hermes gateway status` shows "not running" but no error in logs
- `ps aux` shows zombie hindsight-api processes
- Web UI / WeChat / Feishu all offline (because gateway is dead)

## Quick Fix (during an OOM event)

```bash
# 1. Kill the biggest memory hog first
kill -9 $(pgrep -f hindsight-api) 2>/dev/null
sleep 1

# 2. Check memory freed
free -h

# 3. Restart gateway (in background via terminal tool)
hermes gateway run &
```

The hindsight daemon auto-starts on next memory operation — no manual intervention needed.

## Long-term Prevention: Add Swap

WSL2 doesn't allocate swap by default. A `.wslconfig` file in the Windows user's home directory adds it:

### 1. Create `C:\Users\<your-username>\.wslconfig`

```ini
[wsl2]
# 4GB swap as OOM safety net
swap=4GB

# Optional: hard memory limit to prevent runaway processes
# memory=6GB
```

### 2. Restart WSL from PowerShell/CMD

```powershell
wsl --shutdown
```

Then restart your WSL terminal. Verify swap is active:

```bash
swapon --show
free -h
# Expected: Swap: 4.0Gi total
```

### Memory Limit (Optional)

If you want to prevent any single WSL process from consuming all host memory, add `memory=6GB` to `.wslconfig`. This caps WSL at 6GB. Without it, WSL uses up to 50% of host RAM by default.

**Tradeoff**: With a hard limit, the kernel starts swapping or OOM-killing earlier than without. If your workload typically runs fine within the limit, this is safe; if it occasionally spikes, prefer swap without a hard limit.

## Prevention: Reduce Memory Per Process

See `references/hindsight-memory-setup.md` → **Memory Optimization for Low-RAM Environments** for hindsight daemon tuning (reduce `idle_timeout`, increase `retain_every_n_turns`).

## Auto-start Script Maintenance

The Windows Task Scheduler script at `C:\\Tools\\hermes-gateway-start.bat` starts services in sequence. The startup order matters: Web UI first (starts API bridge), then Dashboard, then Gateway:

```batch
@echo off
echo Starting Hermes Web UI (8648)...
wsl.exe -d Ubuntu -u yanxin bash -lc "nohup /home/yanxin/.npm-global/bin/hermes-web-ui start > /dev/null 2>&1 &"
echo Starting Hermes Dashboard (9119)...
wsl.exe -d Ubuntu -u yanxin bash -lc "nohup /home/yanxin/.local/bin/hermes dashboard --port 9119 --host 127.0.0.1 --no-open > /dev/null 2>&1 &"
echo Starting Hermes Gateway...
wsl.exe -d Ubuntu -u yanxin bash -lc "cd /home/yanxin/Hermes-Agent && source venv/bin/activate && hermes gateway run --replace"
```

### Pitfall: /mnt/c/ file permissions

Files created by Windows processes under `C:\Tools\` may have Linux permissions `0555` (read-only for WSL user). If you get `Permission denied` when trying to rewrite them from WSL:

```bash
chmod 644 /mnt/c/Tools/hermes-gateway-start.bat
# Then write the file
```
