# ⛏️ PanHandlers Cognitive Archaeology Protocol v0.2 — ACTIVE

> **The dig instrument, second edition.** v0.1 (Nova, 2026-07-16) survived contact
> with reality for exactly one deployment: pasted whole into an old chat, it was
> received as *an artifact submitted for review*, not *an instruction to execute* —
> the extractor opened with "This is already very strong, but…" and sharpened the
> shovel instead of digging. Nova's diagnosis: **a mode-control failure, not a
> reasoning failure** — no execution lock, no immediate stage target, candidate
> operator names inviting methodological reflection, and an extractor trained by
> this very project to improve frameworks on sight.
>
> v0.2 adopts her improvements. v0.1 is preserved as provenance in
> [`CHAT_EXTRACTION_PROTOCOL_v0.1.md`](CHAT_EXTRACTION_PROTOCOL_v0.1.md).

**Output destination:** `evidence/chat_extractions/` (one packet per chat, all four stage outputs)
**Promotion path:** packet → review → `SOURCE_INDEX.md` entries → labeled profile claims
**Filing-side rules:** see **Archive Integration** section at the end (not part of any paste)

---

## The Mode-Control Rule

**Never paste the whole protocol and expect an extraction.** Run digs as staged
execution commands, sent **one at a time**, each opening with the execution
wrapper. Optionally paste the protocol first *for reference only* — but the work
happens through the stage commands.

**Execution wrapper — mandatory, verbatim, at the top of every stage command:**

> This is an execution command, not a request for protocol review. Do not
> critique, improve, summarize, or discuss the protocol. Execute the requested
> stage now using the complete conversation above as the source corpus. Mark
> missing evidence as UNKNOWN. Do not ask questions. Return only the requested
> extraction output.

Save each stage's output before sending the next stage.

## What Changed From v0.1 (Nova's field-test improvements)

1. Execution split into **four saved stages** (was: fourteen passes in one prompt).
2. **Museum-blind extraction** (Stage 2) runs *before* candidate operator names
   are shown (Stage 4) — the candidate list in v0.1's Pass E was a priming risk.
3. **Availability test** for claimed omissions — an unused move only counts if
   there is evidence the actor plausibly had it available.
4. Explicit separation of **cognitive operators, epistemic brakes, rhetorical
   tactics, role behavior, relationship dynamics, and protocol-induced behavior**.
5. New per-move fields: **Functional Type** and **Voluntariness**.
6. **Stronger promotion thresholds** for profile-ready claims (see Archive Integration).
7. **Recoverable chronological source anchors** required (speaker + unique opening
   phrase or recoverable wording + approximate location).
8. Dispute records gain **Surface Question / Underlying Question / Jurisdiction
   Conflict / Mutation Point** fields.
9. **Extraction self-audit** (Stage 4) — the instrument reports its own likely errors.
10. **Relationship-level operator ledger** — interaction loops owned by a pair,
    not a person (files into `RELATIONSHIP_MAP.md`).

v0.1's source-discipline labels (G-DIRECT / G-REPORTED / Z-DIRECT /
NOVA-INTERPRETATION / CO-CONSTRUCTED / UNCLEAR) and final constraints carry
forward unchanged.

---

## STAGE 1 — Source and Positions

### ✂️ PASTE STAGE 1 ✂️

# PANHANDLERS DIG EXECUTION — STAGE 1

This is an execution command, not a request for protocol review.

Do not critique, improve, rewrite, summarize, or discuss the extraction protocol.

Use the complete conversation above this message as the source corpus. Do not rely on generalized memory from other chats.

Perform **Stage 1 only**:

1. Source and attribution audit
2. Conversation map
3. Dispute-origin analysis
4. Grant position ledger
5. Ziggy position ledger

For each material claim, distinguish:

* **G-DIRECT** — Grant's own words appear in this chat.
* **G-REPORTED** — Ziggy reports or paraphrases something Grant said elsewhere.
* **Z-DIRECT** — Ziggy states his own position directly.
* **NOVA-INTERPRETATION** — the assistant interprets Grant, Ziggy, or the dispute.
* **CO-CONSTRUCTED** — Ziggy and the assistant develop the idea together.
* **UNCLEAR** — attribution cannot be confidently determined.

