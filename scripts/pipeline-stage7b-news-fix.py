#!/usr/bin/env python3
"""Stage 7b: 修复新闻页内容丢失 — 从爬取页重新提取公告正文。
Stage 7 的整行删除误伤单行公告正文；此处按 'Announcement YYYY-MM-DD' 标记精准截取。"""
import re, html, glob, os

def extract_announcement(crawl_file: str) -> str:
    raw = open(crawl_file, encoding='utf-8', errors='ignore').read()
    text = re.sub(r'<script[^>]*>.*?</script>|<style[^>]*>.*?</style>', ' ', raw, flags=re.S)
    text = html.unescape(re.sub(r'<[^>]+>', ' ', text))
    text = re.sub(r'\s+', ' ', text).strip()
    # 公告正文起点：Announcement 日期标记
    i = text.find('Announcement 20')
    if i < 0:
        return ''
    body = text[i:]
    # 去掉 "Announcement YYYY-MM-DD" 前缀
    body = re.sub(r'^Announcement \d{4}-\d{2}-\d{2} ', '', body)
    # 去掉紧跟其后的重复标题（页面 title 会在正文前重复一次）
    # 尾部噪声截止
    for marker in ['Platform Catalog Customization', 'Popular Peptides', 'Legal Terms', 'Track Your Order']:
        j = body.find(marker)
        if j > 200:
            body = body[:j]
    return body.strip()

def main():
    fixed = 0
    for path in glob.glob('src/content/news/*.md'):
        raw = open(path, encoding='utf-8').read()
        parts = raw.split('---\n', 2)
        if len(parts) < 3:
            continue
        fm, body = parts[1], parts[2]
        m = re.search(r'slug: "([^"]+)"', fm)
        slug = m.group(1) if m else ''
        if not slug or slug == '__news':
            continue
        crawl = f'.crawl-src/pages/__news__{slug}'
        if not os.path.exists(crawl):
            crawl = f'.crawl-src/pages/__news__{slug}.html'
        if not os.path.exists(crawl):
            continue
        announce = extract_announcement(crawl)
        if not announce:
            continue
        # 现有 body 若已含公告正文（>200词）则跳过
        if len(body.split()) > 200 and announce.split()[0][:20] in body:
            continue
        intro = ("Peptides of China — our platform for **china peptides** sourcing — publishes short updates "
                 "like this one whenever something material changes: catalog additions, quality-process notes, "
                 "and sourcing announcements. The substance of this update is below.\n\n")
        closer = ("\n\n## China Peptides Sourcing Perspective\n\n"
                  "For catalog listings, batch specifications, and ordering information, see the [catalog](/catalog/) "
                  "or [how sourcing works](/how-it-works/).\n")
        # H1 + 公告正文
        m2 = re.search(r'title: "([^"]+)"', fm)
        title = m2.group(1) if m2 else slug
        new_body = f"{intro}# {title}\n\n{announce}{closer}"
        open(path, 'w', encoding='utf-8').write(f'---\n{fm}\n---\n{new_body}')
        fixed += 1
    print(f'新闻正文修复: {fixed}')

if __name__ == '__main__':
    main()
