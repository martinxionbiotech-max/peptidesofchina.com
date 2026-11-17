---
title: "Sequence Confirmation for Peptides: Methods and Evidence"
slug: "what-is-sequence-confirmation-clinical-peptides"
description: "What sequence confirmation proves, how MS/MS, Edman degradation, and amino acid analysis differ, and the acceptance criteria a report should state."
author: "POC Tech Team"
---
**Sequence confirmation answers one question that purity and intact mass cannot: is the amino acid order what the label says?** A peptide can be 99% pure by HPLC area and still be the wrong sequence. It can show the correct intact mass and still carry a substitution that happens to be isobaric, or a deletion balanced by an unexpected modification. Only a method that reads the chain residue by residue closes that gap.

For research buyers, sequence confirmation is the difference between a batch that is verifiably the compound on the order and a batch that is merely consistent with it. For development programs, the same evidence is what supports a specification, a comparability assessment, or a supplier change.

This guide covers what each method proves, where each one fails, and the acceptance criteria that belong in a specification rather than in a conversation after delivery.

## What Sequence Confirmation Proves

Three claims get confused under the word "identity."

**Molecular identity.** The intact mass matches the formula. This is a strong signal and a weak proof: it confirms composition, not order.

**Sequence identity.** The residues are in the stated order. This requires fragmentation or stepwise degradation, and it is what "sequence confirmation" properly means.

**Compositional identity.** The amino acid ratios match theory. This catches some substitutions and misses positional information entirely.

A complete confirmation file answers all three, and each answer comes from a different method. A supplier who reports "identity confirmed by MS" has confirmed molecular identity; the sequence claim needs its own evidence. The [molecular weight verification guide](/blog/peptide-molecular-weight-verification-steps/) covers the mass side in detail.

## Intact Mass Is Not Sequence

Intact mass measurement is the first check because it is fast and sensitive. Electrospray ionization produces multiply charged ions; deconvolution converts them to a single neutral mass, which is compared with the theoretical mass calculated from the sequence.

The tolerance depends on the instrument. A unit-mass quadrupole is typically read to ±0.5 Da; a high-resolution instrument with 5 ppm accuracy on a 2,000 Da peptide resolves to ±0.01 Da. The tighter tolerance is useful because it distinguishes some modifications that differ by a fraction of a dalton, such as deamidation at +0.984 Da.

Mass alone cannot distinguish:

- **Leucine from isoleucine.** Same elemental composition, same mass, different residue.
- **A deletion plus a modification from the intended sequence.** A missing residue (−131.13 Da for leucine) and an unrelated addition can sum to the same nominal mass.
- **Positional isomers.** Two sequences with the same composition produce the same intact mass.
- **Isoaspartate from aspartate.** The cyclic imide opens to either form; the mass does not change.

Each of those requires fragmentation or a separate chemical method. A COA that lists intact mass and calls it "sequence confirmed" is overstating the evidence.

## MS/MS Sequencing and Fragment Ion Coverage

Tandem mass spectrometry fragments the peptide along the backbone and reads the resulting ladder. Collision-induced dissociation cleaves the amide bond, producing two complementary ion series: b ions retaining the N-terminal side and y ions retaining the C-terminal side. The mass difference between adjacent b ions, or adjacent y ions, gives the residue at that position.

Coverage is the operative metric. A 20-mer has 19 backbone bonds; a report that annotates fragments covering 90% of them has evidence for most positions but not all. The gaps matter: a substitution in an unannotated region is invisible.

Three acceptance criteria belong in the specification:

1. **Coverage.** At least 90% of backbone bonds assigned by b or y ions.
2. **Fragment quality.** At least two consecutive fragment ions supporting each assigned position, which reduces false assignment from noise peaks.
3. **Mass accuracy.** Fragment tolerance of 0.02 Da on a high-resolution instrument, or the instrument's stated tolerance with the calibration standard named.

De novo interpretation is the harder version of the same exercise: the software derives the sequence without a reference, which is what a buyer needs when the supplier's claimed sequence is itself in question. Database search is faster but assumes the answer, so it can confirm a expected sequence and miss a substitution that the scoring function tolerates. The [characterization reporting checklist](/blog/peptide-characterization-reporting-checklist/) lists the fields a de novo report should carry.

| Fragment series | Retains | Cleavage | Use |
|---|---|---|---|
| a / x | N-terminal / C-terminal | Cα–C bond | Complementary evidence |
| b / y | N-terminal / C-terminal | Amide bond | Standard CID sequencing |
| c / z | N-terminal / C-terminal | N–Cα bond | Electron transfer dissociation |

