---
title: "Peptide Supplier Contracts: Terms Procurement Should Fix"
slug: "peptide-supplier-contract-negotiation-tips-for-procurement"
description: "The clauses that decide whether a peptide order is recoverable: specification, sampling, acceptance window, change control, and nonconformance remedies."
author: "POC Tech Team"
---
**A peptide supply contract is only as strong as its specification clause.** Price, lead time, and payment terms get negotiated because they are visible. The clauses that decide whether a failed batch is recoverable — conformity definition, sampling plan, acceptance window, change notification, and remedy — usually get copied from a template written for a different product.

The consequences are asymmetric. A buyer who overpays by three percent loses three percent. A buyer who cannot reject a batch that fails identity loses the order, the study schedule, and the cost of the independent testing that proved the failure.

This article sets out the terms worth fixing before a purchase order is issued, with the convention or statute behind each one. It is commercial drafting guidance for procurement teams, not legal advice; governing law and enforceability vary by jurisdiction, and a contract review should involve counsel in the buyer's jurisdiction.

## Start with the Specification, Not the Price

The specification is the contract's technical center of gravity. Every other clause refers back to it, so an ambiguous specification makes rejection, replacement, and damages arguments unwinnable.

Write the specification as a numbered document with a version, and attach it to the agreement by reference. At minimum it should name the product, the sequence or catalog identifier, the lot size, the purity method with column and gradient, the identity method with mass tolerance, the counterion, the water limit, the fill convention, and the documentation set. The [supplier contract guide](/blog/how-peptide-sourcing-contracts-work-a-procurement-guide/) covers the commercial structure around it.

Two specification habits prevent most disputes.

**Name the method, not just the result.** "Purity ≥98.0% by RP-HPLC, C18 4.6 × 250 mm, 5 µm, 214 nm, gradient 5–65% acetonitrile over 30 minutes, reporting threshold 0.05% area" is testable. "Purity ≥98%" is a negotiation.

**Separate release tests from informational tests.** A COA can report appearance, water content, and net peptide content as information while only purity and identity are release criteria. Marking which is which stops a marginal water result from being used to reject a batch that meets every release specification.

| Clause | What to write | Failure mode if absent |
|---|---|---|
| Specification | Versioned annex with methods and acceptance values | Dispute over whether a result passes |
| Sampling | Plan, sample size, who draws samples | Supplier tests a different vial than the one shipped |
| Acceptance window | Days from receipt to inspect and notify | Late notice waives the claim |
| Change control | Notice period and re-qualification triggers | Silent reformulation between orders |
| Remedy | Replacement, credit, or refund, and timing | Refund conversation with no deadline |
| Records | Retention period and audit access | No evidence to support a claim |

## Conformity, Inspection, and Notice Windows

Under the UN Convention on Contracts for the International Sale of Goods, which governs many China-to-overseas sales unless excluded, conformity is defined in Article 35: goods must match the quantity, quality, and description in the contract, and be fit for the purpose the seller knew or ought to have known. Article 38 requires the buyer to examine the goods within as short a period as is practicable. Article 39 requires notice of a lack of conformity within a reasonable time, and in any event within two years of delivery unless that period conflicts with a contractual guarantee period.

Those articles set the floor, not the ceiling. A contract can shorten the inspection window, and many suppliers do — thirty days is common, ten working days is not unusual. Procurement teams should decide deliberately whether that window is realistic for the test they intend to run. An HPLC plus MS panel at a third-party laboratory often takes longer than ten working days from sample submission, and a notice clause that expires before the result arrives is a clause that has already failed.

Three drafting moves help.

**Start the clock at receipt, not shipment.** The buyer cannot inspect material in transit.

**Define "discovery" for latent defects.** Purity and identity can be tested on arrival; a stability failure or a slow aggregation may appear months later. A clause that preserves claims for latent defects discovered within the retest period is worth more than a longer initial window.

**Preserve the mitigation duty.** Article 77 of the convention requires the buyer to take reasonable steps to mitigate loss. Documenting that rejected material was quarantined and not used supports the claim rather than weakening it.

## Putting Sampling and Acceptance Criteria in the Contract

A specification without a sampling plan is silent on the most common source of disagreement: which vial was tested.