Do not silently convert G-REPORTED into G-DIRECT. Do not attribute an assistant-generated phrase to Grant or Ziggy unless that person explicitly adopted it.

For every major dispute include:

* Surface Question
* Underlying Question
* Jurisdiction Conflict
* Mutation Point
* Source Anchor

A source anchor must contain the speaker, a unique opening phrase or recoverable wording, and its approximate location in the conversation.

Do not extract or name Museum operators yet.

Do not ask me questions. Mark missing evidence `UNKNOWN`.

Return only:

```text
PANHANDLERS_CHAT_EXTRACTION — STAGE 1

Chat title:
Approximate date:
Primary topic:
Evidence balance:

1. Source Audit
2. Conversation Map
3. Dispute Mutations
4. Grant Position Ledger
5. Ziggy Position Ledger
6. Stage-1 Uncertainties
```

Begin the extraction now.

### ✂️ END STAGE 1 ✂️

---

## STAGE 2 — Blind Cognitive Architecture

### ✂️ PASTE STAGE 2 ✂️

# PANHANDLERS DIG EXECUTION — STAGE 2

Continue using the complete conversation and the completed Stage-1 extraction as the source corpus.

This is an execution command. Do not critique or improve the protocol.

Perform Museum-blind cognitive extraction. Do not use or mention existing Museum or Circle operator names.

Identify:

1. repeated reasoning moves;
2. consequential one-time moves;
3. operator sequences;
4. offense/defense differences;
5. role-induced behavior;
6. relationship-level interaction loops.

For each proposed move provide:

* Provisional neutral name
* Actor
* Definition
* Trigger
* Operation
* Output
* Productive function
* Failure mode
* Functional Type:
  * TRANSFORMATIVE
  * EXPLORATORY
  * EVALUATIVE
  * REGULATORY / INHIBITORY
  * RHETORICAL
  * PROTOCOL-INDUCED
  * UNKNOWN
* Voluntariness:
  * VOLUNTARY
  * PROMPT-INDUCED
  * ROLE-INDUCED
  * UNCLEAR
* Source Anchor
* Confidence
* Alternative explanation

Do not convert a substantive belief, rhetorical tactic, isolated reaction, or relationship dynamic into an individual cognitive operator without explicitly defending that classification.

Do not ask me questions. Mark missing evidence `UNKNOWN`.

Return only:

```text
PANHANDLERS_CHAT_EXTRACTION — STAGE 2

1. Museum-Blind Reasoning Moves
2. Operator Sequences
3. Offense/Defense Analysis
4. Role-Induced Behaviors
5. Relationship-Level Loops
6. Classification Uncertainties
```

Begin Stage 2 now.

### ✂️ END STAGE 2 ✂️

---

## STAGE 3 — Omissions, Counterevidence, Alternative Readings

### ✂️ PASTE STAGE 3 ✂️

# PANHANDLERS DIG EXECUTION — STAGE 3

This is an execution command, not a request for protocol review.

Do not critique, improve, rewrite, summarize, or discuss the extraction protocol.

Continue using the complete conversation plus the completed Stage-1 and Stage-2 extractions as the source corpus.

Perform **Stage 3 only**:

1. **Omission analysis with availability test.** Identify important moves that were available but absent — for example: reconstructing the opposing framework before scoring it; applying the same burden to one's own framework; distinguishing `unknown` from `zero`; temporarily granting a possibility; asking what function a framework serves; clarifying the jurisdiction of a standard; conceding a limited point; testing a conclusion under reversed roles.

   For each claimed omission provide:
   * why the move was relevant at a specific point (with source anchor);
   * **Availability evidence** — grounds for believing the actor plausibly had the move available: they used it elsewhere in this conversation, it was explicitly offered to them and declined, or it is standard practice they demonstrably know. If no availability evidence exists, mark availability `UNKNOWN` and do not treat the omission as informative;
   * whether the absence changed the outcome;
   * whether the absence appears stable or situational.

   Do not treat every unused move as a defect.

