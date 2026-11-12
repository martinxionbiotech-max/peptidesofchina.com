---
title: "Peptide Catalog Pricing: A 2026 Cost-per-Milligram Analysis"
slug: "research-peptide-catalog-2026-wholesale-sourcing-price-analysis"
description: "Compare 2026 peptide catalog prices on a common unit: landed cost per milligram of peptide content, including purity, salt form, water, MOQ, freight, and duty."
---
Two 2026 peptide catalogs can list the same compound at the same fill mass and the same purity, and one can be 25% more expensive per milligram of peptide. The difference is not visible on the price line. It sits in content, salt form, water, minimum order quantity, freight terms, and what the supplier has included in the quote.

The fix is a single unit: landed cost per milligram of peptide content, at a stated purity and salt form, delivered to the buyer's site. Every quote can be converted to that unit, and once it is, the catalog becomes comparable.

This guide builds the calculation, explains which cost lines are easy to miss, and shows how purity and purification yield interact with price. The numbers used in the worked examples are illustrative, not market quotations. The formulas are the part to keep.

## Why Catalog Prices Cannot Be Compared Directly

A catalog price is attached to a stock-keeping unit, not to a chemical quantity. The SKU usually specifies the compound, the fill mass, and sometimes the salt form. It rarely specifies peptide content, water content, counterion, purity method, or Incoterms.

Those omissions are not cosmetic. Fill mass is the mass of the powder in the vial, including water and counterion. Purity is an area percentage from a chromatogram, not a mass fraction. A 10 mg vial at 99% purity can hold 8 mg of peptide or 9.6 mg, depending on the salt form and the drying process.

The catalog also hides the commercial terms. A price quoted EXW excludes freight, insurance, duty, and customs brokerage. A DDP price includes them, but the seller has built in a margin for the risk. Comparing an EXW price with a DDP price is comparing a factory gate with a delivered door.

The first step in any analysis is to normalize the commercial term. The second is to normalize the chemical quantity.

## The Unit That Makes Comparison Possible

The unit is:

Landed cost per mg peptide = total landed cost ÷ (fill mass × peptide content %)

Total landed cost includes the unit price, freight, insurance, duty, brokerage, and any testing the buyer pays for. Peptide content is the mass fraction of the peptide in the fill, expressed on a stated basis.

A quote that cannot supply a content figure cannot be converted to this unit. That is a useful screening result in itself: a supplier that does not know its own content is not a supplier you can compare.

The formula also makes the purity question explicit. If two suppliers quote the same price per vial but one is 98.0% and the other is 95.0%, the difference in peptide mass may be smaller than the difference in price. Purity affects the cost of the peptide that is not the target, not the mass of the target itself. Content is the mass lever; purity is the quality lever.

## Purity, Yield, and the Cost Curve

Purification is a separation process, and separation costs yield. A crude peptide mixture is loaded onto a preparative column, the target peak is collected, and the fractions are pooled. Tightening the collection window raises purity and lowers the amount of product recovered.

The relationship is not linear. Removing the last few percent of impurities usually costs a disproportionate share of yield, because the impurity peaks closest to the main peak are the hardest to separate. A process that reaches 95% with a broad collection window may need a second purification step, or a much narrower window, to reach 98%.

For the buyer, the practical consequence is that a 98% product is not simply a 95% product with a small premium. It may require more crude peptide, more column time, and more solvent per gram of finished material. That cost is real, and it is one reason a 98% quote can be materially higher than a 95% quote.

The other consequence is that purity claims should be read with the method. A 98.0% area result at 220 nm on a well-resolved column is a different claim from a 98.0% result on a short column with a shallow gradient. HPLC and LC-MS answer different questions, and neither replaces content testing.

| Cost driver | What changes | Effect on price per mg |
| --- | --- | --- |
| Higher purity target | Narrower cuts or a second purification | Higher; yield falls |
| Larger batch | Fixed setup spread over more grams | Lower per gram, until capacity binds |
| Smaller particle size | Better resolution, higher back pressure | Higher consumable cost |
| Lyophilisation | Water removal and cycle time | Higher than liquid fill |
| Salt form | Counterion mass and additional step | Higher fill mass per mg peptide |
| Testing panel | Identity, purity, content, water, counterion, endotoxin | Higher, but small relative to product |

## Salt Form and Counterion Mass

Salt form changes the denominator of the cost calculation without changing the peptide. A di-arginine salt of a 1,400 Da peptide carries roughly 350 Da of counterion, which is about 20% of the fill mass. An acetate salt carries much less.

The buyer who compares two vials by fill mass is comparing two different products. The buyer who compares by peptide content is comparing the same peptide.

