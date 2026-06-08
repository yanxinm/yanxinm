#!/usr/bin/env python3
"""
冰箱贴风格旅行打卡海报拼合脚本（v2 珐琅徽章版）
用法: python3 travel-poster-compose.py --icon <图标路径> --photo <照片路径> --place "地名" --date "May,2026" --bg-rgb 111 144 185 [--crop-y 806]

--crop-y: 照片中主体头顶的像素Y坐标（缩放至1080宽后）。
          默认：从底部裁（竖构图常见）
          如传了值：从该位置向下取720px
"""

import argparse
import os
import sys

from PIL import Image, ImageDraw, ImageFont
import numpy as np

CANVAS_W, CANVAS_H = 1080, 1440
HALF = CANVAS_H // 2
FONT_PATH = "/tmp/DancingScript.ttf"


def remove_white_bg(img, threshold=235):
    """去除白底"""
    pixels = img.load()
    w, h = img.size
    for y in range(h):
        for x in range(w):
            r, g, b, a = pixels[x, y]
            if r > threshold and g > threshold and b > threshold:
                pixels[x, y] = (r, g, b, 0)
    return img


def compose(icon_path, photo_path, place, date, bg_rgb, crop_y=None):
    canvas = Image.new("RGB", (CANVAS_W, CANVAS_H), bg_rgb)
    draw = ImageDraw.Draw(canvas)

    # ── 图标 ──
    icon = Image.open(icon_path).convert("RGBA")
    icon = remove_white_bg(icon)
    icon_w = int(CANVAS_W * 0.40)  # 40% 宽度
    ratio = icon_w / icon.width
    icon = icon.resize((icon_w, int(icon.height * ratio)), Image.LANCZOS)
    ix = (CANVAS_W - icon.width) // 2
    iy = 80
    canvas.paste(icon, (ix, iy), icon)

    # ── 文字 ──
    text = f"{place} | {date}"
    font = None
    if os.path.exists(FONT_PATH):
        font = ImageFont.truetype(FONT_PATH, int(CANVAS_W * 0.035))
    else:
        font = ImageFont.load_default()
    ty = iy + icon.height + 20
    bbox = draw.textbbox((0, 0), text, font=font)
    tx = (CANVAS_W - (bbox[2] - bbox[0])) // 2
    draw.text((tx, ty), text, fill=(40, 22, 10), font=font)

    # ── 底部原图（支持 crop_y 主体定位裁切）──
    photo = Image.open(photo_path).convert("RGB")
    pw, ph = photo.size
    # 先缩放到宽度 1080
    scale = CANVAS_W / pw
    photo = photo.resize((CANVAS_W, int(ph * scale)), Image.LANCZOS)
    _, new_h = photo.size

    if new_h > HALF:
        if crop_y is not None:
            start_y = max(0, min(crop_y, new_h - HALF))
        else:
            start_y = new_h - HALF  # 从底部裁
        photo = photo.crop((0, start_y, CANVAS_W, start_y + HALF))
    elif new_h < HALF:
        padded = Image.new("RGB", (CANVAS_W, HALF), bg_rgb)
        offset_y = (HALF - new_h) // 2
        padded.paste(photo, (0, offset_y))
        photo = padded
    canvas.paste(photo, (0, HALF))

    out = f"/tmp/{place.lower().replace(' ', '_')}_poster.jpg"
    canvas.save(out, "JPEG", quality=97)
    print(f"✅ 海报完成: {out}")
    return out


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="冰箱贴海报拼合")
    parser.add_argument("--icon", required=True)
    parser.add_argument("--photo", required=True)
    parser.add_argument("--place", required=True)
    parser.add_argument("--date", default="May,2026")
    parser.add_argument("--bg-rgb", nargs=3, type=int, required=True)
    parser.add_argument("--crop-y", type=int, default=None,
                        help="主体头顶 Y 坐标（缩放至1080宽后），默认从底部裁")
    args = parser.parse_args()
    compose(args.icon, args.photo, args.place, args.date,
            tuple(args.bg_rgb), crop_y=args.crop_y)
