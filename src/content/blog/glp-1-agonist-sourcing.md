---
title: "GLP-1 Agonist Sourcing: A Procurement Checklist for Labs"
slug: "glp-1-agonist-sourcing"
description: "GLP-1 agonist sourcing differs by molecule, salt form, and assay. A procurement checklist for documentation, batch testing, and cold-chain handling."
author: "POC Tech Team"
updated: "2026-11-18"
---
GLP-1 agonist sourcing is not a single product category. Semaglutide, tirzepatide, liraglutide, and the newer triple agonists differ in sequence, fatty-acid modification, molecular mass, and analytical behavior. A specification written for one molecule does not transfer to another, and a certificate copied from one product family is a warning sign rather than a convenience.

This guide is a procurement checklist for research laboratories buying GLP-1 receptor agonist material. It covers the molecule-level differences that change a purchase order, the documentation that should accompany a lot, the content arithmetic that determines price per milligram of peptide, and the cold-chain and verification steps that follow delivery. It does not discuss human dosing, administration, or therapeutic effects.

## The class is not one product

The GLP-1 receptor agonist class includes peptides with different lengths, different receptor profiles, and different half-life extension strategies. Semaglutide is a 31-amino-acid analogue with a C18 fatty diacid attached through a linker, designed to bind albumin. Tirzepatide is a 39-amino-acid dual GIP/GLP-1 agonist with a similar albumin-binding strategy. Liraglutide is a 31-amino-acid analogue with a C16 fatty acid. Retatrutide is a 39-amino-acid triple agonist that adds glucagon receptor activity.

Those differences are not marketing detail. They change the molecular mass, the hydrophobicity, the purification challenge, and the analytical method. A laboratory that writes one generic “GLP-1 agonist” specification and applies it to all four will mis-specify at least three of them.

The first procurement step is therefore to name the molecule, the sequence, and the declared salt form. A catalog listing that says “GLP-1” without a compound name is not a specification. A certificate that does not repeat the sequence is not a lot record.

## Molecule-by-molecule sourcing differences

| Molecule | Approximate mass | Structural feature | Analytical implication |
| --- | --- | --- | --- |
| Semaglutide | About 4,114 Da | 31 residues; Aib substitution; C18 diacid via linker | Hydrophobic tail drives late elution and strong MS adducts |
| Tirzepatide | About 4,813 Da | 39 residues; dual GIP/GLP-1 agonist; fatty acid chain | Larger molecule; more charge states; impurity profile differs |
| Liraglutide | About 3,751 Da | 31 residues; C16 fatty acid | Lower mass; different retention and solubility |
| Retatrutide | Molecule-specific | 39 residues; GIP/GLP-1/glucagon triple agonist | Method transfer required; do not assume a semaglutide method |

The masses above are approximate and depend on the salt form and the presence of counterions. The exact theoretical mass should come from the sequence and the declared modifications, not from a catalog title. PubChem lists semaglutide at a molecular weight of about 4,114 and tirzepatide at about 4,813; the certificate should state whether the reported value is monoisotopic or average.

The fatty-acid chain is the part that makes these molecules difficult. It increases hydrophobicity, promotes albumin binding, and can produce carryover and adducts in mass spectrometry. A method that works for an unmodified peptide may not resolve the acylated species from its des-acyl impurity. The [HPLC versus LC-MS comparison](/blog/hplc-vs-lc-ms-peptides/) explains why the method choice changes the result.

## API, finished material, and research-grade lots

Three product types appear in sourcing conversations, and they are not interchangeable.

An API is an active pharmaceutical ingredient manufactured under a quality system, usually ICH Q7 for chemical APIs. A finished product is a formulated medicine with excipients, a container, and a label approved by a regulator. A research-grade lot is material sold for laboratory use, often released against a supplier specification rather than a pharmacopeial monograph.

Research laboratories usually buy the third type. That does not make the lot inferior, but it changes the evidence package. A research-grade certificate may report purity, identity, water, and counterion without the full batch record, stability data, or impurity identification that an API buyer would expect. The buyer should decide which of those records the study needs before comparing prices.

A supplier that presents research material as a finished drug, or implies that a catalog lot is approved for human use, is making a claim the documents do not support. The [research-grade specification guide](/blog/research-grade-peptides-2026-lab-procurement-guide/) sets out the evidence tiers.

## Purity and impurity expectations for a GLP-1 batch

Purity by reverse-phase HPLC is the first number buyers compare, and it is the least standardized. A result of 98% by area at 220 nm means that 98% of the integrated UV signal came from the main peak under that method. It does not mean 98% of the mass is peptide, and it does not identify the impurities that make up the remaining 2%.

