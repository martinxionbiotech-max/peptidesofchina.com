---
title: "Just-in-Time Peptide Sourcing: Where It Works"
slug: "what-is-just-in-time-peptide-sourcing-for-researchers"
description: "JIT procurement for research peptides: lead-time mapping, vial-level demand signals, buffer-stock math, and the QC steps that cannot be compressed."
author: "POC Tech Team"
updated: "2026-11-22"
---
Just-in-time works when lead time is short relative to the cost of holding stock. For research peptides, synthesis and release set a floor that no procurement team can compress, so JIT becomes a forecasting and buffer problem rather than a zero-inventory policy. The labs that run it well hold less stock than their peers, not none.

This guide explains where JIT fits in peptide procurement, how to map the lead time you actually have, how to size a buffer with a defensible calculation, and when a stockpiling model is the better choice. It is written for laboratory operations and research purchasing.

## JIT is a lead-time problem, not a storage trick

The core idea is simple: order so that material arrives shortly before it is needed, and avoid paying for inventory that sits unused. The idea assumes that replenishment is reliable and that the cost of a stockout is manageable. Both assumptions need testing before a lab adopts JIT for a peptide that takes weeks to make.

A peptide is not a catalog consumable with a two-day restock. The synthesis run, purification, lyophilization, release testing, and documentation each take time. Some of those steps can be parallelized; few can be shortened without changing the product. JIT therefore starts with a lead-time map, not a spreadsheet of order quantities.

The second assumption is the cost of a stockout. If a study can pause for a week without losing a cohort or a scheduled instrument slot, a thin buffer is reasonable. If a delay invalidates a run, the buffer should be sized to the cost of failure, not to the carrying cost of a few vials.

## Map the lead time you actually have

Ask the supplier for a written lead time broken into stages. A single average hides the step that is most likely to move. The table below shows a planning range for a catalog peptide; confirm the actual values for the product and season you are buying.

| Stage | Planning range | What can move it |
| --- | --- | --- |
| Order confirmation and stock check | 1–2 working days | Custom requirements, payment review |
| Synthesis or stock allocation | 10–20 working days | Queue position, resin availability |
| Purification and lyophilization | 3–7 working days | Crude purity, cycle scheduling |
| Release testing | 3–5 working days | HPLC queue, sterility incubation |
| Documentation | 1–2 working days | Certificate review, signatory |
| Transit and customs | 5–10 working days | Route, carrier, inspection |

The total is not the sum of the midpoints. The stages overlap in some suppliers and queue behind each other in others. Ask which stages run in parallel and which are gated by a single instrument or a single signatory. A release laboratory with one HPLC and one analyst is a bottleneck that a large order cannot fix.

Track actual arrival dates against the quoted lead time for at least three orders. The difference between the quote and the observed dates is the number to use in planning. A supplier that quotes 30 days and delivers in 45 is a 45-day supplier, whatever the quote says. The [lead-time evaluation guide](/blog/how-to-evaluate-peptide-supplier-lead-times-in-2026/) sets out the questions to ask at the quotation stage.

## Why peptide QC cannot be compressed

Some steps can be accelerated with more capacity. Release testing is not one of them, because the methods have fixed durations and the results have to be valid.

A reversed-phase HPLC assay typically takes 30–60 minutes per injection, plus column equilibration and a system suitability run. Karl Fischer titration takes 5–10 minutes per sample. A LAL endotoxin assay takes about an hour, including controls. Sterility testing under USP &lt;71&gt; requires a 14-day incubation. None of these can be shortened by paying for priority service without changing the method or the acceptance criteria.

That has two consequences for JIT. First, the QC leg sets a minimum replenishment time even when the peptide is in stock. Second, a supplier that offers "same-week release" for a sterile product is either holding pre-tested stock or describing a test it did not run. Ask which tests were performed on the shipped lot and when.

