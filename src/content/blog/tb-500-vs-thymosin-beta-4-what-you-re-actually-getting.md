---
title: "TB-500 vs Thymosin Beta-4: What You Are Actually Getting"
slug: "tb-500-vs-thymosin-beta-4-what-you-re-actually-getting"
description: "TB-500 is usually a 17-residue fragment of thymosin beta-4, not the full 43-residue protein. Here is how the labels differ and how to verify the sequence you receive."
author: "POC Tech Team"
updated: "2026-11-19"
---
TB-500 is not a synonym for thymosin beta-4. In most of the research market, TB-500 refers to a synthetic 17-residue fragment derived from the N-terminus of thymosin beta-4, while the full protein is a 43-residue, actin-binding peptide. The two are related by sequence, not interchangeable by identity.

The confusion is commercial as well as scientific. Some suppliers label the full protein as TB-500. Some label the fragment as thymosin beta-4. Some sell a shorter fragment under a similar name. A certificate that says “TB-500” without a sequence, an observed mass, and a purity method does not tell a laboratory which molecule is in the vial.

This guide sets out the difference, the analytical checks that resolve it, and the sourcing questions that matter before a batch is accepted.

## The Naming Problem

“TB-500” began as a trade-style label, not a pharmacopoeial name. It has no single definition enforced across suppliers. The label can refer to:

- the N-terminal 17-residue fragment of thymosin beta-4, usually acetylated;
- the full 43-residue thymosin beta-4;
- a shorter fragment from the actin-binding region;
- a blend or a salt form of one of the above.

The ambiguity is not harmless. A laboratory that plans an actin-binding assay, a cell-migration study, or an analytical method validation needs to know the sequence length, the terminal modifications, and the counterion. A 17-mer and a 43-mer differ in mass by roughly 3 kDa, in charge distribution, and in the number of potential cleavage sites. They are not interchangeable in a binding experiment.

The practical rule is to treat “TB-500” as a product family label and to require the exact sequence on the batch record. The [HPLC versus LC-MS comparison](/blog/hplc-vs-lc-ms-peptides/) explains why a single purity number cannot resolve the difference.

## What Thymosin Beta-4 Is

Thymosin beta-4 is a small actin-sequestering protein. The human gene, TMSB4X, encodes a 44-residue precursor; the initiator methionine is removed, leaving a 43-residue mature peptide that is acetylated at the N-terminus. UniProt entry P62328 records the sequence and the N-terminal acetylation [7].

The mature sequence begins SDKPDMAEIEKFDKSKLKKTETQEKNPLPSKETIEQEKQAGES. It contains no disulfide bond and no glycosylation site. Its biological interest comes largely from its interaction with actin: thymosin beta-4 sequesters monomeric actin and influences filament dynamics, which is why it appears in cell-migration and tissue-repair literature [6].

For a sourcing decision, three features matter:

1. **Length.** The full protein is 43 residues, not 17.
2. **N-terminal acetylation.** The mature peptide is acetylated. A recombinant or synthetic full-length product without the acetyl group is not structurally identical.
3. **No disulfide.** The protein is linear, so a certificate does not need a reduction/alkylation step to report the main chain.

The full protein is more demanding to synthesize than a short fragment. The [synthesis failure review](/blog/common-peptide-synthesis-failures-a-practical-lab-guide/) describes the truncation and deletion products that make sequence verification necessary. A 43-residue chain requires more coupling steps, more purification, and more careful characterization. That cost difference is one reason the market drifted toward the fragment.

## What TB-500 Usually Is

The common TB-500 product is the N-terminal 17-residue fragment of the mature sequence: Ac-SDKPDMAEIEKFDKSKLK. It is acetylated at the N-terminus, linear, and roughly 2 kDa. The sequence corresponds to the first 17 residues of the mature protein, which is the region often described as the actin-binding or active fragment.

That description should be treated as a hypothesis about function, not a license to claim equivalence. The fragment is not the whole protein. It may share some binding properties and lack others. The published literature on the full protein does not automatically transfer to the fragment, and vice versa.

A supplier that sells the fragment should state:

- the exact sequence, including terminal acetylation and amidation;
- the observed monoisotopic or average mass;
- the counterion (acetate, trifluoroacetate, hydrochloride);
- the purity method and the limit;
- the water content and net peptide content;
- the batch number and the date of analysis.

Without those fields, “TB-500” is a label, not an identity.

## The Difference That Changes an Experiment

The sequence difference is not cosmetic. A 43-residue protein and a 17-residue fragment differ in:

