---
title: "Epithalon Wholesale Sourcing: A 2026 Manufacturer Guide"
slug: "epithalon-wholesale-sourcing-a-b2b-guide-to-direct-manufacturer-channels-2026"
description: "A B2B guide to Epithalon wholesale sourcing: AEDG identity, tetrapeptide analytics, manufacturer versus trader channels, and lot-level documents."
---
Epithalon wholesale sourcing is a small-peptide problem disguised as a commodity purchase. The sequence is four residues — Ala-Glu-Asp-Gly, or AEDG — and the molecule is about 390 Da. That simplicity makes synthesis cheap and comparison difficult: the fill weight can be dominated by water and counterion, the peptide has no aromatic residue for a 280 nm assay, and almost any vial with a white cake looks the same.

A direct manufacturer channel does not fix those facts. It only gives the buyer a better chance of getting a lot-specific record that describes what is actually in the vial. This guide sets out the identity fields, analytical methods, channel checks, and receiving steps that make an Epithalon purchase auditable. The procurement steps below assume a laboratory or reseller buyer and a research-use-only end use.

## The Short Answer

Buy Epithalon on the sequence, not the trade name. Require AEDG in one-letter code, a stated counterion, net peptide content, water content, and a lot-specific HPLC chromatogram with a mass spectrum. Ask whether the seller manufactures the peptide or buys bulk powder and vials it. Price per gram is meaningless until those fields are fixed, because a 10 mg fill at 98% area purity and 70% peptide content contains 7 mg of peptide, while a 10 mg fill at 95% purity and 85% content contains 8.5 mg.

## What "Epithalon Wholesale" Actually Means

Epithalon is the common name for the synthetic tetrapeptide AEDG. The sequence appears in the research literature as Epitalon, Epithalon, and epithalamin-related fractions, which is one source of catalogue confusion. The synthetic peptide is not the same material as the bovine pineal extract that preceded it, and a listing that blurs the two is already imprecise.

The research literature is concentrated. The foundational papers come from the St. Petersburg Institute of Bioregulation and Gerontology and its collaborators. A 2003 paper in *Bulletin of Experimental Biology and Medicine* reported telomerase activity and telomere elongation in human somatic cells exposed to Epithalon. A 2025 study in *Biogerontology* examined telomere length in human cell lines and attributed the effect to either telomerase upregulation or alternative lengthening of telomeres, depending on the line. The second paper is a useful corrective to the first: the mechanism is not uniform, and the endpoint depends on the model.

For procurement, the literature matters for one reason. It defines the material of interest as AEDG, not as a pineal extract, not as a longer fragment, and not as a product with an undefined "epithalamin" content. Write that definition into the request.

## Why a Four-Residue Peptide Is Hard to Compare

Small peptides concentrate several analytical problems.

**No aromatic residue.** AEDG contains alanine, glutamic acid, aspartic acid, and glycine. None absorbs at 280 nm. A purity assay must run at 214 nm, where the peptide bond absorbs, and the mobile phase must be transparent at that wavelength. A certificate that reports "purity by UV" without a wavelength is not comparable to one that states 214 nm.

**Counterion mass.** The molecule has two acidic residues, so the salt form can carry a meaningful counterion load. An acetate salt and a trifluoroacetate salt of the same peptide do not have the same mass per milligram of peptide. Ion chromatography or capillary electrophoresis can quantify the counterion; a certificate that says only "acetate salt" leaves the fill mass undefined.

**Water content.** Lyophilised tetrapeptides can hold several percent water, especially if the lyophilisation cycle is short. Karl Fischer titration gives a number. A 10 mg fill with 6% water contains 0.6 mg of water before any counterion is counted.

**Net peptide content.** Amino acid analysis after hydrolysis, or nitrogen determination by Kjeldahl, gives the peptide mass fraction. For many lyophilised peptide salts the figure falls between 70% and 90% w/w. A certificate that reports only chromatographic purity has not measured content.

**Weak retention.** A hydrophilic tetrapeptide can elute near the solvent front on a standard C18 gradient. A method with a shallow initial hold, low organic start, and a 120 Å column is easier to reproduce than a generic 5–95% gradient. The exact conditions should be printed on the certificate.

The practical consequence is that two suppliers can both report 98% and ship materially different amounts of peptide. The [article on why purity and concentration tests are not enough](/blog/why-purity-and-concentration-tests-are-not-enough/) covers the distinction in more detail.

## Specification Fields for a Tetrapeptide

