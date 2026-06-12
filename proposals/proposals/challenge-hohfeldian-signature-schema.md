# [challenge] schema: Hohfeldian signature: alignment with the Conceptual Foundation

*Paste into a **Term challenge** issue. Edits already drafted with v1.1.0 history entries.*

**Term:** hohfeldian-signature-schema
**Glossary version:** v1.0.0

**Objection / motivation:**

Conceptual Foundation §2.3: the typed numerus clausus signature includes 'whether it binds the world at large as a proprietary relation (in rem) or only specific parties as a personal relation (in personam)'. The schema lacked the field. Note this is a schema change affecting /schema/term.schema.yaml plus eight term records.

**Proposed amendment:**

Add 'in_rem' (boolean/null) to the Hohfeldian signature schema and set it where clear: easement, praedial right, security, strata title, separated ownership, conventional incidents (true); permit, allocated incidents (false — personal/administrative).

**Impact:** see drafted edits. Minor-release material per GOVERNANCE.md (no existing conforming usage changes meaning).
