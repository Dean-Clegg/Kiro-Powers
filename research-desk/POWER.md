---
name: "research-desk"
displayName: "Research Desk"
description: "Evidence-first research assistant. Activate by asking to research or investigate a topic. Takes its time, searches multiple sources, backs every claim with a citation, clearly separates verified facts from inference, and can export findings to Markdown, CSV, or PDF on request."
keywords: ["research", "citations", "fact-checking", "anti-hallucination", "export", "report", "investigation"]
author: "Dean Clegg"
---

# Research Desk

> **Status: early scaffold (v0.1.0).** The behavior and export script work, but
> the rules and export format are still being refined. See `POWER-INTENT.md` for
> the design intent and open decisions.

## Overview

**Research Desk** turns a research request into a thorough, honest investigation
instead of a first-plausible-answer guess. It searches multiple independent
sources, backs every claim with a citation, and clearly separates what is
**verified** from what is **inferred** from what it **couldn't confirm**. When
you ask, it can export the findings to a Markdown, CSV, or PDF report.

It is for **researching topics and producing reports** — not for building code.

## How It Works

1. **Search before answering.** It consults multiple independent sources rather
   than the first hit, preferring official docs over reputable secondary sources
   over blogs and forums, and notes source type and date when recency matters.
2. **Cite everything.** Every non-obvious claim carries an inline `[source](url)`.
3. **Label honestly.** Each finding is tagged **Verified** (backed by a source),
   **Inferred** (reasoning, not directly sourced), or **Unknown** (couldn't
   verify) — assumptions are never presented as facts.
4. **Surface disagreement.** When sources conflict, it shows the conflict instead
   of silently picking one, and closes with a short "confidence & gaps" note.
5. **Export on request.** Only when you ask, it hands off to the export skill to
   generate a report file.

## Skills

- **research** — the evidence-first investigation behavior (cite, label, verify).
- **export-findings** — writes findings to Markdown, CSV, or PDF via a single
  stable script. Markdown and CSV need no dependencies; PDF needs one optional
  library and degrades gracefully if it isn't installed. Export is on-demand only.

## Getting Started

After installing, just say:

- **"research [topic]"** or **"investigate / look into [topic]"** — runs the
  evidence-first investigation.
- **"export that to PDF / Markdown / CSV"** — turns the findings into a report
  file (only when you ask).

## Structure

```
plugin.json                              # agent-plugins manifest (loader)
POWER.md                                 # metadata + overview (this file)
POWER-INTENT.md                          # design intent + open decisions
skills/
  research/SKILL.md                      # evidence-first research behavior
  export-findings/SKILL.md               # export to md / csv / pdf
  export-findings/scripts/export.py      # stable export script
```

## License

MIT. See [LICENSE](../LICENSE).
