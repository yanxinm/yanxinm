# SkillSpector Setup

SkillSpector (by NVIDIA) is a security scanner for AI agent skills. It detects vulnerabilities, malicious patterns, and policy risks before installing skills from external sources.

## Installation

```bash
cd ~
git clone https://github.com/nvidia/skillspector.git
cd skillspector
python3 -m venv .venv
source .venv/bin/activate
pip install hatchling -i https://mirrors.aliyun.com/pypi/simple/
pip install -e . -i https://mirrors.aliyun.com/pypi/simple/ --default-timeout=600
```

⚠️ **Pitfall (China network):** Use Aliyun mirror (`mirrors.aliyun.com`) — default PyPI is slow or blocked. Installation has 100+ dependencies including langgraph, langchain, anthropic, openai, grpcio, and may take 5-10 minutes.

⚠️ **Pitfall (Tencent Meeting):** If dpkg fails with `liblzma.so.5: version 'XZ_5.4' not found`, rename the conflicting library first:
```bash
sudo mv /opt/wemeet/lib/liblzma.so.5 /opt/wemeet/lib/liblzma.so.5.bak
```
Then retry the pip install. See `hermes-base-operations` §八 for details.

## Usage

```bash
# Activate venv first
source ~/skillspector/.venv/bin/activate

# Scan a local skill
skillspector scan ./my-skill/

# Scan a GitHub repo
skillspector scan https://github.com/user/skill-name --no-llm

# Output formats
skillspector scan ./skill/ --format json --output report.json
skillspector scan ./skill/ --format markdown --output report.md
skillspector scan ./skill/ --format sarif --output report.sarif  # CI/CD integration
```

## LLM Semantic Analysis (Optional)

For deeper semantic analysis, configure an LLM provider:

```bash
export SKILLSPECTOR_PROVIDER=openai
export OPENAI_API_KEY=***
skillspector scan ./my-skill/

# Or with Anthropic
export SKILLSPECTOR_PROVIDER=anthropic
export ANTHROPIC_API_KEY=***

# Skip LLM (static analysis only — faster)
skillspector scan ./my-skill/ --no-llm
```

## What It Detects

64 vulnerability patterns across 16 categories:

| Category | Examples |
|----------|----------|
| Prompt Injection | Instruction override, hidden instructions, exfiltration commands |
| Data Exfiltration | External transmission of context/data |
| Privilege Escalation | Overbroad permissions, sudo usage |
| Tool Misuse | Dangerous commands, shell escapes |
| Dangerous Code | AST analysis of Python/JS/shell |
| MCP Tool Poisoning | Malicious MCP server configs |

## Risk Scoring

- 0-100 scale
- Severity labels: CRITICAL, HIGH, MEDIUM, LOW
- Clear remediation recommendations per issue

## Workflow

Before installing any skill from GitHub or external source:

```bash
# 1. Scan first
skillspector scan https://github.com/user/skill-name --no-llm

# 2. Review report (risk score + issues)

# 3. If acceptable, install
hermes skills install https://github.com/user/skill-name
```

## Location

- Installed at: `~/skillspector/`
- Command: `source ~/skillspector/.venv/bin/activate && skillspector`
