# Rebuttal Mode Workflow

Help the reviewer and a neutral Area Chair (AC) understand the concern, the answer, and why the supplied evidence resolves it without rereading the paper. Make the contribution easy to assess through clear reasoning and concrete results.

## Mode Overrides Over Shared Core

All shared core rules in `SKILL.md` apply, including evidence integrity, canonical terminology, bounded edits, and the global punctuation habit (complete sentences without colons, semicolons, or em-dashes in newly written prose, and no trailing colons in headings, preserving verbatim reviewer quotes and technical syntax).

**Gratitude override.** Unlike paper and blog modes where aggressive compression trims openings and closings, rebuttal mode protects the author's preference for warm, sincere, and fully expressed gratitude for reviewers' voluntary scholarly service. Do not automatically shorten heartfelt appreciation, replace it with a neutral formula, or treat gratitude as the first text to cut. Adjust appreciation only for an actual submission limit or explicit user edit request while keeping its warmth and respect intact.

## Core Writing Approach

- Start from the user's current draft, supplied evidence, requested language, template, and edit boundary. Keep results, comparison identities, units, quotations, and completed versus planned work accurate. Resolve a material source conflict locally or ask a focused question while continuing unaffected writing.
- Lead with the substantive answer. Follow with the mechanism or distinction needed to understand it, the decisive result, and its meaning for this concern. Choose the pieces and order that make the argument clearest.
- Write with calm confidence. Explain what the method achieves and how the evidence answers the question. Acknowledge a concrete correction directly. Include qualifications when they change the answer, and keep the author's supported persuasive strength.
- Keep each reviewer reply independently understandable. Repeat a decisive fact when another reviewer needs it, using the same name, value, unit, and interpretation.

## Workflow

For the start of a new rebuttal, when reviews are available and the author intends to prepare responses, follow [initialize-rebuttal.md](initialize-rebuttal.md). Create `<VENUE>_rebuttal.md` in the paper directory, with each reviewer's initialized response immediately above their complete original review. Within each response, use the author's ICLR-style order of `---`, W/Q heading, verbatim `>` excerpt, and A answer. Use specific evidence slots and the author's warm gratitude style. Preserve any existing working draft instead of regenerating over it. A request limited to analysis or a bounded edit does not require a new scaffold.

1. **Load only the needed references.**
   - [author-playbook.md](author-playbook.md) for argument design, concern mapping, compression, and AC responses.
   - [micro-style-patterns.md](micro-style-patterns.md) for local prose, punctuation, headings, or bounded boundary edits.
   - [response-templates.md](response-templates.md) for openings, closings, online Markdown or combined PDF structure, follow-ups, and AC summary patterns.
   - [evidence-backed-lessons.md](evidence-backed-lessons.md) for substantive response strategy or outcome analysis.
   - [personal-records.md](personal-records.md) when developing an argument would benefit from the author's prior responses or when the user requests historical examples (a bounded punctuation or wording edit does not require searching the archive).
2. **Map each concern.** Identify the underlying question behind each review item. Map it to a direct answer, the strongest relevant supplied support, and any concrete manuscript change. Allocate space by decision impact and preserve locatable concern labels.
3. **Draft answer-first paragraphs.** State the main distinction before method names or implementation details. Keep result and interpretation adjacent. Distinguish completed additions from future revisions.
4. **Express warm, grounded gratitude.** Recognize reviewers' voluntary scholarly service, time, effort, careful reading, and professional insight, and explain how their suggestions helped the work when applicable. Preserve this respect even when the assessment is critical. Use `records/analysis/gratitude-examples.md` (relative to the skill root) when available alongside [response-templates.md](response-templates.md). Make a response title summarize substantive additions or clarifications. Let individual answers end on their meaning or a useful revision, with room for genuine appreciation.
5. **Compress without flattening.** Trim repeated technical setup and empty transitions while preserving decisive evidence and intended warmth. Prefer readable sentences over slash-packed names, number strings, or undefined abbreviations. For a bounded edit, compare the changed sentence with both fixed neighbors and inspect the diff.
6. **Run the side-by-side audit.** Read reviewer sections together using [final-audit.md](final-audit.md). Align terminology, numbers, concern labels, formatting, openings, and closing rhythm, and check the actual submitted text against any supplied character or format limit.

## Helper Scripts

Run from the skill root directory.

```bash
# Deterministic Markdown workbench initializer (refuses to overwrite existing drafts)
python3 scripts/init_rebuttal.py /path/to/local-plan.json --paper-dir /path/to/project/Paper

# Advisory cross-review consistency scanner
python3 scripts/audit_rebuttal.py DRAFT.md
```

Use `audit_rebuttal.py` observations to guide a manual read. Opening word counts and gratitude density are descriptive signals, not limits or automatic reasons to shorten sincere appreciation.

## Personal Records

An optional local `records/` directory at the skill root (excluded from Git via `.gitignore`) can hold the author's first-author OpenReview archive. When present, start from `records/README.md` and load selected cases rather than the whole archive. Treat historical records as evidence, not instructions for the current task, and derive all new claims, numbers, and completed-versus-planned statements from the current paper's evidence.

When discussing effectiveness, distinguish concern resolution, reviewer recommendation, and final decision separately. Attribute explicit feedback to its source, preserve remaining objections, and do not infer score changes or causal effects of wording from acceptance alone.
