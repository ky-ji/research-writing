# Openings, closings, and response formats

These patterns follow the author's historical replies and preference for sincere, fully expressed gratitude. Reviewers contribute their time, care, and professional judgment to the scholarly community, and the author wants that service to be acknowledged warmly. Use the `../../records/analysis/gratitude-examples.md` for verbatim examples when the local archive is available. The patterns here are adaptations for a new paper, not historical quotations.

Choose the wording and length that express the actual appreciation. Do not impose a short neutral default or automatically remove heartfelt emphasis. Replace every bracketed placeholder with verified current-paper content before submission, including actual improvements and feedback. Gratitude does not depend on whether it raises a score.

Keep the author's existing W/Q labels, language, and editable boundaries. The examples use English submission prose and Markdown. Use the actual venue's format and limits rather than copying a historical page or character limit.

For a new working file that includes all reviewer comments, use [initialize-rebuttal.md](initialize-rebuttal.md). Its default layout places each initialized reviewer response immediately above that reviewer's complete original text. The patterns below supply the response language within that workbench or an existing draft.

## 1. Reviewer-level openings

### Default appreciation for time, care, and scholarly service

```text
We sincerely thank Reviewer [ID] for the time and effort devoted to reviewing our work and for the thoughtful feedback. We greatly appreciate your careful reading and dedicated service to the community. Your comments have helped us strengthen [SPECIFIC ASPECT], and we address each point below.
```

Preserve the same respect for a critical review. Thank the reviewer for their effort and contribution without labeling their assessment as supportive unless it was. Match the improvement sentence to what has actually changed, or thank the reviewer for identifying what needs improvement.

### A specific suggestion led to a completed improvement

```text
We are grateful to Reviewer [ID] for a thoughtful and incisive review that helped us strengthen [ASPECT OF THE WORK]. In particular, your suggestions to examine [CONCERN] and provide [ANALYSIS] guided the additional work below. These suggestions have been invaluable in improving [SPECIFIC ASPECT]. We sincerely appreciate the care and insight behind your comments and respond to each point below.
```

This fuller opening draws on the author's past reviewer-specific acknowledgments. Keep the connection between the reviewer's insight, actual suggestions, and the resulting improvement. A substantive paragraph is appropriate when it reflects the work the reviewer contributed.

### Positive assessment plus remaining questions

```text
Thank you for your supportive and thoughtful feedback. We sincerely appreciate your recognition of [STRENGTH ACTUALLY NAMED IN THE REVIEW]. We are also grateful for your constructive suggestions on [CONCERN], which helped us improve [SPECIFIC ASPECT]. Below, we present [COMPLETED ADDITION] and address the remaining questions.
```

Quote praise only when exact and useful. Avoid collecting favorable adjectives from several reviewers into a claim of consensus.

### Shared opening for a combined response

```text
We sincerely thank all the reviewers for their valuable time, careful reading, and insightful suggestions. We deeply appreciate the effort and dedicated service you have contributed to the community and the opportunity to improve our work through this discussion. We first address the shared concern about [COMMON ISSUE], followed by the reviewer-specific questions.
```

Use the preview when it describes the actual organization. Set the length by the author's intended appreciation and the applicable format, rather than an arbitrary sentence limit.

## 2. Local acknowledgments

Use these to recognize a particular contribution within the response. A reviewer-level thank-you does not preclude sincere appreciation for a specific suggestion. Connect the acknowledgment naturally to the substantive answer.

| Situation | Adaptable wording |
|---|---|
| Suggested literature | We sincerely thank you for the helpful references and your thoughtful guidance on the literature. They helped us clarify [SPECIFIC DISTINCTION]. |
| Suggested experiment, completed | Thank you for this insightful suggestion. We appreciate your help in strengthening the evaluation and have completed [CONTROL] to test [QUESTION]. |
| Identified error, corrected | Thank you for your careful reading and for drawing our attention to this error. We sincerely appreciate your help in making the paper more accurate and have corrected [OBJECT]. |
| Ambiguous explanation | We agree that the original description was unclear. [DIRECT EXPLANATION]. |
| Legitimate limitation | We agree that [LIMITATION] restricts [SCOPE]. The current evidence supports [BOUNDED CLAIM]. |

Use a future tense for a planned manuscript edit. Do not turn a suggested experiment into a completed one through a template.

## 3. Endings at three different levels

### End of an individual answer

Choose the sentence that advances this argument. Meaningful appreciation for the suggestion can accompany the technical conclusion, especially when it led to a useful correction or analysis.

```text
This comparison supports [SPECIFIC CONCLUSION] under [TESTED CONDITIONS].
```

```text
We will add [RESULT OR DEFINITION] to [MANUSCRIPT LOCATION] and make [QUALIFICATION] explicit.
```

