---
title: "Peptide Specification Sheets: What a Spec Must Contain"
slug: "why-peptide-specification-sheets-matter-in-procurement"
description: "A peptide specification sheet fixes sequence, salt form, assay basis, purity method, water content and acceptance limits before a purchase order is issued."
author: "POC Tech Team"
updated: "2026-11-17"
---
A peptide specification sheet is the document that turns a marketing claim into a testable requirement. It names the sequence, the salt form, the assay basis, the analytical method, the units and the acceptance limit for each attribute. Without it, a buyer is comparing adjectives; with it, a buyer is comparing numbers that a laboratory can reproduce.

The sheet matters most before money moves. Once a purchase order is signed, the specification becomes the only shared definition of what "acceptable" means. A certificate of analysis issued against a vague specification is not evidence of much, because almost any result can be declared conforming when no limit was written down.

## What a Specification Sheet Is, and What It Is Not

Three documents get confused in procurement conversations: the listing, the specification, and the certificate of analysis. They serve different purposes and carry different authority.

| Document | What it states | What it proves | Who controls it |
| --- | --- | --- | --- |
| Catalog listing | A commercial claim, often a purity range | That a supplier is willing to advertise a number | Supplier marketing |
| Specification sheet | Required identity, methods, limits and basis | What the buyer and seller agreed to test | Both parties, by contract |
| Certificate of analysis | Measured results for one lot | What that laboratory found in that sample | Issuing laboratory |
| Independent test report | Results from a laboratory the buyer selected | Whether a sample met the stated limits | Buyer's contract lab |

A specification is a requirement. A certificate is a result. When a supplier sends a certificate but no specification, the buyer has been given an answer to a question nobody wrote down.

The distinction has a practical consequence at receiving. If the specification says "purity ≥98.0% by RP-HPLC, area percent at 220 nm" and the certificate reports 98.4%, the buyer can accept the lot on the documented basis and retain a sample for confirmation. If the specification says only "high purity", the same certificate supports no decision, because there is no agreed threshold to compare against and no agreed method that produced the number.

## The Fields That Decide Whether a Spec Is Usable

Most peptide specification sheets are one or two pages. The useful ones share a structure: identity block, material description, analytical table, packaging and storage, revision history. The table below lists the fields that change a purchasing decision, with example limits a research buyer might write. The values are examples of how limits are expressed, not universal requirements.

| Field | Why it changes the decision | Example expression |
| --- | --- | --- |
| Sequence | Distinguishes the target from analogues and scrambles | One-letter sequence with N- and C-terminus stated |
| Molecular formula and mass | Gives the theoretical mass for identity checks | C62H98N16O22; 1419.5 Da |
| Salt or counterion form | Changes mass, solubility and net peptide content | Acetate salt; acetate 5.0–12.0% w/w |
| Appearance | First-line check for gross defects | White to off-white lyophilised powder |
| Purity method and wavelength | Defines what the percentage means | RP-HPLC, 220 nm, area percent |
| Purity limit | Release threshold | ≥98.0% area |
| Assay and basis | Separates peptide content from area purity | 95.0–102.0% on anhydrous, counterion-free basis |
| Water content | Explains part of the mass that is not peptide | ≤8.0% by Karl Fischer |
| Residual TFA | Relevant when TFA was used in purification | ≤1.0% w/w |
| Endotoxin | Sets a ceiling for a stated use | ≤10 EU/mg by LAL |
| Bioburden | Indicates microbial load before sterile filtration | ≤100 CFU/g |
| Storage and retest | Defines the usable window | −20 °C, protect from light, retest 24 months |

Two fields deserve more attention than they usually get: the assay basis and the counterion specification. Both determine how much peptide is actually in the vial, and both are frequently omitted from supplier documents because omitting them makes the purity number look better.

## Identity: Sequence, Salt Form and Counterion

