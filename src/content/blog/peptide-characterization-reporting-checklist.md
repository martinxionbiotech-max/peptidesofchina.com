---
title: "Peptide Characterization Reporting Checklist: Identity, Purity, and Impurity Data"
slug: "peptide-characterization-reporting-checklist"
description: "A reviewer's checklist for peptide characterization reports: sequence and mass confirmation, orthogonal purity methods, impurity profiling, assay validation, and report fields."
---

A peptide characterization report should let an independent reviewer answer four questions without opening the vial: is this the intended sequence, how much of the sample is that sequence, what else is in it, and which method would detect a change on stability? A certificate that reports a single HPLC percentage answers only part of the second question. It does not establish identity, does not describe the impurity profile, and does not show whether the method can detect a degradation product.

This checklist is for research procurement teams and laboratory reviewers who receive characterization data from a supplier or contract laboratory. It covers the analytical package, the method details that make a result reproducible, and the report fields that separate a characterization report from a marketing attachment.

## What the report must establish

Characterization is a set of orthogonal measurements, not one test with a longer name. Each measurement answers a different question, and a gap in any row leaves the material partially defined.

| Question | Primary method | What the report should show |
| --- | --- | --- |
| Is the sequence correct? | LC-MS/MS or Edman sequencing | Observed mass, fragment coverage, matched sequence |
| Is the mass consistent with the structure? | ESI-MS or MALDI-MS | Monoisotopic or average mass, deconvoluted value, mass error |
| How pure is the target? | RP-HPLC | Column, gradient, wavelength, integration, main-peak percentage |
| What impurities are present? | RP-HPLC plus orthogonal separation | Relative retention, peak area, tentative identification |
| Is the counterion consistent? | Ion chromatography | TFA, acetate, or chloride content |
| How much is peptide by mass? | Amino acid analysis or nitrogen determination | Net peptide content, correction factor |
| Is the higher-order structure intact? | CD, FTIR, or NMR | Spectrum, comparison with reference, interpretation |
| Will the method detect degradation? | Forced degradation | Conditions, mass balance, degradant peaks |

A report can omit a method when the product does not require it. A 10-residue linear peptide does not need a full higher-order structure package. It cannot omit identity, purity, impurity, and content, because those four determine whether the material is usable.

## Identity: mass, sequence, and composition

The first identity check is mass. For a linear peptide, the theoretical monoisotopic mass is calculated from the sequence, including modifications, counterions if the method measures the salt, and any expected disulfide bonds. The observed mass from LC-MS is compared with that value. The [molecular weight verification guide](/blog/peptide-molecular-weight-verification-steps) shows how to calculate the expected value and where salt forms change it.

Low-resolution mass spectrometry confirms unit mass but cannot distinguish a deletion of glycine from a substitution of alanine in some cases. High-resolution mass spectrometry adds mass accuracy, typically within 5 ppm on a QTOF or Orbitrap instrument. A 2,000 Da peptide at 5 ppm allows a 0.01 Da window, which is enough to separate many near-isobaric variants.

Mass alone is not sequence confirmation. Two different sequences can share the same mass. The stronger evidence is MS/MS fragmentation with sequence coverage. For a 20-residue peptide, a report should show fragment ions covering most of the backbone, with the b- and y-ion series labeled. A report that shows only a single deconvoluted mass has confirmed the mass, not the sequence.

Edman degradation remains useful for the N-terminal sequence of short peptides, but it fails on blocked N-termini and cannot read through modified residues. For routine research lots, LC-MS/MS with a documented fragmentation pattern is the practical standard.

Amino acid analysis hydrolyzes the peptide into free amino acids and quantifies them. The result gives a composition ratio, which can confirm the expected residues and detect a deletion or substitution that mass alone missed.

