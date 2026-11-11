---
title: "Amino Acid Composition Analysis: What It Adds to Peptide QC"
slug: "amino-acid-composition-analysis-benefits"
description: "AAA measures net peptide content and composition when HPLC and MS cannot. Learn hydrolysis, separation, calculations, and acceptance limits."
---
Amino acid composition analysis (AAA) is the test that tells you how much peptide is actually in the vial. HPLC reports a purity percentage, mass spectrometry confirms identity, and neither measures the mass fraction of the intended molecule after water, counterions, and residual solvents. AAA hydrolyses the peptide into its constituent amino acids, quantifies them, and reconstructs the peptide mass from the composition. That reconstructed value is net peptide content, usually expressed as % w/w.

The test earns its place in three situations: concentration-critical work where a systematic error would bias every replicate, comparability studies where two lots or two suppliers must be shown to match, and supplier qualification when a new source has little documentation history. This guide covers the hydrolysis chemistry, the separation options, the calculation, the acceptance criteria, and the limits of the method. All material discussed is for research use only.

## What AAA Measures, and What It Does Not

AAA measures the molar composition of a peptide after complete hydrolysis. The result is a set of amino acid recoveries, normally in nanomoles or micrograms, which are compared with the theoretical composition. From that comparison, the laboratory calculates net peptide content and can flag a composition that does not match the expected sequence.

AAA does not determine sequence order. It cannot tell whether a glycine sits at position 3 or position 12. It does not measure impurity profile, counterion identity, water content, or endotoxin. It is a composition and content method, not a purity method. A peptide can pass AAA and still contain a closely related deletion analogue that hydrolyses to the same amino acid ratios.

The method also struggles with certain residues. Tryptophan is destroyed by acid hydrolysis. Cysteine and cystine require oxidation before hydrolysis. Glutamine and asparagine deamidate to glutamate and aspartate under the standard conditions, so the measured Glu/Asp value combines the original residues and their deamidated forms. These are known limitations, and a competent laboratory will state how it handled them.

## The Hydrolysis Step

The standard approach uses 6 N hydrochloric acid at 110 °C for 24 hours in a sealed, evacuated tube. The vacuum removes oxygen, which limits oxidative loss of sensitive residues. Vapour-phase hydrolysis, where the sample sits above the acid rather than in it, reduces contamination and is common in pharmacopoeial work.

The conditions are a compromise. A 24-hour hydrolysis is long enough to release most residues from sterically hindered bonds but long enough to destroy tryptophan completely and to cause partial losses of serine, threonine, and cysteine. A 48-hour hydrolysis improves recovery of some hydrophobic residues but increases losses of others. Many laboratories run a single 24-hour hydrolysis and apply correction factors, while others run two time points and extrapolate to zero.

Sample preparation matters. Use a known amount of peptide, typically 1–5 mg, and add an internal standard such as norleucine before hydrolysis. The internal standard corrects for injection volume and derivatisation efficiency. If the peptide contains norleucine, choose a different standard. For a formulated product, remove excipients that would interfere with the separation, or validate that they do not.

Cysteine needs a separate preparation. Performic acid oxidation converts cysteine and cystine to cysteic acid before hydrolysis, which is stable under the acid conditions. Tryptophan requires an alkaline hydrolysis or a separate spectrophotometric method. A report that lists tryptophan without stating the method used has probably assumed a value rather than measured one.

## Separation and Detection Options

Three platform families dominate. Ion-exchange chromatography with post-column ninhydrin detection is the classical pharmacopoeial approach and remains a reference method. Reverse-phase HPLC with pre-column derivatisation, using OPA, FMOC, PITC, or AccQ-Tag chemistry, is common in contract laboratories because it uses standard HPLC equipment. HILIC coupled to mass spectrometry is increasingly used for isotope dilution work because it provides structural information and low detection limits.

| Platform | Detection | Strength | Limitation |
| --- | --- | --- | --- |
| Ion-exchange | Post-column ninhydrin | Mature, pharmacopoeial, good for complex mixtures | Long run times; dedicated instrument |
| RP-HPLC, pre-column derivatisation | UV or fluorescence | Widely available; good sensitivity | Derivatisation variability; reagent stability |
| HILIC-MS | Mass spectrometry | Specific; isotope dilution possible | Requires MS expertise; matrix effects |

