# Glossary and definitions (v1.0.0)
_The single-source terminology for the land-transactions portfolio_

> Convenience snapshot rendered from glossary v1.0.0 at the canonical URI <https://w3id.org/land-transactions/glossary>. The repository, not this file, is authoritative.

**Absorption**
:   The termination form for conventional incidents: the separated claim-right is reintegrated into its parent bundle on expiry, surrender, or satisfaction of the obligation it secured. For the corresponding operation on allocated incidents (public-law privileges), see *Extinguishment*; for reserved incidents (PLRs), see *Rescission*. The counterpart of *derivation*.

**Acceptance criteria**
:   The conditions a transaction submission must satisfy before it is routed to a decision officer. Applied as automated gates at the pre-submission stage under five principles: specificity (a well-formedness check) and capacity, power, consent, and admissibility (validity checks). Applied in a fail-fast order, automated gating prevents avoidable rework without removing officer discretion. There are five gates; professional capability is a limb of *capacity*.

**Administrative unit**
:   In LADM, the object representing the rights package associated with a parcel: it defines what is held and under what conditions. Combined with a spatial unit (geometry), it forms the complete representation of a land object.

**Admissibility principle**
:   One of the five acceptance criteria (a validity check). Requires that the *resulting state* of a transaction is itself lawful: the right type is within the jurisdiction's recognised set (*numerus clausus*), mandatory rules are satisfied, any plan hierarchy is conformed to, and applicable PLRs are not breached. Distinct from *power* (provenance of authority) and *specificity* (clarity of description), which it relieves of carrying outcome-legality.

**Alienation**
:   Alienation is the **VoI + VoP composite** (derive the incident, then allocate it by transfer), not a single primitive. It is the *necessary minimal pattern* for bringing any derived conventional incident into a holder's hands: a derivation alone leaves the incident within the grantor's holding, so at least one allocating transfer must follow. See *Variation of Incidents*, *Variation of Party*.

**Allocated incidents**
:   Public-law authorisations (permits, licences, and time-limited approvals) vested by agencies exercising statutory powers. One of three incident types in the typology used by this paper, alongside *conventional incidents* and *reserved incidents*. In Hohfeldian terms, the issuing authority exercises a *power* to vest a *privilege* in the applicant from the authority's own jural position. The applicant receives something; they do not recover something that was always theirs. Modelled as a VoI derivation with explicit parameterisation of effective period, conditions, and discharge triggers. See *Derivation*, *Variation of Incidents*.

