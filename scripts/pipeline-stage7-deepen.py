#!/usr/bin/env python3
"""Stage 7: 二次深化 — 修复残留噪声 + 薄页原创增厚。
1. 新闻页：删除 H1 后的重复标题/面包屑噪声行
2. contact/静态薄页：原创增厚（补全必要信息）"""
import re, glob

def strip_news_noise(body: str) -> str:
    # "H1\n\nChina Holiday Shipping Update: September 24–October 8 Home › News › ... Announcement 2026-09-17 China Holiday Shipping Update: ..."
    # H1 后紧跟的重复标题行（含 Home › 面包屑）整行删除
    lines = body.split('\n')
    out = []
    h1_seen = False
    for line in lines:
        if line.startswith('# '):
            h1_seen = True
            out.append(line)
            continue
        if h1_seen and ('Home ›' in line or 'Home ·' in line):
            continue  # 面包屑+重复标题噪声行
        out.append(line)
    return '\n'.join(out)

CONTACT_BODY = """# Contact

Contact Peptides of China for wholesale inquiry, custom manufacturing, product specifications,
private-brand sourcing, or questions about an existing order.

**What to include in your message**

- The compounds and catalog numbers you are interested in
- Quantities and your target market
- Whether you need specifications, COA, or other batch documentation

**Sourcing scope** — Peptides of China coordinates factory sourcing for research peptides
manufactured in China: availability confirmation, manufacturer specifications, order processing,
international logistics, and delivery support. For an overview of the model, see
[How It Works](/how-it-works/).

**Research use only** — All products are intended for laboratory research use. Inquiries about
human or veterinary use cannot be supported.

For the full list of services, see the [catalog](/catalog/) or
[peptide quality](/peptide-quality/) pages."""

def deepen(path):
    raw = open(path, encoding='utf-8').read()
    parts = raw.split('---\n', 2)
    if len(parts) < 3:
        return False
    fm, body = parts[1], parts[2]
    m = re.search(r'slug: "([^"]+)"', fm)
    slug = m.group(1) if m else ''
    changed = False
    if '/news/' in path:
        new_body = strip_news_noise(body)
        changed = new_body != body
        body = new_body
    if slug == 'contact':
        body = CONTACT_BODY
        changed = True
    if changed:
        open(path, 'w', encoding='utf-8').write(f'---\n{fm}\n---\n{body}')
    return changed

fixed = 0
for path in glob.glob('src/content/**/*.md', recursive=True):
    if deepen(path):
        fixed += 1
print(f'修复/增厚: {fixed}')
