---
title: "Peptide Molecular Weight Verification: A Practical MS Workflow"
slug: "peptide-molecular-weight-verification-steps"
description: "How to calculate theoretical peptide mass, choose between MALDI-TOF and LC-ESI-MS, and set acceptance criteria that a supplier COA can be audited against."
---

Verification is a comparison, not a measurement. You calculate the theoretical mass of the stated sequence, acquire an intact mass on a named instrument, and decide whether the difference falls inside a tolerance you declared before the run — typically ±1 Da on MALDI-TOF or under 5 ppm on a Q-TOF or Orbitrap. A mass spectrum on its own proves that something ionized. Only the comparison proves that the vial contains the peptide on the label.

That distinction matters at the procurement stage, because most certificates of analysis report a number without the context needed to audit it. This guide covers the arithmetic, the platform choice, the sample preparation that decides whether the spectrum is interpretable, and the acceptance criteria worth writing into a purchase specification.

## What the comparison actually requires

Four inputs have to be fixed before any instrument time is booked:

1. **The sequence**, in single-letter code, including any non-standard residues and terminal modifications.
2. **The mass mode** — monoisotopic or average — stated explicitly for both the theoretical and observed values.
3. **The instrument class**, because tolerance is a property of the platform, not of the peptide.
4. **The acceptance window**, chosen before seeing the result so the result cannot choose the window.

Most disputes about a "failed" mass check trace back to one of these inputs being unstated. A vendor reports 2,411.7 Da, the buyer calculates 2,410.9 Da, and both are correct — one used average mass on a low-resolution reading, the other used monoisotopic mass on a high-resolution calculation. The apparent 0.8 Da discrepancy is an artifact of mixed conventions, not a synthesis failure.

For a broader treatment of how identity and purity evidence fit together, see the [HPLC versus LC-MS comparison](/blog/hplc-vs-lc-ms-peptides) and the guide to [reading a peptide COA](/blog/how-to-read-a-peptide-coa-a-researchers-guide-to-hplc-and-ms-reports).

## Mass arithmetic: monoisotopic, average, and the terminal water

A peptide's mass is the sum of its residue masses plus one water molecule, because each condensation removes H₂O and the intact chain retains the termini:

**M = Σ(residue masses) + 18.01528 Da** (average) or **+ 18.01056 Da** (monoisotopic)

The difference between those two water values — 0.0047 Da — is trivial on its own. The difference between average and monoisotopic *residue* masses is not. Carbon alone contributes about 0.0107 Da per atom when averaged over natural isotope abundance, and a 2,000 Da peptide contains roughly 90 carbon atoms. The gap accumulates at about 0.5 Da per 1,000 Da of peptide mass, which is why it becomes visible on any instrument with better than 500 ppm accuracy.

A worked example makes the scale concrete. Take the sequence ACDEF. The monoisotopic residue masses sum to 565.18424 Da; adding monoisotopic water at 18.01056 Da gives 583.19480 Da. The average residue masses sum to 565.59830 Da; adding average water at 18.01528 Da gives 583.61358 Da. The 0.419 Da gap is 719 ppm. On a MALDI instrument with ±1 Da tolerance it is invisible; on an Orbitrap it is a catastrophic mismatch if the two numbers are compared in the wrong modes. This is the single most common false failure in peptide mass verification, and it costs buyers batches that were manufactured correctly.

Two practical rules follow. First, use monoisotopic mass for anything compared against high-resolution MS data. Second, use average mass for bench weighing and for stoichiometry, where isotopic fine structure is irrelevant. Never mix the two inside one comparison.

## Choosing the platform: MALDI-TOF, LC-ESI, or MS/MS

MALDI-TOF is the fast path. Laser desorption from a crystalline matrix produces mostly singly charged ions, so the spectrum shows one dominant [M+H]⁺ peak per species and needs little interpretation. It tolerates moderate contamination and consumes femtomole to picomole amounts.

