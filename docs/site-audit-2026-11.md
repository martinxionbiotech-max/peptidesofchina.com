# peptidesofchina.com — 深度站点审计（2026-11）

**审计对象：** https://peptidesofchina.com 线上站 + 本地 `npm run build` 产物  
**仓库：** `/home/ubuntu/work/peptidesofchina.com`，`main`，HEAD `5da491e`  
**审计时间：** 2026-11-17 19:34 CST  
**构建：** Astro 7；388 HTML（含 404）/ 387 sitemap URL / 387 markdown sidecar  
**线上核对：** 线上 sitemap 387 URL，与本地一致；`/llms.txt`、`/blog/.../index.md`、404、http→https 均实测  
**审计口径：** 七维站点分（完整度/SEO/AIO/数据一致性/原创性/主观见解/内容深度），另加 E-E-A-T 与合规风险两个镜头。分数为可复现度量，不是印象分。

> 说明：仓库内 `docs/peptidesofchina-content-audit-2026-11-17.md` 是上一轮“内容六维”快照；其中“0 个 author/date”“soft-404 200”等结论已与当前构建不一致，本文以本次构建为准。

---

## 1. 总表

| 维度 | 权重 | 得分 | 加权分 | 一句话依据 |
|---|---:|---:|---:|---|
| 完整度 | 15% | 72 | 10.8 | 387 页、0 孤儿、0 断链、深度≤3；但信任/法务页薄，无法定实体与地址 |
| SEO | 20% | 64 | 12.8 | title/H1/canonical 全过；description 仅 113/387 合规；OG/Twitter 全站为 0 |
| AIO | 15% | 44 | 6.6 | sidecar 全覆盖，但 llms 仅 35%；26 页无 JSON-LD，Breadcrumb 仅目录页 |
| 数据一致性 | 15% | 34 | 5.1 | 三套价格互不一致（frontmatter / PDF / schema）；库存与 MOQ 口径矛盾 |
| 原创性 | 15% | 68 | 10.2 | 剔除模板句后 0 对 >15%；但 125 篇共用开头、110 篇共用同一 Author's Take |
| 主观见解 | 10% | 15 | 1.5 | 明确第一人称立场仅 13/235（5.5%）；模板化“立场”不算立场 |
| 内容深度 | 10% | 72 | 7.2 | blog 中位 2,445 词、catalog 2,612 词；news 285 词、漏斗页 160–331 词 |
| **总分** | **100%** |  | **54.2** | 内容量强，结构化数据、价格与信任面拖累 |

**E-E-A-T 镜头（四维，0–100）：** Experience 35 / Expertise 62 / Authoritativeness 32 / Trust 25；加权 **36/100**。内容团队显然读过分析文献，但“谁在经营、凭什么信、出错找谁”没有可核验答案。

---

## 2. 站点规模与正面项

| 项 | 实测 |
|---|---:|
| HTML 页面 | 387（+404 = 388 构建页） |
| sitemap URL | 387 |
| Markdown sidecar | 387/387（100%） |
| blog | 195 篇，中位 2,445 词（min 602） |
| catalog | 127 个产品 + 1 个索引，中位 2,612 词（min 2,106） |
| news | 38 篇 + 1 个索引，中位 285 词（min 176） |
| static/policy | 22 页，中位 538 词 |
| 内部断链 | 0 |
| 孤儿页 | 0 |
| 点击深度 | 0:1 / 1:24 / 2:361 / 3:1 |
| title 重复 | 0 |
| title >60 字符（html.unescape 后） | 0 |
| H1 数量异常 | 0（仅 `/blog/cartalax/` 与 `/catalog/cartalax/` H1 同名，属产品与文章同名） |
| canonical 缺失/重复 | 0 / 0 |
| 图片缺 alt | 0（259 张 `<img>` 全部有 alt） |
| 404 | 真 404，不是 soft-404 |
| robots | 允许 AI 检索/训练爬虫，sitemap 指向 `sitemap-index.xml` |
| http→https | 301 正常 |

这些是站点底座：Astro 静态构建、无前端框架 JS、页面量真实、内链完整。问题集中在“结构化数据、元数据、价格/库存事实、信任与合规”。

---

## 3. 七维证据

### 3.1 完整度 — 72

**达标：**
- 387 页全部可抓，sitemap 387 条，0 孤儿、0 断链，点击深度≤3。
- 法务页齐全：privacy-and-cookie、terms、shipping、refund、research-use-disclaimer 均存在且页脚可达。
- 404、robots、canonical、sidecar 都能工作。

