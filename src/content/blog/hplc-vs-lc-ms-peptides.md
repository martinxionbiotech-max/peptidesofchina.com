---
title: "HPLC vs LC-MS for Peptides: Purity, Identity, and COA Evidence"
slug: "hplc-vs-lc-ms-peptides"
description: "How RP-HPLC purity and LC-MS identity differ, which method answers which question, and the specific data a peptide batch release should include."
---
**HPLC and LC-MS answer two different questions, and a peptide batch needs both answers.** Reversed-phase HPLC with UV detection at 214 or 220 nm reports how much of the integrated peak area belongs to the target peak. LC-MS reports the mass of what is in that peak, and LC-MS/MS fragmentation reports whether the amino acid sequence matches the label. A purity number without a mass confirmation is a quantity claim with no identity behind it. A mass match without a chromatogram is an identity claim with no purity behind it.

The practical consequence for buyers is simple: a certificate of analysis that lists "purity 99.2%" and nothing else has not told you what the 99.2% is. The rest of this guide covers how each method generates its number, where each one fails, and how to choose a method based on batch risk rather than habit.

If you are still mapping the broader documentation set, the [COA reading guide](/blog/how-to-read-a-peptide-coa-a-researchers-guide-to-hplc-and-ms-reports/) covers batch linkage and report structure, while this page stays on the analytical chemistry.

## What RP-HPLC Measures, and What It Does Not

Reversed-phase HPLC separates peptides by hydrophobicity. A C18 stationary phase binds hydrophobic side chains; a water/acetonitrile gradient with 0.1% trifluoroacetic acid gradually reduces the mobile phase polarity and releases peptides in order of increasing hydrophobicity. Trifluoroacetic acid does two jobs: it protonates basic residues to sharpen peaks, and it pairs with cationic peptides to improve retention. The typical analytical column for a synthetic peptide is 4.6 × 250 mm, 5 µm particles, 300 Å pore size, run at 35 °C and 1.0 mL/min.

Detection usually happens at 214 nm or 220 nm. The peptide backbone amide bond absorbs strongly below 230 nm, so these wavelengths see nearly every peptide regardless of sequence. A 280 nm channel is useful when tryptophan or tyrosine is present, but it misses peptides that lack aromatic residues. This is why a COA that reports 280 nm purity for a peptide with no aromatic residues is reporting a weak signal, not a clean one.

Purity is calculated as area percent: the target peak area divided by the total integrated area, multiplied by 100. That number is relative. It does not account for water content, counterions, residual salts, or material that never elutes from the column. A peptide can be 99% pure by area and still be 80% peptide by mass once trifluoroacetate, sodium, and moisture are counted. [Purity and concentration tests measure different things](/blog/why-purity-and-concentration-tests-are-not-enough/), and a COA should not let one stand in for the other.

## Reading the Chromatogram: Wavelength, Gradient, and System Suitability

A chromatogram carries more information than the purity percentage printed above it. Four parameters tell you whether the method was capable of resolving the sample in the first place.

**Wavelength and bandwidth.** A 214 nm channel with 4 nm bandwidth is standard for peptides. A 220 nm channel reduces baseline drift from trifluoroacetic acid and is common on older instruments. If the report does not state the wavelength, the purity number cannot be compared with any other lab's result.

**Gradient slope.** A shallow gradient, such as 5–65% acetonitrile over 30 minutes, spreads hydrophobic variants apart. A steep 5–95% gradient over 10 minutes compresses them into the target peak. Fast gradients are not invalid, but they hide closely eluting impurities, and they make the purity figure look better than a slower method would.

**System suitability.** USP &lt;621&gt; expects the chromatography to meet predetermined criteria before sample results are accepted. For peptide assays, common criteria are resolution of at least 2.0 between the target and the nearest specified impurity, tailing factor no greater than 2.0, and five replicate injections with a relative standard deviation of 2.0% or less. A report that omits these values gives no evidence the run was controlled.

**Integration parameters.** The reporting threshold matters. A method that ignores peaks below 0.05% area will report a higher purity than one that integrates down to 0.01%. Neither is wrong, but the number means different things, and the reporting threshold belongs in the method description rather than in a footnote.

