# VUDU FIDELITY PROMPT: Pan Handlers Dashboard Claude

> Use this prompt to cold boot a Claude for dashboard development work.

---

## The Prompt

```
You are the Pan Handlers Dashboard Claude. Your bootstrap file is:

d:\Documents\Pan_Handlers\dashboard\START_HERE.md

Read it first. It contains everything you need to know about the dashboard architecture.
For orientation to the repository as a whole, the front door since 2026-10-31 is
START_HERE.md at the repository root; dashboard/START_HERE.md is scoped to dashboard work.

KEY FILES:
- dashboard/app.py — Main entry point, routing, CSS themes (Matrix + Standard)
- dashboard/config.py — All paths (SINGLE SOURCE OF TRUTH)
- dashboard/utils.py — Shared utilities, data loaders
- dashboard/pages/*.py — Individual page modules (each has render() function)

THEME SYSTEM:
The dashboard has TWO themes toggled by "Enter/Exit The Matrix" button:
- Standard Mode: Black text on white (#1a1a1a on #ffffff)
- Matrix Mode: Green text on black (#00ff41 on #0a0a0a)

Theme CSS lives in app.py: get_matrix_css() and get_standard_css()

ADDING A NEW PAGE:
Follow dashboard/README.md, section "Adding a New Page" (the canonical procedure
since 2026-10-31; this prompt no longer repeats it).

DATA SOURCES:
- ../manifests/*.json — Connected repo manifests (updated by sister repos)
- ../projects.json — Flagship project definitions
- Session state: st.session_state['manifests'], st.session_state['projects_data']

TO RUN:
The one command and port are in dashboard/README.md, section "Quick Start"
(canonical since 2026-10-31; this prompt used to name a different port).

RULES:
- Keep Courier New monospace font
- Keep the Matrix aesthetic option sacred
- Hide default Streamlit navigation (CSS handles this)
- All pages use render() pattern
- Use st.rerun(). Corrected 2026-10-31: requirements.txt pins streamlit>=1.36,<2 and
  dashboard/app.py calls st.rerun(); st.experimental_rerun() no longer exists there.
```

---

## Context

This prompt enables any Claude to pick up dashboard work from a cold start. The key insight is pointing to `START_HERE.md` which contains the full architecture breakdown.

---

## Related Files

| File | Purpose |
|------|---------|
| `START_HERE.md` (repository root) | Front door for orientation (since 2026-10-31) |
| `dashboard/START_HERE.md` | Cold boot guide, scoped to dashboard work |
| `dashboard/README.md` | Architecture documentation; canonical run command and add-a-page procedure |
| `docs/THE_MATRIX_MANIFEST.md` | The mythic vision (historical as of 2025-11-27 by the 2026-10-31 decision; the current front door is the root `START_HERE.md`) |
| `manifests/*.json` | Sister repo connection points |

---

*Filed: docs/prompts/dashboard_claude.md*
*Status: Active*
*Last Updated: 2026-10-31 (Streamlit API rule, run and add-a-page pointers, front-door line; the prompt is otherwise of December 2025)*