The release panel also determines how much stock you need to hold. If a lot must be quarantined until sterility results are available, the effective lead time includes the 14-day incubation. A JIT model that ignores the quarantine period will run out of material while the certificate is pending.

## Demand signal at vial level

Most labs forecast in milligrams and order in kits. The mismatch produces either excess or a shortage. Convert demand to the unit you actually consume: vials opened per week, at the fill mass you use.

A workable demand signal has three inputs:

- **Planned experiments.** The number of runs, replicates, and timepoints that will consume the peptide.
- **Consumption per run.** Measured from previous runs, not estimated from the label.
- **Attrition.** Vials lost to failed preparations, repeats, and quality holds.

Track the three separately for a quarter. The planned number is usually stable; attrition is the variable that causes surprises. A lab that plans 20 vials and consumes 26 has a 30% attrition rate, and a buffer sized on the plan will fail.

For multi-compound studies, track demand at the compound level but order at the kit level. A 10-vial kit may cover several months for one compound and two weeks for another. The [bulk order minimum guide](/blog/bulk-peptide-order-minimums-2026-research-lab-guide/) explains how kit configuration and minimum order values interact with that calculation.

## Reorder point math that survives variability

A reorder point is the inventory level that triggers a new order. The simple version is average daily use multiplied by lead time. The version that survives real variability adds a safety stock:

**Reorder point = (daily use × lead time) + (z × daily use × lead-time standard deviation)**

The first term covers demand during the lead time. The second covers the chance that the lead time is longer than expected. The z value sets the service level: 1.65 for 95%, 2.33 for 99%.

A worked example. A lab uses 1.2 vials per day, the supplier's observed lead time is 35 days, and the standard deviation of that lead time is 6 days. At a 95% service level:

- Demand during lead time: 1.2 × 35 = 42 vials.
- Safety stock: 1.65 × 1.2 × 6 = 11.9 vials.
- Reorder point: 42 + 11.9 = 53.9, rounded to 54 vials.

That is the level at which the next order should be placed, not the level at which the lab runs out. The calculation is only as good as the lead-time data; a supplier with no history gets a wider standard deviation and a larger buffer.

| Model | Stock held | Best for | Main risk |
| --- | --- | --- | --- |
| Pure JIT | Minimal, frequent orders | Stable demand, short lead time, low stockout cost | A single delay stops the study |
| Reorder-point JIT | Buffer sized to lead-time variability | Most research labs | Buffer can drift out of date |
| Seasonal stockpile | Several months of cover | Long lead times, predictable campaigns | Storage and expiry risk |
| Vendor-managed stock | Supplier holds inventory | High-volume repeat orders | Less visibility and control |

The reorder-point model is the practical middle. It keeps inventory visible and ties the buffer to a number rather than a feeling. The [safety stock guide](/blog/role-of-safety-stock-in-peptide-procurement/) covers the same calculation from the supplier side, and the [procurement KPI guide](/blog/procurement-kpis-for-peptide-sourcing-2026-guide/) lists the metrics worth tracking.

## Supplier capacity and booking

A JIT model assumes the supplier can slot your order into the queue when you place it. That assumption fails when the supplier's capacity is booked by larger customers or when a single raw material is short.

Ask three questions before relying on JIT:

1. How many production lines can make this product, and what is the current booking lead time?
2. Is the resin or a key protected amino acid single-sourced?
3. What happens to my queue position if I increase the order at short notice?

A supplier that cannot answer the first question is not managing capacity; it is accepting orders. A supplier that names a single-source raw material is telling you where the next delay will come from. A supplier that can hold a capacity slot for a standing order is offering something more valuable than a discount.

For a study with a fixed start date, book the batch rather than the vial. A capacity reservation with a defined specification and a delivery window is more useful than a promise of stock. Put the reservation in writing, with the lot size, the release tests, and the latest acceptable ship date.

## A JIT scorecard

