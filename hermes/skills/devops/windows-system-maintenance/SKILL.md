---
name: windows-system-maintenance
description: Windows system administration tasks performed from WSL — registry cleanup, installed program management, file operations on Windows drives, and related troubleshooting.
triggers:
  - User asks to clean up remnants of an uninstalled program
  - User needs to query/modify Windows registry from WSL
  - User needs to delete Windows files/folders from WSL
  - User encounters Windows permission or path issues via WSL
  - User asks about uninstalling or finding leftovers of a Windows app
---

# Windows System Maintenance (from WSL)

This skill covers Windows system administration tasks that you perform from inside WSL (Windows Subsystem for Linux). It focuses on the common pitfalls with cross-boundary tooling.

## Registry Cleanup from WSL

After uninstalling a Windows program, registry remnants often remain. Use `reg.exe` (Windows registry tool available inside WSL) to clean them.

### Key Tactics

| Task | Command | Notes |
|------|---------|-------|
| Search for a program | `reg.exe query "HKLM\Software" /s /f "ProgramName"` | May timeout on large HKLM queries; prefer targeted paths |
| Delete a key (HKCU) | `reg.exe delete "HKCU\Software\Path\To\Key" /f` | Works without elevation |
| Delete a key (HKLM) | `reg.exe delete "HKLM\Software\Path\To\Key" /f` | Needs admin rights |
| Delete single value | `reg.exe delete "Key\Path" /v "ValueName" /f` | Leaves other values intact |
| Delete all values + subkeys | `reg.exe delete "Key\Path" /f` | Removes the entire key recursively |

### Common Search Locations for Remnants

```
HKCU\Software\Microsoft\Windows\CurrentVersion\Uninstall\
HKCU\Software\Microsoft\Windows\CurrentVersion\AppListBackup\
HKCU\Software\Microsoft\Windows\CurrentVersion\Explorer\FeatureUsage\AppSwitched
HKCU\Software\Microsoft\Windows\CurrentVersion\Search\JumplistData
HKCU\Software\Microsoft\Windows\CurrentVersion\Start\TileProperties\
HKCU\Software\Microsoft\Windows NT\CurrentVersion\AppCompatFlags\Compatibility Assistant\Store
HKCU\Software\Classes\Local Settings\Software\Microsoft\Windows\Shell\MuiCache
HKCU\Software\Classes\               (URL protocol handlers)
HKLM\Software\Microsoft\Windows\CurrentVersion\Uninstall\
HKLM\Software\                       (per-app GUID keys)
```

## Pitfalls

1. **cmd.exe does NOT work from UNC paths.** WSL mounts at `\\\\wsl.localhost\\...`, and cmd.exe refuses to run from a UNC path. Always use `reg.exe` directly (it works from WSL), or use `powershell.exe` with a script file on a Windows drive (C:). For diskpart: use `cmd.exe /c "cd /d C:\ && diskpart /s <tempfile>"` — pipes to diskpart from bash are unreliable; temp files are the reliable pattern. See `references/diskpart-from-wsl.md` for the full pattern including drive letter juggling.

2. **Batch files with Chinese characters created in WSL get mangled.** Line endings and encoding issues. Write scripts as individual reg.exe commands, or use PowerShell script files written to a Windows path (e.g., `C:\Users\<user>\Desktop\`).

3. **`$` in registry key names.** PowerShell interprets `$` as variable interpolation. Either escape each `$` with backtick (`` `$ ``) in inline commands, or better: write a PowerShell `.ps1` script file using single-quoted PowerShell strings and `Remove-Item -Path`.

4. **`reg delete /va` only deletes VALUES, not SUBKEYS.** To delete a full key with all subkeys, omit `/va` and just use `reg delete "Key\Path" /f`.

5. **HKLM modifications need admin rights.** If running from a non-admin WSL shell, HKLM operations will fail with "access denied." Consider asking the user to run the WSL terminal as Administrator, or write a script they can right-click -> Run as Administrator.

6. **HKLM recursive queries timeout.** Scanning `HKLM\Software` with `/s /f` can take >180s. Prefer targeted paths (e.g., `HKLM\Software\Microsoft\Windows\CurrentVersion\Uninstall`).

7. **/mnt/c/ files created by Windows processes may be read-only from WSL.** Files under `C:\Tools\` (and other Windows-created paths) often have Linux permissions `0555` (r-xr-xr-x), which blocks WSL writes even when the WSL user *yanxin* is the owner. Fix:
   ```bash
   chmod 644 /mnt/c/Path/To/File
   ```
   This preserves executable permission if needed: `chmod 755 /mnt/c/Tools/*.bat`.

## References

- `references/registry-cleanup-example.md` — complete worked example of cleaning AiPy Pro registry remnants
- `references/backup-push-fail-detection.md` — handling `git push` failures under `set -e`, GitHub Push Protection recovery

## Cross-References to Other Skills

For Hermes infrastructure health checks, service restarts, watchdog scripts, and platform connectivity verification (Gateway, Web UI, Dashboard, TDAI Memory, WeChat, Feishu), use the **hermes-gateway-ops** skill. It covers:

- Full-stack health checks (`references/hermes-full-stack-health-check.md`)
- WSL service watchdog and EPIPE crash analysis (`references/wsl-service-watchdog.md`)
- Scheduler overnight gap detection (`references/scheduler-overnight-gap-detection.md`)
- Cron-based auto-restart scripts

All of those topics were previously duplicated here; the canonical sources now live under hermes-gateway-ops.

## Verification

After cleanup, verify with targeted queries:
```
reg.exe query "HKCU\Software" /s /f "ProgramName" 2>&1 | grep -c "ProgramName"
reg.exe query "HKLM\Software\Microsoft\Windows\CurrentVersion\Uninstall" /s /f "ProgramName" 2>&1
```

Exit code 1 + "0 matches" means clean. If grep finds a match, check the exact key path and delete it.