- **Mass.** The full protein is about 4.9 kDa; the 17-mer is about 2.0 kDa.
- **Charge and solubility.** The full sequence contains more basic residues and a different charge distribution, which changes solubility and adsorption behaviour.
- **Binding surfaces.** The fragment contains the N-terminal actin-binding region but lacks the C-terminal half of the protein. Any assay that depends on the missing region will not behave the same.
- **Stability.** Shorter peptides can be more or less prone to aggregation depending on the sequence; the difference cannot be assumed in either direction.
- **Detection.** An LC-MS method tuned for a 2 kDa peptide may not recover a 5 kDa protein with the same sensitivity, and the reverse is also true.

For a laboratory, the practical consequence is that the analytical method must match the product. A method validated for the 17-mer should not be used to release the full protein without a bridging study.

## How Labels Fail in Practice

Four label failures are common enough to check on every order.

| Failure | What the buyer sees | What is actually in the vial |
| --- | --- | --- |
| Fragment sold as full protein | “Thymosin Beta-4” on the label | A 17-residue fragment, about 2 kDa |
| Full protein sold as TB-500 | “TB-500” with a 4.9 kDa mass | The 43-residue protein, sometimes without acetylation |
| Missing terminal modification | Sequence matches, mass is off by 42 Da | Unacetylated fragment or a different salt |
| Shorter fragment mislabeled | “TB-500 fragment” with no residue numbers | A fragment from a different region, often 17–23 |

The 42 Da difference is a useful diagnostic. Acetylation adds approximately 42 Da to the mass. A certificate that reports a mass 42 Da below the expected value for the acetylated peptide is telling the buyer that the terminal group is missing, even if the sequence text looks correct.

The “fragment 17–23” label is a separate trap. Residue numbering depends on whether the initiator methionine is counted. A fragment described as 17–23 in one numbering scheme may be a different sequence in another. The only safe description is the actual sequence.

## Analytical Verification: Sequence, Mass, and Purity

A batch of TB-500 should be characterized on three levels: identity, purity, and content. No single method covers all three.

| Test | Method | What it establishes | What it does not establish |
| --- | --- | --- | --- |
| Intact mass | LC-MS or MALDI-TOF | Molecular weight consistent with the proposed sequence | Sequence order or terminal modifications alone |
| Sequence | MS/MS or Edman degradation | Amino-acid order and terminal residues | Purity or biological activity |
| Purity | RP-HPLC, 214 or 220 nm | Area percentage of the main peak | Net peptide content or salt content |
| Counterion | Ion chromatography or titration | Acetate, TFA, or chloride content | Peptide identity |
| Water | Karl Fischer | Residual moisture | Purity |
| Amino-acid analysis | Hydrolysis plus chromatographic quantification | Composition and recovery | Sequence order |
| Endotoxin | LAL, USP <85> | Endotoxin load | Sterility |

For a 17-mer, intact LC-MS with a mass accuracy of 10 ppm or better is achievable on a modern instrument. A report that shows only “molecular weight: 2,000” with no decimal places is not sufficient to distinguish the target from a close analogue. For the full protein, intact mass alone is less decisive because the mass is larger and the isotope envelope is broader; MS/MS coverage or amino-acid analysis becomes more important.

Purity by HPLC area percentage is not the same as peptide content. A 98% area result can sit on a vial with 80% peptide by mass once water and counterion are counted. The [COA reading guide](/blog/how-to-read-a-peptide-coa-a-researchers-guide-to-hplc-and-ms-reports/) explains the difference, and the [molecular weight verification guide](/blog/peptide-molecular-weight-verification-steps/) covers mass accuracy and sample preparation.

Method validation expectations are set out in FDA’s guidance on analytical procedures and methods validation and in USP <1225> [3][4]. A supplier certificate does not need a full validation report, but it should name the method, the column, the gradient, the wavelength, and the system-suitability results. The [laboratory verification guide](/blog/peptide-testing-and-analysis-a-professional-guide-to-laboratory-verification/) sets out a practical testing sequence. A chromatogram with no method is a picture.

## Reading a COA for a TB-500 Batch

A useful certificate for a TB-500 batch has a small number of non-negotiable fields. The rest is supporting detail.

