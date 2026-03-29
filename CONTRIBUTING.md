# Contributing to the Media Integrity Registry

Thank you for your interest in contributing to the Media Integrity Registry (MIR). This document outlines the process for adding new entries, proposing changes, and maintaining data quality.

---

## Types of Contributions

### 1. Adding a New Media Entry

This is the most common contribution. To add a new entry:

1. **Fork** this repository.
2. **Copy** the template: `cp templates/new_entry_template.json data/entries/mir-XXXX.json` (replace `XXXX` with the next available ID).
3. **Fill in** all required fields. See [docs/DATA_DICTIONARY.md](docs/DATA_DICTIONARY.md) for field definitions.
4. **Validate** your entry: `python scripts/validate_registry.py data/entries/mir-XXXX.json`
5. **Submit** a pull request with:
   - A descriptive title (e.g., "Add MIR-0014: [Media Title]")
   - A brief description of the media and why it belongs in the registry
   - Confirmation that you have verified the metadata accuracy

### 2. Correcting Existing Entries

If you find an error in an existing entry (wrong date, broken URL, incorrect AI classification):

1. Open an **Issue** describing the error with evidence.
2. Or submit a **Pull Request** with the correction and a note explaining the change.

### 3. Schema Changes

Proposals to modify the data schema should:

1. Open a **Discussion** (not an Issue) explaining the rationale.
2. Include examples showing how existing entries would be affected.
3. Reference relevant metadata standards (Dublin Core, DataCite, Schema.org).

### 4. Script/Tooling Improvements

Bug fixes and enhancements to scripts in `scripts/` follow standard PR workflow. Please include tests where applicable.

---

## Entry Quality Standards

Every entry **must** include:

- `title` — Exact title as published by the creator
- `creator.name` — Full name of the primary creator
- `datePublished` — ISO 8601 date, verified against the platform
- `platform.url` — Direct URL to the media on its original platform
- `mediaType` — One of: `video`, `audio`, `image`, `interactive`
- `aiGenerated` — One of: `none`, `partial`, `full`

Every entry **should** include (strongly recommended):

- `doi` — A minted DOI, or `"pending"` with a note in `archival.doiStatus`
- `duration` — ISO 8601 duration for time-based media
- `creator.url` — Link to the creator's profile or website
- `tags` — At least 3 subject keywords
- `citation.apa` — Pre-formatted APA 7th edition citation string

---

## AI Classification Guidelines

The `aiGenerated` field requires careful assessment:

| Value | Definition | Examples |
|---|---|---|
| `none` | No AI tools used in content creation | Traditional filmmaking, screen recording, live performance |
| `partial` | AI tools assisted but human creativity dominates | AI-assisted editing, AI background music, AI thumbnails |
| `full` | Content is primarily or entirely AI-generated | Sora/Runway-generated video, AI voice synthesis, deepfakes |

When in doubt, classify as `partial` and document your reasoning in `aiDisclosure.notes`.

---

## Archival Best Practices

When archiving media locally:

1. **Always respect copyright.** Only archive media you have legal right to preserve.
2. **Use checksums.** Generate SHA-256 hashes for all archived files.
3. **Preserve original metadata.** Use `yt-dlp --write-info-json` to capture platform metadata.
4. **Document the archive date.** Record when the local copy was made.
5. **Store in BagIt format** when possible for institutional preservation.

---

## Code of Conduct

All contributors are expected to follow our [Code of Conduct](CODE_OF_CONDUCT.md). Be respectful, constructive, and collaborative.

---

## Questions?

Open a Discussion or Issue. We're happy to help.
