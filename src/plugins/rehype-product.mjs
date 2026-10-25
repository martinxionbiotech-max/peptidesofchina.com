/**
 * Sätteri hast plugin for /src/content/products/** pages.
 *
 * Responsibilities (presentation + machine-readability only; never rewrites facts):
 * 1. Extract flattened "Label value" / "Label: value" specification pairs
 *    (Chemical Class, CAS Number, Molecular Formula, ...) out of long body text
 *    and expose them as `compoundProfile` for the page's spec table.
 * 2. Extract Frequently Asked Questions Q&A pairs into `faq`
 *    (question text + answer HTML) and remove the raw section from the body.
 * 3. Match the names found in "Related Products" sections against the catalog
 *    and expose them as `related` [{name, slug}], removing the raw section.
 *
 * Data travels through ctx.data.astro.frontmatter, which Astro surfaces as
 * `remarkPluginFrontmatter` on `render(entry)`.
 */
import fs from 'node:fs';
import path from 'node:path';

// Space-separated flattened keys ("Chemical Class X Synonyms Y ...").
const SPACE_KEYS = [
  'Proposed Active Components',
  'Half-Life (approximate)',
  'Half-life (research)',
  'Primary Application',
  'Common Use Cases',
  'Chemical Class',
  'Copper Chelation',
  'Receptor Targets',
  'Receptor Target',
  'Primary Target',
  'Primary Mechanism',
  'Primary Function',
  'Primary Components',
  'Parent Compound',
  'Molecular Formula',
  'Molecular Weight',
  'Amino Acids',
  'Active Fraction',
  'Active Components',
  'Concentration',
  'Osmolality',
  'Modification',
  'CAS Number',
  'PubChem CID',
  'Sequence Length',
  'Disulfide Bonds',
  'Disulfide Bond',
  'Half-Life',
  'Developed',
  'Synonyms',
  'Sequence',
  'Storage',
  'Structure',
  'Research Axes',
  'Key Modification',
  'Key Target',
  'Key Feature',
  'Alpha Subunit',
  'Beta Subunit',
  'Secondary Components',
  'Optional Components',
  'Parent Sequence',
  'Peptide Origin',
  'Volume',
  'Form',
  'pH',
];

// Colon-separated keys ("Category: X Total variants: 2 ...").
const COLON_KEYS = [
  'Standard pack size',
  'In-stock variants',
  'Total variants',
  'Testing method',
  'Category',
  'Purity',
];

const PREFERRED_ORDER = [
  'Chemical Class',
  'Synonyms',
  'Sequence',
  'Sequence Length',
  'Amino Acids',
  'Copper Chelation',
  'Receptor Targets',
  'Receptor Target',
  'Primary Target',
  'Parent Compound',
  'Modification',
  'Key Modification',
  'Developed',
  'Half-Life',
  'Molecular Formula',
  'Molecular Weight',
  'CAS Number',
  'PubChem CID',
  'Disulfide Bonds',
  'Disulfide Bond',
  'Structure',
  'Alpha Subunit',
  'Beta Subunit',
  'Form',
  'Storage',
  'Concentration',
  'Volume',
  'pH',
  'Osmolality',
  'Active Fraction',
  'Active Components',
  'Proposed Active Components',
  'Primary Components',
  'Secondary Components',
  'Optional Components',
  'Primary Mechanism',
  'Primary Function',
  'Key Target',
  'Key Feature',
  'Parent Sequence',
  'Peptide Origin',
  'Primary Application',
  'Common Use Cases',
  'Research Axes',
  'Category',
  'Total variants',
  'In-stock variants',
  'Purity',
  'Standard pack size',
  'Testing method',
];

