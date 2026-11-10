---
title: "Common Peptide Synthesis Failures: A Buyer's Lab Guide"
slug: "common-peptide-synthesis-failures-a-practical-lab-guide"
description: "Where peptide synthesis fails: incomplete coupling, aspartimide, racemisation, oxidation, and how each impurity shows up in HPLC and mass spectra."
---
**Peptide synthesis rarely fails in one step. It fails by accumulation.** Thirty coupling cycles at 98% efficiency each still leave a crude product where roughly half the material is not the full-length target. The vial can look normal, dissolve cleanly, and pass a casual purity check while carrying deletion sequences, diastereomers, and oxidized species that matter to a sensitive assay.

The useful question for a buyer is not "did the synthesis fail" but "which failure mode is present, and can I see it in the data I was given". Each failure mode leaves an analytical signature: a mass shift, a retention behaviour, a peak pattern. This guide maps the common failures to those signatures, so a certificate can be read as a process record rather than a score. The [molecular weight verification guide](/blog/peptide-molecular-weight-verification-steps/) covers the mass arithmetic in more detail.

## Failure Is Cumulative, Not Binary

Solid-phase peptide synthesis builds a chain one residue at a time. Each cycle has three chemical steps that must go essentially to completion: deprotection of the N-terminal Fmoc group, coupling of the incoming protected amino acid, and washing to remove excess reagent.

The arithmetic is unforgiving. A 30-residue peptide at 99% coupling efficiency per step yields 0.99^30, or about 74% full-length material before purification. At 98% per step, the figure is about 55%. At 95%, it is about 21%. Those numbers explain why crude purity for long peptides sits in the 60–85% range even at well-run facilities, and why purification is not optional.

The corollary is that a crude purity figure tells you something about the process, not just the product, which is why [crude and purified grades](/blog/what-is-crude-vs-purified-peptide/) are not interchangeable. A 40-mer with 85% crude purity indicates unusually good coupling control. A 10-mer with 70% crude purity indicates a problem, because ten cycles cannot lose 30% without a systematic failure.

## Incomplete Coupling, Deprotection, and Truncated Impurities

Incomplete coupling leaves a fraction of chains missing the residue just added. When the next residue couples, the chain continues without it, producing a deletion sequence that is one residue shorter than the target.

The mass shift equals the mass of the missing residue minus water. For glycine, that is 57.02 Da; for alanine, 71.04 Da; for aspartic acid, 115.03 Da. Because the deletion peptide is often similar in hydrophobicity to the target, it can elute close to the main peak and be integrated as part of it.

Three process factors drive this failure. Steric hindrance from the growing chain makes coupling slower at the middle and C-terminal region of long peptides. Aggregation of the resin-bound chain hides reactive sites. And insufficient reagent excess — below three to five equivalents of activated amino acid — leaves unreacted amine.

Competent facilities monitor coupling with a ninhydrin or chloranil test after each step, or with on-resin mass spectrometry at intervals. A facility that cannot describe its monitoring method is relying on the final HPLC to catch a problem that was invisible for twenty cycles.

Fmoc removal uses 20% piperidine in dimethylformamide, usually for two short treatments rather than one long one. Incomplete deprotection leaves a capped chain that cannot accept the next residue, producing a truncated peptide ending at that position.

The analytical signature is a series of peaks with mass differences that correspond to the residues missing from the C-terminus. A cluster of truncated species is more diagnostic than a single impurity, because it points to a deprotection step that failed repeatedly rather than a one-off coupling problem.

Piperidine also causes a side reaction: it can form a piperidine amide at aspartic acid residues through aspartimide formation, which is covered below. Longer deprotection times reduce truncation and increase aspartimide. The process window is narrow, which is why deprotection conditions are sequence-specific.

## Aspartimide Formation and Iso-Aspartate

Aspartic acid followed by glycine, serine, or threonine is the classic aspartimide motif. Under basic deprotection conditions, the aspartyl side chain attacks the backbone amide, forming a five-membered succinimide ring. Hydrolysis of that ring can reopen at either carbonyl, producing the normal peptide or an iso-aspartate where the backbone runs through the side-chain carboxyl.

The mass signature is a loss of 18.011 Da for the aspartimide intermediate, and no mass change at all for iso-aspartate, because the formula is identical. This is the failure mode that mass spectrometry cannot see on its own. Separation requires chromatography that resolves the isoform, and confirmation usually requires enzymatic digestion or MS/MS fragmentation that locates the backbone branch.

The rate depends on sequence, temperature, and the basicity of the deprotection reagent. Piperidine at 20% is standard but aggressive; HOBt or Oxyma additives in the deprotection cocktail reduce aspartimide formation. A facility that runs every sequence on the same deprotection protocol will produce higher iso-aspartate levels on Asp-Gly motifs.

## Racemisation and Oxidation

Racemisation converts an L-residue to its D-enantiomer. The peptide gains no mass and changes little in hydrophobicity, so it can co-elute with the target and pass a mass check. The consequence is a diastereomer that behaves differently in a binding assay while looking identical on a certificate. The [characterization checklist](/blog/peptide-characterization-reporting-checklist/) lists the methods that can resolve it.

