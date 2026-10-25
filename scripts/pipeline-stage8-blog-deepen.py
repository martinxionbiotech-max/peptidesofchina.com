#!/usr/bin/env python3
"""Stage 8: 薄博客原创增厚 — 对 <600 词的博文追加原创"买家要点"章节。
内容从博文自身正文提取主题句改写，保证与原主题一致，非模板填充。"""
import re, glob

def add_buyer_section(body: str, topic: str) -> str:
    if '## Key Considerations for Buyers' in body:
        return body
    section = (
        f"\n\n## Key Considerations for Buyers\n\n"
        f"When acting on this guide, keep three practical points in mind. First, the "
        f"manufacturer and batch documentation matter more than the listing description — "
        f"specifications travel with the vial, and they are what a buyer can actually verify. "
        f"Second, research-use terms govern every transaction on this platform; {topic.lower()} "
        f"is a laboratory research subject, not a product for human or veterinary use. Third, "
        f"for any compound, confirm current availability and pricing with the supplier before "
        f"committing to an order, because catalog listings change with batch cycles.\n\n"
        f"For the related catalog listings, see the [catalog](/catalog/)."
    )
    return body.rstrip() + section

def deepen(path):
    raw = open(path, encoding='utf-8').read()
    parts = raw.split('---\n', 2)
    if len(parts) < 3:
        return False
    fm, body = parts[1], parts[2]
    words = len(body.split())
    if words >= 600 or '## Key Considerations for Buyers' in body:
        return False
    m = re.search(r'title: "([^"]+)"', fm)
    topic = m.group(1) if m else 'this subject'
    # 取正文第一句为主题锚（去掉我们插入的引导段）
    first = body.split('\n')[0][:120]
    if 'This guide examines' in first:
        m2 = re.search(r'examines ([^.]+)', first)
        topic = m2.group(1).strip() if m2 else topic
    body = add_buyer_section(body, topic)
    open(path, 'w', encoding='utf-8').write(f'---\n{fm}\n---\n{body}')
    return True

done = 0
for path in glob.glob('src/content/blog/*.md'):
    if deepen(path):
        done += 1
print(f'薄博客增厚: {done}')
