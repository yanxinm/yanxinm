# Prototype · 足踝外科

mini-viable 样本，验证医疗强监管行业。

**严肃声明**: 本 skill 给的是认知框架，绝不替代执业医生的临床判断。每个具体患者必须由执业医生面诊 + 完整评估再决定方案。

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

- 3 心智模型：保守治疗优先于手术 / 影像学 ≠ 临床症状原因 / 骨与软组织失衡是大多数慢性足踝痛的根源
- 5 决策规则
- 3 研究维度（病史 + 临床体征 / 影像学解读 / 治疗路径选择）
- 2 工作流：急性踝扭伤评估 + 慢性足底筋膜炎管理

## 重新生成

```bash
python3 tools/skill_writer.py create \
  --skill-dir prototypes/foot-ankle-surgery-master/output \
  --intake prototypes/foot-ankle-surgery-master/intake.json \
  --synthesis prototypes/foot-ankle-surgery-master/references/synthesis.md \
  --template references/skill-template.md \
  --research-dir prototypes/foot-ankle-surgery-master/references/research
```
