# 公众号写作助手 (微信公众号文章 全链路 — 选题 / 标题 / 开篇 / 结构 / 行文 / 排版 / 配图 / 推送 / 涨粉 / 留言 / 二次传播 / 变现, 单 artifact = 一篇公众号推文) CLI

把 公众号写作助手 (微信公众号文章 全链路 — 选题 / 标题 / 开篇 / 结构 / 行文 / 排版 / 配图 / 推送 / 涨粉 / 留言 / 二次传播 / 变现, 单 artifact = 一篇公众号推文) master skill 的认知 OS 物化成 bash 工具。
不替代 SKILL.md（思维顾问），是它的「执行端」：交互问询 → 应用 playbook / protocol → 输出结构化报告。

## 用法

所有脚本支持 `--help` / `--explain` / `--dry-run` / `--json` 四个标准 flag。

```bash
# 拿到新问题时, 按 N 个研究维度做功课
./protocol/agentic.sh

# 决策树评估 (基于 playbook)
./decision/voice.sh
# SOP 走查 (workflow)
./workflow/0-single-article-production.sh

# 看背后的心智模型 / playbook (不交互)
./protocol/agentic.sh --explain
```

## 脚本清单

| 脚本 | 作用 |
|------|------|
| `protocol/agentic.sh` | Agentic Protocol (5 维度) — 拿到新问题时按这一行的研究维度做功课 |
| `decision/voice.sh` | Voice 决策树 (1 条规则) |
| `decision/topic-2.sh` | 数据 决策树 (2 条规则) |
| `decision/general-playbook.sh` | 通用 Playbook 决策树 (5 条规则) |
| `workflow/0-single-article-production.sh` | 单篇推文 0 → 推送 (Single-Article Production) SOP 走查 |
| `workflow/0-long-term-account-growth.sh` | 一个号 0 → 商业化 (Long-term Account Growth) SOP 走查 |
| `workflow/monetization-pipeline.sh` | 变现路径选择 + 接入 (Monetization Pipeline) SOP 走查 |

## 设计与生成

CLI 子树由 `tools/cli_writer.py` 自动从 `references/synthesis.md` (Section 2 Playbook + Section 9 Agentic Protocol) 和 `references/research/03-workflows.md` 生成。

完整 spec 在 master-skill 仓库 `references/cli-spec.md`。

## 重新生成

如果 synthesis.md 或 03-workflows.md 更新了, 重跑:

```bash
python3 <master-skill>/tools/cli_writer.py emit \
  --skill-dir <this-skill-dir> \
  --synthesis references/synthesis.md \
  --workflows references/research/03-workflows.md \
  --industry-cn "公众号写作助手 (微信公众号文章 全链路 — 选题 / 标题 / 开篇 / 结构 / 行文 / 排版 / 配图 / 推送 / 涨粉 / 留言 / 二次传播 / 变现, 单 artifact = 一篇公众号推文)"
```
