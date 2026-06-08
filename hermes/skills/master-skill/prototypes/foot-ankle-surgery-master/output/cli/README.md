# 足踝外科 CLI

把 足踝外科 master skill 的认知 OS 物化成 bash 工具。
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
| `protocol/agentic.sh` | Agentic Protocol (5 维度) — 拿到新问题时按这一行的研究维度做功课 |
| `decision/topic-1.sh` | 手术 决策树 (4 条规则) |
| `decision/topic-2.sh` | 患者 决策树 (2 条规则) |
| `decision/topic-3.sh` | 期望 决策树 (1 条规则) |
| `decision/general-playbook.sh` | 通用 Playbook 决策树 (2 条规则) |
| `workflow/workflow-1.sh` | 急性踝扭伤评估 + 保守治疗启动 SOP 走查 |
| `workflow/workflow-2.sh` | 慢性足底筋膜炎管理 SOP 走查 |
| `workflow/hallux-valgus.sh` | 拇外翻 (Hallux Valgus) 评估 + 决策 SOP 走查 |
| `workflow/achilles-rupture.sh` | 跟腱断裂 (Achilles Rupture) 评估 + 治疗决策 SOP 走查 |
| `workflow/vs.sh` | 终末期踝关节炎 — 关节置换 vs 关节融合 决策 SOP 走查 |

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
  --industry-cn "足踝外科"
```
