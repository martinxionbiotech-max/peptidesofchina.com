---
title: "Switching Peptide Suppliers Without Reformulation"
slug: "switch-peptide-supplier-without-reformulation"
description: "A comparability plan for changing peptide suppliers: match salt form, assay basis and impurity profile, then bridge with three lots and stability data."
author: "POC Tech Team"
---
Switching peptide suppliers without reformulation means proving that the new material is equivalent to the old material on the attributes your work depends on, before the old stock runs out. The sequence does not change. The salt form should not change. What changes is the manufacturer, and with it the impurity profile, the counterion content, the water content and the batch-to-batch variation.

The work is a comparability exercise, not a new formulation. For a research reagent, that usually means three new lots, a side-by-side analytical panel against a retained reference lot, and a short stability bridge. Skip those steps and the switch becomes an uncontrolled variable in every experiment that follows.

## What "Without Reformulation" Actually Requires

Reformulation changes the composition of a test article: a different buffer, a different excipient, a different concentration. A supplier switch should change none of those. If the new material forces a change in how the stock is prepared, the switch has already failed the "without reformulation" test, even if the certificate looks acceptable.

The practical definition is narrower than most buyers assume. Two materials are interchangeable for research purposes when they share the same sequence, the same salt form, a comparable impurity profile, and a comparable net peptide content per vial. Price and lead time are commercial attributes; they do not make a material equivalent.

There is an important boundary here. A supplier comparability package for a research reagent is not a regulatory bioequivalence study, and it does not establish therapeutic equivalence. It establishes that the analytical and handling characteristics stayed inside limits you defined. That is the right scope for research procurement, and claiming more would be unsupported.

## The Four Attributes That Must Match First

Before writing a protocol, check four attributes. A mismatch on any of them is a stop signal, not a negotiation point.

**Sequence and terminal groups.** The one-letter sequence should match exactly, including N-terminal acetylation, C-terminal amidation and any non-natural residues. A peptide that differs by a single terminal group can have a different mass, a different charge profile and a different stability profile.

**Salt form and counterion.** Free base, acetate, hydrochloride and TFA salts behave differently in solution and carry different mass. A switch from acetate to TFA can change solubility and can introduce a residual TFA burden that the old specification never allowed.

**Assay basis.** "98%" means different things on an as-is basis and on an anhydrous, counterion-free basis. If the old supplier reported 98% as-is and the new supplier reports 98% after correcting for water and acetate, the new material may contain more peptide per milligram, not less. The direction of the difference matters for every concentration calculation downstream.

**Impurity profile.** Two lots can both report 98.5% area purity and still differ in the number, identity and retention times of the impurities. A new impurity at 0.4% may be irrelevant, or it may be a deletion sequence that competes in a binding assay. The chromatogram, not just the percentage, is the comparison.

| Attribute | Match criterion before the switch | Method | If it fails |
| --- | --- | --- | --- |
| Sequence | Exact match, including terminal modifications | LC-MS/MS or intact mass plus sequence record | Stop; do not order |
| Salt form | Same counterion, stated stoichiometry | Ion chromatography | Stop or re-qualify handling |
| Assay basis | Same basis, or converted with a documented factor | HPLC assay, Karl Fischer, IC | Recalculate; do not compare raw percentages |
| Purity | Within 1.0 area% of reference | RP-HPLC, same method | Investigate impurity profile |
| Impurity profile | No new peak above 0.10% | RP-HPLC, 214 or 220 nm | Obtain identification before use |
| Water | Within 1.0 percentage point | Karl Fischer | Adjust net peptide calculation |
| Endotoxin | Same limit and same method | LAL | Re-test or reject |

## A Comparability Protocol in Five Steps

A workable protocol fits on two pages. It does not need to be elaborate; it needs to be specific enough that two people would run it the same way.

**Step 1: Freeze the reference.** Set aside at least three vials of the current lot as a reference standard. Record the lot number, the certificate, the storage temperature and the date placed in storage. Once the old supplier is gone, this material is the only bridge to the past, and it cannot be replaced.

**Step 2: Define the panel.** Choose the attributes that matter to the work: identity by mass, purity by RP-HPLC, assay by external standard, water by Karl Fischer, counterion by ion chromatography, appearance, and endotoxin if the application is sensitive to it. Add solubility at the working concentration if the new material will be dissolved.

**Step 3: Test three new lots.** One lot proves that a batch exists. Three lots give a preliminary view of batch-to-batch variation. For a first switch, three consecutive lots from the new supplier is a reasonable minimum. Test them against the frozen reference in the same analytical run, not in separate runs weeks apart.

**Step 4: Compare with pre-set limits.** Write the acceptance limits before the data arrive. A typical panel might require purity within 1.0 area%, assay within ±2.0% of the reference, water within 1.0 percentage point, counterion within 1.5 percentage points, mass within ±0.5 Da on a unit-resolution instrument, and no new impurity above 0.10%. If the limits are written after seeing the results, the exercise becomes a justification rather than a test.

