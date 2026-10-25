#!/usr/bin/env python3
"""Stage 2: cleanup + rebrand — strip nav/footer noise, rebrand to Peptides of China,
drop injected duplicate H1. Deterministic, no content invention."""
import re, glob, json

FOOTER_MARKERS = [
    'Platform Catalog Customization How It Works',
    'Popular Peptides BPC-157',
    'Compare vs. Amino Asylum',
    'Track Your Order Resources',
    'Legal Terms & Conditions',
]
# leading noise: "Buy AICAR | Research Grade | Peptides From China AICAR Buy AICAR — ..."
LEAD_NOISE = re.compile(r'^[\w\s\-.]+ \| Research Grade \| Peptides From China ')

BRAND_MAP = {
    'PeptidesFromChina.co': 'Peptides of China',
    'Peptides From China': 'Peptides of China',
    'peptidesfromchina.co': 'peptidesofchina.com',
}

def clean_body(body: str) -> str:
    for marker in FOOTER_MARKERS:
        i = body.find(marker)
        if i > 200:
            body = body[:i]
    m = LEAD_NOISE.search(body)
    if m:
        body = body[m.end():]
    for old, new in BRAND_MAP.items():
        body = body.replace(old, new)
    body = re.sub(r'\n{3,}', '\n\n', body)
    return body.strip()

def main():
    stats = {}
    for cat in ('products', 'blog', 'news', 'pages'):
        count = 0
        for path in glob.glob(f'src/content/{cat}/**/*.md', recursive=True):
            raw = open(path, encoding='utf-8').read()
            parts = raw.split('---\n', 2)
            if len(parts) < 3:
                continue
            fm_block = parts[1]
            body = parts[2]
            lines = body.split('\n')
            if lines and lines[0].startswith('# '):
                lines = lines[1:]
            body = clean_body('\n'.join(lines))
            open(path, 'w', encoding='utf-8').write(f'---\n{fm_block}\n---\n\n{body}\n')
            count += 1
        stats[cat] = count
    print(json.dumps(stats, indent=2))

if __name__ == '__main__':
    main()
