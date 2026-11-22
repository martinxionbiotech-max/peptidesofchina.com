---
title: "Research Peptide Sourcing and Verification"
slug: "research-peptides-an-operational-guide-to-sourcing-and-verification-in-2026"
description: "A procurement workflow for research peptides: specification fields, entity checks, lot-linked HPLC and MS review, receiving tests, and document reconciliation."
author: "POC Tech Team"
updated: "2026-11-22"
---
A verified research-peptide purchase is a chain of four matches: the specification matches the assay, the purchase order matches the specification, the certificate matches the vial label, and your receiving result matches the certificate. Break one link and the vial is unverified, however professional the folder looks.

This guide sets out that chain as an operating procedure for laboratory procurement. It covers the fields to fix before a quote, the entity checks that separate a manufacturer from a storefront, the four claims inside a certificate of analysis, and the receiving tests that decide whether a lot enters inventory. It is written for research purchasing, not clinical supply or personal use.

## The four matches that define verification

Most sourcing failures are not analytical failures. They are documentation failures that only become visible when someone compares two records that should agree.

| Match | Records compared | Typical failure |
| --- | --- | --- |
| 1. Specification to assay | Purchase brief versus method used by the supplier | Purity quoted by a method the assay cannot tolerate |
| 2. Order to specification | PO line versus approved brief | Substituted salt form, fill mass, or kit configuration |
| 3. Certificate to vial | COA lot string versus label and packing list | Certificate belongs to a different lot or an older run |
| 4. Receiving result to certificate | In-house or contract-lab result versus supplier values | Result outside the stated uncertainty, or a method mismatch |

The sequence matters. A buyer who starts with the certificate is auditing a document. A buyer who starts with the specification is auditing a material. The document only becomes evidence when it is tied to the material by a lot string and a sampling record.

## Write the specification before the quotation

A catalog name is not a specification. "BPC-157 10 mg" leaves the counterion, purity basis, peptide content, water limit, and storage condition unresolved. Two suppliers can quote those three words and ship materials that behave differently in the same assay.

Put these fields in a numbered brief and attach it to the RFQ:

1. Compound name and full amino acid sequence, including terminal modifications.
2. Salt or counterion form: acetate, trifluoroacetate, hydrochloride, or another declared form.
3. Presentation: milligrams per vial, vials per kit, and fill mass with a tolerance. A ±2% fill tolerance is a practical starting point for a manual fill line.
4. Purity basis: chromatographic method, column, mobile phase, gradient, wavelength, and integration rule.
5. Net peptide content basis: amino acid analysis, nitrogen determination, or another named method.
6. Water content limit, usually by Karl Fischer titration.
7. Residual counterion and solvent limits that matter to the assay.
8. Endotoxin and sterility requirements, stated as separate attributes.
9. Storage and shipping condition, with a temperature range and a excursion policy.
10. Documents required at delivery and the acceptance tests the buyer will run.

Add a version number and a date. When a method or limit changes, keep the old version in the procurement file so the change is visible. The [peptide documentation package](/blog/peptide-documentation-package/) checklist maps each document to the question it answers, which helps when a supplier offers a standard pack that does not match your brief.

Two fields deserve more attention than they usually get. Purity without a wavelength is not comparable across suppliers: a sample read at 214 nm and one read at 280 nm can report different percentages for the same lot. Net content without a method is not a measurement: a supplier that repeats the HPLC purity figure as "content" has not measured the mass fraction of peptide in the vial.

## Qualify the legal entity, not the storefront

Before price, establish who is responsible for the batch. Ask five questions in writing:

1. What is the legal name and registered address of the entity that will invoice us?
2. Which site synthesized, purified, and filled the lot?
3. Which organization released the batch, and who signed the certificate?
4. If you are not the manufacturer, what written authorization do you have to share the manufacturer's records?
5. Which quality system covers the site, and what is the certificate number and scope?

A trading company is not automatically a bad supplier. An intermediary that states its role and can obtain lot-linked records is easier to work with than a manufacturer that cannot answer a technical question. The disqualifying signal is an unclear role: an invoice from one entity, a certificate from a second, and a shipping label from a third, with no explanation of how they relate.

Certification claims need the same treatment. ISO 9001 covers a quality management system, not analytical competence. ISO/IEC 17025 covers a testing laboratory for the tests listed in its scope schedule; a laboratory accredited for water chemistry is not thereby accredited for peptide purity by HPLC. Check the accreditation body's public directory and the certificate scope, not the logo on a PDF. The [manufacturer verification protocol](/blog/china-peptide-manufacturer-verification-a-2026-b2b-sourcing-protocol/) sets out the records and site checks behind these claims.

## Read the COA as four separate claims

A certificate of analysis is easier to audit when it is split into four questions. Each one uses a different method and carries a different blind spot.

