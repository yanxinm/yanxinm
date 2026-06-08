# Prototype · 恋爱高手

mini-viable 样本，验证软技能 / 非工作类行业 + 中文 locale。

这个 prototype 检验大师.skill 框架对**心理学 / 软技能**类行业的适配性 — 不只能蒸馏技术或商业行业。

## 目录内容

| 路径 | 说明 |
|---|---|
| `intake.json` | 行业澄清结果 |
| `references/research/0X-*.md` | 6 路调研笔记 (大部分占位, 仅 03-workflows 完整) |
| `references/synthesis.md` | 蒸馏文档 |
| `output/SKILL.md` | 生成的 skill |
| `output/meta.json` | 元数据 |
| `output/cli/` | 自动生成的 bash 工具 |

## 蒸馏要点

- 3 心智模型: 价值感不是装的, 是活出来的 / 双向选择市场 / 需求要直接说
- 5 决策规则
- 3 研究维度 (自我状态 / 对方信号 / 互动模式)
- 2 工作流: 单身期自我建设 + 关系冲突修复

注意：本 skill 给的是认知框架, 不替代心理咨询. 真正的心理问题需要专业咨询师.

## 重新生成

```bash
python3 tools/skill_writer.py create \
  --skill-dir prototypes/love-coach-master/output \
  --intake prototypes/love-coach-master/intake.json \
  --synthesis prototypes/love-coach-master/references/synthesis.md \
  --template references/skill-template.md \
  --research-dir prototypes/love-coach-master/references/research
```
