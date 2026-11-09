---
title: "Tirzepatide Wholesale Sourcing: 2026 B2B Guide"
slug: "tirzepatide-wholesale-sourcing-a-2026-b2b-procurement-guide"
description: "A procurement file for tirzepatide research material: identity data, acceptance limits, batch records, supplier vetting, receipt testing, and landed cost."
---
Tirzepatide wholesale sourcing is a documentation exercise before it is a purchasing one. The buyer needs to establish three things in order: that the material is the intended 39-residue peptide, that the batch record connects the vial to a defined manufacturing event, and that the commercial terms define what happens when a result misses the specification. A supplier's price list answers none of those questions.

This guide is for laboratory procurement teams buying research-use-only tirzepatide. It does not discuss approved medicines, dosing, administration, or therapeutic use. It also does not assume that a certificate is true because it is signed. The method here is to make each claim checkable.

Wholesale means a quantity large enough to justify a specification, not a quantity large enough to skip one. At catalog scale, a buyer can treat a purchase as a sample and accept more uncertainty. At wholesale scale, the same uncertainty is multiplied across every vial in the lot and every downstream experiment that uses it.

Three claims need separate evidence.

**Identity.** The material is the intended molecule, not a related analogue, a truncated sequence, or a different salt. Identity is a structure question, and it is answered by mass and fragmentation data, not by a product name.

**Purity and content.** The target peak is the stated proportion of the detected material, and the vial contains the stated mass of peptide after water and counterion are accounted for. These are two numbers, not one.

**Traceability.** The certificate, the vial label, the packing list, and the batch record refer to the same lot. A perfect analysis of a different batch is not evidence about the material in the box.

A supplier can be strong on one claim and weak on another. The procurement file exists to stop a strong certificate from hiding a weak traceability chain.

## The Identity File: 39 Residues and One Mass

Tirzepatide is a 39-amino-acid peptide engineered as a dual GIP and GLP-1 receptor agonist. Its free-base molecular formula is C225H348N48O68, and the molecular weight is approximately 4813.45 Da. The CAS registry number used for the research material is 2023788-19-2. Those three identifiers are the minimum identity header for a batch record.

The molecule also carries a fatty acid side chain and non-natural residues that distinguish it from a native GIP sequence. A supplier should be able to state the modifications in the sequence field rather than the trade name alone. If the certificate says "Tirzepatide" and nothing else, the buyer cannot tell whether the batch is the 39-residue analogue or a related peptide with a similar label.

Mass spectrometry is the first check. For electrospray in positive mode, m/z = (M + zH) / z. At a neutral mass of 4813.45 Da, the 4+ envelope is centred near m/z 1204, the 5+ near 964, and the 6+ near 803. A report should annotate the charge states rather than print a single peak and call it the molecular weight.

Tolerance must be stated. A unit-resolution instrument may accept ±0.5 Da; a high-resolution run at 60,000 resolution can hold ±5 ppm, which at 4813.45 Da is about ±0.024 Da. MALDI-TOF with a CHCA matrix often lands within 0.1%. Without a tolerance, the result cannot be accepted or rejected, only admired.

Mass alone confirms composition, not sequence order. Tandem MS produces b and y ion series that cover the backbone. For a 39-residue peptide, full de novo coverage is uncommon on a routine release certificate, but partial terminal coverage plus the expected mass shift from the side chain is enough to distinguish the target from a scrambled sequence of the same composition. Ask for the fragment table if the project depends on sequence confirmation, not just mass.

## Write the Acceptance Specification

A specification is a set of limits with methods attached. The following template is deliberately explicit; adjust the numeric limits to the project, but do not delete the method column.

