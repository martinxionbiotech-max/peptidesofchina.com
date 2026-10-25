---
title: "Amino Acid Coupling Efficiency: The Manufacturing Metric Behind Peptide Purity"
slug: "what-is-amino-acid-coupling-efficiency"
description: "Discover the importance of amino acid coupling efficiency in solid-phase peptide synthesis, and learn how it impacts your peptide yields."





---
This guide examines what is amino acid coupling efficiency from the perspective of a **china peptide** buyer. For researchers and resellers sourcing **chinese peptides**, the practical questions are the same regardless of compound: who manufactured the vial, what the batch documentation shows, and whether the specification matches the listing. We answer those questions below.

Amino acid coupling efficiency is the percentage of resin-bound peptide chains that successfully acquire a new amino acid residue in a single synthesis cycle during solid-phase peptide synthesis (SPPS). The [classic SPPS literature](https://pubmed.ncbi.nlm.nih.gov/2134063/) established two operational thresholds that remain the standard reporting benchmark: couplings at or below 99% per cycle are classified as “incomplete,” and those at or below 98% are classified as “high incomplete.” These are not absolute pass/fail cutoffs but widely adopted conventions for flagging when a coupling step needs intervention.

A single-cycle coupling rate just under [100%](https://pubs.acs.org/doi/10.1021/la802864v) compounds over long sequences, substantially reducing the theoretical maximum full-length yield for sequences with many residues. Deletion sequences, truncated chains, and racemized species fill the gap, and they all appear in the crude product. For long or complex targets, even a modest and consistent shortfall in per-cycle efficiency can dominate crude purity and complicate downstream purification.

- Single-cycle coupling efficiency is measured as the proportion of resin-bound chains that successfully incorporate the amino acid in one cycle.
- Literature thresholds classify couplings at or below about 99% as incomplete and at or below about 98% as highly incomplete.
- Compounding effect: a 98% per-cycle rate across a 30-mer yields roughly 55% full-length product theoretically
- Monitoring and intervention at each cycle, not just at the end, is the only reliable control strategy

---

## Key Takeaways

| Point | Details |
| --- | --- |
| Definition and thresholds | Coupling efficiency is percent conversion per cycle; ≤99% = incomplete, ≤98% = high incomplete per classic SPPS literature. |
| Compounding effect | A 98% per-cycle rate across a 30-mer yields roughly 55% theoretical full-length product; monitor every cycle for long sequences. |
| Top monitoring methods | Kaiser/chloranil colorimetric tests, Fmoc UV quantitation, and test-cleavage LC-MS each serve different resolution and speed needs. |
| Most effective fixes | Verify deprotection first, then upgrade to HATU/HOAt, double-couple with fresh reagents, or apply microwave assistance for resistant positions. |
| Supplier and QC requirements | Require per-cycle monitoring logs, lot-specific resin data, test-cleavage HPLC/MS, and independent COA verification from any synthesis supplier. |

---

## Table of Contents

- How coupling efficiency is defined and calculated
- What is the mechanism of activation and what side reactions reduce efficiency?
- Which coupling reagents and additives give the best results?
- What physical and sequence factors reduce coupling efficiency?
- How do you measure and monitor coupling efficiency in practice?
- How can you improve single-cycle coupling efficiency?
- How does coupling efficiency affect crude purity and batch records?
- Choosing suppliers who protect coupling efficiency at scale
- The gap between per-cycle numbers and manufacturing reality
- Sources

## How coupling efficiency is defined and calculated

Coupling efficiency, in the SPPS context, is a per-cycle metric. It measures the fraction of free N-terminal amines on the resin that are converted to amide bonds with the incoming protected amino acid in a single activation and coupling step. The formula is straightforward:

**Percent coupling efficiency = [(free amines before coupling − free amines after coupling) / free amines before coupling] × 100**

A worked example makes the compounding effect concrete. Assume a 15-residue target synthesized at a consistent 98% single-cycle rate. After the first coupling, 98 of every 100 chains carry the correct residue. After the second, 96.04 chains do. By residue 15, the theoretical full-length population is 0.98¹⁵, or approximately 74%. In practice, crude purity is also affected by racemization and side-chain deprotection artifacts, so the real full-length fraction is typically lower than the theoretical maximum.

Reporting conventions vary by lab, but a complete batch record for a coupling step should capture:

- Amino acid identity, lot number, and equivalents used
- Activating reagent and additive, with lot numbers and equivalents
- Solvent system and volume relative to resin mass
- Resin identity, lot, and loading (mmol/g)
- Coupling time and temperature
- Monitoring test used and result (colorimetric score, UV absorbance, or LC-MS percent conversion)
- Any corrective actions taken (recoupling details, reagent changes)

Cumulative yield across the full sequence is a separate metric, calculated as the product of all per-cycle efficiencies. Labs that report only final crude purity lose the per-cycle resolution needed to identify which residue positions are problematic. Per-cycle monitoring, logged against the batch record, is the only way to build a traceable picture of where efficiency is lost.

---

## What is the mechanism of activation and what side reactions reduce efficiency?

The amino acid coupling mechanism in SPPS begins with activation of the carboxyl group of the incoming protected amino acid. With carbodiimide reagents such as DCC or DIC, this produces an O-acylisourea intermediate, a highly reactive species that can acylate the resin-bound amine directly. The problem is that O-acylisourea is also prone to two competing reactions that reduce apparent coupling efficiency.

The first is rearrangement to N-acylurea, an irreversible side reaction that consumes the activated amino acid without forming a peptide bond. [Carbodiimide activation](https://organic-synthesis.com/acid-amine-coupling-using-dcc/) is well-documented to produce this byproduct, particularly when the O-acylisourea is not intercepted quickly. The second is oxazolone formation, which occurs when the activated carbonyl cyclizes with the backbone amide nitrogen of the preceding residue. Oxazolones are prone to racemization because the alpha-carbon becomes acidic under basic conditions, and the resulting epimeric mixture is difficult to remove by HPLC.

N-hydroxy additives, specifically HOBt, HOAt, and Oxyma (ethyl cyano(hydroxyimino)acetate), intercept the O-acylisourea to form a more stable active ester. This interception chemistry reduces N-acylurea formation and suppresses racemization by shortening the window during which oxazolone can form. HOAt is generally considered more effective than HOBt at suppressing racemization because its proximity effect positions the active ester for faster aminolysis. Oxyma has largely replaced HOBt in many labs due to HOBt’s explosive classification at certain concentrations.

Additional side reactions to monitor:

- Hydrolysis of the active ester, consuming the activated species before it can acylate the resin
- Diketopiperazine (DKP) formation, particularly at dipeptide stages involving Pro or Gly at the C-terminus
- Aspartimide formation at Asp residues under prolonged basic conditions
- Incomplete deprotection of the preceding residue’s Fmoc group, which blocks the amine and registers as a coupling failure even when the coupling reagent is functioning correctly

The role of DIPEA (N,N-diisopropylethylamine) is to maintain a mildly basic environment that keeps the resin-bound amine nucleophilic without promoting racemization. Too little base leaves the amine partially protonated; too much accelerates aspartimide formation and can promote oxazolone racemization.

**Pro Tip:** *Watch active-ester lifetime carefully. For residues with fast-hydrolyzing active esters, extending coupling time past the point of ester stability increases hydrolytic loss rather than conversion. Kinetic data from time-resolved NMR studies categorize active esters as fast-hydrolyzing (t < 6 h), slowly hydrolyzing (6–24 h), or non-hydrolyzing (>24 h), and coupling times should be matched to that profile rather than defaulted to a fixed protocol.*

---

## Which coupling reagents and additives give the best results?

Reagent selection is one of the most consequential decisions in SPPS protocol design. The major classes differ in activation speed, racemization risk, byproduct handling, and compatibility with automated synthesizers.

Carbodiimides (DCC, DIC, EDC) are the classical activators. DCC produces a dicyclohexylurea byproduct that precipitates in DCM but remains insoluble in DMF, complicating filtration in solution-phase work. DIC generates a diisopropyl urea that is more soluble and easier to wash away, making it the preferred carbodiimide for Fmoc SPPS. EDC is water-soluble and used primarily for aqueous coupling or surface conjugation, not standard resin-based synthesis. All three require an additive (HOBt, HOAt, or Oxyma) to suppress N-acylurea formation and racemization.

Uronium and phosphonium reagents (HATU, HBTU, TBTU) pre-activate the amino acid more rapidly and are generally faster than carbodiimides. HATU, paired with DIPEA in DMF, is widely regarded as the most efficient activator for difficult couplings and is the standard choice for automated Fmoc SPPS. HBTU and TBTU are slightly less reactive and carry a lower racemization risk in some contexts, making them useful when sequence sensitivity is a concern. The key operational constraint with uronium reagents is that they must not contact the free amine before activation is complete, or guanidinylation of the resin occurs, capping chains permanently.

| Reagent class | Typical coupling efficiency | Racemization risk | Recommended equivalents / time | Common side products | Typical solvent / base |
| --- | --- | --- | --- | --- | --- |
| DIC + Oxyma | High (>99% for most residues) | Low | 3–5 eq / 30–60 min | Diisopropyl urea (washable) | DMF / DIPEA |
| DCC + HOBt | High | Low–moderate | 3–5 eq / 30–60 min | Dicyclohexylurea (filtration needed) | DMF or DCM / DIPEA |
| HATU + DIPEA | Very high (fastest activation) | Low with correct base | 3–4 eq / 5–20 min | Guanidinylation if premixed | DMF / DIPEA |
| HBTU + HOBt | High | Low | 3–5 eq / 20–45 min | Guanidinylation risk lower than HATU | DMF / DIPEA |
| TBTU + HOBt | Moderate–high | Low | 3–5 eq / 30–60 min | Similar to HBTU | DMF / DIPEA |
| EDC + HOBt | Moderate (aqueous context) | Moderate | 3–5 eq / 60 min | Water-soluble urea | Aqueous buffer / NMM |

Oxyma has become the additive of choice in many facilities because it matches HOBt’s suppression of N-acylurea formation without the explosive hazard. HOAt offers a proximity effect that further reduces racemization, particularly valuable for Cys, His, and Arg residues. The base of choice across nearly all Fmoc SPPS protocols is DIPEA, typically at 6–10 equivalents relative to the amino acid.

**Pro Tip:** *For borderline difficult residues, pairing HATU with a short coupling time (10–15 min) and a fresh Oxyma addition is more effective than simply extending the reaction. Longer times with slower activators increase hydrolytic loss and do not compensate for poor diffusion into aggregated resin.*

---

## What physical and sequence factors reduce coupling efficiency?

Coupling efficiency is as much a physical problem as a chemical one. Reagent diffusion into the resin matrix, resin swelling, and on-resin secondary structure formation can each reduce effective coupling rates independently of activator choice.

Resin loading is a primary variable. High loading (above 0.8 mmol/g for most resins) compresses the spacing between chains, reduces effective swelling, and limits reagent diffusion to interior sites. For sequences longer than 20 residues or those with known aggregation tendencies, loading in the 0.2–0.5 mmol/g range generally gives better per-cycle efficiency. The tradeoff is lower absolute yield per gram of resin, which matters at scale but is secondary to sequence integrity in research contexts.

Solvent choice directly affects resin swelling. DMF is the standard solvent for Fmoc SPPS and swells most polystyrene-based resins adequately. NMP (N-methyl-2-pyrrolidone) swells certain resins more effectively and is preferred for aggregation-prone sequences. Mixed solvent systems, such as DMF/DCM or DMF/NMP, can improve diffusion for specific resin types. PEG-based resins (ChemMatrix, TentaGel) swell well in both aqueous and organic solvents and are the standard choice for difficult sequences.

Sequence-dependent aggregation is the most common cause of persistent low coupling efficiency. Beta-sheet-forming motifs, runs of consecutive hydrophobic residues (Val, Ile, Leu), and sequences containing multiple Pro or N-methyl amino acids create secondary structures on-resin that physically block the N-terminal amine from reagent access. A large stepwise SPPS study covering 88 peptides and 696 couplings showed that residue identity, the identity of the acylated residue, and growing chain length are all predictive factors for difficult couplings, meaning that problem positions can often be anticipated before synthesis begins.

Diagnostic checklist for physical coupling failures:

- Run a small-scale test cleavage and LC-MS after a suspect coupling to confirm the failure before recoupling
- Perform a colorimetric test (Kaiser or chloranil) immediately after coupling to detect residual free amines
- Swap DMF for NMP or add DCM to the wash cycle to improve swelling
- Switch to a lower-loading or PEG-based resin for the next attempt
- Incorporate pseudoproline dipeptide building blocks at Ser or Thr positions within aggregation-prone stretches
- Consider backbone protection (Hmb or Dmb groups) at positions that consistently show low efficiency

**Pro Tip:** *Pre-synthesis route planning using residue-pattern libraries from the difficult-coupling literature is more efficient than troubleshooting mid-synthesis. Sequences with three or more consecutive hydrophobic residues, or with Val-Val or Ile-Ile motifs, warrant pseudoproline or backbone protection as a default, not a fallback.*

---

## How do you measure and monitor coupling efficiency in practice?

Three monitoring methods cover the practical range from rapid in-process checks to quantitative percent-conversion data.

The Kaiser test (ninhydrin) is the standard colorimetric method for detecting free primary amines on resin. A blue-purple color indicates incomplete coupling; a yellow color indicates complete acylation. The chloranil test is used for secondary amines (Pro, N-methyl residues) where Kaiser gives a false negative. Both tests are qualitative unless calibrated against a standard curve, but they are fast enough to run between cycles on an automated synthesizer and provide immediate go/no-go information.

Fmoc UV quantitation measures the dibenzofulvene-piperidine adduct released during Fmoc deprotection at 301 nm or 290 nm. Because every Fmoc group released corresponds to one chain that successfully incorporated the previous residue, this method gives a direct per-cycle incorporation count. The calculation:

1. Measure absorbance of the deprotection filtrate at 301 nm
2. Apply Beer-Lambert: moles of Fmoc = (Absorbance × volume) / (ε × path length), where ε ≈ 7,800 L·mol⁻¹·cm⁻¹ at 301 nm
3. Divide by theoretical moles of resin-bound chains (resin mass × loading)
4. Multiply by 100 for percent incorporation

Test cleavage followed by LC-MS or HPLC is the most definitive method. A small aliquot of resin is cleaved, deprotected, and analyzed. The ratio of full-length product peak area to total peak area (including deletion sequences) gives a direct percent conversion for that point in the synthesis. [Real-time monitoring combined with immediate recoupling](https://pubs.rsc.org/en/content/articlehtml/2019/ra/c9ra06124j) when tests flag incomplete coupling consistently outperforms fixed-cycle approaches in final crude purity. Sequence confirmation workflows using LC-MS are covered in detail in the [sequence confirmation guide for clinical peptides](/blog/what-is-sequence-confirmation-clinical-peptides).

Recommended monitoring cadence:

- Every coupling cycle for sequences longer than 20 residues or known difficult sequences
- Every 3–5 cycles for routine short sequences with established protocols
- Mandatory test cleavage + LC-MS after any coupling that fails colorimetric testing
- Full LC-MS analysis of a representative test cleavage before committing to full-scale recoupling

**Pro Tip:** *Run a short test cleavage and LC-MS on a 5–10 mg resin aliquot after any suspected failed coupling before committing to full-scale recoupling. The 30–60 minutes spent on the analysis saves the cost of a full reagent charge and avoids introducing additional side products from unnecessary recoupling cycles.*

---

## How can you improve single-cycle coupling efficiency?

When per-cycle efficiency falls below target, the intervention sequence matters. Applying the wrong fix wastes reagents and can introduce new side products.

1. Verify deprotection completeness first. A failed coupling is sometimes a failed Fmoc removal. Run a Kaiser test immediately after deprotection, before adding the amino acid. If free amines are not detected, repeat deprotection with fresh piperidine/DMF before proceeding.
2. Check reagent freshness and equivalents. HATU and HOAt degrade over time, particularly if exposed to moisture. Verify lot age and storage conditions. Increase equivalents to 5–6 if the standard 3–4 eq protocol is not achieving complete coupling.
3. Improve solvation. Pre-swell the resin in DMF for 30–60 minutes before coupling. For aggregation-prone sequences, switch to NMP or add 20–30% DCM to the coupling solvent.
4. Switch the activator/additive pair. If DIC/Oxyma is not achieving complete coupling, move to HATU/HOAt/DIPEA. The faster activation kinetics of HATU reduce the window for hydrolysis and N-acylurea formation.
5. Double-couple. Add a second full charge of fresh amino acid and activator after the first coupling cycle without washing. This is the most common rescue strategy and is effective when the first coupling achieved 90–97% conversion.
6. Apply heat or microwave assistance. Microwave-assisted SPPS has demonstrated improved coupling efficiency for certain residue classes, particularly at sterically hindered positions. Temperatures of 50–75°C for 5–10 minutes are typical for microwave protocols.

Protocol templates for recoupling:

- Quick recouple: same amino acid and activator, fresh charge, 20–30 min at room temperature. Use when colorimetric test shows partial but not severe incomplete coupling (estimated 90–97% conversion).
- Forced recouple: HATU/HOAt/DIPEA at 5–6 equivalents, 45–60 min, optionally with mild heating (40–50°C). Use when colorimetric test shows severe incomplete coupling or when a quick recouple fails.
- Backbone-protection approach: incorporate Hmb or Dmb backbone protection at the problem position in a redesigned synthesis route. Use when a specific position consistently fails across multiple batches despite reagent and solvent optimization.

Racemization risk increases with extended coupling times and elevated temperatures, particularly for Cys and His. For these residues, shorter recoupling cycles with fresh activator additions are preferable to a single prolonged coupling.

**Pro Tip:** *For expensive or rare amino acids, prefer two short recoupling cycles with fresh activator over one extended cycle. Active-ester hydrolysis accumulates over time, so a 60-minute single coupling with a degraded active ester delivers less conversion than two 20-minute cycles with freshly activated species.*

---

## How does coupling efficiency affect crude purity and batch records?

The relationship between per-cycle efficiency and crude purity is direct and calculable. For a 12-residue target synthesized at a consistent 98% per-cycle rate, the theoretical full-length yield is 0.98¹², or approximately 78.5%. In practice, racemized species and truncated chains from premature capping add to this impurity load, and crude purity is typically lower than the theoretical maximum.

The impurity profile matters for downstream QC. Deletion sequences that differ by only one residue from the target are the hardest to remove by preparative HPLC and the most likely to co-elute with the target peak. Racemized species (D-amino acid diastereomers) are often detectable by chiral HPLC or by characteristic mass shifts in MS/MS fragmentation but require dedicated analytical methods to quantify. A [peptide characterization reporting checklist](/blog/peptide-characterization-reporting-checklist) provides a structured format for capturing these QC elements in batch records.

QC checklist items for each synthesis batch:

- Resin lot number, supplier, loading value (mmol/g), and swelling test result
- Amino acid lot numbers, supplier, and purity certificates
- Reagent lot numbers (activator, additive, base) and age at time of use
- Per-cycle monitoring test results (Kaiser/chloranil score or Fmoc UV absorbance)
- Corrective actions: recoupling details, reagent changes, solvent switches
- Final crude purity by HPLC (percent area at 214 nm or 220 nm)
- MS confirmation of target molecular weight
- Identity of major impurity peaks by MS or MS/MS

Supplier specifications should reflect these parameters. Acceptance thresholds for crude purity, deletion-sequence content, and racemization should be stated explicitly in sourcing contracts, not left to the supplier’s default reporting format. Independent verification, including third-party HPLC traces and MS confirmation, is the only reliable check when the synthesis facility’s in-process monitoring is not directly observable. The [peptide quality assurance guide](/blog/peptide-quality-assurance-process-a-researchers-guide-to-sourcing-integrity) covers the framework for building these verification requirements into procurement workflows.

**Pro Tip:** *Require a runoff test-cleavage LC-MS trace for the first production lot of any new sequence and whenever a new resin lot or synthesis route is introduced. A single HPLC trace with MS confirmation at this stage catches systematic coupling failures before they propagate across a full production run.*

---

## Choosing suppliers who protect coupling efficiency at scale

Coupling efficiency at the bench is a chemistry problem. At production scale, it becomes a process-control and supply-chain problem. The variables that a researcher controls directly in a lab, such as reagent freshness, resin lot selection, and per-cycle monitoring, are delegated to the synthesis facility when peptides are sourced externally. The quality of that delegation determines batch consistency.

Supplier selection criteria focused on coupling efficiency:

- Documented process parameters: the facility should be able to provide written protocols specifying reagent equivalents, coupling times, activator/additive pairs, and solvent systems for each sequence class
- Resin and reagent sourcing transparency: lot numbers, supplier names, and storage conditions for resins and activators should be available on request
- In-process monitoring: the facility should run Kaiser or Fmoc UV checks at defined intervals and log results in batch records
- Willingness to share method validation data: a facility that cannot provide representative in-process monitoring logs or test-cleavage HPLC traces has no verifiable process control

Batch-consistency items to request from any supplier:

- Lot-to-lot resin loading data and swelling test results
- In-process monitoring logs for representative batches (Kaiser/Fmoc UV results per cycle or per defined interval)
- Test-cleavage HPLC and MS data for at least one batch per sequence
- Independent third-party COA with HPLC purity and MS confirmation

Contract language should specify acceptance thresholds explicitly. Sampling plans should specify the number of batches to be tested per lot and the analytical methods to be used.

Peptides of China coordinates sourcing from established Chinese manufacturing facilities together with international logistics. Products are subject to the manufacturer’s applicable quality-control procedures and specifications. Manufacturer-side analytical documentation may be available depending on the product and batch. Peptides of China is not an independent analytical testing laboratory. Peptides of China coordinates sourcing from established Chinese manufacturing facilities together with international logistics. Buyers requiring independent verification may arrange third-party analytical testing. For procurement teams sourcing research-grade peptides such as KPV or [Epithalon](/catalog/epithalon), this means COA-backed HPLC and MS data are standard, not negotiable. Vendor qualification frameworks that translate coupling-efficiency requirements into contract language are covered in the [peptide vendor qualification guide](/blog/china-peptide-manufacturer-verification-a-2026-b2b-sourcing-protocol/).

For biopharma researchers integrating sourced peptides into screening workflows, [drug screening compound handling practices](https://blog.hopeatrarelabs.com/blog/drug-screening-tips-for-biopharma-researchers) provide additional context on how upstream synthesis quality affects downstream assay reliability.

**Pro Tip:** *When evaluating a new synthesis supplier, ask for in-process monitoring logs from a recent batch of a sequence with known difficult positions, not just the final COA. A supplier who can provide per-cycle Kaiser or Fmoc UV data for a difficult sequence demonstrates real process control. One who offers only a final purity certificate is reporting outcomes without evidence of how they were achieved.*

---

## The gap between per-cycle numbers and manufacturing reality

The chemistry of coupling efficiency is well-understood. The operational reality at production scale is more complicated, and the gap between the two is where most batch failures originate.

For sequences longer than 25 residues, or for those containing multiple consecutive hydrophobic residues, maintaining that rate across every cycle requires active monitoring and willingness to intervene. Facilities that run fixed-cycle automated protocols without per-cycle checks will accumulate deletion sequences at predictable positions without detecting the problem until final HPLC analysis, at which point the batch is already compromised.

They cluster at predictable sequence positions, and those positions can be identified before synthesis begins using residue-pattern analysis. Pre-emptive backbone protection or pseudoproline incorporation at known problem positions is more cost-effective than recoupling after the fact, particularly for long sequences where a single missed coupling at position 20 of a 40-mer contaminates the entire batch.

Reagent and resin lot changes are the most common source of unexpected coupling failures in production. A resin lot with lower-than-specified loading or reduced swelling, or an activator lot with degraded potency, can drop per-cycle efficiency by several percentage points without any visible change in the synthesis protocol. This is why lot-to-lot resin swelling data and reagent age tracking are not administrative overhead but direct inputs to coupling efficiency. When a batch fails QC, the first diagnostic step should be checking whether a lot change preceded the failure, not adjusting the coupling time.

---

## Sources

The following primary literature and protocol references provide the authoritative detail behind the methods and thresholds discussed:

- [Coupling efficiencies of amino acids in the solid phase …](https://pubmed.ncbi.nlm.nih.gov/2134063/)
- [Unwanted hydrolysis or α/β-peptide bond formation: how long should the rate-limiting coupling step take? - RSC Advances](https://pubs.rsc.org/en/content/articlehtml/2019/ra/c9ra06124j)
- [Acid-Amine Coupling using DCC – Organic Synthesis](https://organic-synthesis.com/acid-amine-coupling-using-dcc/)

## China Peptides Sourcing Perspective

Everything discussed above applies to the broader question of sourcing **china peptides**: the compound's research profile matters, but the manufacturer and the batch documentation decide whether the vial in your hand matches the description on the page. For catalog listings, batch specifications, and ordering information, see the [catalog](/catalog/) or [how sourcing works](/how-it-works/).

## Related Products

- [BPC-157](/catalog/bpc-157/)
- [Semaglutide](/catalog/semaglutide/)
- [Tirzepatide](/catalog/tirzepatide/)
- [TB-500](/catalog/tb-500/)