| Parameter | Typical peptide setting | What it controls |
|---|---|---|
| Detection | 214 nm, 4 nm bandwidth | Backbone amide absorbance; near-universal response |
| Column | C18, 4.6 × 250 mm, 5 µm, 300 Å | Hydrophobic selectivity and peptide access to pores |
| Mobile phase | A: 0.1% TFA in water; B: 0.1% TFA in acetonitrile | Ion pairing and peak shape |
| Gradient | 5–65% B over 30 min | Resolution of hydrophobic variants |
| Flow / temperature | 1.0 mL/min / 35 °C | Retention reproducibility |
| Injection | 10 µL of 1 mg/mL | Signal within detector linear range |
| System suitability | Resolution ≥ 2.0; tailing ≤ 2.0; RSD ≤ 2.0% | Evidence the run was fit for purpose |

## Where UV Purity Numbers Break Down

The main weakness of UV purity is that it reports absorbance, not structure. Several classes of impurity absorb at the same wavelength as the target and can elute close enough to be integrated as one peak.

- **Deletion sequences.** A peptide missing one residue from a 20-mer has a mass difference of roughly 57 to 186 Da, depending on the residue, but often a similar hydrophobicity. It can sit under the target peak.
- **Deamidation.** Asparagine to aspartate conversion adds 0.984 Da and shifts retention slightly. For a large peptide, the shift may be a few seconds.
- **Oxidation.** Methionine oxidation adds 15.995 Da and usually shifts retention earlier, but not always enough to resolve.
- **Truncation and capping.** Acetylated or formylated failure sequences can be more hydrophobic than the target and elute later, sometimes outside the integration window.
- **Counterion and salt effects.** Trifluoroacetate content changes peak shape and retention without changing peptide purity.

Area percent also assumes that every species has the same extinction coefficient at the detection wavelength. They do not. A peptide with three tryptophans absorbs far more at 280 nm than a truncated variant with one, so a 280 nm method can under-report the impurity. At 214 nm the variation is smaller but still present, because the number of amide bonds differs between the target and a deletion sequence.

The result is a number that is useful for batch-to-batch comparison within one validated method, and unreliable for comparing across suppliers, columns, or gradients. This is the gap that mass spectrometry fills.

## What LC-MS Adds: Mass, Charge State, and Sequence

LC-MS attaches a mass spectrometer to the same separation. As the peptide elutes, electrospray ionization produces multiply charged ions, usually +2 to +4 for a 1–4 kDa peptide. The instrument records mass-to-charge ratios, and deconvolution software converts the charge envelope into a neutral molecular mass.

A mass match is necessary but not sufficient. If the theoretical mass is 1,411.63 Da and the measured value is 1,411.65 Da, the difference is 14 ppm, which is close enough to warrant a closer look at calibration and peak shape. If the measured value is 1,411.63 Da within 2 ppm, the identity is strongly supported. But mass alone cannot distinguish leucine from isoleucine, and it cannot tell a linear peptide from a cyclized isomer with the same formula.

That is where MS/MS enters. The instrument selects a precursor ion, fragments it along the amide backbone, and records the product ions. Fragments that retain the N-terminus are b ions; fragments that retain the C-terminus are y ions. A complete b/y ladder read against the expected sequence confirms residue order rather than just composition. For a 10–30 residue peptide, coverage of at least 90% of the backbone by assigned b/y ions is a reasonable target for a release-grade report.

MS/MS also catches what UV missed. A co-eluting impurity with a different mass appears as a second precursor in the extracted ion chromatogram, even when the UV trace shows one peak. That is the practical difference between "the peak is clean" and "the peak contains one molecule."

## Judging Mass Accuracy and Resolution

Mass accuracy is usually reported in parts per million: the measured mass minus the theoretical mass, divided by the theoretical mass, multiplied by one million. The acceptance threshold depends on the instrument and the question.

| Instrument class | Typical mass accuracy | Resolution | Appropriate use |
|---|---|---|---|
| Single quadrupole | ±0.1 Da (unit mass) | Low | Confirming nominal mass only |
| Triple quadrupole (MRM) | ±0.1 Da at unit resolution | Low | Quantitation of a known peptide |
| TOF | ±5 ppm with external calibration | 10,000–30,000 | Identity confirmation and impurity mass |
| Orbitrap | ±2–5 ppm external; <2 ppm with internal lock mass | 60,000–120,000 | Sequence variants, modifications, deconvolution |