| Claim | Method | What it establishes | Blind spot |
| --- | --- | --- | --- |
| Identity | ESI-LC-MS or MALDI-TOF | The intact mass is consistent with the stated sequence | Does not distinguish some isomers or quantify content |
| Purity | RP-HPLC, usually 214 or 220 nm | The share of UV signal assigned to the main peak | Area percent is not mass fraction |
| Content | Amino acid analysis, nitrogen determination, or qNMR | Mass of peptide per mass of powder | Hydrolysis losses and method-specific bias |
| Safety attributes | LAL endotoxin, USP &lt;71&gt; sterility, KF water | Pyrogen load, viable organisms, residual water | Each test covers only its own attribute |

A typical peptide assay runs a C18 column at 4.6 × 250 mm with 5 µm particles, 0.1% trifluoroacetic acid in water against acetonitrile, a 5–65% organic gradient over 30 minutes, 1.0 mL/min, a 20 µL injection, and detection at 214 or 220 nm. Change the gradient slope and the impurity profile changes with it. Two suppliers can both report 98% and mean different things.

Mass accuracy is a property of the platform. A MALDI-TOF result within ±1 Da and a Q-TOF result within 5 ppm can both be correct; they are not evidence of different quality. What matters is that the certificate states the theoretical mass, the observed mass, the mass mode (monoisotopic or average), the instrument model, and the tolerance. The [COA reading guide](/blog/how-to-read-a-peptide-coa-a-researchers-guide-to-hplc-and-ms-reports/) walks through the field-by-field comparison, and the [HPLC versus LC-MS comparison](/blog/hplc-vs-lc-ms-peptides/) explains why neither method covers the other's question.

Content is the number that changes bench calculations. Lyophilized TFA salts commonly run 70–90% peptide by mass once water, counterion, and residual solvent are subtracted. If a protocol calls for 2.0 mg of peptide and the lot is 80% net content, weighing 2.0 mg of powder delivers 1.6 mg of peptide. That 20% shortfall propagates through every dilution. Ask for the content value and the method, not a repeat of the purity percentage.

Safety attributes are separate tests with separate sample handling. Endotoxin is reported in EU/mg or EU/vial against a stated limit; "endotoxin free" is not a result. Sterility is a pass/fail method with an incubation period, typically 14 days under USP &lt;71&gt;. The [endotoxin testing guide](/blog/endotoxin-testing-peptide-manufacturing/) covers inhibition and enhancement controls, which decide whether a low reading is real.

## Set acceptance criteria you can measure

Release criteria belong in the specification; receiving criteria belong in your own SOP. They can be the same tests, but the decision rules should be written before the first vial arrives.

| Test | Method | Suggested release limit | Receiving action |
| --- | --- | --- | --- |
| Identity | LC-MS or MALDI-TOF | Within stated mass accuracy of theoretical | Repeat at higher resolution if outside |
| Purity | RP-HPLC, 214–220 nm | ≥95% area for research grade; ≥98% for stricter work | Compare against baseline lot at same method |
| Net peptide content | AAA or nitrogen determination | Report % w/w and method; 70–90% common for TFA salts | Recalculate weighing; do not assume 100% |
| Water | Karl Fischer | ≤5.0% w/w | Check cake appearance and storage history |
| Counterion | Ion chromatography | TFA ≤1.0% w/w; acetate varies with basic residues | Flag if the assay is pH-sensitive |
| Endotoxin | LAL | Report EU/mg against a stated limit | Retest with inhibition control if near limit |
| Sterility | USP &lt;71&gt; | Pass, with method and incubation stated | Quarantine until result is available |
| Appearance | Visual inspection | White to off-white cake or powder, no discoloration | Photograph and compare with reference |

Receiving sampling is part of the criterion. Take three vials from the lot, photograph the labels and cake, and store them at −20 °C. Send one to the analytical laboratory, retain one for retest, and keep one sealed as a reference. Label each with the supplier lot, your internal sample ID, the receipt date, and the storage location. Do not rely on the supplier label alone; it can fade or detach in transit.

If the material is divided into smaller containers, record the parent-child relationship. A later result must be traceable to the original lot, not just to the aliquot in the freezer. The [molecular weight verification workflow](/blog/peptide-molecular-weight-verification-steps/) gives the mass-mode arithmetic that prevents a false failure when comparing a supplier's MALDI result with your own high-resolution data.

## Receiving inspection: label, cake, temperature, retain

The receiving bench is the last point where a mismatch can be caught cheaply. Record five things before the vials go into storage:

- **Label fields.** Product name, lot string, fill mass, storage condition, and any expiry or retest date.
- **Packaging condition.** Outer box, cold-chain indicator, data logger, and whether the gel packs were still within their working range.
- **Cake appearance.** Uniform plug or powder, no shrinkage, melting, or discoloration. A collapsed cake is not automatically a failed lot, but it is a question for the supplier.
- **Document set.** Packing list, certificate, and any deviation note. Check that the lot string on all three agrees.
- **Receipt record.** Date, time, carrier, ambient temperature, and the person who opened the package.

