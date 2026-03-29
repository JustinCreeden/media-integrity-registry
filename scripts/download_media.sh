#!/usr/bin/env bash
# =============================================================================
# download_media.sh — Archival download wrapper for yt-dlp
# Part of the Media Integrity Registry (MIR)
# =============================================================================
#
# Usage:
#   bash download_media.sh <URL> <OUTPUT_DIR> [MIR_ID]
#
# Example:
#   bash download_media.sh "https://www.youtube.com/watch?v=VIDEO_ID" ./archive/ MIR-0013
#
# Prerequisites:
#   - yt-dlp (pip install yt-dlp)
#   - ffmpeg (for format merging)
#
# What this script does:
#   1. Downloads the best available video+audio quality
#   2. Saves platform metadata (.info.json)
#   3. Downloads subtitles (all available languages)
#   4. Downloads thumbnail
#   5. Saves the creator's description
#   6. Generates SHA-256 checksums
#   7. Creates a README.txt with archival context
# =============================================================================

set -euo pipefail

# --- Arguments ---------------------------------------------------------------
URL="${1:?Usage: download_media.sh <URL> <OUTPUT_DIR> [MIR_ID]}"
OUTPUT_DIR="${2:?Usage: download_media.sh <URL> <OUTPUT_DIR> [MIR_ID]}"
MIR_ID="${3:-UNASSIGNED}"

# --- Preflight checks --------------------------------------------------------
if ! command -v yt-dlp &> /dev/null; then
    echo "ERROR: yt-dlp is not installed."
    echo "Install it with: pip install yt-dlp"
    exit 1
fi

if ! command -v ffmpeg &> /dev/null; then
    echo "WARNING: ffmpeg is not installed. Some format merging may fail."
    echo "Install it with: sudo apt install ffmpeg (or brew install ffmpeg)"
fi

if ! command -v sha256sum &> /dev/null; then
    # macOS uses shasum
    SHA_CMD="shasum -a 256"
else
    SHA_CMD="sha256sum"
fi

# --- Setup -------------------------------------------------------------------
TIMESTAMP=$(date -u +"%Y-%m-%dT%H:%M:%SZ")
DATE_SHORT=$(date -u +"%Y-%m-%d")
ENTRY_DIR="${OUTPUT_DIR}/${MIR_ID}"

mkdir -p "${ENTRY_DIR}"

echo "============================================="
echo "  Media Integrity Registry — Archival Download"
echo "============================================="
echo "  URL:        ${URL}"
echo "  MIR ID:     ${MIR_ID}"
echo "  Output:     ${ENTRY_DIR}"
echo "  Timestamp:  ${TIMESTAMP}"
echo "============================================="
echo ""

# --- Download ----------------------------------------------------------------
echo "[1/4] Downloading media (best quality)..."
yt-dlp \
    --format "bestvideo[ext=mp4]+bestaudio[ext=m4a]/bestvideo+bestaudio/best" \
    --merge-output-format mp4 \
    --write-info-json \
    --write-description \
    --write-thumbnail \
    --write-subs \
    --write-auto-subs \
    --sub-langs "all" \
    --convert-subs vtt \
    --embed-metadata \
    --output "${ENTRY_DIR}/${MIR_ID}_%(title)s_${DATE_SHORT}.%(ext)s" \
    --no-overwrites \
    --restrict-filenames \
    "${URL}"

echo ""
echo "[2/4] Download complete. Files:"
ls -lh "${ENTRY_DIR}/"

# --- Checksums ---------------------------------------------------------------
echo ""
echo "[3/4] Generating SHA-256 checksums..."
cd "${ENTRY_DIR}"
${SHA_CMD} * > checksum.sha256 2>/dev/null || true
echo "Checksums written to ${ENTRY_DIR}/checksum.sha256"

# --- README ------------------------------------------------------------------
echo ""
echo "[4/4] Writing archival README..."
cat > README.txt << EOF
=============================================================================
MEDIA INTEGRITY REGISTRY — ARCHIVAL RECORD
=============================================================================

MIR Identifier:  ${MIR_ID}
Source URL:       ${URL}
Archive Date:    ${TIMESTAMP}
Archived By:     MIR download_media.sh script

This directory contains an archival copy of web-hosted media, preserved as
part of the Media Integrity Registry project. The archive includes the
primary media file, platform metadata, subtitles (if available), thumbnail,
and the creator's description.

PURPOSE:
This copy exists for research reference and long-term preservation in case
the original source becomes unavailable. It is not intended for
redistribution.

INTEGRITY:
File checksums are recorded in checksum.sha256. Verify with:
  sha256sum -c checksum.sha256

LEGAL:
This archival copy is made under applicable research/fair use provisions.
The original content remains the intellectual property of its creator.
See the registry entry for license details.
=============================================================================
EOF

echo ""
echo "============================================="
echo "  Archival download complete!"
echo "  Location: ${ENTRY_DIR}"
echo "============================================="
echo ""
echo "Next steps:"
echo "  1. Verify the download: sha256sum -c ${ENTRY_DIR}/checksum.sha256"
echo "  2. Update the registry entry with:"
echo "     - archival.localCopy: true"
echo "     - archival.localPath: ${ENTRY_DIR}"
echo "     - archival.archiveDate: ${DATE_SHORT}"
echo "     - archival.checksum (from checksum.sha256)"
echo "  3. Consider minting a DOI via Zenodo (see docs/DOI_WORKFLOW.md)"
