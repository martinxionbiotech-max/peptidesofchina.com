---
title: "Custom Peptide Sourcing for Product Development in 2026"
slug: "custom-peptide-sourcing-for-product-development-in-2026"
description: "How to specify a custom peptide: sequence review, purity tiers, release panel, scale-up milestones, and the terms worth fixing before a deposit."
author: "POC Tech Team"
updated: "2026-11-17"
---
**Custom peptide sourcing succeeds or fails on the specification, not the price list.** A sequence pasted into an email is not an order. It becomes an order when length, modifications, counterion, fill format, purity method, and release tests are written down in a form both sides can inspect. Suppliers quote the ambiguity, and the buyer pays for it later as a re-run, a re-purification, or a batch that cannot be released.

The commercial stakes are higher than for catalog compounds because there is no second source to compare against. A catalog peptide can be benchmarked across three suppliers; a custom sequence has one supplier at a time, and switching means repeating technology transfer. That makes the first specification the most valuable document in the project.

This guide covers the specification fields, the yield arithmetic behind purity tiers, the modifications that change the synthesis route, and the milestone structure that keeps a deposit recoverable.

## What Custom Sourcing Actually Covers

"Custom" is used for three different jobs, and they carry different risks.

**De novo synthesis.** The facility builds a sequence it has not made before, from resin and protected amino acids. Risk sits in coupling efficiency, difficult sequences, and purification. This is the case that needs the full specification.

**Modification of a known sequence.** A catalog compound with a lipid chain, a phosphorylation site, a dye label, or a non-natural residue. Risk sits in the added chemistry and in whether the modification survives cleavage.

**Format customization.** A catalog peptide supplied at a different fill mass, in a different vial, or with a different counterion. Risk is mostly analytical and fill-related, not synthetic.

The distinction matters because suppliers price and schedule them differently, and because a buyer who asks for "custom" without naming the category often receives a quote for the simplest interpretation. If the project needs a new sequence, say so in the first line. The [custom synthesis overview](/blog/custom-peptide-synthesis-brands-a-researchers-guide/) covers how the supplier landscape differs.

## Turning a Sequence into a Manufacturable Specification

A specification that a facility can manufacture against has ten fields. Missing any one of them moves a decision into the supplier's discretion.

| Field | What to write | Why it matters |
|---|---|---|
| Sequence | One-letter code with modifications at named positions | Ambiguity at a single residue can change the product |
| Length and termini | Residue count; free or acetylated N-terminus; free or amidated C-terminus | Terminal charge changes retention and stability |
| Disulfides | Pairing pattern, if more than one bridge | Random pairing produces isomers that co-purify |
| Scale | Milligrams or grams, as net peptide | Gross-mass quoting hides counterion weight |
| Purity | Area percent by RP-HPLC at a stated wavelength | A number without a method is not a specification |
| Counterion | Trifluoroacetate, acetate, or chloride | Affects solubility, mass balance, and assay |
| Water content | Limit by Karl Fischer | Wet material loses shelf life and weighs heavy |
| Fill | Vial size, fill mass, overfill allowance | Underfill is a common and quiet shortfall |
| Appearance | Cake or powder, color range | A release criterion the buyer can check on arrival |
| Documentation | COA fields, raw chromatogram, MS spectrum | Determines whether the batch is auditable |

Two conventions cause most disputes. The first is **net versus gross mass**: a 10 mg fill of a trifluoroacetate salt may contain roughly 7.5 mg of peptide, and a specification that does not say which figure it means is open to interpretation. The second is **purity method**: 98% by area on a 30-minute shallow gradient is a stricter claim than 98% on a 10-minute fast gradient, because the fast method compresses impurities into the main peak. State the column, the gradient, the wavelength, and the reporting threshold.

A useful discipline is to write the specification as though the supplier will change next year. If a second facility can read the document and quote the same product without a call, the document is complete.

## Purity Tiers and the Yield Trade-Off

Purity is not a dial that moves independently of yield. Every added percentage point of purity removes material, and the removal cost rises as the target approaches the limit of the method.

The synthesis arithmetic explains why. If each amino acid coupling proceeds at 99.0% efficiency, a 20-residue peptide reaches full length at 0.99^20, or about 81.8%. At 99.5% per step the figure is 90.5%; at 99.8% it is 96.1%. The crude mixture therefore contains roughly 4–18% of truncated sequences before purification begins, and those sequences differ from the target by one or more residues, which often means they elute close to it.

| Tier | Typical HPLC area | Relative purification yield | Sensible use |
|---|---|---|---|
| Crude | 70–80% | Highest | Screening where identity is confirmed separately |
| Research grade | 85–90% | High | Exploratory work with tolerance for variants |
| Premium | 95–97% | Moderate | Assay development, reference standards in training |
| High purity | ≥98% | Lowest | Quantitative work, batch comparison, release testing |

Purification recovery for a difficult sequence commonly lands between 40% and 70% of the crude peptide, and the last two percentage points of purity can consume more than half of that recovery. A quote that offers 99% at the price of 95% is either using a different method, a different scale, or a different definition of purity. Ask which.

