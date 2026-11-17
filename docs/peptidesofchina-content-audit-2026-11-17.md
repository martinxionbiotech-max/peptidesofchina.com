# peptidesofchina.com — Content Quality Audit

**Date:** 2026-11-17  
**Mode:** READ_ONLY — no content page changed  
**Repo:** `/root/.openclaw/workspace/repos/peptidesofchina.com`  
**HEAD:** `da9b74f`  
**Scope:** all 382 Markdown content files  
**Supersedes:** `docs/peptidesofchina-content-audit-report.md` (2026-11-05) for current content status

---

## 1. Conclusion summary

The current content set is materially better than the 2026-11-05 audit. The previous P0 product-template duplication is **not reproduced** in the current corpus: no 4-gram pair within products, blog, news or pages reaches 0.30 Jaccard, and product unique-sentence share has a minimum of 0.68.

The remaining weaknesses are **metadata and editorial completeness**, not mass duplication:

- 382 content files have **no author field and no date/updated field**.
- 127/127 products have an empty `category`; all 127 are `status: In Stock`.
- Blog: 96/195 have Sources; 70/195 have an Author's Take/Our Read block.
- News: 0/38 sources and 0/38 editorial viewpoint blocks.
- 53 blog titles and 21 blog descriptions exceed the frontmatter length targets.
- Live site has a **soft-404/catch-all behavior**: arbitrary unknown URLs return 200 with the homepage, not 404.

### Six-dimension summary

| Dimension | Result | Key numbers | Severity |
|---|---|---|---|
| Repetition | **PASS** | 0 pairs ≥0.30 in all collections; product unique-sentence min 0.68 | — |
| AI traces | **PARTIAL** | 189 AI-word hits across 102/195 blog pages; 29 across 26/127 products | P1 |
| Thin content | **PASS / P2** | Product 2,073–3,220 words; blog 496–4,488; news 131–648; pages 153–6,138 | P2 |
| No-value language | **PASS / P2** | Empty marketing phrases: blog 27 hits/23 pages; news 2/2; pages 1/1; products 0 | P2 |
| Subjective viewpoint | **PARTIAL** | Author's Take/Our Read: products 127/127, blog 70/195, pages 6/22, news 0/38 | P1 |
| Non-originality | **PARTIAL** | No source corpus; Sources: products 127/127, blog 96/195, news 0/38, pages 5/22 | P1/P2 |

---

## 2. Inventory

### Collection counts and length

| Collection | Files | Words min / mean / median / max | H2 min / mean / max |
|---|---:|---|---:|
| products | 127 | 2,073 / 2,577 / 2,608 / 3,220 | 9 / 10.1 / 14 |
| blog | 195 | 496 / 2,353 / 2,432 / 4,488 | 7 / 11.6 / 29 |
| news | 38 | 131 / 245 / 227 / 648 | 1 / 2.2 / 12 |
| pages | 22 | 153 / 1,827 / 523 / 6,138 | 2 / 8.6 / 18 |

**Total content files:** 382  
**Sitemap URLs:** 386 (382 content + 4 index/list/static routes; not all route mappings individually re-checked)

### Source / viewpoint coverage

| Collection | External links | Sources/References | Author's Take / Our Read |
|---|---:|---:|---:|
| products | 121 / 127 | 127 / 127 | 127 / 127 |
| blog | 172 / 195 | 96 / 195 | 70 / 195 |
| news | 7 / 38 | 0 / 38 | 0 / 38 |
| pages | 7 / 22 | 5 / 22 | 6 / 22 |

**Author/date metadata:** 0 / 382 files have an `author` field; 0 / 382 have a `date` or `updated` field in the frontmatter.

---

## 3. Six-dimension findings

### 3.1 Repetition — PASS

Method: 4-gram Jaccard within each collection, all pairs; unique-sentence word share per file.

| Collection | Pairs ≥0.90 | Pairs 0.70–0.90 | Pairs 0.50–0.70 | Pairs 0.30–0.50 |
|---|---:|---:|---:|---:|
| products | 0 | 0 | 0 | 0 |
| blog | 0 | 0 | 0 | 0 |
| news | 0 | 0 | 0 | 0 |
| pages | 0 | 0 | 0 | 0 |

Unique-sentence word share:

| Collection | Mean | Median | Min |
|---|---:|---:|---:|
| products | 0.82 | 0.83 | 0.68 |
| blog | 0.86 | 0.87 | 0.60 |
| news | 0.74 | 0.75 | 0.48 |
| pages | 0.84 | 0.84 | 0.64 |