This is not an argument against arginine salts. There are formulation reasons to choose one. It is an argument against paying a per-vial premium for a product that contains less peptide per milligram. The [BPC-157 salt-form comparison](/blog/bpc-157-arginine-salt-vs-acetate-for-research-a-sourcing-comparison/) works through the arithmetic for one compound.

Counterion content also affects shipping weight and, at large scale, freight. A product that is 20% counterion requires 25% more mass for the same peptide quantity. That is a small line item in air freight and a larger one in a multi-kilogram order.

## Water Content and Fill Mass

Lyophilised peptides are hygroscopic. Water content is usually specified at ≤5.0% for a well-dried product, but the actual value depends on the cycle, the vial, the stopper, and the storage history.

Water is included in the fill mass and excluded from the peptide content. A product at 5% water has 5% less peptide per milligram of powder than the same product at 0% water. The difference is small compared with a salt form, but it is not zero, and it accumulates across a large order.

Water also affects stability and handling. A cake that has absorbed moisture may collapse, stick to the vial, or degrade faster. The [stability and storage guide](/blog/retatrutide-stability-and-storage-what-research-buyers-can-and-cannot-infer/) covers the inference problem: a certificate's water result describes the lot at testing, not the vial after six months in a freezer with a broken seal.

Ask for water by Karl Fischer on the finished vial, not on the bulk solution. The vial is what the researcher opens.

## MOQ, Tiers, and Inventory Cost

Minimum order quantities are a pricing mechanism as much as a production constraint. A supplier that quotes a low unit price at a 100-gram MOQ is not offering the same product as a supplier that quotes a higher unit price at 1 gram.

The comparison should include the cost of holding inventory. A larger order lowers the unit price and raises the capital tied up in stock, the storage space, and the risk of expiry. The relevant formula is:

Annual cost = purchase cost + holding cost + obsolescence cost − volume discount

Holding cost includes storage, insurance, and the cost of capital. For a lyophilised peptide stored at −20 °C, the storage cost is modest per gram but not zero, and the freezer space is shared with other materials.

The [bulk order minimum guide](/blog/bulk-peptide-order-minimums-2026-research-lab-guide/) covers the tier structures, and the [lead time guide](/blog/how-to-evaluate-peptide-supplier-lead-times-in-2026/) covers the cost of waiting. A low price with a 12-week lead time can be more expensive than a higher price with stock on hand, because the experiment that cannot start has a cost too.

## Testing and Documentation as Cost Lines

A certificate is not free. Identity by mass spectrometry, purity by HPLC, water by Karl Fischer, counterion by ion chromatography, and endotoxin by LAL each carry a cost, whether the supplier performs them in-house or subcontracts them.

A quote that includes a full panel is not directly comparable with a quote that includes a purity number and nothing else. The buyer will pay for the missing tests, either before the order or after a problem appears.

The [wholesale COA verification guide](/blog/coa-verified-peptides-wholesale-2026-sourcing-verification-guide/) describes the panel and the sampling logic. For budgeting, the practical approach is to add a testing allowance per lot and per shipment, then compare the total.

Documentation also has a time cost. A supplier that takes a week to produce a batch record is a supplier that will delay a shipment when a customs broker asks a question. That delay belongs in the landed cost, even if it is hard to quantify.

## Freight, Insurance, Duty, and Landed Cost

The landed cost build-up has more lines than most buyers expect.

| Line | What it covers | How it is quoted |
| --- | --- | --- |
| Unit price | Peptide at the agreed specification | Per vial or per gram |
| Packaging | Vials, desiccant, cold-chain box | Often included or added |
| Freight | Air, courier, or sea | By weight and service |
| Insurance | Loss or damage in transit | Percentage of cargo value |
| Duty | Tariff on the classified goods | By HTS code and origin |
| Brokerage | Entry preparation | Per shipment |
| Taxes | VAT, GST, or equivalent | By jurisdiction |
| Testing | Retest or release panel | Per lot |

Incoterms decide which lines sit with the seller and which with the buyer. EXW puts almost everything on the buyer; DDP puts almost everything on the seller. FOB and CIF sit in between, and the risk transfer point matters when a shipment is damaged.

Duty is the line most often estimated badly. The rate depends on the classification of the goods, the country of origin, and the trade measures in force at the time of entry. Peptides are not one tariff line, and a generic description on the invoice can lead to a classification that is either more expensive or inadmissible. The [HS code guide](/blog/hs-code-for-peptides/) explains the decision, and the [customs guide](/blog/research-peptide-customs-clearance-a-professional-b2b-sourcing-guide-2026/) covers the entry documents.

