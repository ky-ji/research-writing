# Lessons from response, follow-up, and decision evidence

Use these lessons when planning a substantive rebuttal or analyzing its impact. They come from paired readings of the author's archived responses, reviewer follow-ups, and decisions. They are qualitative observations from related papers across different venues, not a causal estimate of the effect of wording or rebuttal effort.

The optional private `../../records/analysis/2026-11-06-rebuttal-lessons.md` contains the paper-specific evidence and provenance. The writing workflow remains usable without that archive.

## 1. Separate three outcomes

Track concern resolution, reviewer recommendation, and paper decision separately. A reviewer can confirm that questions were answered while retaining a weak recommendation. A score can increase while the paper is rejected. Acceptance can reflect the contribution's overall value or an explicit program decision despite unresolved concerns.

When analyzing a case, record the original concern, the author's action, the reviewer's actual reaction, the remaining objection, and the final decision. If the reviewer confirms the response as a whole, do not attribute that confirmation to each sentence or experiment individually. A decision that explicitly discusses particular additions provides stronger evidence for that narrower attribution.

An intention to increase, a self-reported increase, a currently displayed score, and an AC's retrospective account are different evidence. Attribute them accurately. Missing discussion and AI-generated review text cannot establish human persuasion.

## 2. Match the evidence to the decision criterion

Identify what makes the requested evidence relevant before drafting a reply.

| Reviewer doubt | Useful response evidence | Common incomplete answer |
|---|---|---|
| Fairness relative to an acceleration baseline | Comparison on the requested budget axis, explicit included costs and controlled conditions | More baseline names without matching the budget |
| Practical deployment | Requested hardware, closed-loop outcome, and appropriately measured end-to-end cost | Simulation speedup, offline proxy, or promised deployment alone |
| Stability of the claimed improvement | Appropriate independent runs or trials, condition-level results, uncertainty and failures | A pooled mean that conceals the challenged condition |
| Novelty relative to close prior work | Precise shared idea and difference, then evidence of its consequence | New terminology, repeated priority claims, or citations alone |
| Mechanism or alternative explanation | A discriminating control and the limits of its interpretation | Visualization or an intuitive explanation presented as proof |
| Reported numbers do not reproduce | Exact setting, checkpoint, metric, version and verifiable source of the mismatch | Asserting that the numbers are correct |
| Unclear overhead or implementation | Absolute cost, scaling dimensions, and the operational explanation | Calling the overhead negligible without its referent |

Use only the evidence the current paper actually has. These are possible responses to the corresponding doubts, not a mandatory experiment checklist for every rebuttal.

## 3. Completing the experiment does not settle the claim

Read the new result before writing the victory sentence. Requested analyses may expose variance, regression, confounding, or a narrower operating range. State what the new evidence establishes, where it does not, and how the claim changes.

Do not substitute a favorable new protocol for an unfavorable original one. Explain the different questions, retain the original result, and justify the scope of each. An average improvement cannot establish improvement in every condition. An empirical explanation cannot become a rigorous bound through wording.

When an apparent gain is statistically unsupported, a precise reduction in claim strength can answer the concern more convincingly than another speculative explanation. Non-significance alone is not proof of equivalence. Use the analysis and independent sampling unit appropriate to the actual question.

## 4. Treat novelty as a substantive comparison

Start with what is shared with the nearest prior work. Explain the exact change and why it matters under a controlled comparison or a relevant demonstrated capability. If the reviewer asks for head-to-head results, acknowledge whether those results exist.

Additional citations, cleaner definitions, and a stronger contribution paragraph can resolve presentation gaps. They need not resolve a judgment that the technical contribution is incremental. Avoid responding to that judgment solely by repeating `novel`, `first`, or other reviewers' praise.

## 5. Use the follow-up to locate the residual issue

When the reviewer says most concerns are addressed, identify the exception. When they refine the question, answer that refined question with the right measurement rather than repeating a nearby analysis. When they maintain or lower a score without a reason, record the uncertainty rather than inventing a cause.

A successful rebuttal is not always one in which every reviewer changes their assessment. Concentrate the remaining space on the concern that still governs the recommendation, and preserve honest limits.

## 6. Make new evidence available to the actual decision process

When the venue permits revision, integrate decisive new results, setup details, and narrowed claims into the manuscript and supply accurate locations. Distinguish an experiment completed during rebuttal from a manuscript revision already completed.

If revisions are unavailable at the current stage, make the allowed response self-contained and describe later integration accurately. A substantially changed empirical argument may require a new review cycle even after useful rebuttal work. Do not assume a promise of camera-ready insertion resolves that issue.

## 7. Express gratitude for scholarly service and keep the answers readable

The archive supports specific scientific lessons much more strongly than it supports any causal claim about winning phrases. This does not make gratitude less valuable. The author's stated preference is to thank reviewers sincerely and fully for their voluntary service, time, effort, careful reading, and professional guidance, regardless of the score or final result.

Follow the warmth of the author's past replies. Recognize specific suggestions and the improvements they enabled. Preserve fuller openings, genuine appreciation within answers, and thoughtful closings when appropriate. Do not automatically compress these into neutral formulas or impose a fixed length. Respect remains equally important when the reviewer is critical. Keep concern labels stable and decisive evidence next to its interpretation so the technical response remains easy to follow.

Use [response-templates.md](response-templates.md) for adaptable language and formats and the private `../../records/analysis/gratitude-examples.md` for original examples when available. These choices reflect the author's values and style. They are not presented as experimentally validated mechanisms for increasing scores.

## 8. Allocate rebuttal effort by what can change the assessment

For a full strategy request, first distinguish factual or presentation misunderstandings, missing but obtainable decisive evidence, unresolved scientific weaknesses, and contribution judgments unlikely to move without a material change. This helps choose the next comparison or rewrite.

Do not estimate acceptance probabilities from this small personal corpus or compare numerical scores across venue scales. Even a reply that does not reverse the decision can reveal the exact revision needed for the next submission. Cross-round improvement is informative, but changed manuscripts, reviewers, and venues prevent attributing the later outcome to one response pattern.
