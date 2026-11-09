---
title: "Third-Party COAs: Why We Don't Provide Them"
slug: "why-we-do-not-provide-third-party-coas-and-what-that-actually-means"
description: "A seller-commissioned COA is not independent verification. What a certificate can prove, where custody breaks, and how buyers should test."
---
A third-party certificate of analysis is evidence about a sample, not a guarantee about the vial in your hand. The distinction matters because the peptide market has learned to treat a laboratory PDF as a quality credential, when the document only certifies what the laboratory received and tested. If the sample was chosen by the seller and the chain of custody is undocumented, the certificate cannot tell you whether the material you bought came from the same batch.

Peptides of China does not provide seller-commissioned third-party COAs. That is a deliberate position, not a gap in service. This article explains the reasoning, what we provide instead, and how a buyer can build an independent verification step that actually attaches to the received lot.

## What a Third-Party COA Can and Cannot Certify

A certificate of analysis reports the results of named tests on a named sample. A competent report will identify the sample, the method, the result, the specification, and the analyst or approver. Those fields make the result traceable to a laboratory event.

The certificate does not, by itself, certify:

- That the sample came from the batch you purchased.
- That the sample was drawn randomly from the lot.
- That the sample was stored and shipped under conditions that preserve the material.
- That the batch was manufactured at the site named on the invoice.
- That every vial in the lot matches the tested sample.

Those are chain-of-custody and sampling questions. They are answered by records, not by analytical chemistry. A laboratory can be technically excellent and still receive a sample that was selected to flatter the batch.

This is not a criticism of laboratories. It is a description of the limits of a test report. The laboratory tests what it is given; it does not audit the supplier's warehouse.

The [COA reading guide](/blog/how-to-read-a-peptide-coa-a-researchers-guide-to-hplc-and-ms-reports/) walks through the fields that make a report usable in the first place: sample identity, method, result, units, and acceptance limit.

## The Chain-of-Custody Gap

A usable chain of custody has at least five links:

1. **Selection.** Who chose the sample, from which part of the lot, and using what sampling plan?
2. **Sealing.** Was the sample sealed, labelled, and photographed before it left the supplier?
3. **Transfer.** Who carried or shipped it, under what conditions, and with what tracking record?
4. **Receipt.** Did the laboratory record the condition and identifier on arrival?
5. **Retention.** Is a portion of the sample retained for a confirmatory retest?

In the reseller segment, these links are often missing. The supplier selects a sample, sends it to a laboratory, receives a PDF, and publishes the PDF on a product page. The buyer sees a result with a batch number that may not appear on the vial label. The laboratory never saw the lot; it saw a sample.

A certificate can be genuine and still fail to connect to the purchased unit. That is the gap that matters.

The [documentation package guide](/blog/peptide-documentation-package/) sets out the records that close this gap: batch record, packing list, certificate, and a retained sample with matching identifiers.

| Link | What a strong record shows | What a weak record shows |
| --- | --- | --- |
| Selection | Sampling plan, date, sampler, sample location | "Sample provided by client" |
| Sealing | Seal number, label photo, weight | No image or identifier |
| Transfer | Courier, tracking, temperature logger | Hand delivery, no record |
| Receipt | Laboratory sample ID and condition | Only a client reference |
| Retention | Retained aliquot and storage location | No retain |

## Seller-Commissioned Testing Is Not Independent Verification

Independence is a relationship, not a laboratory brand. If the seller chooses the sample, pays for the test, receives the report first, and decides which reports to publish, the verification is commissioned by the party with an interest in the result. The laboratory may be accredited and the method may be sound, but the selection and publication decisions sit with the seller.

This is why manufacturer-to-buyer relationships normally place independent testing with the buyer. The manufacturer releases the batch against its own specification and provides a certificate. The buyer, if it needs independent confirmation, samples the received lot and commissions a laboratory under its own protocol. The resulting report belongs to the buyer and is tied to the buyer's sample.

A seller-commissioned report can still be useful as a screening document. It tells you that at least one sample of the product, at some point, passed a test. It does not tell you which batch, which vial, or which storage history. Treat it as a marketing input, not a release decision.

There is also a selection effect. A seller who publishes only favorable reports is not lying about the reports it publishes. It is choosing which reports to show. The buyer sees the winner of a selection process and mistakes it for a random sample.

## What Manufacturer Documents Do Better

Manufacturer-side documents answer a different set of questions, and for batch identity they are stronger than a seller-commissioned certificate.

