# Research Blog Mode Workflow

A research blog is not a compressed paper. A paper proves a claim to reviewers, while a blog makes **one idea** stick in a busy reader's head. Every structural decision below serves that difference while inheriting the shared core rules in `SKILL.md` (including evidence integrity, anti-hype Classic style, paradigm-over-checkpoint framing, and the global punctuation habit).

## Blog-Specific Core Principles

1. **One idea.** The post has exactly one thing the reader should remember, stated in at most 20 words. Every section, figure, and table must support it, or move to an appendix, collapsible block, or a separate post.
2. **Concrete before abstract.** Start from a specific thing the reader can picture (one scene, one rollout, one surprising number). Then generalize to statistics. Only then explain the mechanism and introduce jargon.
3. **Figures carry the argument.** Figure 1 is a schematic or real-frame contrast that explains the idea without the text. Data figures then confirm it. A reader who sees only the figures and headings should get the whole story.
4. **Headings are claims.** Write "Removing the VLM widens the prior" rather than "Results" or "Analysis". The table of contents alone should read like an abstract.
5. **One number per sentence, few per paragraph.** Readers remember at most 3 numbers per post. Put the rest in tables, figures, or collapsible blocks.
6. **Rigor lives below the fold.** Keep protocols, padding dimensions, seeds, N per condition, and ablation grids accurate, and place them in `<details>`, captions, or an appendix. The main text holds only the reasoning chain.
7. **Honest scope.** State what the evidence shows (for example, an existence result with an oracle) right where the claim is made, not only in Limitations.
8. **Classic style (Pinker) with global punctuation.** Write as if pointing at something you both can see, with plain words, active voice, short sentences, no hedging stacks, and no hype. Write newly drafted prose as complete connected sentences without colons, semicolons, or em-dashes, and omit trailing colons in headings (preserve technical syntax in code, KaTeX, BibTeX, and URLs).
9. **Paradigm over checkpoint.** Frame multi-model comparisons as canonical architectural paradigms along an explicit structural axis, with checkpoints named as representative instances, stating both what is invariant and what varies systematically.

## Five-Phase Workflow

Follow these phases in order for new posts or full rewrites. Do not start drafting prose before Phase 2 is complete. For bounded local edits, respect the requested scope and run the relevant items in [checklist.md](checklist.md).

### Phase 1 Distill Before Writing

Produce a short plan and show it to the user when the topic is new.

- **The one sentence** (at most 20 words). Test whether a colleague would repeat it at lunch.
- **The surprise.** State what the reader believes before reading and what they should believe after. If nothing is counter-intuitive, the post is a report rather than a blog.
- **The hook.** Pick the single most concrete observation that makes the question unavoidable.
- **Reasoning chain.** Write 3 to 5 claims, each one sentence, each serving as a future section heading.
- **Evidence map.** Map each claim to the one figure or table that proves it, and drop evidence that maps to no claim.
- **Cut list.** Move everything true yet off the main chain to an appendix, `<details>`, or a follow-up post.

### Phase 2 Figure Plan

Read [figures.md](figures.md) and [Visual clarity](../core/visual-clarity.md). Decide the full visual sequence.

- **Figure 1 (schematic or hero)** presents the idea as one picture, ideally from real data or real frames (such as a grid of robot rollout end-frames comparing success and failure under each condition) rather than cartoons alone.
- **One data figure per claim**, each with a title and one-sentence takeaway above and a short caption below.
- **One fixed color semantic** for the whole post (for example, blue for good or reachable, orange for failure or trap, grey for baseline), declared once.

### Phase 3 Draft Using The Skeleton

Read [structure.md](structure.md). Follow these drafting rules.

- Keep paragraphs to at most 4 sentences with one idea per paragraph.
- Define every term the first time it appears in plain words, then use it consistently.
- Replace code identifiers in running prose (`other_scene_vlm`) with plain names ("wrong scene") and keep identifiers only in tables or `<details>`.
- End each section with the question the next section answers, using light transitions rather than "Next, we...".
- Prefer a short list or compact table when comparing 3 or more conditions.

### Phase 4 Edit (The Most Important Phase)

Run every item in [checklist.md](checklist.md). A typical edit pass removes 25 to 40 percent of words.

- Delete throat-clearing openings and summary-of-what-I-just-said closings.
- Cut adjectives that judge your own results.
- Replace colons, semicolons, and em-dashes in prose with clean periods or ordinary conjunctions.
- Read each paragraph aloud mentally and rewrite any sentence you stumble on.
- Verify every number against the source data and keep rounding identical across prose, figures, and tables.

### Phase 5 Visual Verification

For HTML posts, serve locally, screenshot the full page at 1440px and at true 390px mobile width (use an iframe wrapper for true mobile width with headless Chrome), and inspect every figure for label collisions, legend overlap, unreadable sizes, and inconsistent rounding. Fix figure generators (scripts) rather than hand-editing SVG output so figures stay reproducible.

## Blog Reference Files

- [structure.md](structure.md) for the section skeleton, opening and closing patterns, and TL;DR template.
- [figures.md](figures.md) for web figure design rules and the figure-type cookbook.
- [checklist.md](checklist.md) for the pre-publish review checklist across content, prose, figures, rigor, and visual HTML.
- [exemplars.md](exemplars.md) for style traits to borrow from top researcher blogs and how to study a user-named reference.
- [house-style.md](house-style.md) for `ky-ji.github.io/blogs/` file layout, CSS components, SVG specs, and index updates.
