---
title: "CJC-1295 vs Ipamorelin: Sourcing and Analytics"
slug: "cjc-1295-vs-ipamorelin-a-technical-comparison-for-strategic-peptide-sourcing"
description: "How CJC-1295 and ipamorelin differ in sequence, modification, and release testing — plus the batch documents B2B buyers should verify before ordering."
author: "POC Tech Team"
updated: "2026-11-25"
---
CJC-1295 and ipamorelin are usually discussed as a pair, but from a procurement standpoint they are two different analytical problems. CJC-1295 is a 30-residue GHRH analogue carrying a maleimide-based drug affinity complex; ipamorelin is a five-residue pentapeptide. One has a conjugation step and a lipid-like chromatographic profile, the other has a short sequence where a single deletion is a large fraction of the molecule. A buyer who compares them by product name rather than by sequence record will eventually receive the wrong SKU or the wrong certificate.

The first decision is not "which one." It is "which exact structure is on the label." CJC-1295 with DAC, CJC-1295 without DAC (Mod GRF 1-29), and ipamorelin are three distinct specifications. Each needs its own sequence, mass, release panel, and lot history. The rest of this guide sets out how to write those specifications and how to audit the documents that come back.

## Three SKUs behind two names

The market uses "CJC-1295" for two different molecules. The DAC version is a 30-amino-acid GHRH analogue with a maleimidopropionic acid linker designed to bind serum albumin through a thiol-reactive maleimide. The no-DAC version is Mod GRF 1-29, a 29-amino-acid peptide without that linker. The mass difference is not a rounding error: the DAC form is approximately 3,647.2 Da, while Mod GRF 1-29 is approximately 3,367.9 Da. A certificate that reports a mass near 3,368 Da for a product labeled "CJC-1295 with DAC" is describing a different molecule.

Ipamorelin is a pentapeptide with the sequence Aib-His-D-2-Nal-D-Phe-Lys-NH2 and a molecular mass near 711.9 Da. Its short chain makes synthesis cheaper, but it also changes the analytical failure mode. In a 30-mer, a one-residue deletion is a small mass shift against a large parent mass. In a pentapeptide, the same deletion is a large fraction of the molecule and often a visible chromatographic impurity.

The naming problem is compounded by catalog abbreviations. "CJC-1295" without a DAC qualifier is ambiguous. "Mod GRF 1-29," "CJC-1295 no DAC," and "CJC-1295 without DAC" should resolve to the same sequence, but the buyer should confirm that in writing. The purchase order should carry the full name, the residue count, and the modification state, not just the catalog SKU.

## Sequence and modification map

The table below is the minimum identity block for a purchase order. It does not replace the supplier's certificate; it gives the buyer something to compare the certificate against.

| Attribute | CJC-1295 with DAC | CJC-1295 without DAC | Ipamorelin |
|---|---|---|---|
| Residue count | 30 | 29 | 5 |
| N-terminal modification | None stated | None stated | Aib at position 1 |
| C-terminal modification | Amide | Amide | Amide |
| Key side-chain feature | Maleimidopropionic acid linker | None | D-2-Nal, D-Phe |
| Approximate mass | 3,647.2 Da | 3,367.9 Da | 711.9 Da |
| Main synthesis risk | Conjugation incomplete; linker variants | Truncation; deamidation | Deletion; epimerization |
| Primary identity test | LC-MS plus conjugation check | LC-MS | LC-MS/MS |

Two entries need explanation. The DAC linker is reactive toward thiols, and its presence changes both the mass and the hydrophobicity of the peptide. A reversed-phase method that resolves the unmodified peptide may not resolve the conjugated product from a linker-truncated variant. The ipamorelin sequence contains three non-standard features — Aib, D-2-Nal, and D-Phe — and each is a place where a supplier can substitute a cheaper residue or lose stereochemistry. Mass alone will not catch a D-to-L substitution, because the mass is the same. Chiral analysis or NMR is needed to establish stereochemistry; for routine release, the sequence record and the supplier's batch history are the practical controls.

For mass verification arithmetic, the [molecular weight verification guide](/blog/peptide-molecular-weight-verification-steps/) walks through monoisotopic versus average mass and the terminal water correction. The [HPLC versus LC-MS comparison](/blog/hplc-vs-lc-ms-peptides/) explains why a purity result and a mass result should never be read as substitutes.

## DAC chemistry and the certificate

The DAC modification is a conjugation, not a simple side-chain acylation. The maleimide group reacts with a thiol to form a thioether bond, and the reaction has to go to completion without leaving free maleimide or hydrolyzed maleimide in the product. Those species are analytically distinct from the target and can be detected by LC-MS, but only if the method is set up to see them.

A DAC-specific certificate should therefore include four items beyond the standard peptide panel:

- **Conjugation completeness.** The ratio of conjugated peptide to unmodified peptide, with the method used to calculate it.
- **Free linker or hydrolyzed linker.** A stated limit and a result, not a generic "absent."
- **Mass of the conjugate.** The observed mass should match the peptide plus linker, allowing for the counterion.
- **Lot genealogy.** The batch record should tie the peptide intermediate and the linker lot to the final batch.

