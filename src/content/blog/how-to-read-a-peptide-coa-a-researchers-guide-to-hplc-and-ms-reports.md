---
title: "How to Read a Peptide COA: A Researcher's Guide to HPLC and MS Reports"
slug: "how-to-read-a-peptide-coa-a-researchers-guide-to-hplc-and-ms-reports"
description: "Read a peptide certificate of analysis in a fixed order: batch linkage, identity by mass, purity by HPLC, content basis, then any sterility or endotoxin claim. Includes worked examples and rejection rules."
---
A peptide certificate of analysis is read in a fixed order: batch linkage first, then identity, then purity, then content, then any claim about sterility or endotoxin. Every row should carry a method, a numeric result, units, and a specification. If one of those four is missing, the row is decorative. Most disputes about peptide quality are not disputes about chemistry; they are disputes about which number refers to which vial.

The document itself is usually one page. Reading it well takes about ten minutes and a calculator. This guide walks through the fields, the chromatogram, the mass spectrum, and the arithmetic that connects a purity percentage to the mass of peptide in the tube.

## The Four Questions a COA Must Answer

Before reading any result, establish what the document is claiming.

First, is it about the material you received? That requires a lot number on the vial that matches the lot number on the report, plus a product description specific enough to distinguish this peptide from a related one.

Second, what was measured? "Purity" and "assay" are different quantities. Purity describes the proportion of the target peak within the detected material. Assay describes how much of the labelled mass is the target substance. A certificate can report 99.0% purity and 78% assay without contradiction.

Third, how was it measured? The method determines the meaning of the number. An area percentage from a 280 nm run is not comparable to one from a 220 nm run. [HPLC and LC-MS answer different questions](/blog/hplc-vs-lc-ms-peptides/), and neither is a complete identity check on its own.

Fourth, does the result meet a stated limit? A result without an acceptance criterion is an observation, not a release decision.

A certificate that answers all four is usable. One that answers only the third and fourth is a marketing document with a laboratory header.

## COA Fields, Read in Order

| Field | Why it decides the reading | Common red flag |
| --- | --- | --- |
| Product name and sequence | Distinguishes the peptide from analogues and salt variants | Name only, no sequence or molecular formula |
| Lot or batch number | Ties the report to the physical container | Absent from the vial label |
| Manufacture date | Establishes the age of the material | Later than the test date |
| Test date | Establishes when the numbers were generated | More than 24 months before shipping |
| Issuing laboratory | Identifies who performed the work | Unnamed "QC department" |
| Method for each row | Determines what the result means | "HPLC" with no column or wavelength |
| Result with units | Allows comparison with the specification | Unitless percentages |
| Specification | Defines pass or fail | No limit stated |
| Analyst or approver | Provides attribution | No signature, no printed name |
| Retest or expiry date | Sets the usable window | Missing on a lyophilised product |

The dates deserve separate attention. A synthesis date, a purification date, a test date, and a report date should form a plausible sequence: synthesis before purification, purification before testing, testing before issue. When the test date precedes the synthesis date, the report was assembled from another batch or the dates were typed by hand.

## Reading the HPLC Section

An HPLC report has two parts: the chromatogram image and the integration table. Both matter.

On the chromatogram, the x-axis is time in minutes and the y-axis is absorbance in milli-absorbance units. The void volume of a 4.6 × 250 mm column at 1.0 mL/min arrives at roughly 2 to 3 minutes, so peaks before that point are usually solvent-related. The main peak should sit well clear of the injection front, with a baseline that returns to noise between peaks.

The integration table lists retention time, peak area, peak height, area percentage, and sometimes symmetry and resolution. A worked example: a main peak at 12.84 minutes with an area of 8,327 mAU·s, and total integrated area of 8,412 mAU·s, gives 99.0% by area. Three impurity peaks at 0.4%, 0.3%, and 0.3% account for the remainder. If the table lists only the main peak and reports 100%, the chromatogram was not integrated against anything, and the purity figure is meaningless.

Method conditions belong on the report, not in a separate document. Look for column dimensions and particle size, mobile phase composition, gradient program, flow rate, injection volume, detection wavelength, and run time. A typical peptide method uses a C18 column at 4.6 × 250 mm and 5 µm, 0.1% TFA in water and acetonitrile, a 5–65% gradient over 30 minutes, 1.0 mL/min, 20 µL injection, and 220 nm detection.

System suitability data separate a controlled run from a single injection. Six replicate injections of a [reference standard](/blog/types-of-peptide-reference-standards-a-lab-guide/) should give a peak-area RSD of ≤2.0% and a retention-time RSD of ≤1.0%. Resolution between the main peak and the nearest impurity should be at least 1.5, and symmetry should fall between 0.8 and 1.5. When those numbers are absent, the chromatogram is a picture rather than a measurement.

