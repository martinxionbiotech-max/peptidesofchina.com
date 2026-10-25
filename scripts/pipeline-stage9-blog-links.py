#!/usr/bin/env python3
"""Stage 9: blog 内链强化 — 正文中产品名自动链接到产品页 + 文末 Related Products 区块。
规则：仅在单词边界匹配产品名（≥4 字符或大写缩写），每篇最多 6 个产品链接，避免过度优化。"""
import re, glob, json

# 收集产品 slug→name
products = {}
for f in glob.glob('src/content/products/**/*.md', recursive=True):
    raw = open(f, encoding='utf-8').read()
    m = re.search(r'name: "([^"]+)"', raw)
    s = re.search(r'slug: "([^"]+)"', raw)
    if m and s:
        products[s.group(1)] = m.group(1)

# 排除过短/过泛的名字（避免误伤普通词）
def linkable(name: str) -> bool:
    if len(name) < 4:
        return False
    if name.lower() in ('humanin', 'shred', 'mgf'):  # 与普通词冲突的
        return False
    return True

# 按名字长度降序（长名优先匹配，避免 "BPC" 先于 "BPC-157" 命中）
names = sorted(((n, s) for s, n in products.items() if linkable(n)), key=lambda x: -len(x[0]))

def add_links(text: str) -> tuple[str, list[str]]:
    """返回 (新文本, 已链接的 slugs)。跳过已有 markdown 链接中的文本。"""
    # 先标记已有链接位置，避免在链接文本内再替换
    protected = []
    for m in re.finditer(r'\[[^\]]+\]\([^)]*\)', text):
        protected.append((m.start(), m.end()))
    def is_protected(start, end):
        return any(start < pe and end > ps for ps, pe in protected)

    used_slugs = []
    used_names = set()
    def repl(m):
        nonlocal used_slugs
        name = m.group(0)
        slug = name_to_slug[name]
        if slug in used_names:
            return name
        if is_protected(m.start(), m.end()):
            return name
        used_names.add(slug)
        used_slugs.append(slug)
        return f'[{name}](/catalog/{slug}/)'

    name_to_slug = {n: s for n, s in names}
    pattern = re.compile(r'(?<![A-Za-z0-9\-/])(?:' + '|'.join(re.escape(n) for n, _ in names) + r')(?![A-Za-z0-9\-])')
    # 第一次替换时限制数量：通过计数器在 repl 内控制
    count = {'n': 0}
    def repl_limited(m):
        name = m.group(0)
        if count['n'] >= 6:
            return name
        if name not in name_to_slug:
            return name
        if is_protected(m.start(), m.end()):
            return name
        slug = name_to_slug[name]
        if slug in used_names:
            return name
        used_names.add(slug)
        used_slugs.append(slug)
        count['n'] += 1
        return f'[{name}](/catalog/{slug}/)'

    new_text = pattern.sub(repl_limited, text)
    return new_text, used_slugs

DEFAULT_RELATED = ['bpc-157', 'semaglutide', 'tirzepatide', 'tb-500']

def main():
    stats = {'posts': 0, 'linked_posts': 0, 'total_links': 0}
    for path in glob.glob('src/content/blog/*.md'):
        raw = open(path, encoding='utf-8').read()
        parts = raw.split('---\n', 2)
        if len(parts) < 3:
            continue
        fm, body = parts[1], parts[2]
        if '## Related Products' in body:
            continue
        new_body, used = add_links(body)
        # 文末 Related Products 区块
        related = used[:4] if used else DEFAULT_RELATED
        items = '\n'.join(f'- [{products[s]}](/catalog/{s}/)' for s in related if s in products)
        if items:
            new_body = new_body.rstrip() + f'\n\n## Related Products\n\n{items}\n'
        if new_body != body:
            open(path, 'w', encoding='utf-8').write(f'---\n{fm}\n---\n{new_body}')
            stats['posts'] += 1
            stats['linked_posts'] += 1 if used else 0
            stats['total_links'] += len(used)
    print(stats)

if __name__ == '__main__':
    main()
