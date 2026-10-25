#!/usr/bin/env python3
"""Stage 10 (v2): 产品正文平铺变体数据 → markdown 管道表格（去掉 Price 列——页面不显示价格）。
用正则按行模式提取：name / strength / pack / purity / availability / price。
仅处理 '## Available Variants' 区块内文本。"""
import re, glob

ROW = re.compile(
    r'(?P<name>[A-Za-z0-9\-+./()]+(?:\s+[A-Za-z0-9\-+./()]+)*?)\s+'
    r'(?P<strength>\d+(?:\s*\+\s*\d+)?\s*(?:mg|ml|mL|IU|iu|ui|mcg|μg|units|mg/tablet|iu/ml|mg/ml)|\d+\s*(?:ml|mL)\s*·\s*[\d.]+\s*mg/mL)?\s+'
    r'(?P<pack>\d+\s*(?:vials|vial|ml|tablets)|\d+\s*×\s*\d+\s*(?:ml|mL)\s*ampoules|\d+\s*×\s*\d+\s*(?:ml|mL)\s*(?:vials|vial))?\s+'
    r'(?P<purity>—|≥\d+%|>=\d+%|Pharmaceutical grade|N/A|[A-Za-z0-9 .]*?)\s+'
    r'(?P<avail>In Stock|Pre-Order|Out of Stock)\s+'
    r'\$(?P<price>[\d,.]+)'
)

def convert_variants_block(block: str) -> str:
    # 去掉头部 "Name Strength Pack Size Purity Availability Price (USD)"
    header = re.sub(r'^Name Strength Pack Size Purity Availability Price \(USD\)\s*', '', block.strip())
    rows = []
    for m in ROW.finditer(header):
        name = m.group('name').strip()
        strength = (m.group('strength') or '').strip()
        pack = (m.group('pack') or '').strip()
        purity = (m.group('purity') or '').strip()
        avail = m.group('avail')
        if not name:
            continue
        rows.append((name, strength, pack, purity, avail))
    if not rows:
        return block  # 无法解析，保持原样
    lines = ['| Name | Strength | Pack Size | Purity | Availability |',
             '| --- | --- | --- | --- | --- |']
    for name, strength, pack, purity, avail in rows:
        lines.append(f'| {name} | {strength} | {pack} | {purity} | {avail} |')
    return '\n'.join(lines)

def process(path):
    raw = open(path, encoding='utf-8').read()
    parts = raw.split('---\n', 2)
    if len(parts) < 3:
        return False
    fm, body = parts[1], parts[2]
    if re.search(r'^\| --- \|', body, re.M):
        return False  # 已是表格
    m = re.search(r'## Available Variants\n+(.*?)(?=\n## |\Z)', body, re.S)
    if not m:
        return False
    block = m.group(1)
    table = convert_variants_block(block)
    if table == block:
        return False
    body = body.replace(block, table + '\n')
    open(path, 'w', encoding='utf-8').write(f'---\n{fm}\n---\n{body}')
    return True

done = 0
failed = []
for path in glob.glob('src/content/products/**/*.md', recursive=True):
    if process(path):
        done += 1
    else:
        m2 = re.search(r'## Available Variants', open(path, encoding='utf-8').read())
        if m2:
            failed.append(path)
print(f'表格化: {done} | 无法解析: {len(failed)}')
for f in failed[:8]:
    print(' ', f)