**扣分：**
- **无 `/accessibility/` 页**；内容站九页套缺少这一页。
- **无法定实体、注册号、注册地址**：`/company/` 331 词、`/contact/` 160 词，只有 `aaron@peptidesofchina.com` 与 +64 WhatsApp；`/terms/` 的“Business entity”只写平台描述，Governing law 写“platform's place of operation”，没有可核验主体。
- 信任页厚度不足：contact 160、company 331、manufacturing-partners 229、custom-peptide-services 182、author 132 词；这些是 B2B 漏斗的终点，不是可以忽略的工具页。
- `/reviews/` 声称“30 条 verified reviews、每条绑定 confirmed order”，但页面没有订单号、验证方式、第三方评价源或 schema；无法从站内证明“verified”。

### 3.2 SEO — 64

**达标：**
- 387 个 title 全部唯一，`html.unescape` 后 0 个 >60 字符；H1 全部 1 个；canonical 全部唯一且 apex；内部断链 0。
- URL 结构清楚：`/catalog/<slug>/`、`/blog/<slug>/`、`/news/<slug>/`。

**扣分：**
- **description 只有 113/387（29.2%）落在 140–155 字符**：99 页 <120（news 和部分 catalog 模板 118/119），90 页 120–139，85 页 156–160；合计 189 页越界。catalog 模板的 `${name}: research peptide from China...` 被压到 119 字符；news 直接使用 59–102 字符的短句。
- **OG/Twitter 全站为 0**：`og:title` 0/387、`og:image` 0/387、`og:site_name` 0/387、`twitter:card` 0/387；分享到微信/LinkedIn/X 是空白卡。
- `www.peptidesofchina.com` 返回 200，与 apex 同内容；canonical 指 apex，但缺 301，重复主机。
- 标题构成偏“Buy X | China Peptide — Peptides of China”，127 个产品中 63 个 name 仍是 `peg-mgf`、`retatrutide`、`botulinum-toxin-a` 这类 slug 形态；标题长度合规不等于可点击。
- `/blog/` 按 title 字母序排列，而不是按日期；195 篇文章的“最新”入口不可用。

### 3.3 AIO — 44

**达标：**
- 387/387 页有 `index.md` sidecar；`Accept: text/markdown` 实测返回 markdown。
- robots 明确允许 OAI-SearchBot、Claude-SearchBot、PerplexityBot、GPTBot 等。
- catalog 127 页有 Product + FAQPage + BreadcrumbList；JSON-LD 全部可解析（0 个坏 JSON）。

**扣分：**
- **`llms.txt` 只覆盖 134/387（34.6%）**：127 个 catalog + 7 个 key page；195 篇 blog、38 篇 news、19 个静态/政策页全部缺席。文件头还是“Catalog (127 products)”为主，不是全站索引。
- **26 页完全没有 JSON-LD**：首页、`/faq/`、`/company/`、`/contact/`、`/reviews/`、`/guides/`、`/author/`、全部政策页、blog/news 索引。站点级 Organization/WebSite 节点不存在；Article 里的 Organization 只是作者。
- **BreadcrumbList 只有 127 页（catalog）**；blog 196、news 39、static 24 全部缺。页面上有面包屑，schema 没接。
- **Article 233 个，但无 `datePublished` / `dateModified` / `image` / `publisher`**；Google Article rich result 与 AI 引用都缺关键字段。
- **FAQPage 127 个全在 catalog，`/faq/` 自己反而没有 FAQPage**；这是模板接线遗漏，不是内容不足。
- 0 个 `TechArticle`；5 个 5,700 词级 pillar 页没有用 TechArticle/Article 标出来。
- 外部引用质量混杂（见 3.5）。

### 3.4 数据一致性 — 34

这是本轮最严重的维度，不是“重复内容”，而是**同一事实有三套数字**。

**价格三套口径：**

| 来源 | 价格范围 | 说明 |
|---|---:|---|
| 产品 frontmatter `price` | **$11–$480** | 127 个产品逐 SKU 的真实字段 |
| `/pricelist.pdf` | **$7–$375/box** | 4 页 PDF；如 BPC-157 $40/$58/$85，GHK-Cu $24/$29，Retatrutide $58–$259 |
| Product schema | **全部 $60–$180** | 127/127 个 Product 节点都用 `lowPrice: 60 / highPrice: 180` |