The last item is the one buyers forget. A supplier can purify a conjugated batch to 98% area and still have used an intermediate lot that was itself out of specification. Batch genealogy is what lets an auditor see whether the starting material was released before conjugation.

## Ipamorelin's short-chain analytics

A five-residue peptide is not automatically easier to source. The synthesis is shorter, but the analytical window is narrower. A deletion, an epimer, or a residual protecting group can all sit close to the main peak, and the mass difference for a single residue may be only 57 to 186 Da against a 712 Da parent.

Three tests matter disproportionately for ipamorelin:

1. **Purity by RP-HPLC at 214 nm.** The small molecule size means the main peak elutes early on a standard peptide gradient. A method transferred from a larger peptide may not retain the pentapeptide well enough to resolve hydrophilic impurities.
2. **Identity by LC-MS/MS.** A five-residue peptide fragments into a small number of b/y ions. Full sequence coverage is achievable, and a report that shows only a single mass peak is weaker evidence than one that shows the fragment ladder.
3. **Counterion and water content.** A 712 Da peptide has a high surface-area-to-mass ratio in the lyophilized state, and the counterion can be a significant fraction of the vial mass. A purity figure without peptide content is not a quantity specification.

The same logic applies to the salt form. Ipamorelin is commonly supplied as an acetate or trifluoroacetate salt. The certificate should state which one, and the mass calculation should use the salt mass rather than the free-base mass. A buyer who compares a free-base theoretical mass to a salt-form observed mass will see a discrepancy that is not a synthesis failure.

## Release panel for both products

The panel below is a research-grade specification that can be adapted to a laboratory's own SOP. It is deliberately written as test-method-criterion-evidence so that it can be pasted into a purchase order.

| Test | Method | Acceptance criterion | Evidence to request |
|---|---|---|---|
| Appearance | Visual | White to off-white powder or cake | Batch record entry and photograph |
| Identity | LC-MS | Within 5 ppm of theoretical mass | Deconvoluted spectrum with charge states |
| Sequence | LC-MS/MS | ≥90% backbone coverage | Annotated b/y ion map |
| Purity | RP-HPLC-UV, 214 nm | ≥98.0% area | Full chromatogram with gradient |
| Impurity profile | Same HPLC method | Report every peak ≥0.05% | Peak table with retention times |
| Counterion | Ion chromatography or titration | Stated identity; TFA ≤1.0% w/w | Report with method |
| Water | Karl Fischer | ≤5.0% w/w | KF result |
| Peptide content | Mass balance | Reported | Calculation and raw values |
| Endotoxin | LAL or rFC | ≤5 EU/mg or stated limit | Report with spike recovery |
| Batch linkage | Document review | Same lot on vial, COA, invoice | Cross-reference |

The system suitability criteria belong in the method, not in a footnote. A typical peptide HPLC method might require resolution ≥2.0 between the main peak and the nearest specified impurity, tailing ≤2.0, and five replicate runs with RSD ≤2.0%. If the certificate does not state those values, the chromatogram cannot be judged as a controlled run.

One row is easy to overlook: peptide content. A 98% pure peptide by area can still be less than 85% peptide by mass once counterion and water are counted. For a pentapeptide, where the counterion fraction can be larger, this gap matters more. If the study needs a defined molar amount, the certificate has to give peptide content or the data to calculate it.

## Impurity routes and method choice

The impurity map differs by molecule, and the method should follow the map rather than a generic template.

For CJC-1295 with DAC, the main routes are incomplete conjugation, hydrolyzed maleimide, linker truncation, and the usual peptide failures — deletion, deamidation, and oxidation. A shallow gradient over a C18 column is usually needed to resolve the conjugated product from the unmodified peptide. The mass spectrometer should be tuned to see both species in the same run.

For Mod GRF 1-29, the absence of the linker makes the peptide less hydrophobic, and the main risks are truncation and deamidation. A method that was validated for the DAC version may not be suitable; the two products need separate methods or a documented bridging study.

For ipamorelin, the short chain concentrates the risk into a few positions. Epimerization at the D-2-Nal or D-Phe residue produces a diastereomer with the same mass, so LC-MS alone cannot rule it out. A chiral HPLC method or an NMR check is the orthogonal test. Deletion of the C-terminal Lys removes the amide and changes both mass and charge.

The practical rule is to ask for the impurity profile, not just the purity number. A peak table with retention times and relative areas tells you whether the method saw the species that the molecule can produce. A single "98.4%" tells you nothing about what the other 1.6% is.

## Supplier verification and lot genealogy

Supplier qualification for these products should be a document trail, not a conversation. Six requests do most of the work:

1. The synthesis site and the purification site, with the legal entity named.
2. The sequence record and the theoretical mass calculation for the exact salt form.
3. The last three lot release summaries, including any out-of-specification or rework events.
4. The name of the testing laboratory and whether it is in-house, contract, or manufacturer-owned.
5. A sample of the chromatogram and mass spectrum, not just the summary table.
6. The retention period for raw data and the person responsible for releasing it.

