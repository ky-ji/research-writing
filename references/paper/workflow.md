# Paper Mode Workflow

Turn ideas, codebases, experiments, and rough prose into a coherent, evidence-backed AI/ML/robotics research paper. Resolve the argument before polishing sentences. Explain the central insight, why it matters, how the method realizes it, and what the evidence establishes.

All shared core rules in `SKILL.md` apply, including the global punctuation default, evidence integrity, concrete anti-hype prose, and paradigm-over-checkpoint framing. Choose the narrative shape that fits the paper. Sentence counts, paragraph counts, module counts, and a primary/secondary mechanism pattern are never mandatory.

## Modes

| Mode | Use it for | Expected output |
|---|---|---|
| `build` | Starting from code, notes, or rough ideas | Paper frame with thesis, story spine, outline, figures, and experiment matrix as needed |
| `draft` | Writing a section from a validated story | Requested section, with an outline when useful |
| `polish` | Tightening existing prose | Revised text, with concise notes on substantive changes |
| `review` | Checking narrative and scientific quality | Important issues and concrete rewrite options |

## Author Preferences

Apply these defaults to manuscript prose, including drafts, revisions, and translations. Follow any explicit instructions for the current task.

- Lead each paragraph with its main point. Give the paragraph one job and connect subsequent sentences through explanation, cause, comparison, or implication. Use the opening sentence and its position for emphasis. Reserve bold or highlighting for an explicit request or a layout that requires it.
- Open a results paragraph with the main finding supported by the experiment. Follow with the comparison or number needed to interpret it, then explain how the finding answers the research question or supports the claim. Let figures and tables carry the detailed values. Keep material counterexamples and limitations visible, and attribute effects to a mechanism only when the analysis supports that explanation.
- Describe absolute differences between rates using the values being compared, such as `increases from 80% to 85%`. Avoid `percentage point(s)` and `pp` in manuscript prose. Preserve the distinction between an absolute difference and a relative change.
- Write connected sentences without English or Chinese semicolons. Recast English possessives that use `'s` or `’s` and expand contractions where applicable. Use established terminology, conventional collocations, or a natural phrase in place of coined terms and unusual compounds. Preserve verbatim quotations and punctuation that has a role in formulas, code, or LaTeX syntax.
- Integrate Table and Section references into sentences, such as `as shown in Table~\ref{tab:results}` and `as discussed in Section~\ref{sec:method}`. Avoid parenthetical callouts such as `(Table~\ref{tab:results})` and `(Section~\ref{sec:method})`.
- Use author actions such as `We introduce ...` or `We provide ...` when they explain why a method or section follows. Use `add` for an actual addition. Keep the finding in front when it is the point of the sentence. Replace broad terms such as `evidence` with the specific result, observation, comparison, or analysis when that improves precision.

## Working Approach

1. **Respect scope and syntax.** Preserve finalized names, terminology, notation, LaTeX commands, citations, labels, equations, and macros while editing.
2. **Understand before writing.** Read the available Abstract and Introduction for the research question, terminology, and strength of the claims. For `build`, `draft`, or major rewrites, use the available sources to verify the closest prior work, central insight, actual mechanism, and results. Match the depth of this check to the edit.
3. **Read only the references needed for the task.**
   - [Code to paper](code-to-paper.md) when deriving a paper frame from a repository or implementation notes.
   - [Style transfer](style-transfer.md) for overall argument design and formal paper voice.
   - [Section playbooks](section-frames.md) for Abstract, Introduction, Related Work, Method, Experiments, Figures and Captions, and Conclusion.
   - [Revision](revision.md) for checking paragraph order, tracing major claims to results, and tightening prose while preserving meaning.
   - For peer-review rebuttals, reviewer replies, or AC summaries, switch to [Rebuttal Mode](../rebuttal/workflow.md).
4. **Check and deliver.** Apply the author preferences during the final edit. Return the requested artifact and only the explanation useful for evaluating it. Provide a separate style checklist only when requested.
