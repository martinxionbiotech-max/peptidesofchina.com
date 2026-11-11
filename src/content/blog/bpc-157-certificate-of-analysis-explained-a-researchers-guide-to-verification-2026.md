---
title: "BPC-157 Certificate of Analysis: How to Verify a Lot in 2026"
slug: "bpc-157-certificate-of-analysis-explained-a-researchers-guide-to-verification-2026"
description: "Read a BPC-157 COA line by line: lot linkage, HPLC integration, ESI-MS charge states, water and counterion results, net peptide content, and endotoxin limits."
---
A BPC-157 certificate of analysis is a lot-specific record, not a product brochure. It should connect the vial in your hand to a tested sample, name the method and instrument behind each number, and report identity, purity, water, counterion, content, and endotoxin as separate results. If any of those links is missing, the document cannot tell you what is in the vial.

BPC-157 is a fifteen-residue synthetic peptide, sequence GEPPPGKPADDAGLV, with a monoisotopic mass near 1419.5 Da. That size is easy to synthesise and easy to mischaracterise: a single deletion, an extra glycine, or a missed deprotection changes the mass by enough to matter but not always by enough to be obvious on a low-resolution instrument. This guide walks through the fields that decide a review, with worked examples. The numbers below are illustrative, not results for a Peptides of China lot.

## Identity, Purity, and Content Are Three Different Questions

The most common reading error is collapsing three measurements into one percentage. Identity asks whether the analytical evidence supports the claimed sequence. Purity describes the relative UV signal of components separated by a particular method. Content asks how much of the intended peptide is present on a defined mass basis.

A lot can be 99% pure by HPLC area and still contain 80% peptide by mass. It can also be 99% pure and be the wrong sequence, because a co-eluting analogue with a similar retention time will integrate as one peak. Mass spectrometry addresses identity; amino acid analysis addresses content; neither is a purity test. The [field-by-field COA guide](/blog/how-to-read-a-peptide-coa-a-researchers-guide-to-hplc-and-ms-reports/) covers the general document; this page applies it to BPC-157.

| Question | Method that answers it | Result format | What it cannot tell you |
| --- | --- | --- | --- |
| Is this BPC-157? | ESI-LC-MS or MALDI-TOF, with charge states or sequence coverage | Mass spectrum with tolerance | Purity or quantity |
| How clean is the lot? | RP-HPLC at 214–220 nm with full integration | Area % table and chromatogram | Identity or net content |
| How much peptide is in the vial? | Amino acid analysis or nitrogen determination | % w/w net content | Impurity profile |
| Is it safe for cell work? | LAL endotoxin assay, sterility by USP &lt;71&gt; where claimed | EU/mg and pass/fail | Chemical purity |

## Lot Linkage Comes Before Chemistry

Start with the identifier string. The lot number on the vial label, the certificate, and the packing list should match character for character. Format drift can be a typing convention, but it can also be a relabelled product. Ask which record is authoritative and whether the batch record shows the same string.

Then read the dates as a sequence: synthesis, purification, test, report issue. A test date before synthesis is impossible. A report issued three months after testing is ordinary. A certificate created a week before shipping, for a lot tested two years earlier, raises a storage question that the supplier should answer.

Fill mass belongs in the linkage check. One certificate covering 5 mg and 10 mg vials describes the bulk material, not each fill. That is acceptable when the certificate says so and states the fill mass. It is not acceptable when it implies every vial was individually tested. For BPC-157, where 5 mg and 10 mg presentations are common, this distinction appears often.

Ask for the batch record rather than another certificate. It shows the synthesis run, the purification fractions pooled, the fill step, and the yield. A manufacturer with in-house production usually has one and will share a redacted copy. A reseller frequently does not, which is itself a useful answer. The [documentation package comparison](/blog/peptide-documentation-package/) explains what each supplier type can supply.

## Reading the HPLC Section

A usable BPC-157 HPLC report includes the column, dimensions, particle size, mobile phase, gradient, flow rate, injection volume, detection wavelength, run time, and integration table. A typical method uses a C18 column at 4.6 × 250 mm and 5 µm, 0.1% TFA in water and acetonitrile, a 5–65% organic gradient over 30 minutes, 1.0 mL/min, a 20 µL injection, and 220 nm detection.

The integration table should list every peak with retention time, area, area %, and height. A worked example: the main peak at 12.84 minutes has an area of 8,327 mAU·s against a total integrated area of 8,412 mAU·s, giving 99.0% by area. Three impurities at 0.4%, 0.3%, and 0.3% account for the remainder. If the table lists only the main peak and reports 100.0%, the chromatogram was not integrated against anything and the figure carries no information.

System suitability separates a controlled run from a single injection. Six replicate injections should hold peak-area RSD at ≤2.0% and retention-time RSD at ≤1.0%, with resolution of at least 1.5 to the nearest impurity and peak symmetry between 0.8 and 1.5. A report that omits suitability data may still be valid, but you cannot tell whether the run was in control.