LC-ESI-MS is the accurate path. Electrospray produces a charge-state envelope, and deconvolution of that envelope yields a neutral mass with accuracy that single-charge MALDI rarely matches. The trade-off is sensitivity to salts, ion-pairing agents, and co-eluting contaminants.

| Parameter | MALDI-TOF | LC-ESI Q-TOF | LC-ESI Orbitrap |
| --- | --- | --- | --- |
| Dominant charge state | Singly charged [M+H]⁺ | Multiply charged, z = 2–6 | Multiply charged, z = 2–6 |
| Typical mass accuracy | ±0.1–1 Da external; 10–20 ppm internal | 3–5 ppm | 2–5 ppm |
| Resolution | 10,000–20,000 | 20,000–40,000 | 70,000+ at m/z 200 |
| Salt tolerance | Moderate | Low | Low |
| Sample load | 0.5–1 µL of a 1 mg/mL solution | 1–5 µL of 0.1–0.5 mg/mL | 1–5 µL of 0.1–0.5 mg/mL |
| Run time per sample | 5–15 min | 20–60 min with gradient | 20–60 min with gradient |
| Best use | Rapid identity check, batch triage | Modification mapping, accurate intact mass | Trace variants, isotope-resolved work |

For a 2,000 Da peptide, 5 ppm is 0.01 Da. That precision is what allows you to distinguish deamidation (+0.984 Da) from a missed proton or a calibration drift. MALDI at ±1 Da cannot make that call, and no amount of peak picking will fix it.

## Sample preparation decides the spectrum

Ion suppression and adduct formation are preparation problems, not instrument problems. Three contaminants account for most poor spectra:

- **Alkali salts.** Sodium and potassium dominate the spectrum when desalting is incomplete. Relative to [M+H]⁺, the sodium adduct appears at +21.9819 Da and the potassium adduct at +37.9559 Da.
- **TFA.** Trifluoroacetic acid is excellent for reversed-phase chromatography and hostile to electrospray. Keep it at or below 0.05% for ESI, or remove it before injection.
- **Detergents and chaotropes.** SDS, Triton, guanidine, and high phosphate concentrations suppress ionization and foul the source.

A workable cleanup for a 1 mg/mL stock: bind to a C18 ZipTip or equivalent SPE bed, wash with 0.1% formic acid, elute in 60–80% acetonitrile with 0.1% formic acid, and inject or spot directly. For MALDI, mix 1 µL eluate with 1 µL of 10 mg/mL α-cyano-4-hydroxycinnamic acid in 50% acetonitrile / 0.1% TFA and dry at room temperature. Use DHB for glycopeptides and larger constructs.

Concentration matters more than most protocols admit. Below roughly 0.1 mg/mL, adduct peaks and matrix clusters compete with the analyte signal; above 1 mg/mL, detector saturation and space-charge effects broaden peaks. Aim for the middle of that range. If the peptide will not go into solution cleanly in the first place, work through the [solubility decision framework](/blog/peptide-solubility-troubleshooting) before spending instrument time on a suspension.

## Reading the spectrum: charge states, isotopes, and artifacts

In ESI, adjacent charge states are separated in m/z by approximately (M + z)/z². Isotope peaks within one charge state are separated by 1.0034/z, which is why a triply charged peptide shows isotope spacing near 0.334 m/z. Both relationships let you assign charge by inspection before deconvolution software runs.

The isotope envelope carries its own information. For peptides above roughly 2–2.5 kDa, the monoisotopic peak is no longer the tallest peak in the envelope; the M+1 or M+2 isotope often dominates. Software that assumes the tallest peak is monoisotopic will return a mass that is 1–2 Da too high. Force the deconvolution to use the calculated monoisotopic peak position, or fit the whole envelope rather than picking a single peak.

Common shifts, and what to do first:

| Observed shift | Likely cause | First action |
| --- | --- | --- |
| +15.9949 Da | Methionine or tryptophan oxidation | Re-prepare from a fresh aliquot; check storage history |
| +21.9819 Da vs [M+H]⁺ | Sodium adduct | Repeat desalting; avoid glass and phosphate buffers |
| +37.9559 Da vs [M+H]⁺ | Potassium adduct | Same as sodium; check salt grade and labware |
| +0.9840 Da | Deamidation (Asn to Asp) | Resolve on high-resolution MS; check buffer pH and age |
| −0.9840 Da | C-terminal amidation | Confirm against the synthesis specification |
| −17.0265 Da | N-terminal pyroglutamate | Expected for N-terminal Gln at acidic pH |
| +42.0106 Da | N-acetylation | Confirm whether the modification was ordered |
| +57.0215 Da | Carbamidomethylation | Reduced and alkylated sample, not a native artifact |
| >100 Da deficit | Truncation or wrong sequence | Escalate to peptide mapping |

A deficit larger than 100 Da is not an adduct. It is a different molecule, and no amount of cleanup will close the gap.

## Acceptance criteria and ppm arithmetic

Mass accuracy in ppm is:

**ppm = (observed − theoretical) / theoretical × 10⁶**

At 2,000 Da, 1 Da equals 500 ppm and 0.01 Da equals 5 ppm. Write the window into the specification as both an absolute and a relative figure, because neither alone is sufficient across a catalog: a 1 Da window is loose at 1 kDa and impossible at 10 kDa.

Reasonable defaults:

- MALDI-TOF, external calibration: ±1 Da or ±500 ppm, whichever is tighter.
- MALDI-TOF, internal calibration: ±0.02 Da or ±20 ppm.
- Q-TOF: ±5 ppm.
- Orbitrap: ±5 ppm, with ±3 ppm achievable on clean samples.

Calibrate with a standard that brackets the expected mass, not one that sits at one end of the range. A three-point calibration spanning 500–3,500 Da is adequate for most catalog peptides; a single-point calibration near the target is not. The [reference standard guide](/blog/types-of-peptide-reference-standards-a-lab-guide) covers how calibrant grade and storage affect that bracket.

If a result falls outside the window, repeat the acquisition before rejecting the batch. The repeat costs an hour; a wrongful rejection costs a relationship. Rejection should follow two independent failures, or one failure plus an orthogonal method that agrees.

## When intact mass is not enough

Intact mass confirms composition, not sequence. Two peptides with the same elemental composition — or a target plus a co-eluting truncation that happens to match within tolerance — can pass an intact-mass check. Escalate when the intact result is ambiguous, when the COA claims a modification, or when the observed mass is unexplained by any single shift in the table above.

Peptide mapping is the standard escalation. Digest with trypsin (cleaves C-terminal to Lys and Arg), separate the fragments by reversed-phase LC, and acquire MS/MS. Fragment ion coverage of at least 70% across the sequence is the usual threshold for a confident assignment; below 50%, too much of the molecule is unobserved to rule out substitutions. ExPASy's [FindPept](https://web.expasy.org/findpept/) handles unspecific cleavage and modification mass offsets when the digest does not behave as predicted.

Orthogonal methods add cheap confidence. Tricine-SDS-PAGE resolves peptides in the 1–5 kDa range that glycine gels lose entirely. Capillary electrophoresis gives a quantitative purity figure with better reproducibility than slab gels. Size-exclusion chromatography answers a different question — whether the peptide is monomeric in solution — which intact mass cannot address. If the intact spectrum suggests a deletion rather than a modification, the [synthesis failure guide](/blog/common-peptide-synthesis-failures-a-practical-lab-guide) maps the production causes to the mass evidence you are looking at.

## Auditing a supplier COA

A mass value is auditable only when the surrounding record is complete. Use this checklist before accepting a lot:

| Field | Acceptable | Reason |
| --- | --- | --- |
| Sequence | Full single-letter code | Without it, the theoretical mass cannot be recalculated |
| Theoretical mass | Numeric value plus mode | "Monoisotopic" or "average" must be explicit |
| Observed mass | Numeric value plus mode | Compare like with like |
| Instrument | Manufacturer and model | Tolerance depends on platform class |
| Accuracy | ppm or Da, stated | A bare number cannot be judged |
| Chromatogram | Trace attached, not just a percentage | Area percent without a trace is unauditable |
| Lot linkage | Lot number on the spectrum | Proves the data belongs to this batch |
| Raw data | Available on request | Screenshots can be edited; raw files less easily |

Two red flags deserve a direct question. An observed mass that matches theory to 0.000 Da suggests the number was copied rather than measured. A COA listing "mass spectrometer" with no model suggests the analysis was outsourced without documentation.

When comparing a vendor's MALDI result to your own Orbitrap result, convert both to the same mass mode and compare each against its own tolerance. A vendor result at ±1 Da is not evidence of a worse batch than your own at 3 ppm; it is evidence of a different instrument class. The [manufacturer verification protocol](/blog/china-peptide-manufacturer-verification-a-2026-b2b-sourcing-protocol) covers the wider audit, and the [characterization reporting checklist](/blog/peptide-characterization-reporting-checklist) lists the documents worth requesting alongside the COA.

## The Author's Take

**Position:** The mass mode, not the mass value, is where most sourcing disputes are actually decided. A COA that reports a number without saying whether it is monoisotopic or average is not a weaker document — it is an unauditable one, and it should be treated that way in procurement.

**Reasoning:** Intact mass is only meaningful relative to a stated theoretical value at a stated tolerance on a stated platform. Remove any one of those and the number becomes decorative. Buyers who ask for monoisotopic mass, the instrument model, and the ppm figure get a document they can check in ten minutes. Buyers who accept "MW: 2411.7" get a number that could be right, could be average mass, and could belong to the previous lot. The request itself is cheap, and suppliers with real analytical control answer it without friction. Suppliers who cannot answer it have told you something useful.

**Disclosure:** Peptides of China sells research peptides. This article reflects sourcing and documentation judgment, not a claim about any compound's effects. Products are supplied for laboratory research use only and are not for human or veterinary use.

## Sources

- IUPAC. *Definitions of terms relating to mass spectrometry (IUPAC Recommendations 2013).* Pure and Applied Chemistry 85(7): 1515–1609. https://doi.org/10.1351/PAC-REC-06-04-06
- Aebersold R, Mann M. *Mass spectrometry-based proteomics.* Nature 422: 198–207 (2003). https://pubmed.ncbi.nlm.nih.gov/12634793/
- Steen H, Mann M. *The ABC's (and XYZ's) of peptide sequencing.* Nature Reviews Molecular Cell Biology 5(9): 699–711 (2004). https://pubmed.ncbi.nlm.nih.gov/15340378/
- ExPASy PeptideMass — theoretical peptide mass and modification calculator. https://web.expasy.org/peptide_mass/
- ExPASy FindPept — fragment mass matching with unspecific cleavage and PTM handling. https://web.expasy.org/findpept/
- Bern M, Caval T, Kil YJ, Tang W, Becker C, Carlson E, Kletter D, Sen KI, et al. *Parsimonious charge deconvolution for native mass spectrometry.* Journal of Proteome Research 17(3): 1216–1226 (2018). https://pubmed.ncbi.nlm.nih.gov/29376659/
- Marty MT. *A universal score for deconvolution of intact protein and native electrospray mass spectra.* Analytical Chemistry 92(6): 4395–4401 (2020). https://pubmed.ncbi.nlm.nih.gov/32069030/
- *Applications of tandem mass spectrometry (MS/MS) in protein analysis for biomedical research.* Molecules 27(8): 2411 (2022). https://pubmed.ncbi.nlm.nih.gov/35458608/
