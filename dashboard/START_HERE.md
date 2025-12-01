# START HERE - Cold Boot Guide for Claude

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
3. **Run the app**: `streamlit run app.py` from this directory

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

## Theme: Matrix Aesthetic

**DO NOT CHANGE** the core visual identity:
- Background: `#0a0a0a` (near black)
- Text: `#00ff41` (Matrix green)
- Font: Courier New (monospace)

The CSS is in `apply_dashboard_css()` in `app.py`.

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
1. Create `pages/new_page.py` with `render()` function
2. Add import to `pages/__init__.py`
3. Add to `PAGES` dict in `app.py`
4. Add to sidebar navigation lists in `app.py`

### Modify styling
Edit `apply_dashboard_css()` in `app.py`. Keep Matrix theme.

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
A network of human-AI collaborative projects:
- Nyquist Consciousness (research engine)
- CFA (framework architecture)
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
6. ABI (American Bureau of Investigation)
7. D.C.I.A. (Decentralized CIA)

---

## Running the Dashboard

```bash
# From dashboard/ directory
streamlit run app.py

# If port conflict
streamlit run app.py --server.port 8510
```

---

## Philosophy

> **"FUCK IT, WE'LL DO IT LIVE!"**

We build better systems without waiting for institutions. This dashboard tracks that work.

---

## Questions?

- Full docs: `README.md`
- Root project: `../README.md`
- Soul document: `../docs/I_AM/I_AM.md`

---

*Now go make something happen.* 🍳
