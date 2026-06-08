# 颜色提取与 API Key 获取

## ⚠️ 暗调照片主色提取（已验证案例）

照片整体偏暗（如室内、阴天森林、深色建筑）时，全图 KMeans 或 Counter 会返回**近黑色**作为主色（如 `RGB(11,10,15)`），不宜作为海报背景。

**修复**：只从照片的**中间偏上区域**提取（避开头部的天空/阴影和底部的人物/地面）：

```python
from PIL import Image
import numpy as np

img = Image.open(photo_path)
w, h = img.size
# 取 20%-60% 高度区域（通常包含建筑/主体）
region = img.crop((0, int(h*0.20), w, int(h*0.60)))
region_small = region.resize((100, 100))
pixels = np.array(region_small).reshape(-1, 3)

# 进一步筛选暖色调像素（R > G 且 R > 80）
warm = [tuple(p) for p in pixels 
        if int(p[0]) > 80 and int(p[0]) > int(p[1]) * 1.2 and int(p[0]) > int(p[2]) * 1.5]
if warm:
    avg = tuple(int(np.mean([p[i] for p in warm])) for i in range(3))
    # 提亮 20% 以获得明信片感
    bright = (min(255, int(avg[0]*1.2)), min(255, int(avg[1]*1.3)), min(255, int(avg[2]*1.3)))
    print(f"推荐背景色: RGB{bright}")
```

**西双版纳案例**：傣族寺庙建筑暗棕+金色，全图主色 `RGB(11,10,15)`（几乎黑色），建筑区域暖色平均 `RGB(132,98,69)`，提亮后 `RGB(158,127,89)` 暖棕色，与傣族建筑氛围完美匹配。

## 颜色提取（防 numpy uint8 溢出）

照片主色提取时，`r + g + b` 可能因 numpy uint8 溢出（max 255+255+255=765 > 255），报 `RuntimeWarning: overflow`。

**修复**：显式转换类型。

```python
from PIL import Image
import numpy as np
from collections import Counter

img = Image.open(photo_path)
# 裁掉底部人物区域（通常取上部 70%）
top = img.crop((0, 0, img.width, int(img.height * 0.7)))
top_small = top.resize((100, 75))
pixels = np.array(top_small).reshape(-1, 3)
counter = Counter([tuple(p) for p in pixels])

# 选背景色：跳过太暗/太白，找高饱和度
for color, count in counter.most_common(50):
    r, g, b = int(color[0]), int(color[1]), int(color[2])  # ← 关键：转 int 防溢出
    if max(r,g,b) < 30 or min(r,g,b) > 240:
        continue
    sat = max(r,g,b) - min(r,g,b)
    lum = (r + g + b) / 3
    if sat > 50 and 60 < lum < 200:
        print(f"BG: RGB({r},{g},{b}) #{r:02x}{g:02x}{b:02x} sat={sat} lum={lum:.0f}")
```

## API Key 获取

`~/.hermes/.env` 中 Key 显示为脱敏值（`***`），`config.yaml` 中显示为截断值（如 `sk-877...b8b8`），无法直接读取。

**获取方式**：
1. `hermes config get custom_providers` — 终端命令获取完整配置
2. 直接让用户提供 — 最快最可靠
3. 在 `.env` 以外存储：检查是否有 `APIKEY_FUN_KEY` 环境变量
