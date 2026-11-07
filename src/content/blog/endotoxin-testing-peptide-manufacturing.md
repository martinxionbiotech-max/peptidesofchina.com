---
title: "Endotoxin Testing for Peptides: LAL, rFC, Limits, and COA Review"
slug: "endotoxin-testing-peptide-manufacturing"
description: "How LAL and rFC endotoxin assays work, how to set EU/mL and EU/mg limits, and which method details a peptide COA must show."
---
**Endotoxin testing for a peptide batch comes down to three decisions: which assay format, which limit, and which dilution.** The assay is almost always a Limulus amebocyte lysate (LAL) method or its recombinant Factor C (rFC) equivalent. The limit is expressed in EU/mL or EU/mg and is derived from the intended exposure route or an internal research specification. The dilution is set by the maximum valid dilution (MVD), which determines how far the sample can be diluted before the assay's sensitivity is exhausted.

A certificate of analysis that says "LAL: pass" without a method, a limit, a numeric result, and spike recovery evidence has not reported an endotoxin result. It has reported a conclusion. This guide covers how the assay generates a number, where the number can mislead, and what a reviewer should demand before accepting a batch.

For the wider documentation set, the [COA reading guide](/blog/how-to-read-a-peptide-coa-a-researchers-guide-to-hplc-and-ms-reports/) covers report structure and batch linkage. This page stays on endotoxin chemistry and release logic.

## What Endotoxins Are, and Why Sterility Does Not Cover Them

Endotoxins are lipopolysaccharides (LPS) from the outer membrane of gram-negative bacteria. The molecule has three regions: Lipid A, which anchors it in the membrane and drives immune recognition; a core oligosaccharide; and a variable O-antigen chain. Lipid A is the conserved part, which is why one assay chemistry can detect LPS from many gram-negative species.

The practical problem is persistence. Autoclaving kills bacteria but does not destroy LPS. A 0.22 µm filter removes bacterial cells but does not reliably remove endotoxin, because LPS forms micelles and aggregates small enough to pass. A batch can be sterile by compendial sterility testing and still carry endotoxin from organisms killed upstream. Sterility and endotoxin are separate release tests, and [sterility testing](/blog/sterility-testing-peptide-manufacturing/) does not substitute for endotoxin testing.

Endotoxin units are defined against an international reference standard. As a rough conversion, 1 EU corresponds to about 0.1 ng of reference-standard LPS, though the exact mass equivalence depends on the standard lot and the LPS source. Reports should stay in EU rather than converting to mass, because the unit is what the assay actually measures.

## How the LAL Cascade Produces a Number

LAL reagent is a lysate of horseshoe crab amebocytes. Endotoxin activates Factor C, which activates Factor B, which activates the proclotting enzyme. That enzyme cleaves coagulogen into coagulin, producing a clot. In quantitative formats, the same enzyme cleaves a chromogenic or fluorogenic substrate, and the rate of signal generation is proportional to endotoxin concentration.

The assay is a kinetic cascade, not a chemical titration. That matters for three reasons. First, the reagent is biological, so each lot must be qualified against a reference standard before use. Second, the cascade is sensitive to temperature; USP &lt;85&gt; specifies incubation at 37 ± 1 °C. Third, the reaction is sensitive to pH; the compendial range is pH 6.0–8.0, and a peptide solution outside that window needs buffering before assay.

Gel-clot LAL is the oldest format. It is a limit test: the technician observes clot formation at a stated sensitivity, commonly λ = 0.03 EU/mL, and reports pass or fail at that threshold. It is inexpensive and reliable in the hands of a trained operator, but it does not produce a numerical concentration. Kinetic turbidimetric and kinetic chromogenic methods measure the rate of change and compare it to a standard curve, which is why they are preferred when a COA needs a number rather than a verdict.

## Choosing a Method: Gel-Clot, Turbidimetric, Chromogenic, or rFC

