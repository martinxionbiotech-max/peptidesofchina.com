---
title: "Peptide Synthesis: Methods, Steps, and Buyer Checks"
slug: "peptide-synthesis-explained-methods-and-process-guide"
description: "How SPPS, solution-phase, and recombinant routes differ, which process steps create the impurities on a COA, and the questions that separate facilities."
author: "POC Tech Team"
---
**Nearly every research peptide on the market is made by solid-phase synthesis, and the process itself explains most of what appears on the certificate of analysis.** A 20-residue chain built one amino acid at a time accumulates truncated sequences, deleted residues, and chemically modified side products. The purification step removes most of them. What remains, and how much remains, depends on choices made at the resin, the coupling step, and the cleavage cocktail.

Buyers do not need to run a synthesis to read its fingerprints. A COA that shows a deletion sequence at 0.8%, a mass adduct, or a broad main peak is describing a process, not just a batch. This guide covers the three production routes, the steps inside solid-phase synthesis, the chemistry choices that leave traces, and the questions worth asking a facility before an order.

## Three Routes, Three Different Products

Peptide production is not one method. The route determines the length that is practical, the scale that is economic, and the impurity signature a buyer should expect.

**Solid-phase peptide synthesis (SPPS).** The chain is built on an insoluble resin, one residue at a time, with washing between steps. It dominates research supply because it handles 5–50 residues well, scales from milligrams to kilograms, and can incorporate non-natural residues. Its weakness is length: each coupling has a yield below 100%, and the losses compound.

**Solution-phase synthesis.** Fragments are made separately and coupled in solution. It suits short peptides and industrial quantities where purification at each step is affordable, and it avoids the large resin and cleavage reagent volumes. It is rarely the cheapest route below kilogram scale.

**Recombinant expression.** A host organism produces the peptide, which is then harvested and purified. It suits longer chains and avoids organic synthesis entirely, but it brings host-cell proteins, endotoxin risk, and post-translational heterogeneity that a synthetic route does not have. For a 15-residue research peptide, recombinant production is usually the wrong tool.

| Route | Practical length | Typical scale | Main cost driver | Impurity signature |
|---|---|---|---|---|
| SPPS | 5–50 residues | mg to kg | Resin, amino acids, purification | Deletions, truncations, aspartimide |
| Solution-phase | 2–15 residues per fragment | g to tonnes | Steps, solvents, isolation | Incomplete coupling, epimerization |
| Recombinant | 20–100+ residues | kg and up | Fermentation, chromatography | Host protein, endotoxin, variants |

The [custom sourcing guide](/blog/custom-peptide-sourcing-for-product-development-in-2026/) covers how route choice flows into a quotation, and the [manufacturing partners page](/manufacturing-partners/) describes the facility model we work with.

## Solid-Phase Synthesis, Step by Step

The cycle repeats for each residue. The sequence below reflects standard Fmoc chemistry, the dominant approach for research peptides.

**1. Resin preparation.** The first amino acid is loaded onto a resin, typically a polystyrene or PEG-based support. Loading is expressed in millimoles per gram; 0.3–0.8 mmol/g is a common range for research-scale resins. Loading determines the maximum yield per batch and affects steric crowding during chain growth.

**2. Deprotection.** The Fmoc group on the growing chain's N-terminus is removed with 20% piperidine in dimethylformamide, usually a short pre-soak followed by a 15-minute treatment. Incomplete deprotection leaves chains that cannot accept the next residue, which become deletion sequences one residue shorter than the target.

**3. Coupling.** The activated amino acid is added, commonly at four-fold molar excess with a uronium or phosphonium reagent and a base. Coupling times of 30–60 minutes are typical; difficult sequences need longer or a double coupling. Incomplete coupling produces a truncation at that position.

**4. Washing.** Excess reagent and by-products are removed. Thorough washing is unglamorous and decisive; residual piperidine or reagent carries into the next coupling and lowers its efficiency.

