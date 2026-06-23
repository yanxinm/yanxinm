---
name: hermes-profile-switching
description: "Hermes Profile 切换原则——何时切 profile、何时切回 default。适用于多角色 AI 团队协作场景。"
version: 1.0.0
author: hermes-agent
tags: [profile, switching, multi-role, team]
---

# Hermes Profile 切换原则

## 触发条件

任何涉及 Hermes Agent profile 切换的任务。

## 切换规则

| 场景 | 操作 |
|------|------|
| 日常对话 | 使用 `default` profile |
| 任务分配给子角色 | 切换到对应 profile（jike/wenan/lvyou/sheji/zhidu） |
| 专项长任务 | 切换到对应 profile，完成后**下一次新对话**切回 `default` |

## 子角色映射

| Profile | 职责 |
|---------|------|
| default | 总负责（H 本人） |
| jike | 极客——脚本、运维、技术问题 |
| wenan | 文案——报告、公文、写作 |
| lvyou | 旅游——行程、美食规划 |
| zhidu | 制度——考核、规章 |
| sheji | 设计师——海报、修图、视觉（image-2 出图） |

## 注意事项

- 切换前确认任务归属，不要频繁切换
- 专项任务完成后，提醒用户或在下一次对话开始时切回 default

## 模型路由规则（2026-06-22 起生效）

| Profile | 对话模型 | 视觉分析（看图） | 图像生成 |
|---------|----------|-----------------|---------|
| default | DeepSeek V4 Flash (deepseek provider) | Doubao (ark-doubao provider) | — |
| jike | DeepSeek V4 Flash | Doubao | — |
| lvyou | DeepSeek V4 Flash | Doubao (继承主配置) | — |
| sheji | DeepSeek V4 Flash | Doubao (继承主配置) | **gpt-image-2** via fun-codex (apikey-image-gen 技能) |
| wenan | DeepSeek V4 Flash | Doubao (继承主配置) | — |
| zhidu | DeepSeek V4 Flash | Doubao (继承主配置) | — |

### 说明

- **DeepSeek V4 Flash** 是所有 profile 的默认对话模型
- **Doubao**（`ark-doubao` provider, `doubao-seed-1-6-vision-250815`）负责所有视觉/看图任务。主配置中设置了 `auxiliary.vision`，未覆盖的 profile 自动继承
- **sheji** 出图走 `apikey-image-gen` 技能，通过 Hermes Web UI → fun-codex provider → gpt-image-2
- 主配置已定义 `ark-doubao` provider（ark.cn-beijing.volces.com），各 profile 无需重复
- 配置修改路径：`~/.hermes/config.yaml`（主配置）及各 `~/.hermes/profiles/<name>/config.yaml`