| Format | Readout | Typical working range | Quantitative | Beta-glucan interference | Best fit |
|---|---|---|---|---|---|
| Gel-clot LAL | Clot at endpoint | 0.03–0.25 EU/mL | No | Possible via Factor G | Pass/fail screening, low sample volume |
| Kinetic turbidimetric LAL | Turbidity change over time | 0.001–10 EU/mL | Yes | Possible via Factor G | Routine QC with a plate reader |
| Kinetic chromogenic LAL | Color development over time | 0.005–5 EU/mL | Yes | Possible via Factor G | Release testing with numeric results |
| Recombinant Factor C (rFC) | Fluorescence from synthetic substrate | 0.005–5 EU/mL | Yes | No Factor G pathway | Specific endotoxin measurement, reagent consistency |

The ranges above are method-dependent and should be taken from the reagent manufacturer's validation, not treated as universal. What matters is that the chosen range brackets the MVD-adjusted sample concentration. A method with a lower limit of 0.005 EU/mL is not more sensitive than one at 0.03 EU/mL if the sample must be diluted 100-fold to overcome interference; the effective sensitivity after dilution is what counts.

rFC uses a recombinant form of Factor C and does not require horseshoe crab blood. It avoids the Factor G pathway that responds to beta-glucans, which makes it useful for confirming whether a positive LAL result is endotoxin or fungal carbohydrate interference. Its regulatory acceptance varies by jurisdiction and by product type, so a supplier should state which pharmacopoeia or guidance the method follows rather than describing it as "LAL" generically.

## Setting a Limit: EU/mL, EU/mg, and the Maximum Valid Dilution

Compendial limits are written for pharmaceutical products, not research peptides, but they provide the reference framework. The general parenteral limit is 5 EU/kg body weight per hour; the intrathecal limit is 0.2 EU/kg per hour; Water for Injection is 0.25 EU/mL. These come from the K/M calculation in USP &lt;85&gt;, where K is the threshold dose and M is the maximum human dose per kilogram per hour.

| Matrix | Limit | Basis |
|---|---|---|
| Water for Injection | 0.25 EU/mL | USP &lt;85&gt; |
| Parenteral drug, general | 5 EU/kg/hour | USP &lt;85&gt; K/M calculation |
| Intrathecal drug | 0.2 EU/kg/hour | USP &lt;85&gt; K/M calculation |
| LAL reagent water | ≤ 0.005 EU/mL | Reagent specification |
| Research peptide, internal criterion | Often 1 EU/mg or lower | Buyer-defined specification |

For a lyophilized peptide, the limit is usually written per milligram because the vial is weighed, not measured by volume. The conversion to EU/mL happens at reconstitution. A 10 mg vial reconstituted in 1 mL gives 10 mg/mL; if the specification is 1 EU/mg, the solution limit is 10 EU/mL.

The MVD then sets how far that solution can be diluted while remaining above the assay's sensitivity:

**MVD = (endotoxin limit × sample concentration) / λ**

With a 1 EU/mg limit, a 10 mg/mL sample, and a gel-clot sensitivity of 0.03 EU/mL, the MVD is (1 × 10) / 0.03 = 333-fold. A lab that dilutes 10-fold is not testing at the limit it claims; a lab that dilutes 1,000-fold has diluted past the point where a passing result means anything. The MVD belongs on the report, or at least in the raw data.

## Interference, Spike Recovery, and Low Endotoxin Recovery

Peptide matrices interfere with LAL more often than suppliers admit. Cationic and amphipathic peptides can bind reagent components or mask Lipid A. Low pH, high salt, chelating agents, and residual organic solvents change reaction kinetics. The result can be a false negative, which is the dangerous direction because it produces a passing report.

USP &lt;85&gt; controls this with an interference test: spike a known amount of endotoxin standard into the sample and confirm recovery between 50% and 200%. Outside that window, the sample must be diluted or treated until recovery falls inside it. The spike recovery result should appear on the COA, not just the final EU value. A result of 0.4 EU/mg means little if recovery was 30%.

