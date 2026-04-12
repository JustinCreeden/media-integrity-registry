# media-integrity-registry — Claude Session Context

**Author:** Justin Creeden, MD-PhD
**Copyright:** (c) 2026 Justin Creeden, MD-PhD
**License:** CC BY 4.0 (data) / MIT (code)

---

## What this repo is

A curated, citable database of audiovisual media with provenance tracking, AI-generation detection metadata, and Digital Object Identifiers (DOIs). Public repository.

## Contents

- `data/registry.json` — canonical media registry (JSON-LD)
- `data/schema.json` — JSON Schema for validation
- `data/entries/` — individual entry files
- `docs/` — DATA_DICTIONARY, ARCHIVAL_POLICY, CITATION_GUIDE, DOI_WORKFLOW, METADATA_STANDARDS
- `scripts/` — validate_registry.py, generate_citation.py, generate_bibtex.py, download_media.sh
- `templates/` — new_entry_template.json, ISSUE_TEMPLATE.md

## Standards compliance

FAIR Data Principles, DataCite v4.5, Dublin Core, Schema.org VideoObject, JSON-LD, BagIt (Library of Congress).

## Relationship to jcpd

Part of the Creeden ecosystem but functionally independent. Media entries may be referenced by jcpd's Media mode for therapeutic content provenance tracking.

## Constraints

- **Public repo.** All content must be appropriate for public visibility.
- **No PHI.** Media metadata only — never include patient data.
- **License compliance.** Archived media files are subject to their original creator's license.

## Working directory

`C:\Git\media-integrity-registry\`
