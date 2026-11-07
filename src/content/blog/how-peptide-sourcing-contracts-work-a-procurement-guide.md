---
title: "How Peptide Sourcing Contracts Work: A Procurement Guide"
slug: "how-peptide-sourcing-contracts-work-a-procurement-guide"
description: "How peptide sourcing contracts work: commercial terms, quality agreement clauses, specifications, sampling, and a rejection workflow that holds up under dispute."
---
A peptide sourcing contract works as four documents in one system: a commercial supply agreement, a quality agreement, a versioned specification with test methods, and a lot release package. The commercial agreement sets price, volume, delivery, and liability. The quality agreement assigns who releases, who investigates, who notifies, and who pays for a failure. The specification fixes the numbers. The release package proves a specific lot met them. Deals break when one document is asked to do another's job: a purchase order defining a purity method, or a certificate of analysis treated as a contract.

This article is commercial background for research procurement teams, not legal advice; have contract language reviewed by counsel qualified in the governing law you choose. The terms below are negotiating positions, not statements of what a court will enforce, and the analytical limits are defaults, not regulatory requirements for a research chemical.

## The four-document structure and why merging it fails

The commercial supply agreement covers the buyer and seller entities, product definition, quantities, price, delivery terms, payment, lead time, and remedies.

The quality agreement covers manufacturing and release responsibilities. ICH Q7 section 16 treats contract manufacturing as a defined activity requiring a written agreement, and the same logic applies to contract testing and fill. The agreement names the quality unit that releases each lot, the notification windows, audit rights, and record retention.

The specification is the technical annex: sequence, salt form, presentation, test methods, acceptance limits, version number, and date.

The lot release package is transaction-level evidence: a certificate of analysis for the lot, a batch record extract, deviation status, and the label proof. It belongs to one shipment, not to the relationship.

Two clauses keep the set coherent. An order of precedence clause names the order — quality agreement, specification, commercial agreement, purchase order — with the specification controlling analytical disputes. A documents clause states that a lot is not deliverable until the release package is complete. A shipment without a lot-specific certificate is a warehouse problem, not a quality record.

Where a supplier sells through a trading entity, name both roles in the contract; the [manufacturer verification protocol](/blog/china-peptide-manufacturer-verification-a-2026-b2b-sourcing-protocol/) explains how to test whether the invoicing entity, certificate issuer, and synthesis site agree.

## Commercial terms that decide whether the contract is usable

Pricing is the easy part. The terms that generate disputes are quantity tolerance, delivery risk, documentation timing, and the inspection window.

Set a quantity tolerance explicitly, for example ±5% on bulk orders and exact counts on vial kits, with the price adjusted pro rata. Without a tolerance, a 98-gram shipment against a 100-gram order is a breach; with one, it is a delivery. State whether the tolerance applies to ordered mass, filled mass, or peptide content; those are three different numbers.

Use Incoterms 2020 by name and place, for example DAP Frankfurt or FOB Shanghai. Incoterms allocate transport cost and risk, not conformity, title, or governing law. A DAP term with the seller bearing risk to destination is easier to administer than "door delivery", especially with cold-chain excursions.

A common structure is 30% deposit with the purchase order and 70% against a complete document set before release of the airway bill.

Write a late-delivery credit as a formula: 0.5% of order value per full week late, capped at 5%, with termination available after four weeks. A credit that requires proving loss is a credit nobody claims.

**Table 1. Contract-term checklist for a peptide supply agreement**

| Term | What to write | Workable default |
| --- | --- | --- |
| Parties | Legal name, registration number, signatory authority, notice address | Seller and manufacturer if different |
| Product | Sequence, salt form, presentation, fill mass, catalog code | Specification version and date |
| Quantity | Ordered units, tolerance, adjustment mechanism | ±5% on bulk; exact count on kits |
| Price | Currency, unit basis, validity, index trigger | Fixed for 12 months; review at renewal |
| Delivery | Incoterms rule and place, packaging, cold chain | DAP destination; validated shipper with data logger |
| Payment | Deposit percentage, milestone documents, currency | 30% deposit, 70% against documents |
| Documentation | CoA, batch record extract, packing list, origin statement | CoA before shipment; batch record in 5 business days |
| Inspection | Acceptance window and notice method | 30 calendar days from receipt, written notice |
| Late delivery | Credit formula, cap, termination right | 0.5% per week, 5% cap, termination after 4 weeks |
| Termination | Convenience notice, cause cure period, surviving clauses | 90 days convenience; 30 days cure; quality clauses survive |