The DAC product adds a seventh: the linker lot and the conjugation record. Without those, the certificate describes the final batch but not how it was assembled.

Electronic records should be attributable and audit-trailed. 21 CFR Part 11 is the reference framework for electronic records and signatures in a regulated environment; even a research-grade supplier that is not FDA-regulated can be asked whether its chromatography data system has audit trails enabled and whether records can be exported. A supplier that cannot answer that question is telling you something about its quality system.

For a wider view of supplier qualification, the [manufacturer verification protocol](/blog/china-peptide-manufacturer-verification-a-2026-b2b-sourcing-protocol/) maps the document request to the audit step, and the [laboratory verification guide](/blog/peptide-testing-and-analysis-a-professional-guide-to-laboratory-verification/) covers sampling and third-party testing. The [COA authentication guide](/blog/coa-verified-peptides-supplier-how-to-authenticate-research-purity-in-2026/) covers certificate-level checks, and the [bulk ordering protocol](/blog/how-to-buy-peptides-in-bulk-a-2026-direct-to-manufacturer-sourcing-protocol/) covers lot allocation and acceptance.

## Order mechanics and retention

Buy the batch you can test, not the batch you hope to use. For a first order, three vials from one lot is a workable minimum: one for release testing, one for retention, one for the bench. If the supplier cannot supply three vials from the same lot, the order is a sample, not a batch.

Retain the second vial for at least 24 months at −20 °C, labeled with the lot, receipt date, and test date. If a result is disputed, the retained vial is the only sample that can be re-tested without opening a new batch. Record the storage condition and the desiccant used; a vial that absorbed moisture in storage will not give the same result as the original release.

For the DAC product, ask whether the conjugated batch is shipped as one lot or split across fills; the [CJC-1295 with DAC catalog page](/catalog/cjc-1295-with-dac/) lists the vial sizes currently offered, and the [ipamorelin catalog page](/catalog/ipamorelin/) does the same for the pentapeptide. A split fill can produce two vials with the same lot number but different fill dates, which complicates a re-test. The certificate should state the fill date and the number of vials in the lot.

## The Author's Take

**Position.** The most expensive mistake in this category is buying a product name instead of a sequence record. "CJC-1295" is not a specification, and a certificate that does not state which CJC-1295 it describes is not a release document.

**Reasoning.** The DAC and no-DAC products differ by a linker and about 279 Da, but they behave differently on a column, in a mass spectrometer, and in a batch record. Ipamorelin adds a third specification with its own non-standard residues and its own epimerization risk. A supplier that treats all three as one catalog family will eventually ship the wrong one, and the buyer may not catch it until the study is underway. The cost of a sequence record, a lot history, and a retained vial is small compared with the cost of repeating a batch. I would rather buy three characterized vials than thirty uncharacterized ones.

**Disclosure.** Peptides of China sells research peptides. This article is a procurement and analytical judgment, not a claim about the effects of any compound, a dosing guide, or medical advice. Products are supplied for laboratory research use only. Analytical documentation varies by product and batch, and buyers who need independent confirmation should arrange third-party testing after receipt.

## Sources

- Teichman, S. L. et al. Prolonged stimulation of growth hormone (GH) and insulin-like growth factor I secretion by CJC-1295, a long-acting analog of GH-releasing hormone. *Journal of Clinical Endocrinology & Metabolism* (2006). [pubmed.ncbi.nlm.nih.gov/16352683](https://pubmed.ncbi.nlm.nih.gov/16352683/)
- Raun, K. et al. Ipamorelin, the first selective growth hormone secretagogue. *European Journal of Endocrinology* (1998). [pubmed.ncbi.nlm.nih.gov/9849822](https://pubmed.ncbi.nlm.nih.gov/9849822/)
- ICH Q6B. Specifications: Test Procedures and Acceptance Criteria for Biotechnological/Biological Products. [database.ich.org](https://database.ich.org/sites/default/files/Q6B%20Guideline.pdf)
- ICH Q2(R2). Validation of Analytical Procedures (2023). [database.ich.org](https://database.ich.org/sites/default/files/ICH_Q2%28R2%29_Guideline_2023_1130.pdf)
- USP &lt;621&gt; Chromatography. United States Pharmacopeia. [usp.org/usp-nf](https://www.usp.org/usp-nf)
- FDA Guidance for Industry: Bioanalytical Method Validation (2018). [fda.gov](https://www.fda.gov/regulatory-information/search-fda-guidance-documents/bioanalytical-method-validation-guidance-industry)
- Mant, C. T. et al. HPLC analysis and purification of peptides. *Methods in Molecular Biology* (2007). [pubmed.ncbi.nlm.nih.gov/18604941](https://pubmed.ncbi.nlm.nih.gov/18604941/)
- U.S. Code of Federal Regulations, 21 CFR Part 11: Electronic Records; Electronic Signatures. [ecfr.gov](https://www.ecfr.gov/current/title-21/chapter-I/subchapter-A/part-11)
