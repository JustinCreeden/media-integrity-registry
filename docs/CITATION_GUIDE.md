# Citation Guide

> How to cite media from the Media Integrity Registry in academic and professional contexts.

---

## Citing a Registry Entry

### APA 7th Edition (Recommended)

For YouTube videos, APA 7th edition format is:

```
Creator Last Name, First Initial. [Channel Name]. (Year, Month Day). Title of video [Video]. Platform. URL
```

**Example (Jenny Nicholson entry, MIR-0013):**

```
Nicholson, J. [Jenny Nicholson]. (2026, March 21). My favorite Twilight knockoff [Video]. YouTube. https://www.youtube.com/watch?v=VIDEO_ID
```

If a DOI has been minted via Zenodo, append it:

```
Nicholson, J. [Jenny Nicholson]. (2026, March 21). My favorite Twilight knockoff [Video]. YouTube. https://doi.org/10.5281/zenodo.XXXXXXXX
```

### MLA 9th Edition

```
Creator Last Name, First Name. "Title of Video." Platform, uploaded by Channel Name, Day Month Year, URL.
```

**Example:**

```
Nicholson, Jenny. "My Favorite Twilight Knockoff." YouTube, uploaded by Jenny Nicholson, 21 Mar. 2026, www.youtube.com/watch?v=VIDEO_ID.
```

### Chicago 17th Edition (Notes-Bibliography)

```
Creator First Name Last Name, "Title of Video," Platform, Month Day, Year, video, Duration, URL.
```

**Example:**

```
Jenny Nicholson, "My Favorite Twilight Knockoff," YouTube, March 21, 2026, video, https://www.youtube.com/watch?v=VIDEO_ID.
```

### BibTeX

```bibtex
@misc{nicholson2026twilightknockoff,
  author       = {Nicholson, Jenny},
  title        = {My Favorite Twilight Knockoff},
  year         = {2026},
  month        = mar,
  day          = {21},
  howpublished = {YouTube},
  url          = {https://www.youtube.com/watch?v=VIDEO_ID},
  note         = {Video essay. Accessed 2026-03-22.}
}
```

If a DOI exists:

```bibtex
@misc{nicholson2026twilightknockoff,
  author       = {Nicholson, Jenny},
  title        = {My Favorite Twilight Knockoff},
  year         = {2026},
  month        = mar,
  day          = {21},
  doi          = {10.5281/zenodo.XXXXXXXX},
  howpublished = {YouTube},
  url          = {https://www.youtube.com/watch?v=VIDEO_ID},
  note         = {Video essay}
}
```

---

## Citing the Registry Itself

If you reference the Media Integrity Registry as a dataset or methodology:

### APA 7th

```
Media Integrity Registry Contributors. (2026). Media Integrity Registry: A citable database of audiovisual media with provenance tracking (Version 0.1.0) [Data set]. Zenodo. https://doi.org/10.5281/zenodo.XXXXXXX
```

### BibTeX

```bibtex
@misc{mir2026,
  author       = {{Media Integrity Registry Contributors}},
  title        = {Media Integrity Registry: A Citable Database of Audiovisual Media with Provenance Tracking},
  year         = {2026},
  version      = {0.1.0},
  publisher    = {Zenodo},
  doi          = {10.5281/zenodo.XXXXXXX}
}
```

---

## Best Practices

1. **Always prefer DOIs over bare URLs.** DOIs are persistent; URLs can break.
2. **Include access dates** for web-hosted media, since content can be edited or removed.
3. **Use the MIR identifier** (e.g., `MIR-0013`) in addition to the DOI when referencing entries within this project's ecosystem.
4. **When citing archived copies**, note that the archived version may differ from the live version if the creator has edited the original.
5. **For video essays and longform content**, consider including a timestamp if you are referencing a specific segment: `Nicholson (2026, 1:23:45)`.
