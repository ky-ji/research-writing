# Visual Clarity for Figures and Tables (Shared Core)

Figures and tables carry core research arguments rather than serving as decoration. Use these shared rules across papers and blogs, then apply mode-specific specs in [references/paper/section-frames.md](../paper/section-frames.md) or [references/blog/figures.md](../blog/figures.md).

## 1. One Message per Visual

Decide what the reader should learn before drawing. Write the takeaway sentence first and design the visual so that takeaway is obvious within a few seconds. Cut or relegate any panel or table that maps to no claim in the argument.

## 2. Role Clarity

Distinguish each visual's job clearly.

- **Teaser or Hero (Figure 1)** communicates the central insight and why it matters without requiring the surrounding prose. Prefer real data or real frames over cartoons, and clearly label conceptual schematics as schematics.
- **Method or Architecture figure** explains the mechanism, information flow, and dependencies, distinguishing training from inference and inputs from outputs where relevant.
- **Diagnostic or Observation figure** establishes the surprising behavior or bottleneck motivating the work.
- **Result or Ablation figure** answers one specific empirical question cleanly.

## 3. Clean Encoding and Typography

- **Consistent color and symbol semantics.** Assign fixed meanings to colors and markers for the entire document (for example, one accent for the proposed or reachable regime, a second accent for failure or trap, neutral greys for baselines and context). Limit accents to at most two whenever possible.
- **Direct labels over cluttered legends.** Label lines, regions, and endpoints directly when space allows. If a legend is necessary, keep it short and non-overlapping.
- **Plain-word labels.** Avoid raw code identifiers or unexplained internal acronyms in axis titles, ticks, or legends. Use proper subscripts and units.
- **Minimal chrome.** Use clean white backgrounds, light gridlines, no decorative 3D effects, and no unnecessary boxes or shadows.

## 4. Captions, Alignment, and Reproducibility

- **Takeaway plus setting.** State what the visual shows and provide the exact setting needed to interpret it (axes, units, sample size N, seeds, uncertainty bars, and what colors or marks mean) instead of narrating every single number.
- **Exact numeric alignment.** Every value and rounding choice in a figure or table must match the running prose and archived source logs.
- **Reproducible generation.** Generate data figures with scripts reading archived JSON, CSV, or logs. Fix figure-generation scripts rather than hand-editing rendered SVGs or PDFs.
- **Visual inspection.** Inspect rendered outputs after regeneration to catch clipped numbers, colliding labels, overlapping legends, and illegible font sizes.
