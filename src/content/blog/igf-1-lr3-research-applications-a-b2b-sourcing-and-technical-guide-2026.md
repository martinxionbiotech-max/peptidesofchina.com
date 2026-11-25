---
title: "IGF-1 LR3 Sourcing: Sequence, Analytics, and Supplier Checks"
slug: "igf-1-lr3-research-applications-a-b2b-sourcing-and-technical-guide-2026"
description: "A 2026 B2B guide to IGF-1 LR3 procurement: the LR3 modification, mass verification, stability risks, and the documents a supplier should provide."
author: "POC Tech Team"
updated: "2026-11-25"
---
IGF-1 LR3 is not native IGF-1 with a different label. It is an 83-residue analogue of the 70-residue human sequence, carrying a 13-residue N-terminal extension and substitutions that change its binding behavior. That structural difference is the first thing a buyer should verify, because a supplier that describes the product only as "IGF-1" has not told you which molecule is in the vial. The second thing to verify is the mass: at roughly 9.1 kDa, LR3 produces a broad charge-state envelope, and a single nominal mass reading is weak identity evidence.

The sourcing plan follows from those two facts. Ask for the full sequence, the calculated mass for the stated salt form, a deconvoluted mass spectrum, and a purity method that can resolve the analogue from related species. Then ask for the batch record that ties those results to the vial. This guide covers each step in the order a procurement team encounters it.

## What the LR3 modification changes

Native human IGF-1 is a 70-amino-acid single-chain peptide with three intramolecular disulfide bonds. The LR3 analogue extends the N-terminus by 13 residues (MFPAMPLLSLFVN) and carries a single substitution at position 3, where arginine replaces glutamic acid. Those changes reduce binding to IGF-binding proteins. The result is an 83-residue chain with a molecular mass near 9,111 Da.

Those changes matter for sourcing in three ways:

- **Mass.** The extension adds roughly 1.4 kDa to the native mass, so a certificate that reports a mass near 7.6 kDa is describing native IGF-1, not LR3.
- **Folding.** Three disulfide bonds have to form correctly. A batch with the right mass but the wrong disulfide pairing can be analytically indistinguishable by simple LC-MS and functionally different in a cell-culture study.
- **Aggregation.** A 9 kDa chain with hydrophobic surfaces is prone to self-association at higher concentrations. Size-exclusion chromatography or dynamic light scattering is a more informative release test than purity by RP-HPLC alone.

The name "LR3" itself is a source of ambiguity. Some catalogs use it for the 83-residue analogue, others for a related long-chain variant, and some list "IGF-1 LR3" alongside "IGF-1" without stating the difference. The purchase order should specify the residue count and the N-terminal extension, not just the three-letter tag.

## The sequence and mass you should see on paper

A supplier's identity block should contain five items: the full amino acid sequence in single-letter code, the residue count, the disulfide connectivity, the theoretical mass in monoisotopic and average modes, and the salt form. If any of those is missing, the certificate is incomplete before the first test is run.

The mass calculation deserves its own check. For a 9 kDa peptide, the difference between monoisotopic and average mass is small in absolute terms but not in the context of a 5 ppm tolerance. A 9,111 Da peptide at 5 ppm allows a window of about 0.046 Da. If the certificate reports a mass rounded to the nearest dalton, the buyer cannot tell whether the result is inside that window. The report should give at least one decimal place, and preferably the observed monoisotopic mass with the charge states used for deconvolution.

| Attribute | Native IGF-1 | IGF-1 LR3 |
|---|---|---|
| Residue count | 70 | 83 |
| N-terminal extension | None | 13 residues |
| Approximate mass | ~7.6 kDa | ~9.1 kDa |
| Disulfide bonds | 3 | 3 |
| Binding-protein behavior | High-affinity IGFBP binding | Reduced IGFBP binding |
| Main analytical risk | Identity and oxidation | Identity, disulfide pairing, aggregation |
| Recommended identity test | LC-MS plus peptide mapping | LC-MS deconvolution plus peptide mapping |