| Document | Question it answers | Limit |
| --- | --- | --- |
| Batch record | What was made, when, where, and by which process | Manufacturer's own record; not independent |
| Release COA | What the manufacturer tested and released | Methods and limits must be read closely |
| Raw chromatogram | What the integration actually looked like | Can be copied; check sample IDs and noise |
| Mass spectrum | Whether the mass matches the structure | Does not prove sequence order alone |
| Fill record | Which vials were filled from which bulk lot | Does not prove post-fill storage |
| Stability summary | What the manufacturer claims about shelf life | Review the study design, not the headline |

The batch record is the document that ties a vial to a manufacturing event. It should carry the lot number, the synthesis date, the purification date, the fill date, the site that performed each step, and the specification against which the batch was released. A certificate without a batch record is a result without a parent.

The release COA should be read like a laboratory report, not a brochure. Look for the method, the column and wavelength, the gradient, the integration threshold, the result with units, and the acceptance limit. A row that says "purity: 99%" without a method is not a release decision; it is a slogan.

The [manufacturer verification protocol](/blog/china-peptide-manufacturer-verification-a-2026-b2b-sourcing-protocol/) covers how to check the site and the batch record behind those documents.

## A Buyer-Initiated Testing Protocol

The alternative to a seller-commissioned certificate is a test commissioned by the buyer on the received lot. It does not need to be complicated, but it should be planned before the shipment arrives.

A workable protocol for a lyophilised peptide:

- **Define the lot and sample size.** Record the lot number, vial count, and storage condition on arrival. For a small lot, sample three vials from different positions; keep one unopened as a retain.
- **Photograph before opening.** Capture the vial label, the lot number, the fill appearance, and the outer packaging. These images anchor the sample identity.
- **Weigh the vials.** A calibrated balance gives a fill-mass check and a baseline for content calculations.
- **Test identity.** LC-MS in positive mode with the expected mass and a stated tolerance. Request the annotated charge envelope, not just a deconvoluted number.
- **Test purity.** RP-HPLC at 220 nm with the column, gradient, flow rate, and integration threshold recorded.
- **Test water.** Karl Fischer on the vialed product, because water changes net peptide content.
- **Test endotoxin if required.** LAL in EU/mg with the method and control standard stated.
- **Retain the raw data.** Chromatogram files, spectra, integration tables, and sample IDs should be stored with the lot record.

Use a laboratory accredited to ISO/IEC 17025 for the methods in scope. Accreditation is not a guarantee that a particular result is correct, but it provides a documented quality system, method validation, and a complaints process. Ask for the scope of accreditation and confirm that the methods you need are covered.

The [endotoxin testing guide](/blog/endotoxin-testing-peptide-manufacturing/) explains the LAL method and its limits, and the [molecular weight verification guide](/blog/peptide-molecular-weight-verification-steps/) covers the charge-state arithmetic behind an identity result.

Acceptance rules should be written before the results arrive. Identity outside tolerance is a rejection. Purity below the specification triggers a retest on a second vial from the same lot. Water above the limit requires a content recalculation, not an automatic rejection. Endotoxin above the study limit is a rejection for that study even if purity passes.

A retest is not a second laboratory testing a different sample. It is the same method on a second vial from the same lot, with both raw data sets retained. If the two results disagree beyond the method's repeatability, the lot is heterogeneous, and that is a finding in itself.

## Reading a COA for Batch Linkage

Whether the certificate comes from a manufacturer or a laboratory, the first check is linkage.

| Field | Pass condition | Failure to investigate |
| --- | --- | --- |
| Product name and sequence | Matches the ordered material and salt form | Name only, no sequence or formula |
| Lot number | Appears on vial, certificate, and packing list in the same format | Format changes between documents |
| Manufacture date | Precedes purification, fill, and test dates | Test date before synthesis date |
| Test date | Plausible for the batch age | More than two years before shipping |
| Issuing party | Named legal entity with an address | A logo with no entity |
| Method | Column, gradient, wavelength, run time stated | "HPLC" with no conditions |
| Result and limit | Numeric result with units and a specification | Unitless percentage, no limit |
| Sample ID | Matches the laboratory's receipt record | "Client sample" with no ID |
| Raw data | Available on request | Image-only PDF |

The date sequence is a cheap forensic test. Synthesis before purification, purification before fill, fill before release, and release before shipping. When the order is impossible, the document was assembled rather than generated.

The chromatogram offers a second test. Detector noise is random. Two reports with identical noise patterns, identical minor peak heights, and retention times matching to two decimal places are copies, not independent runs. Real replicate injections vary in the third decimal and in baseline shape.

