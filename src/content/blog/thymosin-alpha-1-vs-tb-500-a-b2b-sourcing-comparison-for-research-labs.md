---
title: "Thymosin Alpha-1 vs TB-500: A B2B Sourcing Comparison"
slug: "thymosin-alpha-1-vs-tb-500-a-b2b-sourcing-comparison-for-research-labs"
description: "How thymosin alpha-1 and TB-500 differ in sequence definition, synthesis, and release testing — plus the supplier documents that resolve name ambiguity."
author: "POC Tech Team"
updated: "2026-11-25"
---
The first problem in comparing thymosin alpha-1 and TB-500 is not biology. It is naming. Thymosin alpha-1 is a defined 28-residue, N-acetylated peptide with a molecular mass near 3,108.3 Da. "TB-500" is used in the market for at least two different things: the 43-residue thymosin beta-4 sequence, and a 7-residue fragment corresponding to residues 17–23 of that protein. The fragment is roughly 889 Da; the full sequence is roughly 4,963 Da. A buyer who orders "TB-500" without pinning down the sequence can receive either one.

That ambiguity drives the sourcing plan. The purchase order should state the sequence, residue count, N-terminal modification, and theoretical mass. The certificate should match all four. The rest of this guide covers the identity block, the synthesis risks, the release panel, and the supplier questions that make the comparison auditable.

## The naming problem comes first

A product name is a label, not a structure. In this category, the same label has been applied to a full-length protein and to a short fragment, and catalogs do not always say which one they stock. The practical response is to ask for the sequence in single-letter code before discussing price.

For thymosin alpha-1, the expected structure is a 28-residue peptide with an acetylated N-terminus. The acetylation is not a trivial detail: it adds 42.011 Da and is part of the identity of the natural peptide. A batch that is missing the acetyl group is a different molecule, even if the amino acid chain is correct.

For TB-500, the first question is whether the product is the 43-residue thymosin beta-4 sequence or the 7-residue fragment. The second is whether the N-terminus is acetylated. The third is whether the product is a synthetic peptide or a recombinant protein. Those three answers determine the mass, the analytical package, and the price.

## What each name should specify

The table below is a minimum identity block. It is not a substitute for the supplier's certificate; it is the standard the certificate should meet.

| Attribute | Thymosin alpha-1 | TB-500 (full Tβ4) | TB-500 (fragment 17–23) |
|---|---|---|---|
| Residue count | 28 | 43 | 7 |
| N-terminal form | Acetylated | Acetylated | Acetylated |
| Approximate mass | 3,108.3 Da | 4,963 Da | 889 Da |
| Notable modification risk | Incomplete acetylation | Oxidation at Met; length-related truncation | Acetylation; deletion |
| Main identity test | LC-MS plus acetyl check | LC-MS plus peptide mapping | LC-MS/MS |
| Main purity risk | Truncation, deamidation | Truncation, oxidation, aggregation | Deletion, residual protecting groups |

The table makes the comparison concrete. A certificate that reports a mass near 889 Da for a product described as "TB-500" is describing the fragment, not the full protein. A certificate that reports 4,963 Da is describing the full sequence. Neither is wrong in the abstract; only one matches the buyer's study.

The same logic applies to thymosin alpha-1. A certificate that reports 3,066 Da instead of 3,108 Da may be describing the unacetylated chain. The 42 Da difference is easy to miss on a low-resolution instrument and easy to catch on a high-resolution one.

## Sequence and modification map

Thymosin alpha-1 is a 28-residue peptide. Its N-terminus is acetylated, and the sequence contains several acidic residues that make the peptide hydrophilic. The free-base mass is approximately 3,108.3 Da. The acetylation adds 42.011 Da to the unmodified chain, and the certificate should state whether the mass refers to the acetylated form.

Thymosin beta-4 is a 43-residue protein with a mass near 4,963 Da. The sequence contains a methionine residue, which is a site for oxidation (+15.995 Da). It also contains a high proportion of charged residues, which affects the choice of HPLC method and the ion-pairing agent.

The 17–23 fragment is a 7-residue peptide with the sequence LKKTETQ and an acetylated N-terminus. Its mass is approximately 889 Da. The short chain makes synthesis cheap, but it also means that a deletion or an incomplete acetylation is a large fraction of the molecule.

| Structural feature | Thymosin alpha-1 | Thymosin beta-4 | Fragment 17–23 |
|---|---|---|---|
| Chain length | 28 | 43 | 7 |
| N-acetyl | Yes | Yes | Yes |
| Methionine | None | One | None |
| Cysteine | None | None | None |
| Approximate mass | 3,108.3 Da | 4,963 Da | 889 Da |
| Recommended HPLC load | 10–50 µg | 10–50 µg | 5–20 µg |