The method details matter. Typical hydrolysis uses 6 M hydrochloric acid at 110 °C for 24 hours under vacuum. Tryptophan is destroyed by acid hydrolysis and must be measured separately after alkaline hydrolysis or by UV spectroscopy. Cysteine requires performic acid oxidation before hydrolysis. Asparagine and glutamine are converted to aspartate and glutamate, so the analysis reports the combined acidic residues.

A composition table should list each residue, the expected molar ratio, the observed ratio, and the acceptance range. A ratio outside 0.9–1.1 of expected for a single residue is a query. The same hydrolysate can be used for net peptide content by comparing the total amino acid recovery with the weighed sample mass.

## Purity: the reversed-phase method is part of the result

Reversed-phase HPLC is the default purity method for synthetic peptides. The reported percentage is only meaningful when the method is described. A reviewer needs the column dimensions and particle size, mobile phase composition, gradient slope and run time, flow rate, detection wavelength, injection volume or mass, and integration parameters.

| Report field | Example entry | Why it matters |
| --- | --- | --- |
| Column | C18, 4.6 × 250 mm, 5 µm, 300 Å | Selectivity and peak capacity |
| Mobile phase | A: 0.1% TFA in water; B: 0.1% TFA in acetonitrile | Ion pairing and baseline |
| Gradient | 5–65% B over 30 minutes | Impurities outside the window are missed |
| Flow rate | 1.0 mL/min | Retention and peak shape |
| Detection | 220 nm, 4 nm bandwidth | Peptide bond absorbance |
| Injection | 20 µL of 0.5 mg/mL solution | Column load and peak symmetry |
| Integration | Manual review, threshold 0.05% | Small peaks can be excluded |
| Result | Main peak 98.2%, largest unspecified 0.4% | Purity claim and impurity limit |

A certificate that reports "purity: 98.5%" with no method is not reviewable. Two laboratories can test the same lot on different gradients and report values that differ by several percentage points. The [COA reading guide](/blog/how-to-read-a-peptide-coa-a-researchers-guide-to-hplc-and-ms-reports) shows how to compare the chromatogram with the written method.

Area normalization also hides anything that does not absorb at the detection wavelength. Water, salts, and residual solvents are invisible. That is why the report needs separate tests for water content, counterions, and residual solvents.

## Orthogonal separation: why one column is not enough

A single reversed-phase method separates by hydrophobicity. Impurities that differ in charge, size, or polarity may co-elute with the target. An orthogonal method uses a different separation mechanism and can reveal what the first method missed.

| Method | Separation basis | Best for | Limitation |
| --- | --- | --- | --- |
| RP-HPLC | Hydrophobicity | Main purity and hydrophobic variants | Co-elution of similar sequences |
| Ion-exchange HPLC | Net charge | Charge variants, deamidation, succinimide | Salt gradients complicate MS coupling |
| Size-exclusion HPLC | Molecular size | Aggregates, dimers, oligomers | Poor resolution for small sequence variants |
| HILIC | Polarity | Very polar or hydrophilic peptides | Method development time |
| Capillary electrophoresis | Charge-to-size ratio | Charge heterogeneity | Lower preparative relevance |

A characterization package for a high-value lot should include at least one orthogonal method beyond RP-HPLC. For a peptide prone to aggregation, SEC is the informative addition. For a peptide with several basic residues, ion exchange can separate deamidated forms that co-elute on C18. The [HPLC versus LC-MS guide](/blog/hplc-vs-lc-ms-peptides) covers method selection in more detail.

## Mass spectrometry: from unit mass to structure

LC-MS serves two roles: confirmation of the intact mass and identification of impurities. For intact mass, the report should state the ionization mode, the charge states observed, the deconvolution method, and the mass error in ppm. For impurity identification, the report should show the mass of each detected impurity and, where possible, a proposed structure.

A practical acceptance criterion for a research peptide is an observed mass within 0.1% of theoretical by low-resolution MS, or within 10 ppm by high-resolution MS. The tighter number is only meaningful if the instrument is calibrated and the method is described. A mass error of 0.3 Da on a 3,000 Da peptide is 100 ppm and should trigger a review.

