# Metadata Standards Mapping

> How MIR fields map to established metadata vocabularies.

---

## Overview

The Media Integrity Registry uses a custom schema designed for audiovisual media with AI-transparency metadata. To ensure interoperability with existing systems, every field maps to one or more established standards.

---

## Schema.org Mapping (Primary)

MIR entries use JSON-LD with `@context: "https://schema.org"`. The primary type is `VideoObject`.

| MIR Field | Schema.org Property | Notes |
|---|---|---|
| `title` | `name` | |
| `description` | `description` | |
| `creator.name` | `author.name` | |
| `creator.url` | `author.url` | |
| `datePublished` | `datePublished` | ISO 8601 |
| `duration` | `duration` | ISO 8601 duration |
| `platform.url` | `contentUrl` or `url` | |
| `platform.name` | `publisher.name` | |
| `resolution` | `videoQuality` | |
| `encodingFormat` | `encodingFormat` | MIME type |
| `tags` | `keywords` | Comma-separated or array |
| `license` | `license` | URL or SPDX identifier |
| `genre` | `genre` | |
| `language` | `inLanguage` | BCP 47 |

---

## Dublin Core Mapping

For cross-compatibility with library systems and institutional repositories.

| MIR Field | Dublin Core Element | Dublin Core Term |
|---|---|---|
| `title` | `dc:title` | `dcterms:title` |
| `creator.name` | `dc:creator` | `dcterms:creator` |
| `description` | `dc:description` | `dcterms:description` |
| `datePublished` | `dc:date` | `dcterms:issued` |
| `language` | `dc:language` | `dcterms:language` |
| `mediaType` | `dc:type` | `dcterms:type` (DCMI Type: `MovingImage`, `Sound`, `StillImage`) |
| `license` | `dc:rights` | `dcterms:license` |
| `doi` | `dc:identifier` | `dcterms:identifier` |
| `tags` | `dc:subject` | `dcterms:subject` |
| `encodingFormat` | `dc:format` | `dcterms:format` |

---

## DataCite Metadata Schema v4.5 Mapping

For DOI registration via Zenodo or other DataCite members.

| MIR Field | DataCite Property | DataCite ID |
|---|---|---|
| `doi` | `Identifier` | 1 |
| `creator.name` | `Creator` | 2 |
| `title` | `Title` | 3 |
| `platform.name` | `Publisher` | 4 |
| `datePublished` | `PublicationYear` | 5 |
| `mediaType` | `ResourceType` | 10 |
| `tags` | `Subject` | 6 |
| `description` | `Description` | 17 |
| `language` | `Language` | 9 |
| `license` | `Rights` | 16 |
| `platform.url` | `RelatedIdentifier` | 12 (relation: `IsSupplementTo`) |
| `creator.orcid` | `Creator.nameIdentifier` | 2.1 (scheme: ORCID) |

---

## Fields Without Standard Equivalents

The following MIR fields are domain-specific and do not have direct equivalents in the standards above:

| MIR Field | Notes |
|---|---|
| `aiGenerated` | Novel field. No existing standard vocabulary covers AI-generation classification for media. Proposed for Schema.org extension. |
| `aiDisclosure.*` | Novel field cluster. Modeled after the C2PA (Coalition for Content Provenance and Authenticity) manifest structure. |
| `archival.*` | Partially mapped to PREMIS (Preservation Metadata: Implementation Strategies). |
| `archival.checksum` | Maps to PREMIS `fixity` with `messageDigestAlgorithm` and `messageDigest`. |

---

## C2PA Alignment

The [Coalition for Content Provenance and Authenticity (C2PA)](https://c2pa.org/) defines a technical standard for content provenance. While MIR does not implement C2PA manifests directly, the `aiDisclosure` object is designed to be compatible:

| MIR Field | C2PA Concept |
|---|---|
| `aiGenerated` | `c2pa.training-mining` assertion |
| `aiDisclosure.tools` | `c2pa.actions` (softwareAgent) |
| `aiDisclosure.methodology` | `c2pa.actions` (description) |

Future versions of MIR may support embedding or referencing C2PA manifests directly.

---

## PREMIS Mapping (Archival Fields)

For digital preservation interoperability.

| MIR Field | PREMIS Semantic Unit |
|---|---|
| `archival.localCopy` | `storageStatus` |
| `archival.localPath` | `contentLocation` |
| `archival.checksum.algorithm` | `fixity.messageDigestAlgorithm` |
| `archival.checksum.value` | `fixity.messageDigest` |
| `archival.archiveDate` | `eventDateTime` (eventType: `ingestion`) |