- **41/127 个产品落在 60–180 之外**（22 个 <60，19 个 >180），schema 对它们的事实陈述是错的。
- 产品页可见区域只写“Latest Price List / Prices in current catalog PDF”，**不显示价格**；schema 的价格既不是可见价，也不是 PDF 价，属于结构化数据与页面不一致。
- 示例：BPC-157 frontmatter $50；PDF $40/$58/$85；schema $60–$180。三个数字没有一个能互相对上。

**其他一致性错误：**
- **HGH 库存矛盾**：`/news/shanghai-manufacturing-partner-suspends-hgh-exports/` 说 HGH 暂停出口、全部标记 Out of Stock；`hgh-191aa-somatropin.md` 与 `hgh-fragment-176-191.md` 仍是 `status: "In Stock"`。
- **押金矛盾**：terms/refund/how-it-works 写“no processing deposit”，FAQ 与 how-to-pay 写“$10 processing deposit required / $10 unpaid deposit”。同一站两套收钱口径。
- **MOQ 表达混乱**：首页/FAQ `$600 per supplier`，catalog 说“one kit of 10 vials”，terms 说“one box is enough to start”，FAQ 又有“first-order trial below $600”。这些可以共存，但页面没有把它们组织成一个清楚规则。
- **图片**：78/127 个产品共用 `generic-vial.png`；`generic-pancragen.webp` 不存在（schema 与可见 `<img>` 都 404）；39 个唯一产品图。
- **产品名**：63/127 个 name 为全小写 slug（`peg-mgf`、`p21`、`epo`、`lemon-bottle-liquid` 等），H1 与目录卡直接显示 slug。
- **时间戳**：382/382 个内容文件的 frontmatter 全部是 `updated: 2026-11-17`，且没有 `published` 字段；Article schema 也没有 `datePublished`/`dateModified`。这是批量盖章，不是逐页复核记录。

### 3.5 原创性 — 68

**先给结论：正文不是批量复制。** 先剔除在 ≥5% 页面出现的共享句，再算 5-gram Jaccard：
- blog 196 页：0 对 >0.15
- news 39 页：0 对 >0.15
- catalog 128 页：0 对 >0.15

**但模板足迹很重，不能按“原创性 PASS”放过：**
- 195 篇 blog 中 **125 篇共用同一句开头**：“For researchers and resellers sourcing **chinese peptides**, the practical questions are the same regardless of compound...”
- **110 篇共用同一组 `## The Author's Take` 三段**：Position / Reasoning / Disclosure 逐字相同；这不是“每篇的立场”，是模板。
- 195 篇都有 `## Sources` 标题，但 **79 篇没有任何外部链接**；21 篇明确写“No external bibliography”。195 个 Sources 标题里，真正可点的引用只有 116 篇。
- 原始（未剔共享句）5-gram 有 632 对 >0.15，top 0.287；这主要是模板句造成，但读者和爬虫看到的是 195 篇开头/结尾高度相似。
- 部分标题带 `-2`/`-3` 后缀（`bestbellpharmacom-alternatives-3`、`biolongevitylabs-com-alternatives-3`、`sinobiowaypeptide-com-alternatives-3`），是程序化变体痕迹。

### 3.6 主观见解 — 15

- 按 `In our view / Our view / We would / Our position / My view` 等明确人称标记，编辑内容 235 篇中只有 **13 篇（5.5%）**有立场。
- 195 篇的 `The Author's Take` 虽然标题像立场，但 110 篇正文完全相同；脚本按渲染文本只能识别出 13 篇真正有独立判断的页面。
- 产品页没有 `notFor` 这类“什么情况下不该买”的字段；catalog 的 FAQ 是通用采购问答，不是品类判断。
- `/reviews/` 的 5.0/30 条是客户评价，不是编辑立场；且全部 5 星、无验证入口。

### 3.7 内容深度 — 72

| 页族 | n | 中位词数 | 最短页 |
|---|---:|---:|---:|
| blog | 196 | 2,445 | 602（retatrutide-side-effects） |
| catalog | 128 | 2,612 | 2,106（ara-290），索引 811 |
| news | 39 | 285 | 176（first-australian-order） |
| static | 24 | 538 | 132（author）、160（contact）、182（custom services） |

