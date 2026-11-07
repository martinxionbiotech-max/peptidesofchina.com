---
title: "Peptide Quality Assurance Process: A Researcher's Guide to Sourcing Integrity"
slug: "peptide-quality-assurance-process-a-researchers-guide-to-sourcing-integrity"
description: "A working QA process for research peptides: who owns each decision, how supplier qualification and incoming inspection work, what a batch release review covers, and how deviations, CAPA, change control, and annual product review close the loop."
---
A peptide quality assurance process is a set of assigned decisions, each with a named owner, a defined evidence requirement, and a documented failure path. It answers five questions for every lot: whether the supplier was qualified, whether the shipped material matches the written specification, whether the batch record supports release, whether any deviation was investigated before release, and whether a change since the previous lot affects the result. A folder of certificates answers none of them, because a certificate records a result while QA records a decision.

This guide covers the buyer's side: a laboratory, procurement group, or distributor receiving research material from a Chinese manufacturer. It assumes a research chemical for laboratory use, not a medicinal product, so the buyer's own file is the quality system of record rather than a regulatory release. The [research peptide specification standard](/blog/research-peptide-quality-standards-2026-guide/) sets out what each test means.

## What a Peptide QA Process Actually Decides

Five decisions carry most of the risk.

The first is supplier approval: whether a specific site, not a brand, may supply a specific product. The second is specification approval: the versioned attributes and acceptance ranges the lot will be judged against. The third is lot release: whether the material in hand may enter inventory. The fourth is deviation disposition: whether an out-of-specification result, a documentation gap, or a handling excursion is acceptable, and on what basis. The fifth is continued approval: whether the supplier stays on the approved list after the year's record is reviewed.

Each decision needs a record of who decided, when, on what evidence, and against which specification version. If a reviewer cannot reconstruct that chain, the decision did not happen in any useful sense.

Regulatory frameworks are reference material here, not obligations. ICH Q10 describes a pharmaceutical quality system built on four elements: process performance and product quality monitoring, corrective and preventive action, change management, and management review; a research buyer can adopt the same four at smaller scale without claiming GMP status. ISO 9001:2015 clause 8.4 covers externally provided processes and clause 8.7 covers nonconforming outputs.

## QA, QC, and the Release Authority

Quality control measures. Quality assurance decides what the measurement means for the batch. The distinction is not academic: a laboratory can produce a valid chromatogram and still release a lot that should have been rejected, because nobody was assigned the release decision.

ICH Q7 section 2.1 requires a quality unit with the authority to approve or reject materials and batches, independent of production. Research material does not fall under Q7, but the structural lesson transfers. Whoever runs the assay should not be the only person who signs the release. In a two-person laboratory, that means a second reviewer; in a larger group, a QA function separate from the bench.

Name the release authority in a document. The record should state the individual, their role, the specification version, and the disposition. A release signed by "the lab" is not a release.

Apply the same test to testing vendors: an ISO/IEC 17025-accredited laboratory documents method validation and traceability, while one that reports results without an accreditation scope does not. [Third-party testing](/blog/peptide-testing-and-analysis-a-professional-guide-to-laboratory-verification/) covers selection.

## The QA Responsibility Matrix

A matrix prevents the common failure where several people believe someone else owns a check. The table is a workable default for a research group receiving peptide lots; adapt the titles, keep one accountable owner per row.

| Decision or activity | Accountable owner | Approver | Record produced | Cadence |
| --- | --- | --- | --- | --- |
| Supplier approval | Procurement lead | QA reviewer | Approved supplier file | Before first order; reviewed every 12 months |
| Specification approval | Laboratory lead | QA reviewer | Versioned specification | Per product; on any change |
| Incoming inspection | Receiving technician | Laboratory lead | Receiving log and sample record | Every lot |
| Identity and purity testing | Analyst | Laboratory lead | Analytical report | Every lot, or per sampling plan |
| Batch record review | QA reviewer | Quality lead | Release checklist | Every lot, before use |
| Deviation handling | Assigned investigator | Quality lead | Deviation report | Per event; investigation within 5 business days |
| CAPA | CAPA owner | Quality lead | CAPA record and effectiveness check | Per event; check at 90 days |
| Change control | Supplier contact and buyer QA | Quality lead | Change request and impact assessment | Per change; 30 days' notice |
| Annual product review | QA reviewer | Quality lead | Annual review report | Every 12 months |
| Retention samples | Laboratory technician | Laboratory lead | Retention inventory | Every lot; reconciled quarterly |