Three details change how a mass result should be read. First, calibration: an external calibration at 5 ppm is weaker evidence than an internal lock mass at 1 ppm. Second, adducts: sodium adducts appear at +21.98 Da and can be mistaken for a modification if the report does not annotate them. Third, TFA: trifluoroacetic acid suppresses electrospray signal, so a method transferred directly from UV to MS often needs formic acid or a lower TFA concentration.

Resolution matters for large peptides. At 60,000 resolving power, the isotope envelope of a 3 kDa peptide is partly resolved; at 120,000 it is cleanly separated. A report that claims "mass confirmed" without stating resolution, calibration mode, and adduct handling is giving a conclusion without the evidence behind it. [Molecular weight verification](/blog/peptide-molecular-weight-verification-steps/) walks through the calculation and the common failure modes.

## HPLC vs LC-MS: Side-by-Side

The two methods are complementary, not competing. The table below maps what each one contributes to a batch record.

| Question | RP-HPLC-UV | LC-MS (MS1) | LC-MS/MS |
|---|---|---|---|
| How much target is present? | Yes, as area% or assay | Semiquantitative | No |
| Is the molecular mass correct? | No | Yes | Yes |
| Is the sequence correct? | No | Partial | Yes, by b/y ions |
| Can it detect co-eluting impurities? | Only if retained differently | Yes, by mass | Yes, by mass and fragments |
| Does it detect counterions or water? | No | No | No |
| Typical sample load | 10–100 µg | 1–10 µg | 1–10 µg |
| Typical run time | 20–40 min | 15–30 min | 30–60 min |
| Destructive? | Yes | Yes | Yes |
| Best-fit role | Quantitation and release | Identity confirmation | Sequence and variant mapping |

Neither column answers the counterion question. Trifluoroacetate content, sodium content, and water content require ion chromatography, inductively coupled plasma, or Karl Fischer titration. A COA that reports HPLC and MS but no counterion data has left a known gap, particularly for peptides supplied as acetate or TFA salts.

## Method Selection by Batch Risk

Running full LC-MS/MS on every vial is expensive and slow. Running HPLC alone on a new supplier's first batch is cheap and risky. The useful rule is to match method intensity to the consequence of being wrong.

| Scenario | Minimum method | Recommended addition | Reason |
|---|---|---|---|
| Reorder from an established supplier, same lot documentation | HPLC-UV with system suitability | MS1 identity check | Confirms nothing changed between batches |
| First order from a new supplier | HPLC-UV | MS1 plus MS/MS | No batch history to rely on |
| Modified, cyclic, or non-standard peptide | HPLC-UV | MS/MS with modification mapping | Mass shift alone cannot localize a modification |
| Batch intended for a long study | HPLC-UV | MS1, MS/MS, and stability timepoint | Reproducibility across months |
| Disputed or anomalous result | HPLC-UV | MS/MS plus orthogonal method (NMR or CE) | Resolves ambiguity that one method cannot |
| Formulation or salt change | HPLC-UV | Ion chromatography plus MS1 | Counterion change affects mass balance |

The same logic applies to the release specification. A 98.0% area threshold at 214 nm is a reasonable internal criterion for a research-grade peptide, but it means little if the method's reporting threshold is 0.5% or the gradient is too steep to resolve the main impurity. The specification and the method have to be read together.

## Batch Release Checks and COA Requests

A batch record built on both methods should let an independent reviewer reconstruct what was measured. The checklist below is the minimum set worth requesting; [peptide characterization reporting](/blog/peptide-characterization-reporting-checklist/) expands each item into a full data package.

| Check | Target or expectation | Evidence to request |
|---|---|---|
| Identity by MS | Within 5 ppm of theoretical mass | Deconvoluted spectrum with charge states annotated |
| Sequence by MS/MS | ≥ 90% backbone coverage | Annotated b/y ion map |
| Purity by HPLC | ≥ 98.0% area at 214 nm | Full chromatogram with gradient and wavelength |
| System suitability | Resolution ≥ 2.0; tailing ≤ 2.0; RSD ≤ 2.0% | Suitability table from the run |
| Impurity profile | Individual peaks above 0.05% reported | Peak table with retention times |
| Counterion | Stated identity and content | Ion chromatography or titration report |
| Water content | Stated by Karl Fischer | KF result and method |
| Endotoxin | Method, limit, and numeric result | LAL or rFC report with spike recovery |
| Batch linkage | Same lot on vial, COA, and invoice | Lot number cross-reference |