Wavelength deserves a second look. At 220 nm, the peptide bond absorbs and most related impurities appear. At 280 nm, only aromatic residues respond; BPC-157 contains no tryptophan and no tyrosine, so a 280 nm run is close to blind to the molecule. A certificate quoting a 280 nm purity for BPC-157 has a method problem, not a purity result.

## Reading the Mass Spectrum

Mass spectrometry answers a narrower question than most buyers assume: is the measured mass consistent with the proposed structure? For BPC-157, the monoisotopic mass is approximately 1419.5 Da. Unit-resolution LC-MS commonly accepts ±0.5 Da; a high-resolution instrument at 60,000 resolution can hold ±5 ppm, which at this mass is roughly ±0.007 Da.

Charge states belong on the report. For BPC-157 at 1419.5 Da, the [M+2H]2+ ion sits near m/z 710.8 and the [M+3H]3+ ion near m/z 474.2. A certificate that labels 710.8 as the molecular weight has misread its own spectrum. Sodium adducts add 21.98 Da and potassium adducts add 37.96 Da, so a signal at 1441.5 is the sodium adduct, not a second peptide.

Sequence coverage is stronger evidence than an intact mass. Tandem MS fragments the peptide and assigns b- and y-ions across the chain. A report that shows coverage of the N-terminal, middle, and C-terminal regions is harder to forge than a single intact mass, and it catches deletion analogues that share a similar mass. For a 15-mer, full coverage is achievable on a routine instrument. The [molecular weight verification guide](/blog/peptide-molecular-weight-verification-steps/) explains the arithmetic in more detail.

## Water, Counterion, and Net Peptide Content

A lyophilised BPC-157 vial is not pure peptide. It contains water, residual trifluoroacetic acid or acetate, and possibly residual solvents from purification. Each is measured separately, and together they determine how much peptide a milligram of powder actually contains.

Karl Fischer titration, coulometric for 50–100 mg samples, commonly specifies ≤5.0% w/w water, with well-controlled cycles landing at 1–3%. Ion chromatography quantifies the counterion: residual TFA is usually held to ≤1.0% w/w, while an acetate salt carries 5–15% acetate by mass depending on the number of basic residues. BPC-157 has several basic residues, so the counterion load is not trivial.

Amino acid analysis gives net peptide content. Hydrolyse the sample, separate the amino acids, and compare molar recovery against the theoretical composition. For many lyophilised BPC-157 salts, 75–90% w/w is a realistic range. A 5 mg fill at 82% content holds 4.1 mg of peptide, not 5.0 mg. That gap propagates through every dilution downstream, which is why content belongs on the certificate rather than in a footnote.

The choice of salt also affects handling. TFA salts are common in research peptides and can be hygroscopic; acetate salts behave differently in aqueous solution. The [TFA removal guide](/blog/tfa-removal-peptides/) covers the trade-offs.

## Endotoxin and Sterility Fields

Endotoxin is a separate attribute with its own method. The LAL assay reports in EU/mg or EU/vial against a stated limit. For cell-based work, a common internal limit is below 1 EU/mg, but the right limit depends on the assay and the positive control. A certificate that says "endotoxin free" without a method, a limit, and a numeric result has not reported anything usable.

Sterility is separate again. USP &lt;71&gt; requires a validated method, appropriate media, and incubation controls. A "sterile" claim on a research peptide certificate should be backed by a report, not a filtration statement. If the supplier did not run the test, the claim should be removed rather than softened.

Both attributes are lot-specific. A sterility report for a bulk lot does not automatically cover a later fill, and an endotoxin result for one vial does not establish homogeneity across the run. Ask how many vials were sampled and whether the sample was taken before or after fill.

## A BPC-157 COA Checklist

| Field | Acceptable entry | Red flag |
| --- | --- | --- |
| Product identity | BPC-157, sequence GEPPPGKPADDAGLV, formula and salt form | Name only, no sequence or counterion |
| Lot linkage | Same lot string on vial, COA, and packing list | Certificate lot appears nowhere else |
| Date sequence | Synthesis ≤ purification ≤ test ≤ report | Test date before synthesis |
| HPLC method | Column, gradient, flow, injection, wavelength, run time | "HPLC" with no conditions |
| Purity integration | Full peak table with areas and area % | Single peak reported as 100.0% |
| Mass identity | Charge states annotated, or deconvoluted mass with tolerance | m/z labelled as molecular weight |
| Water | Karl Fischer result in % w/w with limit | Absent on a lyophilised powder |
| Counterion | Identity and % w/w by ion chromatography | "TFA salt" with no measured value |
| Net content | AAA result in % w/w with method | Purity percentage repeated as content |
| Endotoxin | LAL format, limit, numeric EU/mg | "Endotoxin free" |
| Sterility | USP &lt;71&gt; report or no claim | "Sterile" with no report |
| Release | Analyst, reviewer, signature, date | Blank signature block |

Twelve rows is a low bar. Most certificates pass six or seven.

## How Reused and Template COAs Fail

