# 抖音直播带货 (商家 / 主播 / 直播间运营 + 千川 / 巨量引擎广告投放 + 选品 + 流量场承接 + 合规) CLI

把 抖音直播带货 (商家 / 主播 / 直播间运营 + 千川 / 巨量引擎广告投放 + 选品 + 流量场承接 + 合规) master skill 的认知 OS 物化成 bash 工具。
不替代 SKILL.md（思维顾问），是它的「执行端」：交互问询 → 应用 playbook / protocol → 输出结构化报告。

## 用法

所有脚本支持 `--help` / `--explain` / `--dry-run` / `--json` 四个标准 flag。

```bash
# 拿到新问题时, 按 N 个研究维度做功课
./protocol/agentic.sh

# 决策树评估 (基于 playbook)
./decision/general-playbook.sh
# SOP 走查 (workflow)
./workflow/workflow-1.sh

# 看背后的心智模型 / playbook (不交互)
./protocol/agentic.sh --explain
```

## 脚本清单

| 脚本 | 作用 |
|------|------|
| `protocol/agentic.sh` | Agentic Protocol (7 维度) — 拿到新问题时按这一行的研究维度做功课 |
| `decision/general-playbook.sh` | 通用 Playbook 决策树 (9 条规则) |
| `workflow/workflow-1.sh` | 跑一场完整直播（场前选品 → 场前预热 → 场中节奏 → 场后复盘） SOP 走查 |
| `workflow/0-1-1-10-10-100.sh` | 商家从入驻到稳定输出（0→1 / 1→10 / 10→100 三阶段全生命周期） SOP 走查 |
| `workflow/workflow-2.sh` | 千川直播间冷启动投放 SOP 走查 |
| `workflow/0.sh` | 新账号起号（0 粉到稳定出单） SOP 走查 |
| `workflow/workflow-3.sh` | 直播复盘与下一场优化 SOP 走查 |
| `workflow/workflow-4.sh` | 直播间合规自查 SOP 走查 |

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
  --industry-cn "抖音直播带货 (商家 / 主播 / 直播间运营 + 千川 / 巨量引擎广告投放 + 选品 + 流量场承接 + 合规)"
```