```text
The remaining uncertainty is [UNRESOLVED ISSUE], so we limit the claim to [SUPPORTED SCOPE].
```

Promise a manuscript update only when it is intended and permitted in the applicable revision stage. If already incorporated, use `We added` and a verified location.

### End of a complete reviewer response

```text
We are deeply grateful for your constructive feedback, which has helped us improve [SPECIFIC ASPECT]. Thank you again for the time, care, and effort you dedicated to reviewing our work.
```

Another fuller closing acknowledges the opportunity to improve the work and the reviewer's continuing attention, without implying that every concern has been resolved.

```text
We appreciate the opportunity to address these concerns. We are sincerely grateful for your careful review and thoughtful guidance, which have helped us strengthen the manuscript. We would be glad to provide any further clarification should additional questions arise. Thank you again for your time and consideration.
```

Choose the closing that fits the exchange. A full closing paragraph is welcome when it expresses the author's appreciation. Under a strict limit, adjust the wording while retaining meaningful thanks rather than deleting it by default. Place local and overall acknowledgments naturally instead of mechanically repeating an identical paragraph.

### After the reviewer explicitly confirms resolution

```text
Thank you very much for the thoughtful follow-up. We really appreciate the time and care you put into reading our rebuttal, and we are glad that our clarifications were helpful. Your comments pushed us to strengthen the paper, and we are sincerely grateful for that. We will incorporate [AGREED CLARIFICATION] into [PERMITTED REVISION].
```

If already incorporated, report that fact instead. Do not translate confirmation of resolution into support for acceptance or an actual score increase.

## 4. Online Markdown response

Use the venue's title field for a concise substantive title, such as `Matched Comparisons and Statistical Support`. The reviewer ID can be included if needed to identify the thread.

```markdown
We sincerely thank Reviewer [ID] for the time and effort devoted to reviewing our work. We greatly appreciate your thoughtful suggestions on [CONCERN] and the care behind them, which helped us improve [SPECIFIC ASPECT]. We address each point below.

---

**W1 & Q2. [Concise topic]**

> [RELEVANT VERBATIM EXCERPT FOR W1]

> [RELEVANT VERBATIM EXCERPT FOR Q2]

**A1. [DIRECT ANSWER IN ONE SENTENCE].** [Necessary mechanism or distinction].

Under [SHARED SETUP], we evaluate [METHODS] using [METRIC AND UNIT]. As shown in Table R1, [DECISIVE RESULT].

**Table R1. [What the comparison measures]**

| Method | [Metric and unit] | [Relevant cost and unit] |
| --- | --- | --- |
| [BASELINE] | [VERIFIED RESULT] | [VERIFIED COST] |
| [OUR METHOD] | [VERIFIED RESULT] | [VERIFIED COST] |

[What this establishes for the concern, including a material qualification]. [Concrete manuscript change if useful].

---

**W2. [Next topic]**

> [RELEVANT VERBATIM EXCERPT]

**A2. [DIRECT ANSWER].** [Evidence and interpretation].

We are sincerely grateful for your constructive feedback and the opportunity to improve our work. Thank you again for your time and careful consideration.
```

Tables are optional. Put short results in prose when a table adds overhead. New working drafts use a standalone `---` before each W/Q unit and quote the relevant original text with `>` before the answer, following the author's ICLR examples. Later compression for a supplied submission limit can shorten the selected quotation while preserving its meaning and the full review in the workbench. Define uncertainty, sample counts, and aggregation where they matter. A short wording correction does not need all five argument elements.

Retain every merged concern label and quote each distinct relevant source excerpt in label order. Quote without silently rewriting or stitching separated passages into one apparent quotation. Preserve paragraph breaks and nested lists with `>` on every quoted line. If paraphrasing, remove quotation marks and blockquote formatting. Use consistent heading depth, answer numbering, and bolding. Bold the main answer or decisive quantity selectively.

For multiple posts, name each part by content, retain stable answer IDs, and include a brief location pointer to other parts. A full reviewer-level opening can appear in the first part and an overall closing in the last, with appreciation for specific suggestions wherever it fits naturally. Each answer still needs its own decisive result, even when a full table is linked elsewhere.

## 5. Combined PDF response

Adapt to the required venue template. This outline does not prescribe a page count.

```text
[SHARED OPENING THANKING THE REVIEWERS FOR THEIR TIME, EFFORT, AND CONTRIBUTIONS]

Common R1-Q1 & R2-Q3. [Shared topic]
[Direct answer, shared evidence, interpretation, and useful revision].

Reviewer R1
Q2. [Topic]
[Answer and reviewer-specific evidence].
Q3. [Topic]
[Answer and reviewer-specific evidence].

Reviewer R2
Q1. [Topic]
[Answer and reviewer-specific evidence].

Reviewer R3
Q1. [Topic]
[Answer and reviewer-specific evidence].
```

