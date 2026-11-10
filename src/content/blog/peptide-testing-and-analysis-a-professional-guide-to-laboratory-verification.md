---
title: "Peptide Testing and Analysis: A Lab Verification Guide"
slug: "peptide-testing-and-analysis-a-professional-guide-to-laboratory-verification"
description: "How to commission peptide testing: lab accreditation scope, sampling, method validation, report fields, and retest triggers for batch verification."
---
**Laboratory verification answers one question: does this specific batch match the specification you agreed to, as measured by a method you can defend?** Everything else — the certificate layout, the accreditation logo, the reputation of the lab — is supporting detail. A test result is only useful if the sample came from the vial you received, the method was fit for that material, and the report states enough for another analyst to reconstruct the run.

Most sourcing disputes do not start because a laboratory lied. They start because the buyer and the supplier were measuring different things, or because a sample was pooled, or because a purity number was compared across two methods that were never equivalent. This guide covers the operational side of peptide testing: what to ask a laboratory, how to sample, which validation parameters matter, and when a result should trigger a retest rather than a decision.

For the chemistry behind the numbers, the [HPLC versus LC-MS comparison](/blog/hplc-vs-lc-ms-peptides/) covers separation and detection, the [COA reading guide](/blog/how-to-read-a-peptide-coa-a-researchers-guide-to-hplc-and-ms-reports/) covers report structure, and the [quality testing pillar](/peptide-quality-testing/) collects the wider method set. This page stays on commissioning and evidence.

## What Verification Has to Answer

A verification program closes four gaps between a supplier's claim and your evidence.

The first gap is **identity**. A label says BPC-157; the vial contains a peptide with the right mass. That is necessary but not sufficient, because mass alone does not distinguish sequence isomers or modifications with the same formula.

The second is **purity**. The chromatogram shows what fraction of the detected material elutes as the target peak under a stated method. It does not show what the other fraction is unless the method resolves it and the report lists it.

The third is **content**. A 10 mg vial may contain 10 mg of peptide, or 10 mg of peptide plus counterion and moisture, or 8.6 mg of peptide with the balance being trifluoroacetate and water. Content is a mass-balance question, not a chromatography question.

The fourth is **fitness for the intended work**: endotoxin, sterility, bioburden, counterion identity. None is implied by a purity percentage, and none is interchangeable with another.

The most common analytical mistake in peptide procurement is letting one method stand in for another. The table below maps each question to the method that actually answers it, and to the method that is often substituted by mistake.

| Question | Method that answers it | Common but inadequate substitute |
|---|---|---|
| Is the molecular mass correct? | ESI-LC-MS with deconvolution, 5 ppm tolerance | HPLC retention time against a reference |
| Is the sequence correct? | LC-MS/MS with b/y ion coverage, or Edman degradation | Mass match alone |
| How much of the detected material is target? | RP-HPLC-UV area percent at 214 nm, stated integration threshold | A supplier's "≥98%" claim with no chromatogram |
| How much peptide is in the vial? | Quantitative assay plus Karl Fischer water and counterion content | Area percent converted to mass by assumption |
| Is the material sterile? | USP &lt;71&gt; sterility test, 14-day incubation | Filtration claim with no post-fill test |
| Is endotoxin controlled? | LAL or rFC with spike recovery and a numeric limit | "Endotoxin free" with no method or value |

Each row is a distinct purchase decision. A batch can pass identity and fail content, or pass both and still carry endotoxin above a study's tolerance. Verification means deciding which rows matter for your use, then requiring evidence for those rows and no others.

## Sampling and Chain of Custody Decide the Result

A laboratory can only test what arrives at its bench. If the sample is not representative, the report is precise and wrong.

**Sample size.** A 1–2 mg aliquot from a 5 mg vial supports HPLC, MS, and a Karl Fischer replicate with material left for a retest. Taking the whole vial destroys the retained lot and leaves nothing to re-test if a result is disputed.

**Sampling method.** Lyophilized peptide cakes can stratify. Sampling from the top of a cake while the bottom holds more counterion is a real risk in large vials. Reconstitute the full vial, mix, and split the solution, or sample multiple vials from the same lot and report each result separately.

**Chain of custody.** The record should carry the lot number, the date and time of sampling, the sampler, the storage condition in transit, and the seal number. A report that cannot be tied to that record proves something about a sample, not your batch.

