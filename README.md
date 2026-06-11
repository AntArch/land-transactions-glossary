# Glossary and definitions

**The single-source terminology for the land-transactions portfolio.**

This repository is the canonical, version-controlled home of the glossary. Every other
portfolio document — the conceptual foundation, the reference architecture, the audience
briefs — points here and never redefines a term locally.

| What | Where |
|---|---|
| Human-readable glossary (per-term anchors) | https://w3id.org/land-transactions/glossary/ |
| Term URIs | `https://w3id.org/land-transactions/glossary/<term-id>` |
| SKOS export | [`glossary.ttl`](https://w3id.org/land-transactions/glossary/glossary.ttl) |
| JSON export | `glossary.json` |
| Citable releases (DOI) | Zenodo — see Releases; cite e.g. *Glossary v1.0.0, DOI:10.5281/zenodo.20632452* |
| Challenge a definition | [Open an issue](../../issues/new/choose) |
| Change-control rule | [GOVERNANCE.md](GOVERNANCE.md) |

## Structure

```
glossary.yaml          glossary-level metadata, version, changelog
terms/<id>.yaml        one structured record per term (definition, status,
                       see_also, Hohfeldian signature, LADM mapping, history)
schema/                JSON Schema the term records are validated against
scripts/build.py       generates site/ (HTML + SKOS + JSON + Markdown) from terms/
site/                  generated — do not edit by hand
```

## Editing

1. Open an issue first (Term challenge or New term proposal) — the issue log is the
   public record of why each definition is what it is.
2. Amend or add the term file in `terms/`, appending a `history` entry that links the issue.
3. `python3 scripts/build.py` must pass (CI enforces this on every PR).
4. The custodian merges, bumps the version per [GOVERNANCE.md](GOVERNANCE.md), and tags a
   release; Zenodo archives the release and mints its DOI automatically.

"Locked" means **versioned, not frozen**: documents cite a specific release, and that
release remains permanently retrievable even as the glossary evolves.

## Licence

CC BY 4.0 — see [LICENSE](LICENSE).
