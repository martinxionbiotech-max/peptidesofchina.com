---
title: "Sourcing CJC-1295 from China: DAC Forms, Purity, and Batch Files"
slug: "sourcing-cjc-1295-from-china-2026-lab-procurement-guide"
description: "A lab procurement guide to CJC-1295 from China: DAC versus no-DAC identity, HPLC and MS criteria, batch documents, and import paperwork."
author: "POC Tech Team"
updated: "2026-11-18"
---

Sourcing CJC-1295 from China starts with a naming problem. Two different molecules are sold under the same catalogue name: the modified GRF(1–29) analogue without a linker, and the drug-affinity-complex version that carries a maleimidopropionic acid group and binds serum albumin. They differ by about 279 Da, behave differently in an assay, and are not interchangeable. Before comparing prices, confirm which molecule the quotation describes, then ask for the mass spectrum that proves it. A supplier who cannot tell you which form is in the vial has not established identity, and price is meaningless until identity is settled.

The rest of this guide covers what a Chinese synthesis batch involves, the analytical acceptance criteria that matter for a 29-residue peptide, the document set behind a 10 g order, and the paperwork that decides whether the shipment moves or sits.

## Two molecules, one catalogue name

CJC-1295 without DAC is a modified growth-hormone-releasing hormone fragment, residues 1–29, with four substitutions that resist enzymatic cleavage: D-Ala at position 2, Gln at position 8, Ala at position 15, and Leu at position 27. Its molecular weight is about 3,368 Da.

CJC-1295 with DAC adds a maleimidopropionic acid linker that reacts with the cysteine-34 thiol of serum albumin. The conjugate's molecular weight is about 3,647 Da, roughly 279 Da heavier than the parent. The linker is the reason the two forms are not interchangeable in analytical work: the DAC form gives a different retention time, a different charge envelope in electrospray, and a different stability profile once reconstituted.

Three practical consequences follow:

- **A COA that lists only "CJC-1295" is incomplete.** The form must be stated, and the molecular weight must match it.
- **The mass spectrum should show the expected multiply charged envelope.** For the no-DAC form, the [M+3H]³⁺ ion appears near m/z 1,123 and [M+4H]⁴⁺ near m/z 842. For the DAC form, the corresponding ions sit near m/z 1,216 and 912.
- **Purity is form-specific.** A lot that is 98% pure no-DAC material is not 98% pure DAC material, even if both are labelled CJC-1295.

The [molecular weight verification guide](/blog/peptide-molecular-weight-verification-steps) walks through the calculation for both forms, including how to read the isotope spacing that confirms a triply or quadruply charged ion.

## What a Chinese synthesis batch actually involves

Most research-scale CJC-1295 is made by solid-phase peptide synthesis, purified by preparative reversed-phase HPLC, and lyophilized. The process parameters below are the ones that show up in a batch record and can be audited.

| Stage | Typical parameter | What it controls |
|---|---|---|
| Resin loading | 0.3–0.5 mmol/g | Batch size and coupling stoichiometry |
| Coupling | 4-fold amino acid excess, HBTU/HOBt, DIEA in DMF | Completion of each residue |
| Deprotection | 20% piperidine in DMF, 2 × 10 min | Fmoc removal without aspartimide formation |
| Cleavage | TFA/TIS/water 95:2.5:2.5, 2–3 h | Release from resin, side-chain deprotection |
| Precipitation | Cold diethyl ether at −20 °C | Crude peptide recovery |
| Purification | C18 preparative HPLC, acetonitrile gradient | Removal of truncated sequences |
| Lyophilization | Shelf temperature and vacuum cycle | Residual water and cake appearance |

Two process details matter more than buyers expect. First, the coupling of the histidine residue at position 1 and the adjacent residues is where epimerization and truncation appear; a batch record that shows double coupling at those positions is a sign the process is controlled. Second, cleavage cocktail volume and time affect residual protecting groups: a short cleavage leaves tert-butyl adducts that co-elute near the product and inflate purity by merging peaks.

A direct manufacturer can describe these steps because they run them. A trader describes the product, not the process. That distinction is the reason the [manufacturer verification protocol](/blog/china-peptide-manufacturer-verification-a-2026-b2b-sourcing-protocol) asks for a batch record extract rather than a brochure.

## Reading the certificate: five tests for CJC-1295

A certificate for a 29-residue peptide needs five analytical entries, each with a method and a limit. The table below is a workable acceptance set for research supply.

| Test | Method | Typical acceptance | What it catches |
|---|---|---|---|
| Identity | ESI-MS or LC-MS/MS | Mass within ±0.5 Da of theory | Wrong form, wrong sequence |
| Purity | RP-HPLC, 214 nm | ≥98.0 area% | Truncations, deletions |
| Counterion | Ion chromatography | TFA ≤1.0% w/w | Residual acid load |
| Water | Karl Fischer | ≤5.0% w/w | Net peptide underfill |
| Peptide content | Elemental nitrogen or amino acid analysis | 75–90% w/w | Mass balance |

