---
title: "Sourcing TB-500 from China: Identity and Batch Verification"
slug: "sourcing-tb-500-from-china-a-2026-b2b-procurement-and-verification-guide"
description: "A 2026 B2B guide to sourcing TB-500 from China: full-length versus fragment identity, COA fields, HPLC and LC-MS criteria, and receiving checks."
---
TB-500 can be sourced from China at research grade, but the name is not a specification. Before comparing price, a buyer needs four facts in writing: the exact sequence, the residue count, the N-terminal modification, and the counterion. Without those four, two suppliers can quote the same "TB-500" and ship different molecules.

The rest of this guide is the procurement process that follows from that sentence: how the name became ambiguous, what a usable specification looks like, which analytical records answer which question, and how to inspect a lot on arrival. The audience is laboratory and reseller buyers working under research-use terms, not clinical buyers.

## Why "TB-500" Is Not a Specification

Regulatory and anti-doping literature use "TB-500" for a short fragment of thymosin beta-4. The research supply market often uses the same label for the full 43-residue protein. Both usages are in circulation, and neither is enforced by a naming authority.

A 2012 paper in *Drug Testing and Analysis* characterised the material in a product sold as TB-500 and identified an N-terminally acetylated fragment corresponding to residues 17–23 of thymosin beta-4, with the sequence Ac-LKKTETQ. That is a seven-residue peptide of about 889 Da. The full protein is 43 residues and roughly 4.96 kDa. The mass difference is more than fivefold.

This matters because catalogue copy is inconsistent. Some listings describe a 17-amino-acid fragment, which does not match the published 17–23 fragment and may be a different truncation altogether. Others show a 43-residue sequence in the specification but a fragment price. A buyer who does not request the sequence is comparing labels, not materials.

The ambiguity is not a reason to avoid the compound. It is a reason to make identity the first line of the purchase order.

## Full-Length Thymosin Beta-4 vs the 17–23 Fragment

The two materials share an actin-binding motif but differ in size, synthesis route, and analytical behaviour. The table below is the comparison a buyer should be able to reproduce from the supplier's own documents.

| Attribute | Full-length thymosin beta-4 | 17–23 fragment (Ac-LKKTETQ) |
| --- | --- | --- |
| Residue count | 43 | 7 |
| Approximate mass | 4.96 kDa | 0.89 kDa |
| N-terminus | Acetylated | Acetylated |
| Actin-binding motif | Present, within a larger folded context | Present as an isolated linear motif |
| Synthesis burden | Longer chain, more coupling and purification steps | Short chain, cheaper and faster |
| Typical HPLC window | Wide-pore C18, shallow gradient | Standard C18, steeper gradient |
| Mass confirmation | Deconvolution of multiple charge states | Single charge state dominates |
| Common catalogue label | TB-500, thymosin beta-4 | TB-500, TB-500 fragment |

Neither column is "better" without a study design. The full protein carries sequence context that the fragment lacks; the fragment removes mass and folding complexity that may complicate an assay. What a buyer cannot accept is a certificate that does not say which column the lot belongs to.

A separate article on [TB-500 versus thymosin beta-4](/blog/tb-500-vs-thymosin-beta-4-what-you-re-actually-getting/) covers the research rationale for each form. For procurement, the practical point is simpler: choose one, write it into the specification, and require every subsequent lot to match it.

## A Sequence-Level Specification

A specification that says "TB-500, ≥98%" is not a specification. It is a purity claim attached to an undefined material. The minimum viable document set for a sequence-level purchase contains the fields below.

| Field | Example entry | Why it matters |
| --- | --- | --- |
| Sequence | Ac-LKKTETQ or the 43-residue sequence in one-letter code | Defines the molecule without relying on a trade name |
| Residue count | 7 or 43 | Catches truncation and concatenation errors |
| N-terminal modification | Acetylated | The acetyl group adds 42.0106 Da; des-acetyl material is a different peptide |
| C-terminal form | Free acid or amide | Changes mass and charge; must match the batch record |
| Counterion | Acetate or trifluoroacetate | Changes fill mass and net peptide content |
| Assay basis | Area percent by RP-HPLC at 214 nm | Purity by area is not mass fraction |
| Net peptide content | 70–90% w/w by amino acid analysis or nitrogen determination | Converts fill mass into peptide mass |
| Water content | ≤5.0% w/w by Karl Fischer | Water is fill weight that is not peptide |
| Endotoxin | Numeric EU/mg result with method | "Endotoxin free" is not a result |
| Lot and fill date | String matching the vial label | Links the document to the physical unit |

