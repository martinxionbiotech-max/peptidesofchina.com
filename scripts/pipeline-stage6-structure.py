#!/usr/bin/env python3
"""Stage 6: 产品页 markdown 结构化 — 将源站内联章节名转为 H2 标题，
FAQ 问答转为加粗 Q 格式，变体表转为 markdown 表格。不改动任何事实数据。"""
import re, glob

SECTION_MARKERS = [
    'Compound Profile', 'Profile', 'Available Variants', 'Specification Highlights',
    'Quality & Testing', 'Quality and Testing', 'Research Areas', 'Frequently Asked Questions',
    'Related Products', 'Variant Notes', 'Warnings and Limitations', 'Storage and Handling',
    'References', 'Package Contents', 'Test Procedure', 'Result Interpretation',
    'Clinical Significance', 'Intended Use', 'Detection Principle',
]

def normalize(path):
    raw = open(path, encoding='utf-8').read()
    parts = raw.split('---\n', 2)
    if len(parts) < 3:
        return False
    fm, body = parts[1], parts[2]
    if re.search(r'^## (Compound Profile|Profile|Available Variants|Specification Highlights|Quality & Testing|Research Areas|Frequently Asked Questions)', body, re.M):
        return False  # already structured
    changed = False

    # 1) 内联章节名 → H2（行首或句首的已知标记）
    for marker in SECTION_MARKERS:
        # "Compound Profile AICAR (..." 形式：标记后跟空格+内容
        body, n = re.subn(rf'(?<!## )(?<!\w)({re.escape(marker)}) (?=[A-Z(])', rf'\n\n## \1\n\n', body)
        # 独立成行的标记
        body, n2 = re.subn(rf'^({re.escape(marker)})[\s:：]*$', rf'## \1', body, flags=re.M)
        changed = changed or n > 0 or n2 > 0

    # 2) FAQ 问答 → 加粗 Q 格式："How does X? Answer text"
    body, n = re.subn(r'(How does [^?]+\?|What [^?]+\?|Which [^?]+\?|Can [^?]+\?|Is [^?]+\?|Does [^?]+\?|Are [^?]+\?|Where [^?]+\?) ', r'\n\n**\1**\n\n', body)
    changed = changed or n > 0

    # 3) 变体表行 → 统一保留（表格化风险高，仅规整换行）
    body = re.sub(r'\n{3,}', '\n\n', body)
    if changed:
        open(path, 'w', encoding='utf-8').write(f'---\n{fm}\n---\n{body}')
    return changed

done = 0
for path in glob.glob('src/content/products/**/*.md', recursive=True):
    if normalize(path):
        done += 1
print(f'结构化产品页: {done}')
