# Pan Handlers Specification

**Version:** 1.0
**Status:** Active
**Purpose:** Define the manifest schema and architecture for cross-repo showcase system

> **Note added 2026-10-31.** Historical as of 2025-11-27; the current front door is [START_HERE.md](START_HERE.md). The Matrix theme belongs to the other CFA app. The manifest schema below is still the one the files in `manifests/` follow; the folder structure is corrected to the working tree of 2026-10-31; the page descriptions and the "Adding a New Repo" steps are the 2025 design, with dated corrections where a path does not exist.

---

## Overview

Pan Handlers is a **cross-repo showroom** that connects multiple project repositories into a unified showcase. Each participating repo publishes a `panhandlers_manifest.json` that describes its purpose, status, and projects.

---

## Manifest Schema (v1)

Each participating repo should have a `panhandlers_manifest.json` at its root.

### Required Fields

```jsonc
{
  "repo": "string",                 // Short repo name (no spaces)
  "display_name": "string",         // Pretty title for UI
  "owner": "string",                // Organization or user(s)
  "url_repo": "string",             // Git repository URL
  "url_dashboard": "string",        // Streamlit app URL (if live, or "TBD")
  "role": "string",                 // 1-line what-this-repo-is
  "status": "string",               // "Active", "Incubating", "Archived"
  "tags": ["string"],               // Freeform tags for filtering
  "summary": "string",              // 1-3 sentence description
  "last_updated": "YYYY-MM-DD"      // Last manifest update
}
```

### Optional Fields

```jsonc
{
  "contact": {
    "primary": "string",            // Lead contact name
    "email": "string"               // Contact email
  },
  "pillars": {
    "purpose": "string",            // Why this repo exists
    "methods": "string",            // How it works
    "outputs": "string"             // What it produces
  },
  "projects": [                     // Array of sub-projects
    {
      "id": "string",               // Stable ID (no spaces)
      "title": "string",            // Display title
      "status": "string",           // "Planned", "In Progress", "Complete", "Published"
      "type": "string",             // "Paper", "System", "Experiment", "Pilot", etc.
      "summary": "string",          // Brief description
      "links": {
        "paper": "string",          // Paper/docs URL
        "dashboard": "string",      // Dashboard URL
        "docs": "string"            // Documentation URL
      }
    }
  ]
}
```

### Status Values

**Repo Status:**
- `Active` - Actively developed
- `Incubating` - Early stage, concept phase
- `Archived` - No longer active, preserved for reference

**Project Status:**
- `Planned` - Defined but not started
- `In Progress` - Currently being worked on
- `Complete` - Finished, not published
- `Published` - Released publicly

**Project Types:**
- `Paper` - Academic publication
- `System` - Software/infrastructure
- `Experiment` - Research experiment
- `Pilot` - Real-world test
- `Case Study` - Analysis of specific situation
- `Theory` - Theoretical framework
- `Research` - Ongoing research program

---

## Pan Handlers Architecture

### Folder Structure

