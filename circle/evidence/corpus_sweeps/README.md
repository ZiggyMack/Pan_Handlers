# 🌐 Corpus Sweeps — Orientation Layer

> A **sweep** is an extraction that drew on cross-chat context (project-injected
> summaries, account memory, multiple threads) rather than one bounded
> conversation. Sweeps are the opposite failure-and-feature of digs: useless for
> promotion, excellent for **orientation** — locating which original threads
> hold the strongest material, and surfacing provisional position candidates to
> test in real digs.

**Status:** 1 sweep filed (SWEEP_00: Stage 1 + Stage 2 verbatim, 9 thread leads) · **Last reviewed:** 2026-07-17

## Hard Restrictions

- **ORIENTATION ONLY — NEVER PROMOTABLE.** A sweep must not generate
  `SOURCE_INDEX` entries, profile claims, operator attributions, or lexicon
  promotions. No exceptions — apparent recurrence inside a sweep may just be
  the same summary sampled twice.
- Sweeps may feed exactly two things: the **dig target hunt** (which threads to
  excavate) and **hypothesis formation** (what to look for once there).
- A dig stage output discovered to be contaminated gets preserved here (renamed
  `SWEEP_NN_<slug>_<date-range>.md`), and the dig workbook slot stays empty
  until a repaired bounded run returns (Scope Repair appendix,
  `../../CHAT_EXTRACTION_PROTOCOL.md`).

## Naming

`SWEEP_NN_<slug>_<YYYY-MM_to_MM>.md` — dated by the *range* the sweep spans,
because spanning a range instead of one session is precisely what makes it a
sweep.

## Header Convention

```markdown
# SWEEP NN — <name>

**Status:** ORIENTATION ONLY — NOT PROMOTABLE
**Protocol:** <version + stage that produced it>
**Scope:** <what corpus it actually drew on>
**Purpose:** <thread location / hypothesis formation>
**Restriction:** Must not generate SOURCE_INDEX entries or profile promotions
```
