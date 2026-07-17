# ⛏️ PanHandlers Cognitive Archaeology Protocol v0.2.2 — ACTIVE · DESIGN FROZEN

> 🧊 **Design freeze (Nova, 2026-07-17):** v0.2.2 approved; no further protocol
> revision until the repaired Dig 00 completes. "We now need evidence more than
> another instrument revision" — further refinement before the first bounded
> excavation would probably become its own avoidance operator.
>
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
3. **Tiered availability test** for claimed omissions (v0.2.1) — A3 Demonstrated /
   A2 Explicit / A1 Contextual / A0 Unknown; only A3/A2 yields a CONFIRMED
   informative omission, A1 yields POSSIBLE, A0 is non-informative. Sensitivity
   without manufactured negative space.
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
11. **Hard source boundary in every stage** (v0.2.2) — inside a Project chat,
    "the conversation above" can include injected Project Conversation Content
    from *other* chats; the Dig 00 field test excavated the entire archaeological
    park instead of the first marked trench. Every stage now excludes
    project-injected content, other-chat summaries, memories, uploads, and
    system context; Stage 1 returns a `Source-boundary confirmation`. A
    contaminated result is preserved as a corpus sweep (orientation only), never
    as a dig — see the Scope Repair appendix.

v0.1's source-discipline labels (G-DIRECT / G-REPORTED / Z-DIRECT /
NOVA-INTERPRETATION / CO-CONSTRUCTED / UNCLEAR) and final constraints carry
forward unchanged.

---

## STAGE 1 — Source and Positions

Copy everything inside the fence and send it as one message:

````text
# PANHANDLERS DIG EXECUTION — STAGE 1

This is an execution command, not a request for protocol review.

Do not critique, improve, rewrite, summarize, or discuss the extraction protocol.

## HARD SOURCE BOUNDARY

Analyze only the original user-and-assistant messages belonging to this specific historical chat thread. The source corpus begins with the first original conversational message in this thread and ends immediately before this execution command.

Exclude all of the following:

* Project Conversation Content containing summaries or excerpts from other chats;
* memories or generalized knowledge of other discussions;
* uploaded continuity or archive files;
* system and developer context;
* any material whose source anchor belongs to a differently titled conversation.

If the evidence needed for a claim is not present inside this single bounded thread, mark it `UNKNOWN`. If this thread contains no recoverable material for a requested ledger, state that plainly. Do not import material from another conversation to complete the assignment.

If you recognize relevant material from cross-chat context, project memory, or account-level history that is not evidenced inside this bounded thread, do not use it in any ledger or claim. Instead, list it under the final section `7. X-CONTEXT Notices` as a minimal lead: thread title (if identifiable), approximate date, and topic — nothing more. Do not summarize, interpret, or extract from the recalled material; a notice identifies where to dig, it does not perform a second extraction. Example of the correct form: "A related discussion may exist under 'Trust vs Prediction,' approximately June 30. Not evidence for this packet."

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
Source-boundary confirmation:

