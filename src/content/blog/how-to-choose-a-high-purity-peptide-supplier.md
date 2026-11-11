---
title: "How to Choose a High-Purity Peptide Supplier"
slug: "how-to-choose-a-high-purity-peptide-supplier"
description: "A buyer's screen for high-purity peptide suppliers: lot-linked COAs, HPLC and LC-MS evidence, net peptide content, endotoxin data, and checkable facility claims."
---
A high-purity peptide supplier is one whose purity number can be traced to a specific lot, a named analytical method, and a chromatogram you are allowed to inspect. The headline percentage is the least useful part of the offer. Identity, net peptide content, counterion load, water content, and endotoxin are separate measurements, and a supplier that can discuss them separately is usually the one worth onboarding.

This guide gives buyers a screen that can be run before the first purchase order: six questions, the documents that answer them, the analytical methods behind each number, and the facility claims that survive a check. It is written for laboratory procurement and reseller sourcing, not for clinical use. Every compound discussed is for research use only.

## What a Purity Percentage Actually Measures

Reverse-phase HPLC reports the share of UV-absorbing signal assigned to the main peak. That is an area percentage, not a mass fraction. A lot can read 98.6% by area and still contain 82% peptide by mass once water, trifluoroacetic acid, and inorganic counterions are counted. For a 5 mg vial, the difference is 4.1 mg of peptide versus 5.0 mg, which propagates through every dilution in the study.

The detection wavelength matters as much as the number. At 214 nm, the peptide backbone absorbs strongly and many related impurities appear. At 280 nm, only aromatic residues respond, so a lot with no tryptophan or tyrosine can look cleaner than it is. A certificate that states "purity 99%" without a wavelength is not a measurement you can compare against another supplier's.

Method conditions decide comparability too. A typical peptide assay runs a C18 column at 4.6 × 250 mm, 5 µm particles, 0.1% TFA in water against acetonitrile, a 5–65% organic gradient over 30 minutes, 1.0 mL/min, 20 µL injection, and 220 nm detection. Change the gradient slope and the impurity profile changes with it. Two suppliers can both report 98% and mean different things.

## The Six-Question Supplier Screen

Ask these in writing before requesting a quote. The answers are more informative than a catalogue page, and evasions are data.

| # | Question | Acceptable answer | What a weak answer looks like |
| --- | --- | --- | --- |
| 1 | Which lot will ship, and can the COA carry the same lot string as the vial label? | Lot-specific COA with matching string and fill date | "COA available for the product" |
| 2 | Who performed the purity test, on which instrument? | Laboratory name, HPLC model, detector, asset number | "Our lab" with no instrument |
| 3 | What is the net peptide content, and how was it measured? | AAA or nitrogen determination with % w/w and method | Purity percentage repeated as content |
| 4 | What are water and counterion results? | Karl Fischer % w/w and ion chromatography % w/w | "Dry powder" and "TFA salt" with no values |
| 5 | Is endotoxin tested, by which format, and what is the result in EU/mg? | LAL method, limit, numeric result | "Endotoxin free" |
| 6 | Can raw chromatogram and spectrum files be shared under NDA? | Yes, with a named file format | "Not available" for an in-house lot |

Six questions, one reply. A supplier that answers four and promises the rest after deposit is telling you how the relationship will run.

## Documents That Separate a Manufacturer From a Reseller

The document set is a better predictor of supply reliability than the price list. A manufacturer with an in-house analytical unit can usually produce a batch record, a lot-specific certificate, a packing list, and a stability or retest statement. A trading company can produce a certificate it received, but often cannot explain which lot was sampled.

- **Batch production record.** Shows the synthesis run, purification fractions, fill step, and yield. Usually held by the manufacturer.
- **Lot-specific COA with method headers.** Records the tests performed on the shipped lot. Held by the manufacturer or its contract laboratory.
- **Raw chromatogram and mass spectrum.** The data behind the reported numbers. Available from a manufacturer or contract laboratory, sometimes under NDA.
- **Packing list with lot and fill mass.** Links the document to the box. Held by the manufacturer or distributor.
- **Stability and retest data.** The basis for the expiry or retest date. Usually held by the manufacturer.
- **Endotoxin and sterility reports.** Separate safety attributes, not purity. Held by the manufacturer or contract laboratory.
- **Safety data sheet.** Handling classification, not quality. Available from any legitimate seller.

The [documentation package comparison](/blog/peptide-documentation-package/) sets out what each supplier type can realistically provide. Ask for a redacted batch record rather than another certificate; the response sorts suppliers quickly.

## Analytical Methods: What Each Test Can and Cannot Prove

No single test covers quality. The table below maps the common methods to the question each one answers, the typical acceptance range, and the blind spot a buyer should know.