The choice affects the acceptance criteria. A ninhydrin method may report 2–5% relative standard deviation for well-behaved residues, while a derivatisation method can drift if the reagent ages. An isotope dilution MS method can achieve better precision but costs more per sample. For supplier qualification, the method matters less than consistency: the same platform should be used across lots if the results are to be compared.

The [HPLC and LC-MS comparison](/blog/hplc-vs-lc-ms-peptides/) explains why a separation method and a mass method answer different questions. AAA sits alongside them as a third, composition-based measurement.

## Calculating Net Peptide Content

The calculation starts with the measured molar amount of each amino acid. Multiply each by its residue mass, sum the residue masses, add one water molecule for the free peptide termini, and divide by the sample mass. The result is the mass of peptide in the sample. Express it as a percentage of the weighed sample to get net peptide content.

A worked example: a 10.0 mg sample is hydrolysed, and the recoveries reconstruct to 8.15 mg of peptide. Net content is 81.5% w/w. A 5 mg fill of that lot contains 4.08 mg of peptide, not 5.00 mg. If the protocol calls for a 2.0 mg/mL solution prepared from a 5 mg vial, the actual concentration will be 1.63 mg/mL unless the content is corrected.

The arithmetic is simple; the analytical inputs are not. The laboratory needs a calibrated amino acid standard, a validated hydrolysis procedure, and a clear decision on how to treat partially degraded residues. A report that gives a single content percentage without the underlying recoveries is difficult to audit. Ask for the amino acid table, the standard curve, and the hydrolysis conditions.

The [molecular weight verification guide](/blog/peptide-molecular-weight-verification-steps/) covers the identity side of the same calculation. Mass spectrometry confirms the expected mass; AAA confirms that the amino acid building blocks are present in the expected ratio and gives the mass fraction.

## Method Performance and Acceptance Criteria

AAA is less precise than HPLC purity. A well-run laboratory can hold 2–5% RSD for stable residues and 5–10% for labile ones. That precision is adequate for content, where a 5% error is usually acceptable, but not for trace impurity profiling.

| Parameter | Typical expectation | Notes |
| --- | --- | --- |
| Accuracy | Within ±5% of the theoretical content for a qualified standard | Depends on hydrolysis recovery |
| Precision | 2–5% RSD for stable residues | Higher for Ser, Thr, Cys, Trp |
| Linearity | Calibration across the working range | Amino acid standard mixture |
| Limit of quantitation | Low nanomole range for fluorescence or MS | Matrix-dependent |
| Content acceptance | 75–90% w/w for many lyophilised salts | Method and salt form matter |
| Lot-to-lot consistency | Within ±5% of the approved value | Set before comparing lots |

The acceptance range for content should be set from the product specification, not copied from another peptide. A TFA salt with a high counterion load may legitimately sit at 75–80% content. An acetate salt of a different peptide may sit at 85–90%. The number is meaningful only when the method and the salt form are stated.

## Where AAA Fits in Supplier Qualification

AAA is most useful when a new supplier's certificate is thin. Purity by HPLC can be replicated by any contract laboratory, but content requires a hydrolysis and a calibrated standard, which is a higher bar. A supplier that can provide AAA data, and explain the hydrolysis conditions, is more likely to control its process than one that reports only a chromatogram.

Use AAA at three points. First, on the first lot from a new supplier, alongside identity and purity. Second, on a comparator lot from the incumbent supplier, so the two can be compared on the same basis. Third, at intervals during routine supply, especially when the fill size or the salt form changes. A content shift of more than 5% between lots is a signal to investigate, even if both certificates are within specification.

Write the requirement into the quality agreement. State the method, the sample size, the acceptance range, and the action to take if a result falls outside it. A clause that says "COA required" without naming the content test leaves the supplier free to report purity only. The [documentation package guide](/blog/peptide-documentation-package/) lists the fields that belong in that agreement.

## Complementary Methods

AAA is one measurement in a panel. The table below shows where it sits relative to the other tests a buyer is likely to request.

| Question | Method | What AAA adds |
| --- | --- | --- |
| Is the sequence correct? | LC-MS/MS or intact mass | Composition confirmation, not order |
| How clean is the lot? | RP-HPLC at 214–220 nm | Nothing; AAA is not an impurity method |
| How much peptide is present? | AAA or nitrogen determination | Direct measurement of content |
| How much water is present? | Karl Fischer | AAA does not measure water |
| What counterion is present? | Ion chromatography | AAA does not measure counterions |
| Is endotoxin present? | LAL assay | Nothing; separate safety method |