## Edman Degradation: What It Still Does Better

Edman degradation removes one residue at a time from the N-terminus and identifies it as a phenylthiohydantoin derivative. It is slower and less sensitive than MS/MS, and it requires a free N-terminus, which rules out acetylated or cyclized peptides. Within those limits it does two things MS/MS does poorly.

**It distinguishes leucine from isoleucine.** The two residues are isobaric and produce indistinguishable low-energy fragments. Edman chemistry separates them because the derivatives differ in retention time. A sequence with several Leu/Ile positions benefits from at least partial Edman coverage.

**It reads through certain modifications.** A labile modification that shatters in the gas phase may survive Edman chemistry long enough to be localized, depending on the chemistry involved.

The practical limit is around 50 residues, with signal quality declining as cycles accumulate and carryover from previous cycles accumulates. For a 20-mer, Edman can cover the full chain if the N-terminus is free; for a 40-mer, it usually confirms the first 15–20 positions and leaves the rest to MS/MS.

The two methods are complementary rather than competing. A confirmation file that uses MS/MS for coverage and Edman for the ambiguous isobaric positions is stronger than either alone.

## Amino Acid Analysis as a Composition Check

Amino acid analysis hydrolyzes the peptide into free residues and quantitates them. The standard condition is 6 M hydrochloric acid at 110 °C for 24 hours under vacuum, followed by chromatographic separation with ninhydrin or fluorescence detection.

The result is a molar ratio per residue, compared with the theoretical composition. A deviation of more than about ±10% at a given residue suggests a substitution, a deletion, or a hydrolysis artifact. The method is quantitative and orthogonal to MS, which makes it useful as a cross-check.

Its blind spots are well known. Tryptophan is destroyed by acid hydrolysis and must be measured separately after alkaline hydrolysis or with a protecting reagent. Cysteine requires oxidation to cysteic acid before hydrolysis, otherwise it is lost or recovered poorly. Asparagine and glutamine deamidate to aspartate and glutamate under the hydrolysis conditions, so the analysis reports the sum, not the original amide. Serine and threonine suffer partial destruction, which is corrected with a recovery factor rather than eliminated.

A composition table that matches theory within 10% is consistent with the claimed sequence. It is not proof of order, and it cannot localize a substitution. The [amino acid composition guide](/blog/amino-acid-composition-analysis-benefits/) covers the interpretation in more detail.

## Acceptance Criteria Worth Writing Down

A sequence confirmation specification should be testable by a second laboratory. The table below is a workable starting point for a research-grade synthetic peptide.

| Criterion | Acceptance value | Method |
|---|---|---|
| Intact mass | Within 5 ppm (HRMS) or ±0.5 Da (unit mass) | ESI-MS after deconvolution |
| Sequence coverage | ≥90% of backbone bonds | LC-MS/MS with b/y annotation |
| Fragment support | ≥2 consecutive ions per assigned position | MS/MS fragment map |
| Isobaric residues | Leu/Ile resolved at ambiguous positions | Edman degradation |
| Composition | Each residue within ±10% of theory | AAA after 6 M HCl hydrolysis |
| N-terminal state | Free or acetylated, as specified | MS mass shift (+42.011 Da) or Edman |
| Disulfide pairing | Stated pattern confirmed | Non-reducing digest plus MS/MS |

Two fields are often omitted and both are cheap to add. The first is the **N-terminal state**: an acetylated peptide has a +42.011 Da shift that can be mistaken for a modification elsewhere. The second is **disulfide pairing** for multi-cysteine peptides, where the linear mass is identical for every pairing pattern and only a non-reducing digest or partial reduction sequence can distinguish them.

## Where Confirmation Fails: Isobars and Modifications

Five situations produce a report that looks complete and is not.

**Isobaric substitutions.** Leu/Ile is the common case; another is a pair of residues whose combined mass matches a different pair. De novo interpretation with high-resolution fragments resolves most, but not all, and Edman remains the tie-breaker.

**Isoaspartate.** Aspartimide formation during synthesis or storage produces isoaspartate, which is isobaric with aspartate. Reversed-phase HPLC often shows a shoulder rather than a separate peak, and MS/MS can localize the isoform only with diagnostic ions. A specification that does not mention isoAsp will not detect it.

**Deamidation.** Asn to Asp conversion adds 0.984 Da. At the intact level it appears as a +1 Da satellite; at the fragment level it shifts the affected ions. A report that integrates only the monoisotopic peak can miss a partially deamidated batch.