1. **Product name and lot number.** The name should match the sequence, not just the marketing label.
2. **Sequence.** One-letter code, with N- and C-terminal modifications stated.
3. **Theoretical mass.** Calculated from the sequence and modifications.
4. **Observed mass.** With the method and the mass error.
5. **Purity.** Method, wavelength, area percentage, and limit.
6. **Counterion and water.** Identity and result.
7. **Net peptide content.** Calculated from the fill, water, and counterion.
8. **Endotoxin and bioburden.** Method and result, if the product is intended for cell work.
9. **Storage condition and retest date.** Tied to the batch.
10. **Analyst and date.** A result without a date is not a batch record.

The [documentation package guide](/blog/peptide-documentation-package/) lists the full batch-record set. The [TB-500 catalog page](/catalog/tb-500/) lists the formats supplied by Peptides of China. The [supplier verification protocol](/blog/china-peptide-manufacturer-verification-a-2026-b2b-sourcing-protocol/) explains how to check the site behind the certificate.

## Sourcing Questions That Separate a Fragment from a Protein

The fastest way to find out what a supplier is selling is to ask three questions in writing.

**Question 1: What is the exact sequence, including terminal modifications?**
A supplier selling the 17-mer should answer with the sequence and “N-terminal acetylated.” A supplier selling the full protein should answer with the 43-residue sequence and the same terminal detail. An answer that says “TB-500 sequence” without the letters is not an answer.

**Question 2: What is the observed mass, and what is the expected mass?**
The two numbers should be reported together, with the method and the error. A certificate that reports only a nominal molecular weight cannot distinguish a truncation product from the target.

**Question 3: Which fragment, if any, is this?**
If the product is a fragment, the residue range should be stated against a defined reference sequence. If the supplier cannot state the range, the sequence itself is the only reliable description.

A supplier that answers all three, consistently, across two batches is controlling its supply. A supplier that answers differently on each order is repackaging.

## The Author's Take

**Position.** Buy TB-500 by sequence, not by name. The label is a category; the certificate is the product. If the certificate does not state the sequence, the observed mass, and the terminal modifications, the buyer does not know whether the vial contains a 17-mer, a 43-mer, or something in between.

**Reasoning.** The naming ambiguity is structural. TB-500 has no single pharmacopoeial definition, and the market has filled the gap with labels that sound equivalent but describe different molecules. The analytical tools to resolve the difference are routine: intact mass, MS/MS, amino acid analysis, and a method-backed HPLC purity result. The cost of those checks is small compared with the cost of running a study on the wrong molecule. A supplier that resists the questions is telling you something about its documentation, not about the peptide.

**Disclosure.** Peptides of China sells research peptides, including TB-500 and thymosin beta-4–related products. This article is a sourcing and identity judgment, not an effects claim. All materials are for research use only. Nothing here is medical advice or a guarantee that a particular batch matches a particular sequence; the batch certificate governs.

## Sources

1. International Council for Harmonisation. ICH Q6A: Specifications — Test Procedures and Acceptance Criteria for New Drug Substances and New Drug Products. https://database.ich.org/sites/default/files/Q6A%20Guideline.pdf
2. D'Hondt M, Bracke N, Taevernier L, et al. Related impurities in peptide medicines. Journal of Pharmaceutical and Biomedical Analysis. 2014;101:2–30. https://doi.org/10.1016/j.jpba.2014.06.012
3. U.S. Food and Drug Administration. Analytical Procedures and Methods Validation for Drugs and Biologics: Guidance for Industry. 2015. https://www.fda.gov/regulatory-information/search-fda-guidance-documents/analytical-procedures-and-methods-validation-drugs-and-biologics
4. United States Pharmacopeia. &lt;1225&gt; Validation of Compendial Procedures. https://doi.org/10.31003/uspnf_m99945_40101_01
5. World Anti-Doping Agency. Prohibited List. https://www.wada-ama.org/en/prohibited-list
6. Goldstein AL, Hannappel E, Kleinman HK. Thymosin β4: actin-sequestering protein moonlights to repair injured tissues. Trends in Molecular Medicine. 2005;11(9):421–429. https://doi.org/10.1016/j.molmed.2005.07.004
7. UniProt Consortium. TYB4_HUMAN — Thymosin beta-4, entry P62328. https://www.uniprot.org/uniprotkb/P62328/entry
8. El-Faham A, Albericio F. Peptide coupling reagents, more than a letter soup. Chemical Reviews. 2011;111(11):6557–6602. https://doi.org/10.1021/cr100048w
9. Fosgerau K, Hoffmann T. Peptide therapeutics: current status and future directions. Drug Discovery Today. 2015;20(1):122–128. https://doi.org/10.1016/j.drudis.2014.10.003
