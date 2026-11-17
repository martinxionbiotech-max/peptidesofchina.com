---
title: "Clinical Research Peptide Documentation Checklist"
slug: "clinical-research-peptide-documentation-checklist"
description: "A receiving-to-archive checklist for clinical research peptides: lot linkage, temperature logs, COA fields, deviations, retention periods and audit traps."
author: "POC Tech Team"
updated: "2026-11-17"
---
A clinical research peptide documentation checklist exists to answer one audit question: can you show, from the files alone, which lot was used in which experiment, under what storage conditions, and with what analytical evidence? If the answer requires a phone call to the supplier, the file is incomplete. If the answer requires a memory of what happened during receiving, it is not a record.

This checklist is written for the receiving team, the study coordinator, and the quality reviewer who inherit a shipment after procurement has closed the purchase order. It covers the documents to collect, the fields that link them, the records that are usually missing, and the retention rules that keep the file usable years later. It is not a clinical protocol and does not address administration. The scope is the paperwork and the sample chain.

## The 30-Second Receiving Check

Before signing for the parcel, check three things: the outer label matches the purchase order, the lot number is visible, and the temperature indicator has not triggered. If any of the three fails, accept the parcel under exception and photograph the condition before opening.

The exception record should include the date, the time, the carrier, the tracking number, the observed condition, and the name of the person who accepted it. A photograph of the label and the indicator is worth more than a paragraph of description. If the shipment is refused, record the refusal and notify the supplier the same day.

Open the parcel in a designated receiving area, not at a bench where samples are handled. Check the inner packaging for desiccant, secondary containment, and a temperature logger. Download the logger data before discarding the packaging. A logger that is not downloaded is a plastic tag.

Then compare the vial label with the certificate and the packing list. The lot number, the product name, the fill mass, and the storage condition should match across all three. A mismatch is a documentation deviation, even if the material looks correct.

## The Core Document Set

A complete lot file has eight document groups. The table below lists them with the purpose of each.

| Document | Purpose | Minimum fields |
| --- | --- | --- |
| Purchase order and specification | Defines what was bought | Product, grade, fill, quantity, acceptance criteria |
| Supplier quotation and confirmation | Records the agreed terms | Price, lead time, Incoterms, lot commitment |
| Certificate of analysis | Reports release results | Lot, methods, results, limits, dates, signature |
| Specification sheet | Defines the release limits | Identity, purity, water, content, appearance |
| Safety data sheet | Documents hazards and handling | Version, date, sections 1–16 |
| Packing list and invoice | Links the shipment to the order | Lot, quantity, value, seller, buyer |
| Shipping and temperature record | Documents the chain of custody | Dates, logger data, carrier, condition |
| Receiving inspection record | Documents the acceptance decision | Check items, results, reviewer, date |

Two additional groups apply in some studies: the import or customs file, and the supplier qualification file. The customs file should include the declaration, the broker's classification note, and any permit. The qualification file should include the supplier audit, the sample test results, and the approval decision. Our [documentation package guide](/blog/peptide-documentation-package/) describes how these groups fit together, the [customs clearance guide](/blog/research-peptide-customs-clearance-a-professional-b2b-sourcing-guide-2026/) covers the border documents, and the [characterization reporting checklist](/blog/peptide-characterization-reporting-checklist/) lists the analytical fields a reviewer should expect.

## Lot Linkage: The Field That Decides Everything

The lot number is the join key between the physical sample and the paper record. It should appear on the vial label, the certificate, the packing list, the invoice, and the receiving record. The format should be identical across all five. A lot code that changes punctuation between documents is a warning, not a typo.

Record the lot number exactly as printed, including prefixes and suffixes. Do not normalize it in the receiving log. If the supplier uses a slash in one document and a hyphen in another, record both and note the discrepancy. The auditor will ask which string is the controlled identifier.

