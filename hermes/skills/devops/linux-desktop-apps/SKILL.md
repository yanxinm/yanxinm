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

## 3. Video Player Setup (Full Codec Coverage)

Install VLC (GUI player with own codec library) + mpv (lightweight ffmpeg-based) + all restricted codecs for near-universal format support.

```bash
# Full install (Ubuntu 22.04+/24.04)
sudo apt update && sudo apt install -y \
  vlc \
  mpv \
  ubuntu-restricted-extras \
  gstreamer1.0-plugins-bad \
  gstreamer1.0-plugins-ugly \
  gstreamer1.0-libav \
  libdvd-pkg

# Enable encrypted DVD playback
sudo dpkg-reconfigure libdvd-pkg
```

### What each package provides

| Package | Role |
|---------|------|
| `vlc` | GUI player with self-contained codec library (independent of system ffmpeg) |
| `mpv` | Lightweight player using system ffmpeg — broader format compatibility |
| `ubuntu-restricted-extras` | MP3, DVD, Flash, Microsoft fonts |
| `gstreamer1.0-plugins-bad` | Additional codecs (MPEG-2, AAC, etc.) |
| `gstreamer1.0-plugins-ugly` | Patent-encumbered codecs |
| `gstreamer1.0-libav` | GStreamer ↔ ffmpeg bridge |
| `libdvd-pkg` | libdvdcss for encrypted DVD playback |

### Verification

```bash
vlc --version          # should show 3.0.x
mpv --version          # should show 0.37+
ffmpeg -decoders | wc -l   # expect 500+
ffmpeg -formats | grep -E 'mp4|mkv|hevc|av1'  # key formats present
```

### Why both VLC and mpv?

- **VLC**: Best GUI, self-contained codecs, good for remote desktop use and casual playback
- **mpv**: Uses system ffmpeg (547+ decoders), broader edge-case compatibility, CLI-friendly
- Together they cover virtually all video/audio formats — if one fails, the other usually works

### Usage

```bash
vlc <file>                      # GUI playback
mpv <file>                      # CLI/lightweight playback
mpv --vo=gpu --hwdec=auto <file>  # Hardware-accelerated playback
```

### Pitfalls

- **MS Core Fonts license prompt**: `ubuntu-restricted-extras` triggers a debconf EULA dialog for Microsoft fonts during install. In non-interactive terminals, this silently fails with "user did not accept the license" — fonts won't be installed but video codecs install fine. To accept later: `sudo dpkg-reconfigure ttf-mscorefonts-installer`.
- **Apt mirror 403**: If a configured mirror (e.g., Tsinghua) returns 403 for certain suites, switch to `http://cn.archive.ubuntu.com/ubuntu/` in `/etc/apt/sources.list.d/ubuntu.sources`.
- **libdvd-pkg needs manual reconfigure**: The package builds libdvdcss from source at reconfigure time — not during install. Always run `sudo dpkg-reconfigure libdvd-pkg` after install.

## 4. Native Linux Apps (deb/rpm)

### 4.1 Download from slow CDNs with aria2c

Many Chinese software vendors (Tencent, DingTalk) host .deb/.rpm on CDNs with poor international connectivity. Single-threaded curl/wget can be extremely slow (~100KB/s). Use aria2c for multi-threaded download:

```bash
# Install aria2
sudo apt install -y aria2

# Multi-threaded download (16 connections)
aria2c -x 16 -s 16 -o /tmp/app.deb "https://cdn.example.com/app_x86_64.deb"

# Typical speedup: 100KB/s → 1+MB/s
```

### 4.2 Find official download URLs from flathub

When official download pages are dynamically loaded (React/SPA) and curl can't extract the URL, check the flathub GitHub repo:

```bash
# flathub maintains .deb URLs in their manifest YAML
curl -sL "https://raw.githubusercontent.com/flathub/com.tencent.wemeet/master/com.tencent.wemeet.yml" \
  | grep -E "url:.*updatecdn.*\.deb"

# Example output:
# url: https://updatecdn.meeting.qq.com/cos/xxx/TencentMeeting_xxx_x86_64.deb
# url: https://updatecdn.meeting.qq.com/cos/xxx/TencentMeeting_xxx_arm64.deb
```

Pattern: `https://github.com/flathub/com.<vendor>.<app>/blob/master/com.<vendor>.<app>.yml`

### 4.3 Install deb and fix library paths

Apps installed to `/opt/` may fail with `libxxx.so: cannot open shared object file`:

```bash
# Install the deb
sudo dpkg -i /tmp/app.deb

# If library error occurs, add lib path to ldconfig
sudo sh -c 'echo "/opt/<appname>/lib" > /etc/ld.so.conf.d/<appname>.conf'
sudo ldconfig

# Verify all dependencies resolved
ldd /opt/<appname>/bin/<binary> | grep "not found" || echo "All dependencies satisfied"
```

### 4.4 Run and verify

```bash
# Check installation
dpkg -L <package-name> | grep -E "(bin|desktop)"

# GUI apps won't run headless — test from desktop session
# Application menu entry should be in: /usr/share/applications/

# Verify .desktop file
cat /usr/share/applications/<app>.desktop | grep Exec
```

### Known apps with this pattern

| App | Flathub repo | Notes |
|-----|--------------|-------|
| 腾讯会议 (Tencent Meeting) | `flathub/com.tencent.wemeet` | Wayland screenshare may need workaround |
| 钉钉 (DingTalk) | Check AUR/flatpak | Similar CDN issues |

## Pitfalls

- **`spawn X ENOENT`**: App hardcoded Windows `.exe` path → fix cross-platform detection
- **`Electron failed to install correctly`**: Missing `path.txt` or binary → manual download §1.3
- **`spawn .../electron\n ENOENT`** (trailing newline in path): Used `echo` instead of `printf` to write `path.txt`. `echo` adds `\n`, making the path `electron\n` — use `printf 'electron'` always.
- **`bus.cc(407)`**: No D-Bus session → set env vars §1.5
- **`cannot open display: :0`**: Shell started without DISPLAY → check `echo $DISPLAY`
- **`GetVSyncParametersIfAvailable() failed`**: GPU compositor quirk, non-fatal warning
- **`libxxx.so: cannot open shared object file`**: App installed to `/opt/` but library path not in ldconfig → add to `/etc/ld.so.conf.d/` and run `ldconfig`
- **Slow CDN download (<200KB/s)**: Single-threaded curl hitting rate limit or poor routing → use `aria2c -x 16 -s 16` for 5-10x speedup
- **Dynamic download page, no URL visible**: Official site uses SPA → fetch URL from flathub GitHub manifest
- **`dpkg-deb: liblzma.so.5: version XZ_5.4 not found`**: 腾讯会议等安装在 `/opt/` 的应用自带旧版 liblzma，被系统 dpkg-deb 错误加载导致 apt 安装失败。修复：`sudo mv /opt/wemeet/lib/liblzma.so.5 /opt/wemeet/lib/liblzma.so.5.bak`，安装完成后再恢复（或删除备份，腾讯会议有自己的 bundled lib）
