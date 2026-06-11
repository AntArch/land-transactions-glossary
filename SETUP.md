# SETUP — from this folder to a published, citable, governed glossary

Time required: roughly an hour for steps 1–5; step 6 (w3id) involves waiting for a pull-request review by the w3id maintainers, typically a few days.

## Step 1 — Review the migrated content (before anything goes public)

The 76 term records in `terms/` were generated from the Quarto annex. Before publishing:

1. Skim each file (or at least the conceptually loaded ones). The `definition` text is verbatim from the .qmd, with one transformation: citation keys like `[-@honore_ownership_1961]` remain in the YAML but are stripped from the rendered site. If you'd rather render them as plain citations ("(Honoré 1961)"), rewrite them in the YAML now.
2. `hohfeldian_signature` is pre-filled on the 18 terms where it applies. Review the signatures — in particular the deliberate departures recorded in the notes of *no-privilege* and *restriction* — and adjust where your analysis differs.
3. `ladm_mapping` is pre-filled for all 76 terms against ISO 19152-1:2024 (with Part 4/5 references where relevant). Sub-clauses 3.1.1–3.1.10 and 6.3.x were verified against the standard's published preview; citations marked **VERIFY** name the term but the sub-clause number must be confirmed against the full text (terms alphabetically after "object identifier": party, regulation, responsibility, restriction, right, source, spatial unit). The ISO 19152:2012 numbers alongside are a cross-check. Run `grep -rl VERIFY terms/` to list the affected files.
4. Inferred attributes are also pre-filled: `category` (facet), `broader` (taxonomy — emitted as skos:broader/narrower), `counterpart_of`, `contrasted_with`, `composed_of`, `applies_to`, `abbreviation`/`alt_labels`, and `citations` (BibTeX keys resolving against references.bib). These were derived from explicit statements in the definitions ("counterpart of…", "one of three…", "distinguished from…"); review the taxonomy in particular — e.g. *amendment* is placed under *VoI*, and *cadastral unit* under *administrative unit*, both defensible but judgement calls.
4. Test the build locally: 

```bash 
pip install pyyaml jsonschema rdflib 
python3 scripts/build.py 
open site/index.html        # macOS; use xdg-open on Linux, start on Windows 
```

## Step 2 — Create the GitHub repository

1. Sign in at github.com → **New repository**. Name it (e.g.) `land-transactions-glossary`, set it **Public**, no auto-generated files.
2. From this folder: 

```bash 
git init 
git add . 
git commit -m "Glossary v1.0.0: initial migration from Quarto annex" 
git branch -M main 
git remote add origin https://github.com/AntArch/land-transactions-glossary.git 
git push -u origin main 
```

3. Update `glossary.yaml: repository` and the URL in README.md to the real URL; commit and push again.

## Step 3 — Turn on GitHub Pages (the human-readable site)

1. Repository → **Settings → Pages → Source: GitHub Actions**.
2. The included workflow (`.github/workflows/build-and-deploy.yml`) already builds and deploys on every push to `main`. Push any commit (or re-run the workflow under the **Actions** tab) and the site appears at `https://AntArch.github.io/land-transactions-glossary/`.
3. Check that `…/index.html#allocated-incidents` and `…/allocated-incidents.html` both resolve — those are the two anchor forms other documents will link to.

## Step 4 — Enable the challenge mechanism

Nothing to install — the issue templates are in `.github/ISSUE_TEMPLATE/`. Two settings
to check: **Settings → General → Features → Issues** is ticked, and under
**Issues → Labels** add `term-challenge` and `new-term` labels (the templates apply them).
The issue list is now your public, citable challenge log; record dispositions per
GOVERNANCE.md before closing any issue.

## Step 5 — Zenodo DOI per release

1. Go to zenodo.org → **Log in → Sign in with GitHub**.
2. Profile menu → **GitHub** → find the glossary repository in the list → flip the toggle **ON**. (If it doesn't appear, click "Sync now".)
3. Back on GitHub: **Releases → Draft a new release** → tag `v1.0.0`, title "Glossary v1.0.0", paste the changelog entry from `glossary.yaml`, **Publish**.
4. Within a few minutes Zenodo archives the release and mints two DOIs: a *version DOI* (cite this in documents — it pins v1.0.0 forever) and a *concept DOI* (always resolves to the latest version — use this in README and CITATION.cff).
5. Add the concept DOI to `CITATION.cff` (the commented block at the bottom) and the version DOI to the release notes and README table. Commit and push.

Every future release (step in GOVERNANCE.md's checklist) repeats 3–5 automatically:
tagging a release is what mints the next DOI.

## Step 6 — Persistent identifiers via w3id.org

This makes `https://w3id.org/land-transactions/glossary/<term-id>` the canonical URI,
surviving any future re-hosting.

1. Fork https://github.com/perma-id/w3id.org
2. Create a directory `land-transactions/` containing two files:
	* `README.md` — who you are and what the namespace is for (name, ORCID, contact email, one paragraph of purpose).
	* `.htaccess`: 

```apache
Options +FollowSymLinks
RewriteEngine on

# SKOS / JSON exports
RewriteRule ^glossary/glossary\.(ttl|json|md)$ https://AntArch.github.io/land-transactions-glossary/glossary.$1 [R=302,L]

# Per-term URIs -> per-term redirect stubs on the site
RewriteRule ^glossary/([a-z0-9-]+)$ https://AntArch.github.io/land-transactions-glossary/$1.html [R=302,L]

# Namespace root -> glossary index
RewriteRule ^glossary/?$ https://AntArch.github.io/land-transactions-glossary/ [R=302,L]
```

3. Open a pull request against perma-id/w3id.org; a maintainer reviews and merges (usually days). Once merged, test `https://w3id.org/land-transactions/glossary/voi`.
4. The `base_uri` in `glossary.yaml` already assumes this namespace; if you chose a different path, update it and rebuild.

(If you later self-host or move off GitHub Pages, you change only the `.htaccess`
redirect targets — every published URI keeps working.)


## Ongoing operating rhythm

- Challenge arrives as an issue → custodian records disposition → if accepted, PR amends the term file (with `history` entry linking the issue) → CI validates → merge → when a batch warrants it, bump version, tag, release → Zenodo mints the DOI → update citations only if a *major* version changed meanings.