**Step 5: Bridge with stability.** Put one lot on a short stability program at the storage temperature and at one accelerated condition. Compare against the reference at each time point. The question is not whether the new material is stable in absolute terms; it is whether it degrades at a similar rate and by a similar pathway.

| Stage | Activity | Typical duration | Output |
| --- | --- | --- | --- |
| 0 | Freeze reference vials and records | 1 day | Reference lot register |
| 1 | Document review and attribute match | 3–5 days | Go/no-go memo |
| 2 | Order three lots | 21–35 days | Three batch certificates |
| 3 | Side-by-side analytical panel | 10–15 working days | Comparability table |
| 4 | Stability bridge, 0–3 months | 90 days | Interim stability report |
| 5 | Release and inventory cutover | 1 week | Signed change record |

## Sampling and Side-by-Side Analysis

Sampling error is the quiet failure in comparability work. A single vial from a 50-vial lot may not represent the lot, particularly for a lyophilised powder where fill weight varies. Take at least two vials per lot and prepare independent sample solutions. If the two preparations disagree by more than the method precision, the sampling plan is the problem.

Run the reference and the new lots in the same sequence on the same instrument. Sequence effects are real: a column that has seen twenty injections behaves differently from one that has seen two. A bracketed sequence of reference, new lot A, new lot B, new lot C, reference again lets you check drift across the run.

For HPLC, use the same column lot and the same mobile phase batch. Record the system suitability results for each sequence: six injections, peak-area RSD ≤2.0%, retention-time RSD ≤1.0%, resolution ≥1.5. If the suitability criteria fail, the comparison is not valid, regardless of how the samples looked.

For mass confirmation, report the observed mass and the tolerance, not just "conforms". A unit-resolution instrument should hold ±0.5 Da; a high-resolution instrument at 60,000 resolution can hold ±5 ppm. The [molecular weight verification guide](/blog/peptide-molecular-weight-verification-steps/) walks through the charge-state arithmetic if the report gives m/z values rather than a deconvoluted mass.

For assay, prepare duplicate solutions at two concentrations. A single-point calibration is a screening test, not an assay. The working range should bracket the expected value, and the calibration curve should have at least five points with a coefficient of determination of 0.995 or better.

## Stability Bridging: What to Run and for How Long

A supplier switch does not require a full ICH stability program for a research reagent, but it does require a defensible bridge. The minimum useful design is three time points: zero, one month and three months at the intended storage temperature, plus zero and one month at an accelerated condition.

For lyophilised peptides stored at −20 °C, the accelerated condition is usually 25 °C or 40 °C at a controlled humidity, depending on the packaging. ICH Q1A(R2) describes 25 °C/60% RH and 40 °C/75% RH as standard long-term and accelerated conditions for drug substances, and those conditions are a reasonable reference even when the material is not a drug product. The point is to compare degradation rates between old and new material, not to assign a formal shelf life.

At each time point, measure purity by HPLC, water content, appearance and, if the material is in solution, visible particulates. A new lot that loses 0.3 area% per month at 40 °C while the reference loses 0.1 area% is telling you something about the purification or the residual moisture, even if both pass at t=0.

The stability bridge also catches counterion effects. A TFA salt can show a different solution stability profile from an acetate salt, particularly at neutral pH, because the residual acid affects local pH and aggregation. If the new supplier switched the counterion without saying so, the stability data will often reveal it before the certificate does.

## Documentation for a Supplier Change

The change record should be short and complete. It needs the old and new supplier names, the old and new lot numbers, the specification revisions, the comparability results, the acceptance limits, the deviations, the disposition and the signatures. It should also state what was not tested and why.

Attach the certificates for all lots, the raw chromatograms, the mass spectra, the Karl Fischer and ion chromatography reports, and the stability data. A PDF bundle with a one-page summary at the front is easier to audit than a folder of instrument files.

The [documentation package guide](/blog/peptide-documentation-package/) covers the fields that should follow every lot. For the supplier side, [manufacturer verification](/blog/china-peptide-manufacturer-verification-a-2026-b2b-sourcing-protocol/) explains how to confirm that the entity issuing the certificate is the entity that made the material. A switch to a new trading name that uses the same factory is a different risk from a switch to a new factory.

## Timeline, Inventory and the Cost of a Bad Switch

A supplier switch takes longer than the purchase order suggests. Production of three lots can take three to five weeks. Certificates and shipping add one to two weeks. The analytical panel adds two to three weeks. A stability bridge adds three months if you wait for the final time point, though the interim read at one month is often enough to release material for non-critical work.