For a GLP-1 analogue, the impurities worth asking about are the ones the chemistry predicts: deletion and truncation sequences from incomplete coupling, des-acyl species from incomplete acylation, oxidation products, and isomers from aggregation or rearrangement. The [impurity review](/blog/why-impurities-affect-clinical-study-outcomes/) explains why an unidentified impurity is a variable in a study, not a cosmetic defect.

A practical buyer specification for research material includes purity of at least 98% by area, individual related substances below a stated limit, total related substances below a stated limit, identity by mass with a tolerance, water content, counterion, and net peptide content. The exact limits are a risk decision. The important part is that they are written down before the lot is quoted.

ICH Q3A(R2) provides a useful reference for how regulatory systems treat impurity thresholds, including reporting, identification, and qualification limits. Those thresholds apply to drug substances under a regulatory framework, not to research-grade catalog lots, but they give a buyer a vocabulary for asking which impurities were identified and at what level.

## Assay and content: the milligram label is not a milligram of peptide

A 5 mg vial contains 5 mg of material. The peptide mass is lower, because the material includes water and counterion. For a strongly basic, acylated peptide, the counterion fraction can be several percentage points.

Content arithmetic:

Peptide mass (mg) = fill mass (mg) × net peptide content (%) ÷ 100

Price per milligram of peptide = vial price ÷ peptide mass (mg)

The second formula is the only fair price comparison across suppliers. A 5 mg vial at 85% content contains 4.25 mg of peptide. A 5 mg vial at 92% content contains 4.6 mg. At the same price, the second is about 8% cheaper per milligram of peptide, before any difference in purity or documentation is considered.

Assay is a separate measurement from content. An assay by HPLC compares the sample response with a reference standard and reports the potency of the peptide present. Content by mass balance reports the fraction of the fill mass that is peptide. A certificate that reports one but labels it as the other is not auditable.

## Documentation for a GLP-1 lot

| Document | Minimum content | Why the buyer needs it |
| --- | --- | --- |
| Certificate of analysis | Product, sequence, lot, methods, results, limits, approver, date | Ties the lot to a specification |
| Identity record | Theoretical and observed mass, charge states, method | Confirms the molecule, not just the family |
| Purity record | Chromatogram, column, gradient, wavelength, integration | Allows a method review |
| Content record | Water, counterion, net peptide, basis | Converts fill mass to peptide mass |
| Endotoxin record | Method, limit, numeric result | Required for cell-based work |
| Sterility record | Method, sample size, result | Required when the process claim matters |
| Storage and shipping record | Temperature condition, date, handling | Supports the stability chain |
| Safety data sheet | Handling and disposal information | Required by most institutions |

A certificate that reports “GLP-1 agonist, 99%” without the sequence and the lot-specific methods fails the first row. A certificate that reports a purity but no content fails the fourth. The [COA verification guide](/blog/coa-verified-peptides-wholesale-2026-sourcing-verification-guide/) explains how to cross-check the fields against the packing list and label.

## Cold chain and shipping

Lyophilised peptide is more stable than a solution, but it is not indestructible. Heat, moisture, and repeated temperature cycling degrade the material. Shipping conditions should match the storage condition on the certificate, and the shipment should include a temperature indicator or logger for international orders.

For a lyophilised lot, a common storage condition is −20 °C for long-term use, with short-term handling at 2–8 °C. For a reconstituted solution, the storage condition depends on the compound and the buffer, and it should be defined by the laboratory, not assumed from the catalog. The [stability and handling guide](/blog/peptide-lyophilization-reconstitution-guide-for-researchers/) covers the general sequence.

Customs and import documentation are a separate risk. The invoice should describe the goods specifically, with the compound name, quantity, and declared value. A line that says “peptide sample” creates a classification and traceability problem. The [customs documentation guide](/blog/research-peptide-customs-clearance-a-professional-b2b-sourcing-guide-2026/) covers the field-level requirements, and the [HS code guide](/blog/hs-code-for-peptides/) explains why classification is molecule-specific.

## First-batch verification workflow

A first order should be treated as a qualification batch, not as inventory. The workflow below keeps the evidence together.

1. Write the specification before requesting the quote: molecule, sequence, salt form, fill mass, purity, identity, content, endotoxin, sterility if needed, and documents.
2. Request a lot-specific certificate and confirm that the lot code will match the shipment.
3. On receipt, photograph the labels beside the packing list and check the lot, fill mass, and quantity.
4. Draw at least three vials from different positions; retain two unopened.
5. Commission identity and purity testing from a laboratory with a relevant scope.
6. Compare the observed mass and chromatogram with the certificate, not just the summary number.
7. Calculate peptide mass per vial and price per milligram of peptide.
8. Record the results in a supplier qualification file before placing a repeat order.