A separate problem is low endotoxin recovery (LER). In some matrices, spiked endotoxin becomes undetectable over hours to days even though it is still present. The effect is associated with chelators, surfactants, and certain formulation conditions, and it has been documented across parenteral products. For peptides, the practical implication is that hold time before assay is part of the method. A sample held 72 hours at room temperature may read lower than the same sample assayed within 24 hours at 2–8 °C. The COA should state the hold condition, or the lab should demonstrate that its hold time is validated for that matrix.

Beta-glucan is the other interference route. Standard LAL can react through Factor G, producing a false positive in samples exposed to cellulose filters, some glassware, or fungal-derived materials. rFC avoids that pathway. Glucan-blocking buffers are an alternative for LAL-based methods. Either way, a positive result on a peptide that never contacted gram-negative bacteria deserves a second method before it is accepted as endotoxin.

## Where Contamination Enters Peptide Manufacturing

Endotoxin control is a water and equipment problem before it is a testing problem.

**Water.** LPS is water-soluble and passes standard filtration. Facilities without validated Water for Injection production, distribution, and monitoring cannot assure low endotoxin in the water used for purification, buffer preparation, or lyophilization make-up. WFI is specified at 0.25 EU/mL; LAL reagent water is typically specified at ≤0.005 EU/mL. The difference between those two numbers is the difference between a controlled system and a variable one.

**Raw materials.** Protected amino acids, resins, and solvents can carry endotoxin from their own manufacture. Pharmaceutical-grade suppliers typically state an endotoxin specification; research-grade suppliers often do not. A batch traceability file that stops at the amino acid vendor has a gap.

**Equipment and surfaces.** Synthesis reactors, HPLC columns, filters, and lyophilizer shelves can harbor LPS. Dry heat at 250 °C for at least 30 minutes is the standard depyrogenation cycle for glassware and heat-stable metal, typically validated to a 3-log reduction. Sodium hydroxide cycles are used for some surfaces. A facility that applies these steps to some contact surfaces and not others has a contamination route that testing will eventually find.

**Lyophilization and vialing.** Freeze-drying concentrates the sample but does not destroy endotoxin. LPS present before lyophilization remains in the cake. Stoppers, vials, and the lyophilizer chamber are all potential sources. This is why [lyophilization cycle design](/blog/lyophilization-cycle-peptides/) and component preparation belong in the same quality conversation as the assay.

## Reading Endotoxin Data on a COA

A usable endotoxin report has six elements: method, limit, numeric result, spike recovery, testing laboratory, and lot linkage. The table below turns those into a review checklist.

| Check | Acceptable evidence | Red flag |
|---|---|---|
| Method | Gel-clot, kinetic turbidimetric, kinetic chromogenic, or rFC named | "LAL test" with no format |
| Limit | EU/mL or EU/mg stated with basis | No limit, only "pass" |
| Result | Numeric value below the limit | Pass/fail with no value |
| Spike recovery | 50–200% at the reported dilution | Recovery omitted or outside range |
| MVD | Stated or calculable from raw data | No dilution factor |
| Laboratory | Named lab with accreditation status | "Internal" with no identity |
| Lot linkage | Same lot on vial, COA, and invoice | Generic COA reused across batches |
| Hold condition | Sample hold time and temperature stated | No date or storage detail |

Two further checks are worth making. First, confirm that the assay's lower limit, after dilution, is below the specification. A 0.03 EU/mL gel-clot method diluted 333-fold has an effective limit of 10 EU/mL, which is exactly the specification in the example above; there is no margin for error. Second, check whether the reported result is below the limit of quantification or merely below the limit of detection. "Less than 0.5 EU/mg" is not the same statement as "0.2 EU/mg."

If the report is for a batch intended for cell culture or an in vivo model, the buyer's internal criterion should be set before the batch is ordered, not after the result arrives. A specification written after seeing the number is not a specification. The [documentation package guide](/blog/peptide-documentation-package/) lists the records that should travel with each lot.

## Prevention and the Limits of Depyrogenation

Removing endotoxin from a finished peptide is hard, and every available method has a cost.