- 五个 pillar 页（china-peptide-sourcing 5,783；peptide-quality-testing 5,933；peptide-handling-protocols 5,813；peptide-categories-mechanisms 5,742；peptide-compliance-risk 5,713）达到 5,700 词级，产品页 2,000–3,200 词，这部分是真深度。
- 但新闻 285 词、contact 160 词、custom 182 词、manufacturing 229 词、author 132 词；这些是决策/信任节点，不能只看 blog 中位数。
- 首页 454 词，且主标题“China Peptides From China — Sourced at the Factory Level”语义重复；首页没有 schema/OG，是入口页的完整度缺陷。

---

## 4. 合规与信任红灯（不进入七维分数，但优先级高于分数）

### P0-1 剂量内容与 RUO 立场直接冲突
- 73/195 篇 blog 出现 `mg/mcg/iu` 剂量数字；67 篇出现 `injection`；78 篇出现 `dose/dosage`。
- 4 个标题直接是 Dosage：`aod-9604-dosage`、`5-amino-1mq-dosage`、`semax-dosage-mg-per-day`、`ghk-cu-dosage-benefits`。
- `aod-9604-dosage.md` 给出“250–500 mcg/day”“500–1000 mcg/day”“4–8 weeks / 8–12 weeks”等按日给药与周期；`semax-dosage-mg-per-day.md` 同类。
- 同一站 `/author/poc-tech-team/` 写“The content does not provide human dosing, injection, treatment or cure advice”；`/peptide-compliance-risk/` 还教人搜索 `dose, dosage, cycle, inject` 并改写。**内容与声明互相打脸。**
- 这不只是 SEO 问题：这是 YMYL/医疗内容政策、支付风控、平台审核和监管风险的交汇点。要么删掉剂量页/剂量段，要么把站点明确改成“文献摘要，不提供任何数值型给药范围”，不能靠页尾免责声明兜底。

### P0-2 “verified reviews”无法验证
- `/reviews/` 30 条全部 5 星、平均 5.0；描述声称“每条绑定 confirmed order”，但没有任何订单号、验证标记、第三方源或 schema。
- 多条评论直接谈人体使用/转卖给亲友（Reta、HGH），与 RUO 冲突。
- 没有 `AggregateRating` schema 是好事（至少没有把不可验证评分喂给 Google）；但页面文字本身仍是不可验证的社会证明。

### P0-3 产品组合与收款方式需要法务/支付审查
- catalog 含 `botulinum-toxin-a`、HCG、HGH、EPO、Lemon Bottle、Retatrutide/Semaglutide/Tirzepatide 等；这些不是普通“research peptide”品类，涉及处方药/生物制品/进口限制。
- `/how-to-pay/` 只接受 PYUSD/USDC/USDT 链上转账；FAQ 明确说传统支付“structurally incompatible”，并描述 6–8 周资金冻结。这是业务事实，但也意味着支付争议、退款、KYC/AML 与平台合规风险需要业主书面确认。
- 站点无法定实体/地址；terms 的 governing law 是“platform's place of operation”，无法定位管辖地。

### P0-4 价格 schema 失实
见 3.4：127 个 Product 全写 $60–180，而 frontmatter $11–480、PDF $7–375；41 个产品越界。Google Rich Results 能解析字段，但 Merchant/结构化数据政策要求价格与可见页面一致；当前是三套价格，不能上线为“可抓取的商品价格”。

---

## 5. 短板（决定分数的前三项）

1. **数据一致性 34 分**：价格三套、HGH 库存矛盾、押金/MOQ 矛盾。它是 15% 权重，但会同时破坏信任、富媒体、转化与复购。
2. **AIO 44 分**：llms 35%、26 页无 schema、Breadcrumb 仅目录、Article 无日期/图片/ publisher。站点有 387 个 sidecar，却没有把机器可读层接完整。
3. **主观见解 15 分**：195 篇都有“Author's Take”标题，但 110 篇是同一段文字；这不是编辑判断，是模板。加上 5.5% 的真实立场率，E-E-A-T 很难靠“团队署名”补回来。

SEO 64 分不是最差，但 description 189 页越界 + OG 全站为 0 是低成本、高确定性的失分点，应排在内容和合规之后立即处理。

---

## 6. 修复清单（按加权增益 × 风险排序）

> 编号供后续直接引用；每项都先在仓库确认路径存在。价格为估算工时，不含业主提供实体/证书/实拍图的时间。