The table is not a pharmacology summary. It is a checklist for reading a certificate. A supplier that cannot fill in the right-hand column for its own product has not characterized the batch to the level the study needs.

For the mass arithmetic and the common monoisotopic-versus-average error, the [molecular weight verification guide](/blog/peptide-molecular-weight-verification-steps/) sets out the calculation. The [HPLC versus LC-MS comparison](/blog/hplc-vs-lc-ms-peptides/) explains why a purity number and a mass number should be requested together.

## Synthesis and folding risks

An 83-residue chain is long for solid-phase peptide synthesis. Each coupling step adds a chance for an incomplete chain, and the cumulative yield falls quickly: at 99% per step, 83 couplings retain about 43% of the theoretical full-length product before purification; at 98%, about 19%. Those figures are simplified because the synthesis is not a single sequence of independent events, but they explain why LR3 is more expensive per milligram than a 30-mer and why purification losses are larger.

The disulfide bonds add a second layer of risk. After chain assembly and cleavage, the peptide has to fold so that the three bonds form between the correct cysteine pairs. A supplier may use an oxidative folding buffer, a redox pair, or a directed protecting-group strategy. The certificate rarely describes the folding route, but the batch record should. A product with the correct mass and a clean RP-HPLC peak can still contain scrambled disulfides that co-elute with the target.

Aggregation is the third risk. Lyophilized powder is relatively stable, but a batch that was exposed to high concentration or a poor buffer during purification can carry soluble aggregates into the final fill. SEC-HPLC with a UV detector at 214 or 280 nm is the practical release test; a single peak at the expected retention time is stronger evidence than a purity percentage from RP-HPLC.

## Release panel for IGF-1 LR3

The panel below is a research-grade specification. It is written so that each row can be copied into a purchase order without translation.

| Test | Method | Acceptance criterion | Evidence to request |
|---|---|---|---|
| Appearance | Visual | White to off-white lyophilized powder | Batch record entry and photograph |
| Identity | LC-MS deconvolution | Within 5 ppm of theoretical mass | Spectrum with charge states annotated |
| Sequence | Peptide mapping or MS/MS | ≥90% sequence coverage | Annotated fragment map |
| Purity | RP-HPLC-UV, 214 nm | ≥98.0% area | Full chromatogram with gradient |
| Aggregates | SEC-HPLC | Report monomer, dimer, and higher species | Chromatogram with integration |
| Disulfide pairing | Peptide mapping under non-reducing conditions | Consistent with the stated connectivity | Digest map and retention times |
| Counterion | Ion chromatography or titration | Stated identity; TFA ≤1.0% w/w | Report with method |
| Water | Karl Fischer | ≤5.0% w/w | KF result |
| Peptide content | Mass balance | Reported | Calculation and raw values |
| Endotoxin | LAL or rFC | ≤5 EU/mg or stated limit | Report with spike recovery |
| Batch linkage | Document review | Same lot on vial, COA, invoice | Cross-reference |

The aggregate row is the one most often omitted. A certificate that reports only RP-HPLC purity describes the separation of species by hydrophobicity; it does not describe how much of the product is monomer. For a cell-culture reagent, aggregate content can matter more than a tenth of a percent of a hydrophilic impurity.

The disulfide row is the second omission. Routine release testing rarely includes a non-reducing digest, but a supplier that claims a specific connectivity should be able to show a map that supports it. If the certificate does not address disulfides, the buyer should treat the folding claim as unverified rather than assume it.

## COA fields and batch record

A certificate for a 9 kDa analogue should let a reviewer reconstruct the run. The six fields below are the minimum:

- **Method details.** Column chemistry and dimensions, mobile phase, gradient, flow rate, temperature, wavelength, sample load, and integration threshold.
- **System suitability.** Resolution, tailing, and replicate precision. For a peptide method, resolution ≥2.0, tailing ≤2.0, and RSD ≤2.0% across five runs is a common baseline.
- **Mass evidence.** Instrument class, calibration mode, mass accuracy, adduct assignment, and the deconvoluted spectrum.
- **Batch identifiers.** Lot number, fill date, manufacture date, retest date, and the specification version.
- **Raw data statement.** Whether chromatograms and spectra are retained and for how long.
- **Deviation record.** Whether the batch met specification on first pass and what changed if it did not.

The batch record behind the certificate should also show the folding step, the purification gradient, and the lyophilization cycle. Those are process parameters, not release tests, but they explain why one batch aggregates and another does not. A supplier that cannot describe its folding route is not in a position to make a batch-to-batch consistency claim.

## Stability, shipping, and storage

Lyophilized IGF-1 LR3 is typically shipped at ambient temperature or with a cold pack, depending on the route and the season. The shipping documents should state the expected temperature range and whether a temperature logger is included. A vial that arrives warm is not automatically degraded, but a logger record is the only way to know whether the excursion was brief or prolonged.

Storage recommendations vary by supplier. A common research-grade recommendation is −20 °C for the lyophilized powder and 2–8 °C for a reconstituted solution, with avoidance of repeated freeze-thaw cycles. The certificate or datasheet should state the recommended conditions, the retest period, and the concentration at which the material is stable. A supplier that gives no storage guidance has not characterized the product beyond release.

| Stage | Typical condition | What to record | Red flag |
|---|---|---|---|
| Shipping | Ambient or 2–8 °C with cold pack | Carrier, duration, logger data | No temperature record for a summer shipment |
| Receipt | Inspect vial and desiccant | Appearance, vial integrity, lot | Broken vacuum or damaged cake |
| Lyophilized storage | −20 °C, desiccated | Storage date, location | Repeated warming to room temperature |
| Reconstituted storage | 2–8 °C, short-term | Buffer, concentration, date | Freeze-thaw cycles |
| Retention sample | −20 °C, separate vial | Lot, receipt date, test date | No retained vial |

The table is a handling record, not a dosing instruction. Its purpose is to make a future re-test possible. If a result is disputed six months later, the retained vial and the storage log are the only evidence that the sample was handled consistently.

For reconstitution and handling technique, the [lyophilization and reconstitution guide](/blog/peptide-lyophilization-reconstitution-guide-for-researchers/) covers the practical steps without moving into administration. The [solubility troubleshooting guide](/blog/peptide-solubility-troubleshooting/) covers the common causes of incomplete dissolution.

## Supplier verification questions

Supplier qualification for LR3 should be more document-heavy than for a short peptide. Seven questions do most of the work:

1. **Is the product synthetic or recombinant?** The answer changes the impurity profile and the analytical package. A synthetic 83-mer and a recombinant protein are not release-tested the same way.
2. **Where is the folding performed?** Ask for the site and the folding route, not just the purification site.
3. **What is the aggregate profile?** Request SEC data, not a statement that the product is "monomeric."
4. **What is the disulfide connectivity?** Ask for the mapping method and a representative result.
5. **Which lots are available?** A supplier with one lot has no batch history.
6. **Who performs the testing?** In-house, contract, or manufacturer-owned are different evidence levels.
7. **What happens on failure?** A written nonconformance and replacement rule matters more than a verbal assurance.

Electronic records should be attributable and audit-trailed. 21 CFR Part 11 is the reference framework for electronic records and signatures in a regulated environment; a supplier that cannot say whether its chromatography system has audit trails enabled is not a qualified source for a regulated-adjacent study.

For a wider supplier qualification sequence, the [manufacturer verification protocol](/blog/china-peptide-manufacturer-verification-a-2026-b2b-sourcing-protocol/) maps each request to an audit step. The [customs documentation guide](/blog/research-peptide-customs-clearance-a-professional-b2b-sourcing-guide-2026/) covers the invoice and certificate-of-origin fields that should match the batch record.