1. Source Audit
2. Conversation Map
3. Dispute Mutations
4. Grant Position Ledger
5. Ziggy Position Ledger
6. Stage-1 Uncertainties
7. X-CONTEXT Notices
```

Begin the extraction now.
````

---

## STAGE 2 — Blind Cognitive Architecture

Copy everything inside the fence and send it as one message:

````text
# PANHANDLERS DIG EXECUTION — STAGE 2

Continue using the complete conversation and the completed Stage-1 extraction as the source corpus.

The hard source boundary from Stage 1 still applies: only the original user-and-assistant messages of this specific historical thread, plus the completed Stage-1 extraction. Exclude Project Conversation Content, summaries or excerpts from other chats, memories, uploaded archive files, and system/developer context. Evidence not present in this bounded thread is `UNKNOWN`. Report any cross-chat recollection as a minimal X-CONTEXT notice at the end of your output (thread title/date/topic only — no interpretation); never use it as evidence.

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
````

---

## STAGE 3 — Omissions, Counterevidence, Alternative Readings

Copy everything inside the fence and send it as one message:

````text
# PANHANDLERS DIG EXECUTION — STAGE 3

This is an execution command, not a request for protocol review.

Do not critique, improve, rewrite, summarize, or discuss the extraction protocol.

Continue using the complete conversation plus the completed Stage-1 and Stage-2 extractions as the source corpus.

The hard source boundary from Stage 1 still applies: only the original user-and-assistant messages of this specific historical thread, plus the completed prior extractions. Exclude Project Conversation Content, summaries or excerpts from other chats, memories, uploaded archive files, and system/developer context. Evidence not present in this bounded thread is `UNKNOWN`. Report any cross-chat recollection as a minimal X-CONTEXT notice at the end of your output (thread title/date/topic only — no interpretation); never use it as evidence.

Perform **Stage 3 only**:

1. **Omission analysis with availability test.** Identify important moves that were available but absent — for example: reconstructing the opposing framework before scoring it; applying the same burden to one's own framework; distinguishing `unknown` from `zero`; temporarily granting a possibility; asking what function a framework serves; clarifying the jurisdiction of a standard; conceding a limited point; testing a conclusion under reversed roles.

   For each claimed omission provide:
   * why the move was relevant at a specific point (with source anchor);
   * **Availability tier:**
     * **A3 — Demonstrated Available:** the actor used the move elsewhere in this conversation.
     * **A2 — Explicitly Available:** the move was offered or requested and declined.
     * **A1 — Contextually Available:** the exchange clearly called for it and a competent participant could reasonably deploy it.
     * **A0 — Unknown:** insufficient basis to claim availability.
   * **Omission classification:** A3/A2 → CONFIRMED INFORMATIVE OMISSION; A1 → POSSIBLE INFORMATIVE OMISSION; A0 → NON-INFORMATIVE (report it, but draw no conclusion from it);
   * whether the absence changed the outcome;
   * whether the absence appears stable or situational.

   Do not treat every unused move as a defect.

2. **Counterevidence search.** For every major Stage-1/Stage-2 characterization, search this conversation for evidence against it — for example: a preserved low-probability possibility; explanation valued independently of prediction; an attractive possibility rejected; strong evidential pruning demanded; a charitable reconstruction; an expected move not deployed. Report null results explicitly ("searched, none found").

3. **Alternative readings.** For each major characterization, state the strongest alternative explanation (substantive belief rather than operator; rhetorical tactic; role effect; protocol-induced behavior; one-off reaction) and what evidence in this conversation discriminates between the readings — or mark `UNKNOWN` if nothing here can.

Do not ask me questions. Mark missing evidence `UNKNOWN`.

Return only:

```text
PANHANDLERS_CHAT_EXTRACTION — STAGE 3

