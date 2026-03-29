# Changelog

All notable changes to the Media Integrity Registry are documented here.

Format follows [Keep a Changelog](https://keepachangelog.com/en/1.1.0/).
Versioning follows [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

---

## [0.1.0] — 2026-03-22

### Added
- Initial repository structure and documentation
- JSON-LD schema with Schema.org, Dublin Core, and DataCite mappings
- JSON Schema for entry validation (`data/schema.json`)
- Entry MIR-0013: Jenny Nicholson — "My Favorite Twilight Knockoff" (2026)
- Archival download script (`scripts/download_media.sh`) using yt-dlp
- Citation generator (`scripts/generate_citation.py`) — APA, MLA, Chicago, BibTeX
- BibTeX export (`scripts/generate_bibtex.py`)
- Schema validator (`scripts/validate_registry.py`)
- Documentation suite:
  - `DATA_DICTIONARY.md` — Complete field reference
  - `ARCHIVAL_POLICY.md` — Local preservation guidelines
  - `CITATION_GUIDE.md` — How to cite entries and the registry
  - `DOI_WORKFLOW.md` — Minting DOIs via Zenodo
  - `METADATA_STANDARDS.md` — Crosswalk to Dublin Core, DataCite, Schema.org, PREMIS
- `CITATION.cff` for repository-level citation
- GitHub Actions CI for automated schema validation
- New entry template and issue template
- CC BY 4.0 license (data) + MIT license (code)
- Contributor Covenant Code of Conduct