Purity by area percent is the number buyers fixate on, and it is the least informative on its own. For a peptide of this length, the main peak can hide co-eluting deletion sequences that differ by a single residue. Mass spectrometry catches those because the mass shifts by the residue mass; HPLC alone may not resolve them.

A second check is worth requesting: amino acid analysis after hydrolysis. It gives a molar ratio for each residue and will expose a sequence that is missing or short in one position. The method is slower and needs a dedicated lab, so it is usually reserved for first lots or disputed batches rather than every delivery.

ICH Q3A(R2) sets reporting, identification, and qualification thresholds for organic impurities at 0.05%, 0.10%, and 0.15% for drug substances with a maximum daily dose of 2 g or less. Research peptides are outside that scope, but the thresholds give a defensible reporting convention: name any impurity above 0.10 area% rather than reporting a single "total impurities" figure.

## Impurities that matter in a 29-residue peptide

Longer sequences accumulate more failure modes. The ones that matter for CJC-1295 are predictable, and each has an analytical signature.

- **Deletion sequences.** A missed coupling produces a peptide shorter by one residue, with a mass lower by the residue's residual mass. These are the most common impurity in long SPPS runs and the hardest to see by HPLC alone.
- **Truncations from acid cleavage.** Aspartimide formation at Asp-Pro or Asp-Gly motifs, followed by hydrolysis, gives a mass shift of +18 Da or a split peak.
- **Oxidation.** Methionine and histidine oxidize during storage or lyophilization, adding 16 Da per oxygen. A small oxidized shoulder is common; a large one suggests the lot was exposed to air or light.
- **Residual TFA adducts.** Trifluoroacetate ion pairs shift retention and add mass in the spectrum, which can look like an impurity if the analyst does not account for it.
- **Dimer and aggregate.** Intermolecular disulfide or hydrophobic association appears as a broad peak at higher molecular weight.

Each of these has a mass signature, which is why LC-MS rather than HPLC alone is the appropriate release method for a peptide of this size. The [HPLC versus LC-MS comparison](/blog/hplc-vs-lc-ms-peptides) sets out when the added cost of mass detection pays for itself; for a 29-residue analogue, it usually does on the first lot.

## Ordering: MOQ, lead time, and the sample that proves the lot

CJC-1295 is a mid-volume catalogue peptide. The commercial structure below is typical for direct Chinese supply, though every factory quotes differently.

| Quantity | Typical minimum | Lead time | Notes |
|---|---|---|---|
| 1 g | 1 g | 5–10 business days | From existing purified stock |
| 10 g | 5–10 g | 10–20 business days | Split from a lot, new COA |
| 100 g | 50–100 g | 20–35 business days | Dedicated synthesis slot |
| 1 kg | Custom | 6–8 weeks | Staged release, capacity booking |

Ask for a retention sample of 2–5 g held for 12 months. If a later batch behaves differently, the retained material is the control that settles whether the change is analytical or biological. The [bulk order minimum guide](/blog/bulk-peptide-order-minimums-2026-research-lab-guide) explains how MOQ tiers interact with per-gram pricing and why a 10 g order often costs less per gram than two 5 g orders.

Payment terms carry risk that price comparisons hide. A 30% deposit with 70% against the pre-shipment COA is common. Full prepayment to a new supplier is a credit decision, not a procurement decision; treat it as such and start with a sample-sized order that you can afford to write off.

## Export paperwork and customs

Research peptides move as chemical products, not as food or drugs, and the paperwork reflects that. The documents below are the ones a freight forwarder will ask for.

- **Commercial invoice** with seller and buyer legal names, HS code, country of origin, Incoterms 2020 term, unit value, total value, and gross and net weight.
- **Packing list** with vial count, fill volume, and package dimensions.
- **Certificate of analysis** matching the lot number on the vials.
- **Safety data sheet** in the 16-section GHS format, with the research-use-only statement.
- **Non-hazardous declaration** or dangerous-goods declaration, depending on the carrier's classification.
- **Import permits or registrations** required by the destination country, where applicable.

Classification is the point where assumptions cost money. Many polypeptide hormones and their derivatives are entered under HS 2937.19; some research reagents are classified under 3822 depending on presentation and end use. The tariff line determines duty and whether an import licence applies. Ask the supplier which code they use and confirm it with your customs broker before the first shipment. No supplier can guarantee clearance; what they can do is supply consistent documents that match the invoice.

Country-of-origin marking is a separate obligation in the United States under 19 CFR Part 134. The marking must be visible and permanent on the article or its container, and the origin must be accurate. A vial labelled "Made in China" on the outer carton but not on the primary container is a compliance gap, not a shipping detail.

The [customs clearance guide](/blog/research-peptide-customs-clearance-a-professional-b2b-sourcing-guide-2026) covers the document sequence in more depth, including what to do when a shipment is held for clarification.

## Incoming inspection at the lab

A receiving protocol for CJC-1295 should take under two hours and produce a record you can attach to the batch file.

