---
title: "Peptide Documentation Package: A Batch File Checklist"
slug: "peptide-documentation-package"
description: "The batch-specific records a peptide supplier should provide: COA fields, chromatograms, MS data, endotoxin results, traceability, and red flags."
---
**A peptide documentation package is the batch-specific set of records that lets a buyer prove what is in the vial, who made it, and what was measured before release.** It is not a certificate of analysis with a logo on it. It is a bundle in which every document carries the same lot identifier and every analytical claim is backed by raw data.

The test for completeness is simple: hand the package to an analyst who has never spoken to the supplier and ask whether that person could reconstruct the batch. If the answer depends on calling someone, the package is incomplete. This guide sets out the fields, the documents, and the failure modes that matter in practice. For the analytical side of the same question, the [laboratory verification guide](/blog/peptide-testing-and-analysis-a-professional-guide-to-laboratory-verification/) covers sampling and method validation.

## What Counts as a Complete Package

A usable package answers five questions, and each one requires a different document.

| Question | Document that answers it | What "complete" looks like |
|---|---|---|
| What was made? | Product specification and batch record summary | Sequence, salt form, fill mass, lot number |
| Was it made consistently? | Batch manufacturing record extract | Synthesis scale, coupling strategy, purification runs |
| What did release testing show? | COA with raw chromatogram and mass spectrum | Method, result, acceptance criterion, analyst, date |
| Is it safe for the intended handling? | Endotoxin, sterility, and bioburden reports | Method, limit, numeric result, spike recovery where applicable |
| Can the paperwork be tied to the vial? | Label, packing list, and lot cross-reference | Identical lot identifier on all three |

Most suppliers provide the first and third rows and stop. The second row is where manufacturers separate themselves from traders, because a trader cannot produce a batch record for a product it did not make. The fourth row is frequently missing on research-grade material, and it should be requested explicitly when the study design requires it.

## Batch Linkage: The Field That Makes the Rest Usable

The lot number is the hinge on which the entire package turns. A COA without a lot number, or with a lot number that does not match the vial label, is a generic document. It may describe a real batch, but it does not describe yours.

Three identifiers should agree: the label on the vial, the packing list or invoice line, and the COA header. Ask for a photograph of the labelled vial next to the packing list if you are buying remotely. Suppliers that manufacture their own material can usually produce this in minutes. Suppliers that drop-ship from a distributor often cannot.

Lot numbering conventions vary, which is not itself a problem. A date-coded format such as YYMMDD-sequence, a campaign code, or an internal batch number all work if the supplier can trace the number back to a manufacturing record. What matters is that the identifier is unique, stable, and used consistently across documents. A supplier that reuses one lot number for multiple production runs has removed the ability to investigate a complaint.

The COA should also carry a **manufacture date** and a **retest or expiry date**. For lyophilized research peptides, a 24 to 36 month retest period at −20 °C is common. A COA with no date, or with an expiry date that precedes the manufacture date, is a document-control failure regardless of the analytical results.

## The Analytical Core: Purity, Identity, Content, and Mass Balance

Three measurements form the analytical core, and each one answers a different question.

**Purity by RP-HPLC.** The [COA reading guide](/blog/how-to-read-a-peptide-coa-a-researchers-guide-to-hplc-and-ms-reports/) breaks the report into its component fields; here the point is what the package must contain. The report should state the column dimensions, particle size, pore size, mobile phase composition, gradient, flow rate, column temperature, detection wavelength, injection volume, and integration threshold. A purity value without those parameters cannot be reproduced. For a typical peptide, a C18 column of 4.6 × 250 mm with 5 µm particles and 300 Å pores, run at 1.0 mL/min and 35 °C with a water/acetonitrile gradient containing 0.1% trifluoroacetic acid, is a standard configuration.

**Identity by mass spectrometry.** The deconvoluted mass should be reported alongside the theoretical mass and the difference in ppm or Da. A mass tolerance of 5 ppm is a reasonable expectation for a modern instrument on a peptide under 5 kDa. The report should also show the charge state envelope, because a deconvoluted number with no raw spectrum is a calculation, not evidence.

**Content by quantitative assay.** This is the measurement buyers most often skip and most often need. Amino acid analysis, nitrogen determination, or a validated HPLC assay against a reference standard can establish how much peptide is present by mass. A vial labelled 10 mg may contain 10 mg of total powder, of which 8.6 mg is peptide and the balance is counterion and water.

| COA field | Why it matters | Common omission |
|---|---|---|
| Lot number | Ties the document to the vial | Present but not matched to label |
| Sequence and salt form | Defines what the mass should be | Salt form left as "peptide" |
| HPLC method detail | Makes purity reproducible | Wavelength and gradient absent |
| Chromatogram | Shows what the percentage hides | Summary only, no peak table |
| Mass spectrum | Supports identity | Deconvoluted value only |
| Water content | Part of mass balance | Missing on most research COAs |
| Counterion content | Part of mass balance | Missing unless requested |
| Endotoxin result | Study-dependent safety attribute | "Not tested" with no explanation |