| Attribute | Example specification | Method |
| --- | --- | --- |
| Identity | 4813.45 Da, within stated tolerance | ESI-LC-MS, positive mode |
| Sequence confirmation | Terminal b/y coverage consistent with the stated sequence | MS/MS |
| Purity | ≥98.0% area of the main peak | RP-HPLC, C18, 220 nm |
| Water | ≤5.0% w/w | Karl Fischer |
| Counterion | Stated identity and amount | Ion chromatography |
| Net peptide content | Report value and basis; project minimum | Mass balance |
| Endotoxin | Report EU/mg; limit per study | LAL |
| Sterility | Only if a sterile claim is made | USP &lt;71&gt; |
| Appearance | White to off-white lyophilised cake | Visual |
| Fill mass | Stated mass ± stated tolerance | Balance, calibrated |

Three details make this usable. First, "purity" must specify wavelength and integration threshold; a 214 nm run and a 220 nm run can produce different area percentages on the same sample. Second, "net peptide content" must state whether the result is on an as-is or anhydrous basis. Third, "endotoxin" must specify the unit; EU/mg and EU/vial are not interchangeable without the fill mass.

The specification should also state what is not required. If the study does not need sterility, do not accept a sterility claim as a substitute for identity or purity data. A test that was not needed adds a document, not confidence.

## Five Records That Must Agree

A batch is traceable when five records carry the same identifiers. If one disagrees, stop and resolve it before testing.

| Record | Identifier to check | Common failure |
| --- | --- | --- |
| Vial label | Product, lot, fill mass, storage | Lot format differs from the certificate |
| Certificate of analysis | Product, lot, methods, results, limits | No method column; result without a limit |
| Batch record | Lot, synthesis date, purification date, fill date | Dates out of order; site unnamed |
| Packing list | Lot, quantity, vial count, gross weight | Quantity does not match the invoice |
| Analytical raw file | Sample ID, method, injection sequence | No sample ID; chromatogram image only |

Date order is a cheap forensic check. Synthesis should precede purification, purification should precede fill, and fill should precede release. A certificate whose test date precedes the synthesis date was assembled from another batch or typed by hand. A lot code that changes punctuation between the label and the certificate is not proof of fraud, but it is a reason to ask for the batch record.

The [documentation package guide](/blog/peptide-documentation-package/) and the [COA reading guide](/blog/how-to-read-a-peptide-coa-a-researchers-guide-to-hplc-and-ms-reports/) explain the fields in more detail. The [manufacturer verification protocol](/blog/china-peptide-manufacturer-verification-a-2026-b2b-sourcing-protocol/) covers the site-level questions that sit behind the paperwork.

## Purity, Water, and the Content Calculation

Purity is an area percentage. It is not a mass fraction, and it does not tell you how much peptide is in the vial.

A worked example makes the gap concrete. Suppose the fill mass is 15.0 mg, Karl Fischer water is 4.0%, and ion chromatography finds acetate at 6.0% by mass. The remaining mass is not automatically peptide; residual solvents and inorganic residue can take another share. If the mass balance assigns 1.0% to residual solvents and 0.5% to inorganic matter, the peptide mass is:

15.0 mg × (1 − 0.040 − 0.060 − 0.010 − 0.005) = 13.275 mg.

Net peptide content is 13.275 ÷ 15.0 = 88.5%.

The HPLC result might be 98.7% area. Both numbers can be correct. A buyer who treats 98.7% as "the vial is 98.7% peptide" overstates the peptide mass by more than 10% and under-budgets the amount needed for a study.

Water deserves particular attention because it moves. A lyophilised cake that is exposed to humid air during filling or transit can pick up several percent moisture. Karl Fischer on the finished vial is the check; a water result measured on the bulk powder before filling is not the same measurement. If the specification says "≤5.0% water," the sample should be the vialed product, not the upstream bulk.

Counterion identity matters for the same reason. Acetate and trifluoroacetate salts have different masses per mole of peptide, and TFA removal is a separate process step with its own validation. A certificate that does not state the counterion cannot support a precise content calculation.

## Vetting the Supplier's Role

A supplier's role determines which documents it can legitimately issue.

**A manufacturer** synthesises, purifies, and often fills the peptide. It can produce a batch record, a release certificate, raw analytical data, and a stability summary. It cannot provide independent verification of its own release, because it is the party being verified.

