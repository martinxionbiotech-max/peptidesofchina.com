---
title: "Peptide Quality & Testing: HPLC, MS, COA and Batch Consistency"
slug: "peptide-quality-testing"
description: "What a peptide COA actually proves: HPLC purity, LC-MS/MALDI identity, counterions, endotoxins, sterility, sampling and batch consistency for research buyers."
---

A certificate of analysis is often treated as a verdict. It is closer to a receipt with laboratory attachments. The document records what a manufacturer tested, on which lot, using which method, and what the numbers were. That is useful evidence. It becomes misleading when a buyer reads the purity line and stops there.

This guide explains what each number on a peptide COA can support, where the common analytical methods diverge, and how to judge batch consistency across repeat orders. It is written for laboratory and procurement readers evaluating research compounds. Nothing here is medical advice, and none of it is a recommendation for human use.

## Direct answer: what a peptide COA actually proves

A peptide COA proves three things at most: that a lot was assigned an identifier, that a defined set of tests was performed on a sample from that lot, and that the results fell within the issuer's specification. It does not prove that the vial in your hand came from that lot unless the lot identifier travels with the shipment. It does not prove that the batch is homogeneous, sterile, free of endotoxin, or suitable for a particular assay.

The useful question is not whether a supplier provides a COA. Most do. The useful question is what the document connects to, what was tested, and what the test actually measures. A COA with a matching lot number, a named method, a chromatogram, a mass spectrum, a mass-balance section and a signature is evidence. A one-page table of "conforms" results is a claim wearing the same clothes.

The questions underneath every quality decision are consistent:

1. **Is it the right molecule?** That is an identity question, answered by mass spectrometry, sequencing, or an orthogonal method such as amino acid analysis.
2. **Is it the amount claimed?** That is a content question, answered by net peptide content or assay, not by HPLC area percent.
3. **Is it clean enough for the intended assay?** That is an impurity and microbiology question, answered by related-substance profiles, residual solvent data, endotoxin testing and sterility testing where relevant.

A COA that answers only the first two, or that answers them with a single undifferentiated percentage, leaves the third question open. Most sourcing disputes start there.

## What "purity" means on a peptide COA

Different numbers get called purity, and they are not interchangeable.

**Chromatographic purity (area percent).** The main peak's integrated area divided by the total integrated area of all peaks in the chromatogram, multiplied by 100. This is the number most COAs report. It is a ratio whose denominator is only what the detector can see under the stated method.

**Peptide content (net peptide content).** The mass of the target peptide divided by the total mass of the vial contents, expressed as a percentage or as milligrams per vial. This number accounts for counterions, water, residual solvents and inorganic residue.

**Impurity-based purity.** One hundred percent minus the sum of specified and unspecified impurities, often with individual limits for each.

A COA can legitimately report 98.6% HPLC purity and 82% peptide content. Both can be true. The first says the UV-visible peak area is mostly one species. The second says the vial's mass is mostly the target peptide. The gap is the salt counterion, residual water, residual solvents and inorganic material. Buyers who treat the first number as the second will misstate the molar concentration in every assay.

Purity is also method-relative. Change the column chemistry, gradient slope, detection wavelength, sample load or integration threshold and the number moves. A purity figure without a method description is not a specification. It is a marketing number with a decimal point.

## HPLC/UV, LC-MS and MALDI-TOF: three instruments, three questions

The methods most often cited on peptide COAs answer different questions. The [HPLC versus LC-MS comparison](/blog/hplc-vs-lc-ms-peptides/) covers the method mechanics in more detail; the summary below focuses on what each result can support.

### HPLC/UV: separation and area percent

Reversed-phase HPLC separates peptides by hydrophobicity: a C18 column, a water/acetonitrile gradient acidified with trifluoroacetic acid, and UV detection at 214 or 220 nm. The peptide backbone absorbs in that range, so the method works for compounds without aromatic residues.

The output is a chromatogram and an area-percent calculation. The method's strength is separation: it resolves truncations, deletions and many modified variants. Its weaknesses are structural:

- **Co-elution.** Two species with similar hydrophobicity can merge into one peak. A deamidated variant, a diastereomer, or a side-reaction product may sit under the main peak and never appear as a separate area.
- **No identity.** A clean peak does not prove the peak is the labeled sequence.
- **A moving denominator.** Salts, counterions, water and solvents do not absorb at 220 nm, so they are invisible to the calculation. A sample can be 99% pure by area and still contain a fifth of its mass as non-peptide material.
- **Method dependence.** Column age, stationary-phase batch, temperature, gradient delay and integration settings shift the result. Cross-lab comparisons without a shared method are unreliable.
- **Detection-limit blindness.** Impurities below the UV threshold are not reported. "Total impurities: 0.4%" often means "0.4% of what this method could see."

None of this makes HPLC useless. It makes HPLC a separation and quantification tool, not an identity tool. The [limits of purity and concentration testing](/blog/why-purity-and-concentration-tests-are-not-enough/) are worth reading alongside any COA that reports only area percent.

### LC-MS: mass and, with fragmentation, sequence

Liquid chromatography coupled to mass spectrometry adds a mass dimension. The chromatograph separates, the mass spectrometer measures the mass-to-charge ratio of the eluting species, and software converts that to a molecular mass.

Mass alone is weaker evidence than it looks. A scrambled sequence, a positional isomer, or a peptide with the same elemental composition can produce the same nominal mass. Sequence confirmation requires fragmentation. In tandem MS, the precursor ion is fragmented along the backbone, producing b-ions and y-ions whose mass differences correspond to amino acid residues. Matching that ladder to the expected sequence is a residue-level check, not a whole-molecule check.

LC-MS also improves impurity detection: an extracted ion chromatogram can reveal a co-eluting species with a different mass that the UV trace merged into the main peak. The advantage is not unlimited. Ionization efficiency varies by compound, so MS peak areas cannot be used as purity percentages without authenticated standards, and ion suppression can hide minor components.

A COA line that says "MS: confirmed" without a spectrum, a calculated mass, an observed mass and an adduct annotation is close to unfalsifiable. Ask for the spectrum. The [molecular weight verification guide](/blog/peptide-molecular-weight-verification-steps/) explains the arithmetic and the common adduct patterns.

### MALDI-TOF: a fast identity check with a different bias

Matrix-assisted laser desorption/ionization time-of-flight mass spectrometry co-crystallizes the sample with a UV-absorbing matrix, fires a laser at the spot, and measures the flight time of the resulting ions. It is fast, sensitive, and tolerant of salts and buffers that would clog an electrospray source, and it gives a clean singly charged molecular ion for many intact peptides.

Its limits are different from LC-MS, not absent:

- **Quantitation is poor.** Spot-to-spot variation, matrix heterogeneity and ionization suppression make peak intensity a weak proxy for concentration. MALDI is an identity method, not a purity method.
- **Low-mass interference.** Matrix clusters and adducts clutter the region below roughly 500 to 700 Da, where short peptides and many fragments appear.
- **Adducts and in-source decay.** Sodium and potassium adducts, plus fragmentation during desorption, can shift or split the signal. A good operator annotates them; a copied PDF often does not.
- **No sequence without MS/MS.** A single mass peak confirms mass, not sequence. TOF/TOF instruments can fragment, but many service labs report only intact mass.
- **Crystallization bias.** Hydrophobic or glycosylated peptides may not co-crystallize evenly, so the spectrum can under-represent some species.

MALDI is a useful orthogonal check when the question is "is the expected mass present?" It is a poor primary method when the question is "how much of the batch is the target peptide?"

### Putting the methods together

A defensible package includes an RP-HPLC chromatogram with method conditions, an LC-MS spectrum with calculated and observed mass, and, where the sequence is ambiguous or modified, fragmentation data or an orthogonal technique. MALDI can substitute for electrospray in a pinch, particularly for larger peptides, but it should not be the only identity evidence for a short, heavily modified, or unusually hydrophobic compound.

Two methods that share a blind spot are not orthogonal. HPLC and LC-MS depend on the same sample preparation and often the same chromatography, so their errors can correlate. MALDI changes the ionization mechanism, which is why it adds value, but it brings its own biases. The strongest package uses methods that fail differently.

## The COA, field by field

A COA is easiest to audit in five blocks: traceability, identity, purity, mass balance, and microbiology, with administrative fields checked alongside each. The [full COA reading guide](/blog/how-to-read-a-peptide-coa-a-researchers-guide-to-hplc-and-ms-reports/) walks through a worked example; this section is the checklist.