A template certificate usually fails on linkage rather than chemistry. The same report number appears for two products, the lot string is generic, or the dates are internally impossible. A reused certificate is harder to spot: the document is genuine, but it belongs to another batch.

Three checks catch most cases. First, compare the certificate's lot string with the vial label and the packing list. Second, ask for the raw chromatogram file and check that its acquisition date matches the test date. Third, ask for the batch record and see whether the fill date precedes the shipping date. A supplier that can produce all three has a chain; one that cannot has a document.

Chemical inconsistencies also show up. A BPC-157 certificate reporting a 280 nm purity, a molecular weight of 710.8, or a single peak at 100.0% is describing something other than a clean run. None of these proves fraud, but each removes a check you would otherwise rely on. The [COA authentication protocol](/blog/coa-verified-peptides-supplier-how-to-authenticate-research-purity-in-2026/) sets out the supplier-side questions.

## When to Commission Independent Testing

Desk review catches documentation gaps. It does not catch a well-forged certificate or a genuine certificate for a substituted lot. Independent testing answers that when the stakes justify the cost.

Commission it for a new supplier's first order, for a lot expensive enough that a failed experiment matters, for any discrepancy found during desk review, and for material intended for published or audited work. Routine reorders from a supplier with a consistent record rarely need a full panel.

A workable BPC-157 panel covers purity by RP-HPLC at 220 nm, identity by ESI-MS with charge states, water by Karl Fischer, counterion by ion chromatography, and net content by amino acid analysis. Add LAL endotoxin for cell-based work, and MS/MS sequencing if the sequence is in question. Send three vials from the lot, not one, and retain a fourth at −20 °C for retest. Code samples by lot, not by supplier name; blinding costs nothing and removes a category of bias.

The [HPLC and LC-MS comparison](/blog/hplc-vs-lc-ms-peptides/) explains why the two methods are not interchangeable. For a compound as widely traded as [BPC-157](/catalog/bpc-157/), independent data is often the only way to distinguish a controlled lot from a relabelled one.

## The Author's Take

**Position.** A BPC-157 certificate is worth reading backwards: start with the lot string, then the dates, then the raw data, and only then the purity number. If the first three agree, the chemistry is usually worth checking. If they do not, the chemistry is irrelevant. Buyers who reverse that order tend to pay for a document rather than a lot.

**Reasoning.** BPC-157 is small enough to synthesise almost anywhere and common enough that certificates get copied. The analytical methods are standard; the failure mode is attribution, not technique. A 99% peak attached to the wrong vial is worse than an 97% peak attached to the right one, because it creates false confidence. The checks that resolve attribution are cheap: label photographs, date arithmetic, a raw file request, and one contract laboratory run on three vials. None of them requires a site visit.

**Disclosure.** Peptides of China sells research peptides. This article is sourcing judgment, not an effects claim, and BPC-157 is discussed for research use only. It is not medical advice and does not describe human use. Commercial terms are stated on the [how sourcing works](/how-it-works/) page.

## Sources

1. NIST, Survey of peptide quantification methods and their reproducibility: a case study. https://www.nist.gov/publications/survey-peptide-quantification-methods-and-their-reproducibility-comparison-case-study
2. ICH Q2(R2), Validation of Analytical Procedures (2023). https://database.ich.org/sites/default/files/ICH_Q2%28R2%29_Guideline_2023_1130.pdf
3. ICH Q6A, Specifications: Test Procedures and Acceptance Criteria for New Drug Substances and New Drug Products (1999). https://database.ich.org/sites/default/files/Q6A%20Guideline.pdf
4. FDA, Analytical Procedures and Methods Validation for Drugs and Biologics (2015). https://www.fda.gov/regulatory-information/search-fda-guidance-documents/analytical-procedures-and-methods-validation-drugs-and-biologics
5. FDA, Pyrogen and Endotoxins Testing: Questions and Answers (2012). https://www.fda.gov/regulatory-information/search-fda-guidance-documents/pyrogen-and-endotoxins-testing-questions-and-answers
6. 21 CFR 211.194, Laboratory records. https://www.ecfr.gov/current/title-21/chapter-I/subchapter-C/part-211/subpart-J/section-211.194
7. D'Hondt M, et al. Related impurities in peptide medicines. Journal of Pharmaceutical and Biomedical Analysis. 2014;101:2–30. https://doi.org/10.1016/j.jpba.2014.06.012
8. Sikiric P, et al. Stable Gastric Pentadecapeptide BPC 157 and Striated, Smooth, and Heart Muscle. Biomedicines. 2022;10(12):3221. https://doi.org/10.3390/biomedicines10123221
9. Sikiric P, et al. Stable Gastric Pentadecapeptide BPC 157 as Therapy After Surgical Detachment of the Quadriceps Muscle from Its Attachments for Muscle-to-Bone Reattachment in Rats. Pharmaceutics. 2025;17(1):119. https://doi.org/10.3390/pharmaceutics17010119
10. ISO/IEC 17025:2017, General requirements for the competence of testing and calibration laboratories. https://www.iso.org/standard/66912.html
