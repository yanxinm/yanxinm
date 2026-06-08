# 求职 / 面试辅导(求职教练视角 — 求职定位与职业叙事 / 简历与 ATS 优化 / 求职渠道与内推策略 / 职场社交 / 行为面试与专业面试 / 面试心理与表达 / 谈薪与 offer 决策 / 校招与应届生 / 转行求职 / 特殊群体求职 / 求职教练的执业经营 — 涵盖中国大陆求职生态 + 海外英语区求职体系,两套差异极大) CLI

把 求职 / 面试辅导(求职教练视角 — 求职定位与职业叙事 / 简历与 ATS 优化 / 求职渠道与内推策略 / 职场社交 / 行为面试与专业面试 / 面试心理与表达 / 谈薪与 offer 决策 / 校招与应届生 / 转行求职 / 特殊群体求职 / 求职教练的执业经营 — 涵盖中国大陆求职生态 + 海外英语区求职体系,两套差异极大) master skill 的认知 OS 物化成 bash 工具。
不替代 SKILL.md（思维顾问），是它的「执行端」：交互问询 → 应用 playbook / protocol → 输出结构化报告。

## 用法

所有脚本支持 `--help` / `--explain` / `--dry-run` / `--json` 四个标准 flag。

```bash
# 拿到新问题时, 按 N 个研究维度做功课
./protocol/agentic.sh

# 决策树评估 (基于 playbook)
./decision/topic-1.sh
# SOP 走查 (workflow)
./workflow/workflow-1.sh

# 看背后的心智模型 / playbook (不交互)
./protocol/agentic.sh --explain
```

## 脚本清单

| 脚本 | 作用 |
|------|------|
| `protocol/agentic.sh` | Agentic Protocol (9 维度) — 拿到新问题时按这一行的研究维度做功课 |
| `decision/topic-1.sh` | —— 决策树 (5 条规则) |
| `decision/topic-2.sh` | 简历 决策树 (1 条规则) |
| `decision/topic-3.sh` | 面试 决策树 (1 条规则) |
| `decision/topic-4.sh` | 岗位 决策树 (1 条规则) |
| `decision/general-playbook.sh` | 通用 Playbook 决策树 (1 条规则) |
| `workflow/workflow-1.sh` | 国内校招求职弧线 SOP 走查 |
| `workflow/workflow-2.sh` | 国内社招求职弧线 SOP 走查 |
| `workflow/workflow-3.sh` | 海外求职弧线 SOP 走查 |
| `workflow/workflow-4.sh` | 单次面试的结构（准备 / 临场 / 复盘） SOP 走查 |
| `workflow/workflow-5.sh` | 求职定位与职业叙事流程 SOP 走查 |
| `workflow/jd.sh` | 简历优化流程（JD 拆解 → 量化成就 → 关键词 → 格式） SOP 走查 |
| `workflow/workflow-6.sh` | 谈薪流程 SOP 走查 |
| `workflow/workflow-7.sh` | 转行求职流程 SOP 走查 |
| `workflow/workflow-8.sh` | 求职教练的接案 / 服务流程 SOP 走查 |

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
  --industry-cn "求职 / 面试辅导(求职教练视角 — 求职定位与职业叙事 / 简历与 ATS 优化 / 求职渠道与内推策略 / 职场社交 / 行为面试与专业面试 / 面试心理与表达 / 谈薪与 offer 决策 / 校招与应届生 / 转行求职 / 特殊群体求职 / 求职教练的执业经营 — 涵盖中国大陆求职生态 + 海外英语区求职体系,两套差异极大)"
```
