---
title: "Why Purity and Concentration Tests Are Not Enough"
slug: "why-purity-and-concentration-tests-are-not-enough"
description: "HPLC area percent and mg per vial leave gaps: water, counterions, residual solvents, elemental impurities, endotoxin, and identity each need separate evidence."
---

Purity and concentration are the two numbers most often used to describe a peptide lot. Neither is a quality specification. Purity describes the share of chromatographic signal assigned to the main peak under one method. Concentration describes how much material is present in the vial, often inferred from fill weight or ultraviolet absorbance. A lot can pass both tests and still fail identity, content, safety, or stability.

The gap is structural, not a matter of sloppy testing. Each test answers a narrow question, and the questions that decide whether a lot is fit for a study are broader. This article separates the numbers, shows what each one leaves out, and sets out the additional evidence a buyer should request before treating a certificate of analysis as a release decision.

## The three numbers buyers conflate

Purity, concentration, and content are related but not interchangeable. The table below uses the definitions a laboratory should state explicitly.

| Measurement | What it compares | Typical unit | What it can miss |
| --- | --- | --- | --- |
| Purity by HPLC | Main-peak area versus total integrated peak area | % area | Water, salts, solvents, non-chromophoric impurities, co-eluting species |
| Concentration | Material dissolved or filled per volume or vial | mg/mL or mg/vial | Whether the material is peptide, salt, water, or excipient |
| Net peptide content | Peptide mass versus total powder mass | % w/w | Identity and impurity profile |
| Assay | Measured peptide versus label claim | % of label | Whether the method is stability-indicating |

A certificate that reports "purity 99%" and "10 mg/vial" has not told you that the vial contains 9.9 mg of the intended peptide. It has told you that the main chromatographic peak accounts for 99% of the integrated area, and that some measurement of material content is 10 mg. The basis for the second number is the part that often goes unstated.

The distinction matters most when a study is designed around a nominal amount. If a protocol assumes 10 mg of peptide and the lot contains 7.5 mg of peptide plus 2.5 mg of water and counterion, the molar amount in solution is 25% lower than planned. That is a formulation calculation error, not a purity failure, and it will not be visible in an HPLC percentage.

## What HPLC purity actually measures

Reversed-phase HPLC separates molecules by hydrophobicity. The detector records absorbance, usually at 220 nm for the peptide backbone or 280 nm for aromatic residues. Purity by area normalization divides the main-peak area by the sum of all integrated peak areas.

Four conditions determine the result:

- **The column and gradient determine what is resolved.** A shallow gradient can separate deamidated and oxidized forms that a fast gradient merges into one peak.
- **The wavelength determines what is detected.** At 220 nm, the peptide bond absorbs; at 280 nm, tryptophan and tyrosine dominate. An impurity without those residues may be invisible at 280 nm.
- **The integration threshold determines what is counted.** A method that ignores peaks below 0.1% will report a higher purity than one that reports down to 0.05%.
- **The sample load determines whether impurities are saturated.** Overloading the column can distort the main peak and compress nearby impurities into the baseline.

None of these conditions is hidden from a competent laboratory. The problem is that a catalog claim often reports only the final percentage. The [HPLC versus LC-MS comparison](/blog/hplc-vs-lc-ms-peptides) explains why a second method is needed for identity, and the [COA reading guide](/blog/how-to-read-a-peptide-coa-a-researchers-guide-to-hplc-and-ms-reports) shows which method details should appear on the certificate.

A useful check is to ask for the chromatogram with the integration table. The table should list each integrated peak, its retention time, its area, and its area percent. If the certificate shows only the main peak, the buyer cannot tell whether the method resolved anything else.

## What "10 mg per vial" actually means

Vial fill is a manufacturer's statement about the amount of material placed in the container. It is not a statement about peptide content. A 10 mg fill can mean 10 mg of total powder, 10 mg of as-is material, or 10 mg of net peptide. Those are different quantities, and the difference can be 20–30% for a lyophilized salt.

Net peptide content is usually determined by one of three approaches:

