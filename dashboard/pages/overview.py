"""
OVERVIEW PAGE — Federation Health At-a-Glance

The main dashboard showing overall system health,
project status, and key metrics.
"""

import streamlit as st
from config import PATHS, SETTINGS
from utils import (
    page_divider, section_header, get_status_badge,
    get_project_stats, get_nyquist_integration_stats
)


def render():
    """Render the Overview page."""
    projects_data = st.session_state.get('projects_data', {})
    manifests = st.session_state.get('manifests', [])

    # Header
    st.markdown('<div class="dashboard-title">🍳 Pan Handlers Federation</div>', unsafe_allow_html=True)
    st.markdown('<div class="dashboard-subtitle">System Health Dashboard — "Neither could have done it alone."</div>', unsafe_allow_html=True)

    # === HEALTH STATUS BANNER ===
    nyquist_connected = PATHS['nyquist_status'].exists()
    if nyquist_connected:
        st.markdown("""
        <div style="background: linear-gradient(135deg, rgba(0,255,65,0.15) 0%, rgba(42,157,143,0.1) 100%);
                    border: 2px solid #00ff41; border-radius: 12px; padding: 1em; text-align: center; margin-bottom: 1.5em;">
            <span style="font-size: 1.5em;">🟢</span>
            <span style="font-size: 1.3em; font-weight: bold; color: #00ff41; margin-left: 0.5em;">
                ALL SYSTEMS OPERATIONAL
            </span>
        </div>
        """, unsafe_allow_html=True)
    else:
        st.markdown("""
        <div style="background: linear-gradient(135deg, rgba(244,162,97,0.15) 0%, rgba(231,111,81,0.1) 100%);
                    border: 2px solid #f4a261; border-radius: 12px; padding: 1em; text-align: center; margin-bottom: 1.5em;">
            <span style="font-size: 1.5em;">🟡</span>
            <span style="font-size: 1.3em; font-weight: bold; color: #f4a261; margin-left: 0.5em;">
                NYQUIST CONNECTION UNAVAILABLE
            </span>
        </div>
        """, unsafe_allow_html=True)

    page_divider()

    # === KEY METRICS ROW ===
    col1, col2, col3, col4 = st.columns(4)

    project_stats = get_project_stats(projects_data)
    nyquist_stats = get_nyquist_integration_stats()

    with col1:
        st.markdown(f"""
        <div class="metric-box">
            <div class="metric-value">{len(manifests)}</div>
            <div class="metric-label">Repos Connected</div>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown(f"""
        <div class="metric-box">
            <div class="metric-value">{project_stats.get('total', 0)}</div>
            <div class="metric-label">Flagship Projects</div>
        </div>
        """, unsafe_allow_html=True)

    with col3:
        active = project_stats.get('active', 0) + project_stats.get('in_prep', 0)
        st.markdown(f"""
        <div class="metric-box">
            <div class="metric-value">{active}</div>
            <div class="metric-label">Active / In Prep</div>
        </div>
        """, unsafe_allow_html=True)

    with col4:
        workshop = int(nyquist_stats.get('workshop_ready', 0) * 100)
        st.markdown(f"""
        <div class="metric-box">
            <div class="metric-value">{workshop}%</div>
            <div class="metric-label">Publication Ready</div>
        </div>
        """, unsafe_allow_html=True)

    page_divider()

    # === CONNECTED REPOS STATUS ===
    section_header("Connected Repositories", "🌌")

    # Define color palette for different repo types
    REPO_COLORS = {
        'nyquist': {'bg': 'rgba(155, 89, 182, 0.15)', 'border': '#9b59b6', 'text': '#9b59b6'},  # Purple - Core Engine
        'cfa': {'bg': 'rgba(52, 152, 219, 0.15)', 'border': '#3498db', 'text': '#3498db'},      # Blue - Meta Framework
        'abi': {'bg': 'rgba(231, 76, 60, 0.15)', 'border': '#e74c3c', 'text': '#e74c3c'},       # Red - Investigation
        'dcia': {'bg': 'rgba(230, 126, 34, 0.15)', 'border': '#e67e22', 'text': '#e67e22'},     # Orange - Intelligence
        'ndo': {'bg': 'rgba(46, 204, 113, 0.15)', 'border': '#2ecc71', 'text': '#2ecc71'},      # Green - Data
        'avlar': {'bg': 'rgba(241, 196, 15, 0.15)', 'border': '#f1c40f', 'text': '#d4ac0d'},    # Yellow - Art/Ritual
        'gene': {'bg': 'rgba(26, 188, 156, 0.15)', 'border': '#1abc9c', 'text': '#1abc9c'},     # Teal - Gene Therapy
        'slavery': {'bg': 'rgba(127, 140, 141, 0.15)', 'border': '#7f8c8d', 'text': '#7f8c8d'}, # Gray - Liberation
        'voting': {'bg': 'rgba(142, 68, 173, 0.15)', 'border': '#8e44ad', 'text': '#8e44ad'},   # Deep Purple - Voting
        'nursing': {'bg': 'rgba(243, 156, 18, 0.15)', 'border': '#f39c12', 'text': '#f39c12'}, # Amber - Nursing
    }
    DEFAULT_COLOR = {'bg': 'rgba(0, 255, 65, 0.1)', 'border': '#00ff41', 'text': '#00ff41'}

    def get_repo_color(repo_name):
        """Get color scheme based on repo name."""
        repo_lower = repo_name.lower()
        for key, colors in REPO_COLORS.items():
            if key in repo_lower:
                return colors
        return DEFAULT_COLOR

    if manifests:
        # Display in rows of 3 for better readability
        cols_per_row = 3
        for row_start in range(0, len(manifests), cols_per_row):
            row_manifests = manifests[row_start:row_start + cols_per_row]
            cols = st.columns(cols_per_row)

            for i, manifest in enumerate(row_manifests):
                with cols[i]:
                    repo_name = manifest.get('repo', 'Unknown')
                    display_name = manifest.get('display_name', repo_name)
                    status = manifest.get('status', 'Unknown')
                    colors = get_repo_color(repo_name)

                    st.markdown(f"""
                    <div style="background: {colors['bg']}; border: 2px solid {colors['border']};
                                border-radius: 12px; padding: 1.2em; margin-bottom: 1em; min-height: 180px;">
                        <h4 style="color: {colors['text']}; margin: 0 0 0.5em 0; font-size: 1.1em;">{display_name}</h4>
                        <p style="color: #666; font-size: 0.85em; margin: 0.3em 0;"><strong>Role:</strong> {manifest.get('role', 'N/A')[:80]}...</p>
                        <p style="margin: 0.5em 0;">{get_status_badge(status)}</p>
                    </div>
                    """, unsafe_allow_html=True)
    else:
        st.info("No repository manifests loaded.")

    page_divider()

    # === PROJECT STATUS SUMMARY ===
    section_header("Project Status Summary", "📋")

    if projects_data and 'flagship_projects' in projects_data:
        projects = projects_data['flagship_projects']

        # Status breakdown
        col1, col2 = st.columns([1, 2])

        with col1:
            st.markdown("""
            <div style="background: rgba(0,0,0,0.3); border-radius: 10px; padding: 1em;">
                <h4 style="color: #00ff41; margin-top: 0;">By Status</h4>
            """, unsafe_allow_html=True)

            status_counts = {}
            for p in projects:
                s = p.get('status', 'Unknown')
                status_counts[s] = status_counts.get(s, 0) + 1

            for status, count in sorted(status_counts.items(), key=lambda x: -x[1]):
                badge = get_status_badge(status)
                st.markdown(f"<p style='margin: 0.3em 0;'>{badge} × {count}</p>", unsafe_allow_html=True)

            st.markdown("</div>", unsafe_allow_html=True)

        with col2:
            st.markdown("""
            <div style="background: rgba(0,0,0,0.3); border-radius: 10px; padding: 1em;">
                <h4 style="color: #00ff41; margin-top: 0;">By Track</h4>
            """, unsafe_allow_html=True)

            track_counts = project_stats.get('by_track', {})
            for track, count in sorted(track_counts.items(), key=lambda x: -x[1]):
                bar_width = (count / max(track_counts.values())) * 100
                st.markdown(f"""
                <div style="margin: 0.5em 0;">
                    <div style="color: #888; font-size: 0.9em;">{track}</div>
                    <div style="background: rgba(42,157,143,0.3); border-radius: 4px; height: 20px; width: 100%;">
                        <div style="background: #2a9d8f; border-radius: 4px; height: 100%; width: {bar_width}%;
                                    display: flex; align-items: center; padding-left: 0.5em;">
                            <span style="color: white; font-size: 0.8em; font-weight: bold;">{count}</span>
                        </div>
                    </div>
                </div>
                """, unsafe_allow_html=True)

            st.markdown("</div>", unsafe_allow_html=True)
    else:
        st.info("No project data available.")

    page_divider()

    # === NYQUIST INTEGRATION STATUS ===
    section_header("Nyquist Tunnel Status", "🟢")

    col1, col2, col3 = st.columns(3)

    with col1:
        connected = "🟢 Connected" if nyquist_connected else "🔴 Disconnected"
        st.markdown(f"""
        <div class="tunnel-card">
            <h4>Core Engine</h4>
            <p style="font-size: 1.2em; font-weight: bold;">{connected}</p>
            <p style="color: #666; font-size: 0.9em;">Nyquist Consciousness repo</p>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        armada = nyquist_stats.get('armada_runs', 0)
        st.markdown(f"""
        <div class="tunnel-card">
            <h4>AI Armada</h4>
            <p style="font-size: 1.2em; font-weight: bold;">{armada} Runs</p>
            <p style="color: #666; font-size: 0.9em;">S7 Temporal stability tests</p>
        </div>
        """, unsafe_allow_html=True)

    with col3:
        arxiv = int(nyquist_stats.get('arxiv_progress', 0) * 100)
        st.markdown(f"""
        <div class="tunnel-card">
            <h4>arXiv Progress</h4>
            <p style="font-size: 1.2em; font-weight: bold;">{arxiv}%</p>
            <p style="color: #666; font-size: 0.9em;">Preprint preparation</p>
        </div>
        """, unsafe_allow_html=True)

    # Footer
    page_divider()
    st.markdown("""
    <div style="text-align: center; color: #00ff41; font-family: 'Courier New', monospace; margin-top: 2em; opacity: 0.8;">
        <p><strong>🍳 PAN HANDLERS FEDERATION DASHBOARD</strong></p>
        <p>"These are the things we built together that neither could have done alone."</p>
    </div>
    """, unsafe_allow_html=True)