| Method | Question answered | Typical specification | Blind spot |
| --- | --- | --- | --- |
| RP-HPLC, 214–220 nm | How much UV signal is the main peak? | ≥95% area for research grade; ≥98% for stricter work | Does not identify the peptide or count non-UV mass |
| ESI-LC-MS | Is the mass consistent with the sequence? | ±0.5 Da unit resolution; ±5 ppm on HRMS | Cannot distinguish some isomers or quantify content |
| MALDI-TOF | Is the intact mass in the expected range? | Within 0.1% of theoretical mass | Adducts and matrix effects complicate interpretation |
| Karl Fischer | How much water is in the powder? | ≤5.0% w/w, often 1–3% after good lyophilisation | Sample handling can bias the result |
| Ion chromatography | How much counterion remains? | TFA ≤1.0% w/w; acetate varies with basic residues | Does not capture residual solvents |
| Amino acid analysis | What is the net peptide content? | 70–90% w/w for many lyophilised salts | Hydrolysis losses for some residues |
| LAL assay | How much endotoxin is present? | Report in EU/mg or EU/vial against a stated limit | Low-level inhibition or enhancement |
| USP &lt;71&gt; sterility | Is the lot free of viable organisms? | Pass/fail with method and incubation | Requires valid sampling and controls |

[HPLC and LC-MS answer different questions](/blog/hplc-vs-lc-ms-peptides/), and neither replaces content testing. A certificate with four methods is stronger than one with a single impressive percentage. For cell-based work, [endotoxin testing](/blog/endotoxin-testing-peptide-manufacturing/) is a separate method with its own sample handling and inhibition controls; a purity result says nothing about pyrogen load.

## Net Peptide Content: The Number That Changes Your Calculations

Net peptide content is the mass fraction of the intended peptide in the vial after water, counterions, and residual solvents are subtracted. For lyophilised TFA salts, 70–85% is common. An acetate salt can carry 5–15% acetate by mass depending on the number of basic residues. Water adds another 1–5% in a typical cycle, and residual solvents from purification add a smaller amount.

The practical consequence is simple. If a protocol calls for 2.0 mg of peptide and the lot is 80% net content, weighing 2.0 mg of powder delivers 1.6 mg of peptide. A 20% shortfall at the first weighing becomes a 20% error in every replicate. Suppliers who report net content, and state the method, remove that ambiguity. Those who repeat the HPLC purity figure as if it were content have not measured the right thing.