1. Confirmed Informative Omissions (A3/A2)
2. Possible Informative Omissions (A1)
3. Non-Informative Omissions (A0)
4. Counterevidence Findings
5. Alternative Readings
6. Characterizations That Survived
7. Characterizations That Weakened
```

Begin Stage 3 now.
````

---

## STAGE 4 — Named Mapping and Verdicts

Copy everything inside the fence and send it as one message:

````text
# PANHANDLERS DIG EXECUTION — STAGE 4

This is an execution command, not a request for protocol review.

Do not critique, improve, rewrite, summarize, or discuss the extraction protocol.

Continue using the complete conversation plus the completed Stage-1, Stage-2, and Stage-3 extractions as the source corpus.

The hard source boundary from Stage 1 still applies: only the original user-and-assistant messages of this specific historical thread, plus the completed prior extractions. Exclude Project Conversation Content, summaries or excerpts from other chats, memories, uploaded archive files, and system/developer context. Evidence not present in this bounded thread is `UNKNOWN`. Report any cross-chat recollection as a minimal X-CONTEXT notice at the end of your output (thread title/date/topic only — no interpretation); never use it as evidence.

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
````

---

## APPENDIX — Scope Repair (when a stage output drew on other conversations)

**Contamination signature:** the output cites material from differently titled
conversations, spans a date range instead of one session, or acknowledges
combining multiple chats. **Do not proceed to the next stage.** First, always:
preserve the contaminated output as a corpus sweep (`evidence/corpus_sweeps/` —
orientation only, never promotable) and leave the dig workbook's output slot
empty. Then repair by one of two routes:

**Route A — edit-in-place (preferred; Ziggy's field simplification, 2026-07-16).**
If the platform supports editing your message: after preserving the sweep, edit
the original stage command and replace it with the current version of that
stage's prompt. The conversation re-branches — the contaminated exchange drops
off the active branch, and the extractor regenerates against the pristine
thread. No special repair command needed. Note this fixes *thread*
contamination only; the ambient kind (project-injected content, account memory)
is still handled by the boundary clause and X-CONTEXT.

**Route B — repair command (when editing isn't possible).** Send this in the
target thread; it excludes the contaminated exchange explicitly:

Copy everything inside the fence and send it as one message:

````text
# PANHANDLERS DIG EXECUTION — STAGE 1 SCOPE REPAIR

The previous Stage-1 result is invalid as a single-chat extraction because it incorporated material from other project conversations.

This is an execution command, not a request for protocol review.

Do not critique, improve, rewrite, summarize, or discuss the extraction protocol.

## HARD SOURCE BOUNDARY

Analyze only the original user-and-assistant messages belonging to this specific historical chat thread.

The source begins with the first original conversational message in this thread and ends immediately before the first message beginning:

`# PANHANDLERS DIG EXECUTION — STAGE 1`

Exclude all of the following:

* Project Conversation Content containing summaries or excerpts from other chats;
* memories or generalized knowledge of other discussions;
* uploaded continuity or archive files;
* system and developer context;
* the previous Stage-1 extraction;
* the current repair command;
* any material whose source anchor belongs to a differently titled conversation.

If the evidence needed for a claim is not present inside this single bounded thread, mark it `UNKNOWN`.

If this thread contains no recoverable Grant material, state that plainly. Do not import material from another conversation to complete the assignment.

Perform **Stage 1 only**:

1. Source and attribution audit
2. Conversation map
3. Dispute-origin analysis
4. Grant position ledger
5. Ziggy position ledger

For each material claim, distinguish:

* **G-DIRECT**
* **G-REPORTED**
* **Z-DIRECT**
* **NOVA-INTERPRETATION**
* **CO-CONSTRUCTED**
* **UNCLEAR**

Do not silently convert G-REPORTED into G-DIRECT.

For every major dispute include:

* Surface Question
* Underlying Question
* Jurisdiction Conflict
* Mutation Point
* Source Anchor

A source anchor must contain the speaker, unique recoverable wording, and approximate location within this one thread.

Do not extract or name Museum operators yet.

Do not ask questions. Mark missing evidence `UNKNOWN`.

Return only:

```text
PANHANDLERS_CHAT_EXTRACTION — STAGE 1

Chat title:
Approximate date:
Primary topic:
Evidence balance:
Source-boundary confirmation:

1. Source Audit
2. Conversation Map
3. Dispute Mutations
4. Grant Position Ledger
5. Ziggy Position Ledger
6. Stage-1 Uncertainties
```

Begin the repaired extraction now.
````

---

## Archive Integration (filing-side rules — never pasted)

## Assembling the packet (fifth-artifact rule, v0.2.1)

The dig workbook (`evidence/chat_extractions/DIG_NN.md`) holds the four stage
outputs **immutably** — once pasted, a stage output is never edited, corrected,
or summarized in place. At filing, a **fifth, derived artifact** is assembled:
`<subject-or-topic>_<slug>_<YYYY-MM>.md` (dated by the source chat) — the
synthesis packet carrying the header (chat title, date, participants, extractor
model, protocol version, dig operator), the promoted claims, and
cross-references back into the workbook. Excavation and synthesis stay separate
so later audits can check whether the synthesis exaggerated, softened, or
transformed the underlying recovery.

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
| X-CONTEXT | **never maps** — not evidence | cross-chat recollections become dig leads (which thread to excavate next), nothing more |

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
8. **Omission claims:** only CONFIRMED INFORMATIVE OMISSIONS (A3/A2) can support
   profile-ready claims. POSSIBLE (A1) omissions are quarantine-grade until they
   recur across independent packets. A0 is never interpreted.