Two fields deserve emphasis because they are routinely omitted. The first is the C-terminal form. A free acid and an amide differ by about 1 Da, which is inside the error of a low-resolution mass read but outside the specificity of a sequence. The second is net peptide content. A 10 mg fill at 98% chromatographic purity and 75% peptide content contains 7.5 mg of peptide, not 9.8 mg. Every dilution calculation downstream inherits that difference.

Ask for the specification as a table, not as a sentence in an email. A supplier that cannot produce the table before payment is unlikely to produce it after.

## Analytical Evidence: HPLC, LC-MS, and Acetylation

Three measurements do most of the identity work, and each answers a different question.

**Reverse-phase HPLC** answers how much UV-absorbing signal belongs to the main peak. A workable method for a 43-residue peptide uses a wide-pore C18 column (300 Å), 4.6 × 250 mm, 5 µm particles, 0.1% TFA in water against 0.1% TFA in acetonitrile, a shallow gradient such as 20–50% organic over 30 minutes, 1.0 mL/min, 20 µL injection, and detection at 214 nm. For the seven-residue fragment, a steeper 5–65% gradient on a standard 120 Å column resolves the peptide and its deletion impurities.

Pore size is not a minor detail. A 120 Å column can exclude part of a 43-mer from the stationary phase, producing broad peaks and poor recovery. A 300 Å column gives the protein access to the surface. If a certificate does not state column dimensions and gradient, the purity number is not reproducible.

**LC-MS** answers whether the observed mass matches the expected mass. For the fragment, the expected monoisotopic mass of Ac-LKKTETQ is about 889 Da; a unit-resolution instrument should land within ±0.5 Da, and a high-resolution instrument within ±5 ppm. For the full protein, electrospray produces a charge envelope that must be deconvoluted; a report that lists a single m/z value as the molecular weight has not done that work.

**Acetylation** is confirmed by the mass shift. The acetyl group adds 42.0106 Da to the N-terminus. A batch with the correct amino acid sequence but no acetyl group will be 42 Da lighter. On a 43-mer, that difference is easy to miss at low resolution; on the fragment, it is large enough to see clearly. Either way, the certificate should state the modification, not leave it to inference.

Impurity profiling is a separate exercise. The D'Hondt review of related impurities in peptide medicines sets out the categories a buyer will encounter: deletion sequences, truncated sequences, diastereomers, and modified forms. None of those is visible as a single number on a certificate. The [guide to reading a peptide COA](/blog/how-to-read-a-peptide-coa-a-researchers-guide-to-hplc-and-ms-reports/) walks through the fields line by line, and the [molecular weight verification workflow](/blog/peptide-molecular-weight-verification-steps/) covers the mass side in more detail.

## Documents That Link the Vial to the Batch

A certificate is only useful if it describes the lot in the box. The document chain below is what a buyer should request, in order of increasing difficulty.

1. **Lot-specific COA.** Carries the same lot string as the vial label, the fill date, the tests performed, the methods, the results, and the specification limits.
2. **Raw chromatogram.** Shows the baseline, the main peak, the impurity peaks, and the integration table. A certificate without a chromatogram is a summary, not evidence.
3. **Mass spectrum.** Shows the charge states and the deconvoluted mass. For a fragment, a single spectrum is enough; for the full protein, the deconvolution report matters.
4. **Batch production record (redacted).** Shows the synthesis run, purification fractions, and fill step. A manufacturer can produce this; a trader usually cannot.
5. **Packing list.** Ties the lot, fill mass, and number of vials to the shipment.
6. **Stability or retest statement.** Gives the basis for the expiry or retest date.
7. **Endotoxin report.** Separate from purity, with method and numeric result.

The [documentation package comparison](/blog/peptide-documentation-package/) explains which supplier type can realistically provide each item. The short version: a manufacturer with an in-house analytical unit can produce the first three; a repackager often cannot produce any of them for the lot it ships.

## Supplier Screening Before the First Order

Supplier screening is mostly a test of whether the answers are specific. The questions below are designed so that a vague reply is as informative as a wrong one.

- Which legal entity manufactures the peptide, and at which site?
- Is the material synthesized in-house or purchased as bulk powder and vialed?
- Which lot will ship, and can the COA carry that lot string?
- Who performed the HPLC and MS analyses, on which instruments?
- What is the net peptide content, and how was it measured?
- Is the material the full 43-mer or the 17–23 fragment?
- Can raw chromatogram and spectrum files be shared under NDA?
- What happens if independent testing finds a nonconformity?

