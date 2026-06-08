# 心理咨询 / 心理治疗(临床实践者视角 — 接案与评估 / 个案概念化 / 主流流派技术(CBT 与第三浪潮 / 精神动力 / 人本存在 / 家庭系统 / 创伤治疗) / 伦理边界与危机干预 / 督导与个人成长 / 执业形态与经营 — 涵盖中国大陆行业现状 + 欧美持照体系,两套体系差异极大) CLI

把 心理咨询 / 心理治疗(临床实践者视角 — 接案与评估 / 个案概念化 / 主流流派技术(CBT 与第三浪潮 / 精神动力 / 人本存在 / 家庭系统 / 创伤治疗) / 伦理边界与危机干预 / 督导与个人成长 / 执业形态与经营 — 涵盖中国大陆行业现状 + 欧美持照体系,两套体系差异极大) master skill 的认知 OS 物化成 bash 工具。
不替代 SKILL.md（思维顾问），是它的「执行端」：交互问询 → 应用 playbook / protocol → 输出结构化报告。

## 用法

所有脚本支持 `--help` / `--explain` / `--dry-run` / `--json` 四个标准 flag。

```bash
# 拿到新问题时, 按 N 个研究维度做功课
./protocol/agentic.sh

# 决策树评估 (基于 playbook)
./decision/topic-1.sh
# SOP 走查 (workflow)
./workflow/50.sh

# 看背后的心智模型 / playbook (不交互)
./protocol/agentic.sh --explain
```

## 脚本清单

| 脚本 | 作用 |
|------|------|
| `protocol/agentic.sh` | Agentic Protocol (8 维度) — 拿到新问题时按这一行的研究维度做功课 |
| `decision/topic-1.sh` | —— 决策树 (9 条规则) |
| `decision/general-playbook.sh` | 通用 Playbook 决策树 (1 条规则) |
| `workflow/50.sh` | 单次会谈的结构（开场 → 工作 → 收尾，一次 50 分钟会谈怎么走） SOP 走查 |
| `workflow/workflow-1.sh` | 一个个案从接案评估到结案的完整弧线 SOP 走查 |
| `workflow/workflow-2.sh` | 个案概念化流程（把症状/史/关系/情境组织成可工作的理解 + 计划） SOP 走查 |
| `workflow/workflow-3.sh` | 危机干预流程（自杀 / 自伤 / 虐待 / 急性精神病性发作 的识别 → 评估 → 立即导向危机资源 / 转介 / 上级督导） SOP 走查 |
| `workflow/workflow-4.sh` | 转介流程（识别超出胜任力范围 / 需要其他资源 → 衔接到合适的同行或机构） SOP 走查 |
| `workflow/workflow-5.sh` | 伦理决策流程（遇到伦理两难——保密例外 / 双重关系 / 胜任力边界——怎么走） SOP 走查 |
| `workflow/locale.sh` | 从受训到独立执业的成长路径（欧美持照体系 locale） SOP 走查 |
| `workflow/locale.sh` | 从受训到独立执业的成长路径（中国大陆 locale） SOP 走查 |
| `workflow/workflow-6.sh` | 临床督导流程（带个案进督导 → 呈现 → 加工 → 把督导转化为下一次会谈的调整） SOP 走查 |

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
  --industry-cn "心理咨询 / 心理治疗(临床实践者视角 — 接案与评估 / 个案概念化 / 主流流派技术(CBT 与第三浪潮 / 精神动力 / 人本存在 / 家庭系统 / 创伤治疗) / 伦理边界与危机干预 / 督导与个人成长 / 执业形态与经营 — 涵盖中国大陆行业现状 + 欧美持照体系,两套体系差异极大)"
```
