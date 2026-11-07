---
title: "Crude vs Purified Peptides: Purity Grades, Yield, and What the COA Proves"
slug: "what-is-crude-vs-purified-peptide"
description: "What crude and purified peptide mean in practice: synthesis by-products, preparative HPLC, purity grades, net peptide content, yield loss, and COA verification."
---

Crude peptide is the material recovered after cleavage from the synthesis resin, before chromatographic fractionation. It contains the target sequence plus truncated sequences, deletion variants, diastereomers, residual protecting groups, cleavage reagents, and counterions. Purified peptide is the fractionated product that meets a stated purity threshold, usually 95% or 98% by reversed-phase HPLC area normalization. The distinction is not cosmetic: it changes the impurity profile, the net peptide content, the cost per milligram of active sequence, and the experiments the material can support.

This guide explains where the two grades come from, how the purity number is produced, and which specification fields a buyer should require before treating a "98% peptide" as equivalent to another supplier's 98%.

## What crude peptide actually contains

Solid-phase peptide synthesis builds a chain from the C-terminus on a resin. Each coupling adds an amino acid, and each step has a yield below 100%. A 20-residue peptide with 99% average coupling efficiency leaves roughly 82% of chains full length before cleavage; at 98% average efficiency, the full-length fraction falls to about 67%. Those are illustrations, not supplier specifications, but they explain why crude material is a mixture.

The main impurities in crude peptide fall into five groups:

- **Truncated sequences** from incomplete coupling or premature termination.
- **Deletion sequences** missing one or more internal residues.
- **Diastereomers** from racemization, most often at cysteine and histidine during activation.
- **Oxidized or reduced forms**, especially for methionine, cysteine, and tryptophan.
- **Salts, solvents, and protecting-group remnants** carried through cleavage and precipitation.

Crude peptide is not waste. For screening, epitope mapping, or process development, a 50–70% crude preparation can be adequate and much cheaper. The error is assuming that a crude lot behaves like a purified lot in a quantitative assay.

## What purification removes, and what it cannot

Preparative reversed-phase HPLC separates peptides by hydrophobicity. The target sequence elutes at a characteristic retention time, and the fraction collector takes the portion of the peak that meets a purity criterion. That process removes most deletion and truncation variants that differ enough in hydrophobicity. It also concentrates the target and exchanges the sample into a volatile mobile phase.

It does not remove everything:

- **Co-eluting impurities** with similar hydrophobicity can survive the main peak cut.
- **Diastereomers** may separate poorly on a C18 column, particularly when the change is a single stereocenter far from the hydrophobic face.
- **Counterions** from the mobile phase, typically trifluoroacetate, remain associated with basic residues.
- **Water** remains after lyophilization, often at 3–8% by Karl Fischer titration.
- **Residual solvents** can persist if drying is incomplete.

A 98% HPLC purity means 98% of the integrated peak area at the chosen wavelength is the target peak. It does not mean 98% of the vial mass is peptide. The difference is net peptide content, and it is the number that determines how much sequence you actually have.

## How purity is measured, and where the number misleads

Most certificates report purity by area normalization: the target peak area divided by the total integrated peak area, multiplied by 100. The result depends on the column, gradient, wavelength, injection load, and integration threshold. A typical method uses a C18 column of 4.6 × 250 mm with 5 µm particles and 300 Å pores, a water/acetonitrile mobile phase with 0.1% TFA, a gradient of 5–65% acetonitrile over 30 minutes, detection at 214 or 220 nm, and an injection load of 10–50 µg. Change any of those and the reported percentage can move by several points.

A certificate that states "purity 98.5%" without these details is not reproducible. Two labs can test the same lot and report 96% and 99% by changing the gradient or the integration threshold. The [HPLC versus LC-MS guide](/blog/hplc-vs-lc-ms-peptides) explains why retention time alone is weak identity evidence, and the [COA reading guide](/blog/how-to-read-a-peptide-coa-a-researchers-guide-to-hplc-and-ms-reports) shows how to audit the chromatogram.

Area normalization also ignores non-UV-absorbing impurities. Salts, water, and residual solvents do not appear in the chromatogram. That is why a complete specification includes Karl Fischer water, residual solvent by gas chromatography, counterion content by ion chromatography, and net peptide content by amino acid analysis or nitrogen determination.

## The purification train

Preparative HPLC is the default for research peptides, but it is not the only step. A typical purification sequence combines crude precipitation, one or two chromatographic steps, and lyophilization.

