# [new term] Status change

*Paste into a **New term proposal** issue. Term file already drafted at `terms/status-change.yaml` (status: draft).*

**Proposed term:** Status change

**Proposed definition:**

> An annotation applied to a recorded transaction or version on the transaction log — effective, disputed, void, superseded, corrected, rectified — that asserts nothing new about the world-state. A status change is never a deletion: a void does not itself change who holds what; it declares that the recorded transaction never validly changed anything in the first place. Status changes are not submitted through the acceptance gates; they are directed by the *dispute* pathway against records already in the log. They are the log-level complement of the three world-state operations (variation, *amendment*, *assessment*).

**Why the glossary needs it:**

The CF's change taxonomy is incomplete without the log-level layer: status changes (effective/disputed/void/superseded/corrected/rectified) act on the transaction log, never the world-state, and are never deletions. Rectification's instrument (the void) is undefined without this term. Source: Conceptual Foundation (2026-06-12).

**Relations:**

- see_also: dispute, rectification, correction, bitemporality, good-root-of-title
- LADM: no-counterpart

**On acceptance:** set `status: stable`, link this issue in the term's `history`, include in the v1.1.0 release.