Amino acid analysis is the reference method for content. It hydrolyses the peptide, separates the amino acids, and compares the molar recovery against the theoretical composition. The [NIST comparison of peptide quantification methods](https://www.nist.gov/publications/survey-peptide-quantification-methods-and-their-reproducibility-comparison-case-study) shows why HPLC assay, quantitative NMR, and AAA do not always agree; each has a different basis. For procurement, the useful question is not which method is perfect but whether the supplier names one and applies it consistently across lots.

## Facility Claims: ISO 9001, ISO/IEC 17025, ISO 17034, and GMP

Four claims get mixed together in supplier decks. They mean different things, and only one of them is about laboratory competence.

- **ISO 9001** covers a quality management system. It does not establish analytical competence or product-specific testing. Check the certification body and the certificate scope.
- **ISO/IEC 17025** covers the competence of a testing or calibration laboratory. It does not cover manufacturing, and it applies only to the tests listed in the scope schedule. Check the accreditation body's public directory.
- **ISO 17034** covers the competence of a reference material producer. It does not cover routine lot release testing. Check the scope for the material type.
- **GMP (ICH Q7 or 21 CFR 210/211)** covers manufacturing controls, records, and release. Research-grade material sold without those controls is not GMP material, whatever the certificate says. Check the issuing authority, site address, and product scope.

ISO/IEC 17025 accreditation is granted for a defined scope. A laboratory accredited for water chemistry is not thereby accredited for peptide purity by HPLC. Ask for the accreditation body's name and certificate number, then look the laboratory up in the public directory rather than trusting a logo on a PDF. For GMP, ask which authority inspected which site and which product types are covered. A certificate without a site address is a brochure.

The [manufacturer verification protocol](/blog/china-peptide-manufacturer-verification-a-2026-b2b-sourcing-protocol/) covers the records and site checks behind these claims in more detail.

## Sample Handling and Lot Retention

Testing a single vial tells you about that vial. Fill heterogeneity within a lyophilisation run is real, and shipping stress can affect the cake. A workable receiving protocol takes three vials from the lot, photographs the labels and cake appearance, and stores them at −20 °C. One vial goes to the analytical laboratory, one is retained for retest, and one is kept sealed for reference.

Label the retained vials with the supplier lot, your internal sample ID, the receipt date, and the storage location. Do not rely on the supplier's label alone; it can fade or detach. If the material is divided into smaller containers, record the parent-child relationship so a later result can be tied back to the original lot.

For shipment, ask how the lot was held before dispatch. A certificate dated eighteen months before shipping describes material that has been in storage since testing. That is not automatically a problem, but the supplier should be able to state the storage condition and the retest basis. The [COA authentication guide](/blog/coa-verified-peptides-supplier-how-to-authenticate-research-purity-in-2026/) walks through the date sequence and the fields that expose a mismatch.

## Price, MOQ, and the Signals in a Quote

Price per milligram is a weak comparison unless the basis is the same. A quote for 5 mg at 95% purity, 70% net content, and no endotoxin data is not comparable to a 5 mg quote at 98% purity, 85% net content, and a lot-specific LAL report. Normalise to peptide mass and documentation before comparing.

Three signals matter more than the headline number. First, does the supplier quote different grades with different documentation, or one price with a generic certificate? Second, does the quote state fill mass, lot, lead time, and shipping terms in writing? Third, does the supplier accept a small paid sample before a bulk order? A supplier that will not sell a sample is usually a supplier that cannot control a lot.

Peptides of China works with a USD 600 product minimum and a USD 10 processing deposit credited toward the final invoice; current terms are on the [how sourcing works](/how-it-works/) page. Those numbers are commercial terms, not a quality claim. They matter because they set the point at which a sample-led evaluation becomes practical.

## A 30-Day Onboarding Sequence

A supplier can be evaluated without a full audit. The sequence below front-loads the cheap checks and leaves the expensive ones for after the documentation passes. It applies to any compound, from a widely traded peptide such as [BPC-157](/catalog/bpc-157/) to a custom sequence.

| Day | Action | Pass condition |
| --- | --- | --- |
| 1 | Request lot-specific COA, batch record outline, and instrument list | All three arrive, with lot string |
| 3 | Ask for raw chromatogram and spectrum for the quoted lot | Files or a dated NDA path |
| 5 | Order three vials, not one | Supplier accepts a sample order |
| 8 | Photograph labels, cake, and packing list; store at −20 °C | Lot strings match |
| 12 | Send one vial to a contract laboratory | Purity, identity, water, content within spec |
| 20 | Compare retest result with supplier COA | Differences explained, not dismissed |
| 25 | Request a redacted batch record and stability basis | Documents exist and agree |
| 30 | Decide: approve, approve with retest, or exit | Decision recorded with evidence |

If the supplier fails at day one, stop. If it passes day one and fails at day twelve, the problem is analytical control rather than paperwork. The distinction tells you whether to renegotiate or walk.

## Red Flags Worth Acting On

A single red flag is a question. Three together are a pattern. Watch for certificates that share a report number across products, purity values reported to 100.0% with a single peak, mass spectra labelled with m/z as molecular weight, endotoxin described only as "free", and a refusal to name the testing laboratory. None of these proves fraud, but each removes a check you would otherwise rely on.

The reverse is also true. A supplier that volunteers a method limitation, a failed system suitability run, or a lot that was reworked is giving you information a brochure never contains. Document those answers. Over several lots, the supplier's candour becomes the most useful specification you have.

## The Author's Take

**Position.** Choose the supplier whose paperwork survives an argument, not the one with the highest number on the landing page. Purity is easy to print and hard to verify; lot linkage, net content, and raw data are harder to fake and easier to check. A buyer who screens for those three things will reject some polished suppliers and keep some unglamorous ones, which is the right trade.

**Reasoning.** The analytical methods are mature and widely available. What varies is control: whether the tested sample matches the shipped vial, whether content is measured rather than assumed, and whether the supplier can produce the underlying files. Those questions can be answered before a bulk order with three vials and a contract laboratory. The cost of that screen is small compared with a failed study or a relabelled lot. Facility logos and brochure language do not change the arithmetic.

**Disclosure.** Peptides of China sells research peptides. This article is sourcing judgment, not an effects claim, and every compound discussed is for research use only. It is not medical advice and does not describe human use. Commercial terms referenced here are current at the time of writing and should be confirmed on the [how sourcing works](/how-it-works/) page.

## Sources

1. ISO/IEC 17025:2017, General requirements for the competence of testing and calibration laboratories. https://www.iso.org/standard/66912.html
2. ISO 17034:2016, General requirements for the competence of reference material producers. https://www.iso.org/standard/29357.html
3. ISO 9001:2015, Quality management systems — Requirements. https://www.iso.org/standard/62085.html
4. ICH Q2(R2), Validation of Analytical Procedures (2023). https://database.ich.org/sites/default/files/ICH_Q2%28R2%29_Guideline_2023_1130.pdf
5. ICH Q6A, Specifications: Test Procedures and Acceptance Criteria for New Drug Substances and New Drug Products (1999). https://database.ich.org/sites/default/files/Q6A%20Guideline.pdf
6. ICH Q7, Good Manufacturing Practice Guide for Active Pharmaceutical Ingredients (2000). https://database.ich.org/sites/default/files/Q7%20Guideline.pdf
7. FDA, Analytical Procedures and Methods Validation for Drugs and Biologics (2015). https://www.fda.gov/regulatory-information/search-fda-guidance-documents/analytical-procedures-and-methods-validation-drugs-and-biologics
8. FDA, Pyrogen and Endotoxins Testing: Questions and Answers (2012). https://www.fda.gov/regulatory-information/search-fda-guidance-documents/pyrogen-and-endotoxins-testing-questions-and-answers
9. 21 CFR 211.160, General requirements for laboratory controls. https://www.ecfr.gov/current/title-21/chapter-I/subchapter-C/part-211/subpart-I/section-211.160
10. D'Hondt M, et al. Related impurities in peptide medicines. Journal of Pharmaceutical and Biomedical Analysis. 2014;101:2–30. https://doi.org/10.1016/j.jpba.2014.06.012