1. Photograph the package and record the ambient temperature indicator, if present.
2. Check vial count and fill against the packing list.
3. Verify the lot number on each vial matches the COA.
4. Weigh three vials on a calibrated balance; a systematic shortfall across vials indicates a fill problem rather than a weighing error.
5. Reconstitute one vial at 1 mg/mL in water or 0.1% acetic acid, inspect for clarity, and filter at 0.22 µm.
6. Inject on the HPLC method named in the COA; compare the main peak retention time with the reference lot.
7. Confirm the mass envelope by ESI-MS; record the observed ions and the calculated mass.
8. Quarantine the lot until the results are reviewed and released by the responsible scientist.

The record matters as much as the result. Write the method, column, wavelength, injection volume, and integration parameters into the release file, so a later reviewer can reproduce the decision. The [documentation package guide](/blog/peptide-documentation-package) lists the fields that belong in that file.

## Failure modes and how to catch them early

Four failures account for most CJC-1295 sourcing complaints.

**Wrong form shipped.** The no-DAC and DAC versions are visually identical. The only reliable check is mass. If the COA reports one molecular weight and the vial contains the other, the error is caught at receiving, not at the bench.

**Underfill.** A 10 mg vial containing 8.5 mg is within many suppliers' tolerance but changes every concentration in a study. Weighing three vials at receiving gives an early signal.

**Counterion mismatch.** A lot that switched from TFA to acetate without notice will dissolve differently and may not behave the same in a cell assay. The counterion field on the COA should be compared lot to lot, not read once.

**Moisture uptake.** Lyophilized peptide left open in a humid room gains water quickly. A lot that arrived at 3% water and sits at 8% three months later has lost peptide-equivalent mass. Store sealed with desiccant at −20 °C, and let vials equilibrate to room temperature before opening.

Each of these is cheaper to catch on arrival than after a study has run. The receiving record should note which check caught the problem, so the next order can be specified more tightly.

For compound-specific specifications, the [CJC-1295 with DAC](/catalog/cjc-1295-with-dac/) and [CJC-1295 without DAC](/catalog/cjc-1295-without-dac/) catalogue pages list the batch fields supplied with each lot.

## The Author's Take

**Position.** The form of CJC-1295 is the first fact to establish, and mass spectrometry is the only routine check that establishes it. A buyer who accepts "CJC-1295" without a stated molecular weight is buying an unverified material, whatever the purity line says.

**Reasoning.** The two commercial forms differ by a linker that changes the molecule's behaviour and its analytical signature. Because they look the same and share a name, confusion is easy and consequential: an assay designed around the no-DAC peptide will not behave the same way with the albumin-binding conjugate. Mass settles the question in one injection, and the expected charge envelope is predictable for each form. Purity, water, counterion, and peptide content then complete the picture. Suppliers who report all five fields are usually working from a real batch record; suppliers who report only a purity percentage are asking you to trust a number that cannot distinguish the two products.

**Disclosure.** Peptides of China sells research peptides, including both CJC-1295 forms. This article describes procurement and analytical judgment, not an effects claim. Products are supplied for research use only and are not for human or veterinary use.

## Sources

- Teichman SL, Neale A, Lawrence B, Gagnon C, et al. *Prolonged stimulation of growth hormone (GH) and insulin-like growth factor I secretion by CJC-1295, a long-acting analog of GH-releasing hormone, in healthy adults.* Journal of Clinical Endocrinology & Metabolism 91(3): 799–805 (2006). https://pubmed.ncbi.nlm.nih.gov/16352683/
- Ionescu M, Frohman LA. *Pulsatile secretion of growth hormone (GH) persists during continuous stimulation by CJC-1295, a long-acting GH-releasing hormone analog.* Journal of Clinical Endocrinology & Metabolism 91(12): 4792–4797 (2006). https://pubmed.ncbi.nlm.nih.gov/17018654/
- Timms M, Ganio K, Steel R, et al. *A method for confirming CJC-1295 abuse in equine plasma samples by LC-MS/MS.* Drug Testing and Analysis 11(8): 1128–1136 (2019). https://pubmed.ncbi.nlm.nih.gov/30938069/
- ICH. *Q7: Good Manufacturing Practice Guide for Active Pharmaceutical Ingredients.* https://database.ich.org/sites/default/files/Q7%20Guideline.pdf
- ICH. *Q2(R1): Validation of Analytical Procedures: Text and Methodology.* https://database.ich.org/sites/default/files/Q2%28R1%29%20Guideline.pdf
- ICH. *Q3A(R2): Impurities in New Drug Substances.* https://database.ich.org/sites/default/files/Q3A%28R2%29%20Guideline.pdf
- ICH. *Q6A: Specifications: Test Procedures and Acceptance Criteria for New Drug Substances and New Drug Products.* https://database.ich.org/sites/default/files/Q6A%20Guideline.pdf
- U.S. Food and Drug Administration. *21 CFR Part 211 — Current Good Manufacturing Practice for Finished Pharmaceuticals.* https://www.ecfr.gov/current/title-21/chapter-I/subchapter-C/part-211
- U.S. Customs and Border Protection. *19 CFR Part 134 — Country of Origin Marking.* https://www.ecfr.gov/current/title-19/chapter-I/part-134
