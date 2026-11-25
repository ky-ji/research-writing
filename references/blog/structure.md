# Blog Structure

## Default Skeleton (Findings-Style Research Post)

| # | Section | Job | Length |
|---|---|---|---|
| 0 | Title + subtitle | Title names the lens, and subtitle asks the question the post answers. | — |
| 0 | **TL;DR** | One-sentence answer followed by 3 to 4 bullets, each pairing one claim with one supporting number. | At most 90 words |
| 0 | Hero figure | The idea as one picture (schematic or real frames). Make it interactive only when toggling adds understanding. | 1 figure |
| 1 | The puzzle or hook | One concrete observation that makes the question unavoidable, ending with the question as a pull quote. | 2 to 3 paragraphs + Fig |
| 2 | Framing | Competing hypotheses and the decisive test that separates them, with each hypothesis stating its prediction. | Short |
| 3 | Setup | Frame models by **architectural paradigm** along one structural axis (checkpoints as instances) plus a compact metric glossary. Put protocol details in `<details>`. | Short |
| 4...k | Finding 1...n | Eyebrow "Finding i", claim heading, one-sentence claim callout, evidence (at most 1 figure and 1 table), one surprise or caveat, and a cross-paradigm synthesis (what stays invariant versus what shifts with architecture). | 3 to 6 paragraphs each |
| k+1 | Implications | What changes for practitioners in 2 to 4 concrete, actionable lessons (cards). | Short |
| k+2 | Limitations | At most 3 bullets, each a bold label and one sentence. Full protocol stays in `<details>`. | Short |
| k+3 | Closing | One paragraph answering the title question in plain words with the broader stake and no new results. | 1 paragraph |
| — | Citation | BibTeX block. | — |

For tutorial or survey posts, replace Framing and Findings with Intuition, Formalism, Worked example, Variants, and When it fails.

## Opening Patterns (Pick One)

- **Surprising number.** "Change nothing but the random seed, and success rises from 50% to 81%."
- **Concrete scene.** Describe one specific rollout or example and show exactly what goes wrong.
- **Widely held belief, then crack.** "Everyone assumes X. Here is a case where X predicts the opposite of what happens."

Never open with background history, "In recent years...", a formal definition, or a list of contributions.

## Section Anatomy

```text
[eyebrow: "4 · Finding 1"]
## <Claim as heading>
<one-sentence claim callout>
<intuition or expectation> -> <what actually happens, one number>
<mechanism or explanation in plain words>
[Figure: title + takeaway / image / caption]
<the twist, caveat, or confound check>
<bridge: the question the next section answers>
```

## TL;DR Template

```text
TL;DR
<One-sentence answer to the title question.>
• <Claim 1.> <One supporting number.>
• <Claim 2.> <One supporting number.>
• <Claim 3.> <One supporting number.>
• <Practical consequence.>
```

## Closing Patterns

- Restate the one sentence in new, plainer words.
- Name the cost or risk the finding reveals.
- Point to what should be built or tested next.

Avoid recap lists that duplicate the TL;DR, generic sign-offs such as "we hope this inspires", and new numbers introduced at the end.