// Value plausibility gates: the captured value must start with a plausible token,
// which protects prose like "Form a solution" / "the sequence of events" from being extracted.
const VALUE_GATES = {
  'Half-Life (approximate)': /^[~≈\dN]/,
  'Half-life (research)': /^[~≈\dN]/,
  'Primary Application': /^[A-Z0-9(]/,
  'Common Use Cases': /^[A-Z0-9(]/,
  'Chemical Class': /^[A-Z(]/,
  'Copper Chelation': /^[A-Z]/,
  'Receptor Targets': /^[A-Z0-9]/,
  'Receptor Target': /^[A-Z0-9]/,
  'Primary Target': /^[A-Z0-9]/,
  'Primary Mechanism': /^[A-Z]/,
  'Primary Function': /^[A-Z]/,
  'Primary Components': /^[A-Z]/,
  'Parent Compound': /^[A-Z0-9]/,
  'Molecular Formula': /^[A-Za-z0-9(]/,
  'Molecular Weight': /^(~|≈|\d|n\/a|ca\.|\()/i,
  'Amino Acids': /^[\dN]/,
  'Active Fraction': /^[~≈\dA-Z]/,
  'Active Components': /^[A-Z]/,
  'Proposed Active Components': /^[A-Z]/,
  'Secondary Components': /^[A-Z]/,
  'Optional Components': /^[A-Z]/,
  'Concentration': /^[\d~≈.]/,
  'Osmolality': /^[~≈\d]/,
  'Modification': /^[A-Z]/,
  'Key Modification': /^[A-Z]/,
  'Key Target': /^[A-Z]/,
  'Key Feature': /^[A-Z]/,
  'CAS Number': /^(available|n\/a|\d)/i,
  'PubChem CID': /^[\d]/,
  'Sequence Length': /^[\d]/,
  'Disulfide Bonds': /^[A-Z]/,
  'Disulfide Bond': /^[A-Z]/,
  Structure: /^[A-Z]/,
  'Half-Life': /^[~≈\dN]/,
  Developed: /^(from|by|with|as|[A-Z])/i,
  Synonyms: /^[A-Z0-9(]/,
  Sequence: /^[A-ZÅN]/,
  'Parent Sequence': /^[A-Z]/,
  'Peptide Origin': /^[A-Z]/,
  'Alpha Subunit': /^[\d]/,
  'Beta Subunit': /^[\d]/,
  Storage: /^(−|-|–|2-8|4\s*°|room|rt\b|dry|cool|protect|store|lyophilized)/i,
  Volume: /^[\d]/,
  'Research Axes': /^[A-Z]/,
  Form: /^(lyophilized|sterile|liquid|powder|aqueous|tablet|capsule|oil|gel|spray|cream|solution|injectable|ready|concentrated|vial|reconstituted|buffer|acid|salt|crystal|mix)/i,
  pH: /^[~≈\d]/,
};

const escapeRegex = (s) => s.replace(/[.*+?^${}()|[\]\\]/g, '\\$&');

const SPACE_KEY_SOURCE = [...SPACE_KEYS].sort((a, b) => b.length - a.length).map(escapeRegex).join('|');
const SPACE_KEY_RE = new RegExp(`\\b(${SPACE_KEY_SOURCE})(?=\\s|:|$|\\()`, 'g');
const COLON_KEY_RE = new RegExp(`\\b(${COLON_KEYS.map(escapeRegex).join('|')})\\s*:\\s*`, 'g');

// Boilerplate fragments that can never be part of a spec value.
const VALUE_TERMINATORS =
  /\s+(?:For laboratory research use only|Not for human or veterinary use|Peptides of China|class, and every listing|Buyers sourcing|; we confirm availability|All products are sold)/;

function textOf(node) {
  if (node.type === 'text') return node.value;
  if ('children' in node && Array.isArray(node.children)) {
    return node.children.map(textOf).join('');
  }
  return '';
}

function questionParagraph(el) {
  if (!el || el.type !== 'element' || el.tagName !== 'p') return null;
  const meaningful = el.children.filter((c) => !(c.type === 'text' && c.value.trim() === ''));
  if (meaningful.length !== 1) return null;
  const child = meaningful[0];
  if (child.type !== 'element' || child.tagName !== 'strong') return null;
  const q = textOf(child).trim();
  if (!q.endsWith('?')) return null;
  const whole = textOf(el).trim();
  return q === whole ? q : null;
}

function escapeHtml(s) {
  return String(s).replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;');
}

function serializeNodes(nodes) {
  let out = '';
  for (const node of nodes) {
    if (node.type === 'text') out += escapeHtml(node.value);
    else if (node.type === 'raw') out += node.value || '';
    else if (node.type === 'element') {
      const tag = node.tagName;
      let attrs = '';
      const props = node.properties || {};
      if (tag === 'a' && typeof props.href === 'string') {
        attrs += ` href="${escapeHtml(props.href)}"`;
      }
      const inner = serializeNodes(node.children || []);
      if (tag === 'br' || tag === 'hr' || tag === 'img') out += `<${tag}${attrs} />`;
      else out += `<${tag}${attrs}>${inner}</${tag}>`;
    }
  }
  return out;
}

function normalizeName(s) {
  return String(s)
    .toLowerCase()
    .replace(/[^a-z0-9+]/g, '');
}

function buildCatalogCandidates(catalog, ownSlug) {
  const out = [];
  const seen = new Set();
  for (const item of catalog) {
    if (item.slug === ownSlug) continue;
    const humanized = String(item.slug).replace(/[-_]+/g, ' ');
    const displays = item.name && normalizeName(item.name) !== normalizeName(item.slug)
      ? [item.name, humanized]
      : [humanized, item.name];
    for (const candidate of displays) {
      if (!candidate || normalizeName(candidate).length < 3) continue;
      const key = normalizeName(candidate);
      if (seen.has(key)) continue;
      seen.add(key);
      out.push({ name: item.name, slug: item.slug, display: candidate, norm: key });
    }
  }
  return out.sort((a, b) => b.norm.length - a.norm.length);
}

function matchRelated(text, candidates) {
  const normText = normalizeName(text);
  const consumed = [];
  const picks = [];
  for (const candidate of candidates) {
    const idx = normText.indexOf(candidate.norm);
    if (idx === -1) continue;
    const end = idx + candidate.norm.length;
    if (consumed.some(([s, e]) => idx < e && end > s)) continue;
    consumed.push([idx, end]);
    picks.push({ name: candidate.name, slug: candidate.slug, pos: idx });
  }
  picks.sort((a, b) => a.pos - b.pos);
  return picks.map(({ name, slug }) => ({ name, slug }));
}

/**
 * Extract "Label value"/"Label: value" pairs from a single text node.
 * Returns { text, pairs } where pairs carry removal spans.
 */
function extractSpecFromText(text) {
  const pairs = [];
  const spans = [];

  // Space-separated keys.
  SPACE_KEY_RE.lastIndex = 0;
  let match;
  while ((match = SPACE_KEY_RE.exec(text)) !== null) {
    const key = match[0];
    let valueStart = match.index + match[0].length;
    if (text[valueStart] === ':') valueStart++;
    while (valueStart < text.length && /\s/.test(text[valueStart])) valueStart++;
    if (valueStart >= text.length) continue;

    // Value ends at the next known key, boilerplate, or end of node.
    const outerCursor = SPACE_KEY_RE.lastIndex;
    let valueEnd = text.length;
    SPACE_KEY_RE.lastIndex = valueStart;
    let next;
    while ((next = SPACE_KEY_RE.exec(text)) !== null) {
      if (next.index > valueStart) {
        valueEnd = next.index;
        break;
      }
    }
    SPACE_KEY_RE.lastIndex = outerCursor;
    const terminator = text.slice(valueStart, valueEnd).match(VALUE_TERMINATORS);
    if (terminator) valueEnd = valueStart + terminator.index;

    let value = text
      .slice(valueStart, valueEnd)
      .trim()
      .replace(/^[:,\s]+/, '')
      .replace(/[\s,;:]+$/, '');
    if (!value) continue;

    const gate = VALUE_GATES[key] || /^[A-Z0-9(≥~≈\d]/;
    if (!gate.test(value)) continue;
    if (value.length > 400) continue;

    pairs.push({ label: key, value, start: match.index, end: valueEnd });
    spans.push([match.index, valueEnd]);
  }

  // Colon-separated keys.
  COLON_KEY_RE.lastIndex = 0;
  while ((match = COLON_KEY_RE.exec(text)) !== null) {
    const key = match[0].replace(/\s*:\s*$/, '');
    const valueStart = match.index + match[0].length;
    const outerCursor = COLON_KEY_RE.lastIndex;
    let valueEnd = text.length;
    COLON_KEY_RE.lastIndex = valueStart;
    let next;
    while ((next = COLON_KEY_RE.exec(text)) !== null) {
      if (next.index > valueStart) {
        valueEnd = next.index;
        break;
      }
    }
    COLON_KEY_RE.lastIndex = outerCursor;
    let raw = text.slice(valueStart, valueEnd);
    const terminator = raw.match(VALUE_TERMINATORS);
    if (terminator) {
      valueEnd = valueStart + terminator.index;
      raw = raw.slice(0, terminator.index);
    }
    const dotTerminator = raw.match(/\s+\.\s+[A-Z(]/);
    if (dotTerminator) {
      valueEnd = valueStart + dotTerminator.index;
      raw = raw.slice(0, dotTerminator.index);
    }
    const value = raw.trim().replace(/^[:,\s]+/, '').replace(/[\s,;:]+$/, '');
    if (!value || value.length > 200) continue;

    pairs.push({ label: key, value, start: match.index, end: valueEnd });
    spans.push([match.index, valueEnd]);
  }

  if (!pairs.length) return { text, pairs };

  // Safety net: only trust KV-dense text nodes (two or more distinct keys).
  // Prose paragraphs that mention a single Title-Case key by coincidence stay untouched.
  const distinctKeys = new Set(pairs.map((p) => p.label.toLowerCase()));
  if (distinctKeys.size < 2) return { text, pairs: [] };

  // Merge removal spans; treat whitespace/punctuation-only gaps as removable.
  spans.sort((a, b) => a[0] - b[0] || a[1] - b[1]);
  const merged = [];
  for (const [s, e] of spans) {
    const last = merged[merged.length - 1];
    if (last && s <= last[1]) {
      last[1] = Math.max(last[1], e);
    } else if (last && s > last[1] && /^[\s,.;:·]*$/.test(text.slice(last[1], s))) {
      last[1] = Math.max(last[1], e);
    } else {
      merged.push([s, e]);
    }
  }

  let out = '';
  let cursor = 0;
  for (const [s, e] of merged) {
    out += text.slice(cursor, s);
    cursor = Math.max(cursor, e);
  }
  out += text.slice(cursor);
  const hadLeadingSpace = /^\s/.test(text);
  out = out.replace(/\s{2,}/g, ' ').replace(/^[\s.,;:]+/, '').replace(/[\s,;:]+$/, '');
  if (hadLeadingSpace && out && !/^\s/.test(out)) out = ` ${out}`;
  return { text: out, pairs };
}

function dedupePairs(pairs) {
  const seen = new Set();
  const out = [];
  for (const p of pairs) {
    const canonical = p.label
      .replace(/\s*\((approximate|research)\)\s*$/i, '')
      .replace(/^Half-life$/i, 'Half-Life');
    const key = canonical.toLowerCase();
    if (seen.has(key)) continue;
    seen.add(key);
    out.push({ label: canonical, value: p.value });
  }
  const rank = (label) => {
    const i = PREFERRED_ORDER.indexOf(label);
    return i === -1 ? PREFERRED_ORDER.length : i;
  };
  return out.sort((a, b) => rank(a.label) - rank(b.label));
}

export { extractSpecFromText };

export function loadCatalogNames() {
  const root = path.resolve('src/content/products');
  const out = [];
  const walk = (dir) => {
    for (const entry of fs.readdirSync(dir, { withFileTypes: true })) {
      const full = path.join(dir, entry.name);
      if (entry.isDirectory()) walk(full);
      else if (entry.name.endsWith('.md')) {
        const raw = fs.readFileSync(full, 'utf8');
        const fm = raw.split('---')[1] || '';
        const grab = (key) => {
          const m = fm.match(new RegExp(`^${key}:\\s*(?:"([^"]*)"|'([^']*)'|(.+))$`, 'm'));
          return m ? (m[1] ?? m[2] ?? m[3]).trim() : '';
        };
        const name = grab('name');
        const slug = grab('slug');
        if (name && slug) out.push({ name, slug });
      }
    }
  };
  walk(root);
  return out;
}

const PUNCT_ONLY = /^[\s.,;:·•–—-]*$/;
const UNREMOVABLE_TAGS = new Set(['img', 'video', 'svg', 'picture', 'iframe', 'table', 'canvas', 'audio']);

export default function productLayoutPlugin(options = {}) {
  const catalog = options.catalog || [];

  return (pluginCtx) => {
    const fileURL = pluginCtx?.fileURL?.pathname ?? pluginCtx?.fileURL?.href ?? '';
    const source = pluginCtx?.source ?? '';
    const isProductFile =
      /\/content\/products\//.test(fileURL) ||
      /^slug:\s+.+$/m.test(source) && /^price:\s*[\d.]+/m.test(source) && /^name:\s+.+$/m.test(source);
    if (!isProductFile) return null;

    return {
      name: 'product-layout-extractor',
      before(root, ctx) {
        const astroData = ctx.data?.astro;
        const frontmatter = astroData?.frontmatter;
        if (!frontmatter) return;
        const ownSlug = frontmatter.slug || '';
        const children = root.children;
        const extractedFaq = [];
        const extractedRelated = [];
        const seenQuestions = new Set();
        const seenRelated = new Set();
        const specPairs = [];
        const textReplacements = new Map();
        const nodeRemovals = new Set();
        const deadTextNodes = new Set();

        const removeNode = (node) => {
          if (node && !nodeRemovals.has(node)) {
            nodeRemovals.add(node);
            ctx.removeNode(node);
            // Sätteri applies commands immediately, so mark descendant text nodes
            // as dead here to keep later replacement commands from targeting them.
            const markDead = (n) => {
              if (!n) return;
              if (n.type === 'text') deadTextNodes.add(n);
              for (const c of n.children || []) markDead(c);
            };
            markDead(node);
          }
        };
        const removeRange = (from, to) => {
          for (let k = from; k < to; k++) removeNode(children[k]);
        };

        // Process one section's content, queueing text replacements and pruning
        // elements whose remaining text is punctuation-only.
        const processSectionContent = (from, to) => {
          const processElement = (el) => {
            if (!el || el.type !== 'element') return;
            for (const child of el.children || []) processElement(child);
            // Replace matching text nodes.
            for (const child of el.children || []) {
              if (child.type === 'text' && child.value) {
                const { text, pairs } = extractSpecFromText(child.value);
                if (pairs.length) {
                  textReplacements.set(child, { text });
                  specPairs.push(...pairs);
                }
              }
            }
            // Prune elements emptied by extraction.
            function remainingText(node) {
              let t = '';
              for (const c of node.children || []) {
                if (nodeRemovals.has(c)) continue;
                if (c.type === 'text') t += textReplacements.get(c)?.text ?? c.value;
                else if (c.type === 'element') t += remainingText(c);
              }
              return t;
            }
            function removableChildren(node) {
              return (node.children || []).every((c) => {
                if (nodeRemovals.has(c)) return true;
                if (c.type === 'text') return true;
                if (c.type !== 'element') return false;
                if (UNREMOVABLE_TAGS.has(c.tagName)) return false;
                return removableChildren(c);
              });
            }
            if (UNREMOVABLE_TAGS.has(el.tagName)) return;
            if (
              (el.tagName === 'p' || el.tagName === 'li') &&
              PUNCT_ONLY.test(remainingText(el)) &&
              removableChildren(el)
            ) {
              removeNode(el);
            }
          };
          for (let k = from; k < to; k++) processElement(children[k]);
        };

        const candidates = buildCatalogCandidates(catalog, ownSlug);

        // Pass 0: preamble before the first heading (intro paragraphs carry
        // flattened KV tails that must be extracted too).
        let firstHeading = 0;
        while (
          firstHeading < children.length &&
          !(children[firstHeading].type === 'element' && children[firstHeading].tagName === 'h2')
        ) {
          firstHeading++;
        }
        processSectionContent(0, firstHeading);

        // Pass 1: FAQ + Related sections (remove from tree, collect data).
        let i = firstHeading;
        const sectionRemovalCount = new Map();
        while (i < children.length) {
          const node = children[i];
          if (!(node.type === 'element' && node.tagName === 'h2')) {
            i++;
            continue;
          }
          const title = textOf(node).trim();
          let j = i + 1;
          while (j < children.length && !(children[j].type === 'element' && children[j].tagName === 'h2')) j++;

          if (/^Frequently Asked Questions$/i.test(title)) {
            let currentQ = null;
            let currentA = [];
            const flush = () => {
              if (currentQ && currentA.length) {
                const key = currentQ.trim().toLowerCase();
                if (!seenQuestions.has(key)) {
                  seenQuestions.add(key);
                  extractedFaq.push({ q: currentQ.trim(), a: serializeNodes(currentA) });
                }
              }
              currentQ = null;
              currentA = [];
            };
            for (let k = i + 1; k < j; k++) {
              const q = questionParagraph(children[k]);
              if (q) {
                flush();
                currentQ = q;
              } else if (currentQ && children[k].type === 'element') {
                currentA.push(children[k]);
              }
            }
            flush();
            removeRange(i, j);
            i = j;
            continue;
          }

          if (/^Related Products$/i.test(title)) {
            const text = children.slice(i + 1, j).map(textOf).join(' ');
            const found = matchRelated(text, candidates);
            for (const item of found) {
              if (!seenRelated.has(item.slug)) {
                seenRelated.add(item.slug);
                extractedRelated.push(item);
              }
            }
            removeRange(i, j);
            i = j;
            continue;
          }

          // Pass 2: spec extraction within ordinary sections.
          processSectionContent(i + 1, j);
          let removed = 0;
          for (let k = i + 1; k < j; k++) if (nodeRemovals.has(children[k])) removed++;
          sectionRemovalCount.set(i, removed);
          i = j;
        }

        // Pass 3: prune KV-only headings (Profile / Specification Highlights).
        for (let k = children.length - 1; k >= 0; k--) {
          const node = children[k];
          if (!(node.type === 'element' && node.tagName === 'h2')) continue;
          const title = textOf(node).trim();
          const isProfile = /^(Compound\s+)?Profile$/i.test(title);
          const isSpecHighlights = /^Specification Highlights$/i.test(title);
          if (!isProfile && !isSpecHighlights) continue;
          let j = k + 1;
          while (j < children.length && !(children[j].type === 'element' && children[j].tagName === 'h2')) j++;
          const removed = sectionRemovalCount.get(k) || 0;
          const total = j - k - 1;
          if (total === 0 || (removed === total && total > 0)) {
            removeNode(node);
          }
        }

        // Queue text replacements last so no earlier removal command invalidates them.
        for (const [node, { text }] of textReplacements) {
          if (!nodeRemovals.has(node) && !deadTextNodes.has(node)) {
            ctx.replaceNode(node, { type: 'text', value: text });
          }
        }

        frontmatter.compoundProfile = dedupePairs(specPairs);
        frontmatter.faq = extractedFaq;
        frontmatter.related = extractedRelated;
      },
    };
  };
}