Two practical consequences follow. First, buy the purity the assay needs, not the highest number on the page; a 99.5% specification adds cost without adding information if the detection method cannot resolve the difference. Second, ask for the impurity profile, not just the total. A batch at 97.5% with one 1.8% deletion sequence is a different risk from a batch at 97.5% with twelve peaks below 0.2%.

## Modifications That Change the Synthesis Route

A modification is not a label added at the end. It changes the protected building blocks, the coupling order, and sometimes the cleavage cocktail.

**Disulfide bridges.** Two cysteines can form the correct bridge or the wrong one. Facilities control this with orthogonal protecting groups, such as acetamidomethyl (Acm) for one pair and tert-butylthio for another, then oxidize in a defined order. A specification that names the pairing pattern gives the facility a target; one that says "two disulfides" invites a statistical mixture.

**Lipidation.** Attaching a fatty acid, such as a C16 palmitoyl chain, adds a hydrophobic step that changes solubility and purification behavior. The lipid can also promote aggregation during cleavage, so the cleavage time and temperature become release-relevant parameters.

**Phosphorylation.** Phosphoserine and phosphothreonine require protected building blocks; a phosphate added post-synthetically is less specific. The mass shift is +79.966 Da per phosphate, which is easy to confirm by MS but easy to lose during cleavage if the protection strategy is wrong.

**Non-natural residues and D-amino acids.** These are available as protected monomers but cost more and couple more slowly. A single D-residue can be the difference between a 3-week and a 6-week schedule.

**Cyclization.** Head-to-tail or side-chain cyclization adds a step after cleavage, and the linear precursor must be purified before cyclization or the ring closes on impurities. Ask whether the cyclization yield is measured on purified precursor.

Every one of these modifications should appear in the specification with a position number and a mass delta. The [synthesis process guide](/blog/peptide-synthesis-explained-methods-and-process-guide/) explains where each step sits in the route, and the [common synthesis failures](/blog/common-peptide-synthesis-failures-a-practical-lab-guide/) note describes the impurities that follow from each.

## The Release Panel to Require Before Scale-Up

A development batch needs a release panel that can be repeated at the larger scale without changing methods. Five tests do the core work.

**Purity by RP-HPLC.** C18 column, 214 nm detection, stated gradient and reporting threshold, target ≥98.0% area for a high-purity grade. Request the full chromatogram, not a table row.

**Identity by MS.** Intact mass within ±0.5 Da on a unit-mass instrument, or within 5 ppm on a high-resolution instrument. The spectrum should show charge states and a deconvoluted mass.

**Sequence by MS/MS.** At least 90% backbone coverage with annotated b/y ions. This is the only test that distinguishes a deletion at the N-terminus from a substitution at the C-terminus when the mass happens to match.

**Composition by amino acid analysis.** Hydrolysis in 6 M hydrochloric acid at 110 °C for 24 hours, then chromatographic quantitation. Results should fall within roughly ±10% of theory for each residue; cysteine and tryptophan need separate handling because they degrade or are destroyed under standard hydrolysis.

**Water and counterion.** Karl Fischer for water, ion chromatography or titration for trifluoroacetate. Together with net peptide content, these fields explain why a 10 mg vial is not 10 mg of peptide.

A release panel that cannot be repeated at scale is a development-only panel. Confirm with the facility that the same column chemistry, gradient, and detector settings will be used for the engineering batch; method transfer is a common place for a specification to quietly change.

## Scale-Up: Where Milligram Runs Break

Scaling from 0.1 mmol to tens of litres changes mixing, heat transfer, and reagent access. Three failures are common.

**Resin swelling and mixing.** Resin volume changes with solvent; a reactor sized on dry resin mass can be overloaded. Poor mixing creates channeling, which shows up as variable coupling efficiency across the bed and a broader impurity profile.

**Cleavage exotherm.** Trifluoroacetic acid cleavage is exothermic, and a large batch can overshoot the target temperature. Cleavage above the target temperature increases aspartimide formation and can alkylate tryptophan side chains.

**Purification loading.** A preparative column loaded beyond its capacity produces overlapping fractions; the operator then either narrows the heart cut and loses yield, or widens it and loses purity. Ask what the loading ratio was, in milligrams of crude per gram of stationary phase.

A first engineering run at the target scale should be treated as a qualification batch, not as saleable stock, until the analytical comparison against the small-scale reference passes. A 10–20% yield loss on first scale-up is normal; a purity drop of two points is not, and it usually points to purification rather than synthesis.

## Timeline, Deposit, and Milestone Structure

Custom work is priced against time and risk, so the schedule should be written into the agreement rather than inferred from a quote.

