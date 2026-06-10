#!/usr/bin/env python3
"""
Build the glossary site and machine-readable exports from /terms/*.yaml.

Outputs (written to /site/):
  index.html      human-readable glossary, one anchor per term (#<id>)
  <id>.html       one redirect stub per term so /glossary/<id> resolves
  glossary.ttl    SKOS (Turtle) export
  glossary.json   plain JSON export
  glossary.md     Markdown rendering (convenience snapshot for PDF annexes)

Run:  python3 scripts/build.py
CI runs this on every push; the build FAILS on schema violations,
duplicate ids, or dangling see_also references.
"""
import sys, json, re, html, pathlib, datetime

try:
    import yaml
except ImportError:
    sys.exit("pip install pyyaml")
try:
    import jsonschema
except ImportError:
    jsonschema = None  # validation skipped locally if not installed; CI installs it

ROOT = pathlib.Path(__file__).resolve().parent.parent
TERMS_DIR = ROOT / "terms"
SITE = ROOT / "site"
SITE.mkdir(exist_ok=True)

meta = yaml.safe_load((ROOT / "glossary.yaml").read_text())
BASE = meta["base_uri"].rstrip("/") + "/"
schema = yaml.safe_load((ROOT / "schema" / "term.schema.yaml").read_text())

# ---------- load + validate ----------------------------------------------
print('Load terms')
terms, errors = [], []
for f in sorted(TERMS_DIR.glob("*.yaml")):
    print(f"{f.name}")
    rec = yaml.safe_load(f.read_text())
    if rec.get("id") != f.stem:
        errors.append(f"{f.name}: id '{rec.get('id')}' does not match filename")
    if jsonschema:
        try:
            jsonschema.validate(rec, schema)
        except jsonschema.ValidationError as e:
            errors.append(f"{f.name}: {e.message}")
    terms.append(rec)

print('Validate terms')
ids = [t["id"] for t in terms]
dupes = {i for i in ids if ids.count(i) > 1}
if dupes:
    errors.append(f"duplicate ids: {dupes}")
idset = set(ids)
label2id = {}
for t in terms:
    label2id[t["term"].lower()] = t["id"]
    m = re.match(r"(.+?)\s*\((.+?)\)", t["term"])
    if m:
        label2id[m.group(1).lower().strip()] = t["id"]
        label2id[m.group(2).lower().strip()] = t["id"]
for t in terms:
    for field in ("see_also", "contrasted_with", "composed_of"):
        for ref in t.get(field) or []:
            if ref not in idset:
                errors.append(f"{t['id']}: {field} references unknown id '{ref}'")
    for field in ("broader", "counterpart_of"):
        ref = t.get(field)
        if ref and ref not in idset:
            errors.append(f"{t['id']}: {field} references unknown id '{ref}'")
    if t.get("status") == "deprecated" and not t.get("replaced_by"):
        errors.append(f"{t['id']}: deprecated but no replaced_by")

print('Hierarchy Check')

# broader hierarchy must be acyclic
parent = {t["id"]: t.get("broader") for t in terms}
for start in parent:
    seen, cur = set(), start
    while parent.get(cur):
        cur = parent[cur]
        if cur in seen or cur == start:
            errors.append(f"broader cycle involving '{start}'")
            break
        seen.add(cur)
narrower = {}
for t in terms:
    if t.get("broader"):
        narrower.setdefault(t["broader"], []).append(t["id"])

if errors:
    print("BUILD FAILED:\n  " + "\n  ".join(errors))
    sys.exit(1)

terms.sort(key=lambda t: t["term"].lower())

# ---------- helpers --------------------------------------------------------
def md_inline(text, link=True):
    """Render the tiny Markdown subset used in definitions; hyperlink *Term* refs."""
    out = html.escape(text)
    out = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", out)
    def emph(m):
        label = m.group(1)
        tid = label2id.get(label.lower().rstrip("s")) or label2id.get(label.lower()) \
              or label2id.get((label.lower() + "s"))
        if link and tid:
            return f'<a href="#{tid}"><em>{label}</em></a>'
        return f"<em>{label}</em>"
    out = re.sub(r"\*([^*]+)\*", emph, out)
    # strip citation keys like [-@honore_ownership_1961] / [@beck_effect_2022]
    out = re.sub(r"\s*\[-?@[^\]]+\]", "", out)
    return out

def plain(text):
    t = re.sub(r"\*\*?", "", text)
    t = re.sub(r"\s*\[-?@[^\]]+\]", "", t)
    return t

