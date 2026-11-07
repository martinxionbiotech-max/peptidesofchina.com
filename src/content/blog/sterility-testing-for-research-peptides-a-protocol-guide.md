---
title: "Sterility Testing for Research Peptides: A USP 71 Protocol Guide"
slug: "sterility-testing-for-research-peptides-a-protocol-guide"
description: "How a USP 71 sterility test is run on a research peptide: method choice, sample size, media and incubation, controls, method suitability, and COA review."
---

A sterility test on a research peptide is a growth-based presence/absence assay, and five decisions determine whether the result means anything: membrane filtration or direct inoculation, the number of units sampled, the two media and their incubation temperatures across 14 days, the positive and negative controls run alongside, and whether method suitability has been demonstrated for that peptide matrix. Miss the fifth and a contaminated vial can read as clean.

Certificates spend most of their space on the pass/fail word and almost none on those five decisions. This page covers the protocol, the arithmetic behind a pass, and the documents to request before treating "sterility: pass" as data. The manufacturing view is covered in [sterility testing in peptide manufacturing](/blog/sterility-testing-peptide-manufacturing/).

Research peptides are laboratory reagents. A sterility result on a lyophilised powder is a characterisation data point, not a statement that the material is a sterile medicine, and nothing below is a clinical, dosing, or safety claim for any compound.

## Which Method Fits a Peptide Sample

USP &lt;71&gt; defines two compendial methods, and the choice follows the sample's physical behaviour rather than preference. Membrane filtration passes the product through a 0.45 µm membrane, captures any microorganisms on the surface, rinses the peptide away, and transfers the membrane into culture media. Direct inoculation pipettes the product straight into the medium and leaves it there for the full incubation.

| Parameter | Membrane filtration | Direct inoculation |
|---|---|---|
| Separation step | Microbes retained on a 0.45 µm membrane; product and excipients rinse through | None; product stays in contact with the medium |
| Rinse | Three portions of about 100 mL of diluent, with neutraliser added where justified | Not applicable |
| Product interference | Largely removed before incubation | Present for the whole 14 days; relies on dilution |
| Sample volume tested | Contents of each unit, in full | Limited to the fraction of the vessel the medium can tolerate |
| Typical fit | Lyophilised peptide that dissolves to a clear, filterable solution | Suspensions, viscous formulations, material that clogs the filter |
| Dominant failure mode | Membrane clogging; peptide adsorbing to the filter and carrying microbes with it | False negative from an antimicrobial peptide |
| Compendial position | Preferred method | Alternative when filtration is not feasible |

Membrane filtration is the default for a lyophilised peptide that reconstitutes to a clear solution, because the rinse separates the peptide from the organisms before incubation. Direct inoculation keeps the product in contact with the medium for two weeks, which is why a cationic or amphipathic peptide is a poor candidate: the membrane activity that makes it interesting in a cell assay suppresses growth in a culture vessel.

Two checks sit on top of the method choice: confirm the peptide dissolves at the test concentration, since a cloudy solution blinds the membrane, and confirm the laboratory validated its rinse volume.

## The Protocol, Step by Step

The sequence below is what a contract laboratory should be able to describe from memory. A missing step weakens the result.

1. **Test the filled vial, not the bulk solution.** A test on bulk substance before filling says nothing about contamination introduced at filling, stoppering, or capping — steps described in the [lyophilisation cycle guide](/blog/lyophilization-cycle-peptides/). The sample must be the article the buyer receives.
2. **Reconstitute in sterile diluent with no preservative.** Sterile water for injection or sterile saline is appropriate. Bacteriostatic water contains benzyl alcohol, which is antimicrobial and will suppress growth in the test vessel; using it as the reconstitution diluent builds a false negative into the method.
3. **Pull the compendial number of units.** USP &lt;71&gt; scales the minimum sample with batch size: 10% or 4 units for lots of 100 or fewer, 10 units for 101–500, and 2% or 20 units (whichever is less) above 500. A 1,000-vial lot therefore tests 20 vials.
4. **Filter each unit through 0.45 µm.** Record the membrane manufacturer and lot, because membrane lot variability is a documented source of recovery differences.
5. **Rinse with three portions of about 100 mL.** Add polysorbate 80 or lecithin to the rinse only when method suitability shows the peptide is otherwise inhibitory, and state the concentration.
6. **Divide the membrane between the two media.** One half goes into about 100 mL of fluid thioglycollate medium (FTM); the other into about 100 mL of soybean–casein digest medium (SCDM).
7. **Incubate 14 days and read at intervals.** FTM at 30–35 °C, SCDM at 20–25 °C. Record observations at day 3, day 7, and day 14 rather than only at the end, because a late-appearing turbidity and an early one point to different sources.
8. **Run the controls in the same session.** A positive control per medium and a negative control through the same filtration train. Controls that are not run alongside the sample do not validate that session.