Insurance is optional until it is not. A shipment that is lost or delayed in transit without insurance is a total loss, and the replacement lead time is added to the project timeline. For high-value orders, the premium is a small fraction of the cargo value.

## A Worked Comparison

The following example is illustrative. The prices are hypothetical, and the purpose is to show how the lines combine.

| Line | Supplier A | Supplier B | Supplier C |
| --- | ---: | ---: | ---: |
| Fill mass | 10 mg | 10 mg | 100 mg |
| Peptide content | 96% | 88% | 92% |
| Peptide per unit | 9.6 mg | 8.8 mg | 92 mg |
| Unit price | $110 | $95 | $850 |
| Freight per unit | $6 | $6 | $2 |
| Duty and fees per unit | $4 | $4 | $1 |
| Landed cost per unit | $120 | $105 | $853 |
| Cost per mg peptide | $12.50 | $11.93 | $9.27 |

Supplier B is cheaper per milligram than Supplier A despite a similar vial price, because the content is lower and the price is lower. Supplier C is cheapest per milligram because the bulk order spreads freight and duty over more peptide. The table does not say which supplier is best; it says which unit price is lowest after normalization.

The next step is to add the qualitative lines: testing scope, lead time, replacement terms, and documentation quality. A supplier that is 5% cheaper per milligram but cannot provide a batch record is not cheaper in practice.

## Building a 12-Month Budget

A catalog budget is a forecast of consumption, not a list of prices.

Start with the compounds and the expected mass per experiment. Multiply by the number of experiments, add a waste allowance for reconstitution and failed runs, and convert to peptide mass. Then divide by the content of the chosen product to get fill mass. That number is what you buy.

Add the testing allowance: one full panel per lot, plus a retest allowance for a fraction of lots. Add freight and duty per shipment, and decide how many shipments the year requires. A single large shipment lowers freight per gram and raises inventory; four small shipments do the opposite.

Finally, add a contingency for lead-time variation. A supplier that ships in four weeks in January may take eight weeks before a holiday. The [lead time guide](/blog/how-to-evaluate-peptide-supplier-lead-times-in-2026/) explains the seasonal pattern, and the [procurement KPI guide](/blog/procurement-kpis-for-peptide-sourcing-2026-guide/) covers the metrics worth tracking.

The budget should be reviewed against actual consumption every quarter. A catalog price that looked competitive at the start of the year can become expensive if the supplier's content drops or its lead time doubles.

## The Author's Take

**Position.** I would pay a 10% premium per milligram for a supplier that states peptide content, counterion, water, and test methods on every lot.

**Reasoning.** The price line is the least informative part of a peptide quote. Content, salt form, and testing scope move the true cost by more than 10% in either direction, and they are the lines a buyer can verify before the order. A supplier that publishes them has nothing to hide in the arithmetic. A supplier that does not is asking the buyer to absorb the uncertainty, which is a cost even when the vial price looks low.

**Disclosure.** Peptides of China sells research peptides. This article is a procurement and cost-analysis judgment, not an effects claim, and every compound discussed is for research use only.

## Sources

1. WCO, Harmonized System Nomenclature. https://www.wcoomd.org/en/topics/nomenclature/overview.aspx
2. USITC, Harmonized Tariff Schedule of the United States. https://hts.usitc.gov/
3. European Commission, TARIC Consultation. https://ec.europa.eu/taxation_customs/dds2/taric/taric_consultation.jsp
4. General Administration of Customs of China. http://english.customs.gov.cn/
5. ICC, Incoterms 2020. https://iccwbo.org/resources-for-business/incoterms-rules/incoterms-2020/
6. ICH Q7, Good Manufacturing Practice Guide for Active Pharmaceutical Ingredients (2000). https://database.ich.org/sites/default/files/Q7%20Guideline.pdf
7. ICH Q2(R2), Validation of Analytical Procedures (2023). https://database.ich.org/sites/default/files/ICH_Q2%28R2%29_Guideline_2023_1130.pdf
8. FDA, Analytical Procedures and Methods Validation for Drugs and Biologics (2015). https://www.fda.gov/regulatory-information/search-fda-guidance-documents/analytical-procedures-and-methods-validation-drugs-and-biologics
9. CLSI, Method Evaluation and Validation standards, including EP05 precision studies. https://clsi.org/standards/products/method-evaluation/
10. Fosgerau K, Hoffmann T. Peptide therapeutics: current status and future directions. Drug Discovery Today. 2015;20(1):122–128. https://doi.org/10.1016/j.drudis.2014.10.003
