#!/usr/bin/env python3
"""Peptides of China — content pipeline: crawled HTML → clean markdown collections.
Stage 1: clean-text extraction per page with section detection.
"""
import json, re, html, os, sys

SRC = '.crawl-src'
OUT = 'src/content'

NAV_NOISE = [
    'Peptides From China Catalog Customization Blog How It Works How to Pay Track Order FAQ Contact News',
    'Home › Catalog ›', 'Home · Catalog ·',
]

def clean(text):
    text = html.unescape(text)
    text = re.sub(r'\s+', ' ', text)
    return text.strip()

def extract_main(page):
    """Return (title, body_text) with nav/footer noise stripped."""
    t = page['text']
    # strip leading comments artifacts
    t = re.sub(r'^.*?-->', ' ', t, count=1)
    for n in NAV_NOISE:
        t = t.replace(n, ' ')
    # cut trailing noise
    for marker in ['Copyright', 'All rights reserved', '© 2026', '© 2025', 'Privacy Policy Peptides']:
        i = t.find(marker)
        if i > 500:
            t = t[:i]
    return clean(t)

def main():
    pages = json.load(open(os.path.join(SRC, 'pages-full.json'), encoding='utf-8'))
    products = json.load(open(os.path.join(SRC, 'products.json'), encoding='utf-8'))
    price_by_slug = {p['slug']: p for p in products}

    stats = {'products': 0, 'blog': 0, 'news': 0, 'pages': 0, 'compare': 0, 'static': 0, 'catalog': 0, 'skipped': 0}
    for p in pages:
        cat = p['cat']
        if cat == 'home':
            continue  # homepage built by hand in pages/index.astro
        slug = p['slug']
        body = extract_main(p)
        if len(body.split()) < 60:
            stats['skipped'] += 1
            continue
        if cat == 'catalog':
            if slug not in price_by_slug:
                stats['skipped'] += 1
                continue
            prod = price_by_slug[slug]
            d = os.path.join(OUT, 'products', slug[0].lower())
            os.makedirs(d, exist_ok=True)
            path = os.path.join(d, f'{slug}.md')
            fm = {
                'title': f"Buy {prod['name'] or slug.replace('-', ' ').title()} — Research Grade | Peptides of China",
                'name': prod['name'] or slug,
                'slug': slug,
                'price': prod['price'],
                'status': 'In Stock',
            }
        elif cat == 'blog':
            path = os.path.join(OUT, 'blog', f'{slug}.md')
            title = p['title'] if p['title'] and p['title'] != 'Peptides From China' else slug.replace('-', ' ').title()
            fm = {'title': title, 'slug': slug}
        elif cat == 'news':
            path = os.path.join(OUT, 'news', f'{slug}.md')
            title = p['title'] if p['title'] and p['title'] != 'Peptides From China' else slug.replace('-', ' ').title()
            fm = {'title': title, 'slug': slug}
        else:
            path = os.path.join(OUT, 'pages', f'{slug}.md')
            title = p['title'] if p['title'] and p['title'] != 'Peptides From China' else slug.replace('-', ' ').title()
            fm = {'title': title, 'slug': slug}
        fm['description'] = (p.get('desc') or body[:160])[:200]
        os.makedirs(os.path.dirname(path), exist_ok=True)
        with open(path, 'w', encoding='utf-8') as f:
            f.write('---\n')
            for k, v in fm.items():
                f.write(f'{k}: {json.dumps(v, ensure_ascii=False)}\n')
            f.write('---\n\n')
            f.write(f'# {fm["title"]}\n\n')
            f.write(body)
            f.write('\n')
        stats[cat] += 1
    print(json.dumps(stats, indent=2))

if __name__ == '__main__':
    main()