1. **Nitrogen determination** by elemental analysis or Kjeldahl. The result is converted to peptide mass using the nitrogen content of the sequence.
2. **Amino acid analysis** after hydrolysis. The measured amino acid recoveries are compared with the theoretical composition.
3. **Mass balance** from the measured water, counterion, residual solvent, and inorganic residue, subtracted from 100%.

Each method has assumptions. Nitrogen determination can overestimate peptide if residual ammonium salts are present. Amino acid analysis can lose labile residues during hydrolysis. Mass balance depends on measuring every component, including the ones that are not routinely tested.

A concentration stated in mg/mL has a separate problem. Ultraviolet absorbance at 280 nm depends on the extinction coefficient, which depends on the number of tryptophan and tyrosine residues and on their environment. For a peptide with a lipid chain, the calculated coefficient may not match the behavior of the folded or aggregated form. The report should state the coefficient, the path length, the blank, and whether the measurement was made on a clarified solution.

For semaglutide, the sequence contains tryptophan and tyrosine, so A280 is usable. The coefficient should still be calculated from the sequence and stated on the method. A concentration derived from "vial weight minus tare" is a fill-weight estimate, not an assay.

## The hidden mass: water, counterions, residual solvents

A lyophilized peptide is not pure peptide. It contains water bound to the cake, counterions left from purification, residual solvents from synthesis and chromatography, and inorganic residue from buffers and resins. Those components are part of the vial and should be part of the specification.

| Component | Typical method | Example buyer limit | Why it matters |
| --- | --- | --- | --- |
| Water | Karl Fischer titration, USP <921> | ≤5.0% w/w | Water reduces net peptide content and can drive hydrolysis |
| Trifluoroacetate | Ion chromatography, NMR, or titration | ≤1.0% w/w | Residual TFA affects mass balance and cell-based assays |
| Acetate | Ion chromatography or titration | Report as found | Acetate salts have different mass and solubility |
| Residual solvents | Gas chromatography, ICH Q3C | Class 2 limits by PDE | Acetonitrile, methanol, and dichloromethane are common |
| Inorganic residue | Residue on ignition or ICP-MS | Report as found | Buffer salts and metal residues can interfere with assays |
| Elemental impurities | ICP-MS, ICH Q3D | Risk-based PDE | Catalytic metals can remain from coupling or hydrogenation |

The limits in the table are examples of a buyer specification, not universal pharmacopoeial limits. The method and the limit should be stated together. A water result without a method is difficult to compare across laboratories; a Karl Fischer result with coulometric detection is more sensitive than a volumetric titration and may report a different value at the same moisture level.

Mass balance is the arithmetic check:

**Peptide content + water + counterion + residual solvents + inorganic residue + impurities ≈ 100%.**

If the sum is 105%, one of the numbers is on a different basis. If the sum is 85%, something was not measured. Neither result automatically means the lot is bad, but both require an explanation before the certificate can be used for a release decision.

Residual solvents are governed by ICH Q3C, which sets permitted daily exposures by class. Acetonitrile, methanol, and dichloromethane are Class 2 solvents with PDEs of 4.1 mg/day, 30.0 mg/day, and 6.0 mg/day respectively. Elemental impurities are governed by ICH Q3D, which sets oral PDEs of 5 µg/day for cadmium and lead, 15 µg/day for arsenic, and 30 µg/day for mercury; parenteral limits differ. A research peptide is not a finished drug, but the same analytical logic applies: if the synthetic route uses a metal catalyst or a chlorinated solvent, the specification should say so and test for it.

## Impurity identity is a separate question

Area percent tells you how much of the integrated signal is not the main peak. It does not tell you what those peaks are. Identification requires a second technique, usually LC-MS/MS, high-resolution mass spectrometry, NMR, or comparison with a reference standard.

For peptide lots, the impurities that matter tend to fall into five groups:

- **Truncated sequences** from incomplete coupling or premature cleavage.
- **Deamidated forms** with a mass shift of about +0.984 Da.
- **Oxidized forms** with a mass shift of about +15.995 Da.
- **Diastereomers** from epimerization during coupling or cleavage.
- **Modified side chains**, including acyl migration or linker truncation in lipidated peptides.

