---
title: "Sterility Testing for Peptides: Method, Sampling, and COA Review"
slug: "sterility-testing-peptide-manufacturing"
description: "How USP <71> sterility testing works for peptides: membrane filtration, method suitability, sampling limits, and the fields a COA must show."
author: "POC Tech Team"
updated: "2026-11-27"
---
**A sterility test is a sampling test, not a batch-wide guarantee.** It takes a defined number of units from a lot, incubates them in two media for 14 days, and looks for growth. A passing result means the tested units were sterile under the conditions of the test. It does not mean every vial in the lot is sterile, and it cannot detect a low-frequency contamination event that fell outside the sample.

For a lyophilized peptide, that distinction is the whole review. Sterility is produced by the manufacturing process — controlled environment, validated filtration, aseptic fill, container integrity — and the test is a check on that process. A COA that reports "sterile: pass" without the method, the sample size, and the laboratory has reported a conclusion, not a result.

This guide covers the compendial methods, the statistical limit of a passed test, and the fields a buyer should require before accepting a sterility claim on a peptide lot.

## What the sterility test samples

USP &lt;71&gt; defines the compendial sterility test. The method is built around two media: fluid thioglycollate medium (FTM) for anaerobic and aerobic organisms, and soybean casein digest medium (SCDM) for fungi and aerobic bacteria. FTM is incubated at 30 to 35 °C and SCDM at 20 to 25 °C, both for 14 days.

The sample is drawn from the lot, not from the bulk solution. For a lyophilized product, the vial is reconstituted under aseptic conditions and the contents are transferred to the membrane or inoculated directly. The test therefore samples the container, the closure, the fill, and the lyophilization process together. A failure can originate in any of them.

The compendial method is not a rapid method. Fourteen days is a long time in a supply chain, which is why many manufacturers release on bioburden and environmental data and treat the sterility result as a confirmatory test. That practice is defensible only when the process controls are documented. A sterility result that arrives after the batch has shipped is a retrospective check, not a release gate.

## Membrane filtration versus direct inoculation

Two methods dominate. Membrane filtration passes the sample through a membrane with a nominal pore size of 0.45 µm or smaller, captures microorganisms on the surface, rinses away inhibitory residues, and places the membrane on or in the medium. Direct inoculation adds the sample directly to the medium and relies on dilution to overcome inhibition.

| Method | Principle | Strength | Limitation | Best fit |
|---|---|---|---|---|
| Membrane filtration | Microbes retained on 0.45 µm membrane, then incubated | Removes bacteriostatic peptide and buffer residues; concentrates low bioburden | Requires filter compatibility and validation; membrane can adsorb peptide | Clear solutions, filtrates, products with antimicrobial activity |
| Direct inoculation | Sample added to medium | Simple; no filtration step | Sample volume limited; inhibition harder to overcome | Oily or viscous products; small volumes |
| Most probable number | Serial dilution and growth scoring | Useful for non-sterile bioburden estimates | Not a compendial sterility release method | Raw material and water monitoring |

For peptides, membrane filtration is usually preferred because many sequences and counterions inhibit microbial growth. The filtration step removes the peptide from the organisms, which is the point. The risk is that the membrane also adsorbs the peptide and, with it, any organisms bound to the peptide. Method suitability testing is designed to catch that.

## Method suitability and bacteriostasis

Method suitability is the experiment that proves the test can detect contamination in the presence of the product. A defined inoculum — typically 100 colony-forming units or fewer — is added to the sample and processed through the same method. The organism must be recovered.

USP &lt;1227&gt; describes the validation of microbial recovery. The key variables are the challenge organisms, the rinse volume, the neutralization strategy, and the incubation conditions. For a peptide that inhibits growth, the validation may require a larger rinse volume, a neutralizing diluent, or a smaller sample volume.

A COA rarely shows the suitability result. That is a gap. A sterility test run without a product-specific suitability check is a method applied to a matrix it was not validated for. The reviewer cannot tell whether a passing result reflects sterility or inhibition.

The practical request is therefore two documents: the sterility result and the method suitability summary for that product family. If the supplier cannot produce the second, the first is weaker than it looks.

## The statistics of a passed test

