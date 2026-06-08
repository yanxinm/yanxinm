# Prototype · Cross-border ecommerce master (跨境电商运营)

v1.x mini-validation prototype. 用于验证:
1. zh-CN locale 行业 OS 生成
2. 非技术行业 CLI 工具流生成
3. cli_writer 跨行业 robustness (general-playbook 兜底)

**Scope**: mini-viable (3 mental models / 5 playbook rules / 3 protocol dims / 2 workflows). 完整版应有 13+ figures / 18+ tools / 7+ workflows.

## 目录内容

| 路径 | 说明 |
|---|---|
| `intake.json` | Phase 0A 行业澄清结果 |
| `references/research/0X-*.md` | 6 路调研笔记 (大部分为 stub, 仅 03-workflows 完整) |
| `references/synthesis.md` | Phase 2 提炼 |
| `output/SKILL.md` | Phase 3 生成的可装载 skill |
| `output/meta.json` | 元数据 |
| `output/cli/` | v0.6 自动生成的 bash 工具流 |

## 关键发现 (v1.x cross-industry)

cli_writer 原始 CLUSTER_KEYWORDS 是 LLM agent infra 专属 (framework / eval / RAG / observability / debug). 在跨境电商规则上 0 命中, 所有 5 条 playbook 规则全部 fall back 到 `general-playbook.sh`.

**结论**: clustering 是行业特化的, 但 fallback 机制正确兜住了. 长期看 v1.x 应该让 cluster 关键词从 synthesis 中自动学习, 不写死.

## 重新生成 output/

```bash
cd <repo-root>
python3 tools/skill_writer.py create \
  --skill-dir prototypes/cross-border-ecommerce-master/output \
  --intake prototypes/cross-border-ecommerce-master/intake.json \
  --synthesis prototypes/cross-border-ecommerce-master/references/synthesis.md \
  --template references/skill-template.md \
  --research-dir prototypes/cross-border-ecommerce-master/references/research
```
