# peptidesofchina.com — 内容质量六维审计报告

> 日期：2026-11-05
> 范围：`peptidesofchina.com`（用户写作 “peptideofchina”；实际仓库/站点为 plural）
> 方式：只读审计；只新增本报告，未改动任何内容文件
> 方法：内容质量六维（重复 / AI 痕迹 / 内容薄 / 无价值 / 缺主观观点 / 非原创）+ 结构与元数据抽查

---

## 1. 结论摘要

综合判断：**约 5.5 / 10**。
- **Blog 6.5 / 10**：长文基础较好，引用和结构强于产品页。
- **Product 4.5 / 10**：字数不低，但模板重复严重，产品独有信息占比不足。
- **News/Pages 5 / 10**：news 属于时效短讯，pages 属政策页；本身不是主内容，但存在元数据与来源缺口。

| 维度 | 结果 | 关键数字 | 严重度 |
|---|---|---|---|
| 重复 | **FAIL** | 产品 18 对 ≥0.70；1,338 对 ≥0.50；195 篇 blog 共用同一段 CTA | **P0** |
| AI 痕迹 | **FAIL** | blog：robust 27、leverage 23、elevate 19、not only 18；product：elevate 64 | P1 |
| 内容薄 | **PASS（带 P2）** | product 450–4,235 词；blog 503–5,370 词；news 136–652 词 | P2 |
| 无价值 | **FAIL** | 127 个产品共用多段“工厂直供/批次文件”套话；blog “high quality” 19 次 | P1 |
| 缺主观观点 | **FAIL** | 376 个文件中 `Author's Take / Our Read` = **0**；无作者、无日期 | P1 |
| 非原创 | **PARTIAL / 未完全验证** | product 0 外部来源；blog 45/195 无外链，162/195 无 Sources 段 | P1 |

---

## 2. 盘点（实测）

| 集合 | 文件数 | 字数 min / mean / median / max | H2 均值 | 备注 |
|---|---:|---|---:|---|
| products | 127 | 450 / 1,589 / 1,359 / 4,235 | 11 | 全部 `status=In Stock`；`category` 全部为空 |
| blog | 195 | 503 / 2,284 / 2,368 / 5,370 | 12 | 150 篇有外链；仅 33 篇有 Sources/References |
| news | 38 | 136 / 251 / 234 / 652 | 2 | 时效短讯；7 篇有外链 |
| pages | 16 | 164 / 618 / 380 / 2,150 | 6 | 政策/公司/流程页 |

- 站点 sitemap：**380 个 URL**。
- 所有集合：**0 个 `date` / `author` 字段**。
- 产品 frontmatter `category`：**127/127 为空**（正文里有类似 “Muscle & Performance” 的分类，但未进入结构化字段）。
- Blog 有 1 组完全相同的 meta description（2 篇）。

---

## 3. 六维详情

### 3.1 重复 — FAIL（P0）

**产品页（最严重）**
- 4-gram Jaccard：**18 对 ≥0.70**，**1,338 对 ≥0.50**，最高 **0.745**。
- 最高相似对示例：
  - `bpc-157-10mg-tb-500-10mg-kpv-10mg` ↔ `ghk-cu-50mg-kpv-10mg`：0.745
  - `livagen` ↔ `bronchogen`：0.733
  - `cardiogen` ↔ `vesugen`：0.731
- 产品页共享句（跨 127 个页面重复）：
  - “three points define how we handle it — factory-direct, not trader-sourced…”：**127 次**
  - “Peptides of China is a B2B wholesale supplier…”：**127 次**
  - “for buyers comparing chinese peptides suppliers…”：**127 次**
  - “every batch is tested by the manufacturer…”：**126 次**
  - “China peptides sourcing perspective…”：**109 次**
- 产品正文“独有句词占比”：均值 **0.64**、中位数 **0.72**、最低 **0.33**。也就是说，部分产品页有约 **2/3 的内容是可跨页复用的模板**。