Link the lot to the study batch record. If a study uses multiple lots, record the lot-to-group assignment before the first use. A common audit finding is a study that used two lots but documented only one, because the second lot was opened as a replacement and the change was not recorded.

Link the lot to the analytical file. The certificate should be stored under the same identifier as the receiving record. If the certificate is stored under the order number, a search by lot will fail. If the receiving record is stored under the supplier name, a search by study will fail.

Test the linkage with a retrieval exercise. Pick a study date, ask a colleague to find the lot used on that date, and time the search. If it takes more than a few minutes, the filing scheme is not working.

## Temperature and Chain-of-Custody Records

Lyophilized peptides are usually stored at 2–8°C or at −20°C, depending on the supplier's stability data. The storage condition on the label is the controlling instruction. The receiving record should state the condition at arrival, the condition in storage, and any excursion.

A temperature excursion is not automatically a rejection. It is an event that requires an assessment. Record the duration, the maximum temperature, the product state during the excursion, and the supplier's written guidance. If the excursion occurred in transit, ask the supplier for stability data that covers the condition. If the excursion occurred in your storage, open a deviation and assess the impact on the study.

The chain-of-custody record should show every transfer: carrier to receiving, receiving to storage, storage to preparation area, and back. Each transfer should have a date, a time, a location, and a signature. A chain with a gap is a gap, even if nothing bad happened during it.

For shipments that cross borders, the chain includes the customs broker and the temporary storage facility. Ask for the broker's receipt and the warehouse temperature record if the parcel was held. A held shipment in a warm warehouse is a stability event, not a delay. The [shipping documentation note](/blog/why-legitimate-documentation-matters-in-peptide-shipping/) explains which carrier and customs records are worth keeping in the lot file.

## COA Review: Fields, Methods, Limits

The certificate should be reviewed against the purchase specification, not against a generic standard. Start with the identity row: the method, the observed mass, the theoretical mass, and the tolerance. Then the purity row: the method, the column, the wavelength, the gradient, the main-peak percentage, and the impurity profile. Then the content row: the method, the result, and the basis.

A result without a limit cannot be judged. A limit without a method cannot be reproduced. A method without a wavelength or column cannot be compared with another laboratory's result. The review should record each of these as present, partial, or absent.

The dates deserve their own check. Synthesis, purification, lyophilization, testing, and release should form a plausible sequence. A certificate issued before the test date is impossible. A certificate with a test date more than two years before the shipment date should prompt a retest question.

Our [COA reading guide](/blog/how-to-read-a-peptide-coa-a-researchers-guide-to-hplc-and-ms-reports/) provides a field-by-field method, and the [COA authentication guide](/blog/coa-verified-peptides-supplier-how-to-authenticate-research-purity-in-2026/) covers the forensic checks: font changes, copied chromatograms, and lot numbers that appear on multiple products.

## Deviations, CAPA and Supplier Queries

A deviation is any departure from the specification, the procedure, or the expected document set. It should be recorded even when the material is accepted. The record should state what happened, what was affected, what was done, and who decided.

A supplier query is not a deviation, but it should be tracked like one. Log the date of the query, the question, the response, and the closure. A supplier that answers with a new certificate and no explanation has not closed the query. A supplier that answers with raw data, a root cause, and a corrective action has.

CAPA is the formal step for a recurring issue. If the same document is missing on three shipments, the problem is the supplier's release process, not the receiving clerk's memory. The CAPA should address the supplier's process, the buyer's verification step, or both.

Escalation criteria should be written before the first shipment. A falsified document, a lot mismatch, or a sterility claim without a report should trigger an immediate hold. A late certificate or a missing packing list can be handled with a query. The distinction keeps the team from overreacting to paperwork and underreacting to integrity findings.

## Document Control: Naming, Versioning, Retention

A file name should carry the study, the product, the lot, the document type, and the date. A scheme such as `STUDY-042_IPAMORELIN_LOT-2026-0312_COA_2026-04-18.pdf` is searchable and sortable. A scheme based on the supplier's file name is neither.