**A repackager** buys bulk peptide, fills vials, and may lyophilise. It can issue a fill record and a certificate for the filled lot. It usually cannot produce the synthesis record for the upstream batch, because it did not perform the synthesis.

**A distributor or broker** holds or sources stock and sells it onward. It can provide a supplier certificate and a packing list. It cannot provide a manufacturing record it does not hold.

**A sourcing platform** coordinates between buyers and manufacturers. It can provide supplier documents, order records, and communication trails. It cannot turn a manufacturer's release certificate into an independent test result.

None of these roles is illegitimate. The problem is a supplier that claims one role and documents another. Ask directly: who synthesised the batch, at which site, and who filled the vials? A manufacturer answers with names and dates. A repackager answers the fill question and refers the synthesis question upstream. A broker answers with a product page.

| Question | Strong answer | Weak answer |
| --- | --- | --- |
| Who synthesised the batch? | Site name, city, batch record reference | "Our partner factory" |
| Who purified and lyophilised? | Same site or a named contractor | "Standard production" |
| Who filled the vials? | Fill site and date | "Factory" |
| Whose name is on the release certificate? | The releasing site, with address | A logo with no legal entity |
| Can raw data be requested? | Yes, with a sample ID and method | "COA is enough" |

The [direct sourcing versus resellers guide](/blog/direct-sourcing-vs-peptide-resellers/) covers the commercial implications of each model, and the [supplier quality assurance guide](/blog/peptide-quality-assurance-process-a-researchers-guide-to-sourcing-integrity/) sets out a fuller audit sequence.

## Receipt Testing and Sampling

Receipt testing should answer the questions the certificate cannot: did this lot arrive as described, and does the material in these vials match the record?

A practical sampling plan for a wholesale lot:

1. **Inspect the shipment before opening.** Record the outer packaging condition, temperature indicator if present, and the number of vials. Photograph the labels.
2. **Select three vials.** Take them from different positions in the lot, not the top row. Keep one unopened as a retain sample.
3. **Weigh the vials.** Record the gross mass. A fill-mass check on a calibrated balance is a cheap screen for underfilled or overfilled units.
4. **Test two vials.** Identity by LC-MS, purity by RP-HPLC at 220 nm, water by Karl Fischer. Add LAL endotoxin if the study requires it.
5. **Retain the raw data.** Chromatograms, spectra, integration tables, and the sample IDs should be stored with the lot record.

Three vials are not a statistical sampling plan for a large lot. They are a practical screen that catches a batch-level problem and creates a retained reference. If the project needs a formal sampling plan, define the sample size and acceptance number before the shipment arrives.

Acceptance rules should be written before the results:

- Identity outside the stated mass tolerance: reject the lot.
- Purity below the specification: retest a second vial with the same method before disposition.
- Water above the limit: recalculate net peptide content and compare with the specification basis.
- Endotoxin above the study limit: reject for that study, even if purity passes.
- Label or lot mismatch: quarantine until the supplier resolves the record.

A retest is not a second opinion from a different laboratory on a different sample. It is the same method on a second vial from the same lot, with the raw data retained. If the two results disagree beyond the method's repeatability, the lot is heterogeneous, and that is itself a finding.

## MOQ, Lead Time, and the Cost of a Bad Lot

The purchase price is one line in the total cost of a lot. The others are shipping, duties, testing, storage, and the cost of repeating an experiment because a batch failed.

Peptides of China's standard catalog minimum is USD 600. Multiple catalog products can be combined to reach it, and orders normally start from one 10-vial kit per product. The USD 10 deposit initiates manual processing and is credited toward the final invoice; availability and the current proposal are confirmed before the remaining balance is requested. Those mechanics are described on the [how it works page](/how-it-works/).

Lead time has two parts: the time to confirm availability and the time in transit. A supplier that quotes a transit time without stating the dispatch date has quoted half a lead time. Ask for the date the lot leaves the fill site, the shipping lane, and the expected customs entry point. The [lead-time guide](/blog/how-to-evaluate-peptide-supplier-lead-times-in-2026/) gives a comparison framework.