**Finding:** The previous product-template P0 is no longer current. The current product pages are long and substantially unique. Repeated sentences that do occur are mostly citation/reference boilerplate (e.g. “National Center for Biotechnology Information”), not shared product-body paragraphs.

**Lowest product pages:** `products/p/prostamax.md`, `products/o/ovagen.md`, `products/p/ptd-dbm.md` (0.68 unique-sentence share). These are the first candidates for a manual read, not automatic rewriting.

### 3.2 AI traces — PARTIAL / P1

Mechanical phrase counts:

| Collection | Hits | Pages with a hit |
|---|---:|---:|
| products | 29 | 26 / 127 |
| blog | 189 | 102 / 195 |
| news | 9 | 8 / 38 |
| pages | 12 | 6 / 22 |

Most affected collection: **blog**. The terms include `robust`, `leverage`, `elevate`, `not only`, `crucial`, `furthermore` and `whether you are`.

**Judgment:** This is not proof of AI authorship, but it is a repeated style pattern across half of the blog. Product `elevate` is more likely a marketing template residue than an AI marker.

**Caveat:** “not published”, “pending” and similar evidence-discipline phrases were not counted as AI markers.

### 3.3 Thin content — PASS for articles / P2 for some pages

- Products: minimum 2,073 words — no thin product page.
- Blog: minimum 496 words; the shortest is still a substantive article.
- News: 131–648 words; this is a short-news format, not a thin article failure.
- Pages: 153–6,138 words; the low end is policy/utility pages, not editorial content.
- Product descriptions all have a `description`; no empty product body found.

**P2:** Some pages are likely policy/utility pages with low word counts; verify intent before expanding.

### 3.4 No-value language — PASS with P2 phrase fatigue

Empty/phrase-list hits:

| Collection | Hits | Pages |
|---|---:|---:|
| products | 0 | 0 / 127 |
| blog | 27 | 23 / 195 |
| news | 2 | 2 / 38 |
| pages | 1 | 1 / 22 |

No `high quality`, `best price`, `one-stop`, `professional manufacturer` or `leading manufacturer` pattern was found in products. Blog has some `high quality` / `world-class` residue; remove it where it does not carry evidence.

### 3.5 Subjective viewpoint — PARTIAL / P1

Author's Take / Our Read / Editorial View presence:

| Collection | Present | Total |
|---|---:|---:|
| products | 127 | 127 |
| blog | 70 | 195 |
| news | 0 | 38 |
| pages | 6 | 22 |

General opinion-marker pages:

- products: 127 / 127
- blog: 86 / 195
- news: 2 / 38
- pages: 6 / 22

**Finding:** Products have a consistent judgement block. Blog is uneven: 125/195 lack an explicit Author's Take/Our Read. News is intentionally factual and should not be forced into an editorial opinion block unless the format changes.

### 3.6 Non-originality — PARTIAL

No source-site crawl corpus is stored in this repository, so a hard external 4-gram originality score cannot be produced.

Verified source discipline:

- Products: 127/127 have Sources/References.
- Blog: 96/195 have Sources/References.
- News: 0/38 have a Sources section.
- Pages: 5/22 have Sources.

**Finding:** Product source discipline is strong. Blog and news have a measurable source-section gap. Do not label the site “original” or “copied” without a source corpus; label it **PARTIAL / unverified**.

### 3.7 Metadata and data fields — P1/P2

| Collection | title >60 chars | description >160 chars | Duplicate descriptions |
|---|---:|---:|---:|
| products | 21 / 127 | 0 / 127 | 0 |
| blog | 53 / 195 | 21 / 195 | 0 |
| news | 3 / 38 | 17 / 38 | 0 |
| pages | 3 / 22 | 7 / 22 | 0 |

Additional data issues:

- `products.category`: **127/127 empty**.
- `products.status`: **127/127 `In Stock`**.
- `author`: **0/382**.
- `date` or `updated`: **0/382**.

These are trust/data-completeness issues, not evidence of fabrication. Do not change status/category without source data.

---

## 4. Live sample and technical spot-check

Live samples:

| URL | Status | Title |
|---|---:|---|
| `https://peptidesofchina.com/` | 200 | China Peptides From China \| Peptides of China |
| `https://peptidesofchina.com/blog/` | 200 | China Peptide Blog — Sourcing Guides |
| `https://peptidesofchina.com/news/` | 200 | News — Peptides of China |
| `https://peptidesofchina.com/catalog/5-amino-1mq/` | 200 | Buy 5-Amino-1MQ \| China Peptide |
| `https://peptidesofchina.com/catalog/` | 200 | China Peptide Catalog |

The sampled product page has a self-referencing canonical and a single H1.