Two rules make the matrix work. The approver must see the primary evidence, not a summary from the accountable owner. An approver who signs without commenting on the exceptions is not reviewing, and the file will show it.

## Supplier Qualification Before the First Order

Qualification starts with a scope question: which legal entity, at which address, made the material. A trading company's certificate from a partner factory does not qualify the trading company to release your lot, nor the factory unless the factory is named.

A three-tier model:

- **Critical tier.** Material for a study that cannot be repeated, or a product with a narrow specification. Full questionnaire, document review, and an on-site or remote audit before approval. Reassess every 12 months.
- **Standard tier.** Recurring catalog purchases. Questionnaire plus document review, with an audit at 24 months or on trigger. Reassess every 24 months.
- **Low-risk tier.** Small, one-off purchases for exploratory work. Desk review only, reassessed every 36 months.

Score the questionnaire rather than reading it. A 40-item form covering site identity, quality unit structure, batch record retention, deviation handling, change notification, analytical methods, and retention samples gives a comparable result. Pass at 80% with no critical item unanswered; a supplier that will not answer the quality section fails regardless of the total.

Ask for three consecutive lots of batch records, twelve months of deviation and complaint records, and every change control that touched the product. Those requests cost the supplier real effort, which is itself informative. Bulk orders concentrate the risk, since one qualification decision then covers many lots; [wholesale sourcing](/blog/wholesale-peptides-a-2026-b2b-sourcing-guide-for-research-institutions/) covers the commercial side, and the [supplier GMP assessment guide](/blog/how-to-assess-peptide-supplier-gmp-compliance-in-2026/) covers certificate scope and audit evidence.

Keep an approved supplier list with the approval date, scope, tier, and review date, and review it twice a year. Two consecutive out-of-trend lots, a site change, or a failed regulatory inspection should trigger an out-of-cycle review within 30 days.

## Incoming Inspection and Sampling

Receiving is the last point where a problem can be caught cheaply. Quarantine every lot on arrival: physically separate it, mark it, and do not draw material for a study until release.

Inspect 100% of the shipment for vial count, label legibility, lot number, fill appearance, cake collapse, and container integrity. If the shipment carried a temperature logger, attach the trace to the receiving record; an excursion above 8 °C for more than two hours is a deviation, not a note.

Sample by a defined plan. A common rule is the square root of the number of vials plus one, capped at ten vials; for a ten-vial shipment that is four. Take samples from different positions in the carton, not from the top layer. Retain at least two unopened vials from every lot.

Write acceptance criteria into the specification, not after the result arrives. Typical research-grade limits:

- Identity by ESI-MS within ±0.5 Da at unit resolution, with charge states annotated.
- Purity by RP-HPLC at 220 nm of at least 98.0% area, with resolution between the main peak and nearest impurity of at least 1.5.
- Water by Karl Fischer of no more than 5.0% w/w.
- Endotoxin by LAL of no more than 5 EU/mg where the supplier claims a limit; [endotoxin testing](/blog/endotoxin-testing-peptide-manufacturing/) explains the assay formats.
- Injection precision of RSD no more than 2.0% across six replicate injections before any purity figure is accepted.

Release within five business days of sampling or place the lot on hold with a written reason. An item in quarantine for a month has effectively been released by default; someone will use it.

## Batch Record Review and Lot Release

Review the batch record for every lot, not a sample. The review compares what the manufacturer says it did against the specification and against the analytical results for the same lot number.

Read for internal consistency rather than completeness. Does the synthesis scale match the reported yield? Does the purification date follow the cleavage date? Is the lyophiliser identified and qualified at the time of the run? Does the lot number on the certificate match the vial label? A record that reports a 60% yield from a 5 mmol scale and ships 200 grams is describing two different runs.