Growth promotion covers the other half. Each FTM and SCDM lot is challenged with fewer than 100 CFU of the specified organisms and must show visible growth within seven days at the labelled temperature. Without growth-promotion records for that media lot, the chain has an unverified link.

## Incubation, Media, and Controls

The two media answer different questions, and the pair is not optional. FTM has a low redox potential through most of its depth and supports anaerobes as well as aerobes near the surface. SCDM supports aerobic bacteria and fungi. Running one medium halves the panel and doubles the chance that a slow fungus or an obligate anaerobe goes undetected.

| Vessel | Medium | Temperature | Duration | Inoculum | Expected result |
|---|---|---|---|---|---|
| Test, anaerobic | FTM, about 100 mL | 30–35 °C | 14 days | Contents of sampled units | No growth |
| Test, aerobic/fungal | SCDM, about 100 mL | 20–25 °C | 14 days | Contents of sampled units | No growth |
| Positive control, anaerobic | FTM | 30–35 °C | 14 days | &lt;100 CFU *Clostridium sporogenes* | Visible growth |
| Positive control, aerobic | SCDM | 20–25 °C | 14 days | &lt;100 CFU *Staphylococcus aureus* or *Bacillus subtilis* | Visible growth |
| Positive control, fungal | SCDM | 20–25 °C | 14 days | &lt;100 CFU *Candida albicans* or *Aspergillus brasiliensis* | Visible growth |
| Negative control | Diluent only, through the same filter | Same as test | 14 days | None | No growth |
| Suitability, bacteria | FTM with product | 30–35 °C | 3 days minimum | &lt;100 CFU per organism | Growth comparable to control |
| Suitability, fungi | SCDM with product | 20–25 °C | 5 days minimum | &lt;100 CFU per organism | Growth comparable to control |

A positive control that fails to grow invalidates the run: it means the medium, the incubation, or the handling was faulty, so a "no growth" result on the sample carries no information. A negative control that grows points to contamination introduced by the analyst, the isolator, or the diluent, and the run is void. Both directions matter, and both are routinely omitted from the summary that reaches a buyer.

Testing environment belongs in the same conversation. Compendial testing runs in a Grade A / ISO 5 unidirectional airflow zone, usually an isolator decontaminated with vaporised hydrogen peroxide, inside a controlled background; settle plates there should stay below 1 CFU per 4 hours. A test on an open bench has a different error rate.

## Method Suitability Before Any Result Counts

Method suitability, historically bacteriostasis and fungistasis testing, proves the peptide does not suppress microbial growth in the media. USP &lt;71&gt; requires it; USP &lt;1227&gt; describes the recovery-validation logic. Without a passed study, a sterility result describes the medium, not the product.

The procedure is a comparison: six organisms inoculated at fewer than 100 CFU into medium with the peptide, and the same inoculum into medium without it. Growth in the product vessel must be comparable to the control. The panel is fixed: *Staphylococcus aureus*, *Bacillus subtilis*, *Pseudomonas aeruginosa*, *Clostridium sporogenes*, *Candida albicans*, and *Aspergillus brasiliensis*.

| Check | Evidence to look for | Red flag |
|---|---|---|
| Organism panel | All six compendial strains listed by name | "Suitability performed" with no panel |
| Inoculum | Stated as &lt;100 CFU per organism | No count, or a count above 100 CFU |
| Control comparison | Growth in product medium compared against growth without product | Result reported as "pass" with no comparison |
| Incubation | At least 3 days for bacteria, 5 days for fungi | Single 24-hour read |
| Neutraliser | Identity and concentration stated where used | Neutraliser added with no justification |
| Matrix scope | Tied to the specific peptide, salt form, and reconstitution volume | One study reused across unrelated products |
| Repeat trigger | Re-run on formulation, supplier, or concentration change | Study dated before the current process |