# ---------- HTML -----------------------------------------------------------
rows = []
letter = None
for t in terms:
    first = t["term"][0].upper()
    if first != letter:
        letter = first
        rows.append(f'<h2 class="letter" id="sec-{letter}">{letter}</h2>')
    badge = "" if t["status"] == "stable" else f' <span class="badge {t["status"]}">{t["status"]}</span>'
    rel_bits = []
    def name_of(i): return next(x["term"] for x in terms if x["id"] == i)
    if t.get("broader"):
        rel_bits.append(f'Broader: <a href="#{t["broader"]}">{html.escape(name_of(t["broader"]))}</a>')
    if narrower.get(t["id"]):
        rel_bits.append("Narrower: " + ", ".join(f'<a href="#{n}">{html.escape(name_of(n))}</a>' for n in sorted(narrower[t["id"]])))
    if t.get("counterpart_of"):
        rel_bits.append(f'Counterpart of: <a href="#{t["counterpart_of"]}">{html.escape(name_of(t["counterpart_of"]))}</a>')
    if t.get("contrasted_with"):
        rel_bits.append("Contrast: " + ", ".join(f'<a href="#{c}">{html.escape(name_of(c))}</a>' for c in t["contrasted_with"]))
    if t.get("composed_of"):
        rel_bits.append("Composed of: " + " + ".join(f'<a href="#{c}">{html.escape(name_of(c))}</a>' for c in t["composed_of"]))
    if t.get("applies_to"):
        rel_bits.append("Applies to: " + ", ".join(f'<a href="#{c}">{html.escape(name_of(c))}</a>' for c in t["applies_to"]))
    rels = f'<p class="see">{" &middot; ".join(rel_bits)}</p>' if rel_bits else ""
    see = ""
    if t.get("see_also"):
        links = ", ".join(f'<a href="#{r}">{html.escape(next(x["term"] for x in terms if x["id"]==r))}</a>'
                          for r in t["see_also"])
        see = f'<p class="see">See also: {links}</p>'
    ver = t["history"][-1]["version"]
    cat = f' <span class="cat">{t["category"]}</span>' if t.get("category") else ""
    rows.append(f"""
<article class="term" id="{t['id']}">
  <h3>{html.escape(t['term'])}{badge}{cat}
    <a class="anchor" href="#{t['id']}" title="Permalink">#</a></h3>
  <p>{md_inline(t['definition'])}</p>
  {rels}
  {see}
  <p class="meta">URI: <code>{BASE}{t['id']}</code> · term version {ver}</p>
</article>""")

nav = " ".join(f'<a href="#sec-{c}">{c}</a>' for c in sorted({t["term"][0].upper() for t in terms}))
html_doc = f"""<!doctype html>
<html lang="en"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>{html.escape(meta['title'])} — v{meta['version']}</title>
<style>
 body{{font:16px/1.55 Georgia,serif;max-width:46rem;margin:2rem auto;padding:0 1rem;color:#1a1a1a}}
 h1{{font-size:1.6rem;margin-bottom:.2rem}} .sub{{color:#555;margin-top:0}}
 h2.letter{{border-bottom:1px solid #ccc;color:#777;font-size:1rem;margin-top:2.2rem}}
 article.term{{margin:1.4rem 0}} h3{{margin-bottom:.25rem;font-size:1.05rem}}
 .anchor{{visibility:hidden;text-decoration:none;color:#999;margin-left:.3rem}}
 .term:hover .anchor{{visibility:visible}}
 .meta{{font-size:.78rem;color:#888;margin:.2rem 0 0}} code{{font-size:.85em}}
 .see{{font-size:.88rem;color:#444;margin:.2rem 0 0}}
 .badge{{font-size:.7rem;padding:.1em .5em;border-radius:.6em;vertical-align:middle}}
 .cat{{font-size:.68rem;color:#777;border:1px solid #ddd;padding:.05em .5em;border-radius:.6em;vertical-align:middle;font-family:sans-serif}}
 .badge.draft{{background:#ffe9b0}} .badge.deprecated{{background:#f3c4c4}}
 nav{{font-size:.9rem;margin:1rem 0;letter-spacing:.15em}}
 .frontmatter{{background:#f7f6f2;padding:1rem;border-radius:.4rem;font-size:.9rem}}
 :target{{background:#fdf6d8;transition:background .6s}}
</style></head><body>
<h1>{html.escape(meta['title'])}</h1>
<p class="sub">{html.escape(meta['subtitle'])}</p>
<div class="frontmatter">
<p><strong>Version {meta['version']}</strong> · {meta['date']} · Custodian: {html.escape(meta['custodian']['name'])},
{html.escape(meta['custodian']['affiliation'])}
(<a href="https://orcid.org/{meta['custodian']['orcid']}">ORCID</a>)</p>
<p>This glossary is the single source of truth for terminology across the land-transactions portfolio.
Every other document points here and never redefines a term locally. Each term has a durable URI
(<code>{BASE}&lt;term-id&gt;</code>). To challenge or propose an amendment to any definition,
<a href="{meta['repository']}/issues/new/choose">open an issue</a> — see the
<a href="{meta['repository']}/blob/main/GOVERNANCE.md">change-control rule</a>.</p>
<p>Exports: <a href="glossary.ttl">SKOS (Turtle)</a> · <a href="glossary.json">JSON</a> ·
<a href="glossary.md">Markdown snapshot</a> · <a href="{meta['repository']}">source repository</a></p>
</div>
<nav>{nav}</nav>
{''.join(rows)}
<footer><p class="meta">Licensed {meta['license']}. Generated {datetime.date.today().isoformat()} from glossary v{meta['version']}.</p></footer>
</body></html>"""
(SITE / "index.html").write_text(html_doc)

