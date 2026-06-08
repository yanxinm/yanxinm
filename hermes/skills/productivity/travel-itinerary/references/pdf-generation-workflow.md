# PDF 生成工作流（fpdf2 + 中文字体）

## 环境要求
```bash
pip install fpdf2
```

## 字体配置

### 首选：Windows 字体（WSL 下可访问时）
```
/mnt/c/Windows/Fonts/simhei.ttf       # 黑体（标题用）
/mnt/c/Windows/Fonts/msyh.ttc         # 微软雅黑（正文用）
/mnt/c/Windows/Fonts/MSYHBD.TTC       # 微软雅黑加粗
```

使用前复制到 /tmp：
```bash
cp /mnt/c/Windows/Fonts/simhei.ttf /tmp/
cp /mnt/c/Windows/Fonts/msyh.ttc /tmp/
```

### 备选：系统自带 Noto CJK 字体（WSL /mnt/c 不可访问时）
```python
FONT_PATH = '/usr/share/fonts/opentype/noto/NotoSerifCJK-Bold.ttc'
# 或
FONT_PATH = '/usr/share/fonts/truetype/arphic/uming.ttc'
```
Noto CJK 缺 emoji 字形（emoji 会显示为空白），但不影响正文内容。

### fpdf2 v2.5+ API 变更
`ln` 参数已废弃，改用 `new_x` / `new_y`：
```python
# 旧（废弃）
self.cell(0, 10, '标题', 0, 1, 'C')
# 新
from fpdf.enums import XPos, YPos
self.cell(0, 10, '标题', align='C', new_x=XPos.LMARGIN, new_y=YPos.NEXT)
# 或直接传字符串
self.cell(0, 10, '标题', align='C', new_x="LMARGIN", new_y="NEXT")
```
警告不影响输出但建议用新 API。

## 核心代码模板

```python
from fpdf import FPDF

class ItineraryPDF(FPDF):
    def __init__(self):
        super().__init__('P', 'mm', 'A4')
        self.add_font('CN', '', '/tmp/simhei.ttf', uni=True)
        self.add_font('CN', 'B', '/tmp/simhei.ttf', uni=True)
        self.add_font('CNLight', '', '/tmp/msyh.ttc', uni=True)
    
    def header(self):
        pass
    
    def footer(self):
        self.set_y(-15)
        self.set_font('CNLight', '', 9)
        self.cell(0, 10, f'第 {self.page_no()} 页', 0, 0, 'C')
    
    def title_page(self, title, subtitle):
        self.add_page()
        self.set_font('CN', '', 28)
        self.ln(60)
        self.cell(0, 20, title, 0, 1, 'C')
        self.set_font('CNLight', '', 14)
        self.ln(10)
        self.cell(0, 10, subtitle, 0, 1, 'C')
    
    def day_section(self, day_num, activities):
        """每天行程表"""
        self.add_page()
        self.set_font('CN', '', 16)
        self.cell(0, 12, f'第{day_num}天', 0, 1, 'L')
        self.ln(3)
        
        # 生成表格
        self.set_font('CNLight', '', 11)
        line_h = 7
        col_w = [22, 130, 38]  # 时间/内容/备注 列宽
        for row in activities:
            self.set_font('CNLight', '', 10)
            for i, cell in enumerate(row):
                self.cell(col_w[i], line_h, cell, 1, 0, 'L')
            self.ln()
    
    def cost_section(self, title, costs, total):
        self.add_page()
        self.set_font('CN', '', 16)
        self.cell(0, 12, title, 0, 1, 'L')
        self.ln(3)
        self.set_font('CNLight', '', 11)
        col_w = [80, 40]
        for item, cost in costs:
            self.cell(col_w[0], 8, item, 1, 0, 'L')
            self.cell(col_w[1], 8, cost, 1, 0, 'R')
            self.ln()
        self.ln(3)
        self.set_font('CN', '', 11)
        self.cell(0, 8, total, 0, 1, 'R')

    def checklist_section(self, items):
        """行前清单"""
        self.add_page()
        self.set_font('CN', '', 16)
        self.cell(0, 12, '行前 Checklist', 0, 1, 'L')
        self.ln(3)
        self.set_font('CNLight', '', 11)
        for item in items:
            self.cell(5, 8, '☐', 0, 0)
            self.multi_cell(0, 8, f'  {item}')

    def food_section(self, city_foods):
        """美食推荐"""
        self.add_page()
        self.set_font('CN', '', 16)
        self.cell(0, 12, '🍜 美食推荐', 0, 1, 'L')
        self.ln(3)
        self.set_font('CNLight', '', 11)
        col_w = [35, 100, 55]
        self.set_font('CN', '', 11)
        for h in ['城市', '推荐美食', '备注']:
            self.cell(col_w[self.column_idx], 8, h, 1, 0, 'C')
        self.ln()
        self.set_font('CNLight', '', 10)
        for city, food_list, note in city_foods:
            self.cell(col_w[0], 8, city, 1, 0, 'L')
            self.cell(col_w[1], 8, food_list, 1, 0, 'L')
            self.cell(col_w[2], 8, note, 1, 0, 'L')
            self.ln()
```

## 保存到桌面
```python
import os
desktop = os.path.expanduser('/mnt/c/Users/yanxi/Desktop')
output_path = os.path.join(desktop, '行程文件.pdf')
pdf.output(output_path)
print(f'PDF saved: {output_path}')
```

## 通过微信发送
PDF 生成后通过 `send_message` 发送给用户：
- 先尝试发送，失败等待限流解除再重试
- 限流通常等待 30 秒至数分钟
- 最多重试 3 次
- 如果持续失败，告知用户桌面路径可取

## 已知问题
| 问题 | 解决方法 |
|------|---------|
| TTFontWarning: Unknown font-weight | 部分 TTC 字体会触发警告，不影响输出，忽略 |
| 表格中文换行 | 用 multi_cell 替代 cell 支持自动换行 |
| PDF 文件大小 | 纯文字通常 <200KB |
