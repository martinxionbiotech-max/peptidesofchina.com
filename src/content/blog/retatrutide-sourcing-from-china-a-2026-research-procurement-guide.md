---
title: "Retatrutide Sourcing from China: A 2026 Procurement Guide"
slug: "retatrutide-sourcing-from-china-a-2026-research-procurement-guide"
description: "A research-use procurement guide for retatrutide from China: specification fields, batch documents, analytical checks, payment terms, and supplier red flags."
author: "POC Tech Team"
updated: "2026-11-23"
---
Retatrutide is one of the harder research peptides to buy well, not because listings are scarce but because the material has no pharmacopoeial monograph and no approved finished product to compare against. A buyer cannot open a pharmacopoeia, read the retatrutide entry, and hold a supplier to it. The specification has to be built from the batch documents, the analytical package, and the intended research use. That is the work this guide covers.

The procurement sequence that follows is written for laboratory and institutional buyers ordering research-use material from China. It treats retatrutide as an investigational compound, not as a medicine, and it avoids the clinical claims that make sourcing pages unreliable. The focus is on the four things a buyer can actually control: the definition of the material, the documents attached to the lot, the analytical results that support release, and the commercial terms that determine what happens when a result misses.

## Why retatrutide is a harder purchase than a catalog peptide

Retatrutide, also called LY3437943, is an investigational triple agonist at the GIP, GLP-1, and glucagon receptors. The discovery work and early clinical rationale were published by Coskun and colleagues in *Cell Metabolism* in 2022, and the phase 2 obesity trial was reported in the *New England Journal of Medicine* in 2023. Those papers establish the research context. They do not establish a compendial specification, a release panel, or an accepted purity method for the material sold as retatrutide.

That gap matters at the purchasing desk. For a peptide with a monograph, the buyer can point to a public standard and ask whether the lot meets it. For retatrutide, the buyer has to ask a different set of questions: what sequence was synthesized, what modification is present, what counterion remains, how the purity was measured, and which lot the certificate describes. Each answer is supplier-specific, and each one belongs in the purchase record before payment.

There is a second complication. The name "retatrutide" is used across listings for material that may differ in fill mass, counterion, purity method, and documentation depth. A 10 mg vial is not a specification; it is a fill size. A ≥98% figure is not a specification either, unless the method, wavelength, gradient, and integration rule are stated. Buyers who compare listings on price alone are comparing numbers that were produced under different conditions, which is not a comparison at all.

## Define the material before you request a quote

The most useful thing a buyer can do is freeze a specification before the first email. A supplier can meet a written specification or decline it; it cannot meet a sentence that says "high purity retatrutide." The fields below are the minimum worth putting into a request for quotation, even if the final order uses the supplier's format.

| Field | What to write in the request | Why it prevents a dispute |
|---|---|---|
| Sequence and modification | Full amino-acid sequence, plus any acylation, fatty-acid chain, or terminal modification | The common name does not define the molecule; the sequence does |
| Counterion | Trifluoroacetate or acetate, with the target residual level | Counterion content changes net peptide mass and handling behavior |
| Form and fill | Lyophilized powder, nominal fill mass per vial, number of vials per kit | Fill mass is not the same as peptide content |
| Purity method | RP-HPLC, column and gradient, detection wavelength, integration rule | A percentage without a method cannot be reproduced |
| Identity method | LC-MS or MALDI-TOF, mass mode, tolerance in ppm or Da | Confirms that the main peak is the intended sequence |
| Water content | Karl Fischer titration with an acceptance limit | Residual moisture affects stability and weighing |
| Net peptide content | Amino-acid analysis or nitrogen determination, with method | Corrects for counterion, water, and salt mass |
| Microbiological attributes | Endotoxin method and limit where the study requires it; sterility or bioburden statement | Purity does not cover pyrogen or bioburden risk |

Two fields are routinely omitted. Net peptide content matters because a vial labeled 10 mg may contain 10 mg of total powder, not peptide, once counterion and water are counted. Mass mode matters because an intact mass reported as a bare number cannot be checked against a theoretical value.

## The document set that makes a batch auditable