The [limits of purity and concentration testing](/blog/why-purity-and-concentration-tests-are-not-enough/) are worth reviewing before a certificate is treated as a complete description of a batch.

## What Peptides of China Provides Instead

Peptides of China is a B2B sourcing platform. It coordinates manufacturer-side sourcing, availability, specifications, order processing, international logistics, and support. It does not manufacture peptides, and it does not operate an analytical laboratory.

What we provide is the documentation that connects an order to a batch: the product specification used for the order, the manufacturer-side certificate for the lot where available, the lot identifiers on the vial and packing list, and a communication trail for resolving discrepancies. Where a buyer needs independent analytical evidence, we support buyer-initiated testing rather than substituting a seller-commissioned report.

That division of labor is deliberate. A platform that commissions its own third-party certificate is still the seller. The buyer gains a document, not independence. A buyer who commissions the test owns the sample selection, the chain of custody, and the report.

We coordinate the records described above; the review sequence for what arrives is the same one set out earlier in this article.

The [high-quality sourcing guide](/blog/how-to-source-high-quality-peptides-a-2026-laboratory-verification-guide/) sets out a broader verification sequence for a first order.

## When a Third-Party COA Is Still Useful

A third-party certificate is not worthless. It is useful in four situations:

- **As a screening signal before a first order.** A report from an accredited laboratory, with a sample ID and a method, is better than no analytical information at all.
- **As a comparison between suppliers.** If two suppliers provide reports from the same laboratory with the same method, the results are more comparable than two in-house certificates.
- **As a trigger for your own testing.** A report that shows an unusual impurity profile tells you what to look for when you test the received lot.
- **As evidence in a dispute.** A report that is tied to a sample you selected, with a documented chain of custody, supports a claim. A report commissioned by the seller is weaker evidence.

The key is to keep the document in its proper role. A certificate is an input to a decision, not the decision itself. The decision belongs to the buyer, based on the specification, the batch record, the receipt inspection, and any independent test the project requires.

## The Author's Take

**Position.** A COA should be commissioned by the party that needs to rely on it. When the seller commissions the test, the buyer gets a marketing document with a laboratory letterhead, not independent verification.

**Reasoning.** The analytical methods used on peptides are mature, and an accredited laboratory can produce a valid report on almost any sample. What fails in the market is the link between the report and the vial: who selected the sample, which batch it came from, how it was stored, and whether the published report is one of several. Those questions are structural, not chemical. A buyer who commissions the test on the received lot closes the gap; a buyer who accepts the seller's PDF inherits it. The cost of a buyer-initiated test is small relative to the cost of repeating a study on material that was never characterized.

**Disclosure.** Peptides of China sells research peptides. This article is a sourcing judgment, not an effects claim, and every material discussed is for research use only. We do not provide seller-commissioned third-party COAs, and nothing here should be read as a guarantee of quality for any batch.

## Sources

1. International Organization for Standardization. ISO/IEC 17025:2017 — General requirements for the competence of testing and calibration laboratories. https://www.iso.org/standard/66912.html
2. International Laboratory Accreditation Cooperation. ILAC — accreditation and mutual recognition. https://ilac.org/
3. International Council for Harmonisation. ICH Q2(R2): Validation of Analytical Procedures. 2023. https://database.ich.org/sites/default/files/ICH_Q2%28R2%29_Guideline_2023_1130.pdf
4. U.S. Food and Drug Administration. Analytical Procedures and Methods Validation for Drugs and Biologics: Guidance for Industry. 2015. https://www.fda.gov/regulatory-information/search-fda-guidance-documents/analytical-procedures-and-methods-validation-drugs-and-biologics
5. United States Pharmacopeia. &lt;1058&gt; Analytical Instrument Qualification. https://doi.org/10.31003/uspnf_m1124_10101_01
6. United States Pharmacopeia. &lt;1225&gt; Validation of Compendial Procedures. https://doi.org/10.31003/uspnf_m99945_40101_01
7. D'Hondt M, Bracke N, Taevernier L, et al. Related impurities in peptide medicines. Journal of Pharmaceutical and Biomedical Analysis. 2014;101:2–30. https://doi.org/10.1016/j.jpba.2014.06.012
8. Clinical and Laboratory Standards Institute. Method Evaluation and Validation standards, including EP05 precision studies. https://clsi.org/standards/products/method-evaluation/
9. U.S. Food and Drug Administration. Bioanalytical Method Validation: Guidance for Industry. 2018. https://www.fda.gov/regulatory-information/search-fda-guidance-documents/bioanalytical-method-validation-guidance-industry
