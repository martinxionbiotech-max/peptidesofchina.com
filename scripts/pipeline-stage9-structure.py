#!/usr/bin/env python3
"""Stage 9: rebuild body structure for pages/blog/news from the original crawl HTML."""
import html
import os
import pathlib
import re
import sys
from collections import Counter
from html.parser import HTMLParser

REPO = pathlib.Path(os.environ.get('POC_REPO', '/home/openclaw/peptidesofchina.com'))
SRC = REPO / '.crawl-src/pages'
CONTAINERS = {'div', 'section', 'article', 'aside', 'main', 'header', 'footer',
              'nav', 'figure', 'picture', 'details', 'homepage'}
SKIP_TAGS = {'script', 'style', 'noscript', 'meta', 'link', 'svg', 'source'}


class Node:
    __slots__ = ('tag', 'attrs', 'children')
    def __init__(self, tag, attrs):
        self.tag = tag
        self.attrs = attrs
        self.children = []


def parse_fragment(fragment):
    root = Node('root', {})
    stack = [root]
    class P(HTMLParser):
        def __init__(self):
            super().__init__(convert_charrefs=True)
        def handle_starttag(self, tag, attrs):
            node = Node(tag, dict(attrs))
            stack[-1].children.append(node)
            stack.append(node)
            if tag in ('br', 'hr', 'img', 'input', 'meta', 'link', 'source', 'area', 'base', 'col', 'embed', 'track', 'wbr', 'param'):
                stack.pop()
        def handle_startendtag(self, tag, attrs):
            self.handle_starttag(tag, attrs)
        def handle_endtag(self, tag):
            if len(stack) > 1:
                stack.pop()
        def handle_data(self, data):
            stack[-1].children.append(('text', data))
    p = P()
    p.feed(fragment)
    p.close()
    return root


def raw_text(node):
    out = []
    def walk(n):
        if isinstance(n, tuple):
            out.append(n[1])
        else:
            for c in n.children:
                walk(c)
    walk(node)
    t = ''.join(out)
    t = re.sub(r'[ \t]+', ' ', t)
    t = re.sub(r'\n +', '\n', t)
    t = re.sub(r' +\n', '\n', t)
    return t.strip()


def inline_text(node):
    out = []
    def walk(n):
        if isinstance(n, tuple):
            out.append(n[1])
        else:
            for c in n.children:
                walk(c)
    walk(node)
    return re.sub(r'\s+', ' ', html.unescape(''.join(out))).strip()


def map_href(href):
    if not href:
        return None
    href = href.strip()
    href = re.sub(r'^https?://(www\.)?peptides(fromchina\.co|ofchina\.com)', '', href)
    if href in ('', '#', '/'):
        return None
    if href.startswith('/api/'):
        return None
    return href