**Storage in transit.** Most lyophilized peptides ship at ambient temperature for a few days without degradation. Reconstituted solutions do not, so a solution sample should ship cold and be tested on arrival.

## Accreditation Scope Beats the Logo

ISO/IEC 17025:2017 is the international standard for the competence of testing and calibration laboratories. An accredited laboratory has been assessed against it by an accreditation body, and that body is usually a signatory to the ILAC Mutual Recognition Arrangement. The logo on a report is evidence that a quality system exists. It is not evidence that the specific test you ordered sits inside the accredited scope.

Ask for the scope document and read the method list. A lab accredited for water testing and heavy metals may run peptide HPLC as a non-accredited service. That does not make the result false, but it changes how much weight the report carries in a supplier qualification file or an audit.

Two further distinctions matter. A laboratory accredited to ISO/IEC 17025 is not the same as a reference material producer accredited to ISO 17034. If your method depends on a certified reference standard, its producer should hold the second accreditation, and the certificate should state the assigned value, uncertainty, and expiry.

Independent testing also has a structural meaning. A lab owned by the supplier, or paid by the supplier under a standing contract, is not independent in the sense that matters for dispute resolution. Independence is about who can influence the result, not about whether the invoice is itemised.

## Method Validation: The Six Parameters to Read

ICH Q2(R2) sets out the validation characteristics an analytical procedure should demonstrate. For peptide testing, six of them decide whether a report is usable.

**Specificity.** Can the method separate the target from likely impurities? For a peptide, that means resolution from deletion sequences, oxidized species, and diastereomers. A gradient that runs 5–95% acetonitrile in 10 minutes compresses those species into the main peak. A 5–65% gradient over 30 minutes spreads them out.

**Linearity and range.** Does the detector response track concentration across the working range? For UV area percent, linearity is less critical than for a quantitative assay, but a content assay by HPLC or amino acid analysis needs a calibration curve with documented correlation and residual limits.

**Accuracy.** How close is the measured value to the true value? For a purity method, accuracy is hard to establish without a reference standard, which is why many peptide labs report relative purity and a separate content assay. For endotoxin, accuracy is demonstrated by spike recovery.

**Precision.** Repeatability on the same day and intermediate precision across days or analysts. A common acceptance criterion for injection replicates is a relative standard deviation of 2.0% or less. For content assays, 2–5% RSD is typical depending on the method.

**Detection and quantitation limits.** The reporting threshold determines the purity number. A method that integrates down to 0.01% area will report a lower purity than one that stops at 0.5%. Neither is fraudulent, but the two numbers cannot be compared, and the threshold belongs in the method description.

**Ruggedness.** Does the result survive small changes in column lot, mobile phase pH, temperature, and flow? A method that fails when the column is swapped is not transferable, and a supplier's number from such a method cannot be reproduced by your lab.

| Parameter | What to ask for | Typical peptide expectation |
|---|---|---|
| Specificity | Chromatogram with impurity peaks labelled | Resolution ≥ 2.0 from nearest impurity |
| Linearity | Calibration range and r² | r² ≥ 0.99 across 50–150% of target |
| Accuracy | Recovery or reference standard comparison | 80–120% recovery for content assays |
| Precision | Repeatability and intermediate precision | RSD ≤ 2.0% for replicate injections |
| LOD / LOQ | Signal-to-noise basis and reporting threshold | LOQ ≤ 0.05% area for impurity reporting |
| Ruggedness | Deliberate variation results | No change in pass/fail outcome |

A report that lists results without any of these parameters is a measurement, not a validated method. That is acceptable for a quick incoming check and unacceptable for a supplier qualification, which is the distinction the [supplier COA verification guide](/blog/coa-verified-peptides-supplier-how-to-authenticate-research-purity-in-2026/) builds on.

## Matching the Method to the Material

Method choice should follow the peptide, not the lab's default template.

**Hydrophobic sequences.** Highly hydrophobic peptides can precipitate on a C18 column or elute late in a broad peak. A wider gradient, higher column temperature, or a different organic modifier may be needed. A lab that runs every peptide on the same 15-minute method will produce uninterpretable chromatograms for these sequences.