| Step | Purpose | Typical condition | What it costs |
| --- | --- | --- | --- |
| Ether precipitation | Remove cleavage reagents and some small fragments | Cold methyl tert-butyl ether, repeated washes | Solvent handling and loss of very hydrophobic peptide |
| Preparative RP-HPLC | Main purity upgrade | C18, 5–10 µm, acetonitrile gradient with 0.1% TFA | Column time, solvent, yield loss |
| Ion-exchange chromatography | Separate charge variants and exchange counterion | DEAE or SP Sepharose, salt gradient | Additional buffer and dialysis step |
| Ultrafiltration or dialysis | Remove salts and exchange buffer | 1–3 kDa membrane | Dilution and adsorption loss |
| Lyophilization | Produce stable powder | Shelf temperature below collapse temperature | Cycle time and water content |

The order depends on the peptide. Hydrophobic sequences may need organic co-solvent throughout; basic sequences may bind strongly to C18 and require ion pairing; long sequences may need two orthogonal steps to reach 98%. Each step loses material, and the lost material is often the fraction closest to the target.

A realistic recovery from crude to purified is 40–70% for a well-behaved peptide, lower for hydrophobic, cysteine-rich, or aggregation-prone sequences. That yield loss is the main reason a 98% grade costs more than a 95% grade, and why a supplier quoting the same price for both deserves a question.

## Purity grades and where they fit

Purity grades are a commercial convention, not a universal standard. The labels below reflect common research-market usage; the specification, not the label, is what matters.

| Grade | Typical HPLC purity | Typical use | Main limitation |
| --- | --- | --- | --- |
| Crude | 30–70% | Screening, epitope mapping, process development | Unknown impurity profile; poor quantitative use |
| Desalted | 60–85% | Early assays where salts interfere | Still contains truncations and diastereomers |
| Research grade | ≥95% | General in vitro work | Close impurities may co-elute; net content varies |
| High purity | ≥98% | Assays sensitive to impurity load | Cost; still not a certified reference standard |
| Reference grade | ≥99% with orthogonal data | Method validation, quantification | Requires characterization beyond HPLC |

The grade label should be tied to a specification version. Ask for the exact limit, the method, and the acceptance criteria for each impurity category. "≥98%" without a method is a marketing claim; "≥98% by RP-HPLC, 220 nm, area normalization, single peak, maximum unspecified impurity ≤0.5%" is a specification.

## Yield, cost, and the economics of the last two percent

The cost curve is steep at the top. Moving from 95% to 98% can require a second chromatographic step, tighter fraction pooling, and a larger loss of product. That is why the price per milligram may rise by 50–150% for a two-point purity gain, and why some suppliers sell a "98%" lot that is really a 95% lot with a tighter integration threshold.

The main cost drivers are synthesis scale, crude purity, the number of purification steps, column and solvent consumption, lyophilization cycle time, and documentation. Larger scale usually lowers cost per gram, but a higher crude purity reduces the purification load and can matter more than scale. Ask for the crude HPLC before purification and the recovery after each step; those two numbers explain most of a price difference.

A buyer comparing quotes should compare cost per milligram of net peptide, not cost per vial. A 10 mg vial at 80% net content contains 8 mg of peptide; a 10 mg vial at 95% net content contains 9.5 mg. The difference is 19% more sequence for the same label weight, and it is invisible unless the certificate reports net content.

## Counterions, water, and net peptide content

Lyophilized peptide is rarely pure sequence by mass. Trifluoroacetate, acetate, chloride, or sodium counterions add mass. Water adds mass. Residual solvent adds mass. The sum of these components can be 10–30% of the vial contents.

| Component | Typical range | Method | Consequence |
| --- | --- | --- | --- |
| Water | 3–8% | Karl Fischer titration | Hydrolysis and stability risk |
| Trifluoroacetate | 5–20% by mass for basic peptides | Ion chromatography or fluorine analysis | Acidic solution, altered solubility |
| Acetate | 2–10% | Ion chromatography | Buffer compatibility |
| Residual solvent | <0.5% after drying | Headspace GC | Toxicological and assay interference |
| Net peptide | 70–90% | Amino acid analysis or nitrogen determination | Actual sequence content |

Net peptide content is the correction factor for weighing. If a certificate reports 85% net peptide, 10 mg of powder contains 8.5 mg of peptide. For qualitative work, the correction may not matter. For a concentration-response study, it changes every dilution.

The [molecular weight verification guide](/blog/peptide-molecular-weight-verification-steps) explains how to check the observed mass against the theoretical mass, including the mass shift from counterions. A peptide supplied as the TFA salt will not match the free-base mass, and that is expected, not an error.

Counterions also change dissolution behavior. A TFA salt can drive an unbuffered solution to pH 3 or below, which affects both solubility and assay compatibility. The [solubility troubleshooting guide](/blog/peptide-solubility-troubleshooting) covers the pH and co-solvent decisions that follow.

## How to verify the grade you paid for

Verification has three layers: documents, in-house checks, and independent testing.

**Documents.** Confirm that the certificate is lot-specific, names the method and wavelength, reports the main peak purity and the largest unspecified impurity, and includes water, counterion, and net peptide content. A certificate that reports only "purity: 98%" is incomplete.

