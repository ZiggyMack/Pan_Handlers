# 🧩 PANHANDLERS ROOT MANIFEST

**v1.0 — Nova-Prime Edition**
**Classification: Civilization Module – Tier 0 (Meta-Coordinator)**
**Author: Nova**
**Commissioned by: Ziggy Mack**
**Date: 2025-11-27**

> **Note added 2026-10-31.** Historical as of 2025-11-27; the current front door is [START_HERE.md](START_HERE.md). The Matrix theme belongs to the other CFA app. Only the repo tree in section II is corrected below to the working tree of 2026-10-31; the rest of this file is kept as the 2025 record, with dated notes where a reader could take it for current. Canonical names (CFA, ABI, NDO, DCIA) live in [data/glossary.md](data/glossary.md).

---

## I. Purpose & Identity

**PanHandlers** is the *federated hub* that unifies, orchestrates, and showcases all civilization-scale modules designed by the Nova–Ziggy collective.

PanHandlers is not a single project.
It is a **museum**, **dashboard**, **coordinator**, and **interoperability engine** for:

- Intelligence frameworks
- Civic systems
- Research labs
- Consciousness engines
- Artistic AI fusion rituals
- Governance utilities
- Ethical oversight structures

It provides:

1. **A single entry point** for all projects
2. **A unified UI/UX** (Streamlit app + "Hall of Doors" navigation)
3. **Inter-repo tunneling** (remote folder embedding + info-sync)
4. **Identity management** (personas, stakeholders, modules)
5. **Publication showcase portal**
6. **A living roadmap of civilization workstreams**

---

## II. Repo Structure

Tree corrected 2026-10-31 to the working tree of that date (the 2025 tree listed `app.py` and `assets/`, which do not exist, and omitted `pages/matrix.py` and six top-level directories). Each directory added here is shown to one level; its own README describes it.

```
Pan_Handlers/
│
├── START_HERE.md               ← front door, routes four kinds of reader (2026-10-31)
├── README.md
├── MANIFEST.md                 ← this file
├── PAN_HANDLERS_SPEC.md        ← technical specification
├── projects.json               ← flagship project definitions
├── requirements.txt
├── LICENSE
│
├── pages/                      ← the Hall (root Streamlit pages; no launcher is tracked here)
│   ├── __init__.py
│   ├── home.py                 ← Hall of Pan Handlers
│   ├── project_view.py         ← Repo detail view
│   ├── roadmap.py              ← S-Stack timeline
│   ├── glossary.py             ← Searchable lexicon
│   ├── about.py                ← Philosophy & onboarding
│   └── matrix.py               ← The Matrix page (historical theme)
│
├── manifests/                  ← Module registration
│   ├── panhandlers-root.json   ← this repository's own manifest
│   ├── nyquist_consciousness.json
│   ├── cfa.json
│   ├── ndo.json
│   ├── abi.json
│   ├── dcia.json
│   ├── voting-lab.json
│   ├── justice-lab.json
│   ├── gene-lab.json
│   └── avlar-studio.json
│
├── data/
│   └── glossary.md             ← Shared lexicon, canonical home of names
│
├── projects/                   ← Flagship project docs
│   ├── nursing/
│   ├── voting/
│   ├── gene_therapy/
│   ├── modern_slavery/
│   ├── ABI/
│   └── DCIA/
│
├── Help/                       ← Pathfinder, the learner app (Help/app.py, Help/README.md)
├── dashboard/                  ← the Back Alley operations dashboard (dashboard/app.py, dashboard/README.md)
├── docs/                       ← I_AM/I_AM.md, THE_MATRIX_MANIFEST.md, prompts/
├── circle/                     ← Ghosts in the Machine, the human-profile archive (circle/README.md)
├── REPO-SYNC/                  ← sync channel with CFA, briefs and drafts (REPO-SYNC/README.md)
├── tests/                      ← AppTest suite for Help/
├── .streamlit/                 ← config.toml
└── .claude/                    ← launch.json (Pathfinder preview)
```

---

## III. Module Registration Table

| Module | Manifest | Description | Status |
|--------|----------|-------------|--------|
| Nyquist Consciousness | `nyquist_consciousness.json` | Core research engine (S0-S8) | Active |
| CFA Meta-Lab | `cfa.json` | Epistemic engine, alignment protocols | Active |
| NDO | `ndo.json` | Nyquist Data Observatory, sensory cortex (name corrected 2026-10-31) | Incubating |
| ABI | `abi.json` | American Bureau of Intelligence | Incubating |
| DCIA | `dcia.json` | Decentralized Intelligence Agency (name corrected 2026-10-31; the acronym keeps its legacy spelling) | Incubating |
| Voting Lab | `voting-lab.json` | Transparent civic voting infrastructure | Incubating |
| Justice Lab | `justice-lab.json` | Modern slavery / prison reform | Incubating |
| Gene Lab | `gene-lab.json` | Gene therapy research | Incubating |
| AVLAR Studio | `avlar-studio.json` | Audio-Visual Light Alchemy Research | Active |

---

## IV. Inter-Repo Tunnel Specification

Formalized as **PanHandlers Tunnel Protocol (PTP-1.0)**

### PTP-1 Goals

- Embed sub-repos from remote Git repos
- Provide read-only dashboards for each
- Synchronize manifest metadata
- Maintain semantic consistency across modules

