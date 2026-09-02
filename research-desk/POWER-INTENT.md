# research-desk — Power Intent

> This is a design/intent doc, not part of the plugin spec. It captures what this
> Power is meant to do so you can come back and flesh out the skills later.
> `POWER-INTENT.md` is ignored by the plugin loader (only `plugin.json`, `skills/`,
> and `mcp.json` matter), so it is safe to keep here.

## Purpose

A behavioral Power that makes research rigorous and honest. It exists because a
plain instruction like "don't hallucinate" does nothing mechanically — this Power
instead enforces *process* rules the agent can actually follow, and adds an
optional export step to turn findings into a shareable file.

## Two skills

### 1. `research` (behavior) — activates when the user asks to research/investigate
Enforceable process rules to flesh out:
- Search multiple independent sources before answering (not the first hit).
- Every non-obvious claim carries an inline citation: `[source](url)`.
- Separate **Verified** (backed by a source) from **Inferred / my analysis**
  (reasoning, not directly sourced) from **Unknown / couldn't verify**.
- Never present an assumption as a fact. If a claim can't be verified, say so.
- Prefer official docs > reputable secondary sources > blogs/forums. Note the
  source type and publish date when recency matters.
- Cross-check conflicting sources and surface the disagreement rather than
  silently picking one.
- End with a short "confidence + gaps" note: what is solid, what is thin.

Open decisions:
- Depth tiers? (e.g. "quick" vs "deep" research) or always thorough.
- How many sources counts as "enough" for a claim.

### 2. `export-findings` (tooling) — activates only when the user asks to export
- ONE stable script, not a per-request generated script.
- `scripts/export.py --format md|csv|pdf --input <structured-json> --output <path>`
- MD: zero deps (plain write). CSV: stdlib `csv`. PDF: render from Markdown,
  requires one optional dependency (e.g. `weasyprint` or `reportlab`) — must
  degrade gracefully and tell the user how to install if missing.
- The agent produces the structured content; the script only handles reliable
  file generation. Export is **on-demand only** (never automatic), per decision.

Open decisions:
- Final PDF library choice + how to document the optional install.
- Structured input shape (sections, tables, sources list) the script expects.

## Why a Power (not steering)
Reusable across every project, and the export script is real bundled tooling —
that combination is what justifies the Power format over repo steering.

## Status
Scaffold only. `SKILL.md` files contain outlines + open decisions to finish later.