Most templates get negotiated at the price cell and nowhere else. The [contract negotiation checklist](/blog/peptide-supplier-contract-negotiation-tips-for-procurement/) covers the clauses that are most often left blank, and [blanket purchase orders](/blog/how-blanket-purchase-orders-work-peptides/) are a better fit than repeated one-off contracts when volumes are stable.

## Specifications: the numbers that make a contract enforceable

A specification without methods and limits is a description. A specification with them is an enforceable annex, provided it is versioned and signed.

For a lyophilized research peptide, a defensible minimum set is:

- **Identity** by reversed-phase HPLC retention time against a reference standard, plus intact mass by LC-MS within ±0.5 Da on a unit-mass instrument or 50 ppm on a high-resolution instrument.
- **Purity** by RP-HPLC at 214 nm, reported as area percent, with column, gradient, flow, temperature, injection volume, and integration threshold stated. A common release limit is 98.0% area, with a separate limit for the largest single impurity.
- **Water content** by Karl Fischer titration, typically 8.0% or lower for lyophilized powder.
- **Peptide content** by amino acid analysis or nitrogen determination, with a range such as 80.0% to 92.0% by mass. This is the number that reconciles a 98% chromatographic purity with the mass of peptide in the vial.
- **Counterion** by ion chromatography where the salt form matters, for example trifluoroacetate at 1.0% or lower.
- **Endotoxin** only if the intended research use requires it, expressed as EU/mg with the test method named.

State the retest period and storage condition: for example 24 months at -20 °C, protected from light, with desiccant, long enough to cover the study.

Version control is what makes the annex usable in a dispute. Put a version number and effective date on the specification, attach the signed PDF to the order, and require 30 days' written notice plus buyer approval before any limit, method, or salt form changes. Without that baseline, a silent revision cannot be proved. The [research peptide quality standards guide](/blog/research-peptide-quality-standards-2026-guide/) sets out how to freeze a specification at the research-use level without borrowing pharmaceutical limits that do not apply.

A certificate reporting 98% purity and one reporting 98% peptide content describe different measurements; the [CoA reading guide](/blog/how-to-read-a-peptide-coa-a-researchers-guide-to-hplc-and-ms-reports/) explains the fields, and the distinction belongs in the specification.

## The quality agreement: assign every activity to a named role

A quality agreement is a responsibility map, not a second copy of the commercial contract: every activity in the manufacturing and release chain needs one owner, a notification clock, and a record.

Write the clauses as testable commitments rather than intentions. "Supplier will notify buyer of deviations" is not testable. "Supplier will notify buyer's quality contact within 48 hours of classifying a critical deviation, and within 10 business days for major deviations, with batch number, affected quantity, and interim disposition" is testable.

**Table 2. Quality-agreement clauses and the commitment to write**

| Clause | Owner | Testable commitment |
| --- | --- | --- |
| Batch release | Supplier quality unit | Named release function, specification version, release date on the CoA |
| Deviation notification | Supplier quality unit | Critical within 48 hours; major within 10 business days; log on request |
| OOS investigation | Supplier quality unit | Root cause, batch impact, CAPA, closure before or after release stated |
| Change control | Supplier | 30 days' prior written notice of site, route, resin, column, fill provider, or specification change; buyer approval |
| Complaints | Both parties | Acknowledge within 5 business days; written response within 30 days |
| Audit rights | Buyer | Annual desk or on-site audit, 30 days' notice; for-cause audit within 10 days |
| Retention samples | Supplier | Two vials per lot, labelled and stored at the labelled condition, held 12 months past retest |
| Sub-tier suppliers | Supplier | Approved vendor list and audit status for resin, amino acids, and fill provider on request |
| Records | Supplier | Batch records and release documents retained 5 years, or longer by law |

Two clauses are commonly missing: an escalation path naming a quality contact on each side with a 30-day resolution window before commercial dispute proceedings, and a consequence clause covering open orders if the quality agreement is terminated for cause. Without the second, a buyer can be locked into shipments from a supplier it has just disqualified.

