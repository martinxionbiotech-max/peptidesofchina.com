---
title: "Peptide Facility Procurement: Reading a Factory Before You Order"
slug: "peptide-facility-procurement-navigating-manufacturer-side-sourcing-in-2026"
description: "How lab buyers can assess a peptide synthesis facility from documents: capacity math, equipment lists, segregation, QC scope, and audit signals."
author: "POC Tech Team"
updated: "2026-11-18"
---

Peptide facility procurement means buying from the site that runs the reaction rather than from a trading desk. The practical difficulty is that almost no buyer visits a Chinese peptide plant before the first order, and the marketing material from every supplier looks the same: stainless steel, clean corridors, a row of instruments. The way to read a facility at a distance is to ask for the documents that a real site generates as a by-product of working — equipment logs, column usage records, calibration certificates, deviation reports — and to check whether the numbers in those documents add up. A facility that can produce a coherent capacity story is usually a facility that can produce a coherent batch.

## What "facility" means in a peptide quote

A quotation can come from three kinds of organisation. A synthesis site owns reactors, purification columns, and a lyophilizer. A formulator buys bulk peptide, fills vials, and may not synthesize at all. A trader owns neither and forwards the quote.

The distinction surfaces in small details. Ask which site will manufacture the lot and what equipment the final purification runs on. A synthesis site answers with a column diameter and a resin batch. A formulator answers with a fill line and a lyophilization cycle. A trader answers with a delivery time.

For research peptides, the synthesis site is the relevant facility even when the vial is filled elsewhere. Identity, impurity profile, and counterion are set during synthesis and purification. Filling affects dose accuracy and microbial quality, not sequence. Buyers who audit the filler and ignore the synthesizer are checking the wrong end of the process.

## Reading a site from its documents

A facility review can start with five documents. None of them is a certificate of quality; each is a record that accumulates only if the site operates.

| Document | What it reveals | What a weak site shows |
|---|---|---|
| Equipment list with capacities | Reactor volumes, column sizes, lyophilizer shelf area | Generic list with no model numbers |
| Calibration schedule and certificates | Whether balances, pH meters, and HPLC detectors are maintained | Certificates older than 12 months |
| Column usage log | Purification history and cleaning cycles | No log, or a log with one column for everything |
| Batch record template | Process control, in-process tests, sign-off points | One-page sheet with no in-process checks |
| Deviation and CAPA log | How non-conformance is handled | "Zero deviations" across years of production |

The last row is the most informative. A site that claims no deviations over hundreds of batches is either not recording them or not running the process it describes. A site that shows twelve deviations and twelve closures, with root causes and dates, is showing a working quality system.

Calibration records deserve a specific check: the balance used to weigh 5 mg fills needs a readability of 0.01 mg and a calibration certificate traceable to a national standard. A site that calibrates monthly and keeps the certificates is managing a real risk. A site that calibrates annually is managing a document.

## Capacity math: reactor, resin, and realistic batch size

Batch size claims can be tested with arithmetic. Solid-phase synthesis capacity is bounded by resin loading and reactor volume, and the peptide mass follows from the resin substitution and the molecular weight.

| Parameter | Typical value | Effect on batch size |
|---|---|---|
| Resin loading | 0.3–0.5 mmol/g | Higher loading means more peptide per gram of resin |
| Resin charge in a 50 L reactor | 5–12 kg | Practical fill limits mixing and swelling |
| Crude yield | 60–75% of theoretical | Losses from coupling and cleavage |
| Purified yield | 50–70% of crude | Depends on sequence and impurity profile |
| Lyophilizer shelf area | 1–5 m² | Limits the fill volume per cycle |

A worked estimate: 10 kg of resin at 0.4 mmol/g carries 4 mol of growing chain. For a peptide of about 3,400 Da, the theoretical mass is 4 × 3,400 g, or 13.6 kg. Applying a 65% crude yield and a 60% purification yield gives roughly 5.3 kg of purified peptide before fill. A supplier quoting 20 kg from the same reactor is either using a much larger vessel or quoting a number that the equipment cannot support.

