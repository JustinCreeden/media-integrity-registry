#!/usr/bin/env python3
"""
generate_citation.py — Generate formatted citations from MIR entries.

Usage:
    python generate_citation.py <entry.json> --format apa
    python generate_citation.py <entry.json> --format mla
    python generate_citation.py <entry.json> --format chicago
    python generate_citation.py <entry.json> --format all

If the entry already has pre-formatted citations, those are returned.
Otherwise, citations are generated from the structured metadata.
"""

import json
import sys
import argparse
from pathlib import Path
from datetime import datetime


def parse_date(date_str: str) -> datetime:
    """Parse ISO 8601 date string."""
    return datetime.strptime(date_str, "%Y-%m-%d")


def format_apa(entry: dict) -> str:
    """Generate APA 7th edition citation."""
    # Check for pre-formatted
    if entry.get("citation", {}).get("apa"):
        return entry["citation"]["apa"]

    creator = entry["creator"]["name"]
    parts = creator.rsplit(" ", 1)
    if len(parts) == 2:
        author = f"{parts[1]}, {parts[0][0]}."
    else:
        author = creator

    channel = entry.get("platform", {}).get("channelName", "")
    channel_str = f" [{channel}]" if channel else ""

    dt = parse_date(entry["datePublished"])
    date_str = f"({dt.year}, {dt.strftime('%B')} {dt.day})"

    title = entry["title"]
    media_type = entry.get("mediaType", "video").capitalize()
    platform = entry.get("platform", {}).get("name", "")
    url = entry.get("platform", {}).get("url", "")

    doi = entry.get("doi")
    if doi:
        location = f"https://doi.org/{doi}"
    else:
        location = url

    return f"{author}{channel_str}. {date_str}. {title} [{media_type}]. {platform}. {location}"


def format_mla(entry: dict) -> str:
    """Generate MLA 9th edition citation."""
    if entry.get("citation", {}).get("mla"):
        return entry["citation"]["mla"]

    creator = entry["creator"]["name"]
    parts = creator.rsplit(" ", 1)
    if len(parts) == 2:
        author = f"{parts[1]}, {parts[0]}"
    else:
        author = creator

    title = entry["title"]
    platform = entry.get("platform", {}).get("name", "")
    channel = entry.get("platform", {}).get("channelName", "")
    dt = parse_date(entry["datePublished"])
    months = ["Jan.", "Feb.", "Mar.", "Apr.", "May", "June",
              "July", "Aug.", "Sept.", "Oct.", "Nov.", "Dec."]
    date_str = f"{dt.day} {months[dt.month - 1]} {dt.year}"
    url = entry.get("platform", {}).get("url", "").replace("https://", "").replace("http://", "")

    return f'{author}. "{title}." {platform}, uploaded by {channel}, {date_str}, {url}.'


def format_chicago(entry: dict) -> str:
    """Generate Chicago 17th edition (Notes-Bibliography) citation."""
    if entry.get("citation", {}).get("chicago"):
        return entry["citation"]["chicago"]

    creator = entry["creator"]["name"]
    title = entry["title"]
    platform = entry.get("platform", {}).get("name", "")
    dt = parse_date(entry["datePublished"])
    date_str = f"{dt.strftime('%B')} {dt.day}, {dt.year}"
    url = entry.get("platform", {}).get("url", "")

    return f'{creator}, "{title}," {platform}, {date_str}, video, {url}.'


def format_bibtex(entry: dict) -> str:
    """Generate BibTeX citation."""
    if entry.get("citation", {}).get("bibtex"):
        return entry["citation"]["bibtex"]

    creator = entry["creator"]["name"]
    parts = creator.rsplit(" ", 1)
    if len(parts) == 2:
        author = f"{parts[1]}, {parts[0]}"
    else:
        author = creator

    dt = parse_date(entry["datePublished"])
    months = ["jan", "feb", "mar", "apr", "may", "jun",
              "jul", "aug", "sep", "oct", "nov", "dec"]

    # Generate a cite key
    last_name = parts[1].lower() if len(parts) == 2 else creator.lower().replace(" ", "")
    title_key = "".join(w for w in entry["title"].split()[:3] if w.isalnum()).lower()
    cite_key = f"{last_name}{dt.year}{title_key}"

    url = entry.get("platform", {}).get("url", "")
    platform = entry.get("platform", {}).get("name", "")
    genre = entry.get("genre", ["Video"])[0] if isinstance(entry.get("genre"), list) else entry.get("genre", "Video")

    lines = [
        f"@misc{{{cite_key},",
        f"  author       = {{{author}}},",
        f"  title        = {{{entry['title']}}},",
        f"  year         = {{{dt.year}}},",
        f"  month        = {months[dt.month - 1]},",
        f"  day          = {{{dt.day}}},",
        f"  howpublished = {{{platform}}},",
        f"  url          = {{{url}}},",
        f"  note         = {{{genre.title()}. Accessed {datetime.now().strftime('%Y-%m-%d')}.}}",
        "}"
    ]

    doi = entry.get("doi")
    if doi:
        lines.insert(-1, f"  doi          = {{{doi}}},")

    return "\n".join(lines)


FORMATTERS = {
    "apa": format_apa,
    "mla": format_mla,
    "chicago": format_chicago,
    "bibtex": format_bibtex,
}


def main():
    parser = argparse.ArgumentParser(description="Generate citations from MIR entries")
    parser.add_argument("entry", type=Path, help="Path to a MIR entry JSON file")
    parser.add_argument("--format", "-f", choices=["apa", "mla", "chicago", "bibtex", "all"],
                        default="all", help="Citation format (default: all)")
    args = parser.parse_args()

    with open(args.entry, "r", encoding="utf-8") as f:
        entry = json.load(f)

    print(f"Citations for: {entry['title']}")
    print(f"MIR ID: {entry['@id']}")
    print("=" * 60)

    formats = FORMATTERS.keys() if args.format == "all" else [args.format]
    for fmt in formats:
        print(f"\n--- {fmt.upper()} ---")
        print(FORMATTERS[fmt](entry))

    print()


if __name__ == "__main__":
    main()
