# Data Dictionary

> Complete field reference for Media Integrity Registry entries.

This document defines every field in the MIR schema. Fields marked **Required** must be present in every entry. Fields marked **Recommended** should be included whenever the information is available.

---

## Top-Level Fields

### `@context`
- **Type**: string
- **Required**: Yes
- **Description**: JSON-LD context URL. Always `"https://schema.org"`.

### `@type`
- **Type**: string
- **Required**: Yes
- **Description**: Schema.org type. Always `"VideoObject"` for video entries (use `"AudioObject"`, `"ImageObject"` as appropriate).

### `@id`
- **Type**: URI string
- **Required**: Yes
- **Description**: Unique identifier in the MIR namespace. Format: `mir:XXXX` where XXXX is a zero-padded integer.
- **Example**: `"mir:0013"`

### `doi`
- **Type**: string or null
- **Required**: Recommended
- **Description**: Digital Object Identifier. If the media has a registered DOI, use it. If you plan to mint one via Zenodo, set to `null` and document status in `archival.doiStatus`. For YouTube videos without native DOIs, archive to Zenodo to mint one.
- **Example**: `"10.5281/zenodo.12345678"`

### `title`
- **Type**: string
- **Required**: Yes
- **Description**: Exact title as published by the creator. Do not editorialize or add subtitles unless the creator included them.
- **Example**: `"My Favorite Twilight Knockoff"`

### `alternateTitle`
- **Type**: string or null
- **Required**: No
- **Description**: Alternate or working title, if known.

---

## Creator Object

### `creator.name`
- **Type**: string
- **Required**: Yes
- **Description**: Full name or established pseudonym of the primary creator.
- **Example**: `"Jenny Nicholson"`

### `creator.url`
- **Type**: URL string
- **Required**: Recommended
- **Description**: Link to the creator's primary profile or website.

### `creator.orcid`
- **Type**: string or null
- **Required**: No
- **Description**: ORCID identifier, if the creator has one. Format: `"0000-0000-0000-0000"`.

### `creator.role`
- **Type**: string
- **Required**: No
- **Description**: Creator's role (e.g., `"director"`, `"video essayist"`, `"researcher"`).

---

## Publication Metadata

### `datePublished`
- **Type**: ISO 8601 date string
- **Required**: Yes
- **Description**: Date the media was first publicly published.
- **Example**: `"2026-03-21"`

### `dateAccessed`
- **Type**: ISO 8601 date string
- **Required**: Recommended
- **Description**: Date the entry metadata was collected/verified.

### `language`
- **Type**: BCP 47 language tag
- **Required**: Recommended
- **Description**: Primary language of the media.
- **Example**: `"en"`

---

## Platform Object

### `platform.name`
- **Type**: string
- **Required**: Yes
- **Description**: Name of the hosting platform.
- **Example**: `"YouTube"`

### `platform.url`
- **Type**: URL string
- **Required**: Yes
- **Description**: Direct URL to the media on the original platform.

### `platform.channelName`
- **Type**: string
- **Required**: Recommended
- **Description**: Channel, account, or profile name on the platform.

### `platform.channelUrl`
- **Type**: URL string
- **Required**: Recommended
- **Description**: URL to the creator's channel/profile on the platform.

---

## Media Properties

### `mediaType`
- **Type**: enum string
- **Required**: Yes
- **Values**: `"video"`, `"audio"`, `"image"`, `"interactive"`

### `duration`
- **Type**: ISO 8601 duration string
- **Required**: Required for video/audio
- **Description**: Total runtime.
- **Example**: `"PT1H45M"` (1 hour 45 minutes)

### `resolution`
- **Type**: string
- **Required**: Recommended for video/image
- **Example**: `"1080p"`, `"4K"`, `"720p"`

### `encodingFormat`
- **Type**: MIME type string
- **Required**: Recommended
- **Example**: `"video/mp4"`, `"video/webm"`

---

## AI Transparency Fields

### `aiGenerated`
- **Type**: enum string
- **Required**: Yes
- **Values**: `"none"`, `"partial"`, `"full"`
- **Description**: Classification of AI involvement in content creation. See CONTRIBUTING.md for classification guidelines.

### `aiDisclosure.tools`
- **Type**: array of strings
- **Required**: Required if `aiGenerated` is not `"none"`
- **Description**: List of AI tools/models used.

### `aiDisclosure.methodology`
- **Type**: string
- **Required**: Recommended
- **Description**: How AI tools were used (e.g., `"Background music generated via Suno AI"`, `"Thumbnail created with Midjourney"`).

### `aiDisclosure.notes`
- **Type**: string
- **Required**: No
- **Description**: Free-text notes on AI involvement assessment.

---

## Archival Object

### `archival.localCopy`
- **Type**: boolean
- **Required**: Yes
- **Description**: Whether a local archival copy exists.

### `archival.localPath`
- **Type**: string or null
- **Required**: Required if `localCopy` is true
- **Description**: Relative path to the archived file within the archive storage.

### `archival.checksum`
- **Type**: object or null
- **Required**: Recommended
- **Description**: Integrity hash. Contains `algorithm` (e.g., `"SHA-256"`) and `value`.

### `archival.archiveDate`
- **Type**: ISO 8601 date string
- **Required**: Required if `localCopy` is true
- **Description**: Date the local copy was created.

### `archival.doiStatus`
- **Type**: enum string
- **Required**: Recommended
- **Values**: `"registered"`, `"pending"`, `"not_applicable"`
- **Description**: Status of DOI minting for this entry.

### `archival.zenodoRecord`
- **Type**: URL string or null
- **Required**: No
- **Description**: Link to the Zenodo deposit record, if applicable.

---

## Citation Object

### `citation.apa`
- **Type**: string
- **Required**: Recommended
- **Description**: Pre-formatted APA 7th edition citation.

### `citation.mla`
- **Type**: string
- **Required**: No
- **Description**: Pre-formatted MLA 9th edition citation.

### `citation.chicago`
- **Type**: string
- **Required**: No
- **Description**: Pre-formatted Chicago 17th edition citation.

### `citation.bibtex`
- **Type**: string
- **Required**: Recommended
- **Description**: BibTeX entry for LaTeX users.

---

## Classification & Discovery

### `tags`
- **Type**: array of strings
- **Required**: Recommended (minimum 3)
- **Description**: Subject keywords for discovery. Use lowercase, no special characters.

### `description`
- **Type**: string
- **Required**: Recommended
- **Description**: Brief, neutral summary of the media content (2-3 sentences). Written by the cataloger, not copied from the creator's description.

### `genre`
- **Type**: string or array
- **Required**: No
- **Description**: Genre classification (e.g., `"video essay"`, `"documentary"`, `"music video"`).
