# media-integrity-registry — Claude Session Context

> **Category:** database · **License:** CC BY 4.0 · **HIPAA:** none
>
> **Registry entry:** [meta/ecosystem.yaml#media-integrity-registry](https://github.com/Creeden-Enterprise/jcpd/blob/main/meta/ecosystem.yaml)

---

## Role in ecosystem

Media provenance registry — tracks AI-generation metadata for curated clinical media assets.

See the full project page at [docs/projects/media-integrity-registry.md](https://github.com/Creeden-Enterprise/jcpd/blob/main/docs/projects/media-integrity-registry.md).

## Current state

_Last refreshed: 2026-06-09 — run `jcpd scaffold media-integrity-registry --refresh` to update._

<!-- preserve:start current_state -->
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
<!-- preserve:end current_state -->

## Active work

<!-- preserve:start active_work -->
No active work recorded — check this repo's open GitHub Issues and the Creeden Work Board.
<!-- preserve:end active_work -->

## Sync contract

None — this repo has no sync contract in `meta/ecosystem.yaml`.

## How to start a session

```bash
cd C:/Users/justi/code/active/media-integrity-registry
git pull --rebase origin main
jcpd doctor media-integrity-registry
```

## How to end a session

1. Commit and push on a `session/<description>` branch, then open a PR via `gh pr create --fill`.
2. From the `jcpd` root: `jcpd sync --push` to propagate any ecosystem-level changes.
3. `jcpd drift` — reconcile if this session touched a plugin file (see **Sync contract** above).
4. Update this repo's `STATUS.md` — flip **Status**, bump **Last updated**, triage **Open issues**.

## Skills and rules

If this repo defines `.claude/skills/<name>/SKILL.md` files, the `name:` frontmatter values must not collide with any other active daughter's skills — the launcher's `--add-dir` set means peer-project skills load alongside this repo's, and `Skill()` resolves by first match in load order. See the canonical [skill-resolution rule](https://github.com/Creeden-Enterprise/jcpd/blob/main/.claude/rules/skill-resolution.md) at the hub. `jcpd doctor` enforces uniqueness across the ecosystem.

**Operator hierarchy (per [ADR 0035](https://github.com/Creeden-Enterprise/jcpd/blob/main/docs/adr/0035-multi-operator-topology-j-a-b-c-o.md)):** the ecosystem operates with five operator codes — `Operator J` (Justin, owner), `Operator A` (Claude Code, senior dev), `Operator B` (Codex, junior dev), `Operator C` (TBD competitor agent, reserved), `Operator O` (TBD gold-standard advisor, reserved). When authoring records, handoffs, ops-record PRs, or issues from this repo, use these codes. Cross-operator contract: [`docs/operations/operator-protocol.md`](https://github.com/Creeden-Enterprise/jcpd/blob/main/docs/operations/operator-protocol.md) at the hub.

## Links

- Master repo: https://github.com/Creeden-Enterprise/jcpd
- This repo in registry: [meta/ecosystem.yaml#media-integrity-registry](https://github.com/Creeden-Enterprise/jcpd/blob/main/meta/ecosystem.yaml)
- Handoff protocol: [docs/ecosystem/handoff-protocol.md](https://github.com/Creeden-Enterprise/jcpd/blob/main/docs/ecosystem/handoff-protocol.md)
- Session-start protocol: [docs/operations/session-protocol.md](https://github.com/Creeden-Enterprise/jcpd/blob/main/docs/operations/session-protocol.md)
- Skill resolution rule: [.claude/rules/skill-resolution.md](https://github.com/Creeden-Enterprise/jcpd/blob/main/.claude/rules/skill-resolution.md)
- Gold-standard success criterion rule: [.claude/rules/gold-standard-criterion.md](https://github.com/Creeden-Enterprise/jcpd/blob/main/.claude/rules/gold-standard-criterion.md) — success criterion for evaluating options must itself be gold-standard best practice, never "least surprise" or other convenience proxies

> Conventions: your user-global agent config (`AGENTS.md`). Todos/bugs → a labeled GitHub Issue. Cross-repo view → the Creeden Work Board.