# per-term redirect stubs so BASE/<id> resolves even on plain static hosting
for t in terms:
    (SITE / f"{t['id']}.html").write_text(
        f'<!doctype html><meta charset="utf-8">'
        f'<meta http-equiv="refresh" content="0;url=index.html#{t["id"]}">'
        f'<link rel="canonical" href="{BASE}{t["id"]}">'
        f'<title>{html.escape(t["term"])}</title>'
        f'<p>Redirecting to <a href="index.html#{t["id"]}">{html.escape(t["term"])}</a>…</p>')

# ---------- SKOS (Turtle) ---------------------------------------------------
def ttl_escape(s):
    return s.replace("\\", "\\\\").replace('"', '\\"')

lines = [
    "@prefix skos: <http://www.w3.org/2004/02/skos/core#> .",
    "@prefix dct:  <http://purl.org/dc/terms/> .",
    "@prefix xsd:  <http://www.w3.org/2001/XMLSchema#> .",
    f"@prefix glos: <{BASE}> .",
    "",
    f"<{BASE.rstrip('/')}> a skos:ConceptScheme ;",
    f'    dct:title "{ttl_escape(meta["title"])}"@en ;',
    f'    dct:description "{ttl_escape(meta["subtitle"])}"@en ;',
    f'    dct:creator "{ttl_escape(meta["custodian"]["name"])}" ;',
    f'    dct:license <https://creativecommons.org/licenses/by/4.0/> ;',
    f'    dct:modified "{meta["date"]}"^^xsd:date ;',
    f'    dct:hasVersion "{meta["version"]}" .',
    "",
]
for t in terms:
    lines.append(f"glos:{t['id']} a skos:Concept ;")
    lines.append(f'    skos:inScheme <{BASE.rstrip("/")}> ;')
    lines.append(f'    skos:prefLabel "{ttl_escape(t["term"])}"@en ;')
    alts = list(t.get("alt_labels") or [])
    m = re.match(r"(.+?)\s*\((.+?)\)", t["term"])
    if m and m.group(2).strip() not in alts:
        alts.append(m.group(2).strip())
    for a in alts:
        lines.append(f'    skos:altLabel "{ttl_escape(a)}"@en ;')
    if t.get("abbreviation"):
        lines.append(f'    skos:notation "{ttl_escape(t["abbreviation"])}" ;')
    if t.get("category"):
        lines.append(f'    dct:type "{t["category"]}" ;')
    if t.get("broader"):
        lines.append(f'    skos:broader glos:{t["broader"]} ;')
    for n in narrower.get(t["id"], []):
        lines.append(f'    skos:narrower glos:{n} ;')
    lines.append(f'    skos:definition "{ttl_escape(plain(t["definition"]))}"@en ;')
    related = list(t.get("see_also") or [])
    for f in ("contrasted_with", "composed_of", "applies_to"):
        related += t.get(f) or []
    if t.get("counterpart_of"):
        related.append(t["counterpart_of"])
    seen = set()
    for r in related:
        if r not in seen and r != t.get("broader") and r not in narrower.get(t["id"], []):
            lines.append(f"    skos:related glos:{r} ;")
            seen.add(r)
    for c in t.get("citations") or []:
        lines.append(f'    dct:references "{c}" ;')
    lm = t.get("ladm_mapping") or {}
    if lm.get("iso_19152_clause"):
        note = f"LADM mapping ({lm.get('relation')}): {lm['iso_19152_clause']}"
        if lm.get("notes"):
            note += f" — {lm['notes']}"
        lines.append(f'    skos:note "{ttl_escape(note)}"@en ;')
    lines.append(f'    dct:hasVersion "{t["history"][-1]["version"]}" .')
    lines.append("")
(SITE / "glossary.ttl").write_text("\n".join(lines))

# ---------- JSON + Markdown -------------------------------------------------
(SITE / "glossary.json").write_text(json.dumps(
    {"scheme": {k: meta[k] for k in ("title", "subtitle", "version", "date", "base_uri", "license")},
     "terms": terms}, indent=2, ensure_ascii=False))

md = [f"# {meta['title']} (v{meta['version']})",
      f"_{meta['subtitle']}_",
      "",
      f"> Convenience snapshot rendered from glossary v{meta['version']} at the canonical URI "
      f"<{BASE.rstrip('/')}>. The repository, not this file, is authoritative.",
      ""]
for t in terms:
    md.append(f"**{t['term']}**")
    md.append(f":   {t['definition']}")
    md.append("")
(SITE / "glossary.md").write_text("\n".join(md))

print(f"OK — {len(terms)} terms → site/index.html, glossary.ttl, glossary.json, glossary.md")