That means an eight-to-twelve-week inventory bridge is prudent. Running the old stock to zero before the new material is qualified is the single most common cause of a rushed, undocumented switch. The [lead time evaluation guide](/blog/how-to-evaluate-peptide-supplier-lead-times-in-2026/) explains how to separate production time from QC release and freight.

The cost of a bad switch is not the price difference per vial. It is the repeated experiment, the lost month, and the ambiguity about whether an unexpected result came from the biology or from the new material. Against that, the cost of a three-lot panel is small.

| Failure mode | Early signal | Consequence | Prevention |
| --- | --- | --- | --- |
| Counterion change | Solubility differs; acetate result missing | Concentration errors, pH shifts | Require IC data before order |
| Water increase | Powder clumps; Karl Fischer >8% | Lower net peptide per vial | Set water limit in specification |
| New impurity | Extra peak at 0.2–0.5% | Altered assay response | Compare chromatograms, not just purity |
| Fill weight drift | Vial-to-vial mass variance | Inconsistent reconstitution | Weigh three vials per lot |
| Documentation gap | Certificate lacks method detail | No defensible release | Reject incomplete certificates |

## Failure Modes and When to Stop

Stop the switch if the new material fails identity, if the salt form differs without a documented reason, or if a new impurity appears above 0.10% and cannot be identified. Those are not issues to manage through a deviation; they are reasons to stay with the current supplier or qualify a third one.

Slow down if the assay is within limits but the water content sits at the upper edge. A marginal water result often becomes a failing result in a warmer climate or a longer storage period. Ask for three more lots before committing to a full cutover.

Accept the switch when the panel passes, the one-month stability read is comparable, and the documentation is complete. Then keep the reference vials. A retained reference lot is cheap insurance for the next switch, and for any unexpected result in the following year.

For a concrete example of the attributes involved, the [BPC-157 catalog page](/catalog/bpc-157/) lists the form and purity a buyer would compare, and the [COA reading guide](/blog/how-to-read-a-peptide-coa-a-researchers-guide-to-hplc-and-ms-reports/) shows how to check that the certificate actually supports the comparison. Buyers who want to understand why two suppliers can both be honest and still produce different material should read [why peptide suppliers show inconsistent quality](/blog/why-peptide-suppliers-inconsistent-quality/). If the new material does not dissolve as expected, the [solubility troubleshooting guide](/blog/peptide-solubility-troubleshooting/) is the next stop.

## The Author's Take

**Position.** Most supplier switches fail before the first assay, at the point where the buyer compares a purity percentage instead of a specification. The four attributes that decide compatibility are sequence, salt form, assay basis and impurity profile, and only one of them is usually on the quotation.

**Reasoning.** Purity is the easiest number to market and the hardest to compare across laboratories. A buyer who matches the method and the basis can compare two suppliers honestly; a buyer who matches only the headline percentage is comparing two different measurements that happen to share a unit. The comparability panel costs a few thousand dollars and a month of calendar time. A failed switch costs a study, and often the confidence of whoever funded it.

**Disclosure.** Peptides of China sells research peptides. This article describes sourcing and change-control practice, not an effects claim. All materials discussed are for research use only, and nothing here should be read as a statement about human use or therapeutic equivalence.

## Sources

1. ICH Q5E, Comparability of Biotechnological/Biological Products Subject to Changes in Their Manufacturing Process (2004). https://database.ich.org/sites/default/files/Q5E%20Guideline.pdf
2. ICH Q6B, Specifications: Test Procedures and Acceptance Criteria for Biotechnological/Biological Products (1999). https://database.ich.org/sites/default/files/Q6B%20Guideline.pdf
3. ICH Q1A(R2), Stability Testing of New Drug Substances and Products (2003). https://database.ich.org/sites/default/files/Q1A%28R2%29%20Guideline.pdf
4. ICH Q2(R2), Validation of Analytical Procedures (2023). https://database.ich.org/sites/default/files/ICH_Q2%28R2%29_Guideline_2023_1130.pdf
5. U.S. FDA, 21 CFR 211.84, Testing and Approval or Rejection of Components, Drug Product Containers, and Closures. https://www.ecfr.gov/current/title-21/chapter-I/subchapter-C/part-211/subpart-E/section-211.84
6. U.S. FDA, 21 CFR 211.192, Production Record Review. https://www.ecfr.gov/current/title-21/chapter-I/subchapter-C/part-211/subpart-J/section-211.192
7. D'Hondt M, Bracke N, Taevernier L, et al. Related impurities in peptide medicines. Journal of Pharmaceutical and Biomedical Analysis. 2014;101:2–30. https://doi.org/10.1016/j.jpba.2014.06.012
8. ISO/IEC 17025:2017, General requirements for the competence of testing and calibration laboratories. https://www.iso.org/standard/66912.html
9. CLSI, Method Evaluation and Validation standards, including EP05 precision studies. https://clsi.org/standards/products/method-evaluation/