| Milestone | Deliverable | Commercial treatment |
|---|---|---|
| Sequence review | Feasibility note naming difficult motifs and expected yield | No charge, 3–5 business days |
| Quotation | Price, scale, purity, lead time, payment terms | Valid 30 days |
| Deposit | Order entry and resin/amino acid reservation | 30–50% of order value |
| Synthesis and purification | Batch record, in-process checks | Progress note at week 3 |
| Release testing | COA, chromatogram, MS spectrum, AAA | Balance payable against documents |
| Shipment | Packing list, lot linkage, storage statement | Retain 10% against receipt test, if negotiated |

Lead times vary with scale and modification load. A 10–50 mg unmodified 20-mer commonly runs 3–5 weeks; gram quantities with a disulfide and a lipid can run 8–12 weeks. A supplier who quotes two weeks for a modified gram-scale sequence is either misunderstanding the request or planning to subcontract it.

The deposit deserves a clause, not a handshake. It should be refundable if the batch fails the agreed specification and the supplier cannot re-make it within a stated window, and it should be tied to the specification document by version number. The [sourcing contract guide](/blog/how-peptide-sourcing-contracts-work-a-procurement-guide/) covers the clause structure in more detail; the [bulk order minimums](/blog/bulk-peptide-order-minimums-2026-research-lab-guide/) note explains how scale thresholds change pricing.

## Documentation, IP, and Exit Terms

Three document sets should exist before the first shipment.

**Batch documentation.** COA with method details, the preparative and analytical chromatograms, the intact mass spectrum, the MS/MS annotation, the amino acid analysis, and the Karl Fischer result. A COA that lists results without methods cannot be reproduced by a second laboratory. The [documentation package guide](/blog/peptide-documentation-package/) lists the full file, and the [custom services page](/custom-peptide-services/) describes the request flow.

**Quality agreement.** Who releases the batch, what happens on a deviation, how long records are retained, and what notice applies to a process change. ICH Q7 expects change control for API manufacture; a research peptide supplier that follows the same discipline can describe its change notification interval.

**Technology transfer package.** For a project that may move suppliers, the receiving facility needs the sequence file, the specification, the analytical methods, and a retention sample. Negotiate this at order placement, when the supplier still wants the business; asking after a quality dispute is a weaker position.

Confidentiality should cover the sequence itself, not just the project name. A sequence disclosed without restriction can be re-used for another customer. A two-year non-reuse clause tied to a named compound is a reasonable ask at development scale.

## The Author's Take

**Position.** The cheapest place to reduce custom peptide cost is the specification, and the most expensive place is the re-run. A buyer who spends a week tightening the specification usually removes more cost than a buyer who spends that week negotiating the unit price.

**Reasoning.** Custom synthesis is quoted against uncertainty. When a request omits the counterion, the fill convention, or the purity method, the supplier prices the worst case and adds a margin for the ambiguity. When those fields are fixed, the quote reflects a defined job, and the batch that arrives can be accepted or rejected against a clause rather than an impression. The arithmetic is unforgiving on the other side too: at 99.0% coupling efficiency a 20-mer yields under 82% full-length material before purification, so a purity promise that ignores synthesis reality is a promise about the purification cut, not about the chemistry.

**Disclosure.** Peptides of China sells research peptides and accepts custom synthesis requests. This article describes sourcing and specification practice; it is not an effects claim, a dosing guide, or medical advice. Products referenced on this site are supplied for laboratory research use only. Custom projects are quoted individually, and analytical documentation varies by sequence and batch.

## Sources

- ICH Q6B: Specifications — Test Procedures and Acceptance Criteria for Biotechnological/Biological Products. [database.ich.org](https://database.ich.org/sites/default/files/Q6B%20Guideline.pdf)
- ICH Q7: Good Manufacturing Practice Guide for Active Pharmaceutical Ingredients. [database.ich.org](https://database.ich.org/sites/default/files/Q7%20Guideline.pdf)
- ICH Q2(R2): Validation of Analytical Procedures (2023). [database.ich.org](https://database.ich.org/sites/default/files/ICH_Q2%28R2%29_Guideline_2023_1130.pdf)
- Merrifield, R. B. Solid Phase Peptide Synthesis. I. The Synthesis of a Tetrapeptide. *Journal of the American Chemical Society* (1963). [doi:10.1021/ja00897a025](https://doi.org/10.1021/ja00897a025)
- Fields, G. B. & Noble, R. L. Solid phase peptide synthesis utilizing 9-fluorenylmethoxycarbonyl amino acids. *International Journal of Peptide and Protein Research* (1990). [doi:10.1111/j.1399-3011.1990.tb00939.x](https://doi.org/10.1111/j.1399-3011.1990.tb00939.x)
- Coin, I., Beyermann, M. & Bienert, M. Solid-phase peptide synthesis: from standard procedures to the synthesis of difficult sequences. *Nature Protocols* (2007). [doi:10.1038/nprot.2007.454](https://doi.org/10.1038/nprot.2007.454)
- Rivier, J. et al. Reversed-phase high-performance liquid chromatography: preparative purification of synthetic peptides. *Journal of Chromatography A* (1984). [doi:10.1016/S0021-9673(01)93709-4](https://doi.org/10.1016/S0021-9673%2801%2993709-4)
