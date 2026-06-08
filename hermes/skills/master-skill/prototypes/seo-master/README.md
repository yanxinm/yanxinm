# Prototype · SEO 专家

mini-viable 样本，验证半技术行业 (SEO) + 中文 locale。

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

- 3 心智模型: 用户意图先于关键词 / E-E-A-T 四象 / 技术 SEO 是地基
- 5 决策规则
- 3 研究维度 (SERP 当前状态 / 域名权重 / 算法更新影响)
- 2 工作流: 新站 SEO 上线 + 内容 SEO 单篇产出

## 重新生成

```bash
python3 tools/skill_writer.py create \
  --skill-dir prototypes/seo-master/output \
  --intake prototypes/seo-master/intake.json \
  --synthesis prototypes/seo-master/references/synthesis.md \
  --template references/skill-template.md \
  --research-dir prototypes/seo-master/references/research
```