2. **Counterevidence search.** For every major Stage-1/Stage-2 characterization, search this conversation for evidence against it — for example: a preserved low-probability possibility; explanation valued independently of prediction; an attractive possibility rejected; strong evidential pruning demanded; a charitable reconstruction; an expected move not deployed. Report null results explicitly ("searched, none found").

3. **Alternative readings.** For each major characterization, state the strongest alternative explanation (substantive belief rather than operator; rhetorical tactic; role effect; protocol-induced behavior; one-off reaction) and what evidence in this conversation discriminates between the readings — or mark `UNKNOWN` if nothing here can.

Do not ask me questions. Mark missing evidence `UNKNOWN`.

Return only:

```text
PANHANDLERS_CHAT_EXTRACTION — STAGE 3

1. Omissions With Availability Evidence
2. Omissions With UNKNOWN Availability
3. Counterevidence Findings
4. Alternative Readings
5. Characterizations That Survived
6. Characterizations That Weakened
```

Begin Stage 3 now.

### ✂️ END STAGE 3 ✂️

---

## STAGE 4 — Named Mapping and Verdicts

### ✂️ PASTE STAGE 4 ✂️

# PANHANDLERS DIG EXECUTION — STAGE 4

This is an execution command, not a request for protocol review.

Do not critique, improve, rewrite, summarize, or discuss the extraction protocol.

Continue using the complete conversation plus the completed Stage-1, Stage-2, and Stage-3 extractions as the source corpus.

Only now, map the Stage-2 blind findings onto the named candidate registry below. These are candidates, not predetermined conclusions — a forced match is worse than no match.

Candidate registry (definitions carried inline; you cannot see the source archive):

* **Prediction Sovereignty** — predictive success functions as the highest or final epistemic authority, through which all other forms of success must justify themselves.
* **Universalized Evaluative Jurisdiction** — a standard developed for one class of inquiry is extended into domains where its authority has not been established.
* **Generative Admission Restriction** — certain sources (revelation, tradition, narrative coherence, metaphysical intuition, first-person experience, symbolic compression) are denied authority to generate serious candidate hypotheses before evaluation begins.
* **Unmeasured-to-Zero Conversion** — failure to demonstrate success under the selected instrument is converted into a score of zero rather than unknown / untested / outside jurisdiction.
* **Possibility Compression** — possibilities below a plausibility threshold are treated as functionally irrelevant.
* **Baseline Exemption** — the preferred standard is treated as neutral baseline rather than a framework with its own assumptions, producing asymmetric burden.
* **Reconstruction Bypass** — evaluation begins before the framework has been reconstructed according to its own aims, ontology, and success conditions.
* **Contest-to-Defeat Compression** — a raised objection or unresolved challenge is treated as stronger evidence of defeat than the dialectical situation warrants.
* **Symmetry Testing of Standards** — forcing the evaluating standard to file the same paperwork as the evaluated framework.
* **Contested ≠ Defeated** — explicitly holding an objection open as unresolved rather than decisive.
* **Possibility Preservation** — deliberately keeping low-plausibility possibilities on the map during exploratory inquiry.
* **Cross-Disciplinary Swooping** — importing a structure or distinction from a distant discipline to reframe the live dispute.

For each Stage-2 move give a mapping verdict:

* **MATCHES <name>** — state what matches and what does not;
* **EXTENDS <name>** — a variant; describe the delta;
* **NEW** — no adequate match; keep the provisional neutral name;

and state whether the mapping survives that move's Stage-3 alternative reading.

Then produce final verdicts:

**PROFILE-READY CLAIMS** — only claims meeting ALL of:
* recoverable source anchor;
* survived the Stage-3 counterevidence search and alternative-reading check;
* classification defended (not better explained as rhetoric, role behavior, or protocol-induced behavior);
* confidence stated.

For each include: claim; subject; evidence classification; confidence; source anchor; review condition.

