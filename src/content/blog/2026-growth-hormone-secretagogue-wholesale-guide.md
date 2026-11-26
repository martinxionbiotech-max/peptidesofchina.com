---
title: "Growth Hormone Secretagogue Wholesale: A 2026 Buyer's Guide"
slug: "2026-growth-hormone-secretagogue-wholesale-guide"
description: "Procurement guide to growth hormone secretagogue wholesale: compound classes, batch identity, purity limits, kit economics, documentation, and shipping checks."
author: "POC Tech Team"
updated: "2026-11-26"
---
Growth hormone secretagogues are sold wholesale in the same catalog format as every other research peptide, which hides a useful fact: the class contains at least three chemically distinct families with different synthesis routes, different analytical behavior, and different documentation needs. A buyer who treats them as interchangeable will eventually compare a 29-residue GHRH analogue with a 711 Da pentapeptide and wonder why the certificates do not line up.

This guide separates the families, sets out the batch data that should travel with a wholesale order, and explains the economics of kit-based minimums. It is written for laboratory procurement, not for clinical use.

## What Counts as a Growth Hormone Secretagogue

A growth hormone secretagogue is a compound that stimulates growth hormone release through the growth hormone secretagogue receptor (GHSR), the receptor cloned and characterized in the 1990s, or through the growth hormone-releasing hormone (GHRH) receptor. The two pathways converge on pituitary somatotrophs but use different receptors and different downstream signaling.

That definition matters commercially because sellers apply the label loosely. A GHRH analogue is not a GHSR agonist. A ghrelin mimetic is not a GHRH analogue. MK-677 is not a peptide at all; it is a small-molecule growth hormone secretagogue, and it should never appear on a peptide certificate.

| Family | Examples | Receptor | Structural class |
| --- | --- | --- | --- |
| GHRH analogues | Sermorelin, CJC-1295, tesamorelin | GHRH receptor | 29–44 residue peptides |
| Ghrelin mimetics (GHSR agonists) | Ipamorelin, hexarelin, GHRP-2, GHRP-6 | GHSR | 5–7 residue peptides |
| Non-peptide secretagogues | MK-677, ibutamoren | GHSR | Small molecules, not peptides |

For procurement, the table is a sorting tool. A GHRH analogue order is a long-chain synthesis with a higher chance of deletion impurities. A pentapeptide order is a short synthesis where purity is usually easier to reach but counterion and water content still dominate mass balance.

## Three Classes, Three Sets of Batch Risks

**GHRH analogues.** Sermorelin is GHRH(1-29) amide, a 29-residue fragment. CJC-1295 without DAC is a modified 29-residue analogue; the DAC version carries a maleimidopropionic acid linker that changes its plasma binding behavior and its analytical profile. Tesamorelin is a 44-residue analogue. Longer sequences mean more coupling cycles, more opportunities for deletion and truncation, and a greater chance that the crude peptide requires two purification passes.

**Ghrelin mimetics.** Ipamorelin is a pentapeptide, GHRP-2 and GHRP-6 are hexapeptides, and hexarelin is a hexapeptide. Short sequences are easier to synthesize but not automatically easier to release: they often lack a strong chromophore, which affects UV detection during HPLC, and their low molecular weight makes weighing and Karl Fischer sampling less forgiving.

**Non-peptide secretagogues.** MK-677 is orally active in research models and is frequently bundled into "peptide" catalogs. It is not a peptide, has no amino acid sequence, and requires a different identity method (nuclear magnetic resonance and high-resolution mass spectrometry rather than peptide mapping). A supplier that issues a peptide-style COA for MK-677 is telling you something about its template, not its chemistry.

## Identity and Purity: What a GHS Certificate Should Show

A [certificate](/blog/how-to-read-a-peptide-coa-a-researchers-guide-to-hplc-and-ms-reports/) for a growth hormone secretagogue should report identity by [mass spectrometry](/blog/peptide-molecular-weight-verification-steps/), purity by reverse-phase HPLC, water content, counterion, and — for cell-based work — endotoxin. The methods should be named.

