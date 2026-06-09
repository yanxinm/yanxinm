---
name: linux-desktop-integration
description: Create .desktop entries, fix missing icons, refresh GNOME menus, and handle Electron app quirks on Linux desktop.
---

# Linux Desktop Integration

When you install an app manually (not via apt/snap) and it doesn't appear in the GNOME application menu, or its icon is missing.

## 1. Creating a .desktop Entry

**Minimal template:**

```ini
[Desktop Entry]
Version=1.0
Type=Application
Name=App Name
Name[zh_CN]=中文名
Exec=/path/to/executable
Icon=/path/to/icon.png
Terminal=false
Categories=Category;SubCategory;
StartupNotify=true
```

**Location:** `~/.local/share/applications/<app>.desktop`

### Categories reference
- Web browser: `Network;WebBrowser;`
- Media player: `AudioVideo;Audio;Video;Player;TV;`
- Video tools: `Network;Video;`
- AI/Utility: `Utility;Development;AI;`
- Electron apps: add `StartupWMClass=<class>` for dock grouping

### After creating/editing:
```bash
update-desktop-database ~/.local/share/applications/
```
Then **Alt+F2 → r → Enter** to restart GNOME Shell (refreshes menu).

## 2. Fixing Missing Icons

### Extract ICNS/ICO to PNG
```bash
sudo apt install icoutils -y
icotool -x -o /tmp/ icon.ico          # extracts all sizes
cp /tmp/*_256x256x32.png /target/     # pick the largest
```

### Generate SVG placeholder when icon is missing
```html
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 256 256">
  <rect width="256" height="256" rx="48" fill="#BRAND_COLOR"/>
  <text x="128" y="172" text-anchor="middle" font-size="140"
        font-family="sans-serif" font-weight="bold" fill="white">字</text>
</svg>
```

### Diagnose broken icon paths
```bash
cat ~/.local/share/applications/<app>.desktop | grep Icon
ls -la <the_path>     # check if file exists
```

### Extract official icon from web page source (Nativefier/Electron wraps)
When an app is a Nativefier-wrapped web app (like 豆包), icons may not exist as local files. Extract the favicon URL from the app's HTML:

```bash
# Search the app's page source or nativefier resources for favicon links
grep -oP 'link rel="icon[^"]*" href="\K[^"]+' /path/to/app/index.html
# Or find in the cached page:
find ~/.cache -name "*.html" -newer /path/to/app -exec grep -l "icon shortcut" {} \;

# Download the official icon
curl -sL "https://cdn.example.com/path/to/icon.png" -o /path/to/icon.png
```

**Common CDN patterns:** Look for `<link rel="icon shortcut" href="https://...favicon/128x128.png">` in page source. ByteDance apps use `lf-flow-web-cdn.doubao.com` for static assets including favicons.

### Pitfalls
- `echo "electron" > path.txt` adds a trailing newline → path becomes `electron\n` → ENOENT. Use `printf` instead.
- `wrestool` only works on PE/NE (Windows) binaries, not Linux ELF executables.
- `Alt+F2 → r` may not work if GNOME Shell isn't the active session; rebooting is the fallback.
- Nativefier-wrapped apps may reference icons under `resources/app/` that don't exist on disk — the icon is only embedded in the ASAR or fetched at runtime from the web.

## 3. Electron App Pitfalls on Linux

### Manual Electron binary download (when postinstall fails)
```bash
ELECTRON_VER="30.0.1"  # from package.json devDependencies
URL="https://npmmirror.com/mirrors/electron/v${ELECTRON_VER}/electron-v${ELECTRON_VER}-linux-x64.zip"
ELECTRON_DIR="node_modules/.pnpm/electron@${ELECTRON_VER}/node_modules/electron/dist"
mkdir -p "$ELECTRON_DIR"
curl -L -o /tmp/electron.zip "$URL"
cd "$ELECTRON_DIR" && unzip -o /tmp/electron.zip
```

### Fixing `Error: Electron failed to install correctly`
Electron's `index.js` reads `path.txt` to locate the binary. pnpm sometimes skips the postinstall that creates it.

```bash
# path.txt MUST have NO trailing newline!
printf 'electron' > node_modules/.pnpm/electron@X.Y.Z/node_modules/electron/path.txt
chmod +x node_modules/.pnpm/electron@X.Y.Z/node_modules/electron/dist/electron
```

### Wayland/D-Bus error: `Failed to connect to the bus`
Electron needs D-Bus session variables when launched from a non-GUI terminal:
```bash
export XDG_RUNTIME_DIR=/run/user/1000
export DBUS_SESSION_BUS_ADDRESS="unix:path=/run/user/1000/bus"
DISPLAY=:0 pnpm dev
```
Use `loginctl list-sessions` to find the correct UID.

### Hardcoded Windows paths (yt-dlp.exe)
Some Electron apps hardcode `.exe` extensions. Check `electron/main.ts`:
- `getFfmpegPath()` often does cross-platform correctly (copy the pattern)
- `getYtDlpPath()` if present often hardcodes `yt-dlp.exe` → add `process.platform === 'win32'` check
- Rebuild is automatic with vite-plugin-electron (file watcher)

## 4. Ubuntu Software (Snap Store) Not Loading App Details

Ubuntu 22.04 uses `snap-store` (a snap-packaged GNOME Software). When app detail pages won't load, the usual cause is **PackageKit blocking on unreachable apt sources**.

### Diagnose
```bash
# Check if snap-store is running
ps aux | grep '[s]nap-store'

# Check journal for PackageKit source errors
journalctl -n 30 --no-pager /snap/snap-store/*/usr/bin/snap-store | grep "无法下载"
```

Common failure pattern:
```
E: 无法下载 http://security.ubuntu.com/ubuntu/dists/jammy-security/InRelease
E: 无法下载 https://pkgs.tailscale.com/stable/ubuntu/dists/jammy/InRelease
```

### Fix
1. **Ensure all apt sources use domestic mirrors** — security.ubuntu.com and third-party repos must be reachable
2. **Disable unreachable third-party sources:**
   ```bash
   sudo mv /etc/apt/sources.list.d/<unreachable>.list /etc/apt/sources.list.d/<unreachable>.list.disabled
   ```
3. **Point security.ubuntu.com to a mirror:**
   ```bash
   sudo sed -i 's|http://security.ubuntu.com/ubuntu|https://mirrors.tuna.tsinghua.edu.cn/ubuntu|g' /etc/apt/sources.list
   ```
4. **Clear snap-store cache and restart:**
   ```bash
   pkill -f snap-store
   rm -rf ~/.cache/gnome-software ~/.local/share/gnome-software
   DISPLAY=:0 snap-store &
   ```

### Verification
```bash
sudo apt update  # should complete without errors
systemctl is-active snapd packagekit  # both should be 'active'
```

## 5. Verifying

```bash
# Is the .desktop file valid?
desktop-file-validate ~/.local/share/applications/<app>.desktop

# Is it recognized?
grep -r "<app>" /usr/share/applications ~/.local/share/applications

# Is the electron process actually running?
ps aux | grep -E '[e]lectron' | grep -v zygote
```

### Pitfalls
- `echo "electron" > path.txt` adds a trailing newline → path becomes `electron\n` → ENOENT. Use `printf` instead.
- `wrestool` only works on PE/NE (Windows) binaries, not Linux ELF executables.
- `Alt+F2 → r` may not work if GNOME Shell isn't the active session; rebooting is the fallback.
