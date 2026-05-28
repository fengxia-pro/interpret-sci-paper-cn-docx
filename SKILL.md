---
name: interpret-sci-paper-cn-docx
description: 慢老师解读文献技能20260527V1. Interpret scientific research papers in Chinese using a fixed public-account-style deep-reading framework and export a polished Word document with original figures and a final one-page 文献内化卡片. Use automatically when the user drops/uploads/provides a paper PDF, local PDF path, DOI, URL, article link, or manuscript, even if they only say to process/read/解读 it; also use when the user asks for 原文解读, 文献解读, 论文精读, 公众号风格解读, 文献内化卡片, 慢老师解读文献, or a Word/DOCX output matching the learned template.
---

# 慢老师解读文献技能20260527V1

## Overview

Use this skill to turn a scientific paper PDF or paper link into a structured Chinese deep-reading article and deliver it as a `.docx` file. The output should follow the learned template: rigorous evidence extraction, approachable narration, innovation-logic analysis, figure-by-figure interpretation, writing-structure analysis, methods SOP, critique, three-level take-home messages, and a one-page "文献内化卡片" at the end.

Before writing, read `references/article-interpretation-format.md` for the exact section schema and style rules.

When the user does not specify another destination, place final Word files, source Markdown drafts, and extracted/downloaded figure assets under a clearly named output directory in the current workspace.

Default behavior: if the user provides only a PDF file, local file path, DOI, or paper URL, treat that as a request to run the full interpretation workflow and produce the final Word document. Do not stop at a summary or ask for confirmation unless the source cannot be accessed or the request is ambiguous between multiple papers.

## Workflow

1. Acquire the source paper.
   - If the user provides a local PDF, extract text, metadata, headings, references to figures, and captions from that PDF.
   - If the user provides a DOI or URL, browse or download the article/PDF from reliable sources. Prefer publisher pages, journal pages, DOI pages, arXiv/bioRxiv/chemRxiv, PubMed Central, or the user-supplied file.
   - If the link is inaccessible or paywalled and no PDF is available, ask the user for the paper PDF instead of guessing.

2. Build an evidence notebook before drafting.
   - Capture title, authors, affiliations, journal, received/accepted/published dates, DOI.
   - Extract abstract, conclusion, introduction structure, results section headings, methods details, figure captions, key quantitative results, and limitations.
   - Track which claims are supported by which paper sections or figures. Do not invent data.
   - Acquire the original main figures for the paper. Prefer publisher-provided figure PNGs or high-resolution figure files; otherwise render/crop figures from the PDF. Do not rely only on text captions when the user expects a Word deep-read document.
   - If the user provides a hand-drawn overview, concept-map, "灵魂五问" summary image, or other custom interpretation image, save it as an asset and embed it in section 2 immediately after `灵魂五问：` and before the five Q/A items, unless the user specifies another position.

3. Analyze the paper through the template lenses.
   - Identify the core problem, prior gap, central mechanism/strategy, two to three sub-innovations, evidence chain, and application implication.
   - Read figures in sequence as a narrative: what question each figure answers, what subpanels show, what data matter, and how it supports the core claim.
   - Decode writing craft: title strategy, abstract five-step logic, conclusion compression, introduction funnel, results P-I-E-C paragraphs, methods SOP.
   - Prepare a final internalization card: title, one-sentence story, core scientific contradiction, mechanism chain, three most important figures, strongest evidence, biggest reviewer-style weakness, transferable value, and reusable expressions/logical structures.

4. Draft in Chinese.
   - Use clear academic Chinese with a public-account readable rhythm.
   - Explain technical mechanisms with precise but accessible metaphors when helpful.
   - Preserve chemical formulas and symbols accurately, for example `H2O2`, `OH-`, `HO2-`, `2e- ORR`, `GDE`, `RRDE`.
   - Avoid long verbatim copying from the paper. Summarize and paraphrase, with only short quotes if necessary.
   - Append `## 14. 文献内化卡片` as the final section. Keep it concise enough to feel like one page, using the exact label set from the reference template. For broad or non-mechanistic papers, adapt the mechanism-chain fields and state "本文未直接展开" rather than inventing missing links.

5. Render to Word.
   - Write the completed article as Markdown using the heading skeleton in `references/article-interpretation-format.md`.
   - Insert each main figure in Markdown with `![Fig. X. Short caption](path/to/figure.png)` near its corresponding `Fig. X 整体解读` section.
   - Use `scripts/render_cn_interpretation_docx.py input.md output.docx` to create the Word file. The renderer gives `## 14. 文献内化卡片` a hand-drawn-card inspired Word style with bold black title, red accent, yellow marker shading, and compact boxed text.
   - Verify by reopening or extracting text from the `.docx`; for high-stakes delivery, visually inspect the rendered document or use the Documents skill if available.

## Quality Bar

- The document must feel like a complete interpretation, not a generic summary.
- Every section should connect back to the paper's core scientific problem and innovation claim.
- Figure interpretation must include both whole-figure logic and subpanel-level meaning when the paper provides enough information.
- Main figures must be embedded in the Word output unless unavailable, inaccessible, or explicitly excluded by the user. If a figure cannot be obtained, state which figure is missing and why.
- User-provided overview images for "灵魂五问" are part of the deliverable, not optional decoration. Preserve the exact image file when available; do not recreate or paraphrase it unless the user explicitly asks for regeneration.
- Methods interpretation should be written as an SOP card: objective, principle, inputs/equipment, steps, controls, validation, and unique trick.
- Limitations should be specific to the actual study, not boilerplate.
- The final "文献内化卡片" should be a distilled learning artifact, not a second summary. It must be short, memorable, evidence-bound, and useful for the user's own research transfer.
- If source information is missing, state it briefly in the relevant section rather than fabricating it.

## Bundled Resources

- `references/article-interpretation-format.md`: the learned 14-section structure, style rules, and Markdown skeleton.
- `scripts/render_cn_interpretation_docx.py`: converts the drafted Markdown, including `![caption](image)` figure references, into a styled Word document.
- `scripts/download_springer_nature_figures.py`: downloads Springer Nature HTML figure PNGs from a DOI when the article uses predictable `MediaObjects/*_FigX_HTML.png` URLs.
