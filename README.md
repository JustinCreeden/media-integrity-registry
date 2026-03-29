# Media Integrity Registry (MIR)

**Author:** Justin Creeden, MD-PhD
**Copyright:** (c) 2026 Justin Creeden, MD-PhD
**License:** CC BY 4.0 (data) / MIT (code)

> A curated, citable database of audiovisual media with provenance tracking, AI-generation detection metadata, and Digital Object Identifiers (DOIs).

[![License: CC BY 4.0](https://img.shields.io/badge/License-CC_BY_4.0-lightgrey.svg)](https://creativecommons.org/licenses/by/4.0/)
[![DOI](https://img.shields.io/badge/DOI-10.5281%2Fzenodo.XXXXXXX-blue)](https://doi.org/10.5281/zenodo.XXXXXXX)
[![Data Format: JSON-LD](https://img.shields.io/badge/Data_Format-JSON--LD-orange)]()

---

## Overview

The **Media Integrity Registry** is an open, standards-compliant database designed to catalog audiovisual media with a focus on:

- **Provenance tracking** — Who created it, when, where, and how?
- **AI-generation transparency** — Is the media synthetically generated, partially AI-assisted, or entirely camera-captured?
- **Citability** — Every entry carries a DOI (or instructions to mint one) and machine-readable citation metadata.
- **Local archival** — Best-practice workflows for downloading and preserving local copies of web-hosted media to guard against link rot.

This project follows the [FAIR Data Principles](https://www.go-fair.org/fair-principles/) (Findable, Accessible, Interoperable, Reusable) and uses vocabulary from [Schema.org](https://schema.org/), [Dublin Core](https://www.dublincore.org/), and the [DataCite Metadata Schema](https://schema.datacite.org/).

---

## Repository Structure

```
media-integrity-registry/
├── README.md                  # This file
├── LICENSE                    # CC BY 4.0
├── CITATION.cff               # Citation File Format for this repository
├── CONTRIBUTING.md             # Contribution guidelines
├── CODE_OF_CONDUCT.md          # Contributor covenant
├── CHANGELOG.md                # Version history
├── data/
│   ├── registry.json           # The canonical media registry (JSON-LD)
│   ├── schema.json             # JSON Schema for validation
│   └── entries/                # Individual entry files (one per media item)
│       └── mir-0013.json       # Example: Jenny Nicholson entry
├── docs/
│   ├── DATA_DICTIONARY.md      # Field-by-field documentation
│   ├── ARCHIVAL_POLICY.md      # Local archival & preservation policy
│   ├── CITATION_GUIDE.md       # How to cite entries & the registry itself
│   ├── DOI_WORKFLOW.md         # How to mint DOIs via Zenodo
│   └── METADATA_STANDARDS.md   # Mapping to Dublin Core, DataCite, Schema.org
├── scripts/
│   ├── download_media.sh       # yt-dlp wrapper for archival downloads
│   ├── validate_registry.py    # JSON Schema validator
│   ├── generate_bibtex.py      # Export BibTeX from registry entries
│   └── generate_citation.py    # Export APA/MLA/Chicago citations
├── templates/
│   ├── new_entry_template.json # Blank entry template
│   └── ISSUE_TEMPLATE.md       # GitHub issue template for new submissions
└── .github/
    └── workflows/
        └── validate.yml        # CI: auto-validate registry on PR
```

---

## Quick Start

### 1. Clone the Repository

```bash
git clone https://github.com/JustinCreeden/media-integrity-registry.git
cd media-integrity-registry
```

### 2. Browse the Registry

The canonical data lives in `data/registry.json`. Each entry follows the schema defined in `data/schema.json`.

### 3. Add a New Entry

```bash
cp templates/new_entry_template.json data/entries/mir-XXXX.json
# Edit the file with your media metadata
python scripts/validate_registry.py data/entries/mir-XXXX.json
```

### 4. Archive Media Locally

```bash
# Requires yt-dlp (https://github.com/yt-dlp/yt-dlp)
bash scripts/download_media.sh "https://www.youtube.com/watch?v=VIDEO_ID" ./archive/
```

### 5. Generate Citations

```bash
python scripts/generate_citation.py data/entries/mir-0013.json --format apa
python scripts/generate_bibtex.py data/entries/mir-0013.json
```

---

## Data Model (Summary)

Each registry entry contains:

| Field | Type | Description |
|---|---|---|
| `@id` | URI | Unique identifier (MIR namespace) |
| `doi` | string | Digital Object Identifier (minted or pending) |
| `title` | string | Title of the media |
| `creator` | object | Author/creator with ORCID if available |
| `datePublished` | ISO 8601 | Publication date |
| `platform` | object | Hosting platform and original URL |
| `mediaType` | enum | `video`, `audio`, `image`, `interactive` |
| `duration` | ISO 8601 | Duration (e.g., `PT2H15M`) |
| `aiGenerated` | enum | `none`, `partial`, `full` |
| `aiDisclosure` | object | Details on AI tools used, if any |
| `license` | string | Content license (SPDX identifier or URL) |
| `archival` | object | Local copy status, checksums, storage path |
| `citation` | object | Pre-formatted APA, MLA, Chicago, BibTeX |
| `tags` | array | Subject keywords |
| `resolution` | string | e.g., `1080p`, `4K` |

See [docs/DATA_DICTIONARY.md](docs/DATA_DICTIONARY.md) for the complete field reference.

---

## Citing This Registry

### The Repository Itself

```bibtex
@misc{media_integrity_registry_2026,
  author       = {Creeden, Justin},
  title        = {Media Integrity Registry: A Citable Database of Audiovisual Media with Provenance Tracking},
  year         = {2026},
  publisher    = {Zenodo},
  doi          = {10.5281/zenodo.XXXXXXX},
  url          = {https://github.com/JustinCreeden/media-integrity-registry}
}
```

### An Individual Entry

See [docs/CITATION_GUIDE.md](docs/CITATION_GUIDE.md) for per-entry citation formats.

---

## Standards Compliance

This project aligns with:

- **FAIR Data Principles** — Findable, Accessible, Interoperable, Reusable
- **DataCite Metadata Schema v4.5** — For DOI registration
- **Dublin Core Metadata Element Set** — Cross-compatibility
- **Schema.org VideoObject** — Structured data for search engines
- **JSON-LD** — Linked data serialization
- **OAIS Reference Model** — Archival framework
- **BagIt (Library of Congress)** — File packaging for preservation

---

## Legal & Ethical Considerations

- **Copyright**: Downloading and archiving media must comply with the creator's license and applicable copyright law. This project provides *tooling* for lawful archival (e.g., personal backup, research use under fair use/fair dealing). Users are responsible for ensuring compliance with their jurisdiction's laws.
- **AI Transparency**: The `aiGenerated` field is a good-faith assessment. Contributors should document their methodology in the `aiDisclosure` object.
- **Privacy**: Do not include personally identifiable information beyond what the creator has made publicly available.

---

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines on submitting new entries, proposing schema changes, and reporting issues.

---

## License

- **Registry data**: [Creative Commons Attribution 4.0 International (CC BY 4.0)](https://creativecommons.org/licenses/by/4.0/)
- **Code/scripts**: [MIT License](https://opensource.org/licenses/MIT)
- **Archived media files**: Subject to their original creator's license — see each entry's `license` field.