Tandem mass spectrometry adds sequence information. For a modified peptide, the fragmentation pattern should show the modification site, not just the intact mass. For a disulfide-containing peptide, the report should show the reduced and non-reduced mass, because the intact mass alone does not prove the disulfide connectivity.

## Net peptide content and the mass balance

Net peptide content is the fraction of the vial mass that is the peptide itself, excluding water, counterions, and residual solvents. It is the number a laboratory needs to weigh accurately. A certificate that reports 98% HPLC purity and 80% net peptide describes a material that is 80% peptide by mass, not 98%.

The mass balance approach sums the measured non-peptide components:

**Net peptide content = 100% − water − counterion − residual solvents − inorganic residue − unrelated impurities.**

Each term needs a method. Water is measured by Karl Fischer titration, typically 3–8% for a lyophilized peptide. Counterions are measured by ion chromatography; trifluoroacetate can account for 5–20% by mass in basic peptides. Residual solvents are measured by headspace gas chromatography after drying. Inorganic residue is measured by residue on ignition or thermogravimetric analysis.

A report should state the method and the result for each term. If the sum of the non-peptide components plus the peptide content does not approximate 100%, the mass balance is incomplete and the net content is an estimate.

## Higher-order structure: when it belongs in the report

Higher-order structure methods are often unnecessary for short linear research peptides. They become relevant for longer sequences, helical peptides, disulfide-rich peptides, and any product where aggregation or conformational change affects activity.

Circular dichroism measures secondary structure in the far-UV range, typically 190–260 nm, using a 0.1 cm path-length cell and a peptide concentration of 0.1–0.5 mg/mL. The spectrum can show α-helix, β-sheet, or random coil content, but it is not a quantitative structure determination. FTIR provides a complementary view through amide I band positions. NMR can give residue-level structure for short peptides, at the cost of higher sample concentration and instrument time.

For a research peptide, the practical use of these methods is comparison: does the lot match a reference spectrum, and does the spectrum change after storage? A single CD spectrum without a reference or a stability comparison is difficult to interpret.

## Stability-indicating methods and forced degradation

A purity method is only useful for stability work if it can detect degradation products. Forced degradation demonstrates that it can.

Typical conditions include acid hydrolysis in 0.1 M hydrochloric acid for 24 hours, base hydrolysis in 0.1 M sodium hydroxide for 24 hours, oxidation with 0.3–3% hydrogen peroxide, thermal stress at 40 °C, and photostability under ICH Q1B conditions. The report should show the chromatograms before and after each condition, the mass balance, and the peaks that increased. Acid stress tends to hydrolyze Asp-Pro bonds and deamidate asparagine; base stress can racemize residues and scramble disulfides; oxidation converts methionine to the sulfoxide and modifies tryptophan; thermal stress promotes aggregation and deamidation; light stress attacks aromatic residues.

A method that shows no degradant peaks under any condition is either exceptionally specific or insufficiently stressed. The report should explain which.

## The report template: fields a reviewer should find

A complete characterization report for a research peptide typically contains the following sections. The order is less important than the presence of each field.

1. Product identification: name, sequence, modifications, molecular formula, theoretical mass.
2. Lot number and manufacturing site.
3. Appearance and fill weight.
4. Identity by mass spectrometry: method, observed mass, mass error, spectrum.
5. Identity by MS/MS or sequencing: fragment coverage and interpretation.
6. Amino acid composition: expected and observed ratios, hydrolysis method.
7. Purity by RP-HPLC: method parameters, chromatogram, main peak and impurity table.
8. Orthogonal purity method: method, result, and interpretation.
9. Impurity profile: relative retention, area percentage, tentative identification.
10. Counterion content: method and result.
11. Water content: Karl Fischer method and result.
12. Residual solvents: method and result, if applicable.
13. Net peptide content: method, result, and mass balance.
14. Stability or forced degradation summary, if the lot is intended for a longitudinal study.

