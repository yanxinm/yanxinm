# AI 产品经理 (LLM 应用 / 生成式 AI / Agent 产品 / Copilot 嵌入 — 跨模型评估 / 工作流设计 / 产品-工程协同) CLI

把 AI 产品经理 (LLM 应用 / 生成式 AI / Agent 产品 / Copilot 嵌入 — 跨模型评估 / 工作流设计 / 产品-工程协同) master skill 的认知 OS 物化成 bash 工具。
不替代 SKILL.md（思维顾问），是它的「执行端」：交互问询 → 应用 playbook / protocol → 输出结构化报告。

## 用法

所有脚本支持 `--help` / `--explain` / `--dry-run` / `--json` 四个标准 flag。

```bash
# 拿到新问题时, 按 N 个研究维度做功课
./protocol/agentic.sh

# 决策树评估 (基于 playbook)
./decision/topic-1.sh
# SOP 走查 (workflow)
./workflow/scoping-ai-feature.sh

# 看背后的心智模型 / playbook (不交互)
./protocol/agentic.sh --explain
```

## 脚本清单

| 脚本 | 作用 |
|------|------|
| `protocol/agentic.sh` | Agentic Protocol (7 维度) — 拿到新问题时按这一行的研究维度做功课 |
| `decision/topic-1.sh` | —— 决策树 (7 条规则) |
| `decision/agent.sh` | Agent 决策树 (1 条规则) |
| `decision/topic-3.sh` | 模型 决策树 (1 条规则) |
| `decision/eval.sh` | Eval 决策树 (1 条规则) |
| `workflow/scoping-ai-feature.sh` | Scoping 一个 AI feature（「想法」阶段） SOP 走查 |
| `workflow/poc-poc.sh` | POC / 原型验证（「想法 → POC」） SOP 走查 |
| `workflow/0-eval-poc-mvp.sh` | 从 0 搭起 eval 体系（POC → MVP 之间的前置门） SOP 走查 |
| `workflow/eval-driven-mvp.sh` | Eval-driven 迭代循环（MVP → 生产的主循环） SOP 走查 |
| `workflow/agent-0-ship-high-decay.sh` | Agent 产品从 0 到可 ship（high decay） SOP 走查 |
| `workflow/high-decay.sh` | 搭数据飞轮（「生产 → 数据飞轮」，high decay） SOP 走查 |

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
  --industry-cn "AI 产品经理 (LLM 应用 / 生成式 AI / Agent 产品 / Copilot 嵌入 — 跨模型评估 / 工作流设计 / 产品-工程协同)"
```
