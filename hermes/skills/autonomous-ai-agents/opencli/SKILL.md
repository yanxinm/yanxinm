---
name: opencli
description: OpenCLI — 把任意网站和外部 CLI 变成标准化命令行接口，内置 143 个站点 × 813 条命令 + 12 个外部 CLI 桥接。
version: 1.0.0
author: Hermes Agent
license: MIT
platforms: [linux, macos]
metadata:
  hermes:
    tags: [CLI, Web, Browser, Automation, Skills, Scraping]
    related_skills: [scrapling, duckduckgo-search]
    homepage: https://github.com/jackwener/opencli
prerequisites:
  commands: [node, npm, opencli]
---

# OpenCLI

[OpenCLI](https://github.com/jackwener/opencli) by @jackwener — 将任意网站和 Electron 应用转为 CLI 工具，为 AI Agent 提供标准化接口。

## 安装

```bash
npm install -g @jackwener/opencli
```

## 快速验证

```bash
opencli --version                    # v1.7.22
opencli doctor                       # 诊断（浏览器桥接可选）
opencli list                         # 列出所有可用命令（813条）
opencli list | grep "public"         # 只看免登录的公开命令
```

## 功能概览

### 140+ 网站适配器（部分）

| 站点 | 命令示例 | 说明 |
|------|---------|------|
| 36氪 | `opencli 36kr hot` | 热榜 |
| 知乎 | `opencli zhihu hot` | 热榜 |
| 一亩三分地 | `opencli 1point3acres hot` | 今日热门 |
| arXiv | `opencli arxiv search --query 'llm'` | 论文搜索 |
| Amazon | `opencli amazon bestsellers` | 畅销榜 |
| AIbase | `opencli aibase news` | AI行业日报 |
| 百度学术 | `opencli baidu-xueshu search --query 'AI'` | 学术搜索 |
| BBC News | `opencli bbc-news news` | 新闻头条 |
| Hacker News | `opencli hacker-news top` | 热门 |

### 12 个外部 CLI 桥接

| CLI | 命令 | 状态 |
|-----|------|------|
| Docker | `opencli docker ps` | installed |
| Vercel | `opencli vercel list` | installed |
| GitHub CLI | `opencli gh pr list` | auto-install |
| Notion | `opencli ntn search` | auto-install |
| Obsidian | `opencli obsidian search` | auto-install |
| Lark/飞书 | `opencli lark-cli msg` | auto-install |
| 企业微信 | `opencli wecom-cli` | auto-install |
| 微信 | `opencli wx` | auto-install |
| Telegram | `opencli tg` | auto-install |
| Discord | `opencli discord` | auto-install |
| DingTalk | `opencli dws` | auto-install |
| Longbridge | `opencli longbridge` | auto-install |

## 使用示例（Shell）

```bash
# 一键获取热榜
opencli 36kr hot

# 搜索 arXiv 论文
opencli arxiv search --query 'large language model' --limit 5

# 获取知乎热榜
opencli zhihu hot

# 通过 CLI 桥接操作 Docker
opencli docker ps -a

# 列出所有外部 CLI
opencli list | grep "external CLI"
```

## 使用示例（Hermes execute_code）

```python
from hermes_tools import terminal

# 获取 AI 行业日报
result = terminal("opencli aibase news", timeout=30)
print(result)

# 搜索 arXiv
result = terminal(
    "opencli arxiv search --query 'multimodal' --limit 3",
    timeout=30
)
```

## Browser Bridge（可选）

如需浏览器操控能力，需安装 Chrome 扩展：

```bash
opencli daemon status          # 确认守护进程运行
opencli doctor                 # 查看连接状态
```

扩展下载：https://github.com/jackwener/opencli/releases

## 注意事项

- **网络依赖**：国内访问部分海外站点（arXiv、36kr 热榜、Amazon 等）可能超时，建议设置 `timeout=30` 或走代理
- **Cookie 登录**：带 `[cookie]` 标记的命令需要登录态，首次使用按提示完成验证
- **超时**：部分适配器首次访问可能较慢（36kr hot 曾在 WSL 下超时 20s）
- **守护进程**：`opencli daemon` 自动管理，`opencli doctor` 可查看连接状态
- **版本**：当前安装 v1.7.22
- **与 Scrapling 互补**：热榜/新闻用 OpenCLI 一行搞定，自定义抓取用 Scrapling
- **参考文件**：`references/install-notes.md` 记录了安装验证和踩坑详情

## 与 Scrapling 对比

| 场景 | 推荐工具 | 原因 |
|------|---------|------|
| 热榜/新闻/搜索 | **OpenCLI** | 内置适配器，一行命令 |
| 自定义抓取 + CSS 选择 | **Scrapling** | 灵活可控，可输出 JSON |
| 大规模爬虫 | **Scrapling Spider** | 并发 + 断点续爬 |
| Cloudflare 过盾 | **Scrapling Stealth** | 浏览器反指纹 |
