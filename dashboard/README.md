# Pan Handlers Dashboard - The Back Alley

> **Internal operations dashboard for the Pan Handlers federation.**
> This is where the work happens. The public face is at [panhandlers.streamlit.app](https://panhandlers.streamlit.app).

---

## Quick Start

This is the canonical run instruction for the dashboard (declared 2026-10-31; `START_HERE.md` and `docs/prompts/dashboard_claude.md` point here instead of repeating it). From the `Pan_Handlers` repository root:

```bash
python -m streamlit run dashboard/app.py --server.port 8504
```

Visit http://localhost:8504. The port is the one in the docstring of `app.py`. Streamlit puts the script's own directory (`dashboard/`) on `sys.path`, which is why the bare imports in `app.py` (`config`, `utils`, `pages`) resolve when the command runs from the root; `tests/test_help_console.py` loads the app the same way.

**FIELD GUIDES → Pathfinder** opens the AI-assisted 3D/video learning console (`pages/pathfinder.py`, added 2026-10-04, embeds `Help/console.py`).
Pathfinder also runs on its own, on port 8506; since 2026-10-31 its install-and-run block lives once, in [Help/FILE_MAP.md](../Help/FILE_MAP.md) under "Run Pathfinder". See [the guide README](../Help/README.md) for notes,
JSON restore/export, and the four pipeline expansion plans.

Deploy source of record (Ziggy's decision of 2026-10-31): the hosted apps deploy from the Hall, the root `pages/` package, not from this directory. No launcher for the Hall is tracked in this repository (there is no root `app.py`); the hosted main file is configured on the host. For orientation start at the root [START_HERE.md](../START_HERE.md).

---

## Directory Structure

```
dashboard/
├── .streamlit/
│   └── config.toml          # Streamlit theme config (Matrix green-on-black)
├── pages/
│   ├── __init__.py           # Page module exports
│   ├── overview.py           # 📊 Main dashboard overview
│   ├── federation_health.py  # 🏥 Federation status & health
│   ├── project_tracker.py    # 📋 Track all flagship projects
│   ├── nyquist_tunnel.py     # 🟢 Connection to Nyquist Consciousness
│   ├── pathfinder.py         # Pathfinder (FIELD GUIDES), embeds Help/console.py; added 2026-10-04
│   ├── about.py              # ℹ️ About page
│   └── projects/             # Individual project pages
│       ├── __init__.py
│       ├── whitepaper.py     # 📄 White Paper Pipeline
│       ├── online_voting.py  # 🗳️ Online Voting System
│       ├── nursing.py        # 🏥 Nursing Programs
│       ├── gene_therapy.py   # 🧬 Gene Therapy Research
│       ├── modern_slavery.py # ⛓️ Prison Reform / Modern Slavery
│       ├── abi.py            # 🔍 American Bureau of Intelligence (name corrected 2026-10-31)
│       └── dcia.py           # 🌐 Decentralized Intelligence Agency (name corrected 2026-10-31)
├── app.py                    # Main Streamlit application entry point
├── config.py                 # Path configuration & settings
├── utils.py                  # Shared utilities & data loaders
├── README.md                 # This file
└── START_HERE.md             # Cold boot guide for Claude
```

---

## Architecture

### Entry Point: `app.py`

The main application that:
1. Sets up page config and the theme CSS (Standard by default, Matrix on the sidebar toggle; corrected 2026-10-31)
2. Loads data from `projects.json` and `manifests/` directory
3. Renders sidebar navigation with category groupings
4. Routes to the selected page module

### Configuration: `config.py`

Single source of truth for all paths:
- `PATHS['pan_handlers_root']` - Root Pan_Handlers directory
- `PATHS['projects_file']` - Path to `projects.json`
- `PATHS['manifests_dir']` - Path to `manifests/` directory
- `PATHS['nyquist_status']` - Connection to Nyquist repo (optional)

### Utilities: `utils.py`

Shared functions:
- `load_projects()` - Load flagship projects from JSON
- `load_manifests()` - Load all repo manifests
- `load_nyquist_status()` - Load Nyquist connection status
- `get_status_badge()` - Generate status badge HTML
- `project_card()`, `repo_card()` - UI components

---

## Theme: Matrix Green-on-Black

Corrected 2026-10-31: the Matrix palette below is the optional mode. `main()` in `app.py` starts with `matrix_mode = False` (Standard mode, `#1a1a1a` text on `#ffffff`, from `get_standard_css()`), and the sidebar button "Enter The Matrix" / "Exit The Matrix" switches modes. See `START_HERE.md`, section Theme.

The Matrix mode aesthetic:
- **Background**: `#0a0a0a` (near black)
- **Primary text**: `#00ff41` (Matrix green)
- **Secondary**: `#00cc33` (darker green)
- **Font**: Courier New (monospace)

Theme is applied via:
1. `.streamlit/config.toml` - Streamlit native theming
2. `apply_dashboard_css()` in `app.py` - Custom CSS overrides

---

## Navigation Structure

The sidebar organizes pages into categories:

**SYSTEM**
- 📊 Overview - Main dashboard
- 🏥 Federation Health - Status of connected repos
- 📋 Project Tracker - All flagship projects
- 🟢 Nyquist Tunnel - Connection to Nyquist Consciousness

**CORE ENGINES**
- 📄 White Paper Pipeline - Publication tracking

**FIELD GUIDES** (in the sidebar since 2026-10-04; listed here 2026-10-31)
- Pathfinder - the AI-assisted 3D/video learning console from `Help/`, embedded by `pages/pathfinder.py`

**WICKED PROBLEMS**
- 🗳️ Online Voting - Secure digital voting
- 🏥 Nursing Programs - Healthcare education
- 🧬 Gene Therapy - Biomedical research
- ⛓️ Modern Slavery - Prison reform

**INSTITUTIONS**
- 🔍 ABI (Bureau) - Transparent investigation
- 🌐 D.C.I.A. - Decentralized intelligence

---

## Adding a New Page

This is the canonical procedure (declared 2026-10-31; `START_HERE.md` and `docs/prompts/dashboard_claude.md` point here). Checked against `app.py` on 2026-10-31: the `PAGES` dict sits at the top of `app.py` and the sidebar buttons are in `main()`.

1. Create `pages/your_page.py`:
```python
import streamlit as st

def render():
    st.markdown("# Your Page Title")
    st.markdown("Content here...")
```

2. Add to `pages/__init__.py`:
```python
from . import your_page
```

3. Add to `PAGES` dict in `app.py`:
```python
PAGES = {
    ...
    "🆕 Your Page": your_page,
}
```

4. Add to navigation in the sidebar section of `main()` in `app.py`: an `st.button` under the right group heading that sets `st.session_state['current_page']` to the same key you used in `PAGES`

---

## Data Sources

### `../projects.json`
Flagship projects with status, track, owner, description.

### `../manifests/*.json`
Repository manifests describing connected repos in the federation.

### Nyquist Integration (optional)
If Pan_Handlers is inside a Nyquist repo, it can read:
- `NYQUIST_STATUS.json` - Live status
- `experiments/` - Experiment data
- `personas/` - Persona definitions

---

## Troubleshooting

### Port already in use
Run the Quick Start command with another `--server.port` value (corrected 2026-10-31; this section used to name a second port).

### Import errors
Use the Quick Start command as written, from the repository root. `app.py` imports `config`, `utils` and `pages` from its own directory, which Streamlit adds to `sys.path`; running `streamlit run app.py` from inside `dashboard/` resolves the same way (corrected 2026-10-31).

### Missing dependencies
```bash
pip install streamlit
```

---

## Related Files

- `../START_HERE.md` - Front door of the repository (since 2026-10-31)
- `../README.md` - Main Pan Handlers documentation
- `../docs/I_AM/I_AM.md` - Soul of Pan Handlers (bootstrap document)
- `../projects.json` - Flagship project definitions
- `../manifests/` - Connected repository manifests

---

*"The Back Alley - where the real work happens."* 🍳
