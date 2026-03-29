#!/usr/bin/env python3
"""
validate_registry.py — Validate MIR entries against the JSON Schema.

Usage:
    python validate_registry.py <entry.json>
    python validate_registry.py data/entries/       # Validate all entries in a directory
    python validate_registry.py                     # Validate all entries in data/entries/

Requires: pip install jsonschema
"""

import json
import sys
import os
from pathlib import Path

try:
    from jsonschema import validate, ValidationError, Draft202012Validator
except ImportError:
    print("ERROR: jsonschema is not installed.")
    print("Install it with: pip install jsonschema")
    sys.exit(1)

# Resolve paths relative to the repo root
SCRIPT_DIR = Path(__file__).resolve().parent
REPO_ROOT = SCRIPT_DIR.parent
SCHEMA_PATH = REPO_ROOT / "data" / "schema.json"
ENTRIES_DIR = REPO_ROOT / "data" / "entries"


def load_schema():
    """Load the MIR JSON Schema."""
    if not SCHEMA_PATH.exists():
        print(f"ERROR: Schema file not found at {SCHEMA_PATH}")
        sys.exit(1)
    with open(SCHEMA_PATH, "r", encoding="utf-8") as f:
        return json.load(f)


def validate_entry(filepath: Path, schema: dict) -> list[str]:
    """Validate a single entry file. Returns list of error messages."""
    errors = []
    try:
        with open(filepath, "r", encoding="utf-8") as f:
            entry = json.load(f)
    except json.JSONDecodeError as e:
        return [f"Invalid JSON: {e}"]

    # Schema validation
    validator = Draft202012Validator(schema)
    for error in sorted(validator.iter_errors(entry), key=lambda e: list(e.path)):
        path = " → ".join(str(p) for p in error.absolute_path) or "(root)"
        errors.append(f"  [{path}] {error.message}")

    # Additional semantic checks beyond JSON Schema
    if entry.get("aiGenerated") != "none" and not entry.get("aiDisclosure", {}).get("tools"):
        errors.append("  [aiDisclosure.tools] Must list AI tools when aiGenerated is not 'none'")

    if entry.get("archival", {}).get("localCopy") and not entry.get("archival", {}).get("localPath"):
        errors.append("  [archival.localPath] Required when localCopy is true")

    if entry.get("archival", {}).get("localCopy") and not entry.get("archival", {}).get("archiveDate"):
        errors.append("  [archival.archiveDate] Required when localCopy is true")

    if entry.get("mediaType") in ("video", "audio") and not entry.get("duration"):
        errors.append("  [duration] Recommended for video/audio entries (ISO 8601 duration)")

    return errors


def main():
    schema = load_schema()

    # Determine targets
    if len(sys.argv) > 1:
        target = Path(sys.argv[1])
        if target.is_file():
            targets = [target]
        elif target.is_dir():
            targets = sorted(target.glob("*.json"))
        else:
            print(f"ERROR: {target} is not a file or directory")
            sys.exit(1)
    else:
        targets = sorted(ENTRIES_DIR.glob("*.json"))

    if not targets:
        print("No JSON files found to validate.")
        sys.exit(0)

    print(f"Validating {len(targets)} entries against {SCHEMA_PATH.name}...\n")

    total_errors = 0
    for filepath in targets:
        errors = validate_entry(filepath, schema)
        if errors:
            print(f"✗ {filepath.name}")
            for err in errors:
                print(f"  {err}")
            total_errors += len(errors)
        else:
            print(f"✓ {filepath.name}")

    print(f"\n{'='*50}")
    print(f"Files checked: {len(targets)}")
    print(f"Errors found:  {total_errors}")
    print(f"{'='*50}")

    sys.exit(1 if total_errors > 0 else 0)


if __name__ == "__main__":
    main()