When suitability fails, the fix is methodological, not rhetorical. The usual options are a larger dilution, a neutraliser such as polysorbate 80 or lecithin, a switch from direct inoculation to membrane filtration, or a validated alternative method. A supplier that reports a failed suitability study and then reports a passing sterility test on the same product, with no description of the change, has described two incompatible results.

Suitability also bounds the claim. If the peptide passes only at a 1:100 dilution, the assay tests a 1:100 dilution, and low-level contamination in the neat material may fall below detection. The dilution factor belongs on the report.

## Bioburden, Sterility, and Endotoxin Answer Different Questions

Three microbiological tests appear on peptide documentation, and buyers routinely treat them as one.

Bioburden is a count. ISO 11737-1 describes enumeration of viable microorganisms on a product before sterilisation, reported in CFU per unit or per gram. It is a process-control number, showing whether the upstream process is drifting. Alert and action limits of 10 and 100 CFU/g are buyer-defined, not compendial.

Sterility is a presence/absence verdict on a sample, under those conditions, at that moment. It does not quantify or predict the next vial.

Endotoxin is a chemistry measurement. The LAL or rFC assay detects lipopolysaccharide from gram-negative cell walls in EU/mL or EU/mg, and it is unaffected by whether the organisms are alive. A 0.22 µm filter removes bacterial cells but not LPS micelles, and autoclaving kills cells while leaving the pyrogen intact, so a batch can be sterile and still carry endotoxin. As a working conversion, 1 EU is roughly 0.1 ng of reference-standard LPS. The assay formats, limits, and spike-recovery requirements are covered in the [endotoxin testing guide](/blog/endotoxin-testing-peptide-manufacturing/).

None of the three substitutes for another. A low bioburden count does not prove sterility of the filled vial, a sterility pass does not bound endotoxin, and a clean endotoxin result says nothing about fungal contamination. For cell-culture work all three matter; for a powder used in a biochemical assay, sterility may be irrelevant and endotoxin may still count.

## Sample Size and What a Pass Covers

Sterility testing is a sampling procedure, and the arithmetic is unforgiving.

Twenty units from a 1,000-vial lot is 2% of the batch. If 1% of vials carry a contaminant, the chance that all 20 sampled units happen to be clean is 0.99^20, about 0.82 — meaning the test detects that contamination only about 18% of the time. At a 0.1% contamination rate, detection probability falls to roughly 2%. The test is good at finding a badly contaminated batch and poor at finding a marginally contaminated one.

Assurance of sterility therefore comes from the process, not the test. A terminally sterilised product is validated to a sterility assurance level of 10^-6, a one-in-a-million probability of a non-sterile unit, derived from the sterilisation cycle. A media fill — a process simulation filling and incubating thousands of units — is the aseptic equivalent. Testing 20 vials cannot produce a 10^-6 claim, and no certificate should imply that it does.

For a research peptide the conclusion is narrower. A pass on 20 units is evidence that the lot was produced without gross contamination. It is not evidence that every vial is clean, and it is not a release specification for a sterile medicine. A buyer who needs a sterile article needs a product manufactured and released as one, with the aseptic process documentation that goes with it.

## Hold Time and Sample Integrity

Between sampling and assay, the sample is a biological specimen and it changes.

The working rule is to assay within 24 hours of reconstitution, holding at 2–8 °C in the interval. A 72-hour hold at ambient temperature is a method change, not a scheduling convenience, and it needs a justification in the report. The failure runs in both directions: fastidious organisms lose viability during a long hold and produce a false negative, while a sample held warm in a non-sterile container can pick up contaminants and produce a false positive.

Shipping adds a separate risk. Lyophilised powder should travel as powder; a reconstituted solution shipped at ambient temperature has neither the stability nor the microbiological control of the original vial. Container closure integrity is the third element: a vial with a compromised stopper seal does not stay sterile, and integrity is tested separately, usually by dye ingress or vacuum decay.

Neither test covers handling after receipt. A researcher who reconstitutes with non-sterile water, reuses a syringe, or leaves a solution on the bench for a week owns the contamination that follows. The [reconstitution materials guide](/blog/peptide-reconstitution-materials/) covers the consumables side.

## Reading Sterility Data on a COA

A sterility line that reads "Sterility: Pass (USP &lt;71&gt;)" is a conclusion without a method. The reviewable version carries the following.

