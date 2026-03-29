# Archival Policy

> Guidelines for downloading, storing, and preserving local copies of registry media.

---

## Rationale

Web-hosted media is ephemeral. Videos are removed, platforms shut down, and URLs break. The Media Integrity Registry maintains local archival copies to ensure long-term access to cataloged media for research and reference purposes.

---

## Legal Framework

Local archival must comply with applicable copyright law. Common lawful bases include:

- **Personal backup / fair use (U.S.)**: Section 107 of the U.S. Copyright Act permits limited use for purposes such as criticism, comment, scholarship, and research.
- **Fair dealing (UK, Canada, Australia)**: Similar provisions exist for research and private study.
- **Platform Terms of Service**: Be aware that some platforms prohibit downloading in their ToS, even where copyright law might permit it. This is a contractual matter, not a copyright matter.
- **Creator license**: Some creators publish under Creative Commons or other open licenses that explicitly permit archival.

**This project does not distribute archived media files.** Local copies are stored on private infrastructure and are not made publicly available through this repository. The repository contains only metadata.

---

## Download Procedure

### Tool: yt-dlp

We use [yt-dlp](https://github.com/yt-dlp/yt-dlp), the community-maintained fork of youtube-dl, for downloading media from supported platforms.

```bash
# Install
pip install yt-dlp

# Basic archival download (best quality + metadata)
bash scripts/download_media.sh "URL" ./archive/
```

### What Gets Archived

For each media item, the archival download captures:

| File | Purpose |
|---|---|
| Video/audio file | Primary media (best available quality) |
| `.info.json` | Platform metadata (title, description, upload date, view count, etc.) |
| `.description` | Creator's description text |
| Subtitles (`.en.vtt`, etc.) | Closed captions / subtitles if available |
| Thumbnail (`.jpg`/`.webp`) | Cover image |

### File Naming Convention

```
MIR-{id}_{sanitized-title}_{date}.{ext}
```

Example: `MIR-0013_my-favorite-twilight-knockoff_2026-03-21.mp4`

---

## Storage Architecture

### Recommended Layout

```
archive/
├── MIR-0013/
│   ├── MIR-0013_my-favorite-twilight-knockoff_2026-03-21.mp4
│   ├── MIR-0013_my-favorite-twilight-knockoff_2026-03-21.info.json
│   ├── MIR-0013_my-favorite-twilight-knockoff_2026-03-21.description
│   ├── MIR-0013_my-favorite-twilight-knockoff_2026-03-21.en.vtt
│   ├── MIR-0013_my-favorite-twilight-knockoff_2026-03-21.jpg
│   ├── checksum.sha256
│   └── README.txt
```

### Checksums

Generate SHA-256 checksums for all archived files:

```bash
sha256sum MIR-0013/* > MIR-0013/checksum.sha256
```

Store the checksum value in the registry entry's `archival.checksum` field.

### Storage Requirements

- **Primary storage**: Local server, NAS, or institutional repository
- **Backup**: At least one geographically separated backup
- **Format**: Prefer open formats (MP4/H.264, WebM/VP9, FLAC for audio)
- **Minimum retention**: Indefinite (as long as the registry entry exists)

---

## Integrity Checks

Run periodic integrity checks to detect bit rot:

```bash
# Verify all checksums
cd archive/
for dir in MIR-*/; do
  cd "$dir"
  sha256sum -c checksum.sha256
  cd ..
done
```

---

## BagIt Packaging (Optional, Recommended for Institutional Use)

For institutional preservation, package archived media using the [BagIt specification](https://tools.ietf.org/html/rfc8493) (Library of Congress):

```bash
pip install bagit
bagit.py --contact-name "MIR Project" archive/MIR-0013/
```

This adds manifest files and tag metadata for long-term preservation workflows compatible with institutional repositories (DSpace, Fedora, Archivematica).

---

## Deletion Policy

Archived media should only be removed if:

1. The creator issues a legally valid takedown request.
2. A court order requires removal.
3. The entry is determined to be a duplicate of another entry.

All deletions must be logged in `CHANGELOG.md`.
