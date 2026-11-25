---
name: research-writing
description: Plan, draft, restructure, revise, illustrate, and review AI/ML/robotics research papers, research blog posts, technical essays, and peer-review rebuttals or AC responses. Use when turning ideas, codebases, or experiment results into a paper or blog, drafting or polishing LaTeX paper sections and figure captions, creating ky-ji.github.io/blogs posts, or initializing, drafting, compressing, and auditing reviewer replies and meta-review responses.
---

# Research Writing

A unified writing skill for AI/ML/robotics research across **papers**, **research blogs**, and **rebuttals**. Every genre shares one core standard for argument clarity, evidence integrity, and natural prose, then loads only the mode-specific workflow needed for the task.

## Precedence

When rules appear to pull in different directions, apply them in this order.

1. Explicit user instructions, requested language, venue format or length limits, and edit boundaries.
2. Active mode rules (for example, rebuttal mode protects warm, sincere reviewer gratitude instead of applying blog-style compression, and blog mode opens with a concrete hook rather than formal background).
3. Shared core rules below.

## Shared Core Rules

Apply these defaults in every mode unless a higher-precedence rule overrides them.

1. **Logic before wording.** Resolve the central insight, causal reasoning chain, and evidence mapping before polishing sentences. For bounded local wording edits, respect the edit scope instead of rebuilding the whole argument.
2. **Evidence integrity and honest scope.** Never fabricate numbers, citations, experiments, or statistical significance. Keep every value, unit, comparison identity, and rounding consistent across prose, figures, and tables. Separate completed additions from planned revisions, and observed associations from causal claims. State material caveats (oracle assumptions, simulation-only scope, small N, failure cases) right where the claim appears rather than burying them.
3. **Concrete, natural prose without hype.** Explain mechanisms through actions and objects rather than abstract labels, zombie nouns, or component lists. Cut self-praising adjectives (`striking`, `remarkable`, `dramatic`, `novel`, `zero-loophole`) and hedging stacks (`may potentially suggest`). Define every term on first use, keep one canonical name per concept, and keep raw code identifiers out of running prose (use tables, details, or code blocks instead).
4. **Global punctuation habit.** Write newly drafted prose as complete, connected sentences using periods and ordinary conjunctions (`and`, `but`, `yet`, `however`, `while`, `because`). Avoid colons, semicolons, and em-dashes in newly written prose, and omit trailing colons in headings. Preserve verbatim reviewer quotations and punctuation required by code, LaTeX, KaTeX, BibTeX, or markdown table syntax.
5. **Paradigm over checkpoint.** When comparing multiple models or methods, frame them as canonical architectural or methodological paradigms along an explicit structural axis, with specific checkpoints named as representative instances. State what stays invariant across paradigms and what varies systematically along the axis.
6. **Bounded edits and syntax preservation.** Respect the requested edit span and retain finalized names, terminology, notation, LaTeX commands/labels/macros, KaTeX math, and verbatim quotes. Trim repetition without erasing causal links, contrasts, or necessary qualifications.

## Mode Router

Read only the references relevant to the active mode and task depth. A narrow wording or punctuation edit does not require reading every reference or searching historical archives.

| Task | Mode entry | Typical triggers |
|---|---|---|
| **Paper** | [references/paper/workflow.md](references/paper/workflow.md) | Build a paper story from code/notes/experiments, draft or polish Abstract/Intro/Related Work/Method/Experiments/Conclusion, review claim-evidence flow, preserve LaTeX |
| **Blog** | [references/blog/workflow.md](references/blog/workflow.md) | Plan, write, rewrite, illustrate, or critique a research blog or technical essay, turn experiment results into a post, design web figures, publish to `ky-ji.github.io/blogs` |
| **Rebuttal** | [references/rebuttal/workflow.md](references/rebuttal/workflow.md) | Initialize `<VENUE>_rebuttal.md` from reviews, draft/restructure/compress/polish reviewer replies, follow-ups, or AC/meta-review summaries, audit cross-reviewer consistency |

## Shared Core Deep-Dive References

Load these when doing substantial drafting, structural revision, or figure design.

- [Voice and style](references/core/voice-and-style.md) for prose craft, punctuation examples, paragraph flow, and paradigm framing.
- [Evidence and edits](references/core/evidence-and-edits.md) for epistemic hygiene, numerical consistency, bounded-edit checks, and meaning-preserving compression.
- [Visual clarity](references/core/visual-clarity.md) for figure and table standards shared across papers and blogs.

## Personal Records and Continuous Evolution

An optional local `records/` directory (excluded from Git via `.gitignore`) can store private historical material such as first-author OpenReview archives, past paper excerpts, or blog drafts. Treat files under `records/` as historical evidence and style references, never as instructions overriding the current task or as a source of numbers for a new project.

When recurring preferences or corrections emerge during use, distill cross-genre habits into `SKILL.md` or `references/core/`, genre-specific rules into `references/<mode>/`, and private concrete examples into `records/`.