**Blog**
- 4-gram Jaccard：最高仅 **0.328**，无 ≥0.50 的对；正文层面重复健康。
- 但 195 篇 blog 共用同一段 CTA/介绍句（“For researchers and resellers sourcing chinese peptides…”），属于**模板化块**，不是正文抄袭。

**结论**：blog 正文重复低；product 页是模板复用重灾区，是本次审计的 P0。

### 3.2 AI 痕迹 — FAIL（P1）

机械/AI 高频词统计：
- **Product**：`elevate` 64、`crucial` 3、`robust` 2。
- **Blog**：`robust` 27、`leverage` 23、`elevate` 19、`not only` 18、`crucial` 8、`it is important to` 4、`whether you are` 2、`furthermore` 2、`world-class` 2。
- **News**：`it is important to` 1、`unlock` 1。
- **Pages**：`not only` 1、`elevate` 1、`leverage` 1。

判断：
- Product 的 `elevate` 高频更接近“营销模板词”，不是纯 AI 痕迹。
- Blog 的 `robust / leverage / not only` 属于典型 AI 写作惯性；结合统一的段落节奏和“首先/其次/总之”结构，AI 痕迹为 P1。
- 未发现 `delve`、`world-class` 大量滥用，但 `world-class` 出现 2 次仍建议删除。

### 3.3 内容薄 — PASS（P2）

- Product：最短 450 词，均值 1,589；按 <150 词阈值，**0 个产品页算薄**。
- Blog：最短 503 词，均值 2,284；<300 词为 0。
- News：136–652 词；按新闻短讯可接受，但 136–200 词的几条建议合并或明确 `noindex`。
- Product meta description：5–33 词，**10 个 <15 词**；这是“描述字段薄”，不是页面薄。
- Pages：1 个 164 词（法律/政策页），可接受。

**判断**：主内容不薄；薄点集中在 product meta description 和少量 news。

### 3.4 无价值 — FAIL（P1）

空话/可互换表达：
- Blog：`high quality` 19、`professional manufacturer` 1、`reliable supplier` 1。
- Product：`reliable supplier` 1。
- Pages：`trusted supplier` 1。
- 更大的问题不是这些词，而是 **127 个产品共用“工厂直供/批次文件/中国肽 sourcing”三大段**，导致页面之间可互换，采购区分价值低。

关键词/声明密度（全站词频）：
- `research use only` 611
- `dose` 162
- `healing` 152
- `growth hormone` 54
- `muscle & performance` 43
- `anti-aging` 26
- `testosterone` 19
- `weight loss` 6

这些词本身不一定违规，但 `healing / anti-aging / weight loss / muscle & performance` 与“研究用途”定位存在**内容合规风险**，建议法务/合规复核（本报告不做法学结论）。

### 3.5 缺主观观点 — FAIL（P1）

- `Author's Take` / `Our Read` / `Editorial View`：**376 个文件中 0 个**。
- Blog 有 `we recommend` 9、`you should` 47、`we believe` 1，但都是零散句，不是结构化立场。
- Product / News / Pages：主观判断句基本为 0。
- **0 个文件有 `author` 字段；0 个文件有日期字段**。这同时削弱 E-E-A-T：读者无法判断谁写的、什么时候复核。

**判断**：不是“没有观点”，而是“观点没有形成可引用的编辑立场块”。按 `deep-research-human-writer` 标准，应固定 `## The Author's Take`（Position / Reasoning / Disclosure）。

### 3.6 非原创 — PARTIAL / 未完全验证（P1）

**已验证**
- Product：**0 个外部来源 URL**；没有 Sources 段。产品页的“证据”主要是制造商规格/批次声明，未落到可点击来源。
- Blog：150/195 有外链，共 608 个外部 URL；但只有 **33/195** 有 `Sources / References / Further Reading` 段，**162 篇没有来源段**，**45 篇没有任何外链**。
- News：7/38 有外链；0 个 Sources 段。
- Pages：2/16 有外链。