Version control applies to the specification and the receiving form, not to the certificate. The certificate is a record of a lot and should not be revised. If a supplier issues a corrected certificate, keep both versions and record why the correction was made.

Retention should be defined by the study's regulatory framework and the institution's policy. A common minimum for research records is the study duration plus the retention period required by the funding agreement or the institution. For regulated studies, the sponsor's requirement may be longer. The file should record the retention decision, not just the date.

Backups matter as much as retention. A scanned file on one laptop is not a record. Store the file in the study's controlled repository, with access controls and a backup schedule. If the repository is cloud-based, confirm the data residency and access rules before uploading.

## The Ten Most Common Audit Findings

| Finding | Why it happens | Preventive control |
| --- | --- | --- |
| Lot number missing from receiving record | Clerk records the order number instead | Required field in the receiving form |
| Certificate stored under order number | Filing follows procurement, not lot | Lot-based folder structure |
| Temperature logger never downloaded | Packaging discarded at receiving | Logger download step in SOP |
| Purity recorded without method | Certificate summary copied into log | Method field required in review |
| Expiry or retest date absent | Supplier certificate omits it | Query before acceptance |
| Two lots used, one documented | Replacement vial opened without log entry | Lot-change entry in study record |
| Supplier query not closed | Email thread archived, no status | Query log with closure date |
| Corrected certificate overwrites original | File replaced on receipt | Versioned file naming |
| Retention period not recorded | Policy assumed, not documented | Retention field in file index |
| Scanned file not backed up | Local drive only | Controlled repository and backup check |

Most of these are process findings, not chemistry findings. They are also the findings that take the longest to resolve during an audit, because the missing record cannot be recreated after the fact. A receiving team that wants a specification reference for the product side can use the [catalog](/catalog/), and the [FAQ](/faq/) covers the order and shipping documents that should arrive with a shipment.

## The Author's Take

**Position.** Build the lot file at receiving, not at audit. The hour spent linking the certificate to the vial is the cheapest hour in the study. The same hour spent reconstructing the link two years later costs a week and may end with an unanswerable question.

**Reasoning.** Documentation failures are rarely caused by a lack of documents. They are caused by documents that do not join: a certificate without a lot, a receiving log without a temperature, a study record without a lot change. The join is the work. A team that designs the receiving form around the lot number, and the file structure around the same number, removes most of the failure modes before they occur. The analytical science can be excellent and still be unusable in an audit if the paper chain does not connect.

**Disclosure.** Peptides of China sells research peptides. This article is a documentation and procurement judgment, not an effects claim. All compounds are for research use only and are not for human or veterinary use.

## Sources

1. 21 CFR 211.194, Laboratory records. https://www.ecfr.gov/current/title-21/chapter-I/subchapter-C/part-211/subpart-J/section-211.194
2. 21 CFR 211.192, Production record review. https://www.ecfr.gov/current/title-21/chapter-I/subchapter-C/part-211/subpart-J/section-211.192
3. U.S. FDA, Data Integrity and Compliance With Drug CGMP: Questions and Answers (2018). https://www.fda.gov/regulatory-information/search-fda-guidance-documents/data-integrity-and-compliance-drug-cgmp-questions-and-answers
4. ICH Q2(R2), Validation of Analytical Procedures (2023). https://database.ich.org/sites/default/files/ICH_Q2%28R2%29_Guideline_2023_1130.pdf
5. ICH Q1A(R2), Stability Testing of New Drug Substances and Products. https://www.ich.org/page/quality-guidelines
6. USP &lt;1058&gt;, Analytical Instrument Qualification. https://doi.org/10.31003/uspnf_m1124_10101_01
7. USP &lt;1225&gt;, Validation of Compendial Procedures. https://doi.org/10.31003/uspnf_m99945_40101_01
8. U.S. Customs and Border Protection, Basic Import and Export. https://www.cbp.gov/trade/basic-import-export