Cysteine is the highest-risk residue because the thiol side chain is acidic and the alpha proton is labile under the basic conditions used for Fmoc removal. Histidine is the second, through imidazole-catalysed proton exchange. Coupling reagents that activate without strong base, such as HATU with a hindered tertiary amine, reduce the risk compared with older carbodiimide methods.

Detection requires chiral chromatography, Marfey's reagent derivatisation followed by LC-MS, or careful MS/MS analysis. Most research certificates do not include a racemisation check, and most buyers do not ask for one. For a peptide where a single stereocentre determines activity, that gap is worth closing.

Methionine oxidises to methionine sulfoxide, adding 15.995 Da. Tryptophan oxidation adds the same mass for the first oxidation product and can proceed further. The reaction is driven by oxygen, light, and trace metals, and it can happen during synthesis, purification, lyophilisation, or storage.

On HPLC, oxidized species usually elute earlier than the reduced form because the sulfoxide is more polar. A pair of peaks separated by a small retention difference, with masses 16 Da apart, is the classic pattern. A certificate that reports 98% purity may be counting the oxidized variant as part of the main peak if the gradient is too steep to resolve it.

Control measures are mundane and effective: sparge buffers with nitrogen, avoid metal contact, protect from light, and add a sacrificial reductant where the chemistry allows. A supplier that ships a methionine-containing peptide in a clear vial with no desiccant has not controlled the most likely degradation pathway.

## Aggregation and On-Resin Difficulties

Hydrophobic sequences and those with a high propensity for beta-sheet structure can aggregate on the resin. Aggregated chains bury reactive sites, slowing coupling and deprotection, which produces a crude product rich in deletion and truncation impurities.

Sequence features that predict trouble include runs of hydrophobic residues, alternating hydrophobic-hydrophilic patterns, multiple cysteines, and long stretches without a turn-forming residue. A facility that recognises these features will switch to a lower-loading resin, use a solvent mixture with a chaotrope, or apply a pseudoproline dipeptide to disrupt secondary structure.

For the buyer, the signal is a crude purity that is much lower than the peptide length would predict, combined with a broad or split main peak. A split peak often indicates two conformers or a partially epimerised product rather than two distinct impurities.

## Cleavage Side Reactions and Counterion Residues

Cleavage from the resin uses 95% trifluoroacetic acid with scavengers. The reaction is aggressive, and side products form when scavengers are inadequate or the cleavage time is too long.

Common artefacts include tert-butyl cation adducts from protecting groups, formylation from residual formaldehyde, and acetylation from acetic acid in the cocktail. Mass shifts are +56.06 for tert-butyl, +28.01 for formyl, and +42.01 for acetyl. These are usually minor peaks, but they matter when the specification is tight.

The cleavage step also sets the counterion. The peptide leaves as the trifluoroacetate salt, and that is what the certificate describes unless an exchange step follows. Confusing the counterion with an impurity is a common buyer error: a 113.99 Da offset is a trifluoroacetate adduct, not a synthesis defect.

## Reading the Analytical Signature

The table below maps each failure mode to its mass shift, its chromatographic behaviour, and the method that confirms it.

| Failure mode | Mass shift | HPLC behaviour | Confirmatory method |
|---|---|---|---|
| Deletion of Gly | −57.02 Da | Often co-elutes with target | MS/MS sequence coverage |
| Deletion of Ala | −71.04 Da | Close to target | MS/MS |
| Deletion of Asp | −115.03 Da | Earlier elution | MS/MS |
| Incomplete deprotection | Series of −residue masses | Cluster of truncated peaks | MS with deconvolution |
| Aspartimide | −18.01 Da | Distinct earlier peak | MS plus digestion |
| Iso-aspartate | 0 Da | Closely eluting isomer | MS/MS or enzymatic digest |
| Racemisation | 0 Da | Co-elutes | Chiral HPLC or Marfey's reagent |
| Methionine oxidation | +15.99 Da | Earlier elution | MS/MS at the Met residue |
| TFA adduct | +113.99 Da | Broadened peak | Ion chromatography or MS adduct pattern |
| Sodium adduct | +21.98 Da | Variable | ICP-MS or ion chromatography |

Two rows deserve emphasis. Iso-aspartate and racemisation have no mass signature, so a certificate built on HPLC plus MS1 cannot detect them, a limitation the [COA reading guide](/blog/how-to-read-a-peptide-coa-a-researchers-guide-to-hplc-and-ms-reports/) returns to. If the peptide's activity depends on backbone geometry or a single stereocentre, the release panel needs a method that can see the difference.

Not every peptide carries the same risk. The matrix below groups sequences by the failure modes most likely to appear, which helps a buyer decide what to test rather than testing everything.