class Renderer:
    def __init__(self, frontmatter_title, faq_bold, h1_text=''):
        self.title = re.sub(r'\s+', ' ', frontmatter_title or '').strip().lower()
        self.h1 = re.sub(r'\s+', ' ', h1_text or '').strip().lower()
        self.faq_bold = faq_bold
        self.blocks = []

    def emit(self, text):
        text = text.strip()
        if text:
            self.blocks.append(text)

    def render_node(self, node):
        tag = node.tag
        if tag in SKIP_TAGS or tag == 'img':
            return
        if tag == 'h1':
            return
        if tag in ('h2', 'h3', 'h4'):
            text = self.render_inline(node.children, strip_md=True)
            if not text:
                return
            if tag == 'h2' and text.lower() in (self.title, self.h1):
                return
            if tag == 'h3' and self.faq_bold:
                self.emit(f'**{text}**')
            else:
                level = {'h2': '##', 'h3': '###', 'h4': '####'}[tag]
                self.emit(f'{level} {text}')
            return
        if tag == 'p':
            table = self.try_table(node)
            if table:
                for line in table:
                    self.emit(line)
                return
            self.emit(self.render_inline(node.children))
            return
        if tag in ('ul', 'ol'):
            self.render_list(node)
            return
        if tag == 'blockquote':
            saved = self.blocks
            self.blocks = []
            for c in node.children:
                if not isinstance(c, tuple):
                    self.render_node(c)
            inner = self.blocks
            self.blocks = saved
            for line in inner:
                self.emit('> ' + line)
            return
        if tag == 'pre':
            self.emit('```\n' + inline_text(node) + '\n```')
            return
        if tag == 'hr':
            self.emit('---')
            return
        if tag == 'table':
            self.render_table(node)
            return
        if tag == 'li':
            return
        if tag == 'figcaption':
            self.emit('*' + self.render_inline(node.children) + '*')
            return
        if tag in ('strong', 'b', 'em', 'i', 'a', 'code', 'span', 'small', 'u', 'br'):
            text = self.render_inline([node])
            if text:
                self.emit(text)
            return
        for c in node.children:
            if not isinstance(c, tuple):
                self.render_node(c)

    def try_table(self, node):
        rt = raw_text(node)
        rows = re.split(r'\n\s*\n', rt)
        if len(rows) < 3:
            return None
        header = [c.strip() for c in rows[0].split('\n') if c.strip()]
        if not (2 <= len(header) <= 6) or any(len(h) > 40 for h in header):
            return None
        table_rows = []
        for r in rows[1:]:
            cells = [c.strip() for c in r.split('\n') if c.strip()]
            if len(cells) < len(header):
                return None
            if len(cells) > len(header):
                cells = cells[:len(header) - 1] + [' '.join(cells[len(header) - 1:])]
            if len(cells[0]) > 60:
                return None
            table_rows.append(cells)
        esc = lambda x: x.replace('|', '\\|').strip()
        out = ['| ' + ' | '.join(esc(h) for h in header) + ' |',
               '| ' + ' | '.join('---' for _ in header) + ' |']
        for r in table_rows:
            out.append('| ' + ' | '.join(esc(c) for c in r) + ' |')
        return out

    def li_blocks(self, li):
        blocks = []
        buf = []
        def flush():
            if buf:
                t = self.render_inline(buf)
                if t:
                    blocks.append(t)
                buf.clear()
        for c in li.children:
            if isinstance(c, tuple):
                buf.append(c)
                continue
            if c.tag in ('strong', 'b', 'em', 'i', 'a', 'code', 'span', 'small', 'u', 'br'):
                buf.append(c)
                continue
            flush()
            saved = self.blocks
            self.blocks = []
            self.render_node(c)
            blocks.extend(self.blocks)
            self.blocks = saved
        flush()
        return [b for b in blocks if b.strip()]

    def render_list(self, node):
        for i, li in enumerate(node.children):
            if isinstance(li, tuple):
                continue
            if li.tag != 'li':
                self.render_node(li)
                continue
            marker = '- ' if node.tag == 'ul' else f'{i + 1}. '
            blocks = self.li_blocks(li)
            if not blocks:
                continue
            if len(blocks) == 1:
                self.emit(marker + blocks[0])
                continue
            first = blocks[0]
            if first.startswith('#'):
                self.emit(marker + '**' + first.lstrip('#').strip() + '**')
                rest = blocks[1:]
            else:
                if all(not b.startswith(('- ', '* ', '|', '>', '#', '```', '*')) for b in blocks[1:]):
                    self.emit(marker + ' '.join(blocks))
                    continue
                self.emit(marker + first)
                rest = blocks[1:]
            for b in rest:
                self.emit('    ' + b)

    def render_table(self, node):
        rows = []
        for r in node.children:
            if isinstance(r, tuple):
                continue
            if r.tag != 'tr':
                self.render_node(r)
                continue
            cells = []
            for c in r.children:
                if isinstance(c, tuple):
                    continue
                if c.tag in ('th', 'td'):
                    cells.append(inline_text(c))
            rows.append(cells)
        if not rows:
            return
        width = max(len(r) for r in rows)
        rows = [r + [''] * (width - len(r)) for r in rows]
        esc = lambda s: s.replace('|', '\\|').strip()
        self.emit('| ' + ' | '.join(esc(c) for c in rows[0]) + ' |')
        self.emit('| ' + ' | '.join('---' for _ in range(width)) + ' |')
        for r in rows[1:]:
            self.emit('| ' + ' | '.join(esc(c) for c in r) + ' |')

    def render_inline(self, children, strip_md=False):
        parts = []
        def raw_inline(node):
            out = []
            def walk(n):
                if isinstance(n, tuple):
                    out.append(n[1])
                else:
                    for c in n.children:
                        walk(c)
            walk(node)
            return re.sub(r'\s+', ' ', html.unescape(''.join(out)))
        def walk(nodes):
            for n in nodes:
                if isinstance(n, tuple):
                    parts.append(n[1])
                    continue
                t = n.tag
                if t in SKIP_TAGS or t in ('img', 'picture'):
                    continue
                if t == 'br':
                    parts.append('\n')
                    continue
                if t == 'a':
                    href = map_href(n.attrs.get('href'))
                    raw = raw_inline(n)
                    txt = raw.strip()
                    if raw[:1].isspace() and parts:
                        parts.append(' ')
                    if href and txt and href != txt:
                        parts.append(f'[{txt}]({href})')
                    else:
                        parts.append(txt)
                    if raw[-1:].isspace() and txt:
                        parts.append(' ')
                    continue
                if t in ('strong', 'b'):
                    raw = raw_inline(n)
                    txt = raw.strip()
                    if not txt:
                        continue
                    if raw[:1].isspace() and parts:
                        parts.append(' ')
                    parts.append(txt if strip_md else f'**{txt}**')
                    if raw[-1:].isspace():
                        parts.append(' ')
                    continue
                if t in ('em', 'i'):
                    raw = raw_inline(n)
                    txt = raw.strip()
                    if not txt:
                        continue
                    if raw[:1].isspace() and parts:
                        parts.append(' ')
                    parts.append(txt if strip_md else f'*{txt}*')
                    if raw[-1:].isspace():
                        parts.append(' ')
                    continue
                if t == 'code':
                    parts.append(inline_text(n))
                    continue
                walk(n.children)
        walk(children)
        text = ''.join(parts)
        text = html.unescape(text)
        text = re.sub(r'\]\([^)]*\)(?=[A-Za-z\[])', lambda m: m.group(0) + ' ', text)
        text = re.sub(r'[ \t]+', ' ', text)
        text = re.sub(r' *\n *', '\n', text)
        text = re.sub(r'\n{3,}', '\n\n', text)
        return text.strip()