Tree corrected 2026-10-31 to the working tree of that date. The 2025 tree listed a root `app.py`, `config.py`, `utils.py` and `data/roadmap.json`, none of which exist (the only `config.py` and `utils.py` are the dashboard's, under `dashboard/`), and omitted `pages/matrix.py` and the directories `Help/`, `dashboard/`, `docs/`, `circle/`, `REPO-SYNC/` and `tests/`. The full tree is in [MANIFEST.md](MANIFEST.md), section II.

```
Pan_Handlers/
├── START_HERE.md               # Front door (2026-10-31)
├── README.md
├── MANIFEST.md
├── PAN_HANDLERS_SPEC.md        # This file
├── projects.json               # Flagship project definitions
├── requirements.txt
├── pages/                      # The Hall (root Streamlit pages; no launcher is tracked here)
│   ├── __init__.py
│   ├── home.py                 # Hall of Pan Handlers (main gallery)
│   ├── project_view.py         # Single repo detail view
│   ├── roadmap.py              # Global roadmap across repos
│   ├── glossary.py             # Lexicon of terms
│   ├── about.py                # How this network works
│   └── matrix.py               # The Matrix page (historical theme)
├── manifests/                  # Pan's own descriptions of each module (2025), one JSON each
│   ├── panhandlers-root.json
│   ├── nyquist_consciousness.json
│   ├── cfa.json
│   └── ... (ndo, abi, dcia, voting-lab, justice-lab, gene-lab, avlar-studio)
├── projects/                   # Flagship project documentation
│   ├── nursing/
│   ├── voting/
│   └── ... (gene_therapy, modern_slavery, ABI, DCIA)
├── data/
│   └── glossary.md             # Terms and definitions; canonical home of names
├── Help/                       # Pathfinder, the learner app (Help/app.py)
├── dashboard/                  # The Back Alley operations dashboard (dashboard/app.py, dashboard/config.py, dashboard/utils.py)
├── docs/                       # I_AM/I_AM.md, THE_MATRIX_MANIFEST.md, prompts/
├── circle/                     # Ghosts in the Machine, the human-profile archive
├── REPO-SYNC/                  # Sync channel with CFA, briefs and drafts
└── tests/                      # AppTest suite for Help/
```

### Page Descriptions

#### 1. Home / Hall of Pan Handlers
- Grid of repo cards (each card = one manifest)
- Card contents: display name, role, status badge, tags, summary
- Buttons: View Details, Open Dashboard, View on GitHub
- Styled as "parchment/ledger pages" aesthetic

#### 2. Project View
- Left column: Repo summary (title, role, status, pillars)
- Right column: List of projects from manifest
- Each project as mini-card with title, type, status, links

#### 3. Global Roadmap
- S-Stack timeline (S0-S9 with status indicators)
- Cross-repo initiatives table
- Executive cockpit across all projects

#### 4. Glossary / Lexicon
- Core Concepts (Nyquist, Identity Manifold, Omega Nova, etc.)
- Roles / Personas (Nova, Repo Claude, Ziggy, etc.)
- Artifacts (Omega Ledger, Pan Handlers, etc.)

#### 5. About
- What is Pan Handlers?
- How to add your repo (instructions)
- How repos fit into the bigger picture

---

## Adding a New Repo

1. Create `panhandlers_manifest.json` in your repo root
2. Follow the schema above
3. Submit PR to Pan Handlers repo adding your manifest URL to `config.py`
   (Corrected 2026-10-31: there is no root `config.py`, and `dashboard/config.py` holds no manifest URL list. As the repository stands, a module is registered by adding its JSON file to `manifests/`, which `dashboard/utils.py` loads by directory listing.)
4. Your repo appears as a portal tile in the Hall

---

## Manifest URLs Configuration

Note added 2026-10-31: no file in this repository defines `MANIFEST_URLS`; the block below is the 2025 design, kept as written. Manifests are read from the `manifests/` folder only.

Pan Handlers reads manifests from configured URLs:

```python
MANIFEST_URLS = [
    "https://raw.githubusercontent.com/ZiggyMack/nyquist-consciousness/main/panhandlers_manifest.json",
    "https://raw.githubusercontent.com/ZiggyMack/CFA/main/panhandlers_manifest.json",
    # Add more repos here
]
```

For local development, manifests can also be read from `manifests/` folder.

---

## Design Philosophy

### "The Halls" Metaphor
- Pan Handlers is the **Overworld Map**
- Each repo is a **dungeon/room** you can explore
- Projects are **exhibits** within each room
- You can always return to the Hall from any room

### Two Faces
- **Lab / Dashboard** (inside each repo) = Operations Deck
- **Hall / Showcase** (Pan Handlers) = Gallery of Outcomes

### FUCK IT, WE'LL DO IT LIVE
- Build better systems without waiting for institutions
- Human-AI collaboration as infrastructure
- Neither could have done it alone

---

## Version History

| Version | Date | Changes |
|---------|------|---------|
| 1.0 | 2025-11-27 | Initial specification |

---

Note added 2026-10-31: the two lines below are the 2025-11-27 state, kept as written. The current state is described in [START_HERE.md](START_HERE.md) and [Help/README.md](Help/README.md).

**Status:** Production Ready
**Next Steps:** Implement full Streamlit app with all pages