Write the sampling plan into the annex. For lot acceptance, a common structure is a general inspection level with an acceptance quality limit; ISO 2859-1 is the reference standard most quality teams use, and an AQL of 1.0 for major defects is a frequent starting point for packaged goods. For high-value peptide lots, sampling is usually 100% of vials at the documentation level and a smaller analytical subset, because destructive testing consumes inventory.

Define four things explicitly:

1. **Sample location.** Samples drawn from the delivered lot, not from a pre-production or retained batch held by the supplier.
2. **Sample size.** For a 25-vial lot, a √n + 1 convention yields six vials; state whether those are tested or retained.
3. **Retention.** At least two unopened vials per lot, held for the retest period, available for joint re-test.
4. **Tie-breaker.** If the supplier's result and the buyer's result disagree, name the laboratory or the method that decides, and who pays.

The tie-breaker clause is the one buyers most often omit and most often need. A neutral third laboratory, agreed in advance, converts a standoff into a procedure.

## Change Control and Silent Reformulation

A peptide that passed last quarter can fail this quarter without anyone changing the label. Resin supplier, coupling reagent, cleavage cocktail, purification gradient, and fill line can all change. Some changes are minor; some alter the impurity profile enough to invalidate a study.

Ask for a change notification clause with three elements: a notice period before implementation, a list of changes that trigger notification, and a re-qualification requirement for changes that affect the release specification.

A practical threshold set looks like this: any change to the synthesis route, the purification method, the counterion, the fill mass, or the manufacturing site requires notice; changes that alter the analytical profile require a side-by-side batch comparison before shipment. ICH Q7 treats change control as a core GMP expectation for API manufacture, which gives the clause a recognized reference point even when the product is a research reagent rather than a drug.

The notice period is negotiable. Sixty to ninety days is long enough for a buyer to qualify the new material or find an alternative, and short enough that a supplier can accept it.

## Delivery Terms and Where Risk Transfers

Delivery terms decide who owns the goods when something goes wrong in transit, and they interact with the customs clause that buyers often negotiate separately. Incoterms 2020 is the standard reference.

| Term | Risk transfers | Freight and insurance | Import clearance |
|---|---|---|---|
| FOB | When goods are on board the vessel | Buyer arranges | Buyer |
| CIF | When goods are on board the vessel | Seller pays freight and minimum cover | Buyer |
| DAP | At the named place, ready for unloading | Seller arranges | Buyer |
| DDP | At the named place, import cleared | Seller arranges | Seller |

Two points are widely misunderstood. CIF transfers risk at the port of shipment, not at destination, so a buyer who wants protection until delivery should negotiate additional insurance rather than assume the term covers it. DDP places the import burden on the seller, but no supplier can promise that a customs authority will release a shipment; the honest clause describes who bears the cost and delay if clearance fails, not a promise that it will succeed. The [customs sourcing guide](/blog/research-peptide-customs-clearance-a-professional-b2b-sourcing-guide-2026/) covers documentation and the [HS classification note](/blog/hs-code-for-peptides/) explains why tariff codes for peptides need to be checked against the actual product rather than assumed.

Add a title and retention clause as well. Until payment clears, the seller may retain title; the buyer may need a release document to take delivery. Stating both avoids a warehouse standoff.

## Payment Structure and Security

Payment terms are risk allocation in cash form. Three structures are common in peptide sourcing.

**Deposit and balance.** Thirty percent on order, seventy percent against shipping documents. The seller funds part of the production; the buyer retains security until documents are presented.

**Letter of credit at sight.** The bank pays against a document set. It costs a fee and requires precise documents, but it protects both sides when the relationship is new.

**Milestone payments for custom work.** Deposit, mid-project progress payment, balance against release data. This suits custom synthesis where the batch may take eight to twelve weeks.

Whatever the structure, tie each payment to a document rather than a date. A balance due "on completion" is ambiguous; a balance due "against COA, chromatogram, and MS spectrum meeting the specification in Annex A" is testable.

For repeat orders, negotiate a credit line after three clean batches rather than on the first order. The supplier's willingness to extend terms is a useful signal about its confidence in batch consistency.

## Nonconformance Remedies That Actually Work

A remedy clause should answer four questions in order: what counts as a nonconformity, who decides, what the seller must do, and by when.

A workable structure:

- **Notice.** Buyer notifies within the acceptance window with the test report and lot number.
- **Assessment.** Seller responds within ten business days, either accepting the nonconformity or requesting a joint re-test on retained vials.
- **Remedy.** Replacement batch, credit note, or refund, at the buyer's election for a release-test failure.
- **Timing.** Replacement shipped within 30–45 days; refund processed within 30 days of acceptance.
- **Costs.** Seller covers the buyer's reasonable third-party testing cost when the nonconformity is confirmed.

Liquidated damages for late delivery are a separate clause. A rate of 0.5% of order value per week, capped at 5%, is a common negotiating position; it gives the buyer a remedy without requiring proof of loss. Keep the cap low enough that the supplier will accept it, and make sure the clause does not replace the right to cancel after a long delay.

One caution: a remedy that requires the buyer to return material before a replacement ships can leave a laboratory without inventory for weeks. Negotiate a cross-ship for established customers, or at least a partial shipment of the replacement.

## Audit Rights and Record Retention

Audit rights are the clause buyers use least and value most when a batch fails. Two forms are practical.

**Document audit.** The buyer may request batch records, deviation reports, and change history for the specific lot, with confidential information redacted. This is inexpensive and usually sufficient for a research peptide purchase.

**On-site audit.** Once per twelve months, with 30 days' notice, during a scheduled production window, under a confidentiality agreement. On-site access is worth requesting for a supplier that holds a critical single-source item.

Retention should match the product's useful life. A five-year retention period, or shelf life plus one year, whichever is longer, covers the retest window and any study that used the material. Confirm that records survive a supplier ownership change; a clause that binds successors and assigns is standard in well-drafted agreements and absent from most templates.

The [supplier transparency checklist](/blog/peptide-supply-chain-transparency-buyer-checklist/) lists the documents worth requesting before an audit, and the [lead-time evaluation guide](/blog/how-to-evaluate-peptide-supplier-lead-times-in-2026/) covers the operational metrics that belong in a quarterly review. For internal reporting, the [procurement KPI guide](/blog/procurement-kpis-for-peptide-sourcing-2026-guide/) sets out measures such as on-time-in-full rate and batch acceptance rate.

## The Author's Take

**Position.** Procurement should spend its negotiating capital on the specification, the notice window, and the remedy clause, and treat the unit price as the last variable. A three percent discount on a batch that cannot be rejected is not a saving.

**Reasoning.** Peptide supply failures are rarely dramatic. They look like a purity result at 97.4% against a 98.0% specification, a counterion that changed from trifluoroacetate to acetate, or a replacement batch that arrives six weeks after the study was scheduled to start. Each of those is a contract problem before it is a chemistry problem, because the contract either gives the buyer a procedure or leaves them with an argument. The convention and Incoterms references in this article exist to give that procedure a shared vocabulary; they do not replace local counsel.

**Disclosure.** Peptides of China sells research peptides. This article describes commercial terms and sourcing judgment; it is not legal advice, an effects claim, a dosing guide, or medical advice. Products referenced on this site are supplied for laboratory research use only. Contract terms are agreed case by case, and buyers should have agreements reviewed under their own governing law.

## Sources

- United Nations Convention on Contracts for the International Sale of Goods (CISG), Articles 25, 35, 38, 39, 74, 77. [uncitral.un.org](https://uncitral.un.org/en/texts/salegoods/conventions/sale_of_goods/cisg)
- ICC Incoterms 2020 rules. International Chamber of Commerce. [iccwbo.org](https://iccwbo.org/business-solutions/incoterms-rules/incoterms-2020/)
- ICH Q7: Good Manufacturing Practice Guide for Active Pharmaceutical Ingredients. [database.ich.org](https://database.ich.org/sites/default/files/Q7%20Guideline.pdf)
- ICH Q6B: Specifications — Test Procedures and Acceptance Criteria for Biotechnological/Biological Products. [database.ich.org](https://database.ich.org/sites/default/files/Q6B%20Guideline.pdf)
- 21 CFR Part 211 — Current Good Manufacturing Practice for Finished Pharmaceuticals. [ecfr.gov](https://www.ecfr.gov/current/title-21/chapter-I/subchapter-C/part-211)
- WCO Harmonized System Nomenclature, 2022 edition. World Customs Organization. [wcoomd.org](https://www.wcoomd.org/en/topics/nomenclature/instrument-and-tools/hs-nomenclature-2022-edition.aspx)