| Block | Fields to check | What the field supports |
|---|---|---|
| Traceability | Product name, catalogue number, lot or batch number, manufacture date, release date, retest or expiry date, quantity per vial, storage condition, issuer, signatory | Whether the document can be tied to the material and whether the dates are internally consistent |
| Identity | Sequence, molecular formula, theoretical mass, observed mass, method and instrument, spectrum or chromatogram | Whether the molecule is the labeled compound, and how strong that evidence is |
| Purity | HPLC method, column, mobile phase, gradient, wavelength, flow rate, sample volume, retention time, area percent, individual impurities, total impurities, chromatogram | Whether the separation supports the claimed purity and what the method could not see |
| Mass balance | Net peptide content or assay, counterion identity and content, water content, residual solvents, heavy metals, inorganic residue | Whether the labeled mass is mostly peptide, and what the rest of the vial contains |
| Microbiology | Bioburden, endotoxin method and result, sterility method and result | Whether the material is suitable for cell culture or animal work, if those are relevant |
| Administrative | Specification versus result for each test, method references, raw data availability, page numbering, revision history | Whether the document is a controlled record or a summary table |

The fields most often missing are the ones that matter most for reproducibility: the HPLC method details, individual impurity limits, counterion content, water content and net peptide content. A COA can list twenty tests and still leave the mass balance unknowable.

Two traceability checks deserve emphasis. First, the lot number on the COA must match the lot number on the vial label, the packing slip and the invoice. If any of those documents use a different identifier, the analytical results describe a different population of vials. Second, the dates must be possible: tested before manufactured, released before tested, or a retest date beyond the stability data are all reasons to stop and ask.

The [peptide documentation package](/blog/peptide-documentation-package/) checklist extends this to shipping records and retention samples. The [characterization reporting checklist](/blog/peptide-characterization-reporting-checklist/) is useful when a lab needs to compare vendors on paper before requesting samples.

## Counterions and TFA: the salt is part of the product

Solid-phase peptide synthesis uses trifluoroacetic acid for cleavage and global deprotection. Reverse-phase purification uses TFA as an ion-pairing agent. The result is that many synthetic peptides leave the manufacturer as TFA salts, with the counterion associated with basic residues.