**Amendment**
:   A change to the *terms* of an existing right relationship (a lease extension, a rent review, a change to an easement's scope) where holder, land, and the right's existence are unchanged. Modelled as a continuing version of the same right relationship under its durable identifier (not as absorption followed by a fresh derivation) so that continuity-dependent facts (commencement date, accrued priority, qualifying periods) survive.

**API (Application Programming Interface)**
:   A defined contract through which one software service requests information or actions from another. An API-first design means authoritative services expose their data and functions through stable, documented, machine-readable interfaces that other systems can reliably consume.

**Assessment**
:   The second write operation of the ecosystem, alongside transactional variation. The authorised determination of a *derived fact* about a land object (*value*, *use-class*, or *compliance/discharge status*) as at a date, on a stated basis, contestable through the dispute pathway. Assessment ascribes a fact; it does not change entitlement and it does not alter the land object.

**Authoritative custodian**
:   The agency with the mandate to define, maintain, publish, and correct a given dataset or service. Other agencies reference the custodian's data rather than maintaining diverging local copies. See also: *once-only principle*, *shadow infrastructure*.

**Bitemporality**
:   The recording of two independent timelines on every version of a right or derived fact: *valid time* (when the fact holds in reality which is the basis on which limitation and qualifying periods run) and *transaction time* (when the register recorded it which is the basis for audit and indemnity).

**BPMN (Business Process Modelling Notation)**
:   A standardised graphical notation for representing business processes. Used in this paper to illustrate the permit creation workflow and the agency interactions it depends upon.

**Bundle of rights**
:   The analysis of property ownership as a collection of separable jural incidents (to possess, use, manage, derive income, transmit, and hold residuary character) rather than a single, indivisible entitlement, following Honoré [-@honore_ownership_1961]. These incidents normally travel together but can be separated, constrained, or reallocated individually. This paper uses *incident* as the preferred general term to capture this compound structure. See *Conventional incidents*, *Incident*, *Hohfeldian analysis*.

**Cadastral index**
:   A register of cadastral units providing stable identifiers, geometry, version history, and topology. The backbone service that all other workflows reference to identify unambiguously "what land" is involved in a transaction or permit.

**Cadastral unit (CU)**
:   The administrative object in LADM representing a parcel of land. It carries stable identifiers, is associated with spatial geometry, and provides the reference point for rights, restrictions, and transactions.

**Capability**
:   "Capability" denotes the professional-competence aspect of *capacity* (the professional registration and certification of supporting parties (e.g., surveyors, conveyancers, certifying engineers)) required for a given transaction type. It is evaluated by the *capacity principle*. See *Capacity principle*.

**Capacity principle**
:   One of the five acceptance criteria (a validity check). Requires that parties are legally and professionally capable of granting or receiving rights. Capacity has two limbs: *personal* competence (age, legal competence, inhibitions, sanctions, insolvency freezes and other restrictions on party capacity in the jurisdiction) and *professional* competence (the registration and certification requirements applicable to supporting parties). Professional "capability" is the second limb of this gate, not a separate criterion. See *Capability*.

**Claim-right**
:   In Hohfeldian analysis, the jural position of a holder who is entitled to a specific performance from a correlative duty-bearer. An entitlement enforceable against an identified party. Distinguished from a *privilege*, which merely permits the holder to act without imposing a duty on others. In this paper, conventional private-law incidents (leases, mortgages, easements) create claim-rights in their holders; duty-correlative reserved incidents (planning obligations, restrictive covenants) instantiate the authority's or beneficiary's claim-right with the landowner's duty as its correlative. See *Hohfeldian analysis*, *Privilege*, *No-privilege*.

**Consent principle**
:   One of the five acceptance criteria (a validity check). Requires that where private rights are affected the right-holder's consent is demonstrated and validated, including verification of any authorised representation.

**Conventional incidents**
:   Private-law rights over land created and transferred through conveyancing (e.g., ownership, lease, easement, mortgage). Distinguished from *reserved incidents*, which are public-law constraints imposed by the state.

**Conveyancing**
:   The legal process of transferring, creating, or varying property rights between parties.

**Dealing**
:   Used in two distinct senses. (1) *Tradability sense*: an onward market transfer of a tradable right after its initial allocation: the subsequent independent trading of freehold, leasehold, mortgage, or strata interests. Every dealing is a transaction, but not every transaction is a dealing: the initial grant of a right is a transaction (alienation) but not a dealing in this sense. (2) *Land registration sense*: a registered act or instrument that alters an entry in the title register, the technical meaning in deeds and title-registration systems. Where context does not disambiguate, "transaction" is the preferred general term. See *Tradable*, *Transaction primitive*, *Alienation*.

**Derivation**
:   One of the two directions of a *Variation of Incidents*: the establishment of a new jural incident from an authorised source. For conventional incidents, it carves a claim-right (lease, easement, security, strata interest) from a parent bundle, leaving a residual interest. For reserved incidents, it establishes a restriction or responsibility through a statutory or plan-making process. For allocated incidents, it creates a privilege through the exercise of statutory power. The counterpart of *termination*. Conventional derivation is recursive for certain incidents; allocated incidents are not (a permit cannot be sub-permitted).

**Development control**
:   The regulatory function governing what can be built or changed on land, typically administered through a permitting or planning system.

**Divisible**
:   A type-level property of a right: whether it can be held in undivided fractional shares (co-ownership), and therefore whether the fractional (part) form of a *Variation of Party* is available to it. Independent of *tradable*: the shared areas of a real-estate complex are divisible (held in fractional shares) yet not tradable. Declared in the numerus clausus; restrictable per instance by a recorded term.

**Durable identifier**
:   A stable identity for a right or spatial unit that *persists across variations*. Versions of the entity hang from it, so that continuity-dependent facts (commencement date, accrued priority, qualifying periods) survive a variation. A variation produces a new version under the same durable identifier rather than a new entity.

**Easement / servitude**
:   A right to use another party's land for a specific, defined purpose (e.g., access, drainage, utility corridor). Derived by a VoI and allocated once to the benefiting party by the alienation pattern; being appurtenant, it is referenceable but not tradable onward. Thereafter it runs with the land, moving only when the parcel it benefits is transferred.

**Encumbrance**
:   A right held by a third party that limits (or burdens) a landowners property, limiting the owner's freedom to use  it or transfer its title. While it does not stop the property from being sold, it can diminish its value or impose  ongoing obligations.

**Event-driven architecture**
:   An integration pattern in which services publish notifications when their state changes, allowing subscribing systems to react without polling. Used in this strategy to propagate parcel changes, restriction updates, and rights events across the ecosystem.

**Extinguishment**
:   The public-law counterpart of *absorption*: the cessation of a privilege (permit, licence, or time-limited approval) on expiry, revocation, or breach of conditions. Unlike absorption, extinguishment does not reintegrate anything into a parent bundle: the privilege simply ceases to exist in the holder's hands, and the holder reverts to their prior position of no-privilege. The authority's power to grant further authorisations is unaffected. See *Absorption*, *Allocated incidents*, *Variation of Incidents*.

**Good root of title**
:   The point in a chain of transactions from which title is traced and on the basis of which subsequent dealings are validated. In a deeds-register tradition, the choice of root determines what the register guarantees; in a title-by-registration system, registration itself provides the root and a state guarantee displaces the need to trace further back. The two register traditions are two projections of one ordered transaction log differentiated by the position of good root of title [@beck_effect_2022]. See *Amendment*, *Bitemporality*, *Priority*.

**High-velocity land change**
:   The operating condition of a large-scale programme in which frequent, overlapping subdivision, consolidation, and re-plotting of cadastral units must proceed simultaneously with high-volume permitting and the management of complex public-law constraints. The term defines the environment that motivates the ecosystem architecture and the transactional primitives (VoP, VoL, VoI) proposed in this paper. See *VoL*, *VoP*, *VoI*, *PLR*.

**Hohfeldian analysis**
:   A framework for legal analysis, developed by Wesley Hohfeld, that decomposes legal relations into atomic units: claim-rights, privileges (liberties), powers, and immunities. Used in this paper to distinguish a *privilege* (a freedom to act, owed to no other party) from a *claim-right* (an entitlement enforceable against another), and to characterise the legal nature of permits as privilege-allocations from the granting authority's own jural position. See *Claim-right*, *Immunity*, *No-privilege*, *Privilege*.

**IAM (Identity and Access Management)**
:   The systems and processes governing digital identities, authentication (confirming who a party is), authorisation (defining what they may do), delegation and representation relationships, and the audit trail of actions taken under each identity. In this strategy, IAM is the recommended implementation vehicle for the *Party and Representation service*, covering representation chains, power-of-attorney delegation, company signatory verification, and audited access to transaction services.

**Identifier**
:   A stable, unique reference code assigned to an entity (party, parcel, restriction, permit) that persists across system updates and enables consistent, unambiguous cross-agency referencing.

**Immunity**
:   In Hohfeldian analysis, the jural position that protects its holder from another party's power. The correlative of a *disability* (the other party's incapacity to alter that holder's jural position). Distinct from a *privilege* (freedom from a duty) and a *claim-right* (entitlement against a duty-bearer). Immunities arise in land administration contexts where legislative protections prevent an authority from unilaterally altering a registered right without due process. See *Hohfeldian analysis*, *Claim-right*, *Privilege*.

**Incident**
:   The preferred general term in this paper for any jural position that attaches to, or is allocated over, land: adopted in preference to "right" to reflect the compound and separable structure of what land ownership involves. Three types are distinguished: *conventional incidents* (private-law claim-rights created through conveyancing), *reserved incidents* (public-law restrictions and responsibilities imposed by statute or plan-making), and *allocated incidents* (public-law privileges vested by statutory authority). The term follows Honoré's [-@honore_ownership_1961] analysis of ownership as a bundle of separable standard incidents. See *Bundle of rights*, *Conventional incidents*, *Reserved incidents*, *Allocated incidents*.

**LADM (Land Administration Domain Model)**
:   ISO 19152; an international standard providing a conceptual model and shared vocabulary for land administration systems. Supplies the Party--Right--Land framework underpinning the VoP/VoL/VoI transaction primitives used in this strategy.

**Land object**
:   In LADM  the composite entity comprising an *administrative unit* (the rights package) and its associated *spatial unit* (geometry/extent). The term emphasises the spatial reference used when identifying what land is involved in a transaction or permit. *Property object* refers to the same entity emphasised as the first-class holder of a rights bundle from which incidents are derived or into which they are absorbed. See *Administrative unit*, *Spatial unit*, *Property object*.

**Land Object index**
:   A shared service that mints stable, persistent cross-agency identifiers for land objects and resolves any identifier to the authoritative service that owns it. It does not consolidate geometry; it provides a single resolution point so that rights and permits can unambiguously reference "what land" regardless of which custodian holds the authoritative geometry. New identifiers are published only after the relevant authority service has validated and committed the corresponding spatial change. See *Cadastral index*, *Identifier*, *Once-only principle*.

**Lifecycle specification**
:   The set of properties on a jural incident that govern when it activates and when it terminates: an effective period, the conditions under which it activates, and the triggers (expiry, surrender, satisfaction of an obligation, a staged-release milestone, or statutory rescission) that cause termination. Treating lifecycle as a first-class property of each incident type means that leases, easements, securities, permits, and PLR zones share the same structural shape with different parameters, rather than requiring separate instrument logic for each. See *Termination*, *Amendment*, *VoI*.

**Mandate**
:   The legal authority conferred on an agency to perform a specific public function. In this strategy, agencies improve services within their existing mandate; no transfer of mandates between agencies is required.

**No-privilege**
:   In Hohfeldian analysis, the absence of a privilege: the jural position of a party that lacks the freedom to perform a given act. In this paper, no-privilege is the precise characterisation of a landowner's position with respect to a restricted activity under a public-law constraint. The landowner does not hold a duty-not-to-develop (which would imply a claim-right in another party that could be released), but rather lacks the privilege to act in the first place. A permit does not lift a restriction; the issuing authority vests a privilege from its own jural position. See *Privilege*, *Hohfeldian analysis*, *Allocated incidents*, *Reserved incidents*.

**Numerus clausus**
:   Latin for "closed number." The principle that only a defined set of right types can be carved from a bundle and vested to third parties; parties cannot create novel incidents with the character of property by agreement alone. In this paper, the numerus clausus is the typed registry of derivable incident types for a jurisdiction, each carrying a Hohfeldian signature (jural position, correlative, divisibility, tradability). The *admissibility* gate checks that a proposed transaction produces an incident within this recognised set. See *Admissibility principle*, *Rights Ontology service*, *VoI*.

**Once-only principle**
:   The design principle that authoritative information should be recorded and maintained once by the responsible custodian and reused by other agencies through governed services, rather than re-entered or re-created in local copies that may diverge. See also: *authoritative custodian*, *shadow infrastructure*.

**Party**
:   In LADM, an entity (e.g., natural person, legal person, or organisation) that can hold registerable rights or act in land transactions. Parties also possess *powers* that determine what transactions they can lawfully initiate or consent to.

**Pattern library**
:   A collection of documented, reusable compositions of transaction primitives (VoP, VoL, VoI) covering recurring complex scenarios (e.g., real estate complexes, utility corridors, stacked rights in multi-use buildings). Patterns allow complex workflows to be assembled from known building blocks without expanding the underlying transaction surface.

**Permit**
:   A time-bound authorisation issued by a public authority, conferring on the holder a lawful permission to undertake an otherwise restricted activity on specified land, subject to defined conditions and an effective period.

**Plan hierarchy**
:   The layered structure of planning and land regulation instruments (national policy, regional plan, local plan, site-level conditions) in which lower-tier instruments must conform with those above them. The admissibility gate applies at two levels: it checks that a proposed transaction conforms with applicable PLR constraints *and* that any plan-making instrument is consistent with the tier above it. See *Admissibility principle*, *PLR*, *Reserved incidents*.

**PLR (Public Law Restriction)**
:   A restriction, constraint, or responsibility imposed on land or its use by legislation, regulation, or planning instrument (e.g., planning zones, heritage designations, environmental buffers, safety exclusion zones). Treated in this strategy as first-class, spatially queryable objects with defined authority, versioning, and applicability conditions. See also: *reserved incidents*.

**PoA (Power of Attorney)**
:   A legal instrument by which a principal authorises a named attorney to act on their behalf for defined purposes. In this strategy, a PoA is a representation instrument: the attorney holds no independent power, so the power and capacity acceptance checks run against the *principal*. The *Party and Representation service* must verify that the PoA is valid, current, and covers the proposed transaction type; an enduring PoA additionally requires confirmation that capacity was present at execution. See *Representation*, *Capacity principle*, *Power principle*.

**Power (legal)**
:   The legal capacity to effect a specific change in a Party--Right--Land relationship. Private-law powers derive from rights held (a party can only grant what it has); public-law powers derive from legislative or regulatory authority. Verification of power is a prerequisite for any valid transaction.

**Power principle**
:   One of the five acceptance criteria (a validity check). Requires that every transaction be supported by the granter's legal power, whether derived from rights held or from legislative empowerment.

**Praedial right**
:   A right that attaches to land rather than to a person, and runs with the land when it is transferred. A praedial relationship means that one parcel holds rights in another parcel, with those rights passing automatically to whoever owns the benefiting parcel.

**Priority**
:   The ranking between competing rights over the same land object (typically securities). A property of the *relationship* between rights, not of any single right: the default order derives from valid time (first in time) and is overridden by explicit subordination, postponement, or tacking transactions. A change of priority is itself a first-class, validated transaction.

**Privilege**
:   In Hohfeldian analysis, a freedom to perform an act without owing a duty to any other party to refrain from it. Distinguished from a *claim-right*. In this paper, issuing a permit is characterised as the authority allocating a privilege from its own jural position to the applicant. It is not restoring a pre-existing entitlement to someone from whom it was withheld.

**Property object**
:   A legal construct comprising an administrative unit (the rights package) and its associated spatial unit (geometry). This is considered specifically as the first-class holder of a rights bundle. Distinguished from *land object* (which emphasises the spatial reference) in contexts where rights are being derived from or absorbed back into the bundle: a VoI absorption takes a separated right back into the property object's bundle rather than simply referencing the land's spatial extent.

**Real estate complex**
:   A multi-unit development (block of flats, mixed-use compound) in which individual units are separately owned and common areas are held collectively by unit owners. Modelled in this strategy as a documented composition of VoL, VoI and VoP transactions (see Appendix 1 of the conceptual foundation).

**Referenceable**
:   The property, required of every first-class object (party, parcel, right, PLR, permit), of carrying a durable or at least trusted, authoritative, versioned identifier so that other services can depend on it. The foundation for the once-only principle.

**Representation**
:   The legally recognised authority of one party (agent, attorney, company signatory) to act on behalf of another in land transactions. The ecosystem must model and verify representation consistently so that "who can act for whom?" can be answered auditably at every submission.

**Rescission**
:   The termination form for reserved incidents: a PLR or other public-law restriction is brought to an end through the same statutory or regulatory process that created it. The counterpart of its derivation. Distinguished from *extinguishment* (which applies to allocated incidents/privileges) and *absorption* (which applies to conventional incidents). See *Termination*, *Variation of Incidents*.

**Reserved incidents**
:   Public-law constraints imposed by the state that limit what the holder of conventional property rights may do with land (e.g., planning controls, environmental restrictions). Permits may enable activities that would otherwise be restricted under reserved incidents. See also: *PLR*.

**Responsibility**
:   A positive duty (the holder must perform rather than merely refrain) that may run with land or party (e.g., a development contribution, an affordable-housing condition, a maintenance obligation). In Hohfeldian terms, a responsibility is the landowners' duty that results from a claim-right held by a third party; it differs from a *restriction* only in the direction of the obligation (positive vs negative). A responsibility may arise as a component of a reserved incident (imposed by statutory or plan-making process) or a conventional incident (a positive covenant in a private instrument). Its discharge status is determined by *assessment* and may be enforced as a charge on default. See *Restriction*, *Reserved incidents*, *Hohfeldian analysis*.

**Restriction**
:   A negative duty (the holder must refrain) imposed on land or its use. In Hohfeldian terms a restriction is the landowners' duty that results from a claim-right held by a third party; it differs from a *responsibility* only in the direction of the obligation (negative vs positive). A duty-correlative restriction (a restrictive covenant, a planning obligation owed to an identified body) is released when that holder waives or is satisfied; a disability-type restriction (a development right reserved to the authority) leaves the landowner in a position of *no-privilege* that a permit does not lift but a privilege-allocation supplies. See *Responsibility*, *Reserved incidents*, *No-privilege*.

**Rights Ontology service**
:   A proposed platform service holding the typed *numerus clausus* for a jurisdiction: the schema of permissible incident types, each with its Hohfeldian signature, the power requirements for each transaction type, capacity rules, and admissibility constraints. Separating the rules governing what rights *may* exist from the register recording what rights *do* exist allows the rule set to be versioned independently as legal regimes evolve. See *Numerus clausus*, *Admissibility principle*, *VoI*.

**Security**
:   A right granted over land to secure a financial obligation (e.g., a mortgage or charge). Derived by a VoI; it is discharged and absorbed back into the parent cadastral unit when the underlying obligation is met.

**Shadow infrastructure**
:   Workaround systems or local data copies created by downstream agencies when authoritative services do not provide the identifier stability, versioning, or quality those agencies need. Shadow infrastructures diverge from the authoritative source over time and undermine the once-only principle.

**Spatial unit**
:   In LADM, the geometric extent component of a land object. Combined with an administrative unit (the rights package), it fully represents what practitioners informally call a "parcel."

**Specificity principle**
:   One of the five acceptance criteria, and the only *well-formedness* check (the others test validity). Requires that a transaction unambiguously identifies: the *subject* (the Party--Right--Land state being changed), the *transformation* (VoP, VoL, or VoI), and the *variables* (the parameters needed to evaluate and enact the change).

**Strata title**
:   A form of property ownership in multi-storey or multi-unit buildings in which individual units are separately owned and common areas are held collectively by unit owners. Modelled in this strategy as a VoI derivation from the principal cadastral unit.

**Termination**
:   The ending direction of a *Variation of Incidents*: the operation that closes an existing jural incident. Termination takes a form matched to the incident type. *Absorption* applies to conventional incidents: the separated claim-right is reintegrated into its parent bundle (on expiry, surrender, or satisfaction of the obligation it secured). *Extinguishment* applies to allocated incidents (public-law privileges): the privilege simply ceases to exist in the holder's hands (on expiry, revocation, or breach of conditions), with nothing returning to any parent holding. *Rescission* applies to reserved incidents: a PLR is brought to an end through the same statutory or regulatory process that created it. All three forms are first-class operations; recording a derivation without a termination pathway leaves dangling encumbrances. See *Absorption*, *Extinguishment*, *Derivation*, *Variation of Incidents*.

**Tradable**
:   A type-level property of a derived right: whether it can undergo *subsequent, independent* transfers on a market *after* its initial allocation. The conveyancing market transacts tradable rights (freehold, leasehold, strata, mortgage), which demands persistent, chain-traceable, priority-bearing identifiers. Tradability governs *onward* dealing only. Every derived right is allocated once by the alienation pattern regardless of tradability; a non-tradable right (an easement) is allocated at grant and thereafter passes appurtenant to its parent. Independent of *divisible*; tradability implies referenceability, but not the reverse. Restrictable per instance by a recorded term (e.g., a non-assignability covenant).

**Transaction primitive**
:   One of the three core, reusable state-change patterns (VoP, VoL, VoI) from which land administration workflows are composed. Each is a variation representing a subdivision or consolidation along one axis of the party--right--land triple. Treating these as primitives keeps the transaction service surface small and stable, while allowing complex scenarios to be built as documented compositions.

**VoI (Variation of Incidents)**
:   The primitive that creates, varies, or terminates any jural incident (conventional, reserved, or allocated) associated with a land object. Its two directions are *derivation* (establishing a new incident from an authorised source) and *termination* (closing an existing incident). Termination form is matched to incident type: *absorption* for conventional incidents, *extinguishment* for allocated incidents, *rescission* for reserved incidents. The recognised set covers the private-law *numerus clausus*, the jurisdiction's recognised PLR types, and its recognised statutory authorisation types. Conventional derivation is recursive; allocated incidents are not. For conventional incidents, VoI derivation is always followed by an allocating VoP (the *alienation* pattern); for allocated incidents, derivation and transfer are a single act. VoI also separates jural content changes (its domain) from spatial extent changes (VoL's domain).

