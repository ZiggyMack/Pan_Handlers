"""
🍳 PAN HANDLERS DASHBOARD — Federation Health Monitor
System Health & Status Dashboard for the Pan Handlers Federation

This dashboard monitors the health of all connected repos,
tracks project progress, and provides system-level insights.

Run: streamlit run Pan_Handlers/dashboard/app.py --server.port 8504
"""

import streamlit as st
from pathlib import Path

# Import config and utils
from config import PATHS, SETTINGS
from utils import load_projects, load_manifests, load_nyquist_status, page_divider

# Import page modules
from pages import overview, federation_health, project_tracker, nyquist_tunnel, about
from pages.projects import whitepaper, online_voting, nursing, gene_therapy, modern_slavery, abi, dcia

# ========== PAGE ROUTING ==========

# Organized by category
PAGES = {
    # === SYSTEM ===
    "📊 Overview": overview,
    "🏥 Federation Health": federation_health,
    "📋 Project Tracker": project_tracker,
    "🟢 Nyquist Tunnel": nyquist_tunnel,

    # === CORE ENGINES ===
    "───── CORE ENGINES ─────": None,  # Separator
    "📄 White Paper Pipeline": whitepaper,

    # === WICKED PROBLEMS ===
    "───── WICKED PROBLEMS ─────": None,  # Separator
    "🗳️ Online Voting": online_voting,
    "🏥 Nursing Programs": nursing,
    "🧬 Gene Therapy": gene_therapy,
    "⛓️ Modern Slavery": modern_slavery,

    # === INSTITUTIONAL REDESIGN ===
    "───── INSTITUTIONS ─────": None,  # Separator
    "🔍 ABI (Bureau)": abi,
    "🌐 D.C.I.A.": dcia,

    # === META ===
    "───────────────────────": None,  # Separator
    "ℹ️ About": about,
}


# ========== STYLING ==========