A specification can set limits for specified impurities and a general limit for unspecified impurities. It should also state the reporting threshold and the method used to identify peaks above that threshold. The ICH Q3A/Q3B framework uses reporting, identification, and qualification thresholds rather than a single impurity limit; the exact values depend on the product and the daily dose. Research-grade material is not automatically exempt from the logic, especially when the lot is used in a study that will be repeated.

The [research peptide quality standards guide](/blog/research-peptide-quality-standards-2026-guide) sets out a fuller attribute list. The practical test is whether the certificate identifies the specified degradants and gives numeric results for each, or whether it reports only "total impurities ≤2.0%."

## Safety attributes that purity cannot cover

Purity is a separation result. It says nothing about biological or chemical safety attributes that are measured by separate methods.

| Attribute | Method | Why a purity result cannot substitute |
| --- | --- | --- |
| Bacterial endotoxin | LAL or rFC, USP <85> | Endotoxin is not detected by HPLC; a sterile-looking powder can carry pyrogens |
| Sterility | USP <71> membrane filtration or direct inoculation | Purity does not detect viable organisms |
| Bioburden | USP <61>/<62> | A non-sterile lot can have a microbial count within or above limits |
| Elemental impurities | ICP-MS, ICH Q3D | Metals may be invisible at 220 nm and can catalyze degradation |
| Residual solvents | GC, ICH Q3C | Solvents are not part of the chromatographic peak area |
| Particulates | USP <788> or <787> | Visible and subvisible particles are a container-product attribute |
| Container closure | USP <1207> | Leachables and container integrity are not tested by HPLC |

Endotoxin is the clearest example. A lot can be 99% pure by HPLC and still carry endotoxin above a laboratory's acceptance limit. The [endotoxin testing guide](/blog/endotoxin-testing-peptide-manufacturing) explains the LAL and rFC methods, the EU/mL and EU/mg calculations, and the COA fields that should accompany a claim. Sterility is a separate method with its own sample size and incubation conditions; the [USP <71> protocol guide](/blog/sterility-testing-for-research-peptides-a-protocol-guide) covers the practical details.

A supplier may reasonably not test every attribute on every lot. The buyer's job is to know which attributes are claimed, which are tested, and which are assumed. "Not tested" is a valid answer if it is disclosed. "Endotoxin free" without a method, limit, or result is not a test result.

## Stability and container closure

Release testing describes the lot at the time of testing. Stability describes how the attributes change under defined storage conditions. A lot that passes release can fail after transit, storage, or a freeze-thaw cycle.

ICH Q1A(R2) sets out the standard stability design: long-term conditions, accelerated conditions, and a testing frequency that supports the proposed shelf life. For a lyophilized peptide, a common long-term condition is 5 ± 3 °C, with accelerated testing at 25 °C/60% RH for six months. A laboratory that intends to store material for more than a year should ask for the supplier's stability data, not just the release date.

Three container-product interactions deserve attention:

- **Moisture ingress.** A lyophilized cake can absorb water through a poor seal or a permeable stopper. Karl Fischer results from release may not reflect the vial after storage.
- **Adsorption.** Peptides can adsorb to glass, to filters, and to tubing. A concentration assay performed on a fresh solution may not represent a diluted working solution.
- **Leachables.** Container closure systems can release compounds into the formulation. USP <1207> provides a risk-based framework for package integrity and leachables.

The [lyophilized peptide stability guide](/blog/peptide-stability-why-lyophilized-peptides-are-far-more-stable-than-you-think) explains why a dry cake is not automatically stable, and the [TFA removal guide](/blog/tfa-removal-peptides) covers a counterion issue that can affect both mass balance and assay performance.

## A specification that closes the gaps

A buyer-side specification does not need to reproduce a pharmacopoeial monograph. It needs to state the attributes, methods, limits, and evidence that will be used to accept or reject a lot. A workable structure has ten lines:

1. **Identity.** Intact mass by LC-MS, sequence coverage by MS/MS, and chromatographic comparison with a reference standard.
2. **Purity.** RP-HPLC method with column, mobile phase, gradient, wavelength, flow, temperature, injection load, and integration threshold.
3. **Impurity profile.** Specified degradants with individual limits; unspecified impurities with a general limit and a reporting threshold.
4. **Net peptide content.** Method and result, with water and counterion reported separately.
5. **Water.** Karl Fischer, with a stated limit.
6. **Counterion.** Identity and content, with a stated limit.
7. **Residual solvents.** GC method and results against ICH Q3C limits where relevant.
8. **Elemental impurities.** ICP-MS results against a risk-based limit where the route uses metal catalysts.
9. **Safety attributes.** Endotoxin and sterility only if claimed; otherwise state "not tested."
10. **Batch records and stability.** Lot traceability, release date, specification version, and storage conditions.

The specification should also define the sampling plan and the acceptance rule. A common mistake is to test one vial from a ten-vial kit and treat the result as representative of every vial. That is reasonable for a homogeneous fill, but it is an assumption that should be stated. The [quality assurance process guide](/blog/peptide-quality-assurance-process-a-researchers-guide-to-sourcing-integrity) describes how incoming inspection, deviation handling, and supplier qualification fit together.

## The Author's Take

**Position:** Purity and concentration are release tests, not a quality system. The three questions that predict whether a peptide lot is usable are: what identity evidence exists, what the content number is based on, and which attributes were not tested. A certificate that answers only the first two numbers is a starting point for a conversation, not a release decision.

**Reasoning:** The failures I see discussed most often are not "the peptide was 80% pure." They are "the vial contained less peptide than expected," "the endotoxin result was never measured," and "the same lot number appeared on a certificate from a different batch." Those failures survive a purity test because the test was never designed to catch them. A buyer who asks for the chromatogram, the mass spectrum, the water result, the counterion result, and the batch record extract will get a slower answer from some suppliers. That slower answer is the point. It separates a supplier that has the data from one that has a template.

**Disclosure:** Peptides of China sells research peptides. This article describes analytical and procurement judgment, not an effects claim. Products are supplied for research use only and are not for human or veterinary use.

## Sources

1. ICH. *Q6B: Specifications — Test Procedures and Acceptance Criteria for Biotechnological/Biological Products.* https://database.ich.org/sites/default/files/Q6B%20Guideline.pdf
2. ICH. *Q2(R2): Validation of Analytical Procedures.* 2023. https://database.ich.org/sites/default/files/ICH_Q2%28R2%29_Guideline_2023_1130.pdf
3. ICH. *Quality Guidelines: Q3A, Q3B, Q3C(R8), and Q3D(R2).* https://www.ich.org/page/quality-guidelines
4. U.S. Food and Drug Administration. *Pyrogen and Endotoxins Testing: Questions and Answers.* 2012. https://www.fda.gov/regulatory-information/search-fda-guidance-documents/pyrogen-and-endotoxins-testing-questions-and-answers
5. U.S. Food and Drug Administration. *Analytical Procedures and Methods Validation for Drugs and Biologics — Guidance for Industry.* 2015. https://www.fda.gov/regulatory-information/search-fda-guidance-documents/analytical-procedures-and-methods-validation-drugs-and-biologics
6. USP. *<921> Water Determination, <85> Bacterial Endotoxins Test, <71> Sterility Tests, and <788> Particulate Matter in Injections.* https://www.usp.org/usp-nf
7. D'Hondt M, Bracke N, Taevernier L, et al. Related impurities in peptide medicines. *Journal of Pharmaceutical and Biomedical Analysis.* 2014;101:2–30. https://doi.org/10.1016/j.jpba.2014.06.012
8. El-Faham A, Albericio F. Peptide coupling reagents, more than a letter soup. *Chemical Reviews.* 2011;111(11):6557–6602. https://doi.org/10.1021/cr100048w
9. Eurachem. *The Fitness for Purpose of Analytical Methods: A Laboratory Guide to Method Validation and Related Topics.* 2014. https://www.eurachem.org/index.php/publications/guides/mv