## Reading the Mass Spectrometry Section

Mass spectrometry answers the identity question that HPLC cannot. The report should show either a raw spectrum with charge states annotated or a deconvoluted mass with the software method stated.

For electrospray in positive mode, the observed m/z values follow a simple relationship: m/z = (M + zH) / z, where M is the neutral mass and z is the charge. [The charge-state arithmetic](/blog/peptide-molecular-weight-verification-steps/) is worth practising before reading a report, because the commonest error is treating an m/z value as a molecular weight. For BPC-157 at 1419.5 Da, the 2+ ion appears near m/z 710.8 and the 3+ ion near m/z 474.2. A report that labels a peak at 710.8 as "the molecular weight" has misread its own data; the molecular weight is 1419.5, and 710.8 is a doubly charged ion.

Tolerance should be stated with the result. Unit-resolution instruments commonly accept ±0.5 Da. High-resolution instruments at 60,000 resolution can hold ±5 ppm, which at 1419.5 Da is about ±0.007 Da. MALDI-TOF with a CHCA matrix usually lands within 0.1% of the expected mass. A mass reported as "1419" with no decimal place and no tolerance has thrown away the information needed to judge it.

Adducts are the most common false alarm. Sodium adds 21.98 Da and potassium adds 37.96 Da. A peak at 1441.5 next to a 1419.5 peak is the sodium adduct, not a second peptide. A peak at 1457.5 is the potassium adduct. Suppressing adducts with a small amount of formic acid or ammonium acetate in the mobile phase is normal practice, and their presence is not a defect.

Sequence information sits one level above mass. Tandem MS fragments the peptide along the backbone and produces b and y ion series. For a 15-mer, a partial series covering the termini is often enough to distinguish the target from a scrambled sequence with the same composition. A certificate that reports only a single mass confirms composition, not order.

| Evidence in the report | What it establishes | What it cannot establish | Cross-check |
| --- | --- | --- | --- |
| HPLC-UV area % at 220 nm | Proportion of detected material in the main peak | Identity; water and salt content | Impurity profile; peak resolution |
| ESI-MS charge envelope | Molecular mass within a stated tolerance | Purity; isobaric substitution | Theoretical mass calculation |
| MALDI-TOF mass | Molecular mass, often within 0.1% | Quantitative purity | Consistency with ESI result |
| MS/MS fragment series | Partial or full sequence coverage | Impurity levels | b/y ion assignment |
| Karl Fischer water | Water content of the powder | Residual organic solvents | Mass-balance calculation |
| Ion chromatography | Counterion identity and amount | Peptide content | Salt-form specification |
| LAL endotoxin | Endotoxin activity in EU/mg | Sterility | USP &lt;71&gt; sterility report |

## Units, Basis and the Purity-Content Gap

This is where most misreadings happen, and it is arithmetic rather than chemistry.

Area percent is not mass percent. A 99.0% area purity means that 99.0% of the integrated UV signal at 220 nm came from the main peak. It does not mean the vial is 99.0% peptide. Water, counterion, and residual solvents do not absorb at 220 nm and are excluded from the calculation by construction.

Net peptide content converts the analytical result into a mass. Take a 5 mg fill with 82% peptide content: the vial holds 4.1 mg of peptide. If an assay calls for 2 mg/mL in 2 mL, the requirement is 4.0 mg of peptide, so 4.88 mg of powder is needed, not 4.0 mg.

The salt form changes the conversion. An acetate salt carries 5–15% acetate by mass depending on the number of basic residues; a trifluoroacetate salt carries up to about 1% residual TFA after lyophilisation but a different total counterion mass. Peptide content by amino acid analysis accounts for all of it in one number, which is why that method is worth its cost on a large lot. Residual TFA is a separate line item, and [TFA removal](/blog/tfa-removal-peptides/) changes the mass balance without changing the chromatogram.

Basis is the other trap. Results reported "as is" include water; results reported "on the anhydrous basis" exclude it. The two are not interchangeable, and a certificate that does not state the basis cannot be compared with a specification written on the other one. A 95% "as is" result can correspond to 99% on an anhydrous basis when water sits at 4%.

## Batch Linkage and Document Forensics

A correct-looking certificate for the wrong batch is the failure mode that costs the most and shows the least.

Start with identifiers. The lot number should appear on the vial label, the certificate, and the packing list. Format should be consistent; a lot code that changes format between documents suggests a relabelled product. The product description should include the sequence or at least the molecular formula, because "BPC-157 5 mg" does not distinguish an acetate salt from a TFA salt.

Then look at the file itself. A PDF created three months after the stated test date, or edited a week before shipping, is worth a question. Font changes mid-table, misaligned rows, and a report identifier that appears on another product's certificate are all cheap to check.

