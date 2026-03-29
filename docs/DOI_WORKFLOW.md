# DOI Workflow: Minting DOIs for Media Entries

> How to assign persistent, citable Digital Object Identifiers to media that doesn't natively have one.

---

## Background

Most YouTube videos, social media posts, and web-native media do not have Digital Object Identifiers (DOIs). DOIs are the gold standard for persistent, resolvable identifiers in academic contexts. This document describes the workflow for minting DOIs using **Zenodo**, a free, open repository operated by CERN.

---

## When to Mint a DOI

| Scenario | Action |
|---|---|
| Media already has a DOI (e.g., published in a journal) | Use the existing DOI |
| Media is on a stable platform (YouTube, Vimeo) but has no DOI | Archive to Zenodo and mint a DOI |
| Media is at risk of disappearing (personal site, small platform) | **Priority**: Archive and mint immediately |
| Media is a live stream or ephemeral | Archive first, then mint |

---

## Step-by-Step: Minting via Zenodo

### Prerequisites

- A [Zenodo account](https://zenodo.org/) (free, supports GitHub login)
- The media file (downloaded locally) — see `scripts/download_media.sh`
- Complete metadata for the entry

### 1. Download the Media

```bash
bash scripts/download_media.sh "https://www.youtube.com/watch?v=VIDEO_ID" ./archive/
```

This creates:
- The video file (highest quality available)
- A `.info.json` metadata sidecar
- Subtitles (if available)
- A thumbnail image

### 2. Create a Zenodo Deposit

1. Go to [zenodo.org/deposit/new](https://zenodo.org/deposit/new)
2. Upload the following files:
   - The video file (or a metadata-only record if the file is too large or copyright-restricted)
   - The `.info.json` sidecar
   - A `README.txt` explaining the archival context
3. Fill in the metadata form:

| Zenodo Field | MIR Mapping |
|---|---|
| Title | `title` |
| Authors | `creator.name` |
| Description | `description` + link to original |
| Publication date | `datePublished` |
| Resource type | Video/Audio |
| License | `license` (usually "Other" for copyrighted content) |
| Keywords | `tags` |
| Related identifiers | Original URL (relation: "is supplement to") |

### 3. Reserve a DOI

Before publishing, Zenodo lets you **reserve a DOI** without making the record public. This is useful if:
- You need the DOI for the MIR entry before finalizing the Zenodo record
- The media is under copyright and you want a metadata-only record

Click **"Reserve DOI"** on the deposit page.

### 4. Publish and Record

After publishing:
1. Copy the assigned DOI (format: `10.5281/zenodo.XXXXXXXX`)
2. Update the MIR entry's `doi` field
3. Set `archival.doiStatus` to `"registered"`
4. Set `archival.zenodoRecord` to the Zenodo URL

---

## Metadata-Only Records

For copyrighted media where uploading the full file may not be appropriate, Zenodo supports **metadata-only deposits**. This still mints a valid DOI that resolves to a landing page with:

- Full bibliographic metadata
- A link to the original source
- Archival context and preservation notes

This approach is recommended for most YouTube videos, as it provides a persistent identifier without redistributing copyrighted content.

---

## DOI for the Registry Itself

The MIR repository as a whole should also have a DOI. Use the [Zenodo–GitHub integration](https://docs.github.com/en/repositories/archiving-a-github-repository/referencing-and-citing-content) to automatically mint a new DOI for each tagged release.

1. Connect your GitHub repository to Zenodo
2. Create a GitHub Release (e.g., `v0.1.0`)
3. Zenodo automatically archives and mints a DOI
4. Update `CITATION.cff` with the new DOI

---

## Alternative DOI Providers

| Provider | Cost | Use Case |
|---|---|---|
| **Zenodo** (CERN) | Free | Best for individual researchers and small projects |
| **Figshare** | Free tier | Good for datasets and media files |
| **DataCite** | Institutional | For organizations with a DataCite membership |
| **Crossref** | Publisher | For formal publications |

For this project, Zenodo is recommended as the default.