**未验证（假设）**
- 未做“对 5 个源站的 4-gram 源回声”测试，因为本次没有抓取源站语料。
- 因此不能断言 blog 正文抄袭；从抽样看，长文更像原创综合，但引用纪律不一致。
- Product 页的模板段可能来自行业通用话术/自家文案，需以源站抓取后才能判定逐字重合。

---

## 4. 结构与 SEO 附带发现

- Title >60 字符：**Product 24/127、Blog 64/195、News 3/38**。
- Description >160 字符：**Product 85/127、Blog 10/195、News 17/38**。
- 抽样 canonical / H1 正确；Product 有 `Product` JSON-LD，Blog 有 `Article`；首页与 News 首页无 JSON-LD。
- Sitemap 380 URL，包含全部 product/blog/news；未对 thin news 做排除。
- 1 个 page 零内链。
- Product `category` 字段全空，影响筛选、schema 与内链聚合。

---

## 5. 修复建议（只列不实施，等指令）

### P0 — 先处理产品模板重复
1. **产品页去模板化**：127 个产品页按“化合物独有信息”重写；目标独有句词占比 >0.85（当前中位数 0.72，最低 0.33）。
2. **删除跨页复用段**：把 “three points define…” / “B2B wholesale supplier…” / “every batch tested…” 等改为产品级具体信息，或压缩成一次站点级说明。
3. **补齐 product 结构化字段**：`category` 127/127 为空，先补 category；再处理 85 个 >160 字符的 description、24 个 >60 字符的 title。

### P1 — 内容价值与可信度
4. **加作者/日期/复核日期**：376 个文件目前 0 author / 0 date。
5. **固定 `## The Author's Take`**：每篇 blog 与重点 product 页加 Position / Reasoning / Disclosure；当前 0/376。
6. **来源纪律**：162 篇 blog 补 Sources 段；product 页补“制造商/批次/检测方法”的可追溯引用；news 至少给事件来源。
7. **AI 痕迹清理**：优先清 `robust / leverage / elevate / not only / crucial / world-class`；统一段落节奏，避免“首先/其次/总之”模板。
8. **合规复核**：`healing / anti-aging / weight loss / muscle & performance / dose` 等表述与研究用途定位冲突，建议法务/合规审一遍。

### P2 — 结构与元数据
9. **News 薄页**：<200 词的 news 合并或 `noindex`；不要全部进 sitemap。
10. **重复 description**：blog 有 1 组完全相同的 meta description，改为各自独有。
11. **零内链 page**：补 1–2 条相关内链。
12. **首页/News JSON-LD**：补 Organization / WebSite / CollectionPage（如适用）。

---

## 6. 已验证 vs 假设

**已验证**
- 文件数、字数、H2、title/description 长度、重复 description、外链数量、Sources 段数量。
- 产品 4-gram 相似度、blog 4-gram 相似度、跨页重复句计数。
- AI/空话/主观词频。
- 抽样 live canonical / H1 / JSON-LD / sitemap 380。

**假设/未验证**
- 未做源站 4-gram 源回声，不能判定 blog/product 对外部源站的逐字重合率。
- 未做法律合规判断；`healing/anti-aging` 等仅标风险。
- News 短页是否应保留，取决于其流量/更新价值，需 GSC 数据。

---

## 7. 审计方法（可复现）

- 读取 `src/content/{products,blog,news,pages}/**/*.md`，不读渲染模板。
- 4-gram Jaccard：小写、去标点、去 URL 后按词切分；≥0.50 记模板/近重复候选。
- 重复句：长度 ≥60 字符的句子，规范化后统计跨文件出现次数。
- AI/空话/主观词：固定词表正则统计。
- 元数据：frontmatter title/description 长度；live HTML 抽样 canonical/H1/JSON-LD。
- 只读：本报告是唯一新增文件；建议只列不实施。