The table below is a workable purchase specification for Epithalon. The values are typical research-grade targets, not a universal standard; the supplier should state its own limits and the method behind each result.

| Field | Target or reported value | Method |
| --- | --- | --- |
| Sequence | Ala-Glu-Asp-Gly (AEDG) | Sequence document or certificate |
| Residue count | 4 | Certificate |
| Molecular mass | ~390.4 Da | ESI-MS, ±0.5 Da unit resolution |
| Appearance | White to off-white lyophilised cake | Visual inspection |
| Identity | Main peak mass matches AEDG | LC-MS |
| Purity | ≥98% by area at 214 nm | RP-HPLC, C18 |
| Net peptide content | 70–90% w/w | Amino acid analysis or nitrogen determination |
| Water content | ≤5.0% w/w | Karl Fischer titration |
| Counterion | Acetate, with a numeric limit | Ion chromatography |
| Endotoxin | Numeric EU/mg result | LAL assay |
| Fill mass | Stated per vial, with tolerance | Gravimetric check |
| Storage | −20 °C, protected from light | Supplier stability statement |

Two rows are often missing from real certificates: counterion and net content. Ask for them before the quote is finalised. If the supplier cannot provide a numeric counterion result, ask for the ion chromatography chromatogram; if it cannot provide net content, ask whether amino acid analysis is available for the lot.

## Direct Manufacturer Channel vs Trader vs Repackager

"Direct manufacturer channel" is a phrase with no legal definition. The table below separates the roles a seller can play and the documents each role can realistically produce.

| Role | What it controls | Documents it can usually provide | Main risk to the buyer |
| --- | --- | --- | --- |
| Synthesis site | Coupling, cleavage, purification, lyophilisation | Batch record, in-house COA, chromatogram, spectrum | Limited customer-facing service; lot minimums |
| Contract manufacturer | Synthesis and fill under a customer's specification | Batch record, COA, deviation reports | Specification may be owned by the buyer, not the seller |
| Trader or distributor | Purchase and resale | Supplier COA, packing list | Cannot explain the lot or the method |
| Repackager | Division and vialing of bulk powder | Repackaging record, sometimes a COA | No synthesis record; fill heterogeneity and labeling risk |
| Sourcing platform | Coordination, availability, logistics | Manufacturer-side documents when available | Not the manufacturer and not a testing laboratory |

A seller can occupy more than one row. The question to ask is not "are you a manufacturer?" but "which legal entity performed the synthesis, which entity filled the vials, and which entity signed the certificate?" The answers should be names, not categories.

Peptides of China coordinates manufacturer-side sourcing and international logistics; it does not synthesize peptides or operate an analytical laboratory. That distinction belongs in the buyer's record, because it determines what the seller can verify first-hand and what must come from the manufacturing side.

For a second product form, the catalogue also lists [NA-Epithalon amidate](/catalog/na-epithalon-amidate/). The amidated form is a different molecule with a different mass and should not be substituted without a specification change.

## Batch Documentation and Lot Linkage

A lot-specific document set for Epithalon is short enough to check in an afternoon:

1. Certificate of analysis with the lot string, fill date, tests, methods, limits, and results.
2. HPLC chromatogram with integration table and wavelength.
3. Mass spectrum with the observed mass and the expected mass.
4. Amino acid analysis or nitrogen determination report for net content.
5. Karl Fischer report for water.
6. Ion chromatography report for counterion.
7. Endotoxin report with method and numeric result.
8. Packing list linking the lot to the shipped vials.

The most common failure is not a missing document. It is a document that describes a different lot. Check the lot string character by character, including prefixes and suffixes, and check the fill date against the shipping date. A certificate dated two years before dispatch may still be valid, but the supplier should state the storage condition and retest basis.

The [COA reading guide](/blog/how-to-read-a-peptide-coa-a-researchers-guide-to-hplc-and-ms-reports/) shows where the method header, integration table, and mass labels usually sit. The [documentation package comparison](/blog/peptide-documentation-package/) explains why a repackager often cannot produce items 2 through 6.

## MOQ, Price, and Order Structure

Epithalon is cheap to synthesize, so the commercial terms matter more than the chemistry. A quote should state the fill mass per vial, the number of vials per box, the price per box, the minimum order, the lead time, and the shipping term. Without those five numbers, a per-milligram price is not a price.

Peptides of China currently works with a USD 600 product minimum, excluding shipping, and a USD 10 processing deposit credited toward the final invoice. Standard ordering begins at one same-product kit or box of 10 vials. Mixed-product orders can be combined to reach the minimum, and the current terms should be confirmed at the time of request.

