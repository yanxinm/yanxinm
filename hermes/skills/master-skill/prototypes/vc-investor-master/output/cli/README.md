# 风险投资人 / 早期投资判断(GP + Principal — Deal sourcing / 尽调 / 估值与 term sheet / 投后服务 / 退出 + LP 关系与 fundraising — 涵盖 US 美元基金 + 国内 RMB / 美元基金) CLI

把 风险投资人 / 早期投资判断(GP + Principal — Deal sourcing / 尽调 / 估值与 term sheet / 投后服务 / 退出 + LP 关系与 fundraising — 涵盖 US 美元基金 + 国内 RMB / 美元基金) master skill 的认知 OS 物化成 bash 工具。
不替代 SKILL.md（思维顾问），是它的「执行端」：交互问询 → 应用 playbook / protocol → 输出结构化报告。

## 用法

所有脚本支持 `--help` / `--explain` / `--dry-run` / `--json` 四个标准 flag。

```bash
# 拿到新问题时, 按 N 个研究维度做功课
./protocol/agentic.sh

# 决策树评估 (基于 playbook)
./decision/deal.sh
# SOP 走查 (workflow)
./workflow/gp.sh

# 看背后的心智模型 / playbook (不交互)
./protocol/agentic.sh --explain
```

## 脚本清单

| 脚本 | 作用 |
|------|------|
| `protocol/agentic.sh` | Agentic Protocol (9 维度) — 拿到新问题时按这一行的研究维度做功课 |
| `decision/deal.sh` | Deal 决策树 (7 条规则) |
| `decision/topic-2.sh` | —— 决策树 (3 条规则) |
| `workflow/gp.sh` | 一个 GP / 投资人的一周(三尺度之「周」) SOP 走查 |
| `workflow/deal-inbound-close-deal.sh` | 一个 deal 从 inbound 到 close 的完整路径(三尺度之「一个 deal」) SOP 走查 |
| `workflow/fund-fundraising-exit-7-10-fund.sh` | 一个 fund 从 fundraising 到 exit 的 7-10 年生命周期(三尺度之「一个 fund」) SOP 走查 |
| `workflow/deal-sourcing-proprietary-deal-f.sh` | Deal sourcing — 建 proprietary deal flow SOP 走查 |
| `workflow/due-diligence-founder-reference-.sh` | Due diligence 深做(founder reference call / market sizing / cap table review) SOP 走查 |
| `workflow/term-sheet.sh` | Term sheet 谈判 + 估值 SOP 走查 |
| `workflow/board-service.sh` | 投后服务 / board service SOP 走查 |
| `workflow/portfolio-construction-reserve.sh` | Portfolio construction + reserve 策略 SOP 走查 |

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
  --industry-cn "风险投资人 / 早期投资判断(GP + Principal — Deal sourcing / 尽调 / 估值与 term sheet / 投后服务 / 退出 + LP 关系与 fundraising — 涵盖 US 美元基金 + 国内 RMB / 美元基金)"
```