A peptide is rarely supplied as the free base or free acid. Trifluoroacetate, acetate, and chloride are the common counterions, and each contributes mass that is not peptide. Water content adds more. A mass balance that accounts for peptide, counterion, and water is the difference between a label that means something and a label that describes a container.

Karl Fischer titration is the standard method for water content. For a lyophilized peptide, results in the 2–6% range are common, and a specification of 5.0% or less is typical for material intended for sensitive work. A COA reporting 0.1% water on a lyophilized powder is worth questioning, because the technique is sensitive enough that near-zero values usually indicate a drying issue or a reporting error rather than an exceptionally dry product.

Counterion identity and content are reported less often. Ion chromatography with conductivity detection can quantify trifluoroacetate and acetate, and the result should be expressed as a percentage by mass. For a peptide supplied as the acetate salt, the acetate content belongs on the COA. For a peptide supplied as the trifluoroacetate salt, the same applies. The [TFA removal guide](/blog/tfa-removal-peptides/) covers why this matters for assay work and how the exchange is verified.

The practical consequence: a 10 mg vial at 96% HPLC purity, 90% peptide content, and 85% mass balance contains roughly 7.6 mg of peptide. That is not a defect if the label states fill mass rather than peptide mass. It is a defect if the buyer assumed the two were the same.

## Endotoxin and Sterility Records

Endotoxin and sterility are separate attributes, tested by separate methods, and neither is implied by chemical purity.

The bacterial endotoxins test, described in USP &lt;85&gt;, uses Limulus amebocyte lysate or recombinant factor C to detect lipopolysaccharide. Results are expressed in endotoxin units per milligram or per millilitre, against a limit set by the route and exposure level in the intended application. For research use, the limit is a study decision, not a universal number; the [endotoxin testing guide](/blog/endotoxin-testing-peptide-manufacturing/) covers how limits are set and verified. What the COA must provide is the method, the limit of detection, the numeric result, and the spike recovery for the sample dilution. A recovery outside 50–200% invalidates the quantitation, and many research COAs omit the recovery entirely.

Sterility testing under USP &lt;71&gt; involves a 14-day incubation and is expensive for a research supplier to run on every lot. Many provide bioburden or membrane filtration data instead. That is a different claim. Bioburden estimates the microbial load before a sterilisation step; sterility confirms the absence of viable organisms after it. A COA that says "sterile" with no method name is asserting an outcome without evidence; the [sterility testing protocol guide](/blog/sterility-testing-for-research-peptides-a-protocol-guide/) describes what a valid test record includes.

For lyophilized powders handled in a laminar flow hood with sterile diluent, the practical risk is lower than for a liquid formulation, but the documentation question does not change. If the study protocol requires sterile material, the record must show how sterility was achieved and verified.

## Manufacturing Traceability and Raw Material Lots

Traceability is the part of the package that traders cannot fabricate convincingly. A manufacturer can state which facility ran the synthesis, at what scale, with which resin and coupling reagents, and which raw material lots went in. A reseller can only pass along what it received.

Useful traceability fields include: synthesis site, synthesis scale in millimoles, resin type and loading, coupling reagent, deprotection conditions, cleavage cocktail, purification column and gradient, number of purification passes, lyophilisation cycle parameters, and fill date. Not every supplier will release all of these, and some are legitimately proprietary. The pattern to watch is whether the supplier can answer any of them with specifics.

Raw material lot traceability matters most when a batch fails. If a deletion sequence appears across two production runs, the common factor may be a reagent lot rather than the synthesis method. A manufacturer that records incoming material lots can investigate that. A trader cannot.

## What a Package Should Not Contain

Some documents reduce confidence rather than increase it.

**Identical COAs for different lots.** If two batches produce chromatograms with the same peak heights to two decimal places, one document has been reused. Real chromatography has run-to-run variation.

**A purity value with no chromatogram.** The number is a conclusion. The chromatogram is the data.

**An accreditation logo with no scope.** A laboratory can hold ISO/IEC 17025 accreditation for unrelated methods. The scope document names the methods covered.

**Unsupported superlatives.** "Pharmaceutical grade", "USP grade", and "GMP certified" are claims that map to specific standards. If the package does not name the standard and the certificate, the claim is marketing.

**A COA dated after the shipment.** Document control should prevent this. When it happens, ask which date is wrong, the test date or the shipping date.

## Verification Workflow, Retention, and Versioning

A repeatable workflow prevents the package from being reviewed differently every time.

1. **Match identifiers.** Vial label, packing list, invoice, and COA must carry the same lot number.
2. **Check dates.** Manufacture date, test date, and retest date should be internally consistent and consistent with the shipping date.
3. **Read the method before the result.** Column, gradient, wavelength, and integration threshold determine what the percentage means.
4. **Reconcile the numbers.** Purity plus impurity total should approach 100% of integrated area. Content plus water plus counterion should approach the fill mass.
5. **Verify the mass.** Compare the deconvoluted mass with the theoretical mass for the stated sequence and salt form.
6. **Record the disposition.** Write down pass, pass with deviation, or reject, with the reason. A package that is reviewed but not dispositioned has no evidentiary value later.

