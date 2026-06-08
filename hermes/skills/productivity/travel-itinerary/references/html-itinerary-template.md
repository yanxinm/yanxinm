# HTML 行程单模板

用户偏好 HTML 而非 PDF（手机打开 PDF 乱码），单文件自包含。

## 设计规范

- 暖色系：背景 `#f5f0eb`，卡片白底 `#fff`，主题绿 `#2d5016`
- 手机优先：max-width 600px，padding 12px
- 字体：系统默认中文字体栈（PingFang SC, Microsoft YaHei, sans-serif）
- 卡片布局：每张卡片 border-radius 12px，margin-bottom 12px，轻阴影
- 表格：紧凑字号 12px，表头 `#f0ede8` 暖灰背景

## 关键 CSS 片段

```css
body{font-family:-apple-system,BlinkMacSystemFont,'PingFang SC','Microsoft YaHei',sans-serif;background:#f5f0eb;max-width:600px;margin:0 auto;padding:12px}
.card{background:#fff;border-radius:12px;padding:16px;margin-bottom:12px;box-shadow:0 1px 4px rgba(0,0,0,.08)}
.day-num{background:#2d5016;color:#fff;border-radius:8px;padding:2px 10px;font-size:13px;font-weight:700}
table{width:100%;border-collapse:collapse;font-size:12px}
th{background:#f0ede8;padding:6px 4px;font-weight:600;font-size:11px;border:1px solid #e8e3dc}
td{padding:6px 4px;border:1px solid #e8e3dc}
```

## 文件结构

1. `<h1>` 主标题（emoji前缀）
2. `<h2>` 副标题（路线摘要）
3. `.route` 日期+交通+路线一览
4. 每Day一个 `.card`，内含 `.day-header` + `.meta` + `<table>`
5. 费用 `.card` + `.cost-table`
6. 订房 `.card` + 优先级排序
7. 车程汇总 `.card` + `.summary-box`（深色背景块）
8. 美食 `.card` + 两列 grid
9. 预约 `.card` + 简洁表格
10. Checklist `.card` + 真实 `<input type="checkbox">`

## 生成工具

直接用 Python 写 HTML 字符串后 `write_file`，比 fpdf2 简单且手机效果好。
基地中文字体用 `/usr/share/fonts/opentype/noto/NotoSerifCJK-Bold.ttc`（如需要服务端渲染）。

## 发送

- 优先微信发送 `MEDIA:path`
- 微信限流时改飞书 `feishu:<chat_id>`
- 飞书 channel ID 通过 `send_message(action='list')` 获取