def split_parts(content):
    m = re.match(r'^(---\n.*?\n---\n)(.*)$', content, re.S)
    fm = m.group(1)
    body = m.group(2)
    lines = body.split('\n')
    flat_idx = max(range(len(lines)), key=lambda i: len(lines[i]))
    flat = lines[flat_idx]
    if len(flat) < 400 and '›' not in flat:
        return fm, lines, None, []
    return fm, lines[:flat_idx], flat, lines[flat_idx + 1:]


def _listy(line):
    return bool(re.match(r'^(\s*[-*]\s|\s*\d+\.\s|\|)', line))


def tighten(text):
    lines = text.split('\n')
    res = []
    for i, line in enumerate(lines):
        if line == '' and res and _listy(res[-1]):
            nxt = next((l for l in lines[i + 1:] if l.strip() != ''), None)
            if nxt is not None and _listy(nxt):
                continue
        res.append(line)
    return '\n'.join(res).strip()


def bold_labels_to_h2(body):
    existing = set(x.lower() for x in re.findall(r'^#{1,6}\s+(.*)$', body, re.M))
    out = []
    for line in body.split('\n'):
        m = re.match(r'^\*\*([^*\n]{3,90})\*\*\s*$', line)
        if m:
            label = m.group(1).strip()
            if label and label[-1] not in '.!?,;:' and label.lower() not in existing:
                line = '## ' + label
                existing.add(label.lower())
        out.append(line)
    return '\n'.join(out)


def post_process(body, filename):
    if filename == 'reviews.md':
        body = re.sub(r'^\*\*([^*\n]+?)\*\* (★+ )?(\d{4}-\d{2}-\d{2})$',
                      lambda m: f'### {m.group(1)} {m.group(2) or ""}· {m.group(3)}'.replace('  ', ' '),
                      body, flags=re.M)
    if filename == 'how-it-works.md':
        rows = re.search(r'- \*\*Minimum Order:\*\*[^\n]*\n(?:(?:- \*\*[^*\n]+:\*\*[^\n]*\n)*)', body)
        if rows:
            block = rows.group(0)
            table = ['| Condition | Details |', '| --- | --- |']
            for key, val in re.findall(r'- \*\*([^*]+):\*\* (.*)', block):
                table.append(f'| {key.strip()} | {val.strip()} |')
            body = body.replace(block, '\n'.join(table) + '\n')
    return body


