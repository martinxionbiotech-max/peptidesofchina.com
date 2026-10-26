#!/usr/bin/env python3
"""P0-1: MOQ 统一 — 源站新闻宣布最低订购额 $300 → $600，全站统一到 $600。
只替换 MOQ 语境，保留 $3,500 折扣门槛与价格表数值。"""
import re, glob

# 精确语境替换（不含 $3,500 与 $xxx.00 价格）
PATTERNS = [
    (r'minimum is \$300', 'minimum is $600'),
    (r'\$300 in goods', '$600 in goods'),
    (r'\$300 minimum', '$600 minimum'),
    (r'below \$300', 'below $600'),
    (r'reach \$300', 'reach $600'),
    (r'Minimum Order: \$300', 'Minimum Order: $600'),
    (r'minimum order of \$300', 'minimum order of $600'),
    (r'\$300 per supplier', '$600 per supplier'),
    (r'minimum is \$600(?![\d.])', 'minimum is $600'),
    (r'of \$300 as a first-order trial', 'of $600 as a first-order trial'),
    (r'subject to a \$300 minimum', 'subject to a $600 minimum'),
    (r'\$300 total minimum', '$600 total minimum'),
]

def fix(path):
    raw = open(path, encoding='utf-8').read()
    new = raw
    for pat, rep in PATTERNS:
        new = re.sub(pat, rep, new)
    # 防止误伤 $3,500（理论上 PATTERNS 不含）
    if '$3,500' not in new and '$3,500' in raw:
        pass  # 不会发生，仅防御
    if new != raw:
        open(path, 'w', encoding='utf-8').write(new)
        return True
    return False

count = 0
for path in glob.glob('src/content/**/*.md', recursive=True) + glob.glob('src/pages/**/*.astro', recursive=True):
    if fix(path):
        count += 1
print(f'MOQ 统一修复: {count} 文件')