- **Method named**, plus the subdivision — membrane filtration or direct inoculation.
- **Units tested**, as a number, and whether they were final filled vials.
- **Media and lots**, both FTM and SCDM, with growth-promotion records available.
- **Incubation conditions**, temperatures and the 14-day period, plus reading intervals.
- **Controls**, positive and negative, with results for the same session.
- **Suitability statement**, including the organism panel, the inoculum, and the dilution or neutraliser used.
- **Testing laboratory**, named, with accreditation status. ISO/IEC 17025 covers a testing lab's competence; ISO 13485 is a device quality system, not a test-lab accreditation.
- **Lot linkage**, with the same lot number on vial, certificate, and packing list, and a test date that falls after the fill date.

Two further tells are worth checking. A certificate claiming "sterile" for a lyophilised powder with no described aseptic filling process asserts something the document cannot support: sterility is a property of a process, and a test samples its output. A single test date reused across a product line is a template, not a batch record. The wider document set is set out in the [characterisation reporting checklist](/blog/peptide-characterization-reporting-checklist/), the [documentation package guide](/blog/peptide-documentation-package/), and the [quality standards guide](/blog/research-peptide-quality-standards-2026-guide/).

Rapid methods deserve a note on the certificate. ATP bioluminescence, automated growth detection, and fluorescence platforms return results in 24 hours to 5 days, and published comparisons show reasonable agreement with the compendial method for many products. None is a drop-in replacement without a validation package against USP &lt;71&gt; for that product, and the report should name the method used.

## The Author's Take

**Position.** Treat a sterility result as three claims bundled together — method, sample, and suitability — and accept it only when all three are visible. If any one is missing, the correct move is to ask for the raw report, not to argue about the pass.

**Reasoning.** The assay is simple to run and easy to run badly. A peptide that suppresses growth, a short rinse, a clogged membrane, a preservative in the diluent, or a 24-hour read on a 14-day test will each produce a clean-looking result from a contaminated vial. Those failures are invisible in the word "pass" and visible in the method section, the part most certificates compress. The statistical limit finishes the argument: 20 units out of 1,000 detects a 1% contamination rate less than one time in five, so a pass describes process control, not the vial in your hand.

**Disclosure.** Peptides of China sells research peptides. This article is sourcing judgment, not an effects claim, and every compound discussed is for research use only. Documentation and testing arrangements vary by product and batch; buyers who need independent microbiological data should arrange third-party testing after receipt, and should not read this page as a statement that any product is sterile.

## Sources

1. United States Pharmacopeia, General Chapter &lt;71&gt; Sterility Tests. USP–NF. https://www.usp.org/usp-nf
2. United States Pharmacopeia, General Chapter &lt;85&gt; Bacterial Endotoxins Test. USP–NF. https://www.usp.org/usp-nf
3. United States Pharmacopeia, General Chapter &lt;1227&gt; Validation of Microbial Recovery from Pharmacopeial Articles. USP–NF. https://www.usp.org/usp-nf
4. ISO 11737-1:2018, Sterilization of health care products — Microbiological methods — Part 1: Determination of a population of microorganisms on products. https://www.iso.org/standard/66445.html
5. U.S. Food and Drug Administration, Sterile Drug Products Produced by Aseptic Processing — Current Good Manufacturing Practice (2004). https://www.fda.gov/regulatory-information/search-fda-guidance-documents/sterile-drug-products-produced-aseptic-processing-current-good-manufacturing-practice
6. U.S. Food and Drug Administration, Pyrogen and Endotoxins Testing: Questions and Answers (2012). https://www.fda.gov/regulatory-information/search-fda-guidance-documents/pyrogen-and-endotoxins-testing-questions-and-answers
7. 21 CFR 610.12, Sterility. Electronic Code of Federal Regulations. https://www.ecfr.gov/current/title-21/section-610.12
8. Parveen, S. et al. Evaluation of growth based rapid microbiological methods for sterility testing of vaccines and other biological products. *Vaccine* 29(45):8012–8023 (2011). https://doi.org/10.1016/j.vaccine.2011.08.055
9. Bugno, A. et al. Performance survey and comparison between rapid sterility testing method and pharmacopoeia sterility test. *Journal of Pharmaceutical Innovation* 13(1):27–35 (2018). https://doi.org/10.1007/s12247-017-9303-z
10. European Pharmacopoeia, Chapter 2.6.1 Sterility. EDQM. https://www.edqm.eu/en/european-pharmacopoeia
