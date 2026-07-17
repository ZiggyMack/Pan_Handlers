# 👻 Ghosts in the Machine: The PanHandlers Cognitive Circle

> *"Profile the reasoning, not the soul."*

This directory is the durable archive of the PanHandlers core debate circle — the
people, reasoning operators, idea trails, unresolved disagreements, and collaborative
discoveries that generated the wider project ecosystem.

It is **not** a personality database. It is a living cognitive history: who carried
which ideas, which operators generated them, where debates branched, what changed,
and what remains unfinished.

---

## The Circle

| # | Member | Folder | Role |
| --- | -------- | -------- | ------ |
| 0 | Ziggy | `MEMBERS/00_ZIGGY/` | Primary observer — profiled as **symmetry control** |
| 1 | Grant | `MEMBERS/01_GRANT/` | **Pilot profile** (Phase 1) |
| 2 | Tale Recursion | `MEMBERS/02_TALE_RECURSION/` | Phase 3 |
| 3 | Angles | `MEMBERS/03_ANGLES/` | Phase 3 |
| 4 | Hugz | `MEMBERS/04_HUGZ/` | Phase 3 |
| 5 | Sassy | `MEMBERS/05_SASSY/` | Phase 3 |
| 6 | Snow White | `MEMBERS/06_SNOW_WHITE/` | Phase 3 |
| 7 | Chrome | `MEMBERS/07_CHROME/` | Phase 3 |

Current status of every profile: see [`INDEX.md`](INDEX.md).

---

## The Five Laws (condensed)

1. **Profile the reasoning, not the soul.** Observable argument patterns only.
   Temporary behavior never becomes permanent identity.
2. **Every claim gets a confidence label.** `DIRECT` / `REPEATED` / `INFERRED` /
   `CONTESTED` / `STALE` / `UNKNOWN`. An unlabeled claim is an invalid claim.
3. **Separate position from operator.** What someone believes vs. the recurring
   cognitive move used to get there. Positions drift; operators persist.
4. **Preserve contradictions.** They are research questions, not defects.
5. **Profiles remain revisable.** Versioned, dated, attributed, and answerable —
   every member gets a `MEMBER_RESPONSE.md` with full rights of reply.

Full contract: [`PROFILE_SCHEMA.md`](PROFILE_SCHEMA.md) ·
Founding charter: [`ARCHIVE_PLAN.md`](ARCHIVE_PLAN.md) ·
Ethics: [`ETHICS_AND_CONSENT.md`](ETHICS_AND_CONSENT.md)

---

## Directory Map

```text
circle/
├── ARCHIVE_PLAN.md        ← founding charter (canonical intent)
├── README.md              ← you are here
├── INDEX.md               ← status board for all profiles & phases
├── PROFILE_SCHEMA.md      ← the profile contract (sections A–L)
├── OPERATOR_LEXICON.md    ← shared vocabulary of cognitive operators
├── RELATIONSHIP_MAP.md    ← Phase 4: operator-meets-operator dynamics
├── ETHICS_AND_CONSENT.md  ← safeguards, member rights, publication gate
├── CHAT_EXTRACTION_PROTOCOL.md ← the dig instrument (v0.2 ACTIVE — staged execution)
├── CHAT_EXTRACTION_PROTOCOL_v0.1.md ← superseded original, kept as provenance
├── CONSENT_REGISTER.md    ← consent basis for the public archive (per-member scope)
├── evidence/
│   └── chat_extractions/  ← extraction packets from old-chat digs (staging, most restricted)
├── IDEA_TRAILS/           ← cross-member idea lineage registry
├── DEBATES/               ← individual debate records
├── SHARED_HISTORY/        ← chronology, shared jokes/symbols that carry meaning
└── MEMBERS/
    ├── _TEMPLATE/         ← canonical member-folder skeleton (copy to start)
    └── 00–07 …            ← one folder per circle member
```

---

## How to Work in This Archive

- **Adding a claim about a member** → it goes in their folder, with a confidence
  label and a source link into their `SOURCE_INDEX.md`. No source, no claim above
  `INFERRED`.
- **Mining a past chat** → use `CHAT_EXTRACTION_PROTOCOL.md` v0.2: send its four
  stage commands **one at a time, each with the execution wrapper** — never the
  whole protocol at once (old chat = excavation; fresh thread = synthesis). File
  the packet in `evidence/chat_extractions/`; only Stage-4 PROFILE-READY CLAIMS
  promote into profiles, via the protocol's Archive Integration rules.
  Cross-chat recurrence earns promotion.
- **Naming a new operator** → define it in `OPERATOR_LEXICON.md` first (status:
  CANDIDATE), then instantiate it in the member's `OPERATOR_MAP.md` with evidence.
  Operators are shared vocabulary, not member property.
- **Recording a debate** → one file in `DEBATES/`, linked from each participant's
  `DEBATE_HISTORY.md`.
- **A member disagrees with their profile** → record it in their
  `MEMBER_RESPONSE.md` and mark affected claims `CONTESTED`. Never delete the
  disagreement.
- **Starting a new member profile** → copy `MEMBERS/_TEMPLATE/`, register in
  `INDEX.md`, version starts at 0.1.

---

## 📢 Publication Status: PUBLIC

By Ziggy's decision (2026-07-16), the whole archive is public: *"we are not
focusing on personal information — we are focusing on ideas; all members gave
consent to share their ideas"* (basis: [`CONSENT_REGISTER.md`](CONSENT_REGISTER.md)).
The protection is the **content boundary**, enforced at ingestion: sensitive
personal, non-reasoning material never enters the archive at all. Read
[`ETHICS_AND_CONSENT.md`](ETHICS_AND_CONSENT.md) §2–3 before adding member content.

---

*These are the things we built together that none of us could have built alone.*