def apply_dashboard_css():
    """Apply Pan Handlers Dashboard theme - Full Matrix green-on-black."""
    st.markdown("""
    <style>
    /* Hide default Streamlit elements and navigation */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}

    /* Hide the default Streamlit page navigation in sidebar */
    [data-testid="stSidebarNav"] {display: none !important;}
    div[data-testid="stSidebarNav"] {display: none !important;}
    nav[data-testid="stSidebarNav"] {display: none !important;}
    section[data-testid="stSidebarNav"] {display: none !important;}
    ul[data-testid="stSidebarNavItems"] {display: none !important;}

    /* Make main content area wider */
    .main .block-container {
        max-width: 95% !important;
        padding-left: 2rem !important;
        padding-right: 2rem !important;
    }

    /* Fix column widths */
    [data-testid="column"] {
        min-width: 200px !important;
    }

    /* ===== MATRIX THEME - BLACK BACKGROUND EVERYWHERE ===== */
    .stApp,
    .stApp > div,
    .stApp [data-testid="stAppViewContainer"],
    [data-testid="stAppViewContainer"],
    .main,
    .block-container,
    [data-testid="stVerticalBlock"],
    [data-testid="stHorizontalBlock"],
    [data-testid="stHeader"] {
        background-color: #0a0a0a !important;
        background: #0a0a0a !important;
    }

    /* ===== ALL TEXT MATRIX GREEN ===== */
    .stApp p, .stApp span, .stApp label, .stApp li,
    .stApp h1, .stApp h2, .stApp h3, .stApp h4, .stApp h5, .stApp h6,
    .stApp div,
    .main p, .main span, .main label, .main li,
    .main h1, .main h2, .main h3, .main h4, .main h5, .main h6,
    .main div,
    [data-testid="stMarkdownContainer"] p,
    [data-testid="stMarkdownContainer"] li,
    [data-testid="stMarkdownContainer"] {
        color: #00ff41 !important;
    }

    /* Headers */
    h1, h2, h3, h4, h5, h6 {
        color: #00ff41 !important;
        font-family: 'Courier New', monospace;
    }

    /* Strong/bold text */
    strong, b {
        color: #00ff41 !important;
        text-shadow: 0 0 5px rgba(0,255,65,0.5);
    }

    /* Links */
    a {
        color: #00cc33 !important;
    }
    a:hover {
        color: #00ff41 !important;
        text-shadow: 0 0 10px rgba(0,255,65,0.5);
    }

    /* ===== METRIC CARDS ===== */
    [data-testid="stMetricValue"] {
        color: #00ff41 !important;
        font-family: 'Courier New', monospace;
    }
    [data-testid="stMetricLabel"] {
        color: #00ff41 !important;
    }
    [data-testid="stMetricDelta"] {
        color: #00cc33 !important;
    }

    /* ===== EXPANDERS ===== */
    [data-testid="stExpander"] {
        background-color: #0d0d0d !important;
        border: 1px solid #00ff41 !important;
    }
    [data-testid="stExpander"] * {
        color: #00ff41 !important;
    }

    /* ===== SELECT BOXES & INPUTS ===== */
    .stSelectbox > div > div,
    .stTextInput > div > div > input,
    .stMultiSelect > div {
        background-color: #0d0d0d !important;
        color: #00ff41 !important;
        border-color: #00ff41 !important;
    }

    /* ===== BUTTONS ===== */
    .stButton > button {
        background-color: #0d0d0d !important;
        color: #00ff41 !important;
        border: 2px solid #00ff41 !important;
        font-family: 'Courier New', monospace;
    }
    .stButton > button:hover {
        background-color: #004d1a !important;
        box-shadow: 0 0 15px rgba(0,255,65,0.4);
    }

    /* ===== INFO/WARNING/ERROR BOXES ===== */
    .stAlert {
        background-color: rgba(0,255,65,0.1) !important;
        border: 1px solid #00ff41 !important;
        color: #00ff41 !important;
    }

    /* Pan Handlers Dashboard Theme */
    .dashboard-title {
        font-size: 2.5em;
        font-weight: bold;
        color: #00ff41 !important;
        text-shadow: 0 0 10px rgba(0,255,65,0.5);
        margin-bottom: 0.2em;
        font-family: 'Courier New', monospace;
    }

    .dashboard-subtitle {
        color: #00ff41;
        font-size: 1.1em;
        margin-bottom: 1em;
        font-family: 'Courier New', monospace;
    }

    .health-card {
        background: linear-gradient(135deg, rgba(0,255,65,0.08) 0%, rgba(0,204,51,0.03) 100%);
        border: 2px solid #00ff41;
        border-radius: 12px;
        padding: 1.5em;
        margin-bottom: 1em;
        box-shadow: 0 0 20px rgba(0,255,65,0.2);
    }

    .health-card h3 {
        color: #00ff41 !important;
        margin-top: 0;
        font-family: 'Courier New', monospace;
    }

    .status-good {
        color: #00ff41 !important;
    }

    .status-warning {
        color: #f4a261 !important;
    }

    .status-critical {
        color: #e74c3c !important;
    }

    .metric-box {
        background: linear-gradient(135deg, rgba(0,255,65,0.1) 0%, rgba(0,255,65,0.05) 100%);
        border: 2px solid #00ff41;
        border-radius: 10px;
        padding: 1em;
        text-align: center;
    }

    .metric-value {
        font-size: 2.5em;
        font-weight: bold;
        color: #00ff41 !important;
        font-family: 'Courier New', monospace;
    }

    .metric-label {
        color: #00cc33 !important;
        font-size: 0.9em;
    }

    .section-header {
        color: #00ff41 !important;
        font-size: 1.4em;
        font-weight: bold;
        margin-top: 1.5em;
        margin-bottom: 0.8em;
        font-family: 'Courier New', monospace;
        border-bottom: 2px solid #00ff41;
        padding-bottom: 0.3em;
    }

    .tunnel-card {
        background: linear-gradient(135deg, rgba(155,89,182,0.1) 0%, rgba(52,152,219,0.05) 100%);
        border: 2px solid #9b59b6;
        border-radius: 10px;
        padding: 1.2em;
        margin: 0.8em 0;
    }

    .tunnel-card h4 {
        color: #9b59b6 !important;
        margin-top: 0;
    }

    /* Sidebar styling */
    section[data-testid="stSidebar"] {
        background: linear-gradient(180deg, #0a0a0a, #1a1a1a) !important;
    }

    section[data-testid="stSidebar"] * {
        color: #00ff41 !important;
    }

    section[data-testid="stSidebar"] h1,
    section[data-testid="stSidebar"] h2,
    section[data-testid="stSidebar"] h3 {
        color: #00ff41 !important;
    }

    /* Category separators in sidebar */
    .sidebar-separator {
        color: #006600 !important;
        font-size: 0.8em;
        text-align: center;
        padding: 0.3em 0;
        border-top: 1px solid #004400;
        border-bottom: 1px solid #004400;
        margin: 0.5em 0;
    }

    /* Page divider */
    .page-divider {
        border-top: 2px solid #00ff41;
        margin: 1.5em 0;
        opacity: 0.5;
    }

    /* Horizontal rules */
    hr {
        border-color: #00ff41 !important;
    }

    /* Code blocks */
    code {
        background: rgba(0,255,65,0.1) !important;
        color: #00ff41 !important;
        font-family: 'Courier New', monospace;
    }

    /* Radio buttons */
    .stRadio > div {
        background-color: transparent !important;
    }
    .stRadio label {
        color: #00ff41 !important;
    }
    </style>
    """, unsafe_allow_html=True)


