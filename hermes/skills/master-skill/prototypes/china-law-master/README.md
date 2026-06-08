# Prototype · 法律执业（中国法）

mini-viable 样本，验证强监管 + 强专业行业。

**严肃声明**: 本 skill 给的是认知框架，绝不替代执业律师的法律意见。每个具体案件必须由律师评估 + 出具意见。

## 目录内容

| 路径 | 说明 |
|---|---|
| `intake.json` | 行业澄清结果 |
| `references/research/0X-*.md` | 6 路调研笔记（大部分占位，仅 03-workflows 完整） |
| `references/synthesis.md` | 蒸馏文档 |
| `output/SKILL.md` | 生成的 skill |
| `output/meta.json` | 元数据 |
| `output/cli/` | 自动生成的 bash 工具 |

## 蒸馏要点

- 3 心智模型：程序正义先于实体 / 证据决定胜负不是法条 / 风险防范优于事后救济
- 5 决策规则
- 3 研究维度（法律关系定性 / 程序前置审查 / 证据评估）
- 2 工作流：民商事案件立案前评估 + 商事合同审核流程

注意：本 prototype 仅适用中国大陆法语境，普通法系国家的法律执业逻辑有差异。

## 重新生成

```bash
python3 tools/skill_writer.py create \
  --skill-dir prototypes/china-law-master/output \
  --intake prototypes/china-law-master/intake.json \
  --synthesis prototypes/china-law-master/references/synthesis.md \
  --template references/skill-template.md \
  --research-dir prototypes/china-law-master/references/research
```