A certificate of analysis is the summary. The audit trail is the set of records behind it. For a research peptide without a monograph, the difference between the two is the difference between a claim and evidence.

Ask for the following documents for the specific lot, not for the product family:

- A certificate of analysis that names the product, the lot, the sequence or specification reference, the test methods, the acceptance limits, the results, the release date, and the signatory.
- The chromatogram behind the purity result, with the method header, injection volume, gradient table, wavelength, and peak integration report.
- The mass spectrum behind the identity result, with the observed mass, the calculated mass, the mass mode, and the instrument type.
- Karl Fischer water content, with the sample size and result.
- Counterion identity and content, by ion chromatography or an equivalent method.
- Net peptide content by amino-acid analysis or nitrogen determination, where the supplier offers it.
- Endotoxin result by LAL or rFC, with the method, the limit, the dilution, and spike recovery, when the study requires a pyrogen limit.
- A batch record extract or manufacturing summary that ties the lot to a production date and a site.

The lot number makes the rest usable. A certificate with no lot number, or one that does not match the vial label, cannot be linked to the material in hand. A certificate naming a different legal entity than the invoice is a second warning.

| Document | Minimum content | What it proves | What it does not prove |
|---|---|---|---|
| Certificate of analysis | Product, lot, method, limit, result, date, signatory | That a defined release decision was recorded | That the result belongs to your vial, unless the lot matches |
| HPLC chromatogram | Method header, gradient, wavelength, integration | That a separation was run and how purity was calculated | That co-eluting impurities are absent |
| Mass spectrum | Observed and calculated mass, mass mode, tolerance | That the main component matches the expected mass | That the sequence is correct at every residue |
| Water content | Karl Fischer method and result | Residual moisture at release | Long-term stability under your storage conditions |
| Batch record extract | Lot, scale, dates, deviation summary | That the lot has a manufacturing history | That the process is validated for your use |

The [documentation package guide](/blog/peptide-documentation-package/) sets out a fuller version of this list, and the [COA authentication guide](/blog/coa-verified-peptides-supplier-how-to-authenticate-research-purity-in-2026) explains how to reconcile the certificate with the invoice and the vial.

## Analytical checks and acceptance criteria

The release panel for a research peptide usually combines separation, identity, content, and water.

Reversed-phase HPLC is the standard purity method. A typical method runs a C18 column with a water/acetonitrile gradient containing 0.1% trifluoroacetic acid, detects at 214 or 220 nm, and reports purity by area normalization. The method header should state the column dimensions, particle size, flow rate, gradient table, column temperature, injection volume, and integration parameters. Without those fields, a purity number cannot be reproduced or compared.

System suitability is the check that the method worked before the sample was injected. Common criteria include a minimum plate count, a resolution between the main peak and the nearest impurity, a tailing factor, and a relative standard deviation across replicate injections. The limits are method-specific; the principle is not.

Mass spectrometry answers identity. For an intact peptide, LC-ESI or MALDI-TOF can confirm that the observed mass matches the calculated mass within the platform's tolerance. The certificate should state the mass mode and the tolerance. A MALDI result at ±1 Da and an Orbitrap result at 5 ppm are not equivalent without conversion to the same basis. The [HPLC and LC-MS comparison](/blog/hplc-vs-lc-ms-peptides/) covers the trade-offs between the two techniques.

Water content is measured by Karl Fischer titration. High residual moisture raises the risk of degradation or aggregation during shipping. A common release limit is ≤5.0% water, but the appropriate limit depends on the peptide and the storage condition. The number belongs on the certificate, not in an inference from the cake.

Endotoxin is a separate attribute. USP &lt;85&gt; describes the bacterial endotoxins test, including the limulus amebocyte lysate methods and the calculation of the maximum valid dilution. A result reported only as "pass" is incomplete for audit purposes; the buyer needs the method, the limit, the numeric value, and the spike recovery at the reported dilution. The [endotoxin testing guide](/blog/endotoxin-testing-peptide-manufacturing/) explains why low-endotoxin recovery can produce a false pass.

## Manufacturer, trader, or platform: what each can document

The entity that signs the quotation is not always the entity that made the peptide. Three models are common, and they differ in what they can prove.