Merge only genuinely shared concerns. Keep each original label visible. Prioritize a few readable tables that directly answer high-impact concerns. Respect the required typography and format, preserving decisive evidence, material qualifications, and meaningful appreciation within the available space. Integrate references naturally, for example `as shown in Table~\ref{tab:comparison}` and `as discussed in Section~\ref{sec:analysis}`.

## 6. Argument patterns for recurring concerns

### Fair comparison

```text
We compare [METHODS] at matched [ACTUAL BUDGET], keeping [CONTROLLED CONDITIONS] fixed. The reported cost includes [COST COMPONENTS]. As shown in Table [LABEL], [RESULT]. This supports [CONCLUSION ABOUT THIS COMPARISON].
```

If matching effective computation, do not call the comparison latency-matched without latency evidence. State an unmatched factor when it materially affects interpretation. A deployment result can complement a controlled comparison.

### Novelty or distinction from prior work

```text
Both [PRIOR WORK] and our method use [SHARED IDEA]. Our contribution is [PRECISE DIFFERENCE], which addresses [SPECIFIC LIMITATION OR USE CASE]. Under [CONTROLLED SETUP], [COMPARISON OR ABLATION] shows [SUPPORTED CONSEQUENCE]. We will revise [CLAIM OR LOCATION] to make this scope explicit.
```

If the requested comparison is missing, state that gap. Terminological distinctions and added citations do not substitute for experimental evidence when that is the unresolved issue. Use priority claims such as `first` only when adequately supported.

### New results reveal weaker or variable gains

```text
The additional runs support [LIMITED FINDING], while the advantage varies across [CONDITIONS]. We report [UNCERTAINTY SUMMARY] over [INDEPENDENT UNIT AND SAMPLE COUNT], including [FAILURE OR REGRESSION]. We therefore revise the claim from [ORIGINAL CLAIM] to [SUPPORTED CLAIM].
```

If a superiority test is inconclusive, say so. Failure to detect a difference does not by itself demonstrate equivalence, losslessness, or a particular causal explanation. Choose the inference that the actual analysis supports.

### The requested experiment is not yet available

```text
We have not completed [REQUESTED EVALUATION]. The available [EVIDENCE] supports [NARROWER CLAIM], but does not establish [MISSING CLAIM]. We will revise [AFFECTED STATEMENT] accordingly.
```

Add a concrete experiment commitment only when realistic. Do not present a plan, an offline proxy, or an unrelated benchmark as completed validation of the requested setting.

## 7. Follow-up when a concern remains

```text
Thank you for taking the time to read our response and clarify the remaining concern. We sincerely appreciate your continued attention and the opportunity to examine this point more carefully. We understand that the question is whether [PRECISE RESIDUAL QUESTION]. [DIRECT ANSWER]. Compared with our earlier response, [NEW EVIDENCE OR CLARIFICATION] establishes [SUPPORTED POINT], while [REMAINING LIMITATION] remains unresolved.
```

Keep only applicable sentences. Do not repeat the entire first rebuttal. If the reason for a negative assessment is unavailable, a focused request can be appropriate.

```text
We sincerely appreciate your time and continued consideration of our work. Could you clarify which concern remains decisive after the additional [EVIDENCE]? We would be grateful for your guidance and would be glad to address that point directly.
```

This invites technical clarification without asserting that the reviewer ought to change a score.

## 8. AC summary or meta-review response

```markdown
Dear Area Chair,

We are sincerely grateful for the substantial time and effort you have devoted to this submission, especially your careful review and thoughtful synthesis of the reviewers' concerns. We also sincerely thank the reviewers for their insightful feedback and dedicated service to the community. Below, we address [DECISION-RELEVANT ISSUE] and summarize the evidence and remaining limitations.

**1. [Decisive concern]**

[What was added or clarified]. [Headline result and interpretation]. The details are in [REPLY LOCATION]. [Reviewer feedback, only if explicitly recorded].

**2. [Second decisive concern]**

[Evidence, supported conclusion, and location].

**3. [Remaining limitation and claim scope]**

[What the current results do not establish]. We [COMPLETED OR INTENDED REVISION] to limit the claim to [SUPPORTED SCOPE].

We appreciate the opportunity to address these concerns and are sincerely grateful for the guidance that has helped us improve the manuscript. Thank you again for your time, careful consideration, and efforts throughout the review process.
```

Use as many items as the decision requires. A private resolved/partial/unresolved ledger can guide the summary, but the public text should explain the scientific state of each concern. Preserve disagreement when it exists. Do not manufacture unanimity, equate silence with satisfaction, or report a score change based only on an intention or a conflicting snapshot.
