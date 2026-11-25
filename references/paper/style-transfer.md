# Paper Style Transfer

Build on the shared core standards in [Voice and style](../core/voice-and-style.md) and adapt them to formal research manuscripts.

## Argument Before Wording

Identify what the paper asks the reader to understand and why the answer matters. Connect the research need, the relevant limitation of prior work, the central insight, the mechanism, and the evidence. An observation, failure analysis, or secondary mechanism belongs in that argument when it actually explains the design.

Use this as a flexible way to reason rather than a sequence of mandatory slots. Resolve substantive gaps rather than disguising them with polished language. A narrow edit can preserve the existing argument.

## Writing Voice

Prefer specific actions and relationships over abstract labels, inflated adjectives, and difficult new terminology. A method name should make its insight easier to understand. Preserve established terminology and notation across sections.

Shorten repetition and implementation detail while retaining the original claim, its conditions, and its causal or contrastive meaning. A transition such as `yet` or `however` can keep a compressed sentence natural. Do not insert connective phrases mechanically. Follow the shared global punctuation habit by using periods and ordinary conjunctions rather than colons, semicolons, or em-dashes in newly written prose, while keeping required LaTeX and math syntax intact.

## Abstract Style

State why the capability matters and the obstacle addressed by this paper. Explain the common assumption or practice in the closest work, then introduce the essential insight and the mechanism needed to realize it. Keep the method understandable without turning the abstract into a list of heads, hidden states, or other components.

Include advantages only when the preceding story makes them relevant. Do not append annotation-free or external-teacher-free claims merely because they are true.

Introduce evaluation scope naturally with `Across ...`. Integrate benchmark names into the sentence rather than inserting them in parentheses. Select the key numbers that substantiate the contribution and close by connecting the result back to it.

Adjust length and order to the venue and argument. Neither a fixed sentence count nor a second mechanism is required.

## Introduction Style

Develop the abstract's argument with enough context for the reader to understand the problem and insight. Give each paragraph a clear job. Establish the necessary motivation before introducing the method, and keep the method overview proportional to that job.

Read the closest work before summarizing it. Emphasize the shared practice, assumption, and limitation relevant to this paper. Group work into architectural or methodological paradigms along a clear structural axis only when the grouping explains something.

Use an observation or figure when it helps establish the insight. Do not manufacture a diagnostic or secondary failure to complete a template. Contributions should express research claims rather than enumerate components.

## Method And Results

Explain what each necessary design changes and why. Formalize after establishing the meaning of the quantities. Describe an obvious alternative or its failure when that comparison clarifies the method.

Organize experiments around questions and claims. State the result, the strongest relevant comparison, and what the evidence supports. When comparing multiple models or methods, frame them as paradigms along a clear structural axis and state what stays invariant versus what varies systematically. Attribute a gain to a mechanism only when the analysis or ablations support that explanation.

For detailed section guidance, use [Section Playbooks](section-frames.md). For preserving meaning during edits, use [Revision](revision.md). For reviewer responses, use [Rebuttal Mode](../rebuttal/workflow.md).
