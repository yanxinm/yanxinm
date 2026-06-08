# OpenCLI v1.7.22 — 安装经验与踩坑记录

## 安装方式

```bash
npm install -g @jackwener/opencli
# 成功输出: added 17 packages in 13s
```

执行文件位置：`~/.npm-global/bin/opencli`

## 版本信息

- opencli v1.7.22
- Node.js v23.11.0
- npm 10.9.2

## 基本功能验证

| 命令 | 结果 | 说明 |
|------|------|------|
| `opencli --version` | v1.7.22 | OK |
| `opencli doctor` | Daemon running, Browser extension 未连接（可选） | 核心功能正常 |
| `opencli list` | 813 commands / 143 sites / 12 external CLIs | OK |
| `opencli docker --help` | 正常透传 Docker CLI | 外部 CLI 桥接正常 |

## 踩坑记录

### 1. 部分网站适配器超时
- `opencli 36kr hot` → 在 WSL + 中国大陆环境超时（20s 无响应）
- 可能是 CDN 或防火墙问题，需要代理或设置更长的 timeout
- 建议：对国内站点适配器正常，对部分海外站点可能需要代理

### 2. Browser Bridge 不可用
- Chrome 扩展不连接不影响核心 CLI 功能
- 如需浏览器操控能力，需手动下载扩展并加载到 Chrome

### 3. Cookie 登录态
- 带 `[cookie]` 标记的命令首次使用会提示登录
- 目前环境未配置任何网站的登录 cookie

### 4. 与 Scrapling 的区别
- OpenCLI 适合"即用型"热榜/新闻/搜索（内置适配器）
- Scrapling 适合"自定义型"抓取（CSS 选择器、结构化输出、大规模爬虫）
- 两者互补，可混用

## 可用命令速查

```bash
# 按网站分组的命令数统计
opencli list | grep -c "\["
# 143 个站点

# 只显示公开（免登录）命令
opencli list | grep "public" | wc -l

# 按站点名搜索
opencli list | grep "zhihu"
opencli list | grep "36kr"
```