A peptide name is not a chemical identity. BPC-157 as a free base, as an acetate salt and as a TFA salt are three different materials with different masses, different handling properties and different net peptide content per milligram of powder. The sequence can be identical in all three.

The specification should state the sequence in one-letter code, the expected molecular mass, and the salt form. If the material is an acetate salt, the sheet should give an acetate content range measured by ion chromatography, typically expressed as percent weight by weight. If trifluoroacetic acid was used during purification, the sheet should state a residual TFA limit, because TFA binds to cationic peptides and is not removed by simple lyophilisation. [TFA removal is a separate process step](/blog/tfa-removal-peptides/), and its absence from a specification is a signal that nobody measured it.

Mass verification then has a reference point. For a peptide with a theoretical mass of 1419.5 Da, a low-resolution electrospray result within ±0.5 Da is consistent with the expected composition. A high-resolution instrument at 60,000 resolution can hold a tolerance near ±5 ppm, which is about ±0.007 Da at that mass. The arithmetic behind charge states is covered in the [molecular weight verification guide](/blog/peptide-molecular-weight-verification-steps/); the specification only needs to fix the tolerance and the method.

Counterion stoichiometry is the part buyers underestimate. A peptide with two basic residues may carry two acetate molecules per peptide molecule, and the resulting powder can contain a substantial fraction of acetate by mass. That is not a defect. It is a material property that has to be declared, because it changes the amount of peptide in a 10 mg vial.

## Purity and Assay Are Two Different Numbers

Purity, as usually reported, is an area percentage from a chromatogram. It answers a narrow question: of the material that absorbed at the detection wavelength and eluted within the run, what fraction belonged to the main peak? It says nothing about water, counterions, residual solvents or inorganic salts, because those do not produce a peak in a typical reversed-phase run.

Assay answers a different question: how much of the labelled mass is the target peptide? A certificate can legitimately report 99.0% purity by area and 82% peptide content by mass. Both numbers can be true at the same time.

The arithmetic matters at the bench. Take a 10 mg vial labelled as 10 mg peptide, a purity of 98.5% by area, and a net peptide content of 88%. The mass of target peptide is approximately 10 × 0.985 × 0.88 = 8.67 mg. A researcher who assumes 10 mg and calculates concentrations from that assumption introduces an 11–13% error before the first pipette tip touches the vial. For a review of how these figures appear on a certificate, see the [COA reading guide](/blog/how-to-read-a-peptide-coa-a-researchers-guide-to-hplc-and-ms-reports/).

Wavelength choice adds another layer. A 214 nm method detects the peptide backbone and tends to show more impurity peaks than a 280 nm method, which detects aromatic residues. Two certificates quoting 98% purity are not comparable unless the wavelength, column, gradient and integration threshold are the same. [HPLC and LC-MS answer different questions](/blog/hplc-vs-lc-ms-peptides/), and neither replaces a stated method.

## Water, Counterion and Net Peptide Content

Net peptide content is a mass-balance calculation, not a direct measurement. The usual form is:

Peptide content (%) = 100 − water − counterion − residual solvents − inorganic residue − other impurities.

Each term needs a method. Water is measured by Karl Fischer titration, with a sample size typically between 50 and 100 mg for a lyophilised powder; loss on drying is a cheaper alternative but it also drives off volatile solvents and can overstate water. Counterion content comes from ion chromatography. Residual solvents come from gas chromatography, and the specification should name the solvents that were actually used, not a generic list. Inorganic residue comes from residue on ignition or sulphated ash.

For an acetate salt of a cationic peptide, a net peptide content between 70% and 90% is common. A specification that promises 98% peptide content by mass, while also reporting 99% area purity and no water limit, is internally inconsistent. Either the water and counterion were not measured, or the "98%" refers to something other than mass.

The specification should state the basis explicitly: "on anhydrous, counterion-free basis" or "as-is". The difference between those two phrases can exceed ten percentage points. [The documentation package](/blog/peptide-documentation-package/) should carry the same basis across the specification, certificate and label, because a basis switch between documents is one of the commonest ways a failing lot appears to pass.