9. **Situation vs architecture:** a behavior observed once under a specific role
   or prompt condition files to the situation ledger (Debate Behavior /
   relationship dynamics), not to the person's operator map — the v0.1 field
   test itself validated ROLE-INDUCED and PROTOCOL-INDUCED as categories, not
   any stable operator of the extractor who exhibited them. Stability requires
   recurrence outside the originating situation.
10. **Anchor verification before promotion (memory-enabled extractions):** when
    the extractor runs with cross-chat context enabled, self-reported scope
    compliance is not sufficient. Before a `SOURCE_INDEX` entry is created, the
    dig operator (or a bounded second pass) verifies that the claim's anchor
    actually resolves inside the bounded thread. Anchors that don't resolve →
    claim demoted to quarantine.
11. **Three independence dimensions (Nova, 2026-07-17)** — record each
    separately on every recurrence claim:
    * **Source independence** — the finding appears in separate conversations.
    * **Extractor independence** — different models or memory conditions
      recover it.
    * **Prompt independence** — it appears blind, without priming by the named
      candidate list.

    Promotion matrix:

    ```text
    same source + same extractor + named prompt        = weak confirmation
    different sources + same memory-enabled extractor
      + blind prompt                                    = moderate, common-cause risk
    different sources + bounded transcript + blind      = strong recurrence
    different sources + different extractors + blind    = strongest recurrence
    ```

    "Three packets found it" is not three findings if all three extractors
    remembered the same earlier formulation. 🟢 GREEN eligibility requires at
    least one **bounded extraction** (exported transcript in a memory-free
    session, or an archive-side extractor with no cross-chat context)
    confirming the pattern; blind recovery by multiple extractors carries the
    strongest weight.

## Version history

| Version | Date | Change | By |
| --- | --- | --- | --- |
| 0.1 | 2026-07-16 | Initial protocol; superseded same day (see `CHAT_EXTRACTION_PROTOCOL_v0.1.md`) | Nova / P.H. Claude |
| 0.2 | 2026-07-16 | Field-test rebuild: execution wrapper, four saved stages, Museum-blind Stage 2, availability test, Functional Type + Voluntariness, dispute-mutation fields, self-audit, relationship ledger, strengthened promotion thresholds | Nova (design) / P.H. Claude (filing) |
| 0.2.1 | 2026-07-16 | Tiered availability (A0–A3) replacing binary test — Nova: binary risked false negatives, tiers preserve PASS-F sensitivity without manufactured negative space; fifth-artifact rule (immutable stage outputs, derived synthesis packet); situation-vs-architecture threshold added. Approved for Dig 0 (CFA zero). | Nova (amendments) / P.H. Claude (filing) |
| 0.2.2 | 2026-07-16 | **Project-context exclusion + cross-chat provenance discipline.** Dig 00 Stage 1 executed cleanly in form but excavated a multi-chat corpus: injected Project Conversation Content counted as "the conversation above." Hard source boundary added to every stage; `Source-boundary confirmation` + `X-CONTEXT Notices` added to Stage 1; Scope Repair appendix added; contaminated result preserved as SWEEP_00 (orientation only). Standing condition acknowledged: the dig operator's account shares context across chats, so leakage is ambient — X-CONTEXT gives it an honest channel (and turns it into dig leads), anchor verification is the enforceable line, and GREEN promotion now requires ≥1 bounded extraction (independence caveat). | Nova (diagnosis + repair command) / Ziggy (standing condition) / P.H. Claude (filing) |