**Basic and cationic peptides.** Arginine-rich sequences interact with residual silanols and tail badly at neutral pH. Trifluoroacetic acid at 0.1% in the mobile phase improves peak shape by ion pairing, but it also means the reported purity describes the trifluoroacetate salt, not the free peptide.

**Cysteine-containing peptides.** Disulfide formation, free thiol oxidation, and dimerization change both mass and retention. A single mass peak at the monomer mass does not exclude a mixed disulfide unless the sample was prepared under non-reducing conditions and the chromatogram shows the dimer region.

**Modified and cyclic peptides.** Mass alone cannot localize a modification or confirm a cyclization site. MS/MS with adequate backbone coverage, or a targeted approach such as enzymatic digestion followed by LC-MS, is required. A 5 ppm mass match on a cyclic peptide with a lactam bridge tells you the composition, not the connectivity.

**Small peptides under 1 kDa.** Matrix effects and adduct formation are more prominent, and a deconvoluted mass may show multiple salt adducts. The report should state which adduct was used for the mass assignment.

## Reading the Report Against Your Specification

The specification is the document you agreed to before testing. The report is the evidence. Verification is the comparison, and it should be mechanical rather than impressionistic.

Start with identifiers: product name, lot number, sample description, date received, date tested, method reference, and analyst. If the lot on the report does not match the lot on the vial, stop. Nothing downstream can repair that.

Then read the results table against each specification line. A specification of "purity ≥ 98.0% by RP-HPLC at 214 nm" is only satisfied by a result generated under that method. A 99.1% result from a 280 nm method is not the same measurement, and the difference is not in your favour when the peptide lacks aromatic residues.

Then read the chromatogram. Look for baseline drift, peak shape, the number of integrated peaks, and whether the impurity table accounts for the area not assigned to the main peak. A purity of 98.5% implies 1.5% of integrated area belongs to other peaks. If the impurity table lists 0.2% total, either the integration threshold is hiding peaks or the numbers do not reconcile.

Then read the mass spectrum against the theoretical value, using the arithmetic set out in the [molecular weight verification guide](/blog/peptide-molecular-weight-verification-steps/). The deconvoluted mass should be within the stated tolerance. Check the charge states, the adduct pattern, and whether the reported mass corresponds to the free peptide or a salt form. A 113.99 Da offset is a trifluoroacetate adduct; a 21.98 Da offset is a sodium adduct. Neither is an identity failure, but both change the interpretation.

Finally, check the units. Purity in area percent, content in mass percent, water in percent by Karl Fischer, endotoxin in EU/mg or EU/mL. A number without a unit is not a result, and [a purity figure is not a content figure](/blog/why-purity-and-concentration-tests-are-not-enough/).

## Retest Triggers, Cost, and Turnaround

Not every out-of-specification result means the batch is bad. Some mean the sample was bad, the method was wrong for the material, or the specification was written for a different salt form. A written decision rule prevents ad hoc responses.

| Trigger | First action | What it usually means |
|---|---|---|
| Purity 1–2 points below spec | Repeat injection from the same sample | Integration or column condition, not batch quality |
| Purity more than 3 points below spec | Retest a second vial from the same lot | Batch heterogeneity or a genuine purity gap |
| Mass off by a small integer adduct | Check adduct assignment and sample preparation | Salt form or ionisation artefact |
| Mass off by a residue mass | Request MS/MS and compare with sequence | Deletion or substitution impurity |
| Endotoxin above limit with low spike recovery | Repeat with dilution and valid spike recovery | Assay interference, not necessarily contamination |
| Two labs disagree by more than 2% | Compare methods line by line before re-testing | Method mismatch more often than lab error |

The rule that saves the most money is the simplest: before re-testing, compare methods. Two labs using different gradients or integration thresholds will produce different purity numbers on the same vial.

Cost follows method time, not sample count. An HPLC-UV purity run is inexpensive because the instrument runs overnight on an autosampler. LC-MS/MS with sequence interpretation costs more, because it consumes instrument time and analyst review. Method development for a new or modified peptide costs more again.

Turnaround follows the same logic. A standard panel of HPLC, MS1, water content, and appearance can return in three to five working days at a commercial lab. MS/MS with manual interpretation, sterility testing with a 14-day incubation, or method development can push the timeline to two or three weeks. If a supplier promises a full panel with MS/MS and sterility in 48 hours, the timeline is the claim to question first.