A certificate with HPLC, LC-MS, Karl Fischer, ion chromatography, and AAA covers identity, purity, water, counterion, and content. That is a coherent release panel for a research peptide. Endotoxin and sterility are added when the use requires them. The [testing and analysis guide](/blog/peptide-testing-and-analysis-a-professional-guide-to-laboratory-verification/) describes the full workflow.

Salt form affects the calculation. A TFA salt carries residual TFA that is counted in the sample mass but not in the peptide mass. The [TFA removal guide](/blog/tfa-removal-peptides/) explains why a salt conversion changes the content value even when the peptide is unchanged. If the supplier switches from TFA to acetate without telling the buyer, the AAA result will move and the purity result may not.

## Operational Checklist for Ordering AAA

A useful request pack has five items: the sample mass, the expected sequence and composition, the salt form, the hydrolysis conditions the laboratory will use, and the acceptance range. Ask for the amino acid recovery table, not just the final percentage. Ask whether the laboratory ran a duplicate hydrolysis, and how it handled tryptophan and cysteine.

Turnaround is typically one to three weeks depending on the laboratory and the need for special hydrolysis. Cost is modest compared with a failed study, but the test is not a substitute for a full panel. For a first lot, run AAA alongside HPLC, LC-MS, Karl Fischer, and ion chromatography. For a routine reorder, AAA can be run less often if the supplier's process and salt form are stable.

For a representative peptide with a well-characterised composition, the [semaglutide catalogue entry](/catalog/semaglutide/) shows the presentation and specification fields a buyer would compare. Current order terms are on the [how sourcing works](/how-it-works/) page.

## The Author's Take

**Position.** AAA is the most under-used test in peptide procurement. Buyers argue about 98% versus 99% purity, then prepare solutions from a vial that contains 78% peptide. The content number changes the experiment; the purity difference often does not. If a laboratory can afford only one additional test beyond HPLC and MS, AAA is usually the better buy.

**Reasoning.** Purity is a relative signal. Content is an absolute mass. Every dilution, every concentration, and every comparison across lots depends on the absolute value, and the error is systematic rather than random. AAA also provides a composition check that catches some mixing and substitution problems that a single HPLC peak will not. It is not a sequence method and it is not precise enough for trace work, but it closes the mass-balance gap that HPLC leaves open.

**Disclosure.** Peptides of China sells research peptides. This article is analytical and sourcing judgment, not an effects claim, and every compound discussed is for research use only. It is not medical advice and does not describe human use.

## Sources

1. NIST, Survey of peptide quantification methods and their reproducibility: a case study. https://www.nist.gov/publications/survey-peptide-quantification-methods-and-their-reproducibility-comparison-case-study
2. Koller M, et al. Amino acid analysis for pharmacopoeial purposes. Talanta. 2016;154:150–163. https://doi.org/10.1016/j.talanta.2016.03.071
3. Analysis of Polypeptides by Amino Acid Analysis. Methods in Molecular Biology. 2024;2821:71–82. https://doi.org/10.1007/978-1-0716-3914-6_6
4. Amino Acid Analysis by Hydrophilic Interaction Chromatography Coupled with Isotope Dilution Mass Spectrometry. Methods in Molecular Biology. 2019;2030:111–118. https://doi.org/10.1007/978-1-4939-9639-1_9
5. ICH Q2(R2), Validation of Analytical Procedures (2023). https://database.ich.org/sites/default/files/ICH_Q2%28R2%29_Guideline_2023_1130.pdf
6. ICH Q6A, Specifications: Test Procedures and Acceptance Criteria for New Drug Substances and New Drug Products (1999). https://database.ich.org/sites/default/files/Q6A%20Guideline.pdf
7. FDA, Analytical Procedures and Methods Validation for Drugs and Biologics (2015). https://www.fda.gov/regulatory-information/search-fda-guidance-documents/analytical-procedures-and-methods-validation-drugs-and-biologics
8. 21 CFR 211.160, General requirements for laboratory controls. https://www.ecfr.gov/current/title-21/chapter-I/subchapter-C/part-211/subpart-I/section-211.160
9. ISO/IEC 17025:2017, General requirements for the competence of testing and calibration laboratories. https://www.iso.org/standard/66912.html
10. D'Hondt M, et al. Related impurities in peptide medicines. Journal of Pharmaceutical and Biomedical Analysis. 2014;101:2–30. https://doi.org/10.1016/j.jpba.2014.06.012