**QUARANTINED CLAIMS** — interesting interpretations below threshold, each with the additional evidence that would promote it.

**EXTRACTION SELF-AUDIT** — where this extraction itself may have erred: priming risk from the candidate registry above; over-pattern-matching; asymmetric charity between participants; places where UNCLEAR was converted into a definite label; anything rushed.

Do not ask me questions. Mark missing evidence `UNKNOWN`.

Return only:

```text
PANHANDLERS_CHAT_EXTRACTION — STAGE 4

1. Blind-to-Named Mapping
2. New Operator Candidates
3. Profile-Ready Claims
4. Quarantined Claims
5. Extraction Self-Audit
```

Begin Stage 4 now.

### ✂️ END STAGE 4 ✂️

---

# Archive Integration (filing-side rules — never pasted)

## Assembling the packet

One packet file per source chat in `evidence/chat_extractions/`
(`<subject-or-topic>_<slug>_<YYYY-MM>.md`, dated by the source chat). Header:
chat title, approximate date, participants, extractor model, protocol version
(v0.2), dig operator. Body: all four stage outputs, in order, unedited.

## Label mapping at promotion time

| Extraction label | Archive label (`PROFILE_SCHEMA.md` §1) | Notes |
| --- | --- | --- |
| G-DIRECT + DIRECT | `DIRECT` (about Grant) | the chat itself is the transcript |
| G-REPORTED | at most `INFERRED` (about Grant) — but `DIRECT` about *Ziggy's report* | the double-bookkeeping that prevents retrospective legend |
| Z-DIRECT + DIRECT | `DIRECT` (about Ziggy) | |
| NOVA-INTERPRETATION | `INFERRED`, observer: Nova | Nova is an attributed observer like any other |
| CO-CONSTRUCTED | `INFERRED`, observers: both | never attributable to either alone |
| STRONG INFERENCE | `INFERRED` (candidate `REPEATED` once seen in ≥2 packets) | cross-chat recurrence earns promotion |
| TENTATIVE INFERENCE | `INFERRED` — or stay QUARANTINED | when in doubt, quarantine |
| CONTESTED / REVISED | `CONTESTED` / position state `REVISED` | |
| UNCLEAR / UNKNOWN | `UNKNOWN` | |

## Promotion thresholds (strengthened in v0.2)

1. A packet is promotable only when **all four stages** are complete and saved.
2. Only Stage-4 **PROFILE-READY CLAIMS** may enter profiles; Stage-1/2 material
   alone is never profile-grade.
3. Operator attributions enter a member's `OPERATOR_MAP.md` **with Functional
   Type and Voluntariness recorded**. `PROTOCOL-INDUCED` or `PROMPT-INDUCED`
   evidence cannot support attributing an operator to the *person* — it
   describes the situation, not the architecture.
4. `RHETORICAL` moves and role-induced behavior file under Debate Behavior
   (schema §H), not as cognitive operators.
5. Relationship-level loops file into `RELATIONSHIP_MAP.md`'s ledger, owned by
   the pair, not either member.
6. Cross-chat recurrence still governs the ladder: one packet → candidate;
   ≥2 independent packets → `REPEATED` / lexicon 🟡 PROPOSED; counterexample
   search performed across packets → 🟢 GREEN eligibility.
7. A **blind rediscovery** (Stage 2 finds a move that Stage 4 maps onto an
   existing CO/OP name) is stronger evidence than any primed match — flag these
   explicitly when filing; they also feed the Nyquist Museum's promotion paths.

## Version history

| Version | Date | Change | By |
| --- | --- | --- | --- |
| 0.1 | 2026-07-16 | Initial protocol; superseded same day (see `CHAT_EXTRACTION_PROTOCOL_v0.1.md`) | Nova / P.H. Claude |
| 0.2 | 2026-07-16 | Field-test rebuild: execution wrapper, four saved stages, Museum-blind Stage 2, availability test, Functional Type + Voluntariness, dispute-mutation fields, self-audit, relationship ledger, strengthened promotion thresholds | Nova (design) / P.H. Claude (filing) |
