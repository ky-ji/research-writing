# Voice and Style (Shared Core)

These standards govern prose craft across papers, research blogs, and rebuttals unless the active mode explicitly overrides a detail.

## 1. Argument Before Wording

Resolve what the reader must understand and why it matters before polishing sentences. Connect the question, the relevant baseline or limitation, the central insight, the mechanism, and the decisive evidence. Never disguise a logical gap with smoother phrasing.

Give every paragraph one clear job. Connect adjacent sentences through cause, contrast, consequence, example, or refinement. When neighboring sentences repeat the same idea, merge them or assign one a distinct job.

## 2. Classic Style and Concrete Prose

Write as if pointing at something concrete that both you and the reader can inspect.

- **Concrete subjects and active verbs.** Prefer "the action head contracts toward the mean" over "contraction is observed in the action head."
- **Actions and mechanisms over component lists.** Explain what a mechanism reads, changes, and produces instead of enumerating layers, heads, hidden states, or file names.
- **No self-praising hype.** Cut adjectives that judge your own work, such as `striking`, `remarkable`, `dramatic`, `impressive`, `zero-loophole`, `best-paper`, or unsupported `novel` and `first`. Let numbers and contrasts carry the weight.
- **No hedging stacks or throat-clearing.** Replace "It is worth noting that these findings may potentially suggest" with the actual claim and its honest scope.
- **Plain names in running prose.** Keep raw code identifiers (`other_scene_vlm`, `zero_vlm_mask`, class names, config flags) out of running prose. Use readable plain names and reserve identifiers for tables, collapsible details, appendices, or code snippets.

## 3. Global Punctuation Habit

As this author's default across papers, blogs, and rebuttals, write newly drafted prose without colons, semicolons, or em-dashes, and omit trailing colons in headings.

- Split independent claims into separate sentences with periods.
- Connect closely related clauses with ordinary conjunctions (`and`, `but`, `yet`, `however`, `while`, `because`, `so`) rather than punctuation shortcuts.
- Avoid slash-packed lists (`A/B/C`) when `and`, `or`, or a short table reads more cleanly.
- **Exceptions.** Preserve verbatim reviewer quotations, explicit user formatting instructions, and syntax required by LaTeX, KaTeX, BibTeX, URLs, file paths, Markdown tables, or code.

| Dense punctuation | Preferred revision |
|---|---|
| The modules have distinct roles: A predicts; B acts. | The modules have distinct roles. A predicts the future state, and B selects the action. |
| Removing the VLM widens the prior — not narrows it. | Removing the VLM widens the prior rather than narrowing it. |
| **W1. Added control:** | **W1. Added control** |
| Success rises: 50% to 81%; all else stays fixed. | With all other settings fixed, success rises from 50% to 81%. |

## 4. Paradigm Over Checkpoint

When comparing multiple models, policies, or methods, frame them as canonical architectural or methodological paradigms arranged along an explicit structural axis (for example, decoupled cross-attention versus layer-wise KV-cache coupling). Name specific checkpoints or implementations as representative instances of each paradigm.

State both what remains **invariant** across paradigms and what **varies systematically** along the structural axis. Group prior work into paradigms only when the grouping explains a real mechanistic or empirical difference.

## 5. Canonical Terminology and Read-Aloud Check

Maintain a small private terminology ledger for each project with one canonical name, capitalization, symbol, and abbreviation for every method, baseline, setting, metric, and reference form (`Figure` vs `Fig.`, `Section` vs `Sec.`). Define every new term on first use in plain words, and never give two different objects the same name.

Before delivering substantial prose, read each paragraph aloud mentally. Rewrite any sentence that stumbles, buries its verb, or forces the reader to backtrack.
