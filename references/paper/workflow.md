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

## Working Approach

1. **Respect scope and syntax.** Preserve finalized names, terminology, notation, LaTeX commands, citations, labels, equations, and macros while editing.
2. **Understand before substantial writing.** For `build`, `draft`, or major rewrites, verify the research question, closest prior work, central insight, actual mechanism in code or notes, and available evidence before drafting. A local wording edit does not need to repeat this process.
3. **Read only the references needed for the task.**
   - [Code to paper](code-to-paper.md) when deriving a paper frame from a repository or implementation notes.
   - [Style transfer](style-transfer.md) for overall argument design and formal paper voice.
   - [Section playbooks](section-frames.md) for Abstract, Introduction, Related Work, Method, Experiments, Figures and Captions, and Conclusion.
   - [Revision](revision.md) for repairing existing prose, checking evidence accuracy, and meaning-preserving tightening.
   - For peer-review rebuttals, reviewer replies, or AC summaries, switch to [Rebuttal Mode](../rebuttal/workflow.md).
4. **Return clean deliverables.** Return the requested artifact and only the explanation useful for evaluating it.
