# ⛏️ Chat Extractions — Evidence Staging

> Landing zone for extraction packets produced by running
> `../../CHAT_EXTRACTION_PROTOCOL.md` inside past chat instances.
>
> 📢 **Public like the rest of the archive — which makes this the directory where
> the ingestion filter matters most.** Packets are raw, pre-review mined material:
> run the protocol's §XIV constraints *during* extraction, and remember that
> QUARANTINED means "not profile-grade," not "hidden" — write even quarantined
> claims to publication standard (`../../ETHICS_AND_CONSENT.md` §2).

**Status:** 0 packets filed · **Last reviewed:** 2026-07-16

---

## How This Directory Works

- **Dig workbooks** (`DIG_00.md` … `DIG_11.md`, template `_TEMPLATE_DIG.md`) —
  one per source conversation. Each is self-contained: the four stage prompts
  ready to copy, with an output slot under each. Work top to bottom; pasted
  outputs are **immutable** once in (fifth-artifact rule).
- **Synthesis packets** (`<subject-or-topic>_<slug>_<YYYY-MM>.md`, dated by the
  source chat) — derived artifacts assembled at filing from a COMPLETE workbook:
  header, promoted claims, cross-references back into the workbook. Excavation
  and synthesis stay separate so audits can catch synthesis drift.
