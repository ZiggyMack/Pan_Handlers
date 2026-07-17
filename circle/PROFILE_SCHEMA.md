# 📜 Profile Schema — The Contract

> Every member profile follows this schema. If a profile and this schema disagree,
> either fix the profile or revise this schema with a logged version bump — never
> let them drift silently.
>
> Derived from `ARCHIVE_PLAN.md` §I (Design Principles) and §III (Profile Schema).

**Schema version:** 1.0 (2026-07-16)

---

## 1. Confidence Labels (mandatory on every claim)

| Label | Meaning | Minimum evidence |
| ------- | --------- | ------------------ |
| `DIRECT` | Explicitly stated by the member | ≥1 source link to their own words |
| `REPEATED` | Observed across several discussions | ≥2 independent source links |
| `INFERRED` | Explanatory hypothesis supported by evidence | stated reasoning + whatever evidence exists |
| `CONTESTED` | Disputed by the member or another observer | link to the objection |
| `STALE` | May no longer represent the member | original source + date; flag age |
| `UNKNOWN` | Not enough evidence | nothing — and say so |

**Claim format convention** (inline, end of claim):

```text
Grant treats predictive success as the final court of appeal. (INFERRED; sources: none yet; observer: Ziggy)
```

Rules:

- A claim with no label is an **invalid claim** — fix it or delete it.
- `DIRECT` and `REPEATED` require source IDs from the member's `SOURCE_INDEX.md`.
  No source, no label above `INFERRED`.
- Every inference names its **observer** (who made it). The archive never conceals
  whose interpretation a claim is — especially Ziggy's (see `ETHICS_AND_CONSENT.md`).
- When a member disputes a claim, the label becomes `CONTESTED` — the original
  claim is *kept*, the dispute is linked. Contested ≠ deleted, and contested ≠ defeated.

## 2. Source IDs

Each member's `SOURCE_INDEX.md` assigns IDs: member initials + sequence number
(`Z-001`, `G-001`, `TR-001`, `A-001`, `H-001`, `S-001`, `SW-001`, `C-001`).
A source entry records: ID, date, medium (chat / voice / debate thread / doc),
location or excerpt, and which claims cite it.

Raw evidence from past chats arrives via extraction packets
(`CHAT_EXTRACTION_PROTOCOL.md` → `evidence/chat_extractions/`). Packets use their
own six-way source-discipline labels (G-DIRECT, G-REPORTED, Z-DIRECT,
NOVA-INTERPRETATION, CO-CONSTRUCTED, UNCLEAR); the mapping into this schema's
labels happens **only at promotion time**, per the table in protocol §XV.
Key rule inherited from that table: reported speech is `DIRECT` about the
reporter, at most `INFERRED` about the person reported.

## 3. Position vs Operator (never blur these)

- **Position** — what someone believes. Lives in `POSITION_LEDGER.md`.
  States: `ACTIVE` / `REVISED` / `ABANDONED` / `AMBIGUOUS` / `CONTESTED` / `UNKNOWN`.
- **Operator** — the recurring cognitive move used to reach/defend/revise/reject
  beliefs. Defined once in `../OPERATOR_LEXICON.md` (shared vocabulary, CO-### IDs),
  instantiated per-member in `OPERATOR_MAP.md` with member-specific evidence.

Positions may change while operators remain stable — that is precisely the
phenomenon this archive exists to track.

## 4. Member Folder Layout

```text
NN_MEMBER/
├── PROFILE.md           # Sections A–C, H–K (orientation, commitments, strengths,
│                        #   debate behavior, tensions, open questions summary)
├── OPERATOR_MAP.md      # Sections D–E: operators (cite CO-### from lexicon) + sequences
├── POSITION_LEDGER.md   # Section F: positions with states + revision history
├── IDEA_TRAILS.md       # Section G: member's view into circle-wide trails
├── DEBATE_HISTORY.md    # Section H detail: links into ../../DEBATES/ records
├── RELATIONSHIPS.md     # Section J: intellectual dynamics with other members
├── OPEN_QUESTIONS.md    # Section K: what the profile cannot yet answer + falsifiers
├── SOURCE_INDEX.md      # Section 2 above: the evidence ledger
├── MEMBER_RESPONSE.md   # Section L: the member's rights of reply, recorded verbatim
└── archive/             # superseded profile versions (copy before major revision)
```

## 5. Required Sections (A–L)

Every `PROFILE.md` opens with **A. Orientation**: name/handle, role in circle,
relationship to project, domains most discussed, profile version, last review date,
contributing observers, and a **freshness notice** (how stale might this be?).

| Section | Home file | Non-negotiables |
| --------- | ----------- | ----------------- |
| A. Orientation | PROFILE.md | version, date, observers, freshness notice |
| B. Self-Declared Commitments | PROFILE.md | `DIRECT` claims **only** — nothing inferred belongs here |
| C. Observed Cognitive Strengths | PROFILE.md | each strength: evidence + **failure conditions** |
| D. Recurring Operators | OPERATOR_MAP.md | name, CO-### ref, evidence, trigger, output, productive use, failure mode, counter-operator, confidence |
| E. Operator Sequences | OPERATOR_MAP.md | ordered chains; **hypotheses until validated across multiple debates** |
| F. Position Ledger | POSITION_LEDGER.md | original formulation + **strongest reconstruction** + revisions + state |
| G. Idea Trails | IDEA_TRAILS.md | seed / introducer / transformers / unlocking distinction / branches / unfinished / inheriting project |
| H. Debate Behavior | PROFILE.md + DEBATE_HISTORY.md | offense, defense, neutral analysis, private reflection, group, one-on-one — **kept separate** |
| I. Productive Tensions | PROFILE.md | recorded, not prematurely resolved |
| J. Relationship Dynamics | RELATIONSHIPS.md | intellectual interactions only — complementarities, friction points, translation failures, repair mechanisms, load-bearing shared jokes. **Not gossip.** |
| K. Open Questions | OPEN_QUESTIONS.md | includes **what evidence would falsify** each major interpretation |
| L. Member Response | MEMBER_RESPONSE.md | endorse / reject / revise / annotate / supply context / challenge labels — recorded verbatim, never paraphrased away |

## 6. Section H discipline — the offense/defense firewall

Strategic debate behavior is **not** a person's complete epistemology. A move made
under adversarial pressure gets logged under the context it appeared in. A pattern
only graduates to "recurring operator" when observed across **at least two distinct
contexts** (e.g., offense AND neutral analysis).

## 7. Versioning & Freshness

- Versions: `0.0` stub → `0.x` pre-review drafts → `1.0` after first member
  response → increment thereafter.
- **Major revision** (operator added/removed, position state changed, member
  response integrated): copy the old profile into `archive/` first, then bump.
- Every file carries `Last reviewed:` at top. Any claim older than ~6 months
  without re-confirmation should be considered for `STALE`.
- Register every version bump in `../INDEX.md`.

## 8. JSON Companion

Each member folder carries `<member_id>.json` mirroring the markdown for dashboards
(see `ARCHIVE_PLAN.md` §VII for the shape). **Markdown is canonical**; JSON is
derived. When they disagree, markdown wins and JSON gets regenerated.

## 9. What Discriminates vs What Decorates

The Grant pilot's meta-goal (`ARCHIVE_PLAN.md` §VI Phase 1): discover which schema
sections actually *discriminate between cognitive architectures* and which merely
produce biography. Record schema pain points in `OPEN_QUESTIONS.md` under
"Schema feedback" — Phase 3 profiles are the test of whether we captured genuinely
different architectures or renamed the same generic traits eight times.