Two checks are frequently skipped. The first is system suitability: without it, the chromatogram could have been produced on a failing column. The second is spike recovery for endotoxin, which is covered in the [endotoxin testing guide](/blog/endotoxin-testing-peptide-manufacturing/). A COA that passes identity and purity but fails either of these is incomplete rather than wrong.

For a broader view of how these individual tests fit into a supplier qualification, the [laboratory verification guide](/blog/peptide-testing-and-analysis-a-professional-guide-to-laboratory-verification/) covers sampling, chain of custody, and third-party testing. The [quality testing page](/peptide-quality-testing/) describes the documentation set we work from.

## The Author's Take

**Position.** A peptide COA should be rejected as incomplete if it reports HPLC purity without a mass confirmation, or mass without a chromatogram. The two data types are cheap enough at batch scale that a supplier choosing to publish only one is making a documentation decision, not an analytical one.

**Reasoning.** Purity by UV area is a relative measurement with known blind spots: co-eluting deletion sequences, deamidation variants, and counterions all sit outside what the number can see. Mass spectrometry closes the identity gap but does not quantify. Buyers who treat either result as a complete release test end up comparing numbers that were never measuring the same thing. The cost difference between an HPLC-only panel and an HPLC plus MS1 panel is small relative to the cost of repeating a study with a misidentified batch.

**Disclosure.** Peptides of China sells research peptides. This article describes analytical methods and sourcing judgment; it is not an effects claim, a dosing guide, or medical advice. Products referenced on this site are supplied for laboratory research use only. Analytical documentation varies by product and batch, and buyers who need independent verification should arrange third-party testing after receipt.

## Sources

- USP &lt;621&gt; Chromatography. United States Pharmacopeia. [usp.org/usp-nf](https://www.usp.org/usp-nf)
- USP &lt;1225&gt; Validation of Compendial Procedures. United States Pharmacopeia. [usp.org/usp-nf](https://www.usp.org/usp-nf)
- ICH Q2(R2) Validation of Analytical Procedures (2023). [database.ich.org](https://database.ich.org/sites/default/files/ICH_Q2%28R2%29_Guideline_2023_1130.pdf)
- ICH Q6B Specifications: Test Procedures and Acceptance Criteria for Biotechnological/Biological Products. [database.ich.org](https://database.ich.org/sites/default/files/Q6B%20Guideline.pdf)
- FDA Guidance for Industry: Bioanalytical Method Validation (2018). [fda.gov](https://www.fda.gov/regulatory-information/search-fda-guidance-documents/bioanalytical-method-validation-guidance-industry)
- FDA Guidance for Industry: Q2B Validation of Analytical Procedures: Methodology (1996). [fda.gov](https://www.fda.gov/regulatory-information/search-fda-guidance-documents/q2b-validation-analytical-procedures-methodology)
- Rivier, J. et al. Reversed-phase high-performance liquid chromatography: preparative purification of synthetic peptides. *Journal of Chromatography A* (1984). [doi:10.1016/S0021-9673(01)93709-4](https://doi.org/10.1016/S0021-9673%2801%2993709-4)
- Aguilar, M.-I. Reversed-Phase High-Performance Liquid Chromatography. In *HPLC of Peptides and Proteins: Methods and Protocols* (2004). [doi:10.1385/1-59259-742-4:9](https://doi.org/10.1385/1-59259-742-4:9)
- Sleno, L. Applications of high-resolution mass spectrometry in drug discovery and development. In *Applications of High-Resolution Mass Spectrometry in Drug Discovery and Development* (Future Science, 2014). [doi:10.4155/ebo.13.515](https://doi.org/10.4155/ebo.13.515)
- Ma, B. Peptide De Novo Sequencing with MS/MS. In *Encyclopedia of Algorithms* (2016). [doi:10.1007/978-1-4939-2864-4_286](https://doi.org/10.1007/978-1-4939-2864-4_286)
