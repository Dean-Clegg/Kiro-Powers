---
name: "research"
description: "Conduct evidence-first research that backs every claim with a citation and separates verified facts from inference. Use when the user asks to research, investigate, look into, or find out about a topic."
license: "MIT"
metadata:
  author: "Dean Clegg"
  version: "0.1.0"
---

# Research Desk

## Overview
Turns a research request into a thorough, honest investigation. Instead of the
first plausible answer, it searches multiple independent sources, cites each
claim, and clearly labels what is verified versus inferred versus unknown.

> STATUS: SCAFFOLD. The rules below are an outline to refine. Open decisions are
> listed at the bottom.

## Core Rules (draft)

1. Search before answering. Consult multiple independent sources, not the first hit.
2. Cite every non-obvious claim inline as `[source](url)`.
3. Label each finding: **Verified** (backed by a source), **Inferred** (my
   reasoning, not directly sourced), or **Unknown** (couldn't verify).
4. Never present an assumption as a fact. If it can't be verified, say so plainly.
5. Prefer official docs > reputable secondary sources > blogs/forums. Note source
   type and publish date when recency matters.
6. When sources conflict, surface the disagreement instead of silently choosing.
7. Close with a short "Confidence & gaps" note: what is solid, what is thin.

## Output Shape (draft)

- **Summary** — the direct answer, one short paragraph.
- **Findings** — bulleted, each with a citation and a Verified/Inferred label.
- **Sources** — list of links used.
- **Confidence & gaps** — what couldn't be confirmed.

## Exporting

If the user asks to save/export the findings, hand off to the `export-findings`
skill. Do NOT export automatically.

## Open Decisions (finish later)
- [ ] Depth tiers ("quick" vs "deep") or always thorough?
- [ ] Minimum number of sources before a claim counts as Verified?
- [ ] Any domains to always trust / always distrust for your work?
