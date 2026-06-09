# App Icon Extraction Techniques

Methods for finding/creating icons for `.desktop` entries, ordered by preference.

## 1. Official Favicon from Website HTML (most reliable)

Curl the page, grep for icon/favicon links:

```bash
curl -sL "https://www.doubao.com" -H "User-Agent: Mozilla/5.0" | grep -i 'icon\|favicon'
```

Look for patterns like:
```html
<link rel="icon shortcut" href="https://cdn.example.com/favicon/128x128.png" sizes="128x128">
<link rel="apple-touch-icon" href="https://cdn.example.com/favicon/180x180.png">
```

Download the largest available (128x128 or 192x192 is ideal):
```bash
curl -sL "https://cdn.example.com/favicon/128x128.png" -o app-icon.png
file app-icon.png   # verify: "PNG image data, 128 x 128"
```

**Worked for**: Doubao (豆包) — found favicon URLs in page HTML at `lf-flow-web-cdn.doubao.com/obj/flow-doubao/favicon/`.

Common failure modes:
- Google favicon service (`google.com/s2/favicons`) blocked by GFW
- CDN returning HTML/JSON instead of image (wrong URL guess)
- Direct guesses like `logo.png` or `icon.png` usually 404

## 2. ICO File Extraction

```bash
sudo apt install icoutils -y
icotool -x -o /tmp/ input.ico
ls /tmp/*.png   # multiple sizes extracted
```

Pick the largest (e.g., `*_256x256x32.png`).

**Worked for**: Videdown (`ldstore.ico` → 256x256 PNG).

## 3. PE/EXE Binary Extraction (Windows apps only)

```bash
wrestool -x binary.exe -o /tmp/icons/
```

**Does NOT work on ELF Linux binaries** — `wrestool: not a PE or NE library`.

## 4. SVG Fallback (last resort)

When no icon can be found, generate a simple branded SVG:

```svg
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 256 256">
  <rect width="256" height="256" rx="48" fill="#4F6EF7"/>
  <text x="128" y="172" text-anchor="middle" font-size="140"
        font-family="sans-serif" font-weight="bold" fill="white">豆</text>
</svg>
```

SVG icons work fine in GNOME — no PNG conversion needed.

## Worked Examples

| App | Method | Result |
|-----|--------|--------|
| Google Chrome | `find /opt/google -name "product_logo*.png"` | 256x256 PNG found |
| Videdown | `icotool -x ldstore.ico` | 256x256 PNG extracted |
| 豆包 (Doubao) | `curl doubao.com \| grep favicon` | 128x128 PNG from CDN |
| 豆包 (Doubao) | SVG fallback | Blue rect + "豆" text |