The [manufacturer verification protocol](/blog/china-peptide-manufacturer-verification-a-2026-b2b-sourcing-protocol/) covers the site-level questions that sit behind this workflow. The [documentation package guide](/blog/peptide-documentation-package/) lists the records to request for a full review.

## Commercial terms and MOQ

GLP-1 analogues are longer and more heavily modified than short research peptides, so the synthesis and purification cost per gram is higher, and the minimum order quantity is often set by batch economics rather than by catalog policy. A supplier that quotes a very low price per milligram for a 5 mg vial may be spreading a batch cost across a large number of vials, or may be selling material with a different specification.

Ask for the price at two or three fill masses, the lead time from purchase order to dispatch, and the terms for a failed retest. A quote that does not state the fill mass, content basis, or retest policy is not comparable to one that does. The [bulk ordering guide](/blog/how-to-buy-peptides-in-bulk-a-2026-direct-to-manufacturer-sourcing-protocol/) covers the volume side of the negotiation.

For a laboratory that expects repeat orders, a blanket purchase order with a fixed specification and a defined release schedule is often better than a series of one-off orders. The [blanket purchase order guide](/blog/how-blanket-purchase-orders-work-peptides/) explains the mechanics.

## The Author's Take

**Position.** I would not compare GLP-1 agonist quotes until each supplier has stated the molecule, the salt form, the net peptide content, and the lot-specific test panel. A price per vial without those four facts is not a price for the same product.

**Reasoning.** These molecules differ enough that a generic specification is almost always wrong for at least one of them. The fatty-acid chain changes the analytical behavior, the counterion changes the peptide mass, and the impurity profile changes with the synthesis route. Buyers who reduce the comparison to a purity percentage end up choosing between numbers that were produced by different methods on different molecules. The suppliers worth keeping are the ones who answer a specification request with a lot file, because that file is what makes a repeat order comparable. The cost of that discipline is a slower first purchase. The cost of skipping it is a study that cannot be repeated.

**Disclosure.** Peptides of China sells research peptides. This article is a sourcing and documentation judgment, not an effects claim or a therapeutic recommendation. Products are supplied for laboratory research use only and are not for human or veterinary use.

## Sources

1. Lau J, Bloch P, Schäffer L, et al. Discovery of the Once-Weekly Glucagon-Like Peptide-1 (GLP-1) Analogue Semaglutide. Journal of Medicinal Chemistry. 2015;58(18):7370–7380. https://doi.org/10.1021/acs.jmedchem.5b00726
2. PubChem, Semaglutide, CID 56843331. https://pubchem.ncbi.nlm.nih.gov/compound/56843331
3. PubChem, Tirzepatide, CID 166567236. https://pubchem.ncbi.nlm.nih.gov/compound/166567236
4. PubChem, Liraglutide, CID 16134956. https://pubchem.ncbi.nlm.nih.gov/compound/16134956
5. European Medicines Agency, Ozempic EPAR. https://www.ema.europa.eu/en/medicines/human/EPAR/ozempic
6. ICH Q3A(R2), Impurities in New Drug Substances (2006). https://database.ich.org/sites/default/files/Q3A%28R2%29%20Guideline.pdf
7. ICH Q6A, Specifications: Test Procedures and Acceptance Criteria (1999). https://database.ich.org/sites/default/files/Q6A%20Guideline.pdf
8. USP &lt;1058&gt;, Analytical Instrument Qualification. https://doi.org/10.31003/uspnf_m1124_10101_01
9. D'Hondt M, et al. Related impurities in peptide medicines. Journal of Pharmaceutical and Biomedical Analysis. 2014;101:2–30. https://doi.org/10.1016/j.jpba.2014.06.012

For compound-specific procurement notes, see the [semaglutide sourcing guide](/blog/semaglutide-wholesale-supplier-guide-direct-to-manufacturer-sourcing-in-2026/) and the [tirzepatide sourcing guide](/blog/tirzepatide-wholesale-sourcing-a-2026-b2b-procurement-guide/). For the analytical panel, see [peptide quality testing](/peptide-quality-testing/). Catalog listings are in the [catalog](/catalog/), including [semaglutide](/catalog/semaglutide/) and [tirzepatide](/catalog/tirzepatide/).