Measure the model, not the intention. Six metrics are enough for a quarterly review.

| Metric | Definition | Target |
| --- | --- | --- |
| On-time delivery | Orders received within the quoted window | ≥90% |
| Lead-time accuracy | Quoted versus actual, by stage | Within ±5 working days |
| Stockout events | Days without usable material | 0 |
| Inventory cover | Weeks of stock at current use | 6–12 weeks |
| Expired or unused vials | Value written off | <5% of annual spend |
| Certificate completeness | Lots with full document pack | 100% |

The targets are starting points. A lab with a long study and expensive downtime may want a higher cover; a lab with a short campaign may accept less. The point is to review the numbers together. On-time delivery without lead-time accuracy is luck; inventory cover without stockout data is guesswork.

## When JIT is the wrong model

JIT is a poor fit in four situations:

- **The product is custom or single-source.** A custom sequence may have a 12–20 week first run and a long requalification if the route changes. Holding a batch is cheaper than restarting.
- **The study has a fixed start date.** A delay is not a carrying cost; it is a lost cohort or an idle instrument.
- **The material is stability-limited.** A buffer that exceeds the retest period becomes waste. Size the buffer to the stability data, not to the discount.
- **The supplier's capacity is opaque.** If you cannot get a booking commitment, you cannot run JIT.

In those cases, a stockpile with a defined retest date is the safer model. The [lyophilized stability guide](/blog/peptide-stability-why-lyophilized-peptides-are-far-more-stable-than-you-think/) explains why dry peptide stores well, and the [reconstitution guide](/blog/peptide-lyophilization-reconstitution-guide-for-researchers/) covers the point at which storage changes from an asset to a liability.

## The Author's Take

**Position.** JIT is useful for the consumable part of a peptide program and misleading for the synthesis part. A lab should run a reorder-point model with a buffer sized to lead-time variability, and it should book capacity for any custom or long-lead item. Calling that "JIT" is fine; pretending the buffer is zero is not.

**Reasoning.** The lead time is dominated by steps the buyer cannot accelerate: synthesis queue, purification, lyophilization, and release testing. A zero-inventory policy converts those fixed durations into study risk. The reorder-point calculation keeps the risk visible and prices it in vials rather than in vague assurances. The scorecard then shows whether the supplier is actually delivering the lead time it quoted. That is a more honest model than either pure JIT or a freezer full of unlabelled stock.

**Disclosure.** Peptides of China sells research peptides. This article is an operations and sourcing judgment, not a claim about any compound's effects. Products are supplied for laboratory research use only and are not for human or veterinary use. Lead-time ranges are planning examples; confirm current values with the supplier before committing to a study schedule.

## Sources

1. ICH Q7, Good Manufacturing Practice Guide for Active Pharmaceutical Ingredients (2000). https://database.ich.org/sites/default/files/Q7%20Guideline.pdf
2. ICH Q10, Pharmaceutical Quality System (2008). https://database.ich.org/sites/default/files/Q10%20Guideline.pdf
3. ICH Q1A(R2), Stability Testing of New Drug Substances and Products (2003). https://database.ich.org/sites/default/files/Q1A%28R2%29%20Guideline.pdf
4. ICH Q6A, Specifications: Test Procedures and Acceptance Criteria (1999). https://database.ich.org/sites/default/files/Q6A%20Guideline.pdf
5. ISO 9001:2015, Quality management systems — Requirements. https://www.iso.org/standard/62085.html
6. 21 CFR 211.166, Stability testing. https://www.ecfr.gov/current/title-21/chapter-I/subchapter-C/part-211/subpart-F/section-211.166
7. 21 CFR 211.84, Testing and approval or rejection of components, drug product containers, and closures. https://www.ecfr.gov/current/title-21/chapter-I/subchapter-C/part-211/subpart-E/section-211.84
8. PIC/S, GMP Guide and publications. https://picscheme.org/en/publications