A temperature excursion is a risk event, not a rejection by itself. Ask the supplier for the stability basis that covers the excursion, and quarantine the lot until the analytical result is available. For lyophilized material, the relevant question is whether the cake absorbed moisture during the excursion; a Karl Fischer result on the receiving sample answers it.

## Reconcile documents and close the loop

Document reconciliation is a comparison exercise, not a reading exercise. Put the purchase order, certificate, packing list, and label side by side and check the following:

1. **Lot string.** Exact character match across all four records.
2. **Report number and date.** The test date should fall after the manufacture date and before the ship date.
3. **Instrument and method.** The certificate should name the instrument class and the method conditions, not just the result.
4. **Signature and release.** A named signatory or a release stamp, with the laboratory's identity.
5. **File integrity.** Native PDF, consistent fonts, no pasted-in result blocks, and metadata that matches the document date.

When a value differs, ask for a corrected certificate rather than accepting a handwritten change. When your own result differs from the certificate, repeat the injection before rejecting the lot. Sample preparation, column age, and integration settings account for more discrepancies than synthesis failures. If the repeat agrees with your first result, run an orthogonal method before escalating. A single out-of-spec result is a question; two independent methods that agree are a finding.

## When to reject a lot

Rejection is a commercial decision, but it should be triggered by technical evidence. Five objective triggers are enough for most research purchasing:

- Identity outside the stated mass tolerance on two independent methods.
- Purity below the specification by more than the method's repeatability, confirmed on a repeat injection.
- Net peptide content far below the declared value, making the weighed mass impossible to reconstruct.
- Endotoxin above the stated limit, or a sterility failure on a lot intended for cell work.
- A lot string that cannot be tied to the shipped vials, or a certificate that belongs to an earlier run.

Document the rejection with photographs, analytical results, and the correspondence. Keep the retain vials until the claim is closed; they are the only physical evidence of the lot you received. A supplier that answers a rejection with a batch record extract and a deviation summary is behaving like a manufacturer. A supplier that answers with a replacement offer and no explanation is telling you how the next rejection will be handled.

## The Author's Take

**Position.** The most useful verification step is not the third-party test; it is the specification. A buyer who defines identity, purity basis, content basis, water, and counterion before the quote gets documents that can be compared. A buyer who orders from a catalog and tests afterward is running an audit with no acceptance criteria, which is how good-looking certificates end up attached to the wrong lot.

**Reasoning.** Analytical methods are mature and widely available. What varies is control: whether the tested sample matches the shipped vial, whether content is measured rather than assumed, and whether the supplier can produce the underlying files. Those questions can be answered before a bulk order with three vials and a contract laboratory. The cost of that screen is small compared with a failed study or a relabelled lot. Facility logos and brochure language do not change the arithmetic.

**Disclosure.** Peptides of China sells research peptides. This article is sourcing and documentation judgment, not an effects claim. Products are supplied for laboratory research use only and are not for human or veterinary use. Commercial terms referenced here are current at the time of writing and should be confirmed on the [how sourcing works](/how-it-works/) page.

## Sources

1. ICH Q7, Good Manufacturing Practice Guide for Active Pharmaceutical Ingredients (2000). https://database.ich.org/sites/default/files/Q7%20Guideline.pdf
2. ICH Q6A, Specifications: Test Procedures and Acceptance Criteria for New Drug Substances and New Drug Products (1999). https://database.ich.org/sites/default/files/Q6A%20Guideline.pdf
3. ICH Q2(R2), Validation of Analytical Procedures (2023). https://database.ich.org/sites/default/files/ICH_Q2%28R2%29_Guideline_2023_1130.pdf
4. FDA, Analytical Procedures and Methods Validation for Drugs and Biologics (2015). https://www.fda.gov/regulatory-information/search-fda-guidance-documents/analytical-procedures-and-methods-validation-drugs-and-biologics
5. FDA, Pyrogen and Endotoxins Testing: Questions and Answers (2012). https://www.fda.gov/regulatory-information/search-fda-guidance-documents/pyrogen-and-endotoxins-testing-questions-and-answers
6. 21 CFR 211.84, Testing and approval or rejection of components, drug product containers, and closures. https://www.ecfr.gov/current/title-21/chapter-I/subchapter-C/part-211/subpart-E/section-211.84
7. 21 CFR 211.160, General requirements for laboratory controls. https://www.ecfr.gov/current/title-21/chapter-I/subchapter-C/part-211/subpart-I/section-211.160
8. ISO/IEC 17025:2017, General requirements for the competence of testing and calibration laboratories. https://www.iso.org/standard/66912.html
9. D'Hondt M, et al. Related impurities in peptide medicines. Journal of Pharmaceutical and Biomedical Analysis. 2014;101:2–30. https://doi.org/10.1016/j.jpba.2014.06.012
10. NIST, Survey of peptide quantification methods and their reproducibility. https://www.nist.gov/publications/survey-peptide-quantification-methods-and-their-reproducibility-comparison-case-study
