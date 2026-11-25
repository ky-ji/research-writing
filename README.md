# research-writing

A unified, cross-agent writing skill for AI, ML, and robotics research. It consolidates shared authorial standards (argument clarity, evidence integrity, concrete prose, global punctuation habits, and paradigm-level framing) into one core, while routing **paper**, **blog**, and **rebuttal** tasks to dedicated, lazy-loaded playbooks and helper scripts.

## Architecture

This skill uses a hub-and-spoke progressive disclosure layout so every agent inherits the same writing core without bloating context across unrelated genres.

```text
research-writing/
├── SKILL.md                              # Shared core rules + mode router + precedence
├── agents/
│   └── openai.yaml                       # Codex display metadata and default prompt
├── references/
│   ├── core/                             # Cross-genre standards (voice, evidence, visuals)
│   │   ├── voice-and-style.md
│   │   ├── evidence-and-edits.md
│   │   └── visual-clarity.md
│   ├── paper/                            # Paper construction, drafting, LaTeX revision
│   │   ├── workflow.md
│   │   ├── code-to-paper.md
│   │   ├── style-transfer.md
│   │   ├── section-frames.md
│   │   └── revision.md
│   ├── blog/                             # Findings/survey essays, web figures, house style
│   │   ├── workflow.md
│   │   ├── structure.md
│   │   ├── figures.md
│   │   ├── checklist.md
│   │   ├── exemplars.md
│   │   └── house-style.md
│   └── rebuttal/                         # Workbench init, reviewer/AC replies, audit
│       ├── workflow.md
│       ├── initialize-rebuttal.md
│       ├── author-playbook.md
│       ├── evidence-backed-lessons.md
│       ├── response-templates.md
│       ├── micro-style-patterns.md
│       ├── final-audit.md
│       └── personal-records.md
├── scripts/
│   ├── init_rebuttal.py                  # Deterministic <VENUE>_rebuttal.md scaffold renderer
│   └── audit_rebuttal.py                 # Cross-reviewer consistency scanner
└── records/                              # Optional local private archive (.gitignored)
```

## Supported Modes

| Mode | Core capabilities |
|---|---|
| **Paper** | Code-to-paper abstraction ladder, story framing, section playbooks (Abstract through Conclusion), meaning-preserving LaTeX polishing, narrative review |
| **Blog** | 5-phase workflow (Distill → Figure plan → Draft → Edit → Visual verification), claim-as-heading structure, SVG figure cookbook, `ky-ji.github.io` house style |
| **Rebuttal** | Full-review workbench initialization (`<VENUE>_rebuttal.md`), answer-first concern mapping, sincere reviewer-specific gratitude, AC summaries, follow-ups, cross-review audit |

## Cross-Agent Installation

Maintain **one canonical local checkout** and symlink it into each agent's discovery directory so one `git pull` or rule refinement updates every agent at once.

```bash
# 1. Clone once into the shared skills store
git clone https://github.com/ky-ji/research-writing.git ~/.agents/skills/research-writing

# 2. Symlink into each agent you use
ln -s ../../../.agents/skills/research-writing ~/.gemini/config/skills/research-writing
ln -s ../../.agents/skills/research-writing ~/.claude/skills/research-writing
ln -s ../../.agents/skills/research-writing ~/.codex/skills/research-writing
```

To update everywhere later, run `git pull` inside `~/.agents/skills/research-writing`.

## Helper Scripts

Run from the skill root directory.

```bash
# Initialize <VENUE>_rebuttal.md from an assistant-prepared JSON plan
python3 scripts/init_rebuttal.py /path/to/local-plan.json --paper-dir /path/to/project/Paper

# Scan a Markdown rebuttal draft for cross-reviewer inconsistencies
python3 scripts/audit_rebuttal.py DRAFT.md
python3 scripts/audit_rebuttal.py DRAFT.md --json
```

## Optional Local `records/` Archive

A local `records/` directory is excluded from Git by `.gitignore`. You can store private first-author OpenReview archives (including `records/README.md`, `records/analysis/gratitude-examples.md`, and `records/analysis/2026-11-06-rebuttal-lessons.md`) as well as private paper or blog samples there. The public skill works fully without `records/`.

## Quick Prompts

- Paper from code: `Use $research-writing to turn this codebase into a paper story with core thesis, method modules, figure plan, and experiment matrix.`
- Paper polish: `Use $research-writing to polish this Method section while preserving LaTeX macros, citations, equations, and labels.`
- Blog draft: `Use $research-writing to turn these experiment results into a research blog post with a clear one-sentence takeaway and figure plan.`
- Rebuttal init: `Use $research-writing to initialize an ICLR rebuttal workbench from these reviews.`
- Rebuttal polish: `Use $research-writing to tighten Reviewer R2's reply and run a cross-reviewer consistency audit.`