**In-house checks.** Weigh the vial, reconstitute to a known volume, and measure absorbance at 280 nm if the sequence contains tryptophan or tyrosine. Compare the result with the extinction coefficient calculated from the sequence. A large shortfall can mean low net content, incomplete dissolution, or adsorption to the vial.

**Independent testing.** For a first lot or a high-value order, commission RP-HPLC and LC-MS from a third-party laboratory. Ask for the chromatogram and the mass spectrum, not just a pass/fail line. The [quality standards guide](/blog/research-peptide-quality-standards-2026-guide) lists the acceptance criteria worth specifying.

## Purchase specification checklist

A purchase order for purified peptide should state the following, even if the supplier's catalog already lists a grade:

- Sequence, modifications, and expected molecular formula.
- Counterion form (TFA, acetate, chloride, or free base).
- Purity method, wavelength, gradient, and integration criterion.
- Minimum main-peak purity and maximum largest unspecified impurity.
- Water content limit by Karl Fischer.
- Residual solvent limit if the route uses dimethylformamide or dichloromethane.
- Net peptide content and the method used to determine it.
- Appearance and fill weight per vial.
- Lot-specific certificate and raw data availability.
- Retention sample quantity and storage condition.

For a repeat order, add a batch-to-batch comparison: main peak purity within 1%, impurity profile visually comparable, and net peptide content within 5% of the qualified lot. The [high-purity bulk sourcing guide](/blog/high-purity-peptides-bulk-order-a-b2b-guide-to-direct-sourcing-in-2026) covers scale-up and sampling.

The [reseller comparison](/blog/direct-sourcing-vs-peptide-resellers) is useful when the same grade is offered through several channels at different prices.

## When crude is the better buy

Crude peptide is a reasonable choice when the assay does not depend on absolute purity: initial binding screens, epitope mapping with overlapping sequences, immunization antigen preparation, or process development where the target is recovery rather than final specification. It is a poor choice for quantitative LC-MS, receptor pharmacology with a narrow window, or any study where a 5% impurity could produce the observed effect.

The decision rule is simple: if the impurity could plausibly cause the result, buy purified and characterize the lot. If the impurity cannot plausibly cause the result and the readout is qualitative, crude can save money without weakening the study.

## The Author's Take

**Position:** The useful distinction is not crude versus purified. It is specified versus unspecified. A 95% lot with a complete impurity profile, water content, counterion data, and net peptide content is a better research material than a "98%" lot with a single HPLC percentage and no method details.

**Reasoning:** Purity by area normalization is a ratio, and the denominator is whatever the method happens to integrate. I have seen the same lot pass as 97% on one gradient and 93% on another. Buyers who ask for the chromatogram, the mass spectrum, and the net peptide content get a material they can weigh and defend. Buyers who buy the number get a label. The price premium for 98% is real, but it is only worth paying when the specification explains what the extra two percent excludes.

**Disclosure:** Peptides of China sells research peptides. This article describes analytical interpretation and procurement specifications, not an effects claim. Products are supplied for research use only and are not for human or veterinary use.

## Sources

- European Medicines Agency. *ICH Q6B: Specifications — Test Procedures and Acceptance Criteria for Biotechnological/Biological Products.* https://database.ich.org/sites/default/files/Q6B%20Guideline.pdf
- European Medicines Agency. *ICH Q3A(R2): Impurities in New Drug Substances.* https://www.ema.europa.eu/en/scientific-guidelines/ich-q3a-r2-impurities-new-drug-substances
- European Medicines Agency. *ICH Q2(R2): Validation of Analytical Procedures.* https://www.ema.europa.eu/en/scientific-guidelines/ich-q2r2-validation-analytical-procedures
- United States Pharmacopeia. *USP General Chapter <621> Chromatography.* https://www.usp.org/usp-nf
- Bruckdorfer T, Marder O, Albericio F. *From production of peptides in milligram amounts for research to multi-tons quantities for drugs of the future.* Current Pharmaceutical Biotechnology 5(1): 29–43 (2004). https://doi.org/10.2174/1389201043489620
- Rivier J, McClintock R, Galyean R, Anderson H. *Reversed-phase high-performance liquid chromatography: preparative purification of synthetic peptides.* Journal of Chromatography A 288: 303–328 (1984). https://doi.org/10.1016/S0021-9673%2801%2993709-4
- *Towards a consensus for the analysis and exchange of TFA as a counterion in synthetic peptides and its influence on membrane permeation.* Pharmaceuticals 18(8): 1163 (2025). https://doi.org/10.3390/ph18081163
- *Advances in therapeutic peptides separation and purification.* Separations 11(8): 233 (2024). https://doi.org/10.3390/separations11080233