The workflow takes about twenty minutes per lot once the supplier's format is familiar. It is the cheapest quality control available, because it costs attention rather than instrument time. The [characterization checklist](/blog/peptide-characterization-reporting-checklist/) extends the same six steps into a full data set for higher-risk lots.

Keep the package for as long as you keep the material, and longer if the material supports a published study. For most research groups, that means a minimum of two years and preferably five. The [quality testing pillar](/peptide-quality-testing/) collects the related record types in one place.

Version control matters when a supplier reissues a COA. A reissued document should carry a revision number and a reason. If a supplier replaces a COA after a complaint without marking the change, the original is the document that matters, and you should already have it stored outside the supplier's portal.

Retained samples complete the record. One unopened vial per lot, stored at −20 °C with the lot number on the label, allows a later dispute to be settled by testing rather than argument. Record the storage location in the same file as the paperwork.

Data integrity expectations are described in the MHRA GxP data integrity guidance and in 21 CFR Part 11 for electronic records. The principles are attributable, legible, contemporaneous, original, and accurate. A supplier that provides only a summary PDF, with no chromatogram file or audit trail, is providing a conclusion. For routine research purchasing that may be sufficient. For a file that supports a regulatory submission, it is not.

## Package Depth by Buyer Type

Different buyers need different depths, and asking for more than you need slows the transaction without improving the decision.

| Buyer type | Minimum package | Additional records worth requesting |
|---|---|---|
| Academic lab, pilot study | COA with chromatogram and MS | Retest date, storage condition, batch record summary |
| Core facility, repeated orders | Full analytical core plus water content | Counterion content, lot-to-lot trend data |
| CRO or contract research | Full core plus endotoxin | Sterility or bioburden, raw material lot traceability |
| Reseller or private label | Full core plus manufacturing site disclosure | Batch record extract, label reconciliation, CoC template |
| Regulatory submission | Full core, validation summaries, audit trail | Method validation reports, deviation log, site qualification |

The pattern is consistent: as the consequence of a wrong result rises, the package moves from conclusions toward raw data and traceability. Buyers should decide which row they are in before requesting documents, because a supplier that receives an unfocused request will send whatever is easiest.

## The Author's Take

**Position.** A supplier that cannot produce a batch-matched COA with a chromatogram, a mass spectrum, and a lot number that matches the vial has not documented its product, and the buyer should treat that as a disqualifying gap rather than a negotiating point.

**Reasoning.** The cost of producing a proper package is small for a manufacturer and large for a trader, which makes the package a useful signal. A manufacturer already holds the chromatogram, the mass spectrum, and the batch record as by-products of production. A trader has to request them from someone else, and often cannot. When a supplier offers a polished COA with no raw data, the polish is the product. Buyers who accept that trade discover the gap only when a study fails or a batch is disputed, at which point the missing document cannot be reconstructed. The same logic applies to content and counterion data: they are cheap to measure at release and impossible to infer later.

**Disclosure.** Peptides of China sells research peptides. This article describes documentation practice and procurement judgment; it is not an effects claim, a dosing guide, or medical advice. Products referenced on this site are supplied for laboratory research use only. Documentation varies by product and batch, and buyers who need independent verification should arrange third-party testing after receipt.

## Sources

- 21 CFR Part 11 Electronic Records; Electronic Signatures. Electronic Code of Federal Regulations. [ecfr.gov](https://www.ecfr.gov/current/title-21/chapter-I/subchapter-A/part-11)
- USP &lt;71&gt; Sterility Tests. United States Pharmacopeia. [usp.org/usp-nf](https://www.usp.org/usp-nf)
- USP &lt;85&gt; Bacterial Endotoxins Test. United States Pharmacopeia. [usp.org/usp-nf](https://www.usp.org/usp-nf)
- ICH Q7 Good Manufacturing Practice Guide for Active Pharmaceutical Ingredients. International Council for Harmonisation. [database.ich.org](https://database.ich.org/sites/default/files/Q7%20Guideline.pdf)
- ICH Q6B Specifications: Test Procedures and Acceptance Criteria for Biotechnological/Biological Products. [database.ich.org](https://database.ich.org/sites/default/files/Q6B%20Guideline.pdf)
- MHRA Guidance on GxP Data Integrity (2018). Medicines and Healthcare products Regulatory Agency. [gov.uk](https://www.gov.uk/government/publications/guidance-on-gxp-data-integrity)
- ISO 9001:2015 Quality management systems — Requirements. International Organization for Standardization. [iso.org/standard/62085.html](https://www.iso.org/standard/62085.html)
- Good Distribution Practice guidelines. European Commission, EudraLex Volume 4. [health.ec.europa.eu](https://health.ec.europa.eu/medicinal-products/eudralex/eudralex-volume-4_en)
- PIC/S Good Manufacturing Practice Guide for Active Pharmaceutical Ingredients. Pharmaceutical Inspection Co-operation Scheme. [picscheme.org](https://picscheme.org/en/publications)
