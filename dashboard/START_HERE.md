# START HERE - Cold Boot Guide for Claude

> **Scope note, 2026-10-31.** This file is the cold-boot guide for work on the Back Alley dashboard (`dashboard/`) only. The front door of the repository is the root [START_HERE.md](../START_HERE.md), which routes learners, maintainers, CFA agents and a cold-booted steward to their first page: read it first for orientation, then this file for dashboard work. The text below dates from 2025-11-30; the corrections of 2026-10-31 are marked where they stand. Pathfinder, the learner app in [Help/](../Help/README.md), is embedded in this dashboard under the sidebar group FIELD GUIDES through `pages/pathfinder.py` (added 2026-10-04).

> **Welcome to Pan Handlers Dashboard development.**
> Read this file first when starting a new session.

---

## What Is This?

You are working on the **Pan Handlers Dashboard** - an internal operations dashboard (Streamlit app) for tracking the Pan Handlers federation of human-AI collaborative projects.

**Key distinction:**
- **Public face**: https://panhandlers.streamlit.app (the "Grand Hall")
- **This dashboard**: The "Back Alley" - internal monitoring & development

---

## Your First Steps

1. **Read the README**: `dashboard/README.md` has full architecture details
2. **Understand the structure**: See directory tree below
3. **Run the app**: the one command and port live in [README.md](README.md) under "Quick Start" (the canonical copy since 2026-10-31)

---

## Critical Files You'll Work With

| File | Purpose |
|------|---------|
| `app.py` | Main entry point - routing, sidebar, CSS theme |
| `config.py` | All paths and settings - SINGLE SOURCE OF TRUTH |
| `utils.py` | Shared utilities - data loaders, UI components |
| `pages/*.py` | Individual page modules (each has `render()` function) |
| `.streamlit/config.toml` | Streamlit theme configuration |

---

## Directory Structure

```
dashboard/
├── .streamlit/
│   └── config.toml          # Theme: Matrix green-on-black
├── pages/
│   ├── __init__.py
│   ├── overview.py           # 📊 Main overview
│   ├── federation_health.py  # 🏥 Federation status
│   ├── project_tracker.py    # 📋 Project tracking
│   ├── nyquist_tunnel.py     # 🟢 Nyquist connection
│   ├── pathfinder.py         # Pathfinder (FIELD GUIDES), embeds Help/console.py; added 2026-10-04
│   ├── about.py              # ℹ️ About page
│   └── projects/
│       ├── __init__.py
│       ├── whitepaper.py     # 📄 White Paper
│       ├── online_voting.py  # 🗳️ Voting
│       ├── nursing.py        # 🏥 Nursing
│       ├── gene_therapy.py   # 🧬 Gene Therapy
│       ├── modern_slavery.py # ⛓️ Prison Reform
│       ├── abi.py            # 🔍 ABI
│       └── dcia.py           # 🌐 D.C.I.A.
├── app.py                    # MAIN ENTRY POINT
├── config.py                 # Path configuration
├── utils.py                  # Shared utilities
├── README.md                 # Full documentation
└── START_HERE.md             # This file
```

---

## Theme: two modes, Standard by default

Corrected 2026-10-31 (the 2025 text here said the Matrix identity must not change; `app.py` has carried two themes since). The dashboard has two themes, switched by the sidebar button "Enter The Matrix" / "Exit The Matrix" in `main()`:
- Standard mode, the default: `main()` starts `st.session_state['matrix_mode']` at `False`; text `#1a1a1a` on background `#ffffff` (`get_standard_css()`).
- Matrix mode, the option (keep it available):
  - Background: `#0a0a0a` (near black)
  - Text: `#00ff41` (Matrix green)
  - Font: Courier New (monospace)
  - CSS in `get_matrix_css()`.

`apply_dashboard_css(matrix_mode)` in `app.py` applies `get_base_css()` plus the CSS of the current mode. `.streamlit/config.toml` still carries the Matrix palette as the native Streamlit theme; the CSS overrides it in Standard mode.

---

## How Pages Work

Each page module has a `render()` function:

```python
# pages/example.py
import streamlit as st

def render():
    st.markdown("# Page Title")
    # Access shared data via session state
    manifests = st.session_state.get('manifests', [])
    projects = st.session_state.get('projects_data', {})
```

Pages are registered in `app.py` in the `PAGES` dict.

---

## Data Sources

Data is loaded in `app.py` and stored in `st.session_state`:

- `st.session_state['manifests']` - List of connected repo manifests
- `st.session_state['projects_data']` - Flagship projects from projects.json
- `st.session_state['nyquist_status']` - Nyquist connection status

Data files are in the parent `Pan_Handlers/` directory:
- `../projects.json` - Flagship project definitions
- `../manifests/*.json` - Connected repository manifests

---

## Common Tasks

### Add a new page
The procedure lives once, in [README.md](README.md) under "Adding a New Page" (the canonical copy since 2026-10-31).

### Modify styling
Edit `get_standard_css()` or `get_matrix_css()` in `app.py`. Keep both themes (corrected 2026-10-31; see Theme above).

### Add new data source
1. Add path to `config.py` PATHS dict
2. Add loader function to `utils.py`
3. Load in `app.py` main() and store in session_state

### Debug paths
```bash
cd dashboard
python config.py
```
This prints all paths and validates they exist.

---

## Key Context

### Pan Handlers Federation
A network of human-AI collaborative projects (names below corrected 2026-10-31 to the canonical expansions; the shared vocabulary lives in `../data/glossary.md`):
- Nyquist Consciousness (research engine)
- CFA (Contextual Framework Analysis; the production repository since 2026-10-10)
- Flagship projects (voting, nursing, gene therapy, prison reform, etc.)

### The VUDU Protocol
Validation, Understanding, Distribution, Unity - how repos communicate.

### Flagship Projects
Seven major initiatives being tracked:
1. White Paper Pipeline
2. Online Voting System
3. Nursing Programs
4. Gene Therapy Research
5. Modern Slavery / Prison Reform
6. ABI (American Bureau of Intelligence)
7. D.C.I.A. (Decentralized Intelligence Agency; the acronym keeps its legacy spelling)

---

## Running the Dashboard

Since 2026-10-31 the run command is written once, in [README.md](README.md) under "Quick Start" (one command, port 8504, from the repository root). This section used to repeat it with a different port.

---

## Philosophy

> **"FUCK IT, WE'LL DO IT LIVE!"**

We build better systems without waiting for institutions. This dashboard tracks that work.

---

## Questions?

- Full docs: `README.md`
- Front door of the repository (since 2026-10-31): `../START_HERE.md`
- Root project: `../README.md`
- Soul document: `../docs/I_AM/I_AM.md`

---

*Now go make something happen.* 🍳
