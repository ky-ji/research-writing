# Final Cross-Reviewer Read

Compare the current reviewer replies side by side. Use this pass to make their arguments easy to follow and their presentation internally consistent.

## Concern coverage and answer flow

- Each original concern has a locatable answer, including labels retained in merged items.
- The opening gives the answer or the distinction needed to understand it.
- The decisive supplied result stays next to its interpretation.
- Each reply includes enough context for a reviewer or AC to read it independently.
- Completed additions and future revisions use accurate wording.
- Completing a requested experiment is distinguished from obtaining evidence that supports the claim. Material failures, uncertainty, and remaining objections are retained.
- Reviewer satisfaction, score or recommendation changes, and the final decision are attributed separately. No inferred consensus or unsupported score trajectory is introduced.

## Terminology and numeric presentation

- One object has one canonical name, capitalization, and abbreviation.
- Different objects remain distinguishable.
- Repeated values retain the same comparison, unit, precision, and aggregation.
- Rates and percentage-point differences retain their meaning.
- Equivalent tables and number lists use compatible notation.

When a visible contradiction affects the answer, identify the exact value or label for resolution and continue the independent edits. Match any broader scientific investigation to the task requested by the user.

## Headings, punctuation, and references

- Reviewer and answer headings follow a shared hierarchy and label convention.
- Titles summarize substantive additions or clarifications.
- New rebuttal prose follows the author's default of no colons, semicolons, or em-dashes, and headings have no trailing colon. Verbatim quotations and technical syntax retain their punctuation.
- Sentences remain readable after compression, with clearly assigned numbers and few slash-packed lists.
- Bolding, quotes, math, and table conventions align across sections.
- Initialized workbenches place `---` before each W/Q unit, then the relevant verbatim `>` excerpt and its A answer. Every distinct concern in a merged answer remains represented in the quotations.
- Quoted excerpts preserve source wording, paragraph boundaries, and list structure. The complete review below each reviewer response remains intact.
- Table and Section references are grammatical parts of sentences, with consistent reference forms.

## Openings and closings

Read parallel boundaries together.

- Gratitude follows the author's historical style and preference for sincere, fully expressed respect for reviewers' time, effort, professional judgment, and voluntary scholarly service.
- Recognition is grounded in the actual review. A critical assessment still receives warm appreciation, without being mislabeled as support or combined with other remarks into false consensus.
- Fuller acknowledgments are retained where they express genuine appreciation. There is no automatic sentence cap, neutral-tone default, or rule that repeated thanks must be deleted.
- Reviewer-level thanks recognize specific contributions where possible, and the wording accurately distinguishes completed improvements from planned revisions.
- A title, preview, and first answer each contribute useful information.
- An edited boundary fits its unchanged neighbors.
- Final sentences interpret a result, name a specific revision, or make a useful bridge.
- Repeated technical setup, generic assurances, and automatic self-weakening appendices have been trimmed. Gratitude is adjusted for an actual limit or requested edit while preserving its warmth and purpose.
- A follow-up thanking the reviewer for confirming resolution is used only after that explicit feedback, without implying acceptance or a score change.

## Submission text and bounded edits

Check the actual text that will be submitted against supplied character, quotation, and format requirements. Include all counted headings, spaces, greetings, and line breaks. For a limited edit, inspect the diff against the agreed editable span.

When asked for a consistency report, give observable variants, their reviewer or line locations, and a proposed correction. If the checked dimensions align, say so briefly.

## Optional Markdown helper

```bash
# Run from the skill root
python3 scripts/audit_rebuttal.py DRAFT.md
python3 scripts/audit_rebuttal.py DRAFT.md --json
python3 scripts/audit_rebuttal.py DRAFT.md --term-group 'baseline=Method A|Baseline A'
```

The helper extracts Markdown reviewer profiles and possible presentation mismatches. Confirm its leads in context. Read punctuation, argument flow, quotation fidelity, and submission format manually.
