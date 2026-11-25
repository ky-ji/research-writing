#!/usr/bin/env python3
"""Render a concern-specific Markdown workbench without overwriting a draft.

The assistant prepares a JSON plan from complete reviews. This helper checks
coverage and preserves the supplied original-review Markdown verbatim. It does
not infer scientific answers, parse PDFs, or retrieve venue requirements.
"""

from __future__ import annotations

import argparse
from collections import Counter
import json
from pathlib import Path
import re
import sys


def required_text(value: object, location: str) -> str:
    if not isinstance(value, str) or not value.strip():
        raise ValueError(f"{location} must be a nonempty string")
    return value


def required_list(value: object, location: str) -> list:
    if not isinstance(value, list) or not value:
        raise ValueError(f"{location} must be a nonempty list")
    return value


def validate_plan(plan: object) -> dict:
    if not isinstance(plan, dict):
        raise ValueError("The plan must be a JSON object")
    venue = required_text(plan.get("venue"), "venue")
    if not re.fullmatch(r"[A-Za-z0-9][A-Za-z0-9_-]*", venue):
        raise ValueError("venue must be a filename-safe name such as ICLR or NeurIPS")
    required_text(plan.get("paper_title"), "paper_title")
    required_text(plan.get("source_note"), "source_note")
    if "year" in plan and not isinstance(plan["year"], (str, int)):
        raise ValueError("year must be a string or integer")
    seen_ids = set()
    for index, reviewer in enumerate(required_list(plan.get("reviewers"), "reviewers"), 1):
        loc = f"reviewers[{index}]"
        if not isinstance(reviewer, dict):
            raise ValueError(f"{loc} must be an object")
        reviewer_id = required_text(reviewer.get("id"), f"{loc}.id")
        if not re.fullmatch(r"[A-Za-z0-9_-]+", reviewer_id):
            raise ValueError(f"{loc}.id must be an alphanumeric reviewer ID or alias")
        if reviewer_id.lower() in seen_ids:
            raise ValueError(f"Duplicate reviewer ID {reviewer_id}")
        seen_ids.add(reviewer_id.lower())
        raw = required_text(reviewer.get("original_review"), f"{loc}.original_review")
        for key in ("response_title", "opening", "closing"):
            required_text(reviewer.get(key), f"{loc}.{key}")
        labels = set()
        for item in required_list(reviewer.get("items"), f"{loc}.items"):
            if not isinstance(item, dict):
                raise ValueError(f"{loc}.items entries must be objects")
            label = required_text(item.get("label"), f"{loc}.items.label")
            if not re.fullmatch(r"[A-Z]+[0-9]+[a-z]?", label):
                raise ValueError(f"Invalid concern label {label}")
            if label in labels:
                raise ValueError(f"Duplicate concern label {reviewer_id}-{label}")
            labels.add(label)
            quote = required_text(item.get("quote"), f"{loc}.{label}.quote")
            if quote not in raw:
                raise ValueError(f"{reviewer_id}-{label} is not a verbatim excerpt of its review")
        covered = []
        for response in required_list(reviewer.get("responses"), f"{loc}.responses"):
            if not isinstance(response, dict):
                raise ValueError(f"{loc}.responses entries must be objects")
            required_text(response.get("title"), f"{loc}.responses.title")
            required_text(response.get("body"), f"{loc}.responses.body")
            for label in required_list(response.get("labels"), f"{loc}.responses.labels"):
                if not isinstance(label, str) or label not in labels:
                    raise ValueError(f"Unknown concern label in {reviewer_id}: {label!r}")
                covered.append(label)
        counts = Counter(covered)
        missing = sorted(labels - counts.keys())
        duplicate = sorted(label for label, count in counts.items() if count > 1)
        if missing or duplicate:
            raise ValueError(f"{reviewer_id} coverage mismatch, missing={missing}, repeated={duplicate}")
    return plan


def table_cell(value: object) -> str:
    return str(value).replace("|", r"\|").replace("\n", " ")


def quote_markdown(text: str) -> str:
    """Add blockquote syntax without changing source lines or paragraph breaks."""
    return "\n".join("> " + line if line else ">" for line in text.split("\n"))


