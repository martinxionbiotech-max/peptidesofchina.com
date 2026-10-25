#!/usr/bin/env python3
"""Stage 3 批次 3：剩余产品回退生成器 — 灵活字段提取（Chemical Class / Also Known As / CAS / Research Areas），
为无标准 Profile 结构的产品组句。已有 '## Sourcing' 的跳过。"""
import re, glob

def find_field(body, *names):
    for n in names:
        m = re.search(rf'{re.escape(n)}\s+([^\n]+)', body)
        if m and len(m.group(1).strip()) > 2:
            return m.group(1).strip()
    return ''

def derive_flex(body, slug, name):
    cls = find_field(body, 'Chemical Class', 'Class', 'Category')
    cas = find_field(body, 'CAS Number', 'CAS No', 'CAS')
    research = find_field(body, 'Research Areas')
    # 开头描述句（跳过已有 intro 和标题）
    first = body[:600]
    # 类别来自 Specification Highlights
    if not cls:
        m = re.search(r'Category:\s*([^\n]+)', body)
        if m:
            cls = m.group(1).strip()
    display = name if name else slug.replace('-', ' ').title()
    parts = [f"{display} is listed in our **china peptide** catalog as a finished research compound from an established Chinese manufacturer."]
    if cls:
        parts.append(f"It is catalogued under the {cls} research category, and its specification is confirmed with the manufacturer before the order ships.")
    if cas:
        parts.append(f"Identity documentation includes its CAS registration ({cas}), so buyers can verify the compound independently of the seller's description.")
    if research:
        parts.append(f"Researchers sourcing **chinese peptides** in this field typically evaluate {display} for {research.lower()}; availability and batch documentation are confirmed factory-side before the invoice is issued.")
    parts.append(f"Like every listing on this platform, {display} is supplied for laboratory research use only.")
    return ' '.join(parts)

def sourcing_section(name, slug):
    return f"""## Sourcing {name} From China

{name} is available through our platform as a **china peptide** sourced directly from an
established Chinese manufacturer. Three points define how we handle it:

- **Factory-direct, not trader-sourced.** We confirm availability and specification with the
  manufacturer before the order is confirmed. There is no intermediary resale of unknown-origin
  vials in this catalog.
- **Specification before shipment.** The purity and concentration specification shown on this
  page is the manufacturer's batch specification. Product-specific quality-control information
  travels with the order.
- **Research-use discipline.** Like every listing in our catalog, {name} is supplied for
  laboratory research use only, under strict research-use terms.

For buyers comparing **chinese peptides** suppliers, the practical test is whether the seller can
name the manufacturer and show the batch documentation. We work the other way around: the
manufacturer and the documentation are the offer. [Browse the full catalog](/catalog/) or
[see how sourcing works](/how-it-works/)."""

def expand(path):
    raw = open(path, encoding='utf-8').read()
    parts = raw.split('---\n', 2)
    if len(parts) < 3:
        return False
    fm, body = parts[1], parts[2]
    if '## Sourcing' in body:
        return False
    m = re.search(r'slug: "([^"]+)"', fm)
    slug = m.group(1) if m else None
    if not slug:
        return False
    name_m = re.search(r'name: "([^"]+)"', fm)
    name = name_m.group(1) if name_m else slug.replace('-', ' ').title()
    intro = derive_flex(body, slug, name)
    section = sourcing_section(name, slug)
    body = f"{intro}\n\n{body}"
    if 'Frequently Asked Questions' in body:
        idx = body.find('Frequently Asked Questions')
        body = body[:idx] + section + '\n\n' + body[idx:]
    else:
        body = body.rstrip() + '\n\n' + section + '\n'
    open(path, 'w', encoding='utf-8').write(f'---\n{fm}\n---\n{body}')
    return True

done = 0
for path in glob.glob('src/content/products/**/*.md', recursive=True):
    if expand(path):
        done += 1
print(f'批次3 扩展: {done}')

files = glob.glob('src/content/products/**/*.md', recursive=True)
expanded = sum(1 for f in files if '## Sourcing' in open(f, encoding='utf-8').read())
print(f'总覆盖: {expanded}/{len(files)}')