### P1 technical finding outside the six content dimensions

**Soft 404 / catch-all route:**

```text
/nonexistent-audit-12345/ → 200, homepage title
/products/foo/             → 200, homepage title
```

Unknown paths return the homepage with HTTP 200 instead of a real 404. This can create index bloat and makes content QA unreliable if a URL is mistyped. It should be fixed with a true 404 route or a 404 status in the catch-all handler.

**Sitemap:** `https://peptidesofchina.com/sitemap-0.xml` returned 386 URLs via curl. The Python urllib probe received 403 from the edge; this is an automated-client block, not evidence that the sitemap is broken.

---

## 5. Six-dimensional matrix and priority

| Dimension | Result | P0 | P1 | P2 |
|---|---|---:|---:|---:|
| Repetition | PASS | 0 | 0 | 0 |
| AI traces | PARTIAL | 0 | 1 | 1 |
| Thin content | PASS | 0 | 0 | 1 |
| No-value language | PASS | 0 | 0 | 1 |
| Subjective viewpoint | PARTIAL | 0 | 1 | 1 |
| Non-originality | PARTIAL | 0 | 1 | 1 |
| Metadata/data fields | FAIL (supporting dimension) | 0 | 2 | 2 |

### P0

None in current content. The prior product-template P0 is no longer reproduced by the current 4-gram scan.

### P1

1. **Blog source gaps** — 99/195 lack Sources/References.
2. **Blog viewpoint gaps** — 125/195 lack Author's Take/Our Read.
3. **Author/date metadata absent** — 0/382; weakens E-E-A-T and freshness.
4. **Soft 404** — unknown paths return 200 homepage.
5. **Product data realism** — 127/127 `In Stock` and 127/127 empty category; confirm against real inventory and category data.

### P2

1. Blog title/description length bands.
2. News source sections and description lengths.
3. Pages source sections.
4. AI-style phrase cleanup in blog.
5. Thin policy/utility pages.
6. Repeated citation boilerplate in products; not a body duplication issue.

---

## 6. Recommended fixes

These are recommendations only; no content was changed in this audit.

> **P1 — Source and viewpoint completion**
> - Add Sources/References to the 99 blog pages that lack them.
> - Add Author's Take/Our Read to the 125 blog pages that lack an explicit judgement block, where the format supports it.
> - Do not add a viewpoint block to factual news unless the editorial format changes.

> **P1 — Author/date fields**
> - Add a verified author field and date/updated field to all published content.
> - Do not invent dates. Use the real publication/review dates.

> **P1 — Soft 404**
> - Return 404 for unknown paths and keep the homepage only at `/`.
> - Verify with `/nonexistent-*` and `/products/foo/`.

> **P1 — Product data**
> - Replace blanket `In Stock` with a verified availability state or `RFQ`.
> - Populate `category` from the actual product taxonomy.
> - Do not infer stock from the page template.

> **P2 — Metadata**
> - Bring the 53 blog, 21 product, 3 news and 3 page titles into the target band.
> - Bring 21 blog, 17 news and 7 page descriptions under 160 characters.

> **P2 — Phrase cleanup**
> - Remove `robust`, `leverage`, `elevate`, `not only`, `crucial` and empty marketing phrases where they do not carry evidence.
> - Keep technical vocabulary where it is precise.

---

## 7. Verified vs assumed

### Verified

- 382 Markdown files counted.
- Word and H2 distributions measured directly from files.
- 4-gram Jaccard and unique-sentence share computed from current files.
- Sources/Author's Take counts measured by heading presence.
- Metadata lengths measured from frontmatter.
- Live sample URLs and soft-404 behavior measured with curl.
- Sitemap 386 URLs measured by curl.

### Assumed / not verified

- No external source corpus, so originality is **PARTIAL**, not a hard PASS/FAIL.
- No GSC data, traffic, rankings or manual-action status.
- No full crawl of all 386 live URLs for status/canonical; only sampled pages.
- No human editorial read of every page; phrase counts are mechanical.
- Frontmatter title/description length is not identical to rendered HTML metadata on every template; spot checks show template overrides exist.

---

## 8. Current verdict

**Content health: improved and structurally sound; not finished.**

The major improvement is that product pages are no longer the template-duplication emergency described in the 2026-11-05 report. The current gaps are:

1. Blog source/viewpoint coverage.
2. Author/date provenance across the corpus.
3. Product data truthfulness (`In Stock`, empty category).
4. Soft 404 behavior.
5. Metadata length cleanup.

No mass rewrite is justified. Work should be page-group based, with source and status evidence, and must not invent authors, dates, stock states or credentials.