A 24-line checklist with two signatures is enough for most programs. The table below is a condensed version. The [CoA reading guide](/blog/how-to-read-a-peptide-coa-a-researchers-guide-to-hplc-and-ms-reports/) covers the document-level checks, and the [peptide documentation package](/blog/peptide-documentation-package/) guide lists the full set.

| Release check | Evidence reviewed | Pass condition | Owner |
| --- | --- | --- | --- |
| Lot linkage | Vial label, certificate, packing list, batch record | All four carry the same lot number | QA reviewer |
| Specification version | Purchase order and specification file | Version matches the one approved for the product | QA reviewer |
| Batch record completeness | Signed record extract | No blank fields; operator and reviewer signatures dated | QA reviewer |
| Identity | Mass spectrum with charge states | Within ±0.5 Da of theoretical mass | Analyst |
| Purity | Chromatogram with method header | At least 98.0% area at 220 nm; resolution at least 1.5 | Analyst |
| Water and counterion | Karl Fischer and ion chromatography | Water no more than 5.0% w/w; counterion within salt-form range | Analyst |
| Peptide content | Amino acid analysis or mass balance | 70–95% of fill mass, consistent with the salt form | Analyst |
| Endotoxin, if claimed | LAL report with method and limit | No more than 5 EU/mg | Analyst |
| Deviation status | Deviation log for the lot | All investigations closed before release, or a documented concession | Quality lead |
| Change status | Change control log | No unapproved change to route, site, or method since the last lot | Quality lead |
| Retention sample | Retention inventory entry | Two vials logged at the stated storage condition | Laboratory lead |
| Label check | Physical label | Product name, lot, fill mass, storage condition, research-use statement | Receiving technician |

Four dispositions exist: release, release with a documented concession, reject, or hold. A concession is legitimate when the attribute does not affect the intended assay and the deviation is closed; it is not legitimate when the attribute is identity.

## Deviations, CAPA, and Change Control

A deviation is any result or event that departs from the specification or approved procedure. The system's value is whether a deviation is detected before release and whether the fix holds.

Classify by impact. Critical covers wrong identity, a contaminated or mislabelled lot, or a sterility claim that cannot be supported. Major covers purity below specification, a missing release record, or a temperature excursion with no supporting stability data. Minor covers labelling errors that do not affect identity or use.

Workable timelines: contain within 24 hours, open the investigation within one business day, complete the root-cause analysis for a major deviation within five business days, and close within 30 days. Extensions to 60 days are acceptable with a written justification and an interim control. A deviation closed after the material has been used is a finding regardless of the conclusion.

Corrective and preventive action follows the investigation. The corrective action addresses the specific event; the preventive action addresses the system that allowed it. An effectiveness check at 90 days with a measured result is the minimum evidence that the fix worked. Review recurrence at 12 months.

| Step | Action | Owner | Timeline | Output |
| --- | --- | --- | --- | --- |
| 1 | Detect and contain; quarantine affected vials | Receiving or analyst | Within 24 hours | Hold notice and segregation record |
| 2 | Classify severity and assign investigator | Quality lead | 1 business day | Deviation record with class |
| 3 | Establish root cause with evidence | Investigator | 5 business days for major | Root-cause statement |
| 4 | Assess batch impact and release status | QA reviewer and laboratory lead | Before any release decision | Impact assessment |
| 5 | Define corrective and preventive actions | CAPA owner | 30 days | CAPA plan with owners and dates |
| 6 | Verify implementation | Quality lead | At due date | Closure evidence |
| 7 | Check effectiveness | QA reviewer | 90 days after closure | Measured effectiveness result |
| 8 | Trend and review | QA reviewer | Annual product review | Trend chart and recurrence rate |

Change control is where quiet failures accumulate. A supplier can switch resin vendors, shorten a lyophilisation cycle, or move fill and finish to another building without changing the catalog listing. Classify changes as major (site, route, purification method, specification), moderate (equipment, excipient source, fill provider), or minor (documentation, packaging). Require 30 days' written notice, an impact assessment before implementation, and revalidation where the change touches identity, purity, or stability. A change approved after the fact is a deviation.

Put the notification clause in the purchase agreement, not an email thread. The [manufacturer verification protocol](/blog/china-peptide-manufacturer-verification-a-2026-b2b-sourcing-protocol/) covers the supplier-identity checks that sit alongside this clause.