A sterility test is a binomial sample. If the lot has a contamination rate of p, the probability that a sample of n units contains no contaminated unit is (1 − p)^n. Solving for the upper bound when zero positives are observed gives the rule of three: the 95 percent upper confidence bound is approximately 3/n.

That produces numbers worth remembering. A test of 20 units with zero growth is consistent with a contamination rate as high as about 15 percent at the 95 percent confidence level. A test of 100 units with zero growth bounds the rate at about 3 percent. Neither result proves that every vial is sterile, and neither is designed to.

| Units tested | Zero-positive result | 95% upper bound on contamination rate |
|---|---|---|
| 10 | Pass | ~26% |
| 20 | Pass | ~14% |
| 50 | Pass | ~6% |
| 100 | Pass | ~3% |
| 200 | Pass | ~1.5% |

The table is a statistical property of sampling, not a criticism of the method. It explains why sterility assurance for aseptically filled products comes from process validation, environmental monitoring, and container closure integrity, with the sterility test as one confirmatory element. A supplier that presents a sterility pass as a batch-wide guarantee is overstating what the test can do.

For terminally sterilized products, the equivalent concept is the sterility assurance level, usually 10⁻⁶ — a one-in-a-million probability that a unit is non-sterile after the validated sterilization cycle. Peptides that are lyophilized aseptically do not have a terminal sterilization cycle, so the assurance comes from the aseptic process instead.

## Lyophilised peptides: sterility is a process claim

A lyophilized vial is filled with a sterile solution, then frozen and dried under vacuum. The lyophilization step is not a sterilization step. Organisms introduced during fill remain in the cake, and the open transfer into the dryer is a contamination risk.

The process controls that matter are the ones around the fill: the grade of the environment, the air flow, the personnel gowning, the media fill program, and the integrity of the vial and stopper. EU GMP Annex 1, revised in 2022, frames these as a contamination control strategy rather than a list of isolated tests. It also requires consideration of container closure integrity and, for certain products, pre-use post-sterilization integrity testing of filters.

A supplier that lyophilizes in a non-classified environment and tests the finished vial for sterility is testing a process it did not control. The test may pass. The batch is still not aseptic in any meaningful sense.

## Environmental monitoring and container integrity

Environmental monitoring is the evidence that the fill environment stayed within its classification during the run. For a Grade A zone, the standard is ISO 14644-1 Class 5 at rest, with viable and non-viable particle limits applied during operation. Settle plates, active air samples, and surface swabs are incubated and trended.

Container closure integrity (CCI) is the other half. A vial can be sterile at fill and leak afterwards. Dye ingress, vacuum decay, and headspace analysis are common CCI methods. For a lyophilized product under vacuum, the presence of a vacuum in the vial is itself a weak integrity indicator, but it is not a validated test.

A COA will rarely include environmental monitoring or CCI data; those belong to the batch record and the site's quality system. The buyer's request should therefore separate lot-level release data from site-level process data. The first can be attached to the certificate; the second is reviewed during a supplier audit.

## Reading the sterility row on a COA

The sterility row is one line on a certificate and one of the easiest to over-read. A usable entry has five components.

| Component | Acceptable entry | What a weak entry looks like |
|---|---|---|
| Method | USP &lt;71&gt; membrane filtration, with rinse volume | "Sterility test" with no method |
| Sample size | Number of units tested and lot size | No sample size |
| Media and incubation | FTM 30–35 °C, SCDM 20–25 °C, 14 days | "Incubated per USP" without conditions |
| Result | No growth at 14 days, with test date | "Pass" |
| Laboratory | Named lab, accreditation status | "Internal" with no identity |
| Suitability | Product-specific method suitability on file | Not mentioned |

Two further checks are worth making. First, confirm that the lot number on the sterility report matches the lot on the vial and the invoice. A sterility result attached to a different lot is not evidence for this shipment. Second, check the test date against the fill date. A sterility test started months after fill may have been performed on a retained sample that was stored under conditions different from the shipped lot.

The distinction between "no growth at 14 days" and "sterile" is not pedantic. The first is a test result. The second is a conclusion about the batch. A certificate should report the first and let the reviewer draw the second.

## Sterility, bioburden, and endotoxin are different questions

Three tests are often grouped under "microbiological quality," and they answer different questions.

