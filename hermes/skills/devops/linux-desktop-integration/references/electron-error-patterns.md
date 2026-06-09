# Electron App Debugging on Linux — Error Patterns

## Pattern 1: "Electron failed to install correctly"

```
Error: Electron failed to install correctly, please delete node_modules/electron
    at getElectronPath (electron/index.js:17:11)
```

**Cause:** `path.txt` missing (pnpm ignored build scripts) or has trailing newline.

**Check:**
```bash
xxd path.txt              # trailing newline = 0a at end
ls dist/electron          # binary missing?
```

**Fix:**
```bash
printf 'electron' > path.txt
chmod +x dist/electron
```

---

## Pattern 2: ENOENT on spawn (newline in path.txt)

```
Error: spawn /path/to/electron/dist/electron\n ENOENT
```

Note the `\n` in the path string. **Cause:** `path.txt` has a trailing newline from `echo`.

**Fix:** Use `printf` instead of `echo`.

---

## Pattern 3: D-Bus connection failures

```
[ERROR:bus.cc(407)] Failed to connect to the bus: Could not parse server address
```

**Cause:** Missing `DBUS_SESSION_BUS_ADDRESS` and `XDG_RUNTIME_DIR` env vars. Electron launches fine but has no D-Bus session — non-fatal warnings.

**Fix:** Export D-Bus vars before launch:
```bash
export XDG_RUNTIME_DIR=/run/user/1000
export DBUS_SESSION_BUS_ADDRESS="unix:path=/run/user/1000/bus"
```

---

## Pattern 4: VSync warnings (non-fatal)

```
[ERROR:gl_surface_presentation_helper.cc(260)] GetVSyncParametersIfAvailable() failed for 1 times!
```

Harmless. GPU compositor sync issue on headless-first sessions. App works fine.

---

## Pattern 5: Network service crash / GPU exit

```
[ERROR:network_service_instance_impl.cc(599)] Network service crashed, restarting service.
[ERROR:gpu_process_host.cc(997)] GPU process exited unexpectedly: exit_code=15
```

Occurs when DISPLAY=:0 disappears (user switched TTY, logged out). Process dies cleanly. Restart normally.

---

## Pattern 6: Cross-platform path hardcoding

```typescript
// BROKEN on Linux:
function getYtDlpPath(): string {
  return 'yt-dlp.exe'   // only exists on Windows
}

// FIXED:
function getYtDlpPath(): string {
  const isWin = process.platform === 'win32'
  const name = isWin ? 'yt-dlp.exe' : 'yt-dlp'
  // ... check possible paths, fallback to name
}
```

Always check `process.platform` for binary name suffixes.
