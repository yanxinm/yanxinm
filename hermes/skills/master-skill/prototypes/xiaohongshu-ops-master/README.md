# Prototype · 小红书运营

mini-viable 样本，验证内容运营行业 + 中文 locale。

## 目录内容

| 路径 | 说明 |
|---|---|
| `intake.json` | 行业澄清结果 |
| `references/research/0X-*.md` | 6 路调研笔记 (大部分为占位, 仅 03-workflows 完整) |
| `references/synthesis.md` | 蒸馏文档 |
| `output/SKILL.md` | 生成的 skill |
| `output/meta.json` | 元数据 |
| `output/cli/` | 自动生成的 bash 工具 |

## 蒸馏要点

- 3 心智模型: 内容种草不是销售 / 数据驱动迭代 / 信息流 ≠ 自然流
- 5 决策规则
- 3 研究维度 (内容差距 / 流量池判断 / 投流性价比)
- 2 工作流: 品牌新号冷启动 + 商单笔记生产

## 重新生成

```bash
python3 tools/skill_writer.py create \
  --skill-dir prototypes/xiaohongshu-ops-master/output \
  --intake prototypes/xiaohongshu-ops-master/intake.json \
  --synthesis prototypes/xiaohongshu-ops-master/references/synthesis.md \
  --template references/skill-template.md \
  --research-dir prototypes/xiaohongshu-ops-master/references/research
```