The [GMP compliance assessment guide](/blog/how-to-assess-peptide-supplier-gmp-compliance-in-2026/) covers how to read the audit evidence behind these commitments. ICH Q7 remains the reference for API documentation and contract manufacturing, and ISO 9001:2015 clause 8.4 covers control of externally provided processes, the quality-system analogue.

## Sampling and lot acceptance: write the rule before you test

Sampling is where a good document chain separates from the goods. Decide the plan before shipment and record it in the quality agreement.

For a 10-vial kit, test one vial, retain one unopened vial, and hold a third as a referee. For bulk powder, sample the square root of the container count plus one, rounded up, with a minimum of three containers, taking a top, middle, and bottom increment from each. Record the sampler, date, container identifiers, and a sample ID different from the supplier's lot code, and keep a mapping.

Lot acceptance criteria should be numeric and complete:

- Mean purity across sampled vials at or above 97.0% area, with no individual vial below 95.0%.
- Identity confirmed on at least one vial per lot, with the mass spectrum retained.
- Water content within the specification limit on the tested vial.
- Visual inspection pass: intact cake or powder, no discoloration, no visible particulates, vial and stopper intact.
- Label, certificate, packing list, and batch record lot codes reconciled.

A single failing unit triggers a retest on double the original sample size from the retained vials. Two failures in the retest reject the lot. Choose the rule after the result and the test becomes a negotiation.

Retention is part of acceptance: keep two vials per lot at the labelled condition for the study duration plus 12 months, labelled with lot, receipt date, study code, and sample ID. A retained vial without a location and custodian is just a vial in a drawer.

## Rejection, retest, and replacement: a workflow with clocks

Rejection fails procedurally more often than technically: late testing, verbal notice, a return without an RMA, or destruction before inspection. A written workflow with dates prevents each.

**Table 3. Acceptance and rejection workflow**

| Stage | Clock | Action | Record |
| --- | --- | --- | --- |
| Receipt | Day 0 | Inspect packaging, temperature logger, vial condition; quarantine | Receiving report and photographs |
| Testing | Days 1 to 30 | Test per specification; retain samples | Analytical report and raw data |
| Notice | By day 30 | Written nonconformity: lot, method, result, photos | Email to quality contact; read receipt |
| Acknowledgement | Within 10 business days | Supplier accepts, disputes, or requests samples; RMA issued | RMA number and return instructions |
| Investigation | Days 31 to 60 | Joint review, or referee laboratory on the retained vial | Investigation report |
| Disposition | Within 30 days of acceptance | Replacement, credit, or refund; no consequential damages | Credit note or replacement lot record |
| Closure | By day 100 | Confirm replacement lot meets specification; update supplier score | Supplier file and CAPA |

Three details make it enforceable: notice runs from receipt; supplier silence past the acknowledgement window counts as acceptance; and the ISO/IEC 17025-accredited referee laboratory is named in the contract, its result binding, with the losing party paying.

Do not return or destroy a rejected lot until disposition is agreed in writing. Keep the carton, temperature logger, and vial labels; they show whether the failure happened in transit or in your freezer. The [documentation package checklist](/blog/peptide-documentation-package/) lists the records to keep together, and [supplier KPIs](/blog/procurement-kpis-for-peptide-sourcing-2026-guide/) turn repeated rejection events into a number that appears at the annual review.

## Warranty, indemnity, confidentiality, and IP

The warranty should say three things: the lot conforms to the specification at release, it will remain within specification through the stated retest period when stored as labelled, and the seller has the right to sell it. A 12-month warranty from delivery, or until the labelled retest date, whichever comes first, is reasonable for a research chemical. Anything shorter shifts the risk of degradation back to a buyer who does not control manufacturing.

Indemnity is usually mutual: the supplier covers third-party claims arising from a manufacturing defect, a specification failure, or an IP claim over its process; the buyer covers claims from its own use, handling, or combination of the material. Cap the indemnity at amounts paid in the preceding 12 months and exclude consequential and lost-profit damages, with carve-outs for gross negligence, wilful misconduct, and confidentiality breach. A cap with no carve-outs is cheap for the supplier and nearly worthless for the buyer.

Confidentiality should run five years after termination, with trade secrets protected while they remain secret. Carve out information already public, independently developed, received without restriction, or legally compelled with prior notice where lawful. Include analytical data and batch records in the definition: a supplier's other customers are the last people who should read a custom sequence.