**VoL (Variation of Land)**
:   A generic transaction pattern that changes *what land* a right bundle describes through subdivision or consolidation of spatial units. Because VoL is generic, it applies to any spatially-defined right object: cadastral parcels, planning zones, environmental buffers, heritage areas, and other public-law restriction (PLR) objects. Any alteration to a PLR's spatial extent (redrawing a zone boundary, extending a buffer, splitting a heritage area) is a VoL operation subject to the same acceptance criteria as a cadastral subdivision. **A boundary determination that fixes, adjusts, or re-defines authoritative geometry is a VoL**. VoL is the operational workhorse of high-velocity land change; it requires geometry integrity checks (no gaps or overlaps), recognised survey inputs, and versioned identifier management so that permits and rights always reference the correct spatial state.

**VoP (Variation of Party)**
:   The primitive that varies who holds a right/incident. Where the right is *divisible*, the holding is a fraction and a VoP may subdivide it (a part transfer creating co-ownership) or consolidate it (re-uniting co-owners' shares); for an indivisible right a VoP transfers the whole or nothing. The whole-or-part transfer of a holding from one party to another is its familiar pattern, the *transfer of party*. A VoP can act on a tradable right as an independent object; in addition, every derived right receives at least one allocating VoP at grant (the alienation pattern), even when it is not tradable thereafter.