| Test | Method | Research-grade expectation |
| --- | --- | --- |
| Identity | ESI-MS or MALDI-TOF, with charge states | Observed mass within ±0.1% of theoretical |
| Purity | RP-HPLC at 214 or 220 nm | ≥98.0% area, main peak |
| Water | Karl Fischer titration | ≤5.0% w/w |
| Counterion | Ion chromatography | TFA or acetate, with a stated limit |
| Endotoxin | LAL or rFC | ≤10 EU/mg for cell-culture use |
| Bioburden | Membrane filtration | ≤100 CFU/g |
| Appearance | Visual | White to off-white powder |

For CJC-1295 with DAC, the linker is part of the identity. A mass spectrum that matches the unmodified peptide is evidence of the wrong molecule, not a rounding error. Ask the supplier to state the theoretical mass, the observed mass, and the charge states used to calculate it. The arithmetic should be reproducible from the spectrum.

Purity by HPLC is area percent. It is not mass percent, and it does not account for water, counterion, or residual solvents. A 98% pure lyophilized powder can contain materially less than 98% peptide by mass. Buyers who calculate concentrations from vial weight rather than from assay or mass balance introduce an avoidable error into every experiment.

## Wholesale Unit Economics and the Kit Minimum

Wholesale pricing in this market is usually quoted per kit, with a kit containing ten vials of a fixed fill. A total order minimum may combine several products, and orders can start at one kit per product. The current Peptides of China minimum is $600 total, which can be met across multiple catalog items.

The relevant arithmetic is not the headline price per vial. It is the fully loaded cost per saleable vial:

**Unit cost = (synthesis + purification + release testing + lyophilization + packaging + freight + duty) ÷ saleable vials.**

A ten-vial kit carries the same fixed QC cost as a hundred-vial batch, so the per-vial price at the low end is dominated by testing and handling, not by the peptide. That is why a supplier quoting a suspiciously low kit price has usually removed a test, shared a batch across customers, or substituted a cheaper fill.

Ask three questions before accepting a wholesale quote:

1. What is the batch size behind this quote?
2. Which tests are included, and which are billed separately?
3. What is the fill mass per vial, and is it peptide mass or total powder mass?

The third question is the one most buyers forget. A 10 mg vial label can mean 10 mg of peptide, 10 mg of powder at 90% peptide content, or 10 mg of powder including counterion and water. The difference is large enough to change a concentration calculation by 10–20%.

For a first order in this class, a single kit of [CJC-1295 without DAC](/catalog/cjc-1295-without-dac/) or [ipamorelin](/catalog/ipamorelin/) is enough to run the documentation and identity checks before committing to a larger batch.

## Documentation for a Multi-Compound Order

A wholesale order with four compounds produces four [batch files](/blog/peptide-documentation-package/). They should not be merged into one certificate with a single batch number. Each vial needs its own identifier, and each identifier needs a matching analytical record.

A complete file for a multi-compound order contains:

- A commercial invoice listing each product, quantity, unit price, and total.
- A packing list with vial counts, fill mass, and batch numbers.
- One certificate per batch, not per order.
- The HPLC chromatogram and mass spectrum for each batch.
- A certificate of origin, if the destination customs authority requires one.
- The HS classification used for each line item.

The batch number is the join key. If the invoice says batch A, the vial label says batch B, and the certificate says batch C, the file is internally inconsistent and should be rejected before shipment, not after.

For destinations with strict import review, the [customs document set](/blog/research-peptide-customs-clearance-a-professional-b2b-sourcing-guide-2026/) and the HS code choice matter as much as the chemistry. A misclassified peptide can be held even when every analytical result is correct.

## Shipping and Storage of Lyophilized GHS Peptides

Lyophilized peptides are not fragile in the way liquids are. They tolerate short ambient transit better than most buyers expect, provided the vial stays sealed and the temperature does not spike. The practical risks are heat exposure in a cargo container, repeated freeze–thaw after arrival, and moisture ingress once the stopper is punctured.

A sensible shipping specification for research-grade material:

- Keep the lyophilized powder below 30°C during transit; avoid sustained exposure above 40°C.
- Do not require dry ice for lyophilized powder unless the specific peptide is known to be unstable; freezing can introduce moisture during thaw.
- Store at −20°C on arrival, protected from light.
- Equilibrate the vial to room temperature before opening, to prevent condensation on the powder.
- Record the arrival temperature if a data logger is included.

For GHRH analogues, the longer chain and the N-terminal modification are the stability-relevant features. For short ghrelin mimetics, oxidation of any methionine or tryptophan residue is the more common concern. Neither risk is visible in a photograph of the vial.