A supplier that answers six of eight in writing is worth a sample order. A supplier that answers two and promises the rest after deposit is telling you how the relationship will run.

Facility claims need evidence proportionate to their size. An ISO 9001 certificate covers quality management, not peptide identity. An ISO/IEC 17025 accreditation applies to the testing laboratory, not the synthesis site. GMP status, where claimed, should name the authority and the scope. The [manufacturer verification protocol](/blog/china-peptide-manufacturer-verification-a-2026-b2b-sourcing-protocol/) sets out the document trail for each claim.

## Receiving Inspection and Order Mechanics

Receiving inspection starts before the box is opened. Photograph the outer packaging, the label, and the vial cake. Check that the lot string on the label matches the COA and the packing list. Weigh the sealed vial if the fill mass is stated; a large discrepancy is a question, not automatically a fault, because fill mass includes water and counterion.

Sample three vials from the lot, not one. Store them at −20 °C, label them with the supplier lot and your internal sample ID, and send one to a contract laboratory. The retained vials are what let you answer a question six months later. The [COA authentication guide](/blog/coa-verified-peptides-supplier-how-to-authenticate-research-purity-in-2026/) covers the date and identifier checks that expose a recycled certificate.

On the commercial side, Peptides of China currently works with a USD 600 product minimum, excluding shipping, and a USD 10 processing deposit credited toward the final invoice. Standard ordering begins at one same-product kit or box of 10 vials. Those terms are commercial, not a quality claim; confirm them at the time of order.

International shipping is arranged per destination. Customs classification, documentation, and import requirements vary by country, and no supplier can guarantee clearance. The [customs clearance guide](/blog/research-peptide-customs-clearance-a-professional-b2b-sourcing-guide-2026/) explains the document set a buyer should prepare, and the nomenclature question is covered in the customs documentation rather than assumed from a catalogue listing.

## The Author's Take

**Position.** The right way to source TB-500 from China is to stop treating "TB-500" as a product name and start treating it as a category with at least two members. I would not place a first order until the supplier states the sequence, the residue count, the N-terminal modification, and the counterion in writing. A supplier that can do that is usually also the one that can produce a chromatogram and a mass spectrum. A supplier that cannot is selling a label.

**Reasoning.** The published record shows that material sold as TB-500 has included the acetylated 17–23 fragment, while the supply market also sells the full 43-mer under the same name. The two differ by more than fivefold in mass and by a large margin in synthesis cost. Price competition therefore pushes toward the cheaper form unless the buyer writes the identity into the order. Analytical methods can distinguish the forms, but only if the buyer knows which form was ordered and asks for the data that proves it. That is a procurement control, not a laboratory problem.

**Disclosure.** Peptides of China sells research peptides, so this article reflects a commercial perspective on sourcing. It is a procurement judgment, not a claim about any compound's effects, and every material discussed is for research use only. Nothing here is medical advice or describes human or veterinary use. Confirm current commercial terms on the [how sourcing works](/how-it-works/) page.

## Sources

1. Knoop A, et al. Synthesis and characterization of the N-terminal acetylated 17-23 fragment of thymosin beta 4 identified in TB-500, a product suspected to possess doping potential. *Drug Testing and Analysis*. 2012. https://doi.org/10.1002/dta.1402
2. Thymosin β4 and Actin: Binding Modes, Biological Functions and Clinical Applications. *Current Protein and Peptide Science*. 2023. https://doi.org/10.2174/1389203724666221201093500
3. ICH Q2(R2), Validation of Analytical Procedures (2023). https://database.ich.org/sites/default/files/ICH_Q2%28R2%29_Guideline_2023_1130.pdf
4. ICH Q6A, Specifications: Test Procedures and Acceptance Criteria for New Drug Substances and New Drug Products (1999). https://database.ich.org/sites/default/files/Q6A%20Guideline.pdf
5. FDA, Analytical Procedures and Methods Validation for Drugs and Biologics (2015). https://www.fda.gov/regulatory-information/search-fda-guidance-documents/analytical-procedures-and-methods-validation-drugs-and-biologics
6. 21 CFR 211.84, Testing and approval or rejection of components, drug product containers, and closures. https://www.ecfr.gov/current/title-21/chapter-I/subchapter-C/part-211/subpart-E/section-211.84
7. ISO/IEC 17025:2017, General requirements for the competence of testing and calibration laboratories. https://www.iso.org/standard/66912.html
8. D'Hondt M, et al. Related impurities in peptide medicines. *Journal of Pharmaceutical and Biomedical Analysis*. 2014;101:2–30. https://doi.org/10.1016/j.jpba.2014.06.012