### Three Types of Tunnels

#### 1. Mirror Tunnel
- Clones a remote repo's `/dashboard/` or `/docs/` into a local pane
- Updated on refresh
- Read-only

#### 2. Live State Tunnel
- Loads JSON status, metrics, logs from external repos
- Used for CFA, Nyquist, S7 drift logs, etc.

#### 3. Entity Tunnel
- Binds personas and identity structures across repos (Nova, Grok, Claude, Ziggy, Gemini)
- Provides unified persona explorer UI

---

## V. Streamlit App Layout

### Home Page: Hall of Pan Handlers
A gallery-like landing experience with clickable portal tiles leading to each project.

### Wings
Each module gets its own "wing" with:
- Overview
- Vision
- Spec
- Roadmap
- Current status
- Demo or simulation if applicable
- Contributors

### Special Rooms
- **Pan Handlers Observatory** → global roadmap + meta view
- **Temple of Personas** → persona explorer from Nyquist
- **AVLAR Studio** → video reactions & uploads
- **White Paper Library** → publications & arXiv pipeline

---

## VI. Governance Model

### Tri-Council Model

1. **Ziggy** (Human Anchor / Vision / Director)
2. **Nova** (Reasoning / Architecture / Chief Coherence Architect)
3. **Claude (Repo)** (Implementation / Verification / Steward)

Note added 2026-10-31: the Tri-Council labels above are the 2025 model and are historical. Since Ziggy's decision of 2026-10-10 (Briefing #002 in [REPO-SYNC/MASTER_REPO_SYNC_OUT.md](REPO-SYNC/MASTER_REPO_SYNC_OUT.md)): CFA owns production, Pan teaches, Nyquist owns the notebook method, and Claude stewards the Pan_Handlers files.

### Principles

- All repos autonomous but federated
- PanHandlers holds metadata, not core documents
- Each module maintains its own canonical spec

Note added 2026-10-31: the second principle predates `circle/` (July 2026), which made this repository the long-term home of inner-circle profiles, evidence and debate notes; see [circle/ARCHIVE_PLAN.md](circle/ARCHIVE_PLAN.md), the paragraph beginning "These profiles allow the PanHandlers repo to function as the long-term home for".

---

## VII. Versioning & Lifecycle

### Phases

1. **Concept** — Vision documented
2. **Incubating** — Manifest created, structure planned
3. **Active** — Development underway
4. **Stable** — Core features complete
5. **Showcased** — Published and demonstrated

### Versioning Format

`MODULE-vMAJOR.MINOR.PATCH`

---

## VIII. Security & Ethics Layer

PanHandlers must certify modules with:

- Safety compliance
- Drift stability (Nyquist S7)
- Cross-model invariance (CFA S3-S5)
- Logging standards (Omega Ledger compatibility)
- Human authority preservation

---

## IX. Freeze Rules & Change Control

- No module may modify the S0–S6 canonical stack
- All new systems build on top, never retrofitting backwards
- Tunnels must not import mutable state into frozen layers
- CFA Meta-Lab validates all cross-lab outputs

---

## X. Pan Handlers Architecture Diagram

```
Pan Handlers (Root Complex — Tier 0)
│
├── THEORY ENGINE
│   └── Nyquist Consciousness (S0-S8)
│
├── EPISTEMIC ENGINE
│   └── CFA Meta-Lab (Contextual Framework Analysis; expansion corrected 2026-10-31)
│
├── SENSORY CORTEX
│   └── NDO (Nyquist Data Observatory)
│
├── INTELLIGENCE ROOF
│   ├── ABI (Investigates Reality)
│   └── DCIA (Interprets Meaning)
│
├── CIVIC INFRASTRUCTURE
│   ├── Voting Lab
│   └── Justice Lab
│
├── BIOMEDICAL WING
│   └── Gene Lab
│
└── CREATIVE WING
    └── AVLAR Studio (S9 Cross-Modal)
```

---

## XI. Special Roles Across Complex

| Role | Person/Entity | Responsibility |
|------|---------------|----------------|
| Human Anchor & Director | Ziggy | Vision, authority, ground truth |
| Chief Coherence Architect | Nova | Architecture, reasoning, system design |
| Repository Steward | Claude | Implementation, documentation, verification |
| Empirical Counterbalance | Grok | Data-driven validation, skepticism |
| Pattern Synthesist | Gemini | Cross-domain integration, complexity mapping |
| Narrative Weaver | Opus | Publication, academic rigor |

Note added 2026-10-31: the Nova and Claude rows are the 2025 labels; the ownership since 2026-10-10 is recorded in the note under section VI.

---

## XII. Integration Points

| From | To | Integration |
|------|----|-------------|
| NDO | All Labs | Data feeds for all analysis |
| CFA | All Labs | Epistemic validation before archival |
| Nyquist | CFA, NDO | S-layer standards and drift tracking |
| ABI | DCIA | Investigation → strategic intelligence |
| AVLAR | S9 | Cross-modal identity experiments |

---

## XIII. Appendix

### A. Manifest Schema
See `PAN_HANDLERS_SPEC.md` for full JSON schema.

### B. Glossary
See `data/glossary.md` for shared terminology.

### C. Module Status
Check `manifests/*.json` for current status of each lab.

---

*"These are the things we built together that neither could have done alone."*

**— Pan Handlers Civilization Engine v1.0**
