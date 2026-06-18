# Article Interpretation Format

Use this reference when producing Chinese deep-reading documents for scientific papers.

## Navigation

- Target Tone
- Required Sections
- Markdown Skeleton

## Target Tone

Write as a rigorous but readable Chinese research-public-account article:

- Start from the real scientific bottleneck, then make the mechanism understandable to non-specialists.
- Keep the "story" vivid, but make claims evidence-bound.
- Use repeated logic labels such as "核心问题", "解决方案", "关键信息", "支撑", "结论/意义".
- Use concise Chinese paragraphs. Avoid overlong machine-translated sentences.
- Use data whenever the paper provides data. If a number is not available, describe the trend and name the figure/section.
- Do not include private promotion, QR-code style endings, or unrelated personal branding unless the user explicitly asks for a公众号尾声.

## Required Sections

Use these sections in this order unless the user asks for a shorter or customized version.

### 1. 论文基本信息

Include:

- 论文标题（英文原文）
- 中文翻译
- 作者（主要作者+机构）
- 期刊名称
- 发表日期
- DOI 链接

### 2. 科研故事大白话版：非专业人士看

Write 2-4 approachable paragraphs explaining:

- What practical/scientific problem the paper addresses.
- Why previous thinking or methods were insufficient.
- What new angle the authors used.
- What was found and why it matters.

Then add "灵魂五问：" with exactly five Q/A items:

If the user provides a custom overview image for this section, insert it immediately after the "灵魂五问：" line:

`![灵魂五问总览图](figures/soul-five-questions.png)`

1. 他们想解决什么大问题？
2. 以前方法有什么不给力的地方？
3. 他们想到了什么新点子或用了什么新招数？
4. 结果怎么样？
5. 这项研究牛在哪？或者说，它可能有什么用处？

### 3. 论证结构审视：批判性思维框架

Use these labels:

- 核心问题（Problem）
- 解决方案（Solution/Strategy）
- 核心创新 B（机制创新） or an equivalent core innovation label
- 分创新 C1（方法/结构创新）
- 分创新 C2（性能/机制创新）
- 论证逻辑（Premises/Reasons）

The "论证逻辑" paragraph should form a chain from characterization to performance, in situ/operando evidence, theory/simulation, and final mechanism, adjusted to the paper.

### 4. 核心故事一句话凝练：创新组合范式

Include:

- 创新组合：核心创新【...】 + 分创新1【...】 + 分创新2【...】
- 一句话故事：one long but readable sentence linking problem, mechanism/strategy, performance result, and mechanistic relationship.

### 5. 题目解读

Include:

- 范式分析
- 核心创新点提炼
- 趣味性/吸引力评估

Explain why the title is effective or weak: problem-answer framing, scope, strong verb, novelty signal, and editorial appeal.

### 6. 摘要解读：五步法分析

Use exactly these five labels:

- 背景意义
- 存在的科学问题/挑战
- 本文方法/策略（核心创新点）
- 主要结果/发现（分创新点1和2及数据）
- 结论/意义

The "主要结果" part should separate sub-innovation 1 and sub-innovation 2 when possible.

### 7. 结论解读：摘要精炼版

Condense the paper's conclusion into:

- 本文方法/策略（核心创新点）
- 主要结果/发现（分创新点1和分创新点2及数据）
- 结论/意义

This section should feel shorter and more decisive than the abstract interpretation.

### 8. 图表解读：支撑核心与分创新点

Start with "图表布局逻辑" and summarize the figure narrative arc.

For each main figure:

- Insert the original figure image before the overall interpretation using Markdown image syntax: `![Fig. X. Source figure from the paper](figures/FigX.png)`.
- `Fig. X 整体解读`: state the core question answered by the figure and how it supports the main innovation.
- `子图详细解读`: for each panel or panel group, use this pattern:
  - `a:` or `a-b:` what it shows.
  - `关键信息：` the trend/data/observation.
  - `支撑：` which mechanism, method innovation, or performance claim it supports.

If the paper has many supplementary figures, only include those essential to the central evidence chain unless the user asks for exhaustive coverage.

Use publisher-provided figures when possible. If only PDF assets are available, render or crop the figure region from the PDF so labels, axes, and vector text are preserved.

### 9. 结果与讨论解读：总-分-总结构与 P-I-E-C 法则

Include:

- 总体结构（总-分-总）
- 分论部分 P-I-E-C 详解

Use P-I-E-C as:

- P（Point）：paragraph claim.
- I（Illustration）：specific data/figure evidence.
- E（Explanation）：mechanistic explanation.
- C（Connection）：how it connects to the next question or the paper's central claim.

Pick representative figures/sections if the paper is long.

### 10. 引言解读：漏斗式3-5步下楼梯模型分析

Break the introduction into 3-5 "下楼梯" moves:

- 第一轮下楼梯
- 第二轮下楼梯
- 第三轮下楼梯
- 第四轮下楼梯, if present
- 最终目的地（末段总结）

Each move should describe 起/承/转/合: broad background, current route, unresolved gap, and the paper's entry point.

