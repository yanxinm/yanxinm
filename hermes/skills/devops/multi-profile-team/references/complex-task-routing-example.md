# 复杂任务路由示例：财务工作量与绩效分析 → 考核细化方案

> 来源：2026-06-11 会话，老缪要求"调用制度员出来"分析三年财务数据

## 触发场景

用户说类似："调用制度员/文墨/路书/螺丝刀出来，扫描2024年开始的财务文件夹，分析工作量统计和绩效发放规律，形成考核方案。"

## 总负责执行步骤

### Step 1: 扫描文件目录

```bash
# 查找财务文件夹
find /home/miao/工作台账/ -maxdepth 2 -iname '*财务*' -o -iname '*绩效*' -o -iname '*工作量*' -o -iname '*考核*'

# 逐层查看子目录内容
ls -la "/home/miao/工作台账/2024/财务/"
ls -la "/home/miao/工作台账/2024/财务/绩效/"
ls -la "/home/miao/工作台账/2024/财务/绩效/工作量/"
ls -la "/home/miao/工作台账/2024/财务/绩效/经管/"
# ... 同理 2025/2026
```

### Step 2: 构建完整文件清单

按"考核方案类 / 工作量统计 / 绩效分配 / 年终分配 / 经营数据"分类整理，每类标注年份和人员信息。

### Step 3: 用 delegate_task 路由

```python
delegate_task(
  goal="分析任务目标（详见 context）",
  context=f'''
你是老缪的制度起草与考核设计专家（规尺）。
现需分析2024-2026年财务文件夹数据：

## 一、考核方案类（先读这些了解框架）
2024年: /home/miao/工作台账/2024/财务/2024年紫金山事业部考核方案.doc 等
2025年: ...
2026年: ...

## 二、工作量统计（核心数据）
2024年月度（人员：吴若菡、刘静颐、孙玥...）:
- /home/miao/工作台账/2024/财务/绩效/工作量/（24.01）工作量统计表...xls
- /home/miao/工作台账/2024/财务/绩效/工作量/4月工作量汇总（吴、刘、孙）.xlsx
- ...（逐月列全）

2025年月度（人员：吴、孙）:
- /home/miao/工作台账/2025/财务/绩效/工作量及结项/吴、孙1月工作量.xlsx
- ...

2026年月度:
- /home/miao/工作台账/2026/财务/工作量/2026年工作量1月.xlsx
- ...

## 三、绩效分配表
2024年经管绩效分配（逐月）:
- /home/miao/工作台账/2024/财务/绩效/经管/2024年1月紫金山事业部绩效分配表--经管2.18.xlsx
- ...
2025年绩效分配表:
- /home/miao/工作台账/2025/财务/绩效/绩效分配表/202501紫金山事业部（不含旅游）.xlsx
- /home/miao/工作台账/2025/财务/绩效/绩效分配表/2025年度紫金山事业部绩效总表.xlsx
2026年:
- ...

## 四、年终分配
- ...

## 分析要求
Step 1: 读考核方案（doc/docx/pdf）了解指标体系和权重
Step 2: 用 Python (openpyxl/xlrd) 读取 xlsx/xls 提取每月工作量数值
Step 3: 用 Python 读取绩效分配表，关联工作量与绩效
Step 4: 找出规律：人均基准、绩效/工作量相关系数、季节波动
Step 5: 输出考核细化方案（Markdown，写至 /home/miao/工作台账/文件名.md）

所有建议必须基于数据。引用时标注来源路径。
输出中文。
  ''',
  toolsets=["terminal", "file", "web"]
)
```

### Step 4: 验证输出

```bash
# 确认目标文件已生成
wc -l /home/miao/工作台账/紫金山事业部考核细化方案_2026.md
```

### Step 5: 多角色接力——wenan 润色 + docx 转换（可选）

分析完成后，如需生成正式公文版本，可接力调用第二个 profile：

```python
# 第一步：wenan 润色 Markdown 为正式公文格式
delegate_task(
  goal="以文墨（文案员）身份，将考核细化方案润色为正式公文格式",
  context='''
你是老缪的文案专家（文墨）。源文件在 /home/miao/工作台账/紫金山事业部考核细化方案_2026.md。
请：
1. 读取该文件
2. 改为正式公文格式（一、（一）1. 编号体系）
3. 开头用"为贯彻落实……"标准公文起手式
4. 结尾加落款（紫金山事业部 + 日期）
5. 去掉"起草人"等非正式表述
6. 输出至 /home/miao/工作台账/..._正式稿.md
''',
  toolsets=["file", "terminal"]
)

# 第二步：转为 .docx
from hermes_tools import terminal
result = terminal(
  command="python3 scripts/convert-markdown-to-gov-docx.py /home/miao/工作台账/紫金山事业部考核细化方案_2026_正式稿.md",
  workdir="/home/miao/.hermes/skills/productivity/laomiao-writing-style"
)
```

## 关键工具：读取遗留格式文件

| 文件类型 | 工具 | 命令 |
|---------|------|------|
| .xlsx | Python openpyxl | `python3 -c "import openpyxl; wb=openpyxl.load_workbook('f.xlsx'); ws=wb.active; [print(c.value) for r in ws.iter_rows() for c in r]"` |
| .xls (旧版) | Python xlrd | `python3 -c "import xlrd; wb=xlrd.open_workbook('f.xls'); ws=wb.sheet_by_index(0); [print(c.value) for r in ws.get_rows() for c in r]"` |
| .doc (旧版) | antiword | `antiword file.doc` |
| .docx | python-docx 或 markitdown | 或 `python3 -c "from docx import Document; d=Document('f.docx'); [print(p.text) for p in d.paragraphs]"` |
| 搜索文件 | search_files | 用 pattern 匹配文件名 |

## 方案输出结构（参考）

考核细化方案通常包含：
1. 现状诊断 — 核心问题列表（营收趋势、人均效能、固定成本占比）
2. 考核指标细化 — 双轨制+多维度框架，含各岗位量化指标
3. 工作量计量标准 — 统一计分体系，建议月基准值
4. 绩效分配模型 — 三层分配（基础+工作量+项目分成）
5. 营收挂钩机制 — 阶梯上缴方案
6. 人员定编与人均效能目标
7. 实施步骤 — 四阶段推进计划
8. 风险提示

## 坑

- 子 agent 无 memory，context 必须写全所有文件路径
- xls (旧版) 和 xlsx (新版) 需不同 Python 库（xlrd vs openpyxl）
- .doc 文件不可用 python-docx 读，需 antiword 或 catdoc
- 子 agent 自述"文件已生成"后，总负责必须 read_file 确认
- 输出语言默认英文，必须在 context 中显式写"输出中文"