The arithmetic is not a substitute for an audit. It is a filter. When the claimed capacity and the equipment list disagree by a factor of three, the buyer has learned something without leaving the desk.

## The equipment list that determines quality

Four equipment groups decide whether a peptide lot meets spec.

**Synthesis.** Reactors with mechanical stirring and temperature control, a resin frit of the right porosity, and a solvent delivery system that can handle DMF, DCM, and piperidine. Manual or semi-automated systems are common at research scale; the record of coupling times and equivalents matters more than the brand.

**Purification.** Preparative HPLC with a column sized to the batch. A 50 mm × 250 mm column packed with 10 µm C18 handles tens of milligrams to a few grams per injection; a 100 mm × 500 mm column handles larger loads. The column log should show packing date, cleaning cycles, and performance checks.

**Lyophilization.** Shelf area, shelf temperature control, condenser capacity, and vacuum control. A cycle that runs too warm produces collapse or meltback; a cycle that runs too long wastes capacity. The batch record should name the cycle and the endpoint criterion.

**Quality control.** Analytical HPLC with a photodiode array detector, an LC-MS system, a Karl Fischer titrator, and a balance calibrated for microweights. A site that outsources all four can still produce good material, but it cannot release a lot without a third-party turnaround, which shows up in lead time.

Ask for the instrument list with model numbers and the date of the last qualification. An HPLC detector that has never been qualified can still produce a chromatogram; the question is whether the area percent means anything across years.

## Segregation and cross-contamination

A peptide facility runs many sequences in the same rooms. The risk is not bulk contamination; it is trace carryover from a previous batch, which appears as an extra peak at low area percent and is hard to assign.

Three controls reduce it:

- **Dedicated resin and tubing** for sequences with unusual hydrophobicity, or a documented cleaning step between campaigns.
- **Line clearance** before each campaign, recorded with the previous batch number and the operator's signature.
- **Cleaning validation** for shared vessels, with a swab or rinse sample and an acceptance limit.

The cleaning limit is the detail worth asking about. A limit expressed as "visually clean" is not a limit. A limit expressed as "no peak above 0.1 area% at the retention time of the previous product" can be tested.

For lyophilized products, the lyophilizer is a shared surface that is often overlooked. Sublimation carries volatiles, not peptide, but a poorly cleaned shelf and door gasket can transfer residues. A site that documents a wipe-down between cycles and keeps the log is managing the risk.

## QC capability: in-house versus outsourced

There is no single right answer on outsourcing. What matters is that the release testing is defined and that the site can interpret its own data.

In-house HPLC and MS give fast iteration: a failed purification fraction can be re-run the same day. Outsourced testing gives independence, which is valuable for a disputed lot, but adds three to seven days per round and makes process tweaks slow.

A workable arrangement for research supply:

| Test | Where it runs | Reason |
|---|---|---|
| Identity by MS | In-house | Needed during purification as well as at release |
| Purity by HPLC | In-house, with periodic external check | Fast feedback, external check catches drift |
| Water by Karl Fischer | In-house | Simple, frequent, cheap |
| Endotoxin | Outsourced | Requires validated LAL setup and controls |
| Sterility | Outsourced | Requires microbiology capability |
| Elemental impurities | Outsourced | Requires ICP-MS |

A site that runs its own HPLC but cannot explain how it integrated a shoulder peak is not really running the method. Ask for the integration parameters and the column performance log. A site that outsources everything but sends the third-party report with the raw data has a clearer story.

## Audit findings worth acting on

Most facility audits produce a list. The useful ones cluster into four themes.

**Data integrity.** Chromatograms without audit trails, shared login accounts, results entered into a spreadsheet after the run. Under 21 CFR Part 11, electronic records used for release need access controls and audit trails. A site that cannot show them is not necessarily falsifying data; it is not positioned to prove it did not.

**Equipment qualification.** An unqualified lyophilizer or an HPLC detector with no performance check. The consequence is not a bad batch today; it is the inability to compare a batch from this year with one from three years ago.

**Deviation handling.** Deviations closed without a root cause, or a CAPA that repeats. A site with three deviations on the same lyophilization cycle has a process problem, not a training problem.