A bad lot costs more than its price. The replacement may arrive after the study window closes; the retest consumes vials; the investigation consumes staff time. For a wholesale order, it is rational to pay more for a supplier that can produce the batch record and raw data than to save a few percent on a supplier that cannot. That is not a quality guarantee; it is a reduction in the number of unknowns.

## Contract Terms and Disposition

The purchase terms should define four things: the specification, the sampling method, the acceptance decision, and the remedy.

**Specification by reference.** Attach the specification as a schedule to the order. A statement in an email is harder to enforce than a numbered attachment with limits and methods.

**Sampling and testing.** State who tests, where, and with what method. If the buyer tests on receipt, say so and set a notification window for a failed result.

**Acceptance and retest.** Define what counts as a failure and what triggers a retest. A purity result below the limit is a retest trigger; an identity result outside tolerance is a rejection. Mixing the two creates disputes.

**Remedy.** Decide in advance whether a failed lot is replaced, credited, or refunded, and who pays for the return or destruction. A supplier that will not put a remedy in writing is pricing the risk into your project, not its own.

Customs and import duties sit outside the quality contract. The importer of record is responsible for classification, duties, and entry documents, and a supplier cannot guarantee clearance. The [customs clearance guide](/blog/research-peptide-customs-clearance-a-professional-b2b-sourcing-guide-2026/) explains the document set. A supplier that promises clearance is making a claim it cannot control.

## The Author's Take

**Position.** Buy tirzepatide the way you would buy a reference material: identity first, content second, price third. The batch record is more valuable than a second decimal place on a purity certificate.

**Reasoning.** Tirzepatide is a large, modified peptide with a mass that is easy to state and harder to confirm. The market has many sellers who can forward a certificate and few who can produce the synthesis and fill records behind it. In my experience, the failures that damage studies are not subtle shifts in purity; they are lot mismatches, missing methods, and content calculations that treat an area percentage as a mass fraction. A buyer who demands five matching records and does the net-content arithmetic avoids most of them. The rest requires a laboratory, and that is a budget decision.

**Disclosure.** Peptides of China sells research peptides. This article is a procurement judgment, not an effects claim. Tirzepatide research material is for laboratory research only and is not for human or veterinary use.

## Sources

1. U.S. Food and Drug Administration. Drugs@FDA database. https://www.accessdata.fda.gov/scripts/cder/daf/
2. Coskun T, Urva S, Roell WC, et al. LY3298176, a novel dual GIP and GLP-1 receptor agonist for the treatment of type 2 diabetes mellitus: from discovery to clinical proof of concept. Molecular Metabolism. 2018;18:3–14. https://doi.org/10.1016/j.molmet.2018.09.005
3. International Council for Harmonisation. ICH Q6A: Specifications — Test Procedures and Acceptance Criteria for New Drug Substances and New Drug Products. https://database.ich.org/sites/default/files/Q6A%20Guideline.pdf
4. International Council for Harmonisation. ICH Q2(R2): Validation of Analytical Procedures. 2023. https://database.ich.org/sites/default/files/ICH_Q2%28R2%29_Guideline_2023_1130.pdf
5. U.S. Food and Drug Administration. Analytical Procedures and Methods Validation for Drugs and Biologics: Guidance for Industry. 2015. https://www.fda.gov/regulatory-information/search-fda-guidance-documents/analytical-procedures-and-methods-validation-drugs-and-biologics
6. D'Hondt M, Bracke N, Taevernier L, et al. Related impurities in peptide medicines. Journal of Pharmaceutical and Biomedical Analysis. 2014;101:2–30. https://doi.org/10.1016/j.jpba.2014.06.012
7. United States Pharmacopeia. &lt;1058&gt; Analytical Instrument Qualification. https://doi.org/10.31003/uspnf_m1124_10101_01
8. United States Pharmacopeia. &lt;1225&gt; Validation of Compendial Procedures. https://doi.org/10.31003/uspnf_m99945_40101_01
9. Clinical and Laboratory Standards Institute. Method Evaluation and Validation standards, including EP05 precision studies. https://clsi.org/standards/products/method-evaluation/
