# Proposals: v1.1.0 batch (LRC ontology review + Conceptual Foundation alignment)

TWO sources feed this batch, in priority order:

1. **The Conceptual Foundation (2026-06-12)** — the canonical document. Where it
   conflicted with earlier drafts, the drafts were redrafted (rectification,
   correction, customary-tenure, first-registration) and one inferred hierarchy
   was corrected (amendment is NOT narrower than VoI). It also contributes four
   new terms (status-change, dispute, transaction-algebra,
   digital-public-infrastructure), an `in_rem` field in the Hohfeldian signature
   schema, and five revisions. It also confirms `beck_effect_2022` = Beck & Moss
   (2022), the indefeasibility/error-correction LADM workshop paper.

2. **The LRC ontology review** (original batch below).

Drafted from a systematic comparison of the Land Registration Concepts ontology
(Beck, 2024) against Glossary v1.0.0. Eleven new terms (drafted in /terms/ with
`status: draft`) and seven amendments to existing terms (drafted in place, each
with a v1.1.0 history entry, `issue: null` pending).

Workflow — using the glossary's own governance:

1. Open one GitHub issue per file here, pasting the body into the matching
   template (New term proposal / Term challenge).
2. Dispose of each as custodian, recording reasons on the issue.
3. For accepted new terms: flip `status: draft` -> `stable`; for all accepted
   changes: set the `issue:` field in the history entry to the issue URL.
4. For declined items: revert the term file (new terms: delete the file;
   amendments: remove the definition sentence and history entry) and record the
   disposition on the issue.
5. Bump glossary.yaml to 1.1.0 with a changelog entry, tag, release -> Zenodo DOI.

Outstanding inputs:
- Add Gretton & Steven (2017), *Property, Trusts and Succession*, to
  references.bib (cited by real-right, personal-right, separated-ownership as
  `gretton_steven_2017` — confirm the key matches your bib conventions).
- Ontology defects to carry into the ontology-v2 work: `personalRight` comment
  is a copy-paste of `realRight`; `firstGrant` and `dischargeOfRight` carry
  placeholder comments; `covenantReviewMe` is a WIP class.

This folder is a staging convenience: once every proposal is disposed of on
GitHub, the issues are the record and this folder can be deleted.