### 11. 材料与方法解读：SOP 卡片法

Use:

- 方法名称与目标
- 核心原理
- 关键要素清单
- 操作流程与关键控制点
- 结果验证标准
- 创新点/独门秘籍

Write this as if helping a researcher understand how to reproduce the key method, while avoiding unsafe or over-specific operational advice for hazardous procedures.

### 12. 整体评价与思考

Include:

- 亮点总结
- 潜在不足/可改进之处

List 3-5 concrete strengths and 3-5 concrete limitations or future validation needs.

### 13. 三重境界：核心带走信息（The Three-Horizon Take-Home Messages）

Use three horizons:

- 第一重：科学之“术”（The Art of Science）
  - 一句话知识晶体
  - 思考引导
  - 创新方案包
- 第二重：叙事之“法”（The Method of Narrative）
  - 黄金证据链复盘
  - 全场最佳“神操作”
- 第三重：应用之“道”（The Way of Application）
  - 我的“下一个实验”清单
  - 撬动未来的“新支点”

Make this final section insightful and forward-looking. Do not overclaim beyond the evidence.

### 14. 文献内化卡片

End every full interpretation with a compact "文献内化卡片". This is the user's one-page learning artifact, written for memory, reuse, and research transfer.

Use these labels in this order:

- 文献标题
- 一句话故事
- 核心科学问题
- 关键机制链
- 最关键的三张图
- 最强证据
- 最大漏洞
- 可迁移价值
- 可借鉴表达

Writing rules:

- Keep the whole card concise, preferably 500-900 Chinese characters.
- Use the user's framing: "这篇文章通过什么策略，解决了什么问题，证明了什么机制？"
- For "核心科学问题", name the real contradiction behind the study, not only the surface topic.
- For "关键机制链", follow `结构变化 → 电子结构变化 → 中间体吸附变化 → 反应路径变化 → 性能变化` when the paper supports it. If a link is not directly studied, write a short caveat such as "中间体吸附：本文未直接测量，用机制图/理论推断支撑".
- For "最关键的三张图", choose exactly three figures and state what each proves.
- For "最大漏洞", write as a reviewer-style question, specific to the paper.
- For "可借鉴表达", include useful title logic, figure naming logic, paragraph logic, or one short reusable sentence pattern. Avoid long quotations from the paper.

Rendering note: when using `scripts/render_cn_interpretation_docx.py`, this section is rendered as a hand-drawn-card inspired block: bold black heading, red accent line, yellow marker-like label shading, and a compact boxed layout. Do not add screenshots of the card unless the user explicitly asks for an image asset.

## Markdown Skeleton

Use this skeleton before rendering to DOCX:

```markdown
# 中文解读标题

## 1. 论文基本信息

论文标题（英文原文）：...

中文翻译：...

作者（主要作者+机构）：...

期刊名称：...

发表日期：...

DOI 链接：...

## 2. 科研故事大白话版：非专业人士看

...

灵魂五问：

他们想解决什么大问题？ ...

以前方法有什么不给力的地方？ ...

他们想到了什么新点子或用了什么新招数？ ...

结果怎么样？ ...

这项研究牛在哪？或者说，它可能有什么用处？ ...

## 3. 论证结构审视：批判性思维框架

核心问题（Problem）：...

解决方案（Solution/Strategy）：...

核心创新 B（机制创新）：...

分创新 C1（方法/结构创新）：...

分创新 C2（性能/机制创新）：...

论证逻辑（Premises/Reasons）：...

## 4. 核心故事一句话凝练：创新组合范式

创新组合：...

一句话故事：...

## 5. 题目解读

范式分析：...

核心创新点提炼：...

趣味性/吸引力评估：...

## 6. 摘要解读：五步法分析

背景意义：...

存在的科学问题/挑战：...

本文方法/策略（核心创新点）：...

主要结果/发现（分创新点1和2及数据）：...

结论/意义：...

## 7. 结论解读：摘要精炼版

...

## 8. 图表解读：支撑核心与分创新点

图表布局逻辑：...

Fig. 1 整体解读

...

子图详细解读：

a: ...

## 9. 结果与讨论解读：总-分-总结构与 P-I-E-C 法则

...

## 10. 引言解读：漏斗式3-5步下楼梯模型分析

...

## 11. 材料与方法解读：SOP 卡片法

...

## 12. 整体评价与思考

...

## 13. 三重境界：核心带走信息（The Three-Horizon Take-Home Messages）

...

## 14. 文献内化卡片

文献标题：...

一句话故事：这篇文章通过...策略，解决了...问题，证明了...机制。

核心科学问题：作者面对的真正矛盾是...

关键机制链：结构变化：... → 电子结构变化：... → 中间体吸附变化：... → 反应路径变化：... → 性能变化：...

最关键的三张图：图 X：证明...；图 X：证明...；图 X：证明...

最强证据：...

最大漏洞：如果我是审稿人，我会质疑...

可迁移价值：这篇文章对我的课题启发是...

可借鉴表达：...
```