Ultrafiltration can remove LPS aggregates with a 10 kDa or similar membrane, but amphipathic peptides associate with LPS and may be lost with it. Polymyxin B immobilized on a support binds Lipid A and can capture endotoxin, but it can also bind the peptide, so recovery has to be measured. Dry heat at 250 °C for 30 minutes works for glass and stainless steel, not for peptide powder or most single-use components. None of these methods is a substitute for controlling water, reagents, and contact surfaces upstream.

The economic argument follows. A batch that fails endotoxin after lyophilization is usually a total loss, because rework risks both yield and integrity. A batch made with validated WFI, qualified reagents, and depyrogenated contact surfaces has a much lower probability of reaching that point. Testing verifies control; it does not create it.

Analytical control and contamination control meet in the release decision. A peptide with 99% HPLC purity and a failed endotoxin result is not a release candidate for immunologically sensitive work, and a peptide with low endotoxin and a misidentified sequence is not a release candidate either. The [HPLC and LC-MS comparison](/blog/hplc-vs-lc-ms-peptides/) covers the identity side of that pair, and the [quality testing page](/peptide-quality-testing/) describes how the tests fit together. Handling after receipt, including reconstitution and storage, is covered in the [handling protocols](/peptide-handling-protocols/).

## The Author's Take

**Position.** Endotoxin data should be treated as a method-plus-result claim, never as a standalone pass. If a COA cannot show the assay format, the limit, the numeric value, and spike recovery at the reported dilution, the correct response is to request the raw data rather than to accept the conclusion.

**Reasoning.** LAL is a biological cascade with known interference routes. Peptides are exactly the kind of matrix that produces false negatives through binding and false positives through beta-glucans. The 50–200% recovery window exists because the assay fails in both directions. A supplier that reports only "pass" has removed the information a reviewer needs to judge whether the assay worked. The same logic applies to the limit: an EU/mg figure without a stated specification cannot be evaluated, because the number only means something relative to a threshold.

**Disclosure.** Peptides of China sells research peptides. This article describes assay methods and documentation review; it is not medical advice, a dosing guide, or a claim about the effects of any compound. Products are supplied for laboratory research use only. Endotoxin testing arrangements and documentation vary by product and batch, and buyers who require independent results should arrange third-party testing after receipt.

## Sources

- USP &lt;85&gt; Bacterial Endotoxins Test. United States Pharmacopeia. [usp.org/usp-nf](https://www.usp.org/usp-nf)
- FDA Guidance for Industry: Pyrogen and Endotoxins Testing: Questions and Answers (2012). [fda.gov](https://www.fda.gov/regulatory-information/search-fda-guidance-documents/pyrogen-and-endotoxins-testing-questions-and-answers)
- ICH Q2(R2) Validation of Analytical Procedures (2023). [database.ich.org](https://database.ich.org/sites/default/files/ICH_Q2%28R2%29_Guideline_2023_1130.pdf)
- Cao, Y. et al. Low endotoxin recovery and its impact on endotoxin detection. *Biopolymers* (2021). [doi:10.1002/bip.23470](https://doi.org/10.1002/bip.23470)
- Gorman, A. et al. Lipopolysaccharide structure and the phenomenon of low endotoxin recovery. *European Journal of Pharmaceutics and Biopharmaceutics* (2022). [doi:10.1016/j.ejpb.2022.10.006](https://doi.org/10.1016/j.ejpb.2022.10.006)
- Bolden, J. Recombinant Factor C. In *Endotoxin Detection and Control in Pharma, Limulus, and Mammalian Systems* (2019). [doi:10.1007/978-3-030-17148-3_13](https://doi.org/10.1007/978-3-030-17148-3_13)
- Thurman, T. et al. Comparison of pyrogen assays by testing products exhibiting low endotoxin recovery. *ALTEX* (2022). [doi:10.14573/altex.2202021](https://doi.org/10.14573/altex.2202021)
- Cai, Y. et al. The bacterial endotoxin test in the Chinese pharmacopoeia: A journey of international harmonization and national consideration. *Journal of Microbiological Methods* (2026). [doi:10.1016/j.mimet.2026.107411](https://doi.org/10.1016/j.mimet.2026.107411)