**Oxidation.** Methionine oxidation adds 15.995 Da and is common after exposure to air or peroxide. It is easy to see by mass and easy to overlook if the report only lists the main component.

**Counterion adducts.** Sodium and potassium adducts appear as +22 Da and +38 Da. They are artifacts of sample preparation, not sequence defects, but they can obscure a real modification if the spectrum is not interpreted carefully.

The [purity versus concentration note](/blog/why-purity-and-concentration-tests-are-not-enough/) explains why a single main-peak percentage cannot carry these distinctions, and the [HPLC versus LC-MS comparison](/blog/hplc-vs-lc-ms-peptides/) covers method selection.

## Reading a Sequence Confirmation Report

A report should let a reviewer reconstruct the conclusion without contacting the laboratory. Six elements are non-negotiable.

1. **Sample identification.** Lot number, vial number, and the date the sample was drawn.
2. **Method summary.** Instrument type, ionization mode, fragmentation method, column, and gradient.
3. **Raw evidence.** Annotated spectrum or chromatogram, rather than a summary table alone.
4. **Theoretical versus observed mass.** Both values, with the mass error stated in ppm or Da.
5. **Coverage map.** Which bonds are supported by which ions, with gaps identified.
6. **Conclusion with limits.** "Consistent with the stated sequence over 94% of the backbone; positions 14–15 not resolved" is a usable conclusion. "Sequence confirmed" is not.

The [COA reading guide](/blog/how-to-read-a-peptide-coa-a-researchers-guide-to-hplc-and-ms-reports/) covers how this report sits alongside purity and endotoxin data, and the [quality testing pillar](/peptide-quality-testing/) describes the full release file.

## The Author's Take

**Position.** A sequence confirmation report without a coverage map is a marketing document. The number that matters is not "confirmed" but the percentage of backbone bonds supported by annotated fragments, and the positions that were not resolved.

**Reasoning.** Intact mass is cheap and useful, but it is a composition measurement. Buyers who accept it as sequence proof are relying on the assumption that a supplier with a correct mass could not have shipped a positional isomer, a Leu/Ile swap, or an isoaspartate variant. Those are exactly the errors that survive purification and pass a purity test. The cost of MS/MS with annotation is modest against the cost of repeating a study on a missequenced batch, and the coverage figure gives a buyer something to compare across suppliers and across lots. Where a peptide has multiple Leu/Ile positions or a documented aspartimide risk, Edman and isoAsp-specific checks earn their place in the specification.

**Disclosure.** Peptides of China sells research peptides. This article describes analytical methods and sourcing judgment; it is not an effects claim, a dosing guide, or medical advice. Products referenced on this site are supplied for laboratory research use only. Sequence documentation varies by product and batch, and buyers who need independent confirmation should arrange third-party testing after receipt.

## Sources

- Steen, H. & Mann, M. The abc's (and xyz's) of peptide sequencing. *Nature Reviews Molecular Cell Biology* (2004). [doi:10.1038/nrm1468](https://doi.org/10.1038/nrm1468)
- Medzihradszky, K. F. & Chalkley, R. J. Lessons in de novo peptide sequencing by tandem mass spectrometry. *Mass Spectrometry Reviews* (2013). [doi:10.1002/mas.21406](https://doi.org/10.1002/mas.21406)
- Keller, A. et al. Empirical statistical model to estimate the accuracy of peptide identifications made by MS/MS and database search. *Analytical Chemistry* (2002). [doi:10.1021/ac025747h](https://doi.org/10.1021/ac025747h)
- ICH Q6B: Specifications — Test Procedures and Acceptance Criteria for Biotechnological/Biological Products. [database.ich.org](https://database.ich.org/sites/default/files/Q6B%20Guideline.pdf)
- ICH Q2(R2): Validation of Analytical Procedures (2023). [database.ich.org](https://database.ich.org/sites/default/files/ICH_Q2%28R2%29_Guideline_2023_1130.pdf)
- 21 CFR Part 211 — Current Good Manufacturing Practice for Finished Pharmaceuticals. [ecfr.gov](https://www.ecfr.gov/current/title-21/chapter-I/subchapter-C/part-211)
- Aguilar, M.-I. Reversed-Phase High-Performance Liquid Chromatography. In *HPLC of Peptides and Proteins: Methods and Protocols* (2004). [doi:10.1385/1-59259-742-4:9](https://doi.org/10.1385/1-59259-742-4:9)
