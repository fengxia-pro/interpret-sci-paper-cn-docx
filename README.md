# interpret-sci-paper-cn-docx

把论文 PDF、DOI 或论文链接转成中文深度解读文章，并输出带原图和“文献内化卡片”的 Word 文档的 Agent Skill。

This repository is packaged as an Agent Skill-compatible folder. The skill root is this repository root, with `SKILL.md` as the required manifest and reusable resources stored under `scripts/`, `references/`, and `agents/`.

## What It Does

- Reads a scientific paper from a local PDF, DOI, URL, or user-provided manuscript text.
- Builds an evidence-bound Chinese interpretation instead of a generic summary.
- Follows a 14-section deep-reading template, including figures, innovation logic, methods SOP, critique, and a final 文献内化卡片.
- Renders the Markdown draft into a styled `.docx` file.

## Standard Layout

```text
interpret-sci-paper-cn-docx/
├── SKILL.md
├── README.md
├── requirements.txt
├── agents/
│   └── openai.yaml
├── references/
│   └── article-interpretation-format.md
└── scripts/
    ├── download_springer_nature_figures.py
    └── render_cn_interpretation_docx.py
```

## Install

For Codex or other Agent Skills-compatible clients, copy or clone this folder into one of the client's skill search locations.

Repo-scoped example:

```powershell
New-Item -ItemType Directory -Force -Path ".agents\skills" | Out-Null
Copy-Item -Recurse -Force "D:\32 技能创建\interpret-sci-paper-cn-docx" ".agents\skills\interpret-sci-paper-cn-docx"
```

User-scoped example on Windows:

```powershell
New-Item -ItemType Directory -Force -Path "$HOME\.agents\skills" | Out-Null
Copy-Item -Recurse -Force "D:\32 技能创建\interpret-sci-paper-cn-docx" "$HOME\.agents\skills\interpret-sci-paper-cn-docx"
```

Install Python dependencies when you need to render `.docx` output locally:

```powershell
python -m pip install -r requirements.txt
```

## Use

Invoke explicitly:

```text
Use $interpret-sci-paper-cn-docx to interpret this paper PDF and output a Chinese DOCX with figures and a 文献内化卡片.
```

Or provide a local PDF path, DOI, publisher URL, or article link and ask for 文献解读 / 论文精读 / Word 输出. The skill description is written so compatible agents can trigger it implicitly for those tasks.

## Validate

Basic Codex validation:

```powershell
python C:\Users\Administrator\.codex\skills\.system\skill-creator\scripts\quick_validate.py .
```

Open Agent Skills reference validation, when available:

```powershell
skills-ref validate .
```

## License

No open-source license has been selected in this repository yet. Before broad public redistribution, the repository owner should add a real `LICENSE` file and, if desired, a matching optional `license` field in `SKILL.md`.