def brand_rename(text):
    text = re.sub(r'https?://(www\.)?peptidesfromchina\.(co|com)', 'https://peptidesofchina.com', text)
    text = re.sub(r'\bpeptidesfromchina\.(co|com)\b', 'peptidesofchina.com', text, flags=re.I)
    text = re.sub(r'\bPFC\b', 'Peptides of China', text)
    text = text.replace('Peptidesfromchina', 'Peptides of China')
    text = text.replace('Peptides From China', 'Peptides of China')
    text = text.replace('PeptidesFromChina', 'Peptides of China')
    return text


def build(md_path, html_path, faq_bold=False):
    content = pathlib.Path(md_path).read_text()
    fm, intro, flat, trailing = split_parts(content)
    title_m = re.search(r'^title:\s*"(.*)"\s*$', fm, re.M)
    title = title_m.group(1) if title_m else ''
    desc_m = re.search(r'^description:\s*"(.*)"\s*$', fm, re.M)
    desc = desc_m.group(1) if desc_m else ''

    raw = pathlib.Path(html_path).read_text()
    start = raw.find('<nav aria-label="Breadcrumb"')
    start = raw.find('</nav>', start) + len('</nav>') if start != -1 else raw.find('id="root"')
    end = raw.find('<footer')
    fragment = raw[start:end if end != -1 else len(raw)]
    if not fragment.strip():
        raise ValueError(f'empty fragment for {md_path}')
    root = parse_fragment(fragment)

    def find_h1_container(node):
        for c in node.children:
            if not isinstance(c, tuple) and c.tag == 'h1':
                return node
        for c in node.children:
            if not isinstance(c, tuple):
                got = find_h1_container(c)
                if got is not None:
                    return got
        return None

    container = find_h1_container(root) or root
    h1_text = next((inline_text(n) for n in container.children
                    if not isinstance(n, tuple) and n.tag == 'h1'), '')

    def clean(nodes):
        out = []
        for n in nodes:
            if isinstance(n, tuple):
                continue
            if n.tag in ('time', 'h1'):
                continue
            if n.tag == 'p' and n.attrs.get('class') == 'article-label':
                continue
            if n.tag == 'p' and n.attrs.get('class') == 'lead':
                lead = inline_text(n)
                if lead == desc or lead == title:
                    continue
            out.append(n)
        return out
    container.children = clean(container.children)
    render_nodes = list(container.children)
    for i, n in enumerate(root.children):
        if n is container:
            render_nodes += [x for x in root.children[i + 1:] if not isinstance(x, tuple)]
            break

    r = Renderer(title, faq_bold=faq_bold, h1_text=h1_text)
    for c in render_nodes:
        r.render_node(c)
    structured = brand_rename(tighten('\n\n'.join(r.blocks)))

    if flat is None:
        for i, line in enumerate(intro):
            if line.strip().startswith('## '):
                trailing = intro[i:]
                intro = intro[:i]
                break
    parts = []
    intro_text = '\n'.join(intro).strip()
    if intro_text:
        parts.append(intro_text)
    if structured:
        parts.append(structured)
    trailing_text = '\n'.join(trailing).strip()
    if trailing_text:
        parts.append(trailing_text)
    new_body = '\n\n'.join(parts)
    new_body = post_process(new_body, pathlib.Path(md_path).name)
    if str(md_path).split('/content/')[1].split('/')[0] in ('blog', 'news'):
        new_body = bold_labels_to_h2(new_body)
    return fm + new_body.rstrip() + '\n', flat


def html_for(cat, slug):
    if cat == 'pages':
        for cand in (f'__{slug}', f'__compare__{slug}'):
            p = SRC / cand
            if p.exists():
                return p
        return None
    cand = f'__{cat}__{slug}'
    p = SRC / cand
    if p.exists():
        return p
    if cat == 'news':
        p2 = SRC / f'__news__{slug.replace("peptidesofchina", "peptidesfromchina")}'
        if p2.exists():
            return p2
    return None


def words(text):
    text = re.sub(r'peptides(from|of)china\.(com|co)', 'DOMAIN', text, flags=re.I)
    text = text.replace('**', ' ').replace('*', ' ').replace('`', ' ').replace('|', ' ')
    text = re.sub(r'\[[^\]]*\]\([^)]*\)', lambda m: m.group(0)[1:m.group(0).index(']')], text)
    text = re.sub(r'(?m)^\s*(?:\d+[.)]\s+|[-*]\s+|>\s?)', '', text)
    toks = re.findall(r"[a-z0-9$%''’]+", text.lower())
    return [re.sub(r"[’']s$", '', t) for t in toks]