**Bioburden** is the number of viable organisms in the product or on a component before sterilization or fill. ISO 11737-1 describes the methods. Bioburden is a process control: a low, trending count supports the conclusion that the sterilization or filtration step has enough margin.

**Sterility** is the absence of viable organisms in the tested units after the process. It is a release test.

**Endotoxin** is a chemical marker from gram-negative cell walls. It is not a measure of live organisms, and a sterile product can carry endotoxin from organisms killed upstream. USP &lt;85&gt; and the FDA pyrogen guidance describe the assay and its limits.

A COA that reports sterility but not endotoxin has answered one of three questions. For cell-culture work, all three matter; for a lyophilized research reagent used in a non-cellular assay, the buyer may reasonably accept a lower documentation tier. The decision should be explicit, not inferred from a "sterile" label.

## The Author's Take

**Position.** I treat a sterility claim on a peptide COA as a process statement, not a product guarantee. The claim is only meaningful when the method, the sample size, the laboratory, and the site's environmental controls are all visible. Without them, "sterile" is a word on a page.

**Reasoning.** The arithmetic of sampling is unforgiving. Twenty units with no growth is compatible with a contamination rate near 14 percent at the 95 percent level. That is not a reason to distrust every sterility test; it is a reason to locate assurance where it actually lives — in the aseptic process, the media fills, the environmental monitoring, and the container integrity checks. A supplier that understands this will talk about its fill line before it talks about the test result. A supplier that leads with "sterile: pass" is either simplifying for the buyer or has not thought through what the certificate can support. The buyer's move is to ask for the process evidence and to commission an independent test when the application is sensitive.

**Disclosure.** Peptides of China sells research peptides. This article describes compendial test methods and certificate review; it is not medical advice, a dosing guide, or a claim about the effects of any compound. Products are supplied for laboratory research use only. Sterility status, testing arrangements, and documentation vary by product and batch, and a research-grade label should not be read as a pharmaceutical sterility claim.

## Sources

- USP &lt;71&gt;, Sterility Tests. United States Pharmacopeia. [usp.org](https://www.usp.org/usp-nf)
- USP &lt;1227&gt;, Validation of Microbial Recovery from Pharmacopeial Articles. United States Pharmacopeia. [usp.org](https://www.usp.org/usp-nf)
- USP &lt;1116&gt;, Microbiological Control of Aseptic Processing Environments. United States Pharmacopeia. [usp.org](https://www.usp.org/usp-nf)
- FDA Guidance for Industry: Sterile Drug Products Produced by Aseptic Processing — Current Good Manufacturing Practice (2004). [fda.gov](https://www.fda.gov/regulatory-information/search-fda-guidance-documents/sterile-drug-products-produced-aseptic-processing-current-good-manufacturing-practice)
- 21 CFR 211.167, Special testing requirements. U.S. Code of Federal Regulations. [ecfr.gov](https://www.ecfr.gov/current/title-21/chapter-I/subchapter-C/part-211/subpart-I/section-211.167)
- European Commission, EudraLex Volume 4, Annex 1: Manufacture of Sterile Medicinal Products (2022). [health.ec.europa.eu](https://health.ec.europa.eu/medicinal-products/eudralex/eudralex-volume-4_en)
- ISO 11737-1:2018, Sterilization of health care products — Microbiological methods — Part 1: Determination of a population of microorganisms on products. [iso.org](https://www.iso.org/standard/66445.html)
- FDA Guidance for Industry: Pyrogen and Endotoxins Testing: Questions and Answers (2012). [fda.gov](https://www.fda.gov/regulatory-information/search-fda-guidance-documents/pyrogen-and-endotoxins-testing-questions-and-answers)

For the surrounding release panel, see [endotoxin testing for peptides](/blog/endotoxin-testing-peptide-manufacturing/) and the [sterility protocol guide](/blog/sterility-testing-for-research-peptides-a-protocol-guide/). The [COA reading guide](/blog/how-to-read-a-peptide-coa-a-researchers-guide-to-hplc-and-ms-reports/) covers the certificate structure, and the [quality testing hub](/peptide-quality-testing/) collects the method standards. Supplier site checks are described in the [manufacturer verification protocol](/blog/china-peptide-manufacturer-verification-a-2026-b2b-sourcing-protocol/), with the broader document set in the [documentation package guide](/blog/peptide-documentation-package/).