**5. Monitoring.** The Kaiser test (ninhydrin) detects free amines and turns blue when coupling is incomplete. It is qualitative and does not work for proline or protected cysteine, so facilities supplement it with conductimetric or UV monitoring.

**6. Repetition.** Steps 2–5 run for each residue. A 20-mer goes through the cycle twenty times, and the accumulated yield is the product of the individual step yields.

The arithmetic is the part buyers underestimate. At 99.0% average coupling efficiency, a 20-mer reaches full length at 0.99^20, about 81.8%. At 99.5% the figure is 90.5%; at 99.8% it is 96.1%. The remaining material is a distribution of sequences missing one or more residues, many of which differ from the target by a single amino acid and therefore elute close to it on a reversed-phase column.

## The Chemistry Choices That Leave Traces

Four chemistry decisions show up in the analytical file.

**Fmoc versus Boc.** Fmoc deprotection uses piperidine, a milder base; Boc deprotection uses trifluoroacetic acid, which requires acid-stable linkages and harsher final cleavage. Fmoc chemistry is standard for research peptides because it avoids repeated acid treatment, but it introduces dibenzofulvene and piperidine adducts that must be washed out.

**Coupling reagents.** HBTU and HATU activate the carboxyl group through a uronium intermediate. They are fast and efficient, and they can racemize sensitive residues, particularly cysteine and histidine. DIC with Oxyma or HOBt is a gentler alternative. A facility that uses one reagent for every sequence is optimizing for speed, not for the hard positions.

**Side-chain protection.** Arginine is protected with Pbf or Pmc groups, which require higher acid strength to remove. Serine and threonine use tert-butyl ethers. Cysteine needs a protecting group matched to the disulfide strategy, such as acetamidomethyl (Acm) or tert-butylthio. A mismatch here produces a chain that cleaves but will not fold correctly.

**Difficult sequences.** Beta-branched residues (Val, Ile, Thr), consecutive hydrophobic stretches, and sequences with a propensity to aggregate couple poorly. Facilities address these with pseudoproline dipeptides, microwave irradiation, or higher reaction temperature. Each intervention is a process detail worth asking about, because it changes the impurity profile.

| Impurity | Mass shift | Usual cause | Evidence on the COA |
|---|---|---|---|
| Deletion sequence | − residue mass | Incomplete coupling or deprotection | Extra peak close to main peak |
| Truncation | Variable | Failed coupling at one position | Cluster of earlier-eluting peaks |
| Aspartimide | −18 Da | Asp-Gly motif during cleavage | Mass adduct plus isoAsp shoulder |
| Deamidation | +0.984 Da | Asn/Gln exposure to base or heat | +1 Da satellite in MS |
| Methionine oxidation | +15.995 Da | Air or peroxide exposure | +16 Da species |
| N-terminal acetylation | +42.011 Da | Acetic acid or capping side reaction | +42 Da species |
| Diastereomer | 0 Da (isobaric) | Racemization during coupling | Split or broadened main peak |

The [synthesis failures guide](/blog/common-peptide-synthesis-failures-a-practical-lab-guide/) explains how each of these is diagnosed, and the [HPLC versus LC-MS comparison](/blog/hplc-vs-lc-ms-peptides/) covers the methods that separate them.

## Cleavage, Purification, and Counterion Exchange

Once the chain is complete, it is cut from the resin. The standard cocktail is 95% trifluoroacetic acid with 2.5% triisopropylsilane and 2.5% water, run for two to three hours at room temperature. Triisopropylsilane scavenges carbocations released from side-chain protecting groups; water helps cleave the peptide from the linker. Skipping the scavenger produces alkylated tryptophan and methionine.

Crude peptide is then precipitated, typically with cold ether, and purified by reversed-phase HPLC. A C18 column with a water/acetonitrile gradient in 0.1% trifluoroacetic acid separates the target from deletions and modified variants. The operator pools fractions according to a defined rule — often a minimum purity threshold per fraction rather than a fixed percentage of the peak.