Intellectual property splits three ways. The supplier retains background process knowledge: synthesis routes and purification methods. The buyer owns project data from its own sequence, including assay results and reports. Jointly developed improvements need a stated owner or licence, not a vague reference to cooperation. Add a no-implied-licence clause, a ban on reselling a custom compound to third parties, and exclusivity if the sequence is commercially sensitive. Freedom-to-operate searches belong to the buyer and should be excluded from the supplier's warranties.

## Governing law, arbitration, and force majeure

The CISG applies by default to international sales between parties in different contracting states; China is one. It requires the buyer to examine goods promptly and give notice of non-conformity within a reasonable time, with a two-year outer limit unless the contract sets another period — a reason to write the 30-day inspection window into the contract. If you want domestic sales law instead, exclude the CISG expressly in the governing-law clause.

For US buyers, UCC Article 2 supplies gap-fillers for domestic goods sales, including notice of breach within a reasonable time. The UCC and CISG answer different questions, so name one and exclude the other in a cross-border deal.

Match dispute resolution to deal size: ICC arbitration seated in Hong Kong, Singapore, or London, in English, with a sole arbitrator below USD 1 million and three above. China and most trading partners are New York Convention parties, which supports enforcement in more than 170 states. Keep a court carve-out for injunctive relief; an arbitration clause that blocks emergency relief is a liability.

Force majeure needs a definition, a notice clock, and an exit. The ICC Force Majeure Clause 2020 provides a usable structure: the affected party notifies without undue delay, evidences the impediment, and mitigates. Write a 14-day notice requirement with documentary evidence, suspension rather than automatic termination, and a right for either party to terminate if the event continues beyond 90 days. Exclude market price movements, currency fluctuation, and ordinary freight cost increases; those are commercial risks.

## The Author's Take

**Position.** A peptide contract is a document-linkage system, and the quality agreement is the part most buyers under-negotiate.

**Reasoning.** In the disputes I have seen, the failure is rarely that a supplier cannot synthesise a peptide. It is that nobody wrote down who owns the release decision, who pays for a referee assay, or what happens when a lot arrives without a batch record. Those gaps are cheap to close before signature and expensive to argue after a failed shipment. The specification tells you what you bought, the quality agreement tells you who is responsible when it is wrong, and the release package tells you whether this lot is the one you bought. A buyer who negotiates price for three weeks and signs the quality template in an afternoon has optimised the least risky term.

**Disclosure.** Peptides of China sells research peptides. This article is a sourcing judgment, not a claim about the effects of any compound, and all products discussed are for research use only. Nothing here is legal advice; enforceability depends on the governing law, the signatories, and the facts of a specific dispute.

## Sources

1. ICC Model International Sale Contract. International Chamber of Commerce. https://iccwbo.org/resources-for-business/model-contracts-clauses/icc-model-international-sale-contract/
2. ICC Force Majeure Clause 2020. International Chamber of Commerce. https://iccwbo.org/resources-for-business/model-contracts-clauses/icc-force-majeure-clause/
3. Incoterms 2020. International Chamber of Commerce. https://iccwbo.org/business-solutions/incoterms-rules/incoterms-2020/
4. United Nations Convention on Contracts for the International Sale of Goods (CISG). UNCITRAL. https://uncitral.un.org/en/texts/salegoods/conventions/sale_of_goods/cisg
5. Uniform Commercial Code Article 2, Sales. Cornell Legal Information Institute. https://www.law.cornell.edu/ucc/2
6. ISO 9001:2015, Quality management systems — Requirements. International Organization for Standardization. https://www.iso.org/standard/62085.html
7. ICH Q7, Good Manufacturing Practice Guide for Active Pharmaceutical Ingredients. European Medicines Agency. https://www.ema.europa.eu/en/ich-q7-good-manufacturing-practice-active-pharmaceutical-ingredients
8. ISO/IEC 17025:2017, General requirements for the competence of testing and calibration laboratories. International Organization for Standardization. https://www.iso.org/standard/66912.html
9. UNCITRAL Model Law on International Commercial Arbitration. UNCITRAL. https://uncitral.un.org/en/texts/arbitration/modellaw/commercial_arbitration
10. UNIDROIT Principles of International Commercial Contracts 2016. UNIDROIT. https://www.unidroit.org/instruments/commercial-contracts/unidroit-principles-2016/