def render_response_context(response: dict, items: list[dict]) -> str:
    """Separate the response unit and show its exact reviewer excerpts."""
    source = {item["label"]: item["quote"] for item in items}
    # A merged W/Q response may refer to the same excerpt twice.
    quotes = list(dict.fromkeys(source[label] for label in response["labels"]))
    labels = " & ".join(response["labels"])
    return "\n\n".join([
        "---",
        f"**{labels}. {response['title']}**",
        *(quote_markdown(quote) for quote in quotes),
    ])


def render_reviewer(reviewer: dict, number: int) -> str:
    reviewer_id = reviewer["id"]
    anchor = reviewer_id.lower()
    blocks = [
        f'<a id="reviewer-{anchor}"></a>',
        f"## Reviewer {reviewer_id} (R{number})",
        f'<a id="response-{anchor}"></a>',
        "### Response draft",
        f"<!-- BEGIN RESPONSE {reviewer_id} -->",
        f"**{reviewer['response_title']}**",
        reviewer["opening"].strip(),
    ]
    for answer_number, response in enumerate(reviewer["responses"], 1):
        blocks.extend([
            render_response_context(response, reviewer["items"]),
            f"**A{answer_number}.** {response['body'].strip()}",
        ])
    blocks.extend([
        reviewer["closing"].strip(),
        f"<!-- END RESPONSE {reviewer_id} -->",
        "---",
        f'<a id="review-{anchor}"></a>',
        "### Reviewer comments (reference only)",
        "> The complete review below is source material and is not part of the submitted response.",
        f"<!-- BEGIN ORIGINAL REVIEW {reviewer_id} -->",
        reviewer["original_review"],
        f"<!-- END ORIGINAL REVIEW {reviewer_id} -->",
    ])
    return "\n\n".join(blocks)


def render(plan: dict) -> str:
    venue = " ".join(str(plan.get(key, "")).strip() for key in ("venue", "year")).strip()
    lines = [
        f"# {venue} Rebuttal",
        f"**Paper** {plan['paper_title']}",
        "> Working template for author editing. Fill the bracketed evidence and revision slots before submission. Each reviewer has one response draft followed by the complete original review.",
        plan["source_note"].strip(),
        "<!-- W and Q identify weaknesses and questions in source order. For unnumbered reviews these are author-side labels. The original review text is preserved without inserting these labels. -->",
        "| Reviewer | Rating in source | Confidence in source | Draft | Complete review |\n| --- | --- | --- | --- | --- |",
    ]
    rows = []
    for number, reviewer in enumerate(plan["reviewers"], 1):
        anchor = reviewer["id"].lower()
        rows.append(
            f"| R{number} · {reviewer['id']} | {table_cell(reviewer.get('rating', 'Not supplied'))} "
            f"| {table_cell(reviewer.get('confidence', 'Not supplied'))} "
            f"| [Edit](#response-{anchor}) | [Read](#review-{anchor}) |"
        )
    lines[-1] += "\n" + "\n".join(rows)
    lines.extend(render_reviewer(reviewer, number) for number, reviewer in enumerate(plan["reviewers"], 1))
    return "\n\n".join(lines) + "\n"


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("plan", type=Path, help="Assistant-prepared review and response plan in JSON")
    parser.add_argument("--paper-dir", type=Path, required=True, help="Existing paper directory for VENUE_rebuttal.md")
    args = parser.parse_args(argv)
    try:
        plan = validate_plan(json.loads(args.plan.read_text(encoding="utf-8")))
        paper_dir = args.paper_dir.expanduser().resolve()
        if not paper_dir.is_dir():
            raise ValueError(f"Paper directory does not exist: {paper_dir}")
        output = paper_dir / f"{plan['venue']}_rebuttal.md"
        text = render(plan)
        with output.open("x", encoding="utf-8", newline="") as stream:
            stream.write(text)
    except FileExistsError:
        print(f"Refusing to overwrite {output}. Continue editing the existing draft or choose a different filename/venue label.", file=sys.stderr)
        return 2
    except (ValueError, OSError) as error:
        print(str(error), file=sys.stderr)
        return 2
    count = sum(len(r["responses"]) for r in plan["reviewers"])
    items = sum(len(r["items"]) for r in plan["reviewers"])
    print(f"Created {output}")
    print(f"{len(plan['reviewers'])} reviewers, {items} source items covered by {count} response blocks")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