def loss_check(new_content, old_content, title, desc):
    fm, body = old_content.split('---\n', 2)[1], old_content.split('---\n', 2)[2]
    lines = body.split('\n')
    flat = max(lines, key=len) if lines else ''
    if len(flat) < 400 and '›' not in flat:
        flat = ''
    old_flat = Counter(words(flat))
    new_body = new_content.split('---\n', 2)[2]
    new_all = Counter(words(new_body))
    lost = old_flat - new_all
    noise = set(words((title or '') + ' ' + (desc or '') + ' home blog news pfc peptides from china of and the a to in for is on are with this our by as at it that or an be com co'))
    import datetime
    out = {}
    for w, c in lost.items():
        if w in noise:
            continue
        if re.fullmatch(r'\d{4}-\d{2}-\d{2}|\d{1,4}|[a-z]', w):
            continue
        out[w] = c
    return out


def verify(new_content, old_content):
    old = Counter(words(old_content.replace('Peptides of China', 'PFC').replace('Peptides From China', 'PFC')))
    new = Counter(words(new_content.split('---\n', 2)[2]))
    missing = new - old
    # mask brand expansions: PFC/Peptides From China -> Peptides of China (one per occurrence)
    import itertools
    for _ in range(max(1, missing.get('peptides', 0) + missing.get('china', 0))):
        for w in ('peptides', 'of', 'china'):
            if missing.get(w, 0) > 0:
                missing[w] -= 1
        if all(missing.get(w, 0) <= 0 for w in ('peptides', 'of', 'china')):
            break
    for w in list(missing):
        if missing[w] <= 0:
            del missing[w]
    return missing


if __name__ == '__main__':
    import os
    if len(sys.argv) > 1 and sys.argv[1] == 'dry':
        # preview a single file
        cat, md = sys.argv[2], sys.argv[3]
        md_path = str(REPO / f'src/content/{cat}/{md}')
        hp = html_for(cat, md.removesuffix(".md"))
        new, flat = build(md_path, str(hp))
        print(new)
        sys.exit(0)
    def transform_contact():
        md = REPO / 'src/content/pages/contact.md'
        content = md.read_text()
        fm, body = content.split('---\n', 2)[1], content.split('---\n', 2)[2]
        out = []
        for line in body.split('\n'):
            m = re.match(r'^\*\*([^*\n]+)\*\*\s*(?:—\s*(.*))?$', line)
            if m:
                label = m.group(1).strip()
                rest = (m.group(2) or '').strip()
                if label in ('Contact channels', 'What to include in your message'):
                    out.append('## ' + label)
                elif rest:
                    out.append('## ' + label)
                    out.append('')
                    out.append(rest)
                else:
                    out.append(line)
                continue
            out.append(line)
        md.write_text('---\n' + fm + '---\n' + '\n'.join(out).strip() + '\n')

    transform_contact()
    targets = []
    for cat in ('pages', 'blog', 'news'):
        for p in sorted((REPO / f'src/content/{cat}').glob('*.md')):
            targets.append((cat, p))
    stats = Counter()
    problems = []
    for cat, md in targets:
        if md.name == 'contact.md':
            stats['skipped'] += 1
            continue
        hp = html_for(cat, md.stem)
        if not hp:
            problems.append(f'no html: {md}')
            stats['missing'] += 1
            continue
        old_content = md.read_text()
        title = re.search(r'^title:\s*"(.*)"\s*$', old_content, re.M)
        title = title.group(1) if title else ''
        desc = re.search(r'^description:\s*"(.*)"\s*$', old_content, re.M)
        desc = desc.group(1) if desc else ''
        new_content, _ = build(str(md), str(hp), faq_bold=(md.name == 'faq.md'))
        missing = verify(new_content, old_content)
        if missing:
            problems.append(f'{md.name}: unexpected new words {dict(list(missing.items())[:10])}')
        lost = loss_check(new_content, old_content, title, desc)
        if lost:
            problems.append(f'{md.name}: POSSIBLE LOSS {dict(list(lost.items())[:12])}')
        md.write_text(new_content)
        stats['converted'] += 1
    print(f"converted={stats['converted']} skipped={stats['skipped']} missing={stats['missing']}")
    for p in problems:
        print('PROBLEM', p)
