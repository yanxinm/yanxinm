#!/usr/bin/env python3
"""
旅行打卡海报 — 冰箱贴风格（白描边+投影+手写文字）
用法：修改 ═══ 之间的参数后运行

依赖：pip install Pillow
字体：下载 Dancing Script 到 ~/.fonts/DancingScript.ttf
  curl -sL "https://fonts.gstatic.com/s/dancingscript/v29/If2cXTr6YS-zF4S-kcSWSVi_sxjsohD9F50Ruu7BMSoHTQ.ttf" \
    -o ~/.fonts/DancingScript.ttf
  fc-cache -f ~/.fonts/
"""
from PIL import Image, ImageDraw, ImageFont, ImageFilter
import os

# ═══════════════ 参数配置 ═══════════════
AI_ICON_PATH   = "seedream_xxx.jpeg"      # 豆包生成的建筑图标（1920×1920）
PHOTO_PATH     = "original_photo.jpg"      # 实拍原图
OUTPUT_PATH    = "poster_output.jpg"       # 输出路径
PLACE_NAME     = "JIANSHUI"                # 地名（显示文字）
DATE_TEXT      = "07.2025"                 # 日期
BG_COLOR       = (188, 115, 80)            # 上半部分纯色背景（暖色系）
FONT_SCRIPT    = os.path.expanduser("~/.fonts/DancingScript.ttf")
FONT_FALLBACK  = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"
# ═══════════════ 结束修改 ═══════════════

TW, TH = 1080, 1440
HALF = TH // 2

# ── 1. AI图标：白底去背 ──
icon = Image.open(AI_ICON_PATH).convert("RGBA")
icon = icon.resize((1080, 1080), Image.LANCZOS)

r, g, b, a = icon.split()
gray = icon.convert("L")
new_alpha = gray.point(lambda x: 0 if x > 230 else 255)
new_alpha = new_alpha.filter(ImageFilter.MaxFilter(5))
icon.putalpha(new_alpha)

# ── 2. 缩放 ──
scale = 0.55
iw = int(1080 * scale)
ih = int(1080 * scale)
icon_s = icon.resize((iw, ih), Image.LANCZOS)

# ── 3. 白描边 ──
alpha = icon_s.getchannel("A")
border_mask = alpha.filter(ImageFilter.MaxFilter(21))
border = Image.new("RGBA", (iw, ih), (255, 255, 255, 255))
border.putalpha(border_mask)

# ── 4. 投影阴影 ──
shadow_mask = alpha.filter(ImageFilter.MaxFilter(25))
shadow_mask = shadow_mask.filter(ImageFilter.GaussianBlur(15))
shadow = Image.new("RGBA", (iw, ih), (0, 0, 0, 0))
shadow.putalpha(shadow_mask.point(lambda x: int(x * 0.35)))
# 给阴影一个颜色
for y in range(ih):
    for x in range(iw):
        px = shadow.getpixel((x, y))
        if px[3] > 0:
            shadow.putpixel((x, y), (90, 55, 30, px[3]))

# ── 5. 上半部分 ──
top = Image.new("RGBA", (TW, HALF), (*BG_COLOR, 255))
cx = TW // 2
ix = cx - iw // 2
iy = 10

top.paste(shadow, (ix + 4, iy + 6), shadow)
top.paste(border, (ix, iy), border)
top.paste(icon_s, (ix, iy), icon_s)

# ── 6. 文字 ──
draw = ImageDraw.Draw(top)

font_main = None
font_sub = None
if os.path.exists(FONT_SCRIPT):
    try:
        font_main = ImageFont.truetype(FONT_SCRIPT, 44)
        font_sub = ImageFont.truetype(FONT_SCRIPT, 24)
    except:
        pass
if font_main is None:
    font_main = ImageFont.truetype(FONT_FALLBACK, 38)
    font_sub = ImageFont.truetype(FONT_FALLBACK, 20)

bb1 = draw.textbbox((0, 0), PLACE_NAME, font=font_main)
bb2 = draw.textbbox((0, 0), DATE_TEXT, font=font_sub)
tw1, tw2 = bb1[2]-bb1[0], bb2[2]-bb2[0]

ty = iy + ih + 25
draw.text((cx - tw1//2 + 2, ty + 2), PLACE_NAME, fill=(90, 55, 30), font=font_main)
draw.text((cx - tw1//2, ty), PLACE_NAME, fill=(50, 30, 15), font=font_main)

ty2 = ty + 52
draw.text((cx - tw2//2 + 2, ty2 + 2), DATE_TEXT, fill=(90, 55, 30), font=font_sub)
draw.text((cx - tw2//2, ty2), DATE_TEXT, fill=(50, 30, 15), font=font_sub)

# ── 7. 下半部分：原图 ──
photo = Image.open(PHOTO_PATH).convert("RGB")
pw, ph = photo.size
ratio = max(TW/pw, HALF/ph)
nw, nh = int(pw*ratio), int(ph*ratio)
photo = photo.resize((nw, nh), Image.LANCZOS)
left = (nw - TW) // 2
photo = photo.crop((left, 0, left+TW, HALF))

# ── 8. 拼合 ──
canvas = Image.new("RGB", (TW, TH))
canvas.paste(top.convert("RGB"), (0, 0))
canvas.paste(photo, (0, HALF))

d2 = ImageDraw.Draw(canvas)
for i in range(3):
    d2.line([(0, HALF+i-1), (TW, HALF+i-1)], fill=(220, 200, 180, 60), width=1)

canvas.save(OUTPUT_PATH, quality=95)
print(f"✅ Poster saved: {OUTPUT_PATH} ({TW}×{TH})")