## Setting Acceptance Limits You Can Enforce

A limit copied from another supplier's certificate is a guess. A limit derived from method capability and product risk is a decision. Three questions produce defensible limits.

First, what does the method actually resolve? If the HPLC method has a resolution of 1.2 between the main peak and the nearest impurity, a 99.0% limit cannot be enforced meaningfully, because the method cannot separate the peak being measured from the one next to it. System suitability should require at least six replicate injections, a peak-area relative standard deviation of ≤2.0%, a retention-time RSD of ≤1.0%, resolution ≥1.5 and a tailing factor between 0.8 and 1.5.

Second, what variation is normal between lots? Three consecutive lots give a rough estimate. If the last three lots ran 98.2%, 98.5% and 98.3% by area, a limit of ≥98.0% is achievable but leaves little room. A limit of ≥97.0% with a trend review is often more honest than a nominal 99% that gets waived whenever it is missed.

Third, what does the research application require? A receptor-binding study and a cell-culture study do not carry the same sensitivity to endotoxin or residual TFA. The specification should state limits for the attributes that matter to the stated use, and mark the rest as informational. Writing "endotoxin ≤10 EU/mg" when nobody intends to measure it is worse than leaving it out, because it creates a paper compliance trail with no analytical basis.

| Attribute | Buyer-set limit example | Method | Sampling note |
| --- | --- | --- | --- |
| Purity | ≥98.0% area | RP-HPLC, 220 nm, C18 | Single injection plus system suitability |
| Assay | 95.0–102.0% | External standard HPLC or AAA | Duplicate preparation |
| Water | ≤8.0% | Karl Fischer | 50–100 mg sample |
| Acetate | 5.0–12.0% w/w | Ion chromatography | Report stoichiometry |
| Residual TFA | ≤1.0% w/w | Ion chromatography | Name the extraction method |
| Endotoxin | ≤10 EU/mg | LAL, kinetic chromogenic | Report method sensitivity |
| Bioburden | ≤100 CFU/g | Membrane filtration | State incubation conditions |
| Appearance | White powder, no clumps | Visual | Photograph the lot |

## Specification Drift Between Listing, Quote and Vial

A specification can exist in four places at once: the website listing, the quotation, the purchase order attachment, and the certificate that arrives with the vial. Drift between them is normal in informal procurement and expensive in formal procurement.

The common patterns are predictable. The listing says "≥99% purity" without a method. The quotation says "98% min, HPLC". The purchase order says "per supplier specification". The certificate reports 97.6% by area at 214 nm and passes because no limit was attached to the purchase order. Each document is internally reasonable, and the chain has no enforceable requirement.

A controlled specification fixes this with three habits. It carries a revision number and a date. It is attached to the purchase order by reference, not summarised in the email body. And any change to a limit requires a written deviation with a reason, not a silent edit to the PDF.

Revision control also protects the supplier. If a buyer changes the water limit from ≤8.0% to ≤5.0% between orders without telling anyone, a conforming lot will fail on arrival. The supplier is then blamed for a requirement that was never communicated. A one-page revision history prevents that argument.

## How to Audit a Spec Sheet in Fifteen Minutes

Read in a fixed order. The order matters more than the depth of any single check.

1. **Revision and date.** No revision number means no controlled document. Check that the date precedes the purchase order.
2. **Product identity.** Sequence, molecular formula and theoretical mass should agree with each other. A formula that does not produce the stated mass is a transcription error somewhere.
3. **Salt form and counterion.** Look for a declared form and a numeric counterion range. "Aceate salt" with no percentage is a label, not a specification.
4. **Purity method.** Column, dimensions, particle size, mobile phase, gradient, flow rate, injection volume, wavelength and run time. If the method is summarised as "HPLC", the purity number is not reproducible.
5. **Assay basis.** Anhydrous, counterion-free or as-is. Then check whether the certificate uses the same basis.
6. **Limits and units.** Every attribute needs a comparator and a unit. "Purity: 98" fails the test.
7. **Endotoxin and bioburden claims.** Only count them if a method and a limit are stated. A claim with no method is marketing.
8. **Storage and retest.** Temperature, light protection and retest interval should be consistent with the stability data the supplier is willing to share.
9. **Signature and laboratory identity.** An unsigned sheet from an unnamed QC department has no attribution.
10. **Arithmetic.** Do one net-peptide calculation. If the numbers do not reconcile, stop and ask.

