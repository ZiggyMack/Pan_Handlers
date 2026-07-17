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
| `DIG_AUX_04_bell_theorem_modal_openings_2026-07.md` | Bell's theorem as modal opening (conjunction logic; exhaustiveness challenge; proof/admissibility) — strongest Ziggy site yet; technical-risk HIGH | STAGE 1 COMPLETE (output paste pending) — Stage 2 authorized |
| `DIG_AUX_05.md` | | EMPTY (staged for the mining walk) |
| `DIG_00.md` | *(reserved: CFA-zero — preflight required)* | EMPTY |
| `DIG_01.md` | | EMPTY |
| `DIG_02.md` | | EMPTY |
| `DIG_03.md` | | EMPTY |
| `DIG_04.md` | | EMPTY |
| `DIG_05.md` | | EMPTY |
| `DIG_06.md` | | EMPTY |
| `DIG_07.md` | | EMPTY |
| `DIG_08.md` | | EMPTY |
| `DIG_09.md` | | EMPTY |
| `DIG_10.md` | | EMPTY |
| `DIG_11.md` | | EMPTY |

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
| ☐ | The jurisdiction of justification | Grant | |
| ☐ | Classical theism generating moral norms | Grant | |
| ☐ | Myth as compression | Ziggy | |
| ☐ | Offense-versus-defense scoring asymmetry | both | |
| ☐ | Institutional authority and preferred grounding standards | both | |

**Known thread leads so far:** nine in the SWEEP_00 leads table, plus from
X-CONTEXT notices: **"Grant and Positivism"** (~2026-06-29 — now pointed at by
**two independent bounded digs** (AUX_01, AUX_02): the strongest-signaled Grant
target on the board), "Hilbert spaces and language models" (~2026-07-02,
cross-model convergence), and "Impedance and attention analogy" (~2026-07-02,
convergence across frameworks).

Start with **six to ten** threads where the central disagreement is clearest —
not with everything. After ≥3 packets exist, open one fresh **synthesis thread**
(the integration chamber) and run the cross-packet questions: which operators
recur across independent contexts; which appear only on offense; which are
actually Nova's language imposed on Grant; which survive counterexample search;
how Ziggy's own position has changed.