A report missing items 4, 7, 9, 10, 11, or 13 is incomplete for procurement review. Items 5, 6, and 8 can be waived for a simple sequence, but the waiver should be documented.

## Common failures in review

Three patterns account for most rejected reports.

**The method is described but the data is missing.** A report lists a C18 column and a gradient but provides only a percentage, not the chromatogram. Without the trace, the reviewer cannot see peak shape, shoulders, or integration decisions.

**The mass is reported without the spectrum.** A single number cannot show whether the deconvolution was correct or whether multiple charge states were present. Ask for the raw spectrum and the deconvolution output.

**The impurity table sums to less than the main peak.** If the main peak is 98% and the listed impurities total 0.4%, the remaining 1.6% is unexplained. That gap may be small peaks below the integration threshold, or it may be an incomplete impurity profile. Ask which.

The [quality standards guide](/blog/research-peptide-quality-standards-2026-guide) lists acceptance criteria that can be written into a purchase order. The [reference standards guide](/blog/types-of-peptide-reference-standards-a-lab-guide) explains when a characterized standard is needed for quantification rather than identity. The [quality assurance process guide](/blog/peptide-quality-assurance-process-a-researchers-guide-to-sourcing-integrity) covers how those criteria fit into a release decision.

## The Author's Take

**Position:** A characterization report is a set of claims with a method attached to each one. If a claim has no method, it is not evidence. If a method has no raw data, it is not reviewable.

**Reasoning:** The most common procurement mistake is treating a certificate as a single score. A 98% purity line feels precise, so buyers stop reading. But the number is the least informative part of the report unless the chromatogram, the mass spectrum, and the mass balance are visible. I would rather receive a 96% lot with a complete impurity table and a net peptide content than a 99% lot with a one-line certificate. The first lot can be weighed and defended; the second is a number without a chain of evidence. The same logic applies to supplier qualification: ask for the report template before the first order, not after a failed assay.

**Disclosure:** Peptides of China sells research peptides. This article describes analytical reporting standards, not an effects claim. Products are supplied for research use only and are not for human or veterinary use.

## Sources

- European Medicines Agency. *ICH Q6B: Specifications — Test Procedures and Acceptance Criteria for Biotechnological/Biological Products.* https://database.ich.org/sites/default/files/Q6B%20Guideline.pdf
- European Medicines Agency. *ICH Q2(R2): Validation of Analytical Procedures.* https://www.ema.europa.eu/en/scientific-guidelines/ich-q2r2-validation-analytical-procedures
- U.S. Food and Drug Administration. *Bioanalytical Method Validation — Guidance for Industry.* https://www.fda.gov/regulatory-information/search-fda-guidance-documents/bioanalytical-method-validation-guidance-industry
- United States Pharmacopeia. *USP General Chapter <1058> Analytical Instrument Qualification.* https://www.usp.org/usp-nf
- Clinical and Laboratory Standards Institute. *EP05: Evaluation of Precision of Quantitative Measurement Procedures.* https://clsi.org/standards/products/method-evaluation/
- Bruckdorfer T, Marder O, Albericio F. *From production of peptides in milligram amounts for research to multi-tons quantities for drugs of the future.* Current Pharmaceutical Biotechnology 5(1): 29–43 (2004). https://doi.org/10.2174/1389201043489620
- *Comprehensive analysis of peptide pharmaceutical: development of three orthogonal chromatographic methods and characterization of impurities.* Journal of Pharmaceutical and Biomedical Analysis (2027). https://doi.org/10.1016/j.jpba.2026.117761
- *Improvement of analysis and transferability in peptide purification: from HPLC to FPLC and back again.* Journal of Peptide Science (2026). https://doi.org/10.1002/psc.70090
- Aebersold R, Mann M. *Mass spectrometry-based proteomics.* Nature 422: 198–207 (2003). https://pubmed.ncbi.nlm.nih.gov/12634793/