Shipping terms should be explicit. DAP means the seller delivers to the named place and the buyer handles import formalities; DDP means the seller carries them. Neither term guarantees customs clearance, and a seller that promises clearance is overstating its control. The [customs guide](/blog/research-peptide-customs-clearance-a-professional-b2b-sourcing-guide-2026/) covers the documents a buyer should have ready.

## Receiving Checks and Independent Testing

Receiving inspection for a tetrapeptide should take less than an hour and produce a record that survives an audit.

- Photograph the outer box, the vial label, and the cake before opening.
- Match the lot string on the label to the certificate and packing list.
- Weigh three sealed vials if fill mass is stated.
- Store the vials at −20 °C, protected from light.
- Send one vial to a contract laboratory for identity, purity, water, and content.
- Retain the other two as reference samples.

A useful independent panel for Epithalon is RP-HPLC at 214 nm, ESI-MS for identity, Karl Fischer for water, and amino acid analysis for content. Endotoxin testing is a separate decision, based on the planned assay. The [molecular weight verification workflow](/blog/peptide-molecular-weight-verification-steps/) explains how to compare an observed mass with the theoretical value, and the [solubility troubleshooting guide](/blog/peptide-solubility-troubleshooting/) covers the handling issues that can make a clean lot look problematic.

If the independent result differs from the certificate, do not start with an accusation. Send the chromatogram, the method, and the sample handling record to the supplier and ask for an explanation. A supplier that engages with the data is more useful than one that offers a replacement without asking why.

## The Author's Take

**Position.** For Epithalon, I would rather buy from a channel that can explain the counterion and the net peptide content than from one that advertises a higher purity number. The molecule is too small for a purity percentage to carry the quality story. A 98% area result on a 70%-content lot is a different product from a 98% result on an 88%-content lot, and the buyer pays for peptide, not for chromatogram area.

**Reasoning.** The analytical chemistry is unambiguous. AEDG has no aromatic residue, so the assay must be run at 214 nm; the salt form can carry a counterion load; lyophilised powder can hold several percent water; and content must be measured separately from purity. Those facts do not change with the seller's marketing. What changes is whether the seller can produce the four numbers — purity, water, counterion, content — for the lot being shipped. A direct manufacturer channel is valuable because it can produce them, not because "direct" is inherently better.

**Disclosure.** Peptides of China sells research peptides. The analysis above is sourcing judgment rather than an efficacy claim; all material is offered for research use only and none of it is intended for human or veterinary use. This is not medical advice. Commercial terms change, so verify them on the [how sourcing works](/how-it-works/) page before ordering.

## Sources

1. Overview of Epitalon—Highly Bioactive Pineal Tetrapeptide with Promising Properties. *International Journal of Molecular Sciences*. 2025. https://doi.org/10.3390/ijms26062691
2. Epithalon peptide induces telomerase activity and telomere elongation in human somatic cells. *Bulletin of Experimental Biology and Medicine*. 2003. https://doi.org/10.1023/a:1025493705728
3. Epitalon increases telomere length in human cell lines through telomerase upregulation or ALT activity. *Biogerontology*. 2025. https://doi.org/10.1007/s10522-025-10315-x
4. ICH Q2(R2), Validation of Analytical Procedures (2023). https://database.ich.org/sites/default/files/ICH_Q2%28R2%29_Guideline_2023_1130.pdf
5. ICH Q6A, Specifications: Test Procedures and Acceptance Criteria for New Drug Substances and New Drug Products (1999). https://database.ich.org/sites/default/files/Q6A%20Guideline.pdf
6. FDA, Analytical Procedures and Methods Validation for Drugs and Biologics (2015). https://www.fda.gov/regulatory-information/search-fda-guidance-documents/analytical-procedures-and-methods-validation-drugs-and-biologics
7. 21 CFR 211.84, Testing and approval or rejection of components, drug product containers, and closures. https://www.ecfr.gov/current/title-21/chapter-I/subchapter-C/part-211/subpart-E/section-211.84
8. ISO/IEC 17025:2017, General requirements for the competence of testing and calibration laboratories. https://www.iso.org/standard/66912.html
9. D'Hondt M, et al. Related impurities in peptide medicines. *Journal of Pharmaceutical and Biomedical Analysis*. 2014;101:2–30. https://doi.org/10.1016/j.jpba.2014.06.012
