# peptidesofchina.com — 全面内容修复计划

> 版本：2026-11-05
> 依据：`docs/peptidesofchina-content-audit-report.md`（六维审计）
> 目标：加厚、去模板、提高原创性、加入编辑判断、建立 Pillar + Cluster 结构。

---

## 1. 五个 Pillar

| # | Pillar | URL | 角色 |
|---|---|---|---|
| 1 | China Peptide Sourcing | `/china-peptide-sourcing/` | 供应商、工厂直供、MOQ、付款、物流、文件 |
| 2 | Peptide Quality & Testing | `/peptide-quality-testing/` | HPLC/MS、COA、纯度、内毒素、批次一致性 |
| 3 | Peptide Handling & Research Protocols | `/peptide-handling-protocols/` | 复溶、储存、稳定性、溶解度、实验操作 |
| 4 | Peptide Categories & Mechanisms | `/peptide-categories-mechanisms/` | GHRH/GHRP、GLP-1、 cosmetic、bioregulator、mitochondrial |
| 5 | Peptide Compliance & Sourcing Risk | `/peptide-compliance-risk/` | research-use-only、海关、供应商声明、法规边界 |

**Pillar 页标准**：4,000–6,000 词、12–18 个 H2、15+ 个 cluster 链接、1 个决策框架、8 条 FAQ、`## The Author's Take`、6+ 来源。

## 2. Cluster 结构

### P1 Sourcing
- 现有：`how-to-source-peptides-from-china-a-2026-b2b-procurement-guide`、`peptide-sourcing-myths-the-operational-reality-of-research-procurement-in-2026`、`how-to-buy-peptides-in-bulk-a-2026-direct-to-manufacturer-sourcing-protocol`、`research-peptide-customs-clearance-a-professional-b2b-sourcing-guide-2026`、`how-to-choose-a-high-purity-peptide-supplier`、`peptide-procurement-cost-reduction-strategies-2026-guide`、`epithalon-wholesale-sourcing-a-b2b-guide-to-direct-manufacturer-channels-2026`、`sourcing-tb-500-from-china-a-2026-b2b-procurement-and-verification-guide`、`coa-verified-peptides-wholesale-2026-sourcing-verification-guide`
- 产品 cluster：127 个 catalog 页（按 category 分组）
- 缺口：供应商审计清单、付款与风控、MOQ/阶梯价、交期与节假日、文件包清单

### P2 Quality & Testing
- 现有：`how-we-verify-product-quality-our-3-step-approach-to-china-peptide-sourcing`、`why-so-many-peptides-on-the-market-are-low-quality`、`why-peptide-suppliers-inconsistent-quality`、`why-purity-and-concentration-tests-are-not-enough`、`why-peptide-impurities-affect-study-outcomes-and-how-china-peptide-buyers-can-verify-purity`、`what-are-endotoxins-why-they-matter`、`peptide-molecular-weight-verification-steps`、`peptide-solubility-troubleshooting`、`how-to-assess-peptide-supplier-gmp-compliance-in-2026`
- 缺口：HPLC 方法对比、MS 方法选择、COA 字段逐项解释、内毒素/无菌、第三方复测、批次留样

### P3 Handling & Protocols
- 现有：`peptide-lyophilization-reconstitution-guide-for-researchers`、`retatrutide-stability-and-storage-what-research-buyers-can-and-cannot-infer`、`how-to-reconstitute-bpc-157`、`peptide-efficacy-measurement-a-researchers-2026-guide`、`role-of-counterions-in-peptide-stability`
- 缺口：称量/浓度计算、冻干饼外观、复溶技巧、容器吸附、冻融循环、稳定性设计
- **边界**：只写实验室操作，不写人体剂量/给药/医疗建议

### P4 Categories & Mechanisms
- 现有：`therapeutic-peptide-classification-a-2026-research-guide`、`peptide-selectivity-explained-for-researchers`、`igf-1-lr3-research-applications-a-b2b-sourcing-and-technical-guide-2026`、各产品页的 Compound Profile
- 缺口：GHRH vs GHRP、GLP-1 类、 cosmetic peptides、bioregulators、mitochondrial peptides、blends 的 research rationale

### P5 Compliance & Risk
- 现有：`research-peptide-customs-clearance-a-professional-b2b-sourcing-guide-2026`、`how-to-assess-peptide-supplier-gmp-compliance-in-2026`、`research-use-disclaimer`、`shipping-and-reshipment-policy`、`refund-and-cancellation-policy`
- 缺口：research-use-only 边界、进口文件、供应商声明核验、哪些 claim 不能写、退货/重发风险

## 3. 修复批次

### Batch 1（本批）
5 个 Pillar 页 + `/guides/` hub + nav 入口。

### Batch 2（P0）
产品页去模板：先重写 20 个高优先级产品（bpc-157、tb-500、semaglutide、tirzepatide、retatrutide、ipamorelin、cjc-1295、ghk-cu、melanotan-ii、epithalon 等），每批 10 个。
- 删除跨 127 页复用的三大段
- 每页独有内容 ≥85%
- 加 `## The Author's Take`（sourcing/quality 判断，不做医疗建议）
- 补 `category`、`updated`、来源

### Batch 3（P1）
Blog 升级：先做 30 篇高流量/高商业意图页。
- 加 `## The Author's Take`
- 补 Sources（当前 162/195 无来源段）
- 清 AI 套话（robust/leverage/elevate/not only）
- 每篇 2,500–4,000 词，至少 8 个独有数据点

### Batch 4（P1）
剩余 107 个产品页，按 category 分批 10 个/批。

### Batch 5（P2）
- 元数据：title ≤60、description ≤160、补 author/date
- News 薄页合并/noindex
- 首页/News JSON-LD
- 内链与 sitemap

## 4. 写作标准（强制）

使用 `deep-research-human-writer` v3：
- 流程：Intent → Entity → Research → Evidence → Verification → Analysis → Contradiction → Information Gain → Human Writing → QA
- 禁止 Search → Rewrite → Publish
- 6–10 个来源；claim 表 F/D/I/E/U；contradiction log
- 固定 `## The Author's Take`：Position（第一人称、可引用）/ Reasoning / Disclosure
- 句间重叠 <5%；每页 8+ 独有数据点
- 不编来源/数字/经历/认证；不写人体剂量、给药、医疗建议
- 全部内容保持 research-use-only 框架

## 5. 质量闸门

- 4,000–6,000 词（Pillar）；2,500–4,000 词（Blog）
- 15+ 内链；0 broken links
- 0 人体剂量/医疗建议
- `npm run build` 通过
- 产品独有句词占比 >0.85
- 审计六维复测：重复、AI 痕迹、薄内容、无价值、主观观点、来源覆盖

## 6. 执行顺序

1. Batch 1：5 Pillar + hub + nav
2. Batch 2：20 个产品页
3. Batch 3：30 篇 blog
4. Batch 4：剩余产品
5. Batch 5：元数据与结构收尾
6. 复测六维，出修复报告
