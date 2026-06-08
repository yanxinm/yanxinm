# 微信私域运营 (企微 + 个人号 + 公众号 + 视频号 + 小程序 + 朋友圈 + 社群 全链路 — 引流 / 沉淀 / 触达 / 转化 / 复购 / 裂变) CLI

把 微信私域运营 (企微 + 个人号 + 公众号 + 视频号 + 小程序 + 朋友圈 + 社群 全链路 — 引流 / 沉淀 / 触达 / 转化 / 复购 / 裂变) master skill 的认知 OS 物化成 bash 工具。
不替代 SKILL.md（思维顾问），是它的「执行端」：交互问询 → 应用 playbook / protocol → 输出结构化报告。

## 用法

所有脚本支持 `--help` / `--explain` / `--dry-run` / `--json` 四个标准 flag。

```bash
# 拿到新问题时, 按 N 个研究维度做功课
./protocol/agentic.sh

# 决策树评估 (基于 playbook)
./decision/topic-1.sh
# SOP 走查 (workflow)
./workflow/0-0-1.sh

# 看背后的心智模型 / playbook (不交互)
./protocol/agentic.sh --explain
```

## 脚本清单

| 脚本 | 作用 |
|------|------|
| `protocol/agentic.sh` | Agentic Protocol (6 维度) — 拿到新问题时按这一行的研究维度做功课 |
| `decision/topic-1.sh` | 私域 决策树 (7 条规则) |
| `decision/topic-2.sh` | —— 决策树 (3 条规则) |
| `workflow/0-0-1.sh` | 从 0 启动一个商家的私域（0→1 冷启动） SOP 走查 |
| `workflow/sop.sh` | 公转私漏斗：把公域流量承接进私域（核心 SOP） SOP 走查 |
| `workflow/1v1-sop-sop.sh` | 1v1 触达 SOP：加好友后的标准化私聊触达（核心 SOP） SOP 走查 |
| `workflow/sop-sop.sh` | 社群运营 SOP：从建群到群内转化（核心 SOP） SOP 走查 |
| `workflow/sop-sop.sh` | 朋友圈 SOP：发圈内容矩阵与节奏（核心 SOP） SOP 走查 |
| `workflow/1-10.sh` | 稳定运营期：搭标签体系 + 跑复购 / 会员（1→10 精细化） SOP 走查 |
| `workflow/10-100.sh` | 规模化：私域团队 + 多触点 + 数据归因体系（10→100） SOP 走查 |
| `workflow/workflow-1.sh` | 个人号矩阵迁移到企业微信（一次性迁移工程） SOP 走查 |

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
  --industry-cn "微信私域运营 (企微 + 个人号 + 公众号 + 视频号 + 小程序 + 朋友圈 + 社群 全链路 — 引流 / 沉淀 / 触达 / 转化 / 复购 / 裂变)"
```