# ========== MAIN ==========

def main():
    st.set_page_config(
        page_title="Pan Handlers Dashboard",
        page_icon="🍳",
        layout="wide",
    )

    apply_dashboard_css()

    # Load data into session state
    st.session_state['projects_data'] = load_projects()
    st.session_state['manifests'] = load_manifests()
    st.session_state['nyquist_status'] = load_nyquist_status()

    # Sidebar navigation
    with st.sidebar:
        st.markdown("### 🍳 Pan Handlers")
        st.markdown("*The Back Alley*")
        st.markdown("---")

        # Matrix home button - link to public Pan Handlers
        st.markdown("[![Enter The Matrix](https://img.shields.io/badge/🟢_Enter_The_Matrix-00ff41?style=for-the-badge&labelColor=0a0a0a)](https://panhandlers.streamlit.app)")
        st.markdown("---")

        # Custom navigation with category labels
        st.markdown("**SYSTEM**")
        system_pages = ["📊 Overview", "🏥 Federation Health", "📋 Project Tracker", "🟢 Nyquist Tunnel"]

        st.markdown("**CORE ENGINES**")
        core_pages = ["📄 White Paper Pipeline"]

        st.markdown("**WICKED PROBLEMS**")
        wicked_pages = ["🗳️ Online Voting", "🏥 Nursing Programs", "🧬 Gene Therapy", "⛓️ Modern Slavery"]

        st.markdown("**INSTITUTIONS**")
        institution_pages = ["🔍 ABI (Bureau)", "🌐 D.C.I.A."]

        # All pages for selection
        all_pages = system_pages + core_pages + wicked_pages + institution_pages + ["ℹ️ About"]

        page_selection = st.radio(
            "Navigate:",
            all_pages,
            label_visibility="collapsed"
        )

        st.markdown("---")

        # Quick stats in sidebar
        manifests = st.session_state.get('manifests', [])
        projects_data = st.session_state.get('projects_data', {})

        st.markdown(f"**Repos Connected:** {len(manifests)}")
        if projects_data:
            st.markdown(f"**Flagship Projects:** {len(projects_data.get('flagship_projects', []))}")

        # Health indicator
        st.markdown("---")
        nyquist_connected = PATHS['nyquist_status'].exists()
        if nyquist_connected:
            st.markdown("🟢 **Nyquist:** Connected")
        else:
            st.markdown("🔴 **Nyquist:** Disconnected")

        st.markdown("---")
        st.markdown("*System Health Monitor*")
        st.markdown("*via VUDU Network*")

    # Render selected page
    page_module = PAGES.get(page_selection)
    if page_module and hasattr(page_module, 'render'):
        page_module.render()
    elif page_module is None:
        st.info("Select a page from the sidebar.")
    else:
        st.error(f"Page '{page_selection}' not found")


if __name__ == "__main__":
    main()
