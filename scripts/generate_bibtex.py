#!/usr/bin/env python3
"""
generate_bibtex.py — Export BibTeX entries from MIR registry files.

Usage:
    python generate_bibtex.py <entry.json>                  # Single entry
    python generate_bibtex.py data/entries/                  # All entries in directory
    python generate_bibtex.py data/entries/ -o registry.bib  # Write to .bib file
"""

import json
import sys
import argparse
from pathlib import Path
from datetime import datetime


MONTHS = ["jan", "feb", "mar", "apr", "may", "jun",
          "jul", "aug", "sep", "oct", "nov", "dec"]


def entry_to_bibtex(entry: dict) -> str:
    """Convert a single MIR entry to a BibTeX record."""
    # Use pre-formatted if available
    if entry.get("citation", {}).get("bibtex"):
        return entry["citation"]["bibtex"]

    creator = entry["creator"]["name"]
    parts = creator.rsplit(" ", 1)
    author = f"{parts[1]}, {parts[0]}" if len(parts) == 2 else creator

    dt = datetime.strptime(entry["datePublished"], "%Y-%m-%d")

    last = parts[1].lower() if len(parts) == 2 else creator.lower().replace(" ", "")
    title_words = "".join(c for c in entry["title"] if c.isalnum() or c == " ").split()
    title_key = "".join(title_words[:3]).lower()
    cite_key = f"{last}{dt.year}{title_key}"

    url = entry.get("platform", {}).get("url", "")
    platform = entry.get("platform", {}).get("name", "")
    genre = entry.get("genre", ["Video"])
    if isinstance(genre, list):
        genre = genre[0] if genre else "Video"

    lines = [
        f"@misc{{{cite_key},",
        f"  author       = {{{author}}},",
        f"  title        = {{{entry['title']}}},",
        f"  year         = {{{dt.year}}},",
        f"  month        = {MONTHS[dt.month - 1]},",
        f"  day          = {{{dt.day}}},",
        f"  howpublished = {{{platform}}},",
        f"  url          = {{{url}}},",
    ]

    doi = entry.get("doi")
    if doi:
        lines.append(f"  doi          = {{{doi}}},")

    lines.append(f"  note         = {{{genre.title()}. MIR ID: {entry['@id']}}}")
    lines.append("}")

    return "\n".join(lines)


def main():
    parser = argparse.ArgumentParser(description="Export BibTeX from MIR entries")
    parser.add_argument("path", type=Path, help="Entry file or directory of entries")
    parser.add_argument("-o", "--output", type=Path, default=None,
                        help="Output .bib file (default: stdout)")
    args = parser.parse_args()

    if args.path.is_file():
        files = [args.path]
    elif args.path.is_dir():
        files = sorted(args.path.glob("*.json"))
    else:
        print(f"ERROR: {args.path} not found", file=sys.stderr)
        sys.exit(1)

    records = []
    for fp in files:
        with open(fp, "r", encoding="utf-8") as f:
            entry = json.load(f)
        records.append(entry_to_bibtex(entry))

    output = "\n\n".join(records) + "\n"

    if args.output:
        args.output.write_text(output, encoding="utf-8")
        print(f"Wrote {len(records)} BibTeX entries to {args.output}")
    else:
        print(output)


if __name__ == "__main__":
    main()
