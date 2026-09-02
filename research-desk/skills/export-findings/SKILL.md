---
name: "export-findings"
description: "Export research findings to a Markdown, CSV, or PDF file using a stable export script. Use only when the user explicitly asks to export, save, or generate a document/report from research results."
license: "MIT"
metadata:
  author: "Dean Clegg"
  version: "0.1.0"
---

# Export Findings

## Overview
Writes research output to a file in a reliable, repeatable way. The agent
produces the content; a single stable script handles file generation so output
is deterministic across formats.

> STATUS: SCAFFOLD. The script is a working stub for MD/CSV; PDF is a documented
> optional path. Refine the input shape and PDF library later.

## Key Principle
ONE stable script — never generate a new script per request. The agent fills in
structured content; `scripts/export.py` turns it into a file.

## Usage (draft)

```bash
python3 scripts/export.py --format md   --input findings.json --output report.md
python3 scripts/export.py --format csv  --input findings.json --output report.csv
python3 scripts/export.py --format pdf  --input findings.json --output report.pdf
```

- **md** — zero dependencies.
- **csv** — Python stdlib only.
- **pdf** — requires one optional dependency (see Troubleshooting). Degrades
  gracefully: if missing, the script tells the user how to install it and can
  fall back to Markdown.

## Rules
- Export is ON-DEMAND ONLY. Never export unless the user asks.
- Confirm the output path and format before writing.

## Input Shape (draft — refine later)
See `scripts/export.py` header for the expected JSON structure
(title, summary, findings[], sources[]).

## Troubleshooting

### PDF export fails with a missing-module error
**Cause:** the PDF backend isn't installed.
**Solution:** install it (library TBD, e.g. `pip install weasyprint`) or export
Markdown and convert separately.

## Open Decisions (finish later)
- [ ] Final PDF library choice.
- [ ] Exact structured-input schema (tables? nested sections?).
- [ ] Default output directory.