Purification recovery for a difficult sequence commonly falls between 40% and 70% of the crude mass. The pool is then concentrated and may undergo counterion exchange if the specification calls for acetate rather than trifluoroacetate. Ion exchange or repeated lyophilization from acetic acid reduces residual TFA, which matters for assays where the counterion interferes. The [TFA removal note](/blog/tfa-removal-peptides/) covers the options.

Trifluoroacetate content also explains a mass-balance surprise: a vial labeled 10 mg may contain 7–8 mg of peptide, with the remainder being counterion and water. Net peptide content is a separate specification field, not a rounding detail.

## Lyophilization and the Final Form

Most research peptides ship as a lyophilized cake. Freeze-drying removes water while preserving the solid form, and the cycle is a process parameter that affects both appearance and stability.

The product is frozen below its collapse temperature, then primary drying removes ice by sublimation under vacuum, then secondary drying removes bound water. A cycle typically runs 24–72 hours depending on fill volume and formulation. Incomplete primary drying leaves a cake that collapses or shrinks; incomplete secondary drying leaves water above specification, which accelerates hydrolysis and deamidation on storage.

Formulation matters too. Mannitol or sucrose can be added as a bulking agent or cryoprotectant, and the ratio affects cake structure and reconstitution. A cake that looks collapsed is not automatically degraded, but it is a signal to check water content and appearance against the release specification.

The [lyophilization and reconstitution guide](/blog/peptide-lyophilization-reconstitution-guide-for-researchers/) covers handling after receipt. Storage at −20 °C, protected from light and moisture, is the common recommendation for lyophilized research peptides; the retest date assumes that condition.

## Where Batches Actually Fail

Failures cluster in predictable places.

**The last five residues.** Coupling efficiency drops as the chain lengthens and aggregation increases. A batch that passes at residue 15 can fail at residue 20.

**Aspartimide hot spots.** Asp-Gly and Asn-Gly motifs form a cyclic imide under basic deprotection or acidic cleavage. The ring opens to aspartate or isoaspartate, which are isobaric and often co-elute. A COA that reports a single sharp peak for a peptide with an Asp-Gly motif is not necessarily wrong, but the method should be able to resolve the isoform.

**Cysteine oxidation.** Free cysteine oxidizes to cystine, forming dimers and mixed disulfides. A peptide with an unpaired cysteine needs a reducing agent or a protecting strategy, and the COA should show the monomer as the main peak.

**Cleavage damage.** Over-long cleavage or a hot exotherm alkylates tryptophan and methionine. The mass shifts are diagnostic: +15.995 Da for oxidation, +42.011 Da for acetylation.

**Purification overloading.** Loading a preparative column beyond capacity produces overlapping fractions; the operator then chooses between yield and purity. The analytical chromatogram may look clean while the preparative trace shows a widened cut.

## Reading a Synthesis-Related COA

A COA is a summary; the synthesis history sits in the batch record. Still, four fields tell a buyer whether the batch was made with control.

**Purity with method details.** Look for column dimensions, gradient, wavelength, and reporting threshold. A purity number without these cannot be compared across suppliers.

**Impurity table.** Individual peaks above the reporting threshold, with retention times. A batch with one 1.5% impurity is a different risk from one with fifteen 0.1% peaks, even at the same total purity.

**Mass spectrum.** Charge states, deconvoluted mass, and the mass error. A spectrum with a single charge state and no annotation is a picture, not data.

**Counterion and water.** Ion chromatography or titration for trifluoroacetate, Karl Fischer for water, and a net peptide content figure. These three explain the difference between fill mass and peptide mass.

The [COA reading guide](/blog/how-to-read-a-peptide-coa-a-researchers-guide-to-hplc-and-ms-reports/) expands each field, and the [crude versus purified note](/blog/what-is-crude-vs-purified-peptide/) explains what changes between grades.