## Order mechanics and retention

Buy three vials from one lot for a first order: one for release testing, one for retention, one for the bench. If the supplier cannot provide three vials from the same lot, the order is a sample, not a batch. For LR3, the retention vial should be stored separately from the working vial and labeled with the lot, receipt date, and test date.

Ask for the fill date and the number of vials in the lot. A large lot split across multiple fill dates can produce vials with the same lot number but different thermal histories. The certificate should state the fill date, and the shipping record should show whether the vials traveled together.

The decision rule is straightforward. If the study depends on the LR3 modification, require a mass that matches the 83-residue sequence and a peptide map that supports the disulfide connectivity. If the study is a cell-culture assay where aggregation matters, require SEC data before the first order. If the supplier cannot provide either, the quote is not comparable to one that can. The [IGF-1 LR3 catalog page](/catalog/igf-1-lr3/) lists the vial sizes and the documentation available for the current batch.

## The Author's Take

**Position.** LR3 is a case where the label is less informative than the sequence. A buyer who accepts "IGF-1 LR3" as a specification is one catalog update away from receiving native IGF-1 or a differently extended analogue.

**Reasoning.** The 13-residue extension and the receptor-binding substitutions are the whole point of the analogue, and both are checkable on paper. The mass difference between native and LR3 is large enough to catch a substitution, but only if the certificate states the theoretical mass and gives a deconvoluted spectrum rather than a rounded number. The disulfide and aggregate data are harder to obtain, which is exactly why they are worth asking for: a supplier that can produce them has a process, and a supplier that cannot is guessing. I would rather pay for a smaller batch with a folding record than a larger batch with a purity percentage.

**Disclosure.** Peptides of China sells research peptides. This article is a procurement and analytical judgment, not a claim about the effects of any compound, a dosing guide, or medical advice. Products are supplied for laboratory research use only. Analytical documentation varies by product and batch, and buyers who need independent confirmation should arrange third-party testing after receipt.

## Sources

- Ballard, F. J. et al. Long R3 insulin-like growth factor-I (IGF-I) infusion stimulates organ growth but reduces plasma IGF-I, IGF-II and IGF binding protein concentrations. *Journal of Endocrinology* (1995). [pubmed.ncbi.nlm.nih.gov/7561636](https://pubmed.ncbi.nlm.nih.gov/7561636/)
- ICH Q6B. Specifications: Test Procedures and Acceptance Criteria for Biotechnological/Biological Products. [database.ich.org](https://database.ich.org/sites/default/files/Q6B%20Guideline.pdf)
- ICH Q5C. Stability Testing of Biotechnological/Biological Products. [database.ich.org](https://database.ich.org/sites/default/files/Q5C%20Guideline.pdf)
- ICH Q2(R2). Validation of Analytical Procedures (2023). [database.ich.org](https://database.ich.org/sites/default/files/ICH_Q2%28R2%29_Guideline_2023_1130.pdf)
- USP &lt;621&gt; Chromatography. United States Pharmacopeia. [usp.org/usp-nf](https://www.usp.org/usp-nf)
- FDA Guidance for Industry: Bioanalytical Method Validation (2018). [fda.gov](https://www.fda.gov/regulatory-information/search-fda-guidance-documents/bioanalytical-method-validation-guidance-industry)
- Mant, C. T. et al. HPLC analysis and purification of peptides. *Methods in Molecular Biology* (2007). [pubmed.ncbi.nlm.nih.gov/18604941](https://pubmed.ncbi.nlm.nih.gov/18604941/)
- U.S. Code of Federal Regulations, 21 CFR Part 211: Current Good Manufacturing Practice for Finished Pharmaceuticals. [ecfr.gov](https://www.ecfr.gov/current/title-21/chapter-I/subchapter-C/part-211)
