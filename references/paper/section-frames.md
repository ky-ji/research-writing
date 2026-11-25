# Paper Section Playbooks

## Abstract

Compress the paper into a clear argument about the problem, essential insight, mechanism, and evidence. Explain the real objective rather than replacing it with an incidental benefit such as throughput.

Keep only advantages prepared by that argument. Describe the insight rather than a list of implementation components. Use `Across ...` to introduce evaluation scope, avoid parenthetical benchmark insertions, report the key supported numbers, and end with their implication for the contribution.

Use the length and sentence structure the argument needs. Pair quality with cost or another metric when the claim is about that trade-off, not as a compulsory pattern for every paper.

## Introduction

Plan backward from the contribution. Identify the specific difficulty it resolves, the closest prior approaches that encounter it, and what the proposed insight changes. Explain the technical reason for the difficulty when the available sources support it. For a new task without direct precedents, define the concrete challenges and draw on adjacent work where it helps the reader understand them.

Draft forward from the task and why it matters to the relevant technical challenge, then explain the insight, the method that realizes it, and the resulting contribution. Follow the logic of the abstract and give each paragraph a clear job. Keep the method overview concise enough to serve the introduction.

Summarize shared assumptions rather than collecting citations or forcing a taxonomy. A figure, concrete scenario, or number can provide the necessary context when available.

Prefer verbal explanations in the introduction. Add a formula only when it has an irreplaceable explanatory role. Put formal definitions in preliminaries or the method when appropriate, and retain finalized equations during edits.

Write contributions as research claims supported by the paper. Choose their number from the actual contributions rather than a preset count.

## Related Work

Position the paper through the closest methods and the assumptions relevant to its question. Use categories or architectural paradigms only when they clarify the comparison. Represent prior work fairly, attach citations to the claims they support, and explain the difference that motivates this paper.

Avoid unsupported claims that no one has studied the problem. A paragraph need not end with a criticism when background or a complementary result is its purpose.

## Method

Before drafting, trace each substantive design from its inputs through its operations to its outputs. Identify which later steps use those outputs. Use a working pipeline sketch when it clarifies dependencies or helps choose the order of the subsections.

Open with an overview of the actual approach and its relationship to the insight. Define the problem and quantities needed to understand the design. Explain mechanisms in an order that makes their dependencies clear.

For each substantive design, explain the problem it addresses, how it operates, and what advantage or consequence follows. Ground the consequence in the mechanism, analysis, or measured result that supports it. Include a simple alternative or a failure analysis when the comparison helps explain the design choice. Let the method determine the number of subsections.

### Equations And Pipelines

Explain why a quantity matters before formalizing it and state an equation's role in plain language. Keep notation consistent. Use algorithms for procedures that benefit from explicit steps and pipeline figures for coordination or interactions.

## Experiments

Start from the principal empirical claims and identify the comparison, control, or evaluation setting needed to assess each one. Include the strongest relevant baselines and make the comparison protocol explicit. State what is held fixed and what changes. When the claim depends on coupled choices, consider ablations that can distinguish the effect of each choice from their interaction. Report the harder conditions and failure cases that define the scope of a generalization claim.

Explain the benchmarks, metrics, hardware, training or inference settings, and sample sizes needed to interpret each comparison. Preserve important settings and sample counts when shortening the text.

When comparing multiple models, organize them by canonical architectural or methodological paradigm along a clear axis (naming checkpoints as representative instances) and state both invariants and systematic differences.

Use the main text for decisive comparisons and trends. Place full result matrices and supporting detail in the appendix, with clear references from the text. Retain materially contradictory results and conditions needed to interpret headline findings.

Order results to answer the paper's questions. Include hard cases, generality tests, ablations, or diagnostics when relevant to those claims. Report actual trade-offs. Distinguish observed associations from supported causal explanations.

## Figures And Captions

Follow [Visual clarity](../core/visual-clarity.md). Understand the method or experiment before drawing. Decide what the reader should learn and make the relationships clear.

- A teaser communicates the central insight and why it matters.
- A method figure explains the mechanism, flow, and important dependencies.
- An observation or diagnostic figure establishes a relevant pattern or explains behavior.
- A result or ablation figure answers a specific empirical question.

Use consistent symbols, readable labels, and arrows with clear meanings. Distinguish training from inference, inputs from outputs, and measured results from conceptual illustrations when relevant. Choose editable or image formats according to the request.

A caption should state the takeaway and the setting needed to interpret it. Define axes, units, sample sizes, and uncertainty when applicable rather than narrating every number.

## Conclusion

Return to the resolved problem, the essential insight, and what the evidence establishes. Add no new unsupported claim. Include factual, relevant limitations or other venue-required material without a stock defensive ending.
