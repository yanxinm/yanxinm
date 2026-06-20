#!/usr/bin/env python3
"""
旅行行程海报 - 时间轴布局模板
生成精致版 PIL 代码排版海报，适用于所有行程天数。
用法：复制此文件，修改 timeline_items、天气、酒店等数据，运行生成。
"""
from PIL import Image, ImageDraw, ImageFont
import os

CANVAS_W, CANVAS_H = 1080, 1440

# ========== 配色方案（可全局调整） ==========
BG_COLOR = '#FAF6F0'          # 暖米白背景
CARD_BG = '#FFFFFF'            # 白色卡片
CARD_BORDER = '#E8E2D6'        # 卡片边框
TITLE_GREEN = '#4A6B5A'        # 深绿标题
ACCENT_CORAL = '#D4846A'       # 珊瑚橙点缀
TEXT_DARK = '#2D2D2D'          # 深色正文
TEXT_GRAY = '#888888'          # 灰色辅助文字
TEXT_LIGHT = '#AAAAAA'         # 浅灰日期
TIME_COLOR = '#6B8E6B'         # 时间标签色
DIVIDER = '#E0D8CC'            # 分割线

# ========== 字体路径 ==========
FONT_BOLD = '/usr/share/fonts/opentype/noto/NotoSansCJK-Bold.ttc'
FONT_REG = '/usr/share/fonts/opentype/noto/NotoSansCJK-Regular.ttc'

def get_font(size):
    if size >= 48:
        return ImageFont.truetype(FONT_BOLD, size)
    return ImageFont.truetype(FONT_REG, size)

# ========== 创建画布 ==========
canvas = Image.new('RGB', (CANVAS_W, CANVAS_H), BG_COLOR)
draw = ImageDraw.Draw(canvas)

# ========== 顶部区域 ==========
# 问候语
greeting = '出发啦！贵阳见～'  # ← 修改此处
greet_font = get_font(22)
greet_bbox = draw.textbbox((0, 0), greeting, font=greet_font)
greet_w = greet_bbox[2] - greet_bbox[0]
draw.text(((CANVAS_W - greet_w) // 2, 40), greeting, fill=TEXT_GRAY, font=greet_font)

# Day N 标题
day_label = 'Day 1'  # ← 修改此处
day_font = get_font(56)
day_bbox = draw.textbbox((0, 0), day_label, font=day_font)
day_w = day_bbox[2] - day_bbox[0]
draw.text(((CANVAS_W - day_w) // 2, 100), day_label, fill=TITLE_GREEN, font=day_font)

# 日期
date_text = '7.18 周六'  # ← 修改此处
date_font = get_font(26)
date_bbox = draw.textbbox((0, 0), date_text, font=date_font)
date_w = date_bbox[2] - date_bbox[0]
draw.text(((CANVAS_W - date_w) // 2, 170), date_text, fill=TEXT_LIGHT, font=date_font)

# 分割线
line_y = 220
draw.line([(60, line_y), (CANVAS_W - 60, line_y)], fill=DIVIDER, width=2)
draw.ellipse([(CANVAS_W // 2 - 3, line_y - 3), (CANVAS_W // 2 + 3, line_y + 3)], fill=ACCENT_CORAL)

# ========== 时间线区域 ==========
# ← 修改此处：按实际行程填写
timeline_items = [
    ('10:35', '✈️', '南京禄口T2 出发'),
    ('13:15', '🛬', '贵阳龙洞堡T3 到达'),
    ('13:30', '🚗', '机场取车 店员送车上门'),
    ('14:15', '🛣️', '贵阳→安顺 1.5h'),
    ('16:00', '🏨', '浠岸酒店 入住'),
    ('17:00', '🚶', '安顺古城 · 虹山湖 · 儒林路老街'),
    ('18:30', '🍜', '夺夺粉 · 裹卷 · 顾府街'),
]

tl_start_y = 260
item_h = 65
item_gap = 8
tl_x = 120
time_w = 70
icon_start_x = tl_x + time_w + 10
text_start_x = icon_start_x + 50

# 时间线
tl_line_x = tl_x + time_w // 2
tl_end_y = tl_start_y + len(timeline_items) * (item_h + item_gap)
draw.line([(tl_line_x, tl_start_y), (tl_line_x, tl_end_y)], fill=TIME_COLOR, width=2)

for i, (time, icon, text) in enumerate(timeline_items):
    y = tl_start_y + i * (item_h + item_gap)
    
    # 时间标签
    time_font = get_font(22)
    time_bbox = draw.textbbox((0, 0), time, font=time_font)
    time_tw = time_bbox[2] - time_bbox[0]
    time_box = [tl_x - 5, y + 5, tl_x + time_tw + 5, y + item_h - 5]
    draw.rounded_rectangle(time_box, radius=8, fill=TIME_COLOR)
    draw.text((tl_x, y + 10), time, fill='WHITE', font=time_font)
    
    # 圆点
    dot_y = y + item_h // 2
    draw.ellipse([(tl_line_x - 5, dot_y - 5), (tl_line_x + 5, dot_y + 5)], fill=ACCENT_CORAL)
    
    # 图标 + 文字
    icon_font = get_font(28)
    draw.text((icon_start_x, y + 12), icon, fill=TEXT_DARK, font=icon_font)
    text_font = get_font(26)
    draw.text((text_start_x, y + 10), text, fill=TEXT_DARK, font=text_font)

# ========== 底部天气穿搭区域 ==========
weather_y = tl_end_y + 30
divider_y = weather_y - 10
draw.line([(80, divider_y), (CANVAS_W - 80, divider_y)], fill=CARD_BORDER, width=1)

card_w = (CANVAS_W - 160) // 2
card_h = 100
card_gap = 20

# 天气卡片
wx_box = [60, weather_y, 60 + card_w, weather_y + card_h]
draw.rounded_rectangle(wx_box, radius=16, fill=CARD_BG, outline=CARD_BORDER, width=1)
wx_icon_font = get_font(32)
draw.text((80, weather_y + 20), '☁️', fill=TEXT_DARK, font=wx_icon_font)
wx_text_font = get_font(24)
draw.text((130, weather_y + 22), '22-28°C 阵雨', fill=TEXT_DARK, font=wx_text_font)  # ← 修改天气

# 穿搭卡片
cloth_box = [60 + card_w + card_gap, weather_y, 60 + card_w + card_gap + card_w, weather_y + card_h]
draw.rounded_rectangle(cloth_box, radius=16, fill=CARD_BG, outline=CARD_BORDER, width=1)
draw.text((60 + card_w + card_gap + 80, weather_y + 20), '👕', fill=TEXT_DARK, font=wx_icon_font)
draw.text((60 + card_w + card_gap + 130, weather_y + 22), '短袖+薄外套+雨伞+防滑鞋', fill=TEXT_DARK, font=wx_text_font)  # ← 修改穿搭

# ========== 底部装饰 ==========
footer_y = weather_y + card_h + 40
footer_font = get_font(18)
footer_text = '📍 贵州 · 安顺'  # ← 修改地点
fb = draw.textbbox((0, 0), footer_text, font=footer_font)
fw = fb[2] - fb[0]
draw.text(((CANVAS_W - fw) // 2, footer_y), footer_text, fill=TEXT_LIGHT, font=footer_font)

# ========== 保存 ==========
out_dir = '/home/miao/出图/'
os.makedirs(out_dir, exist_ok=True)
out_path = os.path.join(out_dir, 'Day1_安顺_代码精排.jpg')  # ← 修改文件名
canvas.save(out_path, 'JPEG', quality=97)
print(f'✅ 已保存: {out_path}')
