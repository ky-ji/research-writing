# Blog Figures

Apply [Visual clarity](../core/visual-clarity.md) together with the web-specific layout rules below.

## Rules

1. **One message per figure.** Write the takeaway sentence first, then design the figure so that sentence is visually obvious within 3 seconds.
2. **Three-part frame.** Place an HTML title (`Figure n · ...`) and a one-sentence takeaway above, the image in the middle, and a short caption below (setup, N, and what the marks mean). Never hide the conclusion only inside the caption.
3. **Color equals meaning.** Fix color semantics for the whole post (for example, blue for good, wide, or reachable, orange for failure, trap, or wrong, dark grey for baseline, and light grey for context). Use at most 2 accents.
4. **Direct labels over legends.** Label lines and points at their ends. If a legend is necessary, keep it to at most 3 short items.
5. **Plain-word labels.** Avoid code identifiers (`zero_vlm_mask`) or internal acronyms in figures. Write "no VLM" or "wrong scene", and render real subscripts.
6. **Zero chrome.** Keep a white background, no boxes or shadows, whisper-light gridlines, no 3D, and no rotated text when avoidable.
7. **Native width matches the reading column** (roughly 720 to 740px) so 10.5 to 13px text renders at true size. Verify at 390px mobile width too, allowing horizontal scroll only for schematics.
8. **No collisions.** After every regeneration, screenshot each SVG at 1.5x and inspect labels versus lines, labels versus labels, legend versus axis titles, and clipped edge numbers.
9. **Same numbers, same rounding** across prose, figures, and tables.
10. **Reproducible.** Generate every data figure from archived results with a script, and edit the script rather than the SVG output.

## Figure-Type Cookbook

| Message | Figure type |
|---|---|
| The idea or mechanism | Schematic with 2 to 3 side-by-side panels in identical layout where only the key element changes |
| "It really happens" | Real frames or video grid with rows as conditions, columns as seeds, and outlines for success versus failure |
| Scaling or trend | Line chart with at most 3 lines, directly labeled endpoints, and a bracket highlighting the gap |
| A beats B across settings | Dot or dumbbell plot (cleaner than grouped bars) |
| Composition or share | Single stacked bar per row with percentages inside the bar |
| Two quantities trade off | Scatter plot with shaded "good" and "bad" regions labeled in plain words |
| Per-item distribution | Histogram with the interesting bins shaded and named |
| Architecture comparison | Rows of identical pill-and-arrow diagrams, one row per design, with the outcome in the last column |

## Hero / Figure 1 Checklist

- Understandable without reading anything else.
- Shows the contrast that is the post's surprise (for example, absent conditioning being wide yet reachable versus wrong conditioning being tight yet trapped).
- Prefers real data or real frames, with any cartoon clearly labeled as a schematic.
- Uses interactive toggles only when switching models or settings reveals that the same pattern holds.