- A workbook missing a stage output is not promotable. Profiles never cite
  workbooks or packets directly — they cite `SOURCE_INDEX.md` entries (promotion
  rules: the protocol's Archive Integration section).
- **Profile recursion (the FILED step, made explicit):** when a dig closes,
  Stage-4-cleared material flows to *three* places, not two: (1) the member's
  `SOURCE_INDEX.md`, (2) the synthesis packet, and (3) **the member's
  profile-layer documents** (`OPERATOR_MAP.md`, `POSITION_LEDGER.md`, and the
  PROFILE's Provisional Evidence Ledger) at their promotion ceiling.
  Candidate/sweep material updates instance counts in the member's operator
  map without asserting traits. Profiles grow recursively with every close —
  the Phase-2 synthesis will be built *from* these ledgers, not from scratch.
- **Field-desk reviews** (Nova's verdicts on stage outputs — run the next stage,
  repurpose, quarantine constraints, expected mappings) are filed *in the
  workbook* as `🧭 FIELD-DESK REVIEW` blocks after the relevant OUTPUT section:
  the dig's decision log, attributed as NOVA-INTERPRETATION about the
  extraction, never promotable as chat evidence. Her *predictions* register in
  the relevant idea-trail or dig file **before** the predicted stage returns,
  so they stay scoreable. Her *norms* go to `SHARED_HISTORY/TIMELINE.md`.
- **Contamination check (v0.2.2):** the dig operator's account shares context
  across chats, so leakage is ambient. If a stage output cites other
  conversations or spans a date range, STOP — preserve it in
  `../corpus_sweeps/` (orientation only) and run the Scope Repair command from
  the protocol appendix. Cross-chat recollections belong in X-CONTEXT Notices,
  where they become *dig leads*, never evidence. Anchor verification at filing
  is the enforceable line.
- QUARANTINED CLAIMS never leave their packet until corroborated by another packet.
- A packet is a `DETAILED NOTES`-fidelity source about the chat unless it carries
  verbatim quotes — quoted spans are `TRANSCRIPT`-fidelity for the words quoted.

## Dig Board

**How digs are run (opportunistic, by design):** the dig operator doesn't need to
remember what's in an old chat — that's what the excavation is *for*. Pick any
old conversation, **run the workbook's HUMAN PREFLIGHT** (skim first/last
messages — titles lie in reused chats), then claim the next EMPTY workbook in
numeric order and run the four prompts. Stage 1's output tells us what the chat
actually holds; record it in the Discovered topic column here and in the
workbook's header.

**Plow-through mode (compound sites):** the operator may run wholesale stages
2–4 on a compound thread as *data collection* — Stage 1 source survey → broad
candidate harvest → pressure-test → **provisional mapping only**. Firm rule
(Nova, 2026-07-17): **wholesale compound digs generate leads; they never
promote operators or profile claims without later bounded sub-dig
confirmation.** Field desk marks each output: *clean dig / compound sweep /
profile-capable / orientation only / candidate source for sub-dig*. Child-dig
scope locks are preserved in the parent workbook's field-desk blocks for the
double-back.

**Auxiliary digs (`DIG_AUX_NN_*.md`):** a bounded, scope-clean extraction whose
thread turned out to hold a different subject than intended is not discarded —
it's renamed as an AUX dig and repurposed for whatever it actually evidences
(precedent: DIG_AUX_01, a valid Ziggy/shared-history dig that was aiming for
Grant). Aux digs follow all the same rules; only the campaign changes.
DIG_AUX_00 is a special case: the workbook-form record of the original
scope-creep run — orientation only, canonical copy in `../corpus_sweeps/`.

| Workbook | Discovered topic (after Stage 1) | Status |
| --- | --- | --- |
| `DIG_AUX_00_Scope_CREEP.md` | *(record of the contaminated first run — canonical copy in SWEEP_00)* | ORIENTATION ONLY — NOT PROMOTABLE |
| `DIG_AUX_01_repo_nova_institutional_identity_2026-07.md` | Repo Nova's institutional evolution; Repo Claude complementarity; extraction-design history | STAGE 1 COMPLETE — REPURPOSED (Ziggy/shared-history evidence; Stages 2–4 postponed) |
| `DIG_AUX_02_invariance_and_stable_structure_2026-07.md` | Invariance as transformation-relative stability (Ziggy–Nova conceptual exchange) | ✅ **FILED** — first dig through all 4 stages; seeded IT-014, CO-009, CO-010, Z-001; synthesis: `ziggy_nova_invariance_2026-07.md` |
| `DIG_AUX_03_prediction_ontology_and_effective_theories_2026-07.md` | Prediction vs truth: does predictive success settle ontology? (real clash; Ziggy/Nova; NO Grant evidence) | ✅ **FILED** — 2nd full-pipeline dig; crosswalk executed; yielded CO-011, Z-002, IT-015 close-out, synthesis packet |
| `DIG_AUX_04_bell_boundaries_and_metaphysical_continuations_2026-07.md` *(retitled at close)* | Bell boundaries: conjunction logic; exhaustiveness challenge; claim-scope repair — strongest Ziggy evidence to date; technical-risk HIGH | ✅ **FILED** — 3rd full-pipeline dig; yielded CO-012/013/014 (first Ziggy-attributed operators), Z-003, IT-016 (⚠️ tech gate), synthesis packet |
| `DIG_00.md` | *(reserved: CFA-zero — preflight required; workbook recreated after its file was consumed by a rename)* | EMPTY |
| `DIG_00ABCD.md` *(operator's working name — proper identity assigned at field-desk review)* | Grant's evaluative architecture via the CT/Moral-Substance dispute + development of Diagnostic Interrogation, Coupling Probes, Cognitive Archaeology calibration, invariant-seeking methodology (heavy G-REPORTED; no G-DIRECT) | IN PROGRESS — Stages 1–2 pasted; awaiting field-desk reviews |
| `DIG_01_classical_theism_evil_and_moral_generativity.md` | ⭐ **First Grant-relevant site**: reported 12-step problem-of-evil syllogism → moral-generativity zero; Ziggy's modal-burden + trade-off objections; Grant's reported denial (G-QUOTED-REPORTED) | ✅ **FILED** — 4th full-pipeline dig; **G-001 (first Grant source, reported ceiling)**, Z-004, IT-017, synthesis packet; restraint round: zero new operators, one recorded error (Logical-Status Compression) |
| `DIG_COMPOUND_SWEEP_02_maps_experience_values_and_plausibility.md` *(renamed at close per field desk)* | ⚡ Compound sweep: maps, experience, values, plausibility; ⚠️ privacy gate active | ✅ **COMPLETE — candidate harvest, ZERO promotions (plow-through rule held)**; 3 sweep-strong candidates queued; seeds IT-018; sub-digs A/B/C queued (segment-D scope lock preserved in workbook) |
| `DIG_02.md` | *(reset to clean template for reuse)* | EMPTY |
| `DIG_COMPOUND_SWEEP_03_foundations_justification_and_jurisdiction.md` | ⚡ Compound sweep: Münchhausen trilemma → framework-relative justification → single-value underdetermination → **jurisdiction of justification** (checklist theme #4 — Z-06's home trench) | ✅ **COMPLETE — candidate harvest, ZERO promotions (plow-through held again)**; 2 retain-RED candidates queued (Framework Transplant, Constraint-Exhaustion Stress Test); Jurisdiction Challenge = CO-002's corrective test; seeds IT-019 |
| `DIG_03.md` | | EMPTY |
| `DIG_04.md` | | EMPTY |
| `DIG_05.md` | | EMPTY |
| `DIG_06.md` | | EMPTY |
| `DIG_07.md` | | EMPTY |
| `DIG_08.md` | | EMPTY |
| `DIG_09.md` | *(template consumed into COMPOUND_SWEEP_05)* | — |
| `DIG_COMPOUND_SWEEP_05_prediction_trust_law_and_master_frames.md` | ⚡ Compound sweep: can prediction, truth, suffering, law, religion, or consciousness serve as a **master frame**? Curt Jimungal video entry; presup/method dispute; Grant G-REPORTED only; extractor self-flagged heavy NOVA-INTERPRETATION load ("prediction is a servant," "optimization function") — direct sequel to SWEEP_04's masters neighborhood | 🟡 IN PROGRESS — Stage 1 pasted; Stages 2–4 pending |
| `DIG_10.md` | *(template consumed into COMPOUND_SWEEP_04)* | — |
| `DIG_COMPOUND_SWEEP_04_belief_prediction_foundations_and_masters.md` | ⚡ Largest sweep yet — 5 neighborhoods; spine: belief/justification → foundations → **masters** → CFA meta-audit; ⚠️ external-model contamination risk HIGH (Grok/Claude echoes ≠ witnesses); 6 sub-digs queued (E = prediction/truth/masters is the prize) | ✅ **COMPLETE — candidate harvest, ZERO promotions (plow-through held, 3rd consecutive)**; 3 serious candidates queued (Master-Value Extraction HIGH; Instrument≠Telos ×3; Reflexive Audit protocol); seeds IT-020/021/022; sub-digs E/F = promotion paths |
| `DIG_11.md` | *(template consumed into DIG_AUX_05)* | — |
| `DIG_AUX_05_story_genre_wisdom_compression_and_orientation.md` | Story as wisdom compression; genre plurality vs Hero's Journey; Ethos/Pathos/Logos as orientation channels; **first Tale Recursion appearance**; 3 assistant-imported Grant positions caught & ruled UNSUPPORTED | STAGE 3 COMPLETE — Stage 4 authorized; A3 standard sharpened (specific move demonstrated in-thread, not general ability); orientation weakened to organizing hypothesis; clearest rigor failure: asymmetric functional treatment of science |

Keep the Status column in sync with each workbook's Status line
(EMPTY → IN PROGRESS → COMPLETE → FILED).

## Theme Coverage Checklist (Nova's high-yield themes)

Not assignments — a map of what we hope the digs eventually surface. When a
dig's discovered topic hits one of these, check it off and note the workbook.

| ☐ | Theme | Primary subject | Covered by |
| --- | --- | --- | --- |
| ☐ | **CFA scoring and Grant's zero** (highest value — the pilot question) | Grant | |
| ☐ | Prediction as the ultimate standard | Grant | |
| ☐ | Trust preceding prediction | Grant/Ziggy | |
| ☐ | Possibility versus plausibility | both | |
| 🟡 | The jurisdiction of justification | Grant | `COMPOUND_SWEEP_03` (sweep-grade — bounded sub-dig still needed for promotion) |
| ✅ | Classical theism generating moral norms | Grant | `DIG_01` (Stage 1 complete — first checklist hit) |
| ☐ | Myth as compression | Ziggy | |
| ☐ | Offense-versus-defense scoring asymmetry | both | |
| ☐ | Institutional authority and preferred grounding standards | both | |

**Known thread leads so far:** nine in the SWEEP_00 leads table, plus from
X-CONTEXT notices: **"Grant and Positivism"** (~2026-06-29 — now pointed at by
**two independent bounded digs** (AUX_01, AUX_02): the strongest-signaled Grant
target on the board), "Hilbert spaces and language models" (~2026-07-02,
cross-model convergence), and "Impedance and attention analogy" (~2026-07-02,
convergence across frameworks). **Named-title leads from AUX_05's X-CONTEXT**
(actual chat titles — highest navigability yet): **"digg_03"** (~06-15, myth
compression + reported Grant objection — likely the Compression-vs-Transmission
checklist thread); **"delete_6"** (~06-30, trust and prediction — likely THE
Trust-vs-Prediction lead); **"digg_00"** (~06-06, chosen direction /
pragmatism / final ends — possible "final why" thread); **"digg_05"**
(~06-04, scientific and spiritual jurisdictions).

Start with **six to ten** threads where the central disagreement is clearest —
not with everything. After ≥3 packets exist, open one fresh **synthesis thread**
(the integration chamber) and run the cross-packet questions: which operators
recur across independent contexts; which appear only on offense; which are
actually Nova's language imposed on Grant; which survive counterexample search;
how Ziggy's own position has changed.
