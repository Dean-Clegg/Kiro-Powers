#!/usr/bin/env python3
"""
export.py — stable exporter for research-desk findings.

ONE stable script. The agent produces structured findings as JSON; this script
turns them into a file. Do NOT generate a new script per request.

Expected input JSON shape (draft — refine later):
{
  "title": "string",
  "summary": "string",
  "findings": [
    {"text": "string", "label": "Verified|Inferred|Unknown", "source": "https://..."}
  ],
  "sources": ["https://...", "..."]
}

Usage:
  python3 export.py --format md  --input findings.json --output report.md
  python3 export.py --format csv --input findings.json --output report.csv
  python3 export.py --format pdf --input findings.json --output report.pdf

Formats:
  md   zero dependencies
  csv  stdlib only
  pdf  requires an optional dependency; degrades gracefully with instructions
"""
import argparse
import csv
import json
import sys


def load(input_path):
    with open(input_path, "r", encoding="utf-8") as f:
        return json.load(f)


def render_markdown(data):
    lines = []
    lines.append(f"# {data.get('title', 'Research Findings')}\n")
    if data.get("summary"):
        lines.append("## Summary\n")
        lines.append(data["summary"] + "\n")
    findings = data.get("findings", [])
    if findings:
        lines.append("## Findings\n")
        for f in findings:
            label = f.get("label", "")
            src = f.get("source", "")
            tag = f"**[{label}]** " if label else ""
            cite = f" ([source]({src}))" if src else ""
            lines.append(f"- {tag}{f.get('text', '')}{cite}")
        lines.append("")
    sources = data.get("sources", [])
    if sources:
        lines.append("## Sources\n")
        for s in sources:
            lines.append(f"- {s}")
        lines.append("")
    return "\n".join(lines)


def write_md(data, output_path):
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(render_markdown(data))


def write_csv(data, output_path):
    with open(output_path, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["label", "finding", "source"])
        for item in data.get("findings", []):
            writer.writerow([
                item.get("label", ""),
                item.get("text", ""),
                item.get("source", ""),
            ])


def write_pdf(data, output_path):
    # PDF requires an optional dependency. Library choice is an open decision.
    # Draft implementation via weasyprint; degrade gracefully if unavailable.
    try:
        from weasyprint import HTML  # type: ignore
    except ImportError:
        sys.stderr.write(
            "PDF export needs an optional dependency that isn't installed.\n"
            "Install it (e.g. `pip install weasyprint`) or export Markdown "
            "instead: --format md\n"
        )
        return 3
    md = render_markdown(data)
    # Minimal MD->HTML; replace with a real renderer when finalizing.
    html_body = "<pre style='font-family:sans-serif'>" + (
        md.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
    ) + "</pre>"
    HTML(string=html_body).write_pdf(output_path)
    return 0


def main():
    parser = argparse.ArgumentParser(description="Export research findings.")
    parser.add_argument("--format", required=True, choices=["md", "csv", "pdf"])
    parser.add_argument("--input", required=True, help="Path to findings JSON")
    parser.add_argument("--output", required=True, help="Output file path")
    args = parser.parse_args()

    data = load(args.input)

    if args.format == "md":
        write_md(data, args.output)
    elif args.format == "csv":
        write_csv(data, args.output)
    elif args.format == "pdf":
        code = write_pdf(data, args.output)
        if code:
            return code

    print(f"Wrote {args.output}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