## A Pre-Order Checklist for New Buyers

Before the first wholesale order, a buyer should be able to answer eight questions in writing:

1. Which entity performed the synthesis, and in which country?
2. What is the batch size, and what is the fill mass per vial?
3. Which tests are included in the quoted price?
4. What is the acceptance limit for purity, water, and endotoxin?
5. Can the supplier provide the original chromatogram export?
6. Does the certificate batch number match the vial label?
7. What is the retention sample policy?
8. Which HS code and origin declaration will appear on the invoice?

A supplier that answers all eight is ready for a pilot order. A supplier that answers five and deflects three is a candidate for a smaller trial, not a bulk commitment.

The same logic applies to compound-specific choices. [CJC-1295 with and without DAC](/blog/dac-vs-no-dac/) are different molecules with different masses and different batch risks; [CJC-1295 versus ipamorelin](/blog/cjc-1295-vs-ipamorelin-a-technical-comparison-for-strategic-peptide-sourcing/) is a comparison of two classes, not two SKUs. Treating them as interchangeable in a purchase order is how mismatched certificates enter a lab.

## Where Buyers Get the Molecule Wrong

Three confusions account for a large share of wholesale disputes.

**CJC-1295 with DAC versus without DAC.** The DAC linker adds mass and changes the analytical signature. A certificate for the wrong version will not match the expected mass, and the error is easy to miss if the buyer only checks the purity percentage.

**GHRP-2 versus GHRP-6.** Both are hexapeptides and both are ghrelin mimetics, but they differ in sequence, mass, and impurity profile. A catalog that lists them as interchangeable "GHRP" options is a catalog to read carefully.

**MK-677 as a peptide.** MK-677 is a small molecule. It does not belong in a peptide batch file, and its presence in a "peptide" order usually signals a reseller assembling a catalog rather than a facility reporting its own output.

These are not marketing distinctions. They determine which analytical method is appropriate, which mass is expected, and which certificate is acceptable.

## The Author's Take

**Position:** In this class, I would pay more for a supplier that can explain the DAC linker than for one that offers a lower kit price. The chemistry question is the quality control.

**Reasoning:** Growth hormone secretagogues are a category where the label is often wrong before the purity is. A supplier that conflates CJC-1295 with and without DAC, or sells MK-677 under a peptide certificate, has demonstrated that its catalog is not built from batch records. That failure is upstream of the analytical result and cannot be fixed by a better HPLC column. When the molecule is right, the remaining risks — water content, counterion, endotoxin — are ordinary and measurable. When the molecule is wrong, every downstream number is irrelevant.

**Disclosure:** Peptides of China sells research-use peptides. This is a procurement assessment, not a statement about effects, safety, or medical use. All compounds discussed are for laboratory research only, and nothing here constitutes a promise of purity, customs clearance, or regulatory acceptance.

## Sources

- [Kojima M, et al. Ghrelin is a growth-hormone-releasing acylated peptide from stomach. Nature. 1999](https://pubmed.ncbi.nlm.nih.gov/10604470/)
- [The development of growth hormone-releasing hormone analogs. Rev Endocr Metab Disord. 2025](https://pubmed.ncbi.nlm.nih.gov/39592529/)
- [ICH Q6B: Specifications: Test Procedures and Acceptance Criteria for Biotechnological/Biological Products](https://database.ich.org/sites/default/files/Q6B%20Guideline.pdf)
- [ICH Q2(R2): Validation of Analytical Procedures](https://database.ich.org/sites/default/files/ICH_Q2%28R2%29_Guideline_2023_1130.pdf)
- [FDA Guidance: Q2(R2) Validation of Analytical Procedures](https://www.fda.gov/regulatory-information/search-fda-guidance-documents/q2r2-validation-analytical-procedures)
- [21 CFR 211.194: Laboratory Records](https://www.ecfr.gov/current/title-21/chapter-I/subchapter-C/part-211/subpart-J/section-211.194)
- [Harmonized Tariff Schedule of the United States](https://hts.usitc.gov/)
- [PubMed: growth hormone secretagogue receptor pharmacology](https://pubmed.ncbi.nlm.nih.gov/?term=growth+hormone+secretagogue+receptor+pharmacology)