The load column is a practical detail, not a release criterion. A short peptide at a standard 1 mg/mL load can overload a narrow-bore column and distort the peak shape. The method should state the load and the sample volume, and the certificate should show a chromatogram that is within the detector's linear range.

For the mass arithmetic, the [molecular weight verification guide](/blog/peptide-molecular-weight-verification-steps/) covers monoisotopic versus average mass and the terminal water correction. The [HPLC versus LC-MS comparison](/blog/hplc-vs-lc-ms-peptides/) explains why a purity result and an identity result answer different questions.

## Synthesis and modification risks

Thymosin alpha-1 is made by solid-phase peptide synthesis. The chain is long enough that truncation and deletion are real risks, and the N-terminal acetylation adds a step that can be incomplete. A batch with the correct chain but incomplete acetylation will have a mass 42 Da lower than expected and may co-elute with the target on a generic gradient.

Thymosin beta-4 is a 43-residue sequence. At 99% per coupling, the theoretical share of full-length product after 43 couplings is about 65%; at 98%, about 42%. Purification removes many failures, but the longer chain means more deletion species and a higher purification burden. The methionine residue adds an oxidation route that is sensitive to the cleavage and lyophilization conditions.

The fragment is shorter and cheaper, but it has its own risks. The acetyl group can be incomplete, and the short chain offers few hydrophobic anchors for a reversed-phase method. A gradient that was designed for a 3 kDa peptide may elute the fragment too early to resolve a deletion.

For all three, the purification route should be described in the batch record: the column chemistry, the gradient, the fraction-cutting criterion, and the salt exchange. A certificate that reports only a purity percentage has left out the process information that explains batch-to-batch variation.

## Release panel for both products

The panel below is a research-grade specification. It can be adapted to a laboratory SOP and copied into a purchase order.

| Test | Method | Acceptance criterion | Evidence to request |
|---|---|---|---|
| Appearance | Visual | White to off-white powder or cake | Batch record entry and photograph |
| Identity | LC-MS | Within 5 ppm of the theoretical mass for the stated form | Deconvoluted spectrum with charge states |
| Sequence | LC-MS/MS or peptide mapping | ≥90% coverage | Annotated fragment map |
| N-acetylation | Mass difference or peptide mapping | Consistent with the acetylated form | Spectrum or map showing the N-terminal peptide |
| Purity | RP-HPLC-UV, 214 nm | ≥98.0% area | Full chromatogram with gradient |
| Impurity profile | Same HPLC method | Report every peak ≥0.05% | Peak table with retention times |
| Oxidation | LC-MS or peptide mapping | Report Met oxidation | Extracted ion chromatogram |
| Counterion | Ion chromatography or titration | Stated identity; TFA ≤1.0% w/w | Report with method |
| Water | Karl Fischer | ≤5.0% w/w | KF result |
| Peptide content | Mass balance | Reported | Calculation and raw values |
| Endotoxin | LAL or rFC | ≤5 EU/mg or stated limit | Report with spike recovery |
| Batch linkage | Document review | Same lot on vial, COA, invoice | Cross-reference |

The acetylation row is the one that distinguishes a real certificate from a generic peptide COA. A supplier that reports a mass and a purity but does not address the N-terminus has not shown that the product is the acetylated form. The oxidation row matters for the full Tβ4 sequence, where methionine is present; it is less relevant for the fragment.

Endotoxin is not a universal requirement for every research use, but if the supplier reports a pass, the report should name the assay format, the limit, the numeric value, and spike recovery at the dilution used. The [endotoxin testing guide](/blog/endotoxin-testing-peptide-manufacturing/) explains why a "pass" without those fields cannot be reviewed.

## COA fields and batch linkage

A certificate should let an independent reviewer reconstruct the measurement without calling the supplier. Six fields do most of that work:

- **Method details.** Column chemistry and dimensions, mobile phase, gradient, flow rate, temperature, wavelength, sample load, and integration threshold.
- **System suitability.** Resolution, tailing, and replicate precision. A common peptide baseline is resolution ≥2.0, tailing ≤2.0, and RSD ≤2.0% across five runs.
- **Mass evidence.** Instrument class, calibration mode, mass accuracy, adduct assignment, and the deconvoluted spectrum.
- **Batch identifiers.** Lot number, manufacture date, fill date, retest date, and specification version.
- **Raw-data statement.** Whether chromatograms and spectra are retained and for how long.
- **Deviation record.** Whether the batch met specification on first pass and what changed if it did not.

The batch record behind the certificate should also show the acetylation step and the purification gradient. Those are process parameters, not release tests, but they explain why one batch has a lower acetyl content than another. A supplier that cannot describe its acetylation route is not in a position to make a batch-to-batch consistency claim.

## Supplier verification questions

Supplier qualification for these products should be a document trail, not a conversation. Seven questions cover most of the ground:

1. **Which sequence is this?** Ask for the single-letter sequence and the residue count, not the catalog name.
2. **Is the N-terminus acetylated?** Ask for the mass evidence or the peptide map that shows it.
3. **Is the product synthetic or recombinant?** The answer changes the impurity profile and the analytical package.
4. **Which lots are available?** Ask for the last three lot release summaries, including any rework.
5. **Who performs the testing?** In-house, contract, or manufacturer-owned are different evidence levels.
6. **What is the impurity profile?** Ask for the peak table, not just the main-peak percentage.
7. **What happens on failure?** A written nonconformance and replacement rule matters more than a verbal assurance.

For a first order, request a small sample and send one vial for independent HPLC and LC-MS. The cost is small relative to the cost of repeating a study. The [COA authentication guide](/blog/coa-verified-peptides-supplier-how-to-authenticate-research-purity-in-2026/) covers certificate-level checks, and the [manufacturer verification protocol](/blog/china-peptide-manufacturer-verification-a-2026-b2b-sourcing-protocol/) maps the document request to the audit step.

## Order mechanics and retention

Buy three vials from one lot for a first order: one for release testing, one for retention, one for the bench. If the supplier cannot provide three vials from the same lot, the order is a sample, not a batch. Retain the second vial for at least 24 months at −20 °C, labeled with the lot, receipt date, and test date.

For the full Tβ4 sequence, ask whether the batch was shipped as one lot or split across fills. A split fill can produce vials with the same lot number but different fill dates and thermal histories. The certificate should state the fill date and the number of vials in the lot.

The decision rule is straightforward. If the study depends on the full Tβ4 sequence, require a mass near 4,963 Da and a peptide map that covers the chain. If the study uses the fragment, require a mass near 889 Da and an acetylation check. If the supplier cannot state which sequence it ships, the quote is not comparable. The [thymosin alpha-1 catalog page](/catalog/thymosin-alpha-1/) and the [TB-500 catalog page](/catalog/tb-500/) list the vial sizes and the documentation available for the current batch.

## The Author's Take

**Position.** In this category, the sequence record is the product. A catalog that sells "TB-500" without stating whether it is the 43-residue protein or the 7-residue fragment is not giving the buyer enough information to place an order.

**Reasoning.** The two TB-500 forms differ by more than 4 kDa, and the thymosin alpha-1 identity depends on an N-acetyl group that adds 42 Da. Those are not subtle variations; they are different materials with different analytical packages. A supplier that can state the sequence, the acetylation state, and the mass is telling you that it knows what it is shipping. A supplier that cannot is asking you to trust a label. The cost of a sequence record and a retained vial is small compared with the cost of discovering the mismatch after the batch has been opened.

**Disclosure.** Peptides of China sells research peptides. This article is a procurement and analytical judgment, not a claim about the effects of any compound, a dosing guide, or medical advice. Products are supplied for laboratory research use only. Analytical documentation varies by product and batch, and buyers who need independent confirmation should arrange third-party testing after receipt.

## Sources

- Thymosin alpha-1 clinical applications and evidence landscape: a scoping review. *Pharmaceuticals* (2026). [pubmed.ncbi.nlm.nih.gov/42797537](https://pubmed.ncbi.nlm.nih.gov/42797537/)
- Thymosin β4 and actin: binding modes, biological functions and clinical applications. *Current Protein & Peptide Science* (2023). [pubmed.ncbi.nlm.nih.gov/36464872](https://pubmed.ncbi.nlm.nih.gov/36464872/)
- ICH Q6B. Specifications: Test Procedures and Acceptance Criteria for Biotechnological/Biological Products. [database.ich.org](https://database.ich.org/sites/default/files/Q6B%20Guideline.pdf)
- ICH Q2(R2). Validation of Analytical Procedures (2023). [database.ich.org](https://database.ich.org/sites/default/files/ICH_Q2%28R2%29_Guideline_2023_1130.pdf)
- USP &lt;621&gt; Chromatography. United States Pharmacopeia. [usp.org/usp-nf](https://www.usp.org/usp-nf)
- FDA Guidance for Industry: Bioanalytical Method Validation (2018). [fda.gov](https://www.fda.gov/regulatory-information/search-fda-guidance-documents/bioanalytical-method-validation-guidance-industry)
- Mant, C. T. et al. HPLC analysis and purification of peptides. *Methods in Molecular Biology* (2007). [pubmed.ncbi.nlm.nih.gov/18604941](https://pubmed.ncbi.nlm.nih.gov/18604941/)
- U.S. Code of Federal Regulations, 21 CFR Part 211: Current Good Manufacturing Practice for Finished Pharmaceuticals. [ecfr.gov](https://www.ecfr.gov/current/title-21/chapter-I/subchapter-C/part-211)
