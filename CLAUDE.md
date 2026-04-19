# media-integrity-registry — Claude Session Context

> **Category:** database · **License:** CC BY 4.0 · **HIPAA:** none
>
> **Registry entry:** [meta/ecosystem.yaml#media-integrity-registry](https://github.com/JustinCreeden/jcpd/blob/main/meta/ecosystem.yaml)

---

## Role in ecosystem

Media provenance registry — tracks AI-generation metadata for curated clinical media assets.

See the full project page at [docs/projects/media-integrity-registry.md](https://github.com/JustinCreeden/jcpd/blob/main/docs/projects/media-integrity-registry.md).

## Current state

_Last refreshed: 2026-04-19 — run `jcpd scaffold media-integrity-registry --refresh` to update._

Active **public** repository. The registry is the only ecosystem daughter with `visibility: public` and a Creative Commons license.

**Layout:**

- `data/registry.json` — canonical media registry (JSON-LD)
- `data/schema.json` — JSON Schema for validation
- `data/entries/` — individual entry files
- `docs/` — DATA_DICTIONARY, ARCHIVAL_POLICY, CITATION_GUIDE, DOI_WORKFLOW, METADATA_STANDARDS
- `scripts/` — `validate_registry.py`, `generate_citation.py`, `generate_bibtex.py`, `download_media.sh`
- `templates/` — `new_entry_template.json`, `ISSUE_TEMPLATE.md`

**Standards:** FAIR Data Principles, DataCite v4.5, Dublin Core, Schema.org `VideoObject`, JSON-LD, BagIt (Library of Congress).

**Relationship to jcpd:** functionally independent — media entries may be referenced by `jcpd-emr`'s Media mode for therapeutic-content provenance, but the registry is consumable by any FAIR-aware tool.

**Constraints:** public visibility; no PHI; archived media files respect their original creator's license.

## Active work

No active work recorded. See [jcpd TODO.md](https://github.com/JustinCreeden/jcpd/blob/main/TODO.md) for queued ecosystem items, or this repo's own `STATUS.md` for its current version and blockers.

## Sync contract

None — this repo has no sync contract with `jcpd-emr` in `meta/ecosystem.yaml`.

## How to start a session

```bash
cd C:/Git/media-integrity-registry
git pull --rebase origin main
jcpd doctor media-integrity-registry
```

## How to end a session

1. Commit and push on a `session/<description>` branch, then open a PR via `gh pr create --fill`.
2. From the `jcpd` root: `jcpd sync --push` to propagate any ecosystem-level changes.
3. `jcpd drift` — reconcile if this session touched a plugin file (see **Sync contract** above).
4. Update this repo's `STATUS.md` — flip **Status**, bump **Last updated**, record the new **Current version**, triage **Open issues**.

## Links

- Master repo: https://github.com/JustinCreeden/jcpd
- This repo in registry: [meta/ecosystem.yaml#media-integrity-registry](https://github.com/JustinCreeden/jcpd/blob/main/meta/ecosystem.yaml)
- Handoff protocol: [docs/ecosystem/handoff-protocol.md](https://github.com/JustinCreeden/jcpd/blob/main/docs/ecosystem/handoff-protocol.md)
- Session-start protocol: [docs/operations/session-protocol.md](https://github.com/JustinCreeden/jcpd/blob/main/docs/operations/session-protocol.md)