## What to Ask a Facility Before Ordering

Five questions separate a facility that controls its process from one that runs a recipe.

1. **What is your average coupling efficiency, and how is it measured?** A facility that monitors with Kaiser tests and conductivity can answer with a number and a method.
2. **How do you handle difficult sequences?** Look for pseudoprolines, double coupling, or microwave assistance, not assurances.
3. **What is your purification loading ratio?** Milligrams of crude per gram of stationary phase; an evasive answer suggests the cut is adjusted to hit a purity target.
4. **Which changes trigger a new batch record?** Resin lot, reagent lot, and column lot should be traceable.
5. **Can you provide the preparative chromatogram?** The analytical trace shows the result; the preparative trace shows the decision.

The [validated facility guide](/blog/why-validated-synthesis-facilities-matter-brands/) covers site qualification, and ICH Q7 provides the reference framework for batch records and change control even where formal GMP status does not apply.

## The Author's Take

**Position.** A buyer can judge a synthesis facility by two artifacts: the impurity table and the preparative chromatogram. Marketing pages describe capability; those two documents describe what the facility actually did with a difficult sequence.

**Reasoning.** Every synthesis route produces a predictable family of impurities, and the way a supplier reports them reveals its analytical discipline. A COA that lists only total purity has either not integrated the impurity peaks or chosen not to show them. A preparative trace that shows a narrow heart cut and a large discarded fraction indicates a facility protecting the specification; a trace with a wide cut and no discarded fraction indicates a facility protecting yield. Both are commercial choices, but only one is compatible with a 98% release criterion on a difficult sequence. The coupling arithmetic — 81.8% full-length at 99.0% efficiency for a 20-mer — is why the choice matters more as chains get longer.

**Disclosure.** Peptides of China sells research peptides manufactured by partner facilities. This article describes synthesis chemistry and sourcing judgment; it is not an effects claim, a dosing guide, or medical advice. Products referenced on this site are supplied for laboratory research use only. Process details vary by product and facility, and analytical documentation should be requested for the specific batch.

## Sources

- Merrifield, R. B. Solid Phase Peptide Synthesis. I. The Synthesis of a Tetrapeptide. *Journal of the American Chemical Society* (1963). [doi:10.1021/ja00897a025](https://doi.org/10.1021/ja00897a025)
- Fields, G. B. & Noble, R. L. Solid phase peptide synthesis utilizing 9-fluorenylmethoxycarbonyl amino acids. *International Journal of Peptide and Protein Research* (1990). [doi:10.1111/j.1399-3011.1990.tb00939.x](https://doi.org/10.1111/j.1399-3011.1990.tb00939.x)
- Coin, I., Beyermann, M. & Bienert, M. Solid-phase peptide synthesis: from standard procedures to the synthesis of difficult sequences. *Nature Protocols* (2007). [doi:10.1038/nprot.2007.454](https://doi.org/10.1038/nprot.2007.454)
- Kaiser, E. et al. Color test for detection of free terminal amino groups in the solid-phase synthesis of peptides. *Analytical Biochemistry* (1970). [doi:10.1016/0003-2697(70)90146-6](https://doi.org/10.1016/0003-2697%2870%2990146-6)
- Rivier, J. et al. Reversed-phase high-performance liquid chromatography: preparative purification of synthetic peptides. *Journal of Chromatography A* (1984). [doi:10.1016/S0021-9673(01)93709-4](https://doi.org/10.1016/S0021-9673%2801%2993709-4)
- ICH Q6B: Specifications — Test Procedures and Acceptance Criteria for Biotechnological/Biological Products. [database.ich.org](https://database.ich.org/sites/default/files/Q6B%20Guideline.pdf)
- ICH Q7: Good Manufacturing Practice Guide for Active Pharmaceutical Ingredients. [database.ich.org](https://database.ich.org/sites/default/files/Q7%20Guideline.pdf)