The chromatogram offers a stronger test. Detector noise is random. Two reports with identical noise patterns, identical minor peak heights, and identical retention times to two decimal places are copies, not independent runs. Real replicate injections vary in the third decimal of retention time and in baseline shape.

Finally, ask for the raw data file. Suppliers with an in-house laboratory can usually export a .raw, .d, or CSV file. A supplier that cannot produce raw data for a batch it manufactured has a documentation chain that ends at the PDF. [Peptide documentation packages](/blog/peptide-documentation-package/) vary widely across the market, and the difference is usually visible at this step.

## Reject, Retest or Escalate

Three outcomes, three thresholds.

Reject when identity fails. A mass outside the stated tolerance, a missing charge envelope, or a sequence that does not match the label is a stop condition. Do not average a bad mass with a good purity figure.

Retest when a result is ambiguous. A purity of 97.4% against a 98.0% specification, a water result at 5.4%, or a chromatogram with an unintegrated shoulder all justify a second run before a decision. Retesting means three vials from the lot, the same method, and a second analyst where possible. A single repeat injection on the same vial tests the instrument, not the batch.

Escalate when the documentation is inconsistent but the material may be fine. A mismatched lot code, a missing method column, or a report with no signature is a supplier question first. Ask for the batch record, the raw chromatogram, and the certificate for the specific lot. A supplier that answers within a day with files usually has a real quality system; one that answers with a new certificate and no data usually does not.

The [BPC-157 COA walkthrough](/blog/bpc-157-certificate-of-analysis-explained-a-researchers-guide-to-verification-2026/) applies these rules to a single compound, and [why purity and concentration tests are not enough](/blog/why-purity-and-concentration-tests-are-not-enough/) covers the limits of the two numbers buyers rely on most.

## A Document Review Checklist

| Step | Document element | Pass condition |
| --- | --- | --- |
| 1 | Vial label versus certificate lot | Identical string, same format |
| 2 | Product description and sequence | Matches the ordered salt form and sequence |
| 3 | Date sequence | Synthesis ≤ purification ≤ test ≤ issue |
| 4 | Identity row | Mass within stated tolerance, charge states annotated |
| 5 | Purity row | Method, wavelength, and gradient stated; area ≥98.0% |
| 6 | Chromatogram | Baseline resolved; impurity peaks integrated and listed |
| 7 | Water and counterion | Within the salt-form specification |
| 8 | Content basis | "As is" or anhydrous stated explicitly |
| 9 | Endotoxin or sterility | Raw report present if the claim is made |
| 10 | Raw data availability | Chromatogram and spectrum files offered on request |

## The Author's Take

**Position.** Read the batch linkage before the chemistry. A perfect chromatogram attached to the wrong lot is worse than a mediocre chromatogram attached to the right one, because it creates false confidence.

**Reasoning.** The analytical methods used on peptide certificates are mature and well documented. What fails in practice is the chain between the instrument and the vial: relabelled lots, copied reports, missing method columns, and unit errors that survive because nobody multiplies the numbers out. A buyer who checks ten fields and does one calculation catches most of it in ten minutes. The remaining risk needs a laboratory, and that is a budget decision rather than a reading skill.

**Disclosure.** Peptides of China sells research peptides. This article is sourcing judgment, not an effects claim, and every compound discussed is for research use only.

## Sources

1. ICH Q2(R2), Validation of Analytical Procedures (2023). https://database.ich.org/sites/default/files/ICH_Q2%28R2%29_Guideline_2023_1130.pdf
2. FDA, Bioanalytical Method Validation: Guidance for Industry (2018). https://www.fda.gov/regulatory-information/search-fda-guidance-documents/bioanalytical-method-validation-guidance-industry
3. FDA, Analytical Procedures and Methods Validation for Drugs and Biologics (2015). https://www.fda.gov/regulatory-information/search-fda-guidance-documents/analytical-procedures-and-methods-validation-drugs-and-biologics
4. USP &lt;1058&gt;, Analytical Instrument Qualification. https://doi.org/10.31003/uspnf_m1124_10101_01
5. USP &lt;1225&gt;, Validation of Compendial Procedures. https://doi.org/10.31003/uspnf_m99945_40101_01
6. CLSI, Method Evaluation and Validation standards, including EP05 precision studies. https://clsi.org/standards/products/method-evaluation/
7. D'Hondt M, et al. Related impurities in peptide medicines. Journal of Pharmaceutical and Biomedical Analysis. 2014;101:2–30. https://doi.org/10.1016/j.jpba.2014.06.012
8. Fosgerau K, Hoffmann T. Peptide therapeutics: current status and future directions. Drug Discovery Today. 2015;20(1):122–128. https://doi.org/10.1016/j.drudis.2014.10.003
9. El-Faham A, Albericio F. Peptide coupling reagents, more than a letter soup. Chemical Reviews. 2011;111(11):6557–6602. https://doi.org/10.1021/cr100048w