For routine incoming checks, a tiered approach controls cost. Run HPLC-UV and MS1 on every lot. Add MS/MS, content assay, and counterion analysis on the first lot from a supplier, on any lot intended for a long study, and on any lot where the routine panel shows an anomaly. The [characterization reporting checklist](/blog/peptide-characterization-reporting-checklist/) sets out the full data package for the higher tier.

## Building a Verification File That Survives an Audit

A verification file is not a folder of PDFs. It is a structured record that lets someone who was not present reconstruct what was decided and why.

At minimum, it should contain: the purchase specification, the supplier's certificate for the lot, the independent laboratory report with raw data, the sampling record, the chain-of-custody form, the deviation and retest log, and the disposition decision. Each document should carry the same lot identifier.

Retention matters: lyophilized peptide held at −20 °C in a sealed vial is stable for years for most sequences, which makes a retained sample practical. Keep at least one unopened vial per lot for the retention period your quality system defines, record the storage location, and file the paperwork as described in the [documentation package checklist](/blog/peptide-documentation-package/). If a study fails eighteen months later, the retained vial is the only way to test whether the material changed or the result was always there.

Data integrity expectations apply to small buyers too. The MHRA GxP guidance and 21 CFR Part 11 describe the standard for electronic records: attributable, legible, contemporaneous, original, and accurate. A laboratory that provides only a summary PDF, with no chromatogram file or audit trail, is providing a conclusion rather than data. For a file that supports a regulatory submission, that gap is disqualifying.

## The Author's Take

**Position.** Buyers should commission testing from a laboratory whose accredited scope names the method they need, and should refuse to treat an ISO logo as a substitute for that scope document. The second rule is equally firm: never compare purity numbers from two labs without comparing their methods first.

**Reasoning.** Peptide purity by HPLC is a relative measurement. It depends on wavelength, gradient, column, integration threshold, and sample preparation. Two competent laboratories can report 97.8% and 99.2% for the same vial without either being wrong, because they measured different things. Buyers who treat those numbers as a single scale end up disqualifying good suppliers and retaining bad ones. Accreditation scope closes a different gap: it tells you whether anyone outside the laboratory has examined the method. A lab running your assay outside its scope may still be competent, but in a dispute that absence is what the other side will point to.

**Disclosure.** Peptides of China sells research peptides. This article describes testing and procurement practice; it is not an effects claim, a dosing guide, or medical advice. Products referenced on this site are supplied for laboratory research use only. Analytical documentation varies by product and batch, and buyers who need independent verification should arrange third-party testing after receipt.

## Sources

- ISO/IEC 17025:2017 General requirements for the competence of testing and calibration laboratories. International Organization for Standardization. [iso.org/standard/66912.html](https://www.iso.org/standard/66912.html)
- ILAC Mutual Recognition Arrangement. International Laboratory Accreditation Cooperation. [ilac.org](https://ilac.org/)
- ICH Q2(R2) Validation of Analytical Procedures (2023). International Council for Harmonisation. [database.ich.org](https://database.ich.org/sites/default/files/ICH_Q2%28R2%29_Guideline_2023_1130.pdf)
- USP &lt;621&gt; Chromatography. United States Pharmacopeia. [usp.org/usp-nf](https://www.usp.org/usp-nf)
- USP &lt;85&gt; Bacterial Endotoxins Test. United States Pharmacopeia. [usp.org/usp-nf](https://www.usp.org/usp-nf)
- FDA Guidance for Industry: Bioanalytical Method Validation (2018). U.S. Food and Drug Administration. [fda.gov](https://www.fda.gov/regulatory-information/search-fda-guidance-documents/bioanalytical-method-validation-guidance-industry)
- 21 CFR Part 211 Current Good Manufacturing Practice for Finished Pharmaceuticals. Electronic Code of Federal Regulations. [ecfr.gov](https://www.ecfr.gov/current/title-21/chapter-I/subchapter-C/part-211)
- ISO 17034:2016 General requirements for the competence of reference material producers. International Organization for Standardization. [iso.org/standard/29357.html](https://www.iso.org/standard/29357.html)
- Guideline on bioanalytical method validation. European Medicines Agency. [ema.europa.eu](https://www.ema.europa.eu/en/documents/scientific-guideline/guideline-bioanalytical-method-validation_en.pdf)
