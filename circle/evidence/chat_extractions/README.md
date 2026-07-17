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
| `DIG_02.md` | *(template consumed into COMPOUND_SWEEP_10)* | — |
| `DIG_COMPOUND_SWEEP_10_stochastic_diminishing_roles_noise_and_persuasion_frames.md` | ⚡ Compound sweep: "stochastic diminishing" → **Conversational Possibility-Space Contraction** (six narrowing types; non-monotonic); conversational functions vs identities; noise utility vs participation entitlement (**the Angles dispute — first bounded dig with substantial member-03 material, THIRD-PARTY-REPORTED ceiling**); concept vs implementation; persuasion vs understanding | ✅ **COMPLETE — candidate harvest, ZERO promotions (plow-through held, 9th consecutive)**; **first bounded Angles material (THIRD-PARTY-REPORTED NON-SITE)**; 4 durable families (Descriptive–Evaluative–Policy = strongest distinct result); the excavation's clearest live self-sealing failure + interpretive-capture discriminator; ten-step useful-noise test; *value and access are separate decisions*; seeds IT-061…072 (**12 trails — new single-dig record**; IT-072 = the falsifiability family's index) |
| `DIG_12.md` | *(template consumed into COMPOUND_SWEEP_11)* | — |
| `DIG_COMPOUND_SWEEP_11_consciousness_fundamentality_emergence_and_explanatory_stopping.md` | ⚡ Compound sweep: generative bracketing ("assume mind is fundamental" as sandbox — four legitimacy conditions; Bracketing-to-Privilege Drift named); reason vs cause + PSR version control; mechanism vs experience (three-gap split); lawful emergence vs "magic" → the ontological novelty challenge; explanatory-debt comparison + matter/consciousness symmetry; ⚠️ **opponent UNNAMED — "Grant Position Ledger" renamed Reported Opponent Position Ledger**; aux seed: Aquinas roleplay | ✅ **COMPLETE — candidate harvest, ZERO promotions (plow-through held, 10th consecutive)**; **the protocol's first full self-correction cycle** (defective Stage 3 → repair order → correction command → CORRECTED STAGE 4 with internal repair → final QC PASS); 8 confirmed A3 omissions restored; 6 durable dig-level families; **A3 case law 4th refinement**; QC overlays: dig-level families ≠ actor traits; brute psychophysical law legitimate with honest cost; ontological verdict: *the hard problem establishes incompleteness, not which completion*; seeds IT-073…083 (11 trails); opponent UNNAMED (Reported Opponent Position Ledger); Aquinas = aux seed |
| `DIG_13.md` | *(template consumed into COMPOUND_SWEEP_12)* | — |
| `DIG_COMPOUND_SWEEP_12_lying_justification_culpability_and_productive_disruption.md` | ⚡ ⭐ **MILESTONE: first substantial G-DIRECT Grant material** (screenshots) — the Gavin dispute (did he lie?): mental-state ladder (error → recklessness → truth-indifference → lying); four meanings of "basis"; contemporaneous vs post-hoc; population correlation vs individual accusation; **the credit problem** (occasion ≠ contribution ≠ credit ≠ access); aux seeds: religious discernment; resistance/awakening (self-sealing danger named) | ✅ **COMPLETE — ZERO promotions (plow-through held, 11th consecutive)**; closed through the **second full self-correction cycle** (repair order → correction → **registry-completion patch**, new case law); ⭐ **G-002 = first G-DIRECT Grant source; 3 packet-local seeds** (disciplined standards, not pathologies); Threshold-to-Character Escalation QUARANTINED; 12 confirmed A3s; **omission-derived requirements ≠ demonstrated actor behavior** (new archive-wide restriction); 7 dig-level families; Ziggy = Salvager–Synthesizer; seeds IT-084…092 |
| `DIG_14.md` | *(template consumed into COMPOUND_SWEEP_13)* | — |
| `DIG_COMPOUND_SWEEP_13_faith_uncertainty_evidence_and_action.md` | ⚡ ⭐ **Second G-DIRECT-bearing packet** (Grant's shared-AI screenshots) — can "faith" name acting under uncertainty, and does that pressure evidentialist nonbelief? The false Hume attribution caught (CO-CONSTRUCTED SYNTHESIS); the son-height/milk overbreadth test; the four-way separation (uncertainty ≠ commitment ≠ faith ≠ God); belief threshold ≠ action threshold; the raffle (observation vs report); the trilemma widened | ✅ **COMPLETE — ZERO promotions (plow-through held, 12th consecutive)**; closed through **TWO full self-correction cycles (the archive's third and fourth — first double-cycle dig) + a final targeted tier-ledger correction** (new closure pattern: targeted correction without full reissue); **5th tier case law** (A3 needs no explicit request) + **6th** (*neighboring operations ≠ the operation*); final ledger **10 A3 · 0 A2 · 8 possible A1**; **completed audit architecture ≠ demonstrated actor behavior** ("Profile-ready" struck); Grant's God-classification A0/UNKNOWN (*unknown facts are never omissions*); ⭐ **G-003 = second G-DIRECT source; 2 packet-local seeds** (Hume-attribution testing; extension stress testing); **authority laundering** named; Possibility Preservation = strongest named match (3rd instance); 7 families + aux led by the restored Practical–Ontological Bridge Audit; seeds IT-093…101; **workbook streamlined by operator order — full verbatim chain at commit 782f7ad** |
| `DIG_15.md` | *(template consumed into COMPOUND_SWEEP_15)* | — |
| `DIG_COMPOUND_SWEEP_15_argument_structure_frame_transfer_and_debate_gamesmanship.md` | ⚡ ⚠️ **G-REPORTED-only packet (DIRECT GRANT CORPUS = NONE** — the reported ceiling returns after three G-DIRECT digs) — straw-manning three-level ledger (structure ≠ responsibility ≠ culpability); the divine-command hypothetical four-way (only *illicit hypothetical-to-actual transfer* supports "frame hijacking" — name ruled too loaded → Hypothetical–Actual Commitment Transfer Audit); suffering four levels; behavioral tallying + motive firewall; **retained higher-order evidence from past reasoning** (the differential-equation analogy); Support-Token–Thesis Separation; AI Agency–Verification–Provenance; Trickster–Warrior tension (Z-DIRECT escalation admissions) | 🟡 IN PROGRESS — Stages 1–2 ✅ reviewed; forecast **8/8 — and for the first time in three digs the extractor did NOT drop the central family**; 25 moves → 8 families + 2 cross-cutting methods; renames (Conditional Commitment Boundary); **Unconscious-Motive Reopening QUARANTINED** (conscious denial → motive relocated → unfalsifiable); the co-constructed-label authority loop named; **the escalation symmetry test registered** (how much "mental chess" is co-produced?); ✅ **COMPLETE — ZERO promotions (plow-through held, 14th consecutive)**; closed through **TWO full self-correction cycles (the archive's seventh and eighth — THIRD consecutive double-cycle dig)**; ⚠️ **G-REPORTED-only: 0 Grant operators, hard boundary held**; signature yields: **the escalation self-contribution A3** (his provocation restored to the "mental chess" causal account); **the all-Nova-side A2 ledger (4) + refined A2 definition** (no conscious-refusal proof required); extraction-products-as-evidence violated the dig after it was outlawed; **inverse-operation mapping recurred at Stage 4 (3rd dig running — four corrections)**; *retained higher-order evidence from past reasoning* (IT-112); Support-Token–Thesis Separation formalized (IT-113); final ledger **8 families · 7 profile-ready claims (queue-filed) · 4 A2 · 6 A3 · 19 A1**; seeds IT-110…113; ⚠️ standing owed output: the corrected Stage-3 reissue (produced, governed Stage 4, never pasted); raw captures at commits `ec8c638` + prior |
| `DIG_16.md` | *(template consumed into COMPOUND_SWEEP_16)* | — |
| `DIG_COMPOUND_SWEEP_16_formalization_semantics_frame_protection_and_moral_authority.md` | ⚡ ⭐ **MILESTONE: first packet with direct screenshot material beyond Grant** (Tom, Sorta, Kee, Tapioca — new `T-/S-/K-/TP-DIRECT-SCREENSHOT, PARTIAL` labels) — the divine-command formalization dispute (five-layer audit: proposition individuation → validity → soundness → applicability; the counterpossible problem); "meaning is irrelevant" scope-controlled; protection vs defense w/ reachable loss conditions; frame control six-way; suffering/brute-fact ledger; Sorta's agency objection; Tom's compatibilism + anti-realist condemnation; Ziggy's compressed cognition (traceability protocol) | 🟡 IN PROGRESS — Stage 1 ✅ reviewed; **date/source-boundary leak corrected** (project timing never bounded evidence; date UNKNOWN); internal critique needs no target permission (critic bears the entailment burden); no Grant-utilitarian profile; anti-realism ≠ inability to condemn (Tapioca strong); ⭐ Grant's **premise-rejection allowance** filed as counterevidence; 8-family forecast + 37 pressure questions registered; **10 profile seeds incl. the archive's first Tom seeds**; Stage-2 output pasted, review pending; Stages 3–4 pending |
| `DIG_17.md` | *(fresh slot)* | EMPTY |
| `DIG_19.md` | *(fresh slot — minted 2026-07-17 from "DIG_17 copy" files; DIG_18 already consumed)* | EMPTY |
| `DIG_20.md` | *(fresh slot)* | EMPTY |
| `DIG_21.md` | *(fresh slot)* | EMPTY |
| `DIG_22.md` | *(fresh slot)* | EMPTY |
| `DIG_18.md` | *(template consumed into COMPOUND_SWEEP_14)* | — |
| `DIG_COMPOUND_SWEEP_14_protection_frames_meaning_source_and_moral_authority.md` | ⚡ ⭐ **Third G-DIRECT-bearing packet** (screenshots) — protection vs defense (loss conditions); many "A+" frames (coherence ≠ truth); PCB crosstalk (local coherence vs global compatibility); meaning recovery vs frozen words; mechanism vs source (ayahuasca, unconscious-as-interface); is/ought bridges; internal vs external critique of God; God as archetype vs ground | ✅ **COMPLETE — ZERO promotions (plow-through held, 13th consecutive)**; closed through **TWO full self-correction cycles (the archive's fifth and sixth — second consecutive double-cycle dig)**; new case law: **extraction products are never actor evidence** + **inverse-operation mapping named as a Stage-4 error class** (jurisdiction auditing ≠ performing UEJ — COUNTER-OPERATION); the originating **Protection–Defense and Loss-Condition Audit dropped THREE times, restored each time**; final ledger **8 families · 9 A3 · 0 A2 · 15 A1**; ⭐ **G-004 = third G-DIRECT source; 3 packet-local seeds** (Dichotomy Repair; Conditional Concession; ⭐ positive AI-Authorship Trust Calibration — the first fully positive Ziggy–Grant loop); Grant = local Cognitive-Mechanism Reframing only (naturalizing operator QUARANTINED); extractor "profile-ready" tier filed as queue candidates (3 named matches incl. Possibility Preservation 4th instance + 6 new candidates + the Protection-vs-Defense seed); tier walls: Frame Mapper role / balance value / Christian commitment existential (IT-109); seeds IT-102…109; **X-CONTEXT leads:** E-field/B-field–culture–meaning; Grant's DCT frame; "petty tyrant" (Castaneda); modal-logic-as-reductio; a protection-vs-defense precursor thread |
| `DIG_COMPOUND_SWEEP_03_foundations_justification_and_jurisdiction.md` | ⚡ Compound sweep: Münchhausen trilemma → framework-relative justification → single-value underdetermination → **jurisdiction of justification** (checklist theme #4 — Z-06's home trench) | ✅ **COMPLETE — candidate harvest, ZERO promotions (plow-through held again)**; 2 retain-RED candidates queued (Framework Transplant, Constraint-Exhaustion Stress Test); Jurisdiction Challenge = CO-002's corrective test; seeds IT-019 |
| `DIG_03.md` | *(template consumed into COMPOUND_SWEEP_09)* | — |
| `DIG_COMPOUND_SWEEP_09_plausibility_agnostic_priors_and_miracle_claims.md` | ⚡ Compound sweep, **SPLIT at Stage 1** — primary: the Grant/Mary plausibility dispute (ranking → "agnostic agent" → common ground → rationality requirement; C1/C2/C3 virginity claims split; five-modality ladder; **Agnostic-Proxy Construction** provisionally named); auxiliary seed: attention/intention/boredom (separate future dig, field-desk identity `DIG_AUX_attention_intention_awareness_and_boredom`) | ✅ **COMPLETE — candidate harvest, ZERO promotions (plow-through held, 8th consecutive)**; SPLIT dig (aux phenomenology packet closed as seed, no promotions); 3 durable families + 1 provisional (Normative-Promotion Audit = strongest new candidate, co-constructed); **first A1→A3 upgrade on record**; Reciprocal-Burden Audit = *attempted, incomplete*; category-repair/evidential-escape discriminator + ten-step symmetrical comparison + P1–P4 Grant reconstruction filed as instruments; seeds IT-052…060 (**9 trails — new single-dig record**); Grant: G-REPORTED NON-SITE |
| `DIG_04.md` | *(template consumed into COMPOUND_SWEEP_08)* | — |
| `DIG_COMPOUND_SWEEP_08_belief_justification_action_and_belief_rescue.md` | ⚡ Compound sweep: subjective experience as evidence (E1–E4 split); knowledge vs action thresholds; **what defeating a reason actually defeats** (only argument-level defeat is automatic); **belief rescue vs immunization** — Ziggy's admitted rescue impulse is the hottest prey; ⚠️ opens on Nova's reconstruction of an UNAVAILABLE earlier conversation | ✅ **COMPLETE — candidate harvest, ZERO promotions (plow-through held, 7th consecutive)**; all 4 outputs pasted (Stage-4 landed after the review — audit trail noted); 4 durable families; **Belief Rescue ≠ Possibility Preservation**; repair/immunization discriminator (*may the replacement reasons fail?*); **first confirmed relationship-level Reconstruction Bypass**; preservation bias = deepest structural finding; seeds IT-045…051 (7 trails); Grant: G-REPORTED/NOVA-RECONSTRUCTED NON-SITE |
| `DIG_05.md` | *(template consumed into DIG_AUX_07)* | — |
| `DIG_AUX_07_axioms_prediction_logic_and_epistemic_bedrock.md` | Auxiliary/idea-trail dig: can faith function axiomatically, and does predictive power disqualify it? Grant's reported claim + Ziggy's bedrock counter + the logic-vs-prediction dependency dispute; ⭐ **the pilot's "prediction as ultimate standard" theme in its most direct form yet** (still reported-only) | ✅ **COMPLETE — ZERO promotions (aux ceiling)**; 4 durable families (Bedrock Extraction = strongest Ziggy candidate, danger clause attached); **reciprocal bedrock rule** + 8-step comparison procedure + G1–G6 ladder + six-step religious test case filed as instruments; A2 case law (3rd tier refinement); polarity reversal 6th consecutive dig; Absent-Opponent Reconstruction → RELATIONSHIP_MAP (highest attribution risk on record); seeds IT-039…044 (6 trails); Grant: G-REPORTED/NOVA-RECONSTRUCTED NON-SITE |
| `DIG_06.md` | *(template consumed into COMPOUND_SWEEP_07)* | — |
| `DIG_COMPOUND_SWEEP_07_entropy_semantic_compression_materialism_and_narrative_transmission.md` | ⚡ Compound sweep: Shannon entropy vs semantic value; myth-as-compression (encoding/decoding); story vs cookbook; materialism / explanatory levels; religion as experiential-pattern transmission; prediction as mechanism not sovereign — sequel to AUX_06 + SW05 masters branch | ✅ **COMPLETE — candidate harvest, ZERO promotions (plow-through held, 6th consecutive)**; 4 durable families (Monopoly-Promotion/Telos ×2; Shannon–Semantic Layer; Substrate–Explanatory-Level; Narrative-Transmission Fit) + 2 quarantined research frameworks; **first A2 against a favored theory** (decoder-ring validation); formal-authority residue → IT-038; transmission ≠ content quality; seeds IT-032…038 (7 trails — largest single-dig trail harvest); Grant: G-REPORTED/G-ANTICIPATED NON-SITE |
| `DIG_07.md` | *(template consumed into COMPOUND_SWEEP_06)* | — |
| `DIG_COMPOUND_SWEEP_06_belief_justification_observer_frames_and_scientific_jurisdiction.md` *(renamed at close per field desk from the DIG_07-slot working file)* | ⚡ Compound sweep, 3 sites: belief/justification/warrant/truth; observer facts vs world facts (teapot — anti-relativist correction); scientific jurisdiction over spiritual claim types ("taking the theist idea into their frame to die" got its two-sided test) — G1–G4 Grant theses kept apart | ✅ **COMPLETE — candidate harvest, ZERO promotions (plow-through held, 5th consecutive)**; 3 HIGH candidates queued (Adjudication-Frame Audit; Observer-State/Shared-World Audit; Claim-Type/Method-Fit Audit + domain-immunity safeguard); 14 moves → 5 families; polarity-reversal seed reinforced (4th sweep); seeds IT-027…031; balance point filed permanent (*authority without sovereignty; evidence without immunity*); Grant: REPORTED/RECONSTRUCTED NON-SITE; sub-digs A/B/C queued (A = profile prize, C = Museum prize) |
| `DIG_08.md` | *(template consumed into DIG_AUX_06)* | — |
| `DIG_AUX_06_myth_compression_interpretive_variance_and_projection.md` | **Micro-auxiliary**: does interpretive disagreement undermine myth-as-cultural-compression? One Ziggy report of Grant + one Z-DIRECT reaction + one substantial Nova reconstruction — likely first bounded site for the **Myth-as-Compression checklist theme**; ⭐ central finding: **claim-strength drift** (disagreement ≠ proof of no compression, but principal-explanation claim untouched); field-desk id "AUX_10" noted (off-by-one) | ✅ **COMPLETE — micro-dig, ZERO promotions (Ziggy NONE · Grant NONE · Nova thread-level)**; deepest finding: claim-strength ladder (*possible ≠ reliable ≠ important ≠ principal*); Falsifiability Debt + baseline problem filed theory-level; seeds IT-026; first bounded site for Myth-as-Compression theme; ⚠️ Stage-2 review tail still pending re-relay |
| `DIG_09.md` | *(template consumed into COMPOUND_SWEEP_05)* | — |
| `DIG_COMPOUND_SWEEP_05_prediction_trust_law_and_master_frames.md` | ⚡ Compound sweep: can prediction, truth, suffering, law, religion, or consciousness serve as a **master frame**? Curt Jimungal video entry; presup/method dispute; Grant G-REPORTED only; extractor self-flagged heavy NOVA-INTERPRETATION load ("prediction is a servant," "optimization function") — direct sequel to SWEEP_04's masters neighborhood | ✅ **COMPLETE — candidate harvest, ZERO promotions (plow-through held, 4th consecutive)**; 3 HIGH candidates queued (Monopoly-Promotion Audit — strongest; Claimed-Source/Access; Operative-Rigidity); 22 moves → 5 families; **Detector–Pathology Polarity Reversal = candidate Failure-Atlas seed (3rd sweep running)**; seeds IT-023/024/025; Grant: REPORTED-ONLY NON-SITE; sub-digs A–D queued (C = profile prize, B = most novel) |
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
| ☑ | Prediction as the ultimate standard | Grant | **AUX_07** (most direct site — G1–G6 ladder; reported-only) + SW05/SW07 masters branches; full coverage needs a G-DIRECT thread — "Trust vs Prediction" (4 pointers) is the promotion path |
| ☐ | Trust preceding prediction | Grant/Ziggy | |
| ☐ | Possibility versus plausibility | both | |
| 🟡 | The jurisdiction of justification | Grant | `COMPOUND_SWEEP_03` (sweep-grade — bounded sub-dig still needed for promotion) |
| ✅ | Classical theism generating moral norms | Grant | `DIG_01` (Stage 1 complete — first checklist hit) |
| ☑ | Myth as compression | Ziggy | **AUX_06** (micro, reported-only — claim-strength ladder + falsifiability debt; full coverage needs the "digg_03" thread) |
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
Trust-vs-Prediction lead; **2nd pointer from SWEEP_05**); **"digg_00"**
(~06-06, chosen direction / pragmatism / final ends — possible "final why"
thread; **2nd pointer from SWEEP_05**, adds: prediction, pragmatism, truth,
and the final governing value); **"digg_05"** (~06-04, scientific and
spiritual jurisdictions). **From SWEEP_05's X-CONTEXT (new titles):**
**"Category error in systems"** (~06-15, judging meaning-oriented systems by
physical-science standards; **2nd pointer at SW05 Stage 4**); **"delete_4"**
(~07-01, metaphysics and scientific assumptions); **"delete_5"** (~06-30,
methodological naturalism, framework asymmetry, offense/defense scoring —
likely the checklist's Offense-vs-Defense thread; SW05 Stage 4 repeats the
topic under the title **"Methodological naturalism and framework
asymmetry"**). **"Trust vs Prediction"** (~06-30, whether trust precedes or
overrides prediction — SW05 Stage 4; same date and topic as "delete_6":
likely the same thread under its real title — IT-023's target dig; **4th
pointer at AUX_07 — unambiguously the priority target**). **From
SWEEP_07's X-CONTEXT:** topic-lead *mythology, Christianity, and
Castaneda* (no title/date recovered). **From AUX_07's X-CONTEXT (new
titles):** **"delete_14"** (~06-08, logic foundational / prediction
emergent — AUX_07's own question in an earlier thread; natural companion
dig); **"MASTER BRANCH"** (~07-15, information theory / prediction /
axiomatic foundations — ⚠️ recent thread, possible ambient-memory
contamination risk, preflight carefully). **From SWEEP_08's X-CONTEXT
(new titles):** **"Final Why"** (~06-20, commitment / ultimate values /
action after justificatory chains end — **charter candidate #2's home
thread, long sought**); **"Religion as Technology"** (~06-20 — SW07's
June-20 topic lead now titled); **"How Do You Know That"** (~06-28,
source demands / provenance-disqualification — IT-046's genesis/warrant
question in the wild). "Trust vs Prediction" now at **5 pointers** (**6th at SW09** — via
"delete_6"). **From SWEEP_09's X-CONTEXT (new titles):** **"delete_18"**
(~05-29, value adoption / rational rejection / smuggled normative frames
— the earliest-dated lead yet; kin to SW09's Agnostic-Proxy question);
**"delete_13"** (~06-11, provisional truth / "true as far as we know" —
kin to IT-015's underdetermination trail). **From SWEEP_10's X-CONTEXT
(topic leads):** ⭐ *listening, asymmetrical exchange, and "vampiric
scaling"* (~June 2026 — **charter candidate #9's home thread, long
sought**); *Grant, prediction, justification, local/global frames*
(~May–June); *value rejection and justification demands* (~May).
**From SWEEP_11's X-CONTEXT (new titles):** **"delete_19"** (~05-27,
structure/mechanism/voltage/consciousness — SW11's own question,
earlier thread); **"Castaneda"** (~06-04 — SW07's Castaneda topic lead
now titled); ⭐ **"delete_15"** (~06-07, *a question for Grant about
beliefs that do not need justification* — direct pilot-relevant lead,
kin to the AUX_07/SW08 foundations work); **"B-Storm_02: Assembly vs
High-Level Languages"** (~05-30, prediction/justification/metaphysical
frameworks). **From SWEEP_12's X-CONTEXT:** ⭐ **"B-STORM_04_Castenada"**
(~05-13, inorganic beings / second attention — **the earliest-dated
titled lead in the excavation**); "delete_6" **7th pointer**;
"B-Storm_02" 2nd pointer (Grant's justification/prediction reliance);
"delete_18" 2nd pointer (Grant's value framework); "Castaneda" 2nd
pointer. **From SWEEP_13's X-CONTEXT (new titles):** **"Markov Chains
and Logic"** (~06-03, local vs global reference frames / justification —
kin to SW06's observer work); **"Delayed Choice Quantum Eraser"**
(~05-20, established frameworks and available paths); **"MISC_01"**
(~05-21, "kicking the can down the road" / responsibility for reality —
kin to the stopping-rule family). "Trust vs Prediction" **8th pointer**;
"Assembly vs High-Level Languages" 3rd pointer (full title confirmed).

Start with **six to ten** threads where the central disagreement is clearest —
not with everything. After ≥3 packets exist, open one fresh **synthesis thread**
(the integration chamber) and run the cross-packet questions: which operators
recur across independent contexts; which appear only on offense; which are
actually Nova's language imposed on Grant; which survive counterexample search;
how Ziggy's own position has changed.
