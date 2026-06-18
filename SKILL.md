---
name: interpret-sci-paper-cn-docx
description: Interpret scientific papers in Chinese and export a polished DOCX using a 14-section deep-reading framework with evidence extraction, figure interpretation, writing-structure analysis, methods SOP, critique, and a final 文献内化卡片. Use when the user provides a paper PDF, local PDF path, DOI, URL, article link, or manuscript and asks for 文献解读, 论文精读, 原文解读, 公众号风格解读, 文献内化卡片, figures, or Word/DOCX output.
---

# Interpret Scientific Paper CN DOCX

## Purpose

Use this skill to turn a scientific paper PDF, DOI, or article link into a Chinese deep-reading article and a styled `.docx` file. The deliverable should be evidence-bound, readable for Chinese researchers, and structured around the 14-section template in `references/article-interpretation-format.md`.

Read `references/article-interpretation-format.md` before drafting a full interpretation. Keep `SKILL.md` as the workflow layer and use the reference file for the exact section schema, style rules, and Markdown skeleton.

When the user does not specify a destination, place final Word files, source Markdown drafts, and figure assets under a clearly named output directory in the current workspace, for example `outputs/<paper-short-title>/`.

Default behavior: if the user provides a PDF, local path, DOI, or article URL and asks to read/process/解读 it, run the full interpretation workflow and produce the Word document. Ask a short clarification only when multiple candidate papers or output scopes are ambiguous.

## Source Access Rules

- Prefer the user-supplied PDF or manuscript text as the source of truth.
- For DOI or URL input, use publisher pages, journal pages, DOI pages, arXiv, bioRxiv, chemRxiv, PubMed Central, or other legal full-text sources.
- If only metadata or an abstract is accessible, do not imply that the full paper was read. Either ask the user for the PDF or clearly label the work as an "摘要级解读".
- Do not invent results, methods, figures, quantitative values, limitations, publication dates, or author details.
- Avoid long verbatim copying from the source paper. Paraphrase and cite figures/sections as evidence.

## Workflow

1. Acquire and parse the source.
   - Extract metadata, abstract, conclusion, introduction structure, result headings, methods details, figure captions, key quantitative results, references to figures, and limitations.
   - Keep a working evidence notebook that maps each major claim to the supporting section, figure, table, or data point.

2. Collect figures.
   - Prefer publisher-provided figure PNGs or high-resolution files. If unavailable, render or crop figures from the PDF.
   - For Springer Nature articles with predictable media URLs, try `scripts/download_springer_nature_figures.py <doi> <output-dir> --count <n>`.
   - If a figure cannot be obtained, state which figure is missing and why.
   - If the user provides a hand-drawn overview, concept map, "灵魂五问" image, or other custom interpretation image, preserve the exact file and embed it in section 2 immediately after `灵魂五问：` unless the user asks for another position.

3. Analyze through the template lenses.
   - Identify the core problem, prior gap, central mechanism or strategy, two to three sub-innovations, evidence chain, and application implication.
   - Read figures in sequence as a narrative: question answered, subpanel meaning, key data, and how the figure supports the claim.
   - Decode writing craft: title strategy, abstract five-step logic, conclusion compression, introduction funnel, results P-I-E-C paragraphs, and methods SOP.
   - Prepare the final internalization card with title, one-sentence story, core scientific contradiction, mechanism chain, three most important figures, strongest evidence, reviewer-style weakness, transferable value, and reusable expressions.

4. Draft the Markdown.
   - Use clear academic Chinese with a readable public-account rhythm.
   - Preserve chemical formulas, symbols, gene/protein names, materials names, and mathematical notation accurately.
   - Insert figures with Markdown image syntax near the corresponding figure interpretation section, for example `![Fig. 1. Short caption](figures/fig1.png)`.
   - Append `## 14. 文献内化卡片` as the final section. Keep it compact enough to feel like one page. For broad or non-mechanistic papers, adapt the mechanism-chain fields and write "本文未直接展开" instead of inventing links.

5. Render and verify.
   - Run `python scripts/render_cn_interpretation_docx.py <input.md> <output.docx>`.
   - Reopen or inspect the `.docx` before final delivery. At minimum, verify that the file exists, text is extractable, section 14 is present, and no `[Image missing: ...]` markers remain unless they are intentionally reported.
   - For high-stakes delivery, visually inspect the rendered document or use a document/PDF inspection tool when available.

## Quality Bar

- Complete interpretation, not a generic abstract summary.
- Claims tied to actual evidence from the paper.
- Figure interpretation includes whole-figure logic and subpanel-level meaning when the paper provides enough information.
- Main figures embedded unless unavailable, inaccessible, or explicitly excluded.
- Methods written as an SOP card: objective, principle, inputs/equipment, steps, controls, validation, and unique trick.
- Limitations specific to the actual study, not boilerplate.
- The final 文献内化卡片 is short, memorable, evidence-bound, and useful for research transfer.
- Missing source information is stated briefly rather than fabricated.

## Bundled Resources

- `references/article-interpretation-format.md`: the learned 14-section structure, style rules, and Markdown skeleton.
- `scripts/render_cn_interpretation_docx.py`: converts the drafted Markdown, including `![caption](image)` figure references, into a styled Word document.
- `scripts/download_springer_nature_figures.py`: downloads Springer Nature HTML figure PNGs from a DOI when the article uses predictable `MediaObjects/*_FigX_HTML.png` URLs.