TFA is not a trace curiosity. It contributes mass, and it can change behavior in assays. A 2025 study on counterion analysis validated FT-IR, ¹⁹F-NMR and HPLC-ELSD methods for TFA quantification, found that exchange with 10 mM HCl was the most effective removal condition, and observed that the salt form affected passive membrane permeability for some sequences without changing peptide purity ([Pharmaceuticals, 2025](https://pmc.ncbi.nlm.nih.gov/articles/PMC12389442/)). The practical point for buyers is that two vials of the same peptide, one as the TFA salt and one as the acetate or chloride salt, are not interchangeable in a sensitive assay.

Counterion content should be on the COA as an identity and a percentage or molar ratio. Ion chromatography is the standard quantitative method; the Thermo Fisher application note on TFA in peptides shows the separation of fluoride, acetate and trifluoroacetate in commercial peptide samples ([Thermo Fisher AN 115](https://documents.thermofisher.com/TFS-Assets/CMD/Application-Notes/4077-AN115_LPN0898-01.pdf)). If the COA says "TFA salt" but gives no content, the mass balance is incomplete. If it says "counterion: none," ask what the counterion actually is.

The choice of salt form is a study-design decision, not a quality hierarchy. Acetate is common for biological work; chloride is used where TFA interferes; TFA is convenient for chromatography and can be problematic for spectroscopy and permeability assays. The [counterion stability guide](/blog/role-of-counterions-in-peptide-stability/) covers the mechanism, and the [TFA removal note](/blog/tfa-removal-peptides/) covers the process side. Do not attempt counterion exchange as an improvised bench step without validating it; the exchange can change solubility, aggregation and assay response.

## Water content and net peptide content

A lyophilized peptide looks dry but is not. Residual water in a freeze-dried cake is typically a few percent by mass, and the exact figure depends on the formulation, the cycle and the vial. Karl Fischer titration is the reference method: coulometric titration for low water levels, volumetric titration for higher ones. Mettler Toledo's application note on lyophilized products describes the coulometric approach and why the sample handling matters ([Mettler Toledo](https://www.mt.com/us/en/home/supportive_content/ana_chem_applications/titration/M738.html)).

Water is not an inert filler. It acts as a plasticizer, enables hydrolytic and deamidation reactions, and can collapse or shrink a cake during storage. A product with 8% water may be chemically stable at 4 °C and unstable at room temperature; the same product at 2% water may have a different shelf life. The specification should be product-specific and backed by stability data.

Net peptide content is the number that turns a vial into a molar concentration. The arithmetic is simple and unforgiving:

> weighed mass × peptide content = peptide mass

A 10 mg vial at 80% peptide content contains 8 mg of peptide, not 10 mg. If an assay assumes 10 mg, every concentration is 25% high. This is not a rounding error; it is a systematic bias that propagates through every dilution.

Ask for net peptide content as a percentage or as milligrams per vial, and ask what method produced it. UV absorbance at 280 nm works only for peptides with aromatic residues and depends on the extinction coefficient. Amino acid analysis is more general but slower. A COA that reports only "purity 98%" has not told you how much peptide is in the vial.

The [lyophilized stability note](/blog/peptide-stability-why-lyophilized-peptides-are-far-more-stable-than-you-think/) is a useful counterweight to the assumption that dry means inert: lyophilized peptides are often more stable than solutions, but the margin depends on water content, temperature and sequence.

## Endotoxins: a separate test with a separate failure mode

Endotoxins are lipopolysaccharides from the outer membrane of gram-negative bacteria. They are heat-stable, survive autoclaving, and pass through 0.22-micron filters. A sterile product can still be pyrogenic.

The compendial method is the bacterial endotoxins test in USP <85>, which uses Limulus amebocyte lysate in gel-clot, turbidimetric or chromogenic formats ([USP <85>](https://www.usp.org/harmonization-standards/pdg/general-methods/bacterial-endotoxins)). Recombinant Factor C assays are also used and can be validated against the compendial method. Results are reported in endotoxin units, either per milliliter or per milligram of product. The unit matters: a result of "<0.5 EU/mL" on a reconstituted solution is not comparable to "<0.5 EU/mg" on the powder without the reconstitution volume and the peptide content.

The FDA's points-to-consider document on bacterial endotoxin specifications notes that the test method is typically USP <85> and that the specification should be tied to the product and its intended use ([FDA](https://www.fda.gov/media/183132/download)). For research buyers, the practical question is narrower: will endotoxin at the measured level confound the assay? Cell culture systems, macrophage and microglial work, cytokine assays and animal models are sensitive to LPS. The [endotoxin biology guide](/blog/what-are-endotoxins-why-they-matter/) explains the TLR4 pathway and the experimental failure modes.

A COA line that says "endotoxin: negative" without a method, a limit and a unit is not a result. A line that says "endotoxin: <1 EU/mg" is a result, but it still describes a sample, not every vial. Endotoxin contamination is heterogeneous: it can come from water, glassware, raw materials or the environment, and it can be concentrated in one part of a lot. The [endotoxin testing guide](/blog/endotoxin-testing-peptide-manufacturing/) covers method selection and the sources of false confidence.

## Sterility: what a pass covers

Sterility testing asks whether a sample contains viable microorganisms that can grow under defined conditions. USP <71> describes the two compendial approaches: membrane filtration, which is preferred for filterable solutions, and direct inoculation, which is used for products that cannot be filtered ([USP <71>](https://www.usp.org/sites/default/files/usp/document/harmonization/gen-method/q11_pf_ira_34_6_2008.pdf)). Membrane filtration passes the sample through a 0.45-micron filter, rinses it, transfers the membrane to fluid thioglycollate medium and soybean-casein digest medium, and incubates for 14 days at 30 to 35 °C and 20 to 25 °C respectively.

Before a sterility result is valid, the method must be shown not to inhibit microbial growth. That is the bacteriostasis and fungistasis validation: known challenge organisms are inoculated into the test system and must grow. Without that control, a "pass" can mean the product killed the challenge organism rather than that the sample was sterile.

A sterility pass is a statistical statement about the tested sample. It is not a batch-wide guarantee. The test consumes a small fraction of the lot, and contamination can be unevenly distributed. Sterility and endotoxin are complementary tests, not substitutes.

For research use, sterility matters when the material will enter a cell culture system without a terminal sterile filtration step, or when an animal protocol requires sterile reagents. The [sterility testing guide](/blog/sterility-testing-peptide-manufacturing/) covers rapid methods and their validation status. A COA that says "sterile" without a method reference, a test date and a result is a marketing line, not microbiology.

## Impurity profiles: total purity hides the interesting part

Peptide-related impurities come in families: truncated sequences from incomplete coupling, deletion and insertion sequences, diastereomers from racemization, deamidated asparagine or glutamine residues, oxidized methionine or tryptophan, pyroglutamate formation at the N-terminus, residual protecting groups, and adducts from cleavage or workup.

A total purity number flattens all of that into one figure. A 99% pure batch with a 0.6% oxidized variant may be less useful for a receptor-binding assay than a 96% pure batch whose 4% is water and inorganic salt. The identity and amount of the impurity matter more than the total, which is why the FDA's peptide guidance emphasizes impurity profiles rather than a single purity threshold ([FDA peptide guidances](https://www.fda.gov/drugs/drug-alerts-and-statements/fda-publishes-revised-draft-product-specific-guidances-certain-generic-peptide-products)).

Residual solvents are a separate class. Acetonitrile, dichloromethane, dimethylformamide, trifluoroacetic acid and methanol can remain after synthesis and purification. ICH Q3C sets class-based limits, and a COA should report the solvents relevant to the process, not a generic "residual solvents: none." Heavy metals from catalysts or reagents are a third class, addressed by ICH Q3D and measured by ICP-MS. Inorganic residue, sometimes reported as sulfated ash or residue on ignition, is a fourth.

The [common synthesis failure guide](/blog/common-peptide-synthesis-failures-a-practical-lab-guide/) maps these impurities to process steps. The [impurity effects on study outcomes](/blog/why-impurities-affect-clinical-study-outcomes/) note connects analytical data to experimental interpretation.

## Batch sampling: one vial is not the batch

A COA describes a sample. The batch is the population. The gap between them is sampling.

Manufacturers release a lot by sampling according to an internal plan, testing, and comparing results with the specification. Sampling plans such as ISO 2859-1 define accept, reject and sample-size rules indexed by lot size and inspection level ([ISO 2859-1](https://www.iso.org/standard/2859-1)). A plan designed for attribute inspection, where each unit is classified as conforming or nonconforming, is not a perfect fit for a lyophilized peptide with continuous variables such as purity and water content. Manufacturers often use a combination of sampling tables and internal statistical criteria. The point for buyers is that the plan exists, it is not the same as testing every vial, and the COA rarely states which plan was used.

Lyophilized lots have specific homogeneity risks. Fill weight varies across the run. Vials at different positions in the freeze-dryer see different shelf temperatures and vapor flow, which can affect residual water and cake structure. A composite sample made by pooling several vials can hide that variation; a single grab sample can exaggerate it. The useful sample is random, from the same fill and cycle, with the location recorded.

Buyers can improve their position without auditing the factory:

- Request the COA for the exact lot on the invoice, not a representative COA for the product.
- Buy one extra vial from the same lot and retain it unopened as a reserve sample.
- For a critical study, split the sample: send one aliquot to an independent lab and keep the other in reserve.

The [quality assurance process guide](/blog/peptide-quality-assurance-process-a-researchers-guide-to-sourcing-integrity/) describes a documented incoming-inspection workflow. The [supplier inconsistency note](/blog/why-peptide-suppliers-inconsistent-quality/) explains why two orders of the same catalogue number can behave differently even when both have a COA.

## Batch consistency: what to track across lots

Batch consistency is not the same as batch compliance. A lot can pass a ≥95% specification and still be a poor match for the previous lot if the impurity profile, counterion content or water content has drifted. Consistency is a trend question, and trends require data from more than one lot.

Track a small set of variables across every incoming lot:

- **Retention time and peak shape** on the same HPLC method. A shift in retention time can indicate a column change, a salt-form change or a different impurity profile.
- **Area percent and individual impurity percentages.** Record the full profile, not just the total.
- **Counterion identity and content.** A switch from acetate to TFA can change solubility and assay response.
- **Water content.** A drift from 3% to 7% changes net peptide content and stability.
- **Net peptide content.** This is the variable that converts weighed mass into molar concentration.
- **Appearance and reconstitution behavior.** Cake collapse, discoloration, slow dissolution and persistent turbidity are signals that the lyophilization or the formulation changed.
- **Functional response in the assay.** A bioassay or binding assay is the final check that the analytical specification corresponds to biological behavior.

Plot these values over lots. A purity series of 99.1, 98.9, 99.0, 98.8 is noise around a stable process. A series of 99.1, 98.2, 97.4, 96.8 is a trend, even if every lot passes a ≥95% specification.

Specification width is a business decision disguised as a scientific one. Neither width is inherently better without a method and an impurity profile behind it. A loose specification with a full profile and a stable trend can be more informative than a tight number with no history.

Retest dates belong in this discussion. A retest date is a claim about stability, and it should be supported by stability data at the stated storage condition. A 24-month retest date on a peptide with no stability study is a calendar guess. The [specification sheet guide](/blog/why-peptide-specification-sheets-matter-in-procurement/) covers the commercial side of this, and the [consistent sourcing note](/blog/why-consistent-sourcing-enables-meta-analysis/) explains why lot-to-lot drift matters beyond a single experiment.

## Third-party retest: commissioning a test that means something

Independent testing is a buyer's strongest tool, but only when sample, method and laboratory are chosen as carefully as the manufacturing specification.

Start with the laboratory. ISO/IEC 17025 defines the competence, impartiality and consistent operation requirements for testing and calibration laboratories ([ISO/IEC 17025](https://www.iso.org/standard/66912.html)). Accreditation is a useful filter, but it is not enough on its own: check that the specific test is within the lab's accredited scope, ask for the method and the limit of quantitation, and confirm that the lab will report raw data rather than a summary certificate.

Then control the sample. A retest is only as good as the chain of custody. Record the vial label and lot, photograph the sealed vial, ship it under the conditions specified for the product, and ask the lab to record the receipt condition. A lab result attached to an unidentified sample is an anecdote.

Define the panel before you ship. For a typical research peptide, the minimum independent panel is identity by LC-MS, purity by RP-HPLC with the method reported, counterion by ion chromatography, and water by Karl Fischer. Add endotoxin by LAL or rFC for cell-culture or animal work, sterility by USP <71> for sterile applications, and residual solvents by GC when the process uses high-boiling or toxic solvents. The [testing and analysis guide](/blog/peptide-testing-and-analysis-a-professional-guide-to-laboratory-verification/) covers panel selection in more detail.

Interpret the results against the manufacturer's COA with method differences in mind. Two labs can differ by a percentage point or two on the same sample because of column chemistry, gradient, wavelength or integration. Ask whether the method explains the difference and whether it changes the decision. For a dispute, agree on a referee lab and acceptance criteria before testing.

One structural caution: a third-party COA commissioned by the seller is not the same as a third-party COA commissioned by the buyer. The independence belongs to the party who selects the sample and pays for the test. The [note on why this site does not provide third-party COAs](/blog/why-we-do-not-provide-third-party-coas-and-what-that-actually-means/) explains the reasoning from the supplier side. The [three-step verification approach](/blog/how-we-verify-product-quality-our-3-step-approach/) describes how manufacturer documents and buyer-side checks fit together.

## What a COA does not prove

A COA has limits.

It does not prove that the vial in your hand is the lot that was tested, unless the lot identifier is on the vial and the chain of custody is intact. It does not prove that the batch is homogeneous. It does not prove that the product is sterile, endotoxin-free or free of viruses and prions. It does not prove that the sequence is correct if the only identity evidence is a single mass. It does not prove that unspecified impurities are absent or harmless. It does not prove that the manufacturer operates under GMP, that the facility has been audited, or that the product is legal in your jurisdiction.

It also does not prove that the peptide is suitable for your assay. Analytical purity and biological performance are different questions. A peptide can be 98% pure by HPLC and still fail a binding assay because of aggregation, adsorption to plastic, oxidation during storage, or a counterion that interferes with the readout. The [purity and concentration limitations note](/blog/why-purity-and-concentration-tests-are-not-enough/) develops this point.

And a COA does not convert a research compound into a medicine. Every product discussed on this site is supplied for laboratory research only. A certificate describes analytical attributes; it says nothing about safety, efficacy, administration or fitness for human use. The [research-use disclaimer](/research-use-disclaimer/) is the governing statement.

## Red flags

Bad documentation usually fails on structure before numbers:

- **No lot number, or a lot number that does not match the label and invoice.** Without lot linkage, the rest of the document describes an unknown population.
- **A purity figure with no chromatogram and no method.** A number without a method cannot be interpreted or reproduced.
- **A single sharp peak at the solvent front.** This can indicate a sample that elutes before the gradient resolves anything, not a pure peptide.
- **Mass spectrometry reported as "confirmed" with no spectrum, calculated mass or adduct annotation.** The claim cannot be checked.
- **Identical COAs for different products or different lots.** Reused documents are a known failure mode in the reseller segment.
- **Dates that cannot be true.** Tested before manufactured, released before tested, or a retest date beyond the stability data.
- **"Third-party tested" with no laboratory name, report number or scope.** A logo is not a report.
- **No counterion or water data on a high-purity claim.** The mass balance is incomplete, and the purity number is doing work it cannot do.
- **"Endotoxin: negative" or "sterile: yes" with no method, unit or date.** Microbiology claims need method context.
- **"GMP" without a certificate, audit scope or facility identity.** GMP is a system, not an adjective.
- **A COA issued by a trading company with no manufacturer named.** The issuer may not control the process that generated the data.
- **Specification "conforms" with no numeric result.** A pass/fail table without values cannot be trended.

The [low-quality peptide market note](/blog/why-so-many-peptides-on-the-market-are-low-quality/) and the [research-grade versus GMP comparison](/blog/research-grade-vs-gmp-peptides/) put these flags in commercial context. A price that cannot cover synthesis, purification and testing is a question worth asking.

## Decision framework: match the evidence to the research use

No single documentation standard fits every purchase. A peptide used in a biochemical assay and a peptide used in an animal model do not need the same panel. The framework below matches the minimum evidence to the research context.

| Research context | Minimum evidence | Add when the risk justifies it |
|---|---|---|
| Biochemical assay, ELISA, binding study | Lot-linked COA, LC-MS identity, HPLC purity with method, counterion identity, water content | Net peptide content, individual impurity profile, residual solvents |
| Cell culture | The above plus endotoxin result with method and unit | Sterility by USP <71>, mycoplasma testing, low-endotoxin specification |
| Animal model | The above plus sterility, heavy metals, full impurity profile, net peptide content | Batch-consistency history, independent retest, stability data at the storage condition |
| Formulation or process development | The above plus assay, counterion quantitation, forced degradation, batch history | Reference standard characterization, ICH Q2 validation data, excipient compatibility |
| Regulatory or toxicology package | GMP documentation, validated methods, full ICH Q3C/Q3D package, stability protocol | Facility audit, drug master file, independent referee testing |

Three gates apply across all contexts. **Gate one: traceability.** Can the document be tied to the vial? If not, stop. **Gate two: identity.** Is there mass evidence and, where needed, sequence evidence? A purity number alone does not pass. **Gate three: mass balance.** Do net content, counterion and water add up to a coherent picture of the vial? If not, the purity figure is incomplete.

A COA that passes gate one but fails gate three is partial; request the missing fields before committing to a study. The [research-grade procurement guide](/blog/research-grade-peptides-2026-lab-procurement-guide/) and the [GMP compliance assessment](/blog/how-to-assess-peptide-supplier-gmp-compliance-in-2026/) extend the framework to supplier selection.

For buyers comparing manufacturers, the [manufacturing partners page](/manufacturing-partners/) describes how this site selects production sources, and the [custom peptide services page](/custom-peptide-services/) covers projects where the specification is built from scratch. The [peptide quality overview](/peptide-quality/) is the shorter commercial companion to this page.

## FAQ

### Is a 99% HPLC purity peptide good enough?

Not automatically. The number describes the share of integrated UV peak area under one method, not the share of peptide mass. A 99% area purity can coexist with 80% peptide content, an unidentified co-eluting impurity, or an interfering counterion. Ask for the method, chromatogram, impurity profile and mass balance before treating 99% as a threshold.

### What is the difference between HPLC purity and peptide content?

HPLC purity is a ratio of peak areas at a detection wavelength. Peptide content is the mass fraction of target peptide in the vial. Counterions, water, residual solvents and inorganic residue add mass but not UV peak area, so the numbers diverge. For molar concentration, peptide content is the number to use.

### Do I need both LC-MS and MALDI-TOF?

Usually not. LC-MS with a mass spectrum is the more informative primary identity test, and tandem MS adds sequence confirmation. MALDI-TOF is a useful orthogonal check for intact mass, especially for larger or difficult peptides. If a supplier offers only MALDI, ask whether a second method supports the mass and whether the low-mass region is clear of matrix interference.

### Can a manufacturer's COA be trusted?

As a record of what the manufacturer tested, yes, provided lot linkage is intact and methods are described. It is not independent evidence: the manufacturer selects the sample, runs the test and writes the specification. That does not make the data false; it defines the scope. Buyers who need independence should commission their own retest on a sample they control.

### What does "third-party tested" mean on a peptide listing?

It can mean almost anything. The useful version names the laboratory, report number, test panel and lot. The weak version is a logo and a PDF that cannot be tied to the vial. Ask who selected the sample, who paid, and whether the tested lot matches the invoice.

### How much does an independent retest cost?

It depends on the panel. Identity and purity by HPLC and LC-MS are the least expensive; counterion by ion chromatography, water by Karl Fischer, endotoxin by LAL or rFC, sterility by USP <71> and residual solvents by GC each add cost and time. A full panel can exceed the price of the peptide. For most buyers, a targeted panel based on assay risk is a better use of budget.

### How do I check batch consistency across repeat orders?

Record lot number, HPLC retention time, area percent, individual impurities, counterion content, water and net peptide content for every incoming lot, then plot them. One lot that passes a specification is compliance; a series with a stable profile is consistency. If the trend moves while every lot still passes, ask what changed.

### Does a COA prove a peptide is sterile or endotoxin-free?

No. They are separate tests, and each describes a sample rather than the whole batch. A COA that reports "sterile" without a USP <71> method reference, date and result is making a claim, not reporting data. The same applies to "endotoxin-free" without a method, limit and unit. If those attributes matter, specify the tests and review the raw results.

## The Author's Take

**Position.** A COA is a chain-of-custody document before it is a number. If the lot identifier, the method description and the mass balance do not line up, the purity percentage is decoration. I would rather buy a 96% peptide with a complete, traceable record than a 99.5% peptide with a one-page certificate and no chromatogram.

**Reasoning.** Three observations drive that position. First, most sourcing disputes in this segment are not about a lab making an arithmetic error; they are about a document that cannot be tied to the material in question. Second, the gap between area-percent purity and net peptide content is the most common technical misunderstanding in research purchasing, and it silently biases every concentration in a study. Third, microbiology claims are the most overextended part of the market: sterility and endotoxin are sample-based tests, not product-wide properties, and a "pass" without a method is not a result.

**Disclosure.** Peptides of China is a sourcing intermediary, not an analytical laboratory. It does not manufacture peptides, does not issue third-party COAs, and does not guarantee a universal documentation package. Manufacturer-side documents vary by product and batch. The analytical framework here is the standard I use to read those documents, not a claim that every supplier meets it. This page is research-use-only content; it is not medical advice, and it does not recommend human use of any compound.

## Sources

1. USP. *<85> Bacterial Endotoxins Test.* Harmonized general chapter. https://www.usp.org/harmonization-standards/pdg/general-methods/bacterial-endotoxins
2. USP. *<71> Sterility Tests.* General chapter, PDF. https://www.usp.org/sites/default/files/usp/document/harmonization/gen-method/q11_pf_ira_34_6_2008.pdf
3. International Council for Harmonisation. *ICH Q2(R2): Validation of Analytical Procedures.* 2023. https://database.ich.org/sites/default/files/ICH_Q2(R2)_Guideline_2023_1130.pdf
4. U.S. Food and Drug Administration. *FDA Publishes Revised Draft Product-Specific Guidances for Certain Generic Peptide Products.* https://www.fda.gov/drugs/drug-alerts-and-statements/fda-publishes-revised-draft-product-specific-guidances-certain-generic-peptide-products
5. U.S. Food and Drug Administration. *The Bacterial Endotoxins Specification: Points to Consider.* https://www.fda.gov/media/183132/download
6. *Towards a Consensus for the Analysis and Exchange of TFA as a Counterion in Synthetic Peptides and Its Influence on Membrane Permeation.* Pharmaceuticals, 2025. https://pmc.ncbi.nlm.nih.gov/articles/PMC12389442/
7. Thermo Fisher Scientific. *Application Note 115: Determination of Trifluoroacetic Acid (TFA) in Peptides.* https://documents.thermofisher.com/TFS-Assets/CMD/Application-Notes/4077-AN115_LPN0898-01.pdf
8. Mettler Toledo. *Water Content in Lyophilized Vaccines by Karl Fischer Titration.* https://www.mt.com/us/en/home/supportive_content/ana_chem_applications/titration/M738.html
9. International Organization for Standardization. *ISO 2859-1: Sampling Procedures for Inspection by Attributes.* https://www.iso.org/standard/2859-1
10. International Organization for Standardization. *ISO/IEC 17025: General Requirements for the Competence of Testing and Calibration Laboratories.* https://www.iso.org/standard/66912.html