Fifteen minutes is enough for a first pass. The second pass happens at receiving, when the certificate is compared against the specification field by field. A buyer who runs both passes has a defensible file; a buyer who runs neither has a folder of PDFs.

If the supplier cannot produce a specification with methods and limits, the next question is whether they manufacture the material at all. [Manufacturer verification](/blog/china-peptide-manufacturer-verification-a-2026-b2b-sourcing-protocol/) covers the site-level checks that sit behind the document, and the [quality testing overview](/blog/peptide-testing-and-analysis-a-professional-guide-to-laboratory-verification/) explains what an independent laboratory can add. For a worked example of how a specification maps onto a catalog item, the [semaglutide product page](/catalog/semaglutide/) shows the fields a buyer would expect to see before requesting a batch-specific certificate.

## The Author's Take

**Position.** The specification sheet is the most valuable document in a peptide purchase, and it is usually the one nobody asks for. I would rather buy a 97% lot against a specification I can test than a 99% lot against an adjective.

**Reasoning.** Purity numbers are cheap to print and expensive to verify. A specification forces the supplier to commit to a method, a basis and a limit before the sale, which is exactly when they have an incentive to be accurate. It also gives the buyer a document to test against, which changes the conversation after delivery from opinion to comparison. In my experience reviewing procurement files, the disputes that go badly are almost never about sophisticated chemistry; they are about two parties who never agreed on what the number meant.

**Disclosure.** Peptides of China sells research peptides. This article is sourcing judgment, not an effects claim. Every compound discussed is supplied for research use only, and nothing here is a statement about human use, dosing or therapeutic benefit.

## Sources

1. ICH Q6B, Specifications: Test Procedures and Acceptance Criteria for Biotechnological/Biological Products (1999). https://database.ich.org/sites/default/files/Q6B%20Guideline.pdf
2. ICH Q2(R2), Validation of Analytical Procedures (2023). https://database.ich.org/sites/default/files/ICH_Q2%28R2%29_Guideline_2023_1130.pdf
3. ICH Q1A(R2), Stability Testing of New Drug Substances and Products (2003). https://database.ich.org/sites/default/files/Q1A%28R2%29%20Guideline.pdf
4. ICH Q7, Good Manufacturing Practice Guide for Active Pharmaceutical Ingredients (2000). https://database.ich.org/sites/default/files/Q7%20Guideline.pdf
5. U.S. FDA, 21 CFR 211.194, Laboratory Records. https://www.ecfr.gov/current/title-21/chapter-I/subchapter-C/part-211/subpart-J/section-211.194
6. U.S. FDA, 21 CFR 211.84, Testing and Approval or Rejection of Components, Drug Product Containers, and Closures. https://www.ecfr.gov/current/title-21/chapter-I/subchapter-C/part-211/subpart-E/section-211.84
7. D'Hondt M, Bracke N, Taevernier L, et al. Related impurities in peptide medicines. Journal of Pharmaceutical and Biomedical Analysis. 2014;101:2–30. https://doi.org/10.1016/j.jpba.2014.06.012
8. Fosgerau K, Hoffmann T. Peptide therapeutics: current status and future directions. Drug Discovery Today. 2015;20(1):122–128. https://doi.org/10.1016/j.drudis.2014.10.003
9. ISO/IEC 17025:2017, General requirements for the competence of testing and calibration laboratories. https://www.iso.org/standard/66912.html
