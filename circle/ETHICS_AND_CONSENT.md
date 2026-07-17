# ⚖️ Ethics & Consent — The Gate

> This archive profiles **real people** in a private debate circle. Everything else
> in `circle/` is subordinate to this file. When speed and safeguards conflict,
> safeguards win — that is the one place "fuck it, we'll do it live" does not apply.

**Last reviewed:** 2026-07-16

---

## 1. Publication Status: PUBLIC (decided 2026-07-16)

**Ziggy's ruling:** *"It all goes. We are not focusing on personal information —
we are focusing on ideas. All members gave consent to share their ideas."*
Consent basis is recorded in [`CONSENT_LEDGER.md`](CONSENT_LEDGER.md) with the
archive's own source discipline (reported consent, upgradeable to direct).

`ZiggyMack/Pan_Handlers` is a public GitHub repository, so the whole `circle/`
archive is published. The protection therefore moves from the **repo boundary**
to the **content boundary**:

- The archive publishes **reasoning** — positions, operators, sequences, debates,
  idea trails, intellectual relationship dynamics.
- Material that is not about reasoning (health, family, finances, legal matters,
  private life) **never enters the archive at all** — not "kept private," but
  *excluded at ingestion*. The §3 Do-Not list is the ingestion filter.
- Publishing is one-way: pushed content must be assumed permanently cached and
  indexed even if later deleted. That is exactly why the ingestion filter is
  enforced *before* every commit, not after.

## 2. Content Boundary (replaces the old layer split)

```text
PUBLISHED  (the whole archive, by the 2026-07-16 decision)
    contract docs, member profiles, operator analysis, position ledgers,
    debate records, idea trails, timeline, extraction packets

NEVER ENTERS THE ARCHIVE  (ingestion filter — checked before every commit)
    sensitive personal information (non-reasoning); mental-health framing;
    private motives asserted as fact; jokes converted to traits;
    assistant formulations attributed to members who never adopted them
```

Two disciplines survive the public turn **unchanged**:

- **Consent to share ideas ≠ endorsement of our interpretation of them.** The
  member-response invitation at EVIDENCED status still stands; a profile is not
  1.0 until its subject has seen it, and the `CONTESTED` mechanism matters *more*
  in public, not less.
- **Quarantine is an evidentiary status, not a privacy shield.** QUARANTINED
  claims in extraction packets are public like everything else — quarantine means
  "not profile-grade yet," so write even quarantined claims to publication
  standard.

## 3. Do Not (hard rules, from the founding charter)

- Diagnose mental illness — ever, under any framing.
- Claim private motives as fact.
- Convert jokes into permanent traits.
- Preserve sensitive personal information unnecessarily (health, family, finances,
  legal matters — if it isn't about *reasoning*, it doesn't belong here).
- Treat one bad interaction as identity.
- Write profiles as prosecution briefs — the Grant pilot exists to *explain*
  stability, not to prove wrongness.
- Conceal Ziggy's interpretive role (see §5).
- Allow operator names to become insults — the moment "that's just your CO-004"
  ends an argument instead of opening one, retire the usage.
- Automatically publish private-circle profiles publicly.

## 4. Do (equally hard rules)

- Preserve uncertainty — `UNKNOWN` is a complete and honorable answer.
- Attach evidence — claims above `INFERRED` require source IDs.
- Search for counterexamples — every operator entry ships with falsification
  conditions in the member's `OPEN_QUESTIONS.md`.
- Record member objections verbatim — `MEMBER_RESPONSE.md` is theirs, not ours.
- Permit revision — profiles version forward; superseded versions archive, they
  don't vanish.
- Document who made each inference — observer attribution on every claim.
- Distinguish descriptive models from moral judgments — "uses CO-004" is a
  description of a move, never a verdict on a person.

## 5. The Observer Problem

Ziggy is the primary observer; his interpretations shape this archive. Therefore:

- **Phase 2 (Ziggy control profile) is mandatory, not optional** — the archive must
  not quietly treat his frame as neutral (that would be the archive committing
  CO-007, Baseline Exemption, on itself).
- Claims sourced only from Ziggy's recollection cap at `INFERRED` until a second
  observer or a primary source corroborates.
- AI collaborators (P.H. Claude et al.) are observers too and are attributed the
  same way.

## 6. Member Rights (standing offer, not one-time)

Every profiled member may, at any time: **endorse · reject · revise · annotate ·
supply missing context · challenge operator labels · request removal of specific
content**. Responses are recorded in their `MEMBER_RESPONSE.md`; disputed claims
flip to `CONTESTED` and stay visible *as disputed*. Removal requests for
sensitive-personal (non-reasoning) content are honored without debate — by
deletion from the archive, with the honest caveat that internet caches cannot be
recalled, which is one more reason the §2 ingestion filter is strict.

Members should be *invited* to respond once their profile reaches EVIDENCED status
— a profile is not `1.0` until its subject has seen it.

## 7. Revision of This File

Changes to this file require a logged entry below and should be treated with the
same gravity as changing `PROFILE_SCHEMA.md`.

| Date | Change | By |
| ------ | -------- | ----- |
| 2026-07-16 | Initial contract (restricted-by-default posture) | Ziggy + P.H. Claude (Fable 5) |
| 2026-07-16 | **Publication decision: archive is public.** §1–2 rewritten from repo-boundary protection to content-boundary protection; consent ledger added. | Ziggy (decision); filed by P.H. Claude |
