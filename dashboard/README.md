# Pan Handlers Dashboard - The Back Alley

> **Internal operations dashboard for the Pan Handlers federation.**
> This is where the work happens. The public face is at [panhandlers.streamlit.app](https://panhandlers.streamlit.app).

---

## Quick Start

```bash
cd Pan_Handlers/dashboard
streamlit run app.py
```

Visit http://localhost:8501 (or the port shown in terminal).

**FIELD GUIDES → Pathfinder** opens the new AI-assisted 3D/video learning console.
It also runs independently with `python -m streamlit run Help/app.py --server.port 8506`
from the repository root. See [the guide README](../Help/README.md) for notes,
JSON restore/export, and the four pipeline expansion plans.

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
│   ├── about.py              # ℹ️ About page
│   └── projects/             # Individual project pages
│       ├── __init__.py
│       ├── whitepaper.py     # 📄 White Paper Pipeline
│       ├── online_voting.py  # 🗳️ Online Voting System
│       ├── nursing.py        # 🏥 Nursing Programs
│       ├── gene_therapy.py   # 🧬 Gene Therapy Research
│       ├── modern_slavery.py # ⛓️ Prison Reform / Modern Slavery
│       ├── abi.py            # 🔍 American Bureau of Investigation
│       └── dcia.py           # 🌐 Decentralized CIA
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
1. Sets up page config and Matrix theme CSS
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

The dashboard uses a "Matrix" aesthetic:
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

4. Add to navigation in sidebar section of `app.py`

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
```bash
streamlit run app.py --server.port 8510
```

### Import errors
Make sure you're running from `dashboard/` directory:
```bash
cd Pan_Handlers/dashboard
streamlit run app.py
```

### Missing dependencies
```bash
pip install streamlit
```

---

## Related Files

- `../README.md` - Main Pan Handlers documentation
- `../docs/I_AM/I_AM.md` - Soul of Pan Handlers (bootstrap document)
- `../projects.json` - Flagship project definitions
- `../manifests/` - Connected repository manifests

---

*"The Back Alley - where the real work happens."* 🍳