## Annual Product Review, Retention Samples, and the Archive

The annual product review turns a year of lot records into a judgment about the supplier. Run it within 60 days of period close and cover every lot received.

Include at least these metrics: lots received and released, lots rejected or conceded, deviations per lot, out-of-specification rate by test, complaint count and category, CAPA opened and closed, on-time CAPA closure against a 90% target, change controls approved, audit status, and retention inventory accuracy. A supplier with zero deviations across a year of production is not a good supplier; it is a supplier whose deviation system is not capturing events.

The review produces one of three outcomes: continued approval, conditional approval with a review date, or removal from the list. Record the reasoning; a review that concludes "acceptable" without a metric table is a formality.

Retention samples close the loop on traceability. Keep two unopened vials per lot at −20 °C, protected from light, for 12 months beyond the retest date or 24 months from receipt, whichever is longer. Log the lot, fill mass, location, and date; reconcile quarterly; a retention sample that cannot be found is a traceability failure even if the batch was fine.

The archive holds the rest: batch record extracts, certificates, analytical raw data, deviation and CAPA records, change controls, audit reports, and annual reviews. Keep batch-level records for at least five years, or the life of the study plus two years if longer. A reviewer should be able to retrieve a lot file in one sitting, and access controls should prevent edits without a trace. FDA's data integrity guidance describes the audit-trail and account expectations; the same principles apply at laboratory scale.

## The Author's Take

**Position.** QA is a decision log, not a document collection. The buyer's own release decision is the quality event that matters, and it should be signed by a named person against a versioned specification before the vial is opened.

**Reasoning.** Most sourcing failures I have seen were not analytical. The assay was fine; the process around it was missing. A certificate arrived for a lot never linked to the vial. A purity figure was accepted without a method. A deviation was resolved by email after the material entered a study. Each was a decision nobody owned. The fix is unglamorous: a matrix, a checklist, a few timelines, and an annual review that happens whether or not anything went wrong. The analytical work is necessary; the decision structure is what makes it count.

**Disclosure.** Peptides of China sells research peptides. This article is sourcing judgment, not an effects claim, and all compounds discussed are for research use only. No document set, supplier audit, or testing protocol guarantees the quality of a batch; each reduces a specific risk and leaves a residual one that the buyer retains.

## Sources

1. ICH Q7, Good Manufacturing Practice Guide for Active Pharmaceutical Ingredients. European Medicines Agency. https://www.ema.europa.eu/en/ich-q7-good-manufacturing-practice-active-pharmaceutical-ingredients
2. ICH Q9(R1), Quality Risk Management. European Medicines Agency. https://www.ema.europa.eu/en/ich-q9-quality-risk-management
3. ICH Q10, Pharmaceutical Quality System. European Medicines Agency. https://www.ema.europa.eu/en/ich-q10-pharmaceutical-quality-system
4. ISO 9001:2015, Quality management systems — Requirements. International Organization for Standardization. https://www.iso.org/standard/62085.html
5. USP &lt;1058&gt;, Analytical Instrument Qualification. United States Pharmacopeia. https://doi.org/10.31003/uspnf_m1124_10101_01
6. USP &lt;1225&gt;, Validation of Compendial Procedures. United States Pharmacopeia. https://doi.org/10.31003/uspnf_m99945_40101_01
7. 21 CFR Part 211, Current Good Manufacturing Practice for Finished Pharmaceuticals. U.S. Government Publishing Office. https://www.ecfr.gov/current/title-21/chapter-I/subchapter-C/part-211
8. Data Integrity and Compliance With Drug CGMP: Questions and Answers. U.S. Food and Drug Administration. https://www.fda.gov/regulatory-information/search-fda-guidance-documents/data-integrity-and-compliance-drug-cgmp-questions-and-answers
9. Process Validation: General Principles and Practices. U.S. Food and Drug Administration. https://www.fda.gov/regulatory-information/search-fda-guidance-documents/process-validation-general-principles-and-practices
10. PIC/S Guide to Good Manufacturing Practice for Medicinal Products (PE 009). Pharmaceutical Inspection Co-operation Scheme. https://picscheme.org/en/publications