| # | 动作 | 影响维度 | 预估总分增益 | 工时 |
|---|---|---|---:|---:|
| 1 | **处理剂量内容**：删除/重写 4 个 dosage 页与 73 篇含 mg/mcg 的段落；保留“文献报告了暴露范围”但不给可按日执行的方案；同步 author/compliance 口径 | 合规 + 信任 + 主观见解 | +4~6（且移除 P0） | 1–2 天 |
| 2 | **价格单一事实源**：产品页显示 `price`/规格价，schema 用同一 `Offer.price`（或按真实区间的 AggregateOffer），删除全站 60–180 的假带；同步 PDF 与 frontmatter | 数据 15% + 信任 | +5~6 | 1 天 |
| 3 | **站点级 schema 与社交卡**：BaseLayout 加 Organization/WebSite（logo、sameAs、contactPoint）、OG/Twitter、默认 OG 图；blog/news/static 补 Breadcrumb、Article datePublished/dateModified/publisher/image；`/faq/` 补 FAQPage | AIO 15% + SEO 20% | +4~5 | 6–10h |
| 4 | **description 收敛**：一个 `fitDescription()`，140–155 按词边界；catalog 模板生成 140–155；news 重写 99 条短描述；全量复测 | SEO 20% | +2~3 | 4–6h |
| 5 | **llms 全量生成**：postbuild 读 sitemap，把 195 blog、38 news、静态页按分组写入；验收 387/387 | AIO 15% | +1.5~2 | 2h |
| 6 | **信任面**：补法定实体/注册地址/注册号（业主提供）；contact 从 160 扩到 650+；company/manufacturing/author 加可核验字段；reviews 要么展示验证方式，要么改成“客户留言，未独立验证”并撤掉 5.0 宣称；HGH 库存、押金、MOQ 三处统一 | 完整度 + 数据 + E-E-A-T | +3~4 | 1–2 天 + 业主材料 |
| 7 | **漏斗/新闻薄页**：contact、custom、manufacturing、author 加厚；news 38 篇 176–285 词的更新合并为季度更新或加“这是什么/对买家意味着什么”；guides 439 词改成真正索引 | 深度 10% + 完整度 | +1.5~2 | 1–2 天 |
| 8 | **产品数据清理**：63 个全小写 name 改为展示名；78 个 generic-vial 换真实图/明确 `illustrative vial`；补 `generic-pancragen.webp`；产品页显示价格与 MOQ | 数据 + 转化 | +1~2 | 1 天 + 实拍 |
| 9 | **拆模板 Author's Take**：110 篇同一段改为逐篇 60–90 词（推荐 + 理由 + 例外），先做 20 篇高商业意图；stance 覆盖率目标 ≥60% | 主观见解 10% + 原创性 | +2~3 | 2–3 天 |
| 10 | **引用治理**：79 篇无外链的加 2–5 条权威来源；98 篇引用 vendor/竞品博客的，替换为 PubMed/DOI/FDA/ICH/ISO 或改成 Evidence note；抽查 404（已见 peptidestaff 2 条 404） | AIO + E-E-A-T | +1~2 | 1–2 天 |
| 11 | **www 301**：Pages Functions 或 Redirect Rule，www→apex | SEO/完整度 | +0.3~0.5 | 30 min |

**预估：** 完成 1–7 项，按同口径约 **66–70 分**；完成 1–11 项约 **72–75 分**，前提是业主能提供法定实体/地址、真实产品图与可验证评价。若只做 3/4/5（schema、description、llms），大约到 **60–62**，不能解决合规与数据失实。

---

## 7. 结论

这不是一个“内容不够”的站：127 个产品页中位 2,612 词、195 篇 blog 中位 2,445 词、5 个 pillar 页 5,700 词级，内部链接和 sidecar 都完整。它的问题是**内容层做得比事实层和机器层更深**：

- 三套价格、两套库存、两套押金口径；
- 26 页没有结构化数据，127 个 Product 的价格是统一假带；
- `llms.txt` 只覆盖三分之一；
- 73 篇 blog 提供剂量数字，和“不提供 human dosing”的自我声明冲突；
- 195 篇的“立场”是同一段模板。

如果目标只是“让 Google 抓到”，第 3/4/5 项就能显著改善；如果目标是“能长期投放/被 AI 引用/通过支付与平台审核”，第 1/2/6 项必须先做，否则分数越高，风险越大。

---

*审计只读；本文件是唯一改动。所有数字来自本次 `npm run build` 后的 `dist/` 与线上抽样。*
