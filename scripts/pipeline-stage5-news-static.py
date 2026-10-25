#!/usr/bin/env python3
"""Stage 5: news + 静态页扩展 — 原创品牌语境段落 + 关键词集成。"""
import re, glob

NEWS_INTRO = ("Peptides of China — our platform for **china peptides** sourcing — publishes short updates "
              "like this one whenever something material changes: catalog additions, quality-process notes, "
              "and sourcing announcements. The substance of this update is below.")

STATIC_KEYS = {
    'how-it-works': 'This page explains how **china peptide** orders move from catalog selection to delivery.',
    'peptide-quality': 'This page sets out how we approach quality for **chinese peptides**: what is tested, what is documented, and what a buyer should ask for.',
    'company': 'Peptides of China is a B2B platform for **china peptides** — finished research compounds from established Chinese manufacturers.',
    'faq': 'The answers below cover the questions we most often hear from **china peptide** buyers.',
    'contact': 'Contact Peptides of China for **china peptide** sourcing, specification requests, and order support.',
    'custom-peptide-services': 'Custom peptide services extend our **china peptide** catalog to sequences not listed in stock.',
    'manufacturing-partners': 'Our **chinese peptides** catalog is supplied by established Chinese manufacturers vetted for finished-product capability.',
    'reviews': 'Buyer feedback on **china peptide** orders, published with identifying details removed.',
    'how-to-pay': 'Payment options for **china peptide** orders, including the methods we accept and why.',
    'shipping-and-reshipment-policy': 'Shipping and reshipment terms for **china peptide** orders, including tracking and reshipment conditions.',
    'refund-and-cancellation-policy': 'Refund and cancellation terms for **china peptide** orders.',
    'terms-and-conditions': 'The terms governing use of our platform and **china peptide** sourcing services.',
    'privacy-and-cookie-policy': 'How Peptides of China handles data for **china peptide** buyers and site visitors.',
    'research-use-disclaimer': 'The research-use terms that govern every **china peptide** in our catalog.',
    'amino-asylum-alternative': 'How Peptides of China compares as a **china peptide** sourcing alternative.',
    'peptide-sciences-alternative': 'How Peptides of China compares as a **china peptide** sourcing alternative to retail-focused suppliers.',
}

def main():
    stats = {'news': 0, 'pages': 0}
    # news
    for path in glob.glob('src/content/news/*.md'):
        raw = open(path, encoding='utf-8').read()
        parts = raw.split('---\n', 2)
        if len(parts) < 3:
            continue
        fm, body = parts[1], parts[2]
        if '## China Peptides Sourcing Perspective' in body and 'Peptides of China — our platform' in body:
            continue
        if 'Peptides of China — our platform' not in body:
            body = f"{NEWS_INTRO}\n\n{body}"
        if '## China Peptides Sourcing Perspective' not in body:
            body = body.rstrip() + "\n\n## China Peptides Sourcing Perspective\n\nFor catalog listings, batch specifications, and ordering information, see the [catalog](/catalog/) or [how sourcing works](/how-it-works/).\n"
        open(path, 'w', encoding='utf-8').write(f'---\n{fm}\n---\n{body}')
        stats['news'] += 1
    # static pages
    for path in glob.glob('src/content/pages/*.md'):
        raw = open(path, encoding='utf-8').read()
        parts = raw.split('---\n', 2)
        if len(parts) < 3:
            continue
        fm, body = parts[1], parts[2]
        m = re.search(r'slug: "([^"]+)"', fm)
        slug = m.group(1) if m else ''
        intro = STATIC_KEYS.get(slug)
        if intro and intro.split('.')[0][:40] not in body:
            body = f"{intro}\n\n{body}"
            open(path, 'w', encoding='utf-8').write(f'---\n{fm}\n---\n{body}')
            stats['pages'] += 1
    print(stats)

if __name__ == '__main__':
    main()
