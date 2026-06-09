---
name: linux-desktop-apps
description: Install, configure, and troubleshoot desktop GUI applications on Linux — Electron apps from source, .desktop entries, D-Bus/X11 issues, and cross-platform path fixes.
---

# Linux Desktop Apps

Install and configure GUI applications on Linux (tested on Ubuntu 22.04 + GNOME/Wayland).

## Triggers

- "装一个 XXX（Electron/GUI 应用）"
- "应用菜单里没有图标"
- Electron app crashes with ENOENT for Windows binaries
- D-Bus or X11 errors launching GUI apps

## 1. Electron App from Source (GFW-safe)

### 1.1 Prerequisites

```bash
# Check desktop environment
echo $XDG_SESSION_TYPE   # wayland or x11
echo $DISPLAY            # :0 or :1
loginctl list-sessions   # must have a graphical session
```

**Requires**: GNOME Shell or Xorg running. Not headless.

### 1.2 Install steps

```bash
# 1. Install pnpm + yt-dlp
npm i -g pnpm
pip3 install yt-dlp -i https://pypi.tuna.tsinghua.edu.cn/simple

# 2. Clone repo (use ghproxy if GFW)
git clone https://ghproxy.net/https://github.com/<user>/<repo>.git

# 3. Set mirrors, install dependencies
npm config set registry https://registry.npmmirror.com
ELECTRON_MIRROR=https://npmmirror.com/mirrors/electron/ pnpm install

# 4. Approve build scripts (pnpm v9+)
pnpm approve-builds electron esbuild bufferutil utf-8-validate
```

### 1.3 Electron binary manual download

If `electron postinstall` fails (binary blocked by GFW), download manually:

```bash
ELECTRON_VER="30.0.1"  # check package.json devDependencies
ELECTRON_DIR="node_modules/.pnpm/electron@${ELECTRON_VER}/node_modules/electron/dist"
mkdir -p "$ELECTRON_DIR"

curl -L -o /tmp/electron.zip \
  "https://npmmirror.com/mirrors/electron/v${ELECTRON_VER}/electron-v${ELECTRON_VER}-linux-x64.zip"
unzip -o /tmp/electron.zip -d "$ELECTRON_DIR"

# Create path.txt (required by electron/index.js)
printf 'electron' > "$(dirname "$ELECTRON_DIR")/path.txt"
chmod +x "$ELECTRON_DIR/electron"
```

### 1.4 Cross-platform binary paths

**Pitfall**: Many Electron apps hardcode `*.exe` for Windows. Check for:

```typescript
// WRONG — Linux-only failure
return 'yt-dlp.exe'

// RIGHT — cross-platform
const isWin = process.platform === 'win32'
const name = isWin ? 'yt-dlp.exe' : 'yt-dlp'
return name
```

Search for `.exe` strings in `electron/main.ts` and fix before build.

### 1.5 D-Bus and display env vars

If you see `bus.cc(407) Failed to connect to the bus`:

```bash
export XDG_RUNTIME_DIR=/run/user/1000
export DBUS_SESSION_BUS_ADDRESS="unix:path=/run/user/1000/bus"
DISPLAY=:0 pnpm dev
```

Verify UID matches: `id -u`

## 2. Desktop Entry (.desktop file)

Create application menu entries for manually installed apps:

```bash
cat > ~/.local/share/applications/<app-name>.desktop << 'EOF'
[Desktop Entry]
Version=1.0
Type=Application
Name=<Display Name>
Name[zh_CN]=<中文名>
Exec=/path/to/binary %U
Icon=/path/to/icon.png
Terminal=false
Categories=<Category>;
MimeType=<mimetypes>;
StartupWMClass=<wm-class>
EOF

update-desktop-database ~/.local/share/applications/
```

Refresh GNOME Shell: `Alt+F2` → `r` → Enter.

### Icon discovery

```bash
find /opt/<app> -name "product_logo*.png"
find /usr/share/icons -name "*<app>*"
```

For more techniques (favicon HTML scraping, ICO extraction, SVG fallback), see `references/icon-extraction.md`.

## 3. Video Player Setup

```bash
sudo apt install mpv -y   # H.264/AAC/HEVC all supported via ffmpeg
```

Usage: `mpv <file>` or `yt-dlp -o - <url> | mpv -` for streaming.

## Pitfalls

- **`spawn X ENOENT`**: App hardcoded Windows `.exe` path → fix cross-platform detection
- **`Electron failed to install correctly`**: Missing `path.txt` or binary → manual download §1.3
- **`spawn .../electron\n ENOENT`** (trailing newline in path): Used `echo` instead of `printf` to write `path.txt`. `echo` adds `\n`, making the path `electron\n` — use `printf 'electron'` always.
- **`bus.cc(407)`**: No D-Bus session → set env vars §1.5
- **`cannot open display: :0`**: Shell started without DISPLAY → check `echo $DISPLAY`
- **`GetVSyncParametersIfAvailable() failed`**: GPU compositor quirk, non-fatal warning
