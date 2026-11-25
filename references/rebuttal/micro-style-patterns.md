# Micro-Style Patterns for Rebuttal Prose

Examples below are schematic. Use the actual supplied facts and the user's current template.

## 1. Punctuation and readable sentences

As this author's default, write new rebuttal prose without colons, semicolons, or em-dashes, including trailing colons in headings. Preserve reviewer quotations verbatim and keep punctuation required by technical syntax. Use periods for separate claims and ordinary conjunctions for closely related ideas. Treat this as a writing convention, with the current user's explicit instructions taking precedence.

| Dense wording | Readable revision |
|---|---|
| The components have different roles: A predicts; B acts. | The components have different roles. A predicts the future observation, and B uses it to choose actions. |
| W1. Added control: | W1. Added control |
| Success rises: [before] to [after]; all else is fixed. | With the remaining conditions fixed, success rises from [before] to [after]. |

Prefer `and` or the established `&` convention to slash-packed prose. Make each number's referent visible.

```text
Across [number] trials per method, Method A achieves [a]% success and Method B achieves [b]%.
```

Separate rates, trial counts, and durations into readable clauses or a table when space allows. Preserve the meaning of percentages and percentage-point differences when changing presentation. Keep meaningful distinctions between task-weighted and group-weighted averages.

## 2. Give each sentence a main job

| Job | Purpose |
|---|---|
| Opening | Orient the reviewer and acknowledge their actual focus |
| Answer | State the conclusion immediately |
| Mechanism | Explain how the design addresses the question |
| Result | Give the decisive supplied fact |
| Implication | Explain why that fact matters here |
| Revision | Name the manuscript object and action |
| Bridge | Locate a distinct complementary answer |

When neighboring sentences repeat the same content, combine them or give one a different job. Keep a short explanation between a compact claim and unfamiliar technical detail.

## 3. Lead with the answer

### Direct conclusion

```text
The added control isolates the contribution of the visual input. The policy and execution schedule remain fixed while [input] changes.
```

### Mechanism

```text
The model uses [available information] to predict [relevant change]. This supplies [the information needed by the downstream component].
```

### Design rationale

```text
The design preserves the existing input interface. This lets [the intended user or component] use [the capability] with [the supplied compatibility condition].
```

### Correction

```text
We agree that the definition should be explicit. We will define [term] where it first appears in the method section.
```

Choose openings by rhetorical function. A list of every experiment performed usually delays the answer. Reviewer-level gratitude can carry the social function, leaving local openings free to carry substance.

## 4. Keep results and meaning adjacent

```text
Under the same evaluation setting, success increases from [before]% to [after]%. Changing [the controlled component] therefore accounts for [the supported interpretation].
```

Use the actual comparison and units. When two results concern different settings, name those settings before relating them. This keeps a strong conclusion precise and easy to assess.

## 5. Write useful titles and gratitude

A reviewer-level title can summarize the main completed additions and clarifications.

```text
Added Control Experiments and Expanded Comparisons
```

Follow the author's preference for sincere, generous appreciation, drawing on their previous replies. Explicitly value the time, care, professional insight, and scholarly service behind the review. Connect these qualities to concrete suggestions and their actual effect on the work. Keep heartfelt emphasis such as `sincerely grateful` or `invaluable suggestions` when it fits the author's intent. Do not impose a short neutral default. The examples below are adaptations, not historical quotations. Match the object and tense to the actual revision.

### When the reviewer suggests literature

```text
We sincerely thank you for the helpful references and for the care you have taken in considering our work in the broader literature. Your guidance has helped us clarify [SPECIFIC DISTINCTION FROM PRIOR WORK] and improve the positioning of the paper.
```

Explain how the suggested literature sharpens the positioning. Do not imply that citing it alone resolves a request for experimental comparison.

### When the reviewer suggests an experiment

```text
We are sincerely grateful for your insightful suggestion to examine [QUESTION]. The added [CONTROL] has helped us strengthen [ASPECT OF THE EVALUATION], and we appreciate the care and methodological insight behind this recommendation.
```

Name the actual comparison or analysis, then report its result and interpretation. For a planned addition, use an accurate future tense and do not claim that it has already resolved the question.

### When the reviewer identifies an error

```text
Thank you for your careful reading and for drawing our attention to this error. We sincerely appreciate your help in making the paper more accurate. We corrected [OBJECT] from [OLD VALUE OR DEFINITION] to [CORRECT VALUE OR DEFINITION].
```

Name the actual correction and move directly to its consequence. Match the tense to the completed or planned edit.

Use the established salutation and level of formality. Ground recognition in the actual comment and preserve the author's warmth. Different reviewers can receive different-length acknowledgments when their contributions differ. A substantive opening, appreciation for a local suggestion, and a grateful closing can all belong in the same reply. Avoid inserting identical praise without regard to context.

For fuller openings, different closing levels, and response layouts, use [response-templates.md](response-templates.md). For original examples, use the private `../../records/analysis/gratitude-examples.md` when available. Appreciation expresses respect for scholarly service and does not need a demonstrated effect on scores to be worthwhile.

## 6. End on the result's meaning or the revision

```text
This comparison demonstrates [the supported answer to this concern].
```

```text
We will add the comparison to Table 3 and define the setting in its caption.
```

```text
The complementary control is reported in R2-A3.
```

Choose an ending that advances the answer and preserves any meaningful appreciation. Repeated assurances such as `We hope this addresses the concern` can usually be removed. Keep a future revision promise when it names a real action that helps the reader. A warm overall thank-you can follow the technical answers.

## 7. Use the fixed-neighbor check

For an opening-only edit, read the reviewer-level opening, changed opening, and first unchanged sentence together.

```text
Echoing opening
We added an evaluation under camera shifts.

Fixed next sentence
We evaluate the model under [number] camera shifts.

Better opening
The added evaluation directly tests robustness to viewpoint changes.
```

For a closing-only edit, read the last unchanged result, changed closing, and next heading together. If the result already states the gain, let the closing explain what that gain establishes.

Inspect the diff after a bounded edit. Keep the requested body and neighboring answers fixed.

## 8. Compare parallel boundaries

Read all reviewer openings together, followed by all answer first sentences, all final sentences, and all revision commitments. Look for repeated setup, unexplained differences in respect or warmth, the same first-sentence function everywhere, or mechanical revision endings. A fuller greeting is not a defect merely because it is longer.

Vary the rhetorical job where the content calls for it. Preserve conventions for headings, labels, bolding, quotation style, tables, and math.

## 9. Keep names, numbers, and references stable

Maintain a small private terminology ledger with the canonical method, baseline, setting, metric, difference unit, averaging label, and reference style. Use project terms from the supplied material.

Repeated values retain their comparison, unit, precision, and aggregation. A rate difference in percentage points keeps that meaning even when the prose is shortened. Explain a real distinction once rather than giving different objects one name.

Integrate references into the sentence.

```text
The added comparison is shown in Table~\ref{tab:comparison}.
The evaluation setting is described in Section~\ref{sec:evaluation}.
```

Use supplied labels. Prefer these grammatical references to parenthesized Table or Section references, and keep the chosen `Section` or `Sec.` form consistent.

## 10. Read the final paragraph aloud

Check whether the conclusion is clear on the first read, the sentences connect, and each technical detail helps answer the question. Trim redundant technical setup, generic assurances, and self-weakening language while preserving heartfelt gratitude. Retain facts and qualifications that materially affect the answer.