**Supplier control.** No incoming testing of resin, amino acids, or solvents. A cheap resin with inconsistent loading produces variable crude yield, which is often blamed on the coupling step.

The [GMP compliance assessment guide](/blog/how-to-assess-peptide-supplier-gmp-compliance-in-2026) covers the certificate and audit trail questions in more detail. For a first order, the [manufacturer verification protocol](/blog/china-peptide-manufacturer-verification-a-2026-b2b-sourcing-protocol) sets out the order in which to request documents so that each answer informs the next question.

## From lyophilizer to your loading dock

The facility's responsibility does not end at the dry powder. Three handover steps affect what arrives.

**Fill and closure.** A 5 mg fill in a 10 mL vial is a small target. Gravimetric check-weighing of a sample of vials, with a tolerance of ±5%, is standard. A site that fills by volume without a density check will drift across a batch.

**Secondary packaging.** Vials need protection from light and moisture. A foil pouch with desiccant is appropriate for a hygroscopic peptide; a zip bag is not.

**Cold chain and documentation.** Lyophilized peptide travels well at ambient, but summer transit through a hot hub can push a package above 40 °C for hours. A temperature indicator in the carton costs little and settles disputes. The commercial invoice, packing list, COA, and SDS should travel with the shipment and match the lot numbers on the vials.

The [peptide testing and analysis guide](/blog/peptide-testing-and-analysis-a-professional-guide-to-laboratory-verification) covers the receiving tests, the [documentation package guide](/blog/peptide-documentation-package) lists the records to request with the shipment, and the [HPLC versus LC-MS comparison](/blog/hplc-vs-lc-ms-peptides) explains which method to run first when a lot looks wrong. The [how sourcing works](/how-it-works/) page describes the document flow for a first order, and the [FAQ](/faq/) answers the questions that arrive before a facility review.

## The Author's Take

**Position.** A facility is credible when its equipment list, batch record, and capacity claims agree with each other. Certificates are easy to buy; a coherent set of operating records is not.

**Reasoning.** The arithmetic of resin loading and reactor volume is public, and it constrains what a site can produce. When a supplier's claimed output exceeds what the equipment can hold, one of the two numbers is wrong, and the buyer cannot tell which without asking. The same logic applies to quality: a site that runs its own purification has column logs, and a site that runs its own release testing has calibration records. Those records exist because the work happens. A trader can photocopy a certificate but cannot produce a column log with a packing date and a performance trend. Buyers who ask for the boring documents get a more accurate picture than buyers who ask for the impressive ones.

**Disclosure.** Peptides of China works with manufacturing partners and sells research peptides. This article describes procurement and audit judgment, not an effects claim. Products are supplied for research use only and are not for human or veterinary use.

## Sources

- ICH. *Q7: Good Manufacturing Practice Guide for Active Pharmaceutical Ingredients.* https://database.ich.org/sites/default/files/Q7%20Guideline.pdf
- ICH. *Q1A(R2): Stability Testing of New Drug Substances and Products.* https://database.ich.org/sites/default/files/Q1A%28R2%29%20Guideline.pdf
- ICH. *Q2(R1): Validation of Analytical Procedures: Text and Methodology.* https://database.ich.org/sites/default/files/Q2%28R1%29%20Guideline.pdf
- ICH. *Q3A(R2): Impurities in New Drug Substances.* https://database.ich.org/sites/default/files/Q3A%28R2%29%20Guideline.pdf
- U.S. Food and Drug Administration. *21 CFR Part 211 — Current Good Manufacturing Practice for Finished Pharmaceuticals.* https://www.ecfr.gov/current/title-21/chapter-I/subchapter-C/part-211
- U.S. Food and Drug Administration. *21 CFR Part 11 — Electronic Records; Electronic Signatures.* https://www.ecfr.gov/current/title-21/chapter-I/subchapter-A/part-11
- U.S. Food and Drug Administration. *Contract Manufacturing Arrangements for Drugs: Quality Agreements (Guidance for Industry).* https://www.fda.gov/media/86193/download
- U.S. International Trade Commission. *Harmonized Tariff Schedule of the United States.* https://hts.usitc.gov/