A manufacturer controls the synthesis, purification, lyophilization, and release testing. It can produce a batch record, a chromatogram, a mass spectrum, and a deviation log because those documents are by-products of production. A manufacturer may still trade other suppliers' material, so the buyer should ask which site made the lot and whether the certificate was issued by that site.

A trader buys and resells. It may hold genuine certificates, but it cannot always produce a batch record extract or answer a technical question about a coupling cycle. The useful test is whether the chain of custody is documented. Ask for the manufacturing site, the lot number, and the certificate issuer, and check that the three agree.

A sourcing platform coordinates the order, specification, and logistics without owning the factory. Peptides of China operates in this role. The distinction tells the buyer which questions the platform can answer and which require manufacturer documents or independent analysis. A platform that presents itself as the manufacturer when it is not has created a documentation problem before the first shipment.

The [manufacturer verification protocol](/blog/china-peptide-manufacturer-verification-a-2026-b2b-sourcing-protocol) lists the site-level questions worth asking, including equipment, capacity, water systems, and QC scope. The [quality testing hub](/peptide-quality-testing/) explains how the individual tests fit into a supplier qualification.

## Commercial terms: MOQ, payment, and Incoterms

The commercial terms decide what happens when a batch misses the specification. They deserve the same attention as the analytical panel.

The catalog minimum for Peptides of China is USD 600, and standard orders normally begin with one 10-vial kit per product. Buyers who need a larger lot should ask for a quotation with a defined batch size, lead time, and release date.

Payment structure matters most on a first order. A common split is a deposit against the purchase order and the balance against the pre-shipment inspection record or shipping documents. The exact split is negotiable; the principle is not: do not pay in full before the lot documents exist. Where a letter of credit is used, UCP 600 governs. The bank has five banking days after presentation to examine the documents, and the beneficiary must present within 21 calendar days after shipment unless the credit states otherwise.

Incoterms decide where risk transfers. Under FOB, the buyer's risk begins when the goods are on board the vessel. Under CIF, the seller arranges carriage and insurance but risk still passes at shipment. Under DAP, the seller delivers to the named place and the buyer handles import clearance. Under DDP, the seller takes on import clearance and duty. A research buyer importing a peptide for laboratory use should choose the term that matches who is the importer of record, because that entity is responsible for the declaration. The [customs documentation guide](/blog/research-peptide-customs-clearance-a-professional-b2b-sourcing-guide-2026) covers the invoice and packing-list fields that cause delays.

| Term | Risk transfers | Who arranges main carriage | Who clears import | Practical note for a lab |
|---|---|---|---|---|
| FOB | When goods are on board | Buyer | Buyer | Buyer needs a forwarder and a broker |
| CIF | When goods are on board | Seller | Buyer | Insurance is included, but risk is still at origin |
| DAP | At the named destination | Seller | Buyer | Seller delivers; buyer still owns the import declaration |
| DDP | At the named destination, duty paid | Seller | Seller | Convenient, but the buyer may lose visibility of the declaration |

## Shipping and import documentation

A lyophilized peptide is not a frozen protein, but it is still sensitive to heat, light, and moisture. The quotation should describe the shipping configuration: vial format, secondary packaging, desiccant, insulated container, and any temperature monitor. A buyer who receives a broken cake or visible moisture should quarantine the vial and photograph the packaging before opening a ticket.

The import documents should tell one story. The invoice should name the product in a way that matches the certificate, state quantity and unit value, identify seller and buyer, and state origin. The packing list should reconcile vial, kit, and carton counts. The certificate should carry the same lot number as the vial label, and the air waybill should match the invoice value and Incoterm.

Tariff classification is a separate decision. Peptides can fall under different headings depending on chemical nature and end use, and a code that fits one product may not fit another. The importer of record should obtain a classification decision from a broker or, where available, a binding ruling. A supplier's suggestion is not a ruling. Origin marking follows the same logic: 19 CFR Part 134 sets the U.S. requirements, and the origin on the invoice should match the marking.

No supplier can promise that a shipment will clear customs. What a supplier can do is provide consistent documents, a truthful declaration, and a route for a reshipment or a refund if the shipment is refused. Those commitments belong in the order confirmation.

