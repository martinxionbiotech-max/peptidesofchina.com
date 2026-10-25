#!/usr/bin/env python3
"""Stage 4: 博客标题规范化 + 原创关键词集成段落。
标题规范化：源站 title 的大小写异常（"Dac Vs No Dac" 等）按化合物规范名修正。
扩展：每篇开头插入原创 sourcing 视角段落 + 文末关键词小结。"""
import re, glob

# 标题修正表（源站标题 → 规范标题）
TITLE_FIX = {
    'Dac Vs No Dac': 'CJC-1295 With DAC vs Without DAC: Which Research Variant to Source',
    'Semax Half Life': 'Semax Half-Life in Research: What the Data Shows',
    'Semax Dosage Mg Per Day': 'Semax Dosage in Research: Milligrams, Protocols, and Practical Limits',
    'N Acetyl Semax Amidate': 'N-Acetyl Semax Amidate: The Stabilized Research Variant',
    'Retatrutide Side Effects': 'Retatrutide in Research: Reported Effects and What Buyers Should Verify',
    'Research Peptides': 'What Are Research Peptides? A Primer for B2B Buyers',
    'Peptide Solubility Troubleshooting': 'Peptide Solubility Troubleshooting: A Practical Guide for Research Labs',
    'Peptide Molecular Weight Verification Steps': 'Peptide Molecular Weight Verification: Steps Every Buyer Should Know',
    'Why Impurities Affect Clinical Study Outcomes': 'Why Peptide Impurities Affect Study Outcomes — and How China Peptide Buyers Can Verify Purity',
    'How Peptides Interact With Formulation Base': 'How Peptides Interact With Formulation Bases: What Formulators Need to Know',
    'What Is Amino Acid Coupling Efficiency': 'Amino Acid Coupling Efficiency: The Manufacturing Metric Behind Peptide Purity',
    'How We Verify Product Quality Our 3 Step Approach': 'How We Verify Product Quality: Our 3-Step Approach to China Peptide Sourcing',
    'Tirzepatide Wholesale Sourcing A 2026 B2B Procurement Guide': 'Tirzepatide Wholesale Sourcing: A 2026 B2B Procurement Guide for China Peptides',
    'High Purity Peptides Bulk Order A B2B Guide To Direct Sourci': 'High-Purity Peptides Bulk Order: A B2B Guide to Direct Sourcing',
    'Coa Verified Peptides Supplier How To Authenticate Research': 'COA-Verified Peptides Supplier: How to Authenticate Research Compounds',
}

def title_to_slug(title: str) -> str:
    s = re.sub(r'[^a-z0-9]+', '-', title.lower()).strip('-')
    return s

def main():
    fixed = 0
    expanded = 0
    for path in glob.glob('src/content/blog/*.md'):
        raw = open(path, encoding='utf-8').read()
        parts = raw.split('---\n', 2)
        if len(parts) < 3:
            continue
        fm, body = parts[1], parts[2]
        m = re.search(r'title: "([^"]+)"', fm)
        old_title = m.group(1) if m else ''
        new_title = TITLE_FIX.get(old_title)
        if new_title:
            fm = fm.replace(f'title: "{old_title}"', f'title: "{new_title}"', 1)
            # 同步 slug 以保持 URL 稳定性（源站 slug 保留，仅标题修正）
            fixed += 1
        # 扩展：原创关键词段落
        if '## China Peptides Sourcing Perspective' in body:
            continue
        # 从正文提取关键短语
        first = body[:500]
        topic = old_title or new_title or 'research peptides'
        intro = (f"This guide examines {topic.lower().rstrip('.')} from the perspective of a **china peptide** buyer. "
                 f"For researchers and resellers sourcing **chinese peptides**, the practical questions are the same "
                 f"regardless of compound: who manufactured the vial, what the batch documentation shows, and whether "
                 f"the specification matches the listing. We answer those questions below.")
        closer = ("\n\n## China Peptides Sourcing Perspective\n\n"
                  "Everything discussed above applies to the broader question of sourcing **china peptides**: the "
                  "compound's research profile matters, but the manufacturer and the batch documentation decide "
                  "whether the vial in your hand matches the description on the page. For catalog listings, batch "
                  "specifications, and ordering information, see the [catalog](/catalog/) or "
                  "[how sourcing works](/how-it-works/).")
        body = f"{intro}\n\n{body}".rstrip() + closer + '\n'
        open(path, 'w', encoding='utf-8').write(f'---\n{fm}\n---\n{body}')
        expanded += 1
    print(f'标题修正: {fixed} | 扩展: {expanded}')

if __name__ == '__main__':
    main()
