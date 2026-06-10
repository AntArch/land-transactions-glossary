# Governance and change control

This glossary is a governed artefact with a custodian and a mandate. It applies to itself the
principles it asks of every other authoritative source in the land-transactions portfolio:
one custodian, durable identifiers, versioned amendment rather than replacement, and
once-only with everything else referencing it.

## Custodian

Anthony Beck (Cadastral Concepts Ltd, ORCID 0000-0002-2991-811X) is the custodian of this
glossary. The custodian defines, maintains, publishes, and corrects the terminology; other
documents and systems reference it rather than maintaining diverging local copies.

## Who may propose a change

Anyone, by opening a GitHub issue using the **Term challenge** or **New term proposal**
template. Issues are the public challenge log: every objection to a definition is a tracked,
citable record with a recorded disposition.

## Who disposes of a change

The custodian, with reasons recorded on the issue before it is closed. Dispositions are one
of: **accepted** (an amendment is made and released), **accepted-with-modification**,
**declined** (with reasons), or **deferred** (parked pending external developments, e.g. an
ISO 19152 revision).

## What triggers a version bump

The glossary follows semantic versioning at two levels.

**Glossary level** (`glossary.yaml: version`, tagged as a release):

- **Patch** (1.0.x): typographical or formatting corrections that do not alter the meaning
  of any definition; build/site changes.
- **Minor** (1.x.0): a new term; a clarifying amendment that does not change what any
  existing conforming usage means; new or corrected `see_also`, Hohfeldian-signature, or
  LADM-mapping metadata.
- **Major** (x.0.0): a change that alters the meaning of an existing term, deprecates a
  term, or renames a concept. Documents citing an earlier major version should review
  their usage.

**Term level** (`history` inside each term file): every amendment to a term appends a
history entry with its own version, date, the change, and a link to the issue that
proposed it.

## Durable identifiers

A term's `id` (and therefore its URI) never changes once published. Terms are never
deleted: a superseded term is set to `status: deprecated` with a `replaced_by` pointer,
and remains resolvable so that citations in earlier document versions do not break.

## Locked means versioned, not frozen

Each portfolio document cites a specific glossary release (e.g. "Glossary v1.0,
DOI:10.5281/zenodo.XXXXXXX"). Amendments produce a new release with a changelog; the cited
release remains permanently retrievable via its DOI. This is the amendment-not-replacement
principle applied to the portfolio's own terminology.

## Release procedure (custodian checklist)

1. Merge the amendment PR(s); ensure each amended term's `history` references its issue.
2. Bump `glossary.yaml: version` and append a changelog entry.
3. Run `python3 scripts/build.py` locally; confirm the build passes.
4. Tag and push: `git tag vX.Y.Z && git push --tags`, then create a GitHub Release from
   the tag (this triggers Zenodo archiving and DOI minting).
5. Add the new DOI to the release notes and to README.md.