## Supplier questions and red flags

A short list of questions separates a supplier with a quality system from one with a good sales page.

1. What is the exact sequence and modification of the lot?
2. Which site manufactured it, and who issued the certificate?
3. What is the lot number, and does it appear on the vial label?
4. What is the HPLC method, including column, gradient, wavelength, and integration rule?
5. What is the mass method, mass mode, and tolerance?
6. What are the water content and net peptide content?
7. Can you provide a redacted batch record extract and a deviation summary?
8. What happens if an independent test misses the specification?
9. Who is the importer of record under the quoted Incoterm?
10. Can you provide a second lot's documents in the same format?

Red flags are consistent. A certificate with no lot number. A purity claim of 99.9% with no chromatogram. A mass value with no mass mode. A supplier who offers to describe the goods as something else on the invoice. A payment instruction that changes at the last minute. A refusal to name the manufacturing site. A certificate that is dated before the batch was produced. None of these is proof of fraud on its own, but each one shifts risk to the buyer.

## The Author's Take

**Position.** For an investigational peptide like retatrutide, the buyer is not purchasing a molecule name. The buyer is purchasing a batch with a documentary identity, and the supplier's ability to describe that identity is the product.

**Reasoning.** There is no monograph to fall back on and no approved product to compare against, so every acceptance decision rests on documents the supplier controls. That makes the document set the real specification. A supplier that can name the sequence, the counterion, the method, the lot, and the deviation history has given the buyer something testable. A supplier that can only quote a purity percentage has given the buyer a number that cannot be reproduced. The price difference between those two suppliers is usually smaller than the cost of repeating a study on a batch that cannot be identified.

**Disclosure.** Peptides of China sells research peptides and coordinates sourcing from manufacturing partners. This article describes procurement and documentation judgment, not an effects claim, a dosing guide, or medical advice. Products referenced on this site are supplied for laboratory research use only and are not for human or veterinary use. Analytical documentation varies by product and batch, and buyers who require independent confirmation should arrange third-party testing after receipt.

## Sources

1. Coskun T, Urva S, Roell WC, et al. LY3437943, a novel triple glucagon, GIP, and GLP-1 receptor agonist for glycemic control and weight loss: From discovery to clinical proof of concept. *Cell Metabolism*. 2022. https://pubmed.ncbi.nlm.nih.gov/35985340/
2. Jastreboff AM, Aronne LJ, Ahmad NN, et al. Triple-Hormone-Receptor Agonist Retatrutide for Obesity — A Phase 2 Trial. *New England Journal of Medicine*. 2023;389(6):514–526. https://pubmed.ncbi.nlm.nih.gov/37366315/
3. ClinicalTrials.gov. A Study of Retatrutide (LY3437943) in Participants With Obesity (TRIUMPH-1). NCT05882045. https://clinicaltrials.gov/study/NCT05882045
4. U.S. Food and Drug Administration. Bioanalytical Method Validation: Guidance for Industry (2018). https://www.fda.gov/regulatory-information/search-fda-guidance-documents/bioanalytical-method-validation-guidance-industry
5. International Council for Harmonisation. ICH Q2(R2): Validation of Analytical Procedures (2023). https://database.ich.org/sites/default/files/ICH_Q2%28R2%29_Guideline_2023_1130.pdf
6. International Council for Harmonisation. ICH Q6B: Specifications — Test Procedures and Acceptance Criteria for Biotechnological/Biological Products. https://database.ich.org/sites/default/files/Q6B%20Guideline.pdf
7. United States Pharmacopeia. USP &lt;621&gt; Chromatography. https://www.usp.org/usp-nf
8. United States Pharmacopeia. USP &lt;85&gt; Bacterial Endotoxins Test. https://www.usp.org/usp-nf
9. International Chamber of Commerce. UCP 600: Uniform Customs and Practice for Documentary Credits. https://iccwbo.org/business-solutions/trade-finance/
10. U.S. Customs and Border Protection. 19 CFR Part 134 — Country of Origin Marking. https://www.ecfr.gov/current/title-19/chapter-I/part-134
