#!/usr/bin/env python3
"""
旅行行程信息图海报生成器
用途：生成文字为主的行程海报（非冰箱贴风格）
用法: python3 travel-poster-info.py --day 1 --date "7.18 周六" --output /tmp/day1.jpg

数据通过参数传入，也可从 JSON 文件加载。
"""

import argparse
from PIL import Image, ImageDraw, ImageFont
import os

CANVAS_W, CANVAS_H = 1080, 1440
BG_COLOR = '#FAF8F5'

FONT_PATH = '/usr/share/fonts/truetype/noto/NotoSansCJK-Regular.ttc'


def load_font(size):
    try:
        return ImageFont.truetype(FONT_PATH, size)
    except:
        return ImageFont.load_default()


def generate_poster(day, date_str, greeting, items, location_note, output_path,
                    title_color='#5A7A5A', accent_color='#E88D67'):
    """
    items: list of (icon, text) tuples
    """
    canvas = Image.new('RGB', (CANVAS_W, CANVAS_H), BG_COLOR)
    draw = ImageDraw.Draw(canvas)

    font_greeting = load_font(24)
    font_day = load_font(48)
    font_date = load_font(24)
    font_card_icon = load_font(32)
    font_card_text = load_font(32)
    font_location = load_font(24)

    # 问候语
    gw = draw.textbbox((0, 0), greeting, font=font_greeting)
    draw.text(((CANVAS_W - gw[2]) // 2, 50), greeting, fill='#999999', font=font_greeting)

    # Day N 标题
    dw = draw.textbbox((0, 0), day, font=font_day)
    draw.text(((CANVAS_W - dw[2]) // 2, 110), day, fill=title_color, font=font_day)

    # 日期
    ddw = draw.textbbox((0, 0), date_str, font=font_date)
    draw.text(((CANVAS_W - ddw[2]) // 2, 170), date_str, fill='#AAAAAA', font=font_date)

    # 分割线
    draw.line([(80, 210), (CANVAS_W - 80, 210)], fill='#E0DDD5', width=2)

    # 信息卡片
    y_start = 260
    card_h = 80
    gap = 12

    for i, (icon, text) in enumerate(items):
        y = y_start + i * (card_h + gap)
        box = [80, y, CANVAS_W - 80, y + card_h]
        draw.rounded_rectangle(box, radius=12, fill='#FFFFFF', outline='#E8E5DD', width=1)
        draw.text((110, y + card_h // 2 - 14), icon, fill='#333333', font=font_card_icon)
        draw.text((200, y + card_h // 2 - 10), text, fill='#4A4A4A', font=font_card_text)

    # 底部地点备注
    lw = draw.textbbox((0, 0), location_note, font=font_location)
    draw.text(((CANVAS_W - lw[2]) // 2, CANVAS_H - 60), location_note, fill='#CCCCCC', font=font_location)

    os.makedirs(os.path.dirname(output_path) or '.', exist_ok=True)
    canvas.save(output_path, 'JPEG', quality=97)
    print(f"✅ Poster saved: {output_path} ({CANVAS_W}x{CANVAS_H})")


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='旅行行程信息图海报生成器')
    parser.add_argument('--day', required=True, help='Day N 标题')
    parser.add_argument('--date', required=True, help='日期如 "7.18 周六"')
    parser.add_argument('--greeting', required=True, help='问候语如 "出发啦！贵阳见～"')
    parser.add_argument('--location', required=True, help='底部地点备注')
    parser.add_argument('--output', required=True, help='输出路径')
    parser.add_argument('--items-json', help='JSON 文件路径，格式: [{"icon":"✈️","text":"南京→贵阳 14:50"},...]')
    
    args = parser.parse_args()

    if args.items_json:
        import json
        with open(args.items_json) as f:
            items_raw = json.load(f)
            items = [(item['icon'], item['text']) for item in items_raw]
    else:
        parser.error('--items-json is required')

    generate_poster(args.day, args.date, args.greeting, items, args.location, args.output)