| Sequence feature | Higher risk | Extra check worth requesting |
|---|---|---|
| Asp-Gly or Asp-Ser motif | Aspartimide, iso-aspartate | MS/MS with backbone coverage |
| Multiple cysteines | Wrong disulfide pairing, dimer | Non-reducing HPLC, mass of dimer |
| C-terminal cysteine or histidine | Racemisation | Chiral analysis |
| Methionine or tryptophan | Oxidation | Mass spec for +16 Da species |
| Long hydrophobic stretch | Aggregation, deletion | Crude purity history, peak shape |
| Over 30 residues | Cumulative deletion | MS/MS coverage percentage |
| N-terminal glutamine | Pyroglutamate formation | Mass shift −17.03 Da |

## What a Buyer Should Ask When a Batch Fails

A failed batch is a data problem before it is a commercial one. The first step is to establish whether the failure is in the material or in the measurement.

Ask for the raw chromatogram with the peak table, not the summary. Compare the retention times and peak areas with the certificate. If the impurity peaks are present in the raw data but absent from the summary table, the reporting threshold is the issue.

Ask for the mass spectrum with charge states. A deconvoluted mass alone hides adducts and mixed populations. If the main peak deconvolutes to the target mass but the raw spectrum shows a second envelope, the sample contains two species.

Ask which method was used and whether it was validated for this sequence. A generic 15-minute gradient is not a validated method for a 40-mer, and comparing its result with a supplier's 30-minute gradient produces a difference that neither party can explain.

Then decide the disposition. A minor impurity at 0.3% area is usually acceptable for research work. A deletion sequence at 2% that co-elutes with the target is not, because it changes the effective concentration of the material in every assay. The [HPLC versus LC-MS guide](/blog/hplc-vs-lc-ms-peptides/) explains how to read the two data sets together, the [purity versus concentration guide](/blog/why-purity-and-concentration-tests-are-not-enough/) covers the mass-balance question that follows, and the [quality testing pillar](/peptide-quality-testing/) sets out the full release panel.

## The Author's Take

**Position.** A peptide certificate that reports HPLC purity and a single deconvoluted mass has not demonstrated that the batch is free of the two failure modes most likely to ruin an assay: iso-aspartate and racemisation. Buyers working with Asp-Gly motifs or chiral-sensitive targets should commission the extra method rather than assume the release panel covered it.

**Reasoning.** Both defects are isobaric with the target. They add no mass, change the formula by nothing, and often elute close enough to be integrated as part of the main peak. A supplier running a standard panel is not hiding them; the panel simply cannot see them. The cost of chiral chromatography or a digestion plus MS/MS experiment is small compared with repeating a study whose results were confounded by a diastereomer. The same logic applies to oxidation: a 16 Da species is easy to detect if the method resolves it and easy to miss if the gradient is steep. Buyers who specify the method, not just the purity threshold, get data that can answer the question they actually have.

**Disclosure.** Peptides of China sells research peptides. This article describes synthesis chemistry and procurement judgment; it is not an effects claim, a dosing guide, or medical advice. Products referenced on this site are supplied for laboratory research use only. Impurity profiles vary by sequence and batch, and buyers should request the analytical data for the specific lot they intend to use.

## Sources

- Merrifield, R. B. Solid Phase Peptide Synthesis. I. The Synthesis of a Tetrapeptide. *Journal of the American Chemical Society* 85, 2149–2154 (1963). [doi:10.1021/ja00897a025](https://doi.org/10.1021/ja00897a025)
- Fields, G. B., Noble, R. L. Solid phase peptide synthesis utilizing 9-fluorenylmethoxycarbonyl amino acids. *International Journal of Peptide and Protein Research* 35, 161–214 (1990). [doi:10.1111/j.1399-3011.1990.tb00939.x](https://doi.org/10.1111/j.1399-3011.1990.tb00939.x)
- Kaiser, E., Colescott, R. L., Bossinger, C. D., Cook, P. I. Color test for detection of free terminal amino groups in the solid-phase synthesis of peptides. *Analytical Biochemistry* 34, 595–598 (1970). [doi:10.1016/0003-2697(70)90146-6](https://doi.org/10.1016/0003-2697%2870%2990146-6)
- Sarin, V. K., Kent, S. B. H., Tam, J. P., Merrifield, R. B. Quantitative monitoring of solid-phase peptide synthesis by the ninhydrin reaction. *Analytical Biochemistry* 117, 147–157 (1981). [doi:10.1016/0003-2697(81)90704-1](https://doi.org/10.1016/0003-2697%2881%2990704-1)
- ICH Q6B Specifications: Test Procedures and Acceptance Criteria for Biotechnological/Biological Products. International Council for Harmonisation. [database.ich.org](https://database.ich.org/sites/default/files/Q6B%20Guideline.pdf)
- USP &lt;621&gt; Chromatography. United States Pharmacopeia. [usp.org/usp-nf](https://www.usp.org/usp-nf)
- ICH Q2(R2) Validation of Analytical Procedures (2023). International Council for Harmonisation. [database.ich.org](https://database.ich.org/sites/default/files/ICH_Q2%28R2%29_Guideline_2023_1130.pdf)
- FDA Guidance for Industry: Bioanalytical Method Validation (2018). U.S. Food and Drug Administration. [fda.gov](https://www.fda.gov/regulatory-information/search-fda-guidance-documents/bioanalytical-method-validation-guidance-industry)
