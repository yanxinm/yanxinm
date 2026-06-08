# Prototype · LLM agent infra master

大师.skill v1.0 的端到端验证产物。Phase 0 → 4 全跑通，Phase 4 机械 rubric 10 pass / 1 partial / 0 fail。

## 目录内容

| 路径 | 说明 |
|---|---|
| `intake.json` | Phase 0A 行业澄清结果（输入） |
| `references/research/0X-*.md` | Phase 1 六轨调研笔记（输入） |
| `references/synthesis.md` | Phase 2 提炼（输入） |
| `output/SKILL.md` | Phase 3 生成的可装载 skill |
| `output/meta.json` | Phase 3 生成的元数据 |

## 如何重生成 output/

```bash
cd <repo-root>
python3 tools/skill_writer.py create \
  --skill-dir prototypes/llm-agent-infra-master/output \
  --intake prototypes/llm-agent-infra-master/intake.json \
  --synthesis prototypes/llm-agent-infra-master/references/synthesis.md \
  --template references/skill-template.md \
  --research-dir prototypes/llm-agent-infra-master/references/research

python3 tools/research/quality_check.py check \
  --skill-dir prototypes/llm-agent-infra-master/output
```

中间产物（synthesis-summary, quality-check-rubric, output/references/ 复刻）每次跑都会重新生成，不入版本库。
