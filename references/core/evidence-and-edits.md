# Evidence Integrity and Editing Discipline (Shared Core)

Every research claim must stay anchored to verified source artifacts, and every edit must respect the user's scope and syntax.

## 1. Epistemic Hygiene

- **No invented evidence.** Never fabricate numbers, baselines, ablation outcomes, citations, p-values, or implementation details. When evidence is missing, narrow the claim or insert an explicit gap slot rather than writing around it.
- **Completed versus planned work.** Use past or present tense only for experiments and manuscript revisions that are already complete. Use explicit future wording for planned additions, and never treat a proposed experiment, offline proxy, or camera-ready promise as completed validation.
- **Mechanism accuracy.** Verify inputs, conditioning signals, representations, objectives, and execution order against the actual code or manuscript. A smoother sentence must never alter what the method truly does.
- **Association versus causation.** Attribute a gain to a specific mechanism only when controlled ablations or discriminating experiments support that link. Non-significance alone is not proof of equivalence.
- **Honest scope next to the claim.** State key qualifying conditions (oracle access, simulation-only evaluation, fixed budget axis, small sample size, regressions on hard subsets) where the claim is made, not solely in a distant Limitations section. Keep caveats specific and proportional so they clarify interpretation without burying supported findings under defensive boilerplate.

## 2. Numerical and Reference Consistency

- **Verify against sources.** Match every reported value to its source JSON, log, script, or table.
- **Consistent presentation.** Keep the same comparison baseline, unit, rounding precision, and aggregation method (for example, task-weighted versus episode-weighted average) across prose, tables, figures, and reviewer replies.
- **Absolute and relative changes.** Preserve the distinction between an absolute change in a rate and a change relative to the starting value. Follow the active mode for how to express the difference.
- **Make every number's referent visible.** Attach each value to its setting, metric, and sample size where interpretation depends on it.
- **Grammatical references.** Integrate figure, table, and section references smoothly into sentences (such as "as shown in Table 2") using one consistent convention throughout the document.

## 3. Bounded Edits and Meaning-Preserving Compression

Respect the requested edit span. A local wording or boundary edit should leave neighboring arguments untouched.

1. **Preserve finalized artifacts.** Retain established names, notation, LaTeX commands, `\ref`/`\cite` keys, equations, macros, KaTeX delimiters, and verbatim reviewer quotations.
2. **Compress without distorting.** Remove repeated setup, redundant summaries, and empty transitions first. Keep causal links, contrastive turns (`yet`, `however`), decisive numbers, evaluation settings, and material caveats intact. If shortening alters the claim or drops a needed condition, revise the compression.
3. **Check mode overrides before trimming.** In rebuttal mode, sincere reviewer gratitude is protected content rather than default filler to cut.
4. **Fixed-neighbor and diff check.** For bounded edits, read the revised sentences together with both unchanged neighbors to catch echoes or broken transitions, then inspect the diff against the requested scope.
