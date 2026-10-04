"""Shared presentation for the standalone and embedded Pathfinder console.

The palette and editorial headings follow the Nyquist dashboard. Keep the
Streamlit controls native so keyboard navigation, reruns and the mobile sidebar
continue to work. Explicit widget selectors also override the older federation
dashboard's broad text rules when this console is embedded there.
"""

import streamlit as st


_LIGHT = {
    "paper": "#ffffff",
    "surface": "#ffffff",
    "surface-soft": "#f4f6f5",
    "ink": "#243936",
    "muted": "#62706a",
    "line": "#d7ddd4",
    "accent": "#2a9d8f",
    "accent-text": "#176b62",
    "accent-soft": "#e7f2ed",
    "deep": "#264653",
    "orange": "#f4a261",
    "hero": "#173b3b",
    "hero-text": "#fbfaf3",
    "hero-muted": "#d3e3dc",
    "sidebar": "#0a0a0a",
    "sidebar-ink": "#e8efea",
    "sidebar-muted": "#a6bdb3",
    "sidebar-surface": "#213532",
    "sidebar-line": "#38504a",
    "heading-font": "Georgia, 'Times New Roman', serif",
    "purple": "#7c3aed",
    "purple-soft": "#f3e8ff",
    "purple-ink": "#6d28d9",
    "green": "#10a37f",
    "green-soft": "#e8f5e9",
    "green-ink": "#087555",
    "blue": "#4285f4",
    "blue-soft": "#e3f2fd",
    "blue-ink": "#225ec0",
    "amber": "#f97316",
    "amber-soft": "#fff7ed",
    "amber-ink": "#b74a09",
}

_MATRIX = {
    "paper": "#080e0b",
    "surface": "#101b14",
    "surface-soft": "#14261b",
    "ink": "#baf5c7",
    "muted": "#91b69a",
    "line": "#2d5437",
    "accent": "#00ff41",
    "accent-text": "#67ed89",
    "accent-soft": "#173423",
    "deep": "#8ef8a7",
    "orange": "#f4a261",
    "hero": "#071a0d",
    "hero-text": "#baffcb",
    "hero-muted": "#9acaa5",
    "sidebar": "#070e09",
    "sidebar-ink": "#baf5c7",
    "sidebar-muted": "#91b69a",
    "sidebar-surface": "#132a1a",
    "sidebar-line": "#2d5437",
    "heading-font": "'Courier New', Consolas, monospace",
    "purple": "#b38af5",
    "purple-soft": "#251b35",
    "purple-ink": "#d0b6fb",
    "green": "#40d5a8",
    "green-soft": "#123026",
    "green-ink": "#81e5be",
    "blue": "#79adff",
    "blue-soft": "#142a40",
    "blue-ink": "#acd0ff",
    "amber": "#ffa566",
    "amber-soft": "#35261b",
    "amber-ink": "#ffc299",
}


_CSS = """
/* Application surfaces. Do not hide the header or force the sidebar open. */
.stApp,
.stApp [data-testid="stAppViewContainer"],
.stApp [data-testid="stAppViewContainer"] > div,
.stApp [data-testid="stHeader"] {
    background: var(--help-paper) !important;
    color: var(--help-ink) !important;
}
.stApp :is(.main, [data-testid="stMain"]),
.stApp :is(.main, [data-testid="stMain"]) > div,
.stApp .block-container,
.stApp [data-testid="stVerticalBlock"],
.stApp [data-testid="stHorizontalBlock"],
.stApp [data-testid="stToolbar"] {
    background: transparent !important;
}
.stApp :is(.main, [data-testid="stMain"]) .block-container {
    max-width: 1400px !important;
    padding: 2.5rem 3rem 4rem !important;
}
.stApp :is(.main, [data-testid="stMain"]) :is([data-testid="column"], [data-testid="stColumn"]) {
    min-width: 0 !important;
}
.stApp [data-testid="stDecoration"] { display: none; }
.stApp [data-testid="stAppDeployButton"],
.stApp .stAppDeployButton { display: none; }
#MainMenu, footer { visibility: hidden; }
.stApp [data-testid="stSidebarNav"] { display: none !important; }
.stApp [data-testid="stHeader"] button,
.stApp [data-testid="stSidebarCollapsedControl"] button,
.stApp [data-testid="collapsedControl"] button {
    color: var(--help-accent-text) !important;
}

/* Content typography; no blanket selectors for all divs or descendants. */
.stApp :is(.main, [data-testid="stMain"]) :is(p, li, label, h1, h2, h3, h4, h5, h6),
.stApp :is(.main, [data-testid="stMain"]) [data-testid="stMarkdownContainer"] {
    color: var(--help-ink) !important;
}
.stApp :is(.main, [data-testid="stMain"]) :is(p, li) {
    line-height: 1.65;
}
.stApp :is(.main, [data-testid="stMain"]) :is(h1, h2, h3, h4) {
    font-family: var(--help-heading-font) !important;
    font-weight: 500 !important;
    letter-spacing: -0.025em;
    text-wrap: balance;
}
.stApp :is(.main, [data-testid="stMain"]) h2 { font-size: 1.8rem; }
.stApp :is(.main, [data-testid="stMain"]) h3 { font-size: 1.3rem; }
.stApp :is(.main, [data-testid="stMain"]) :is(strong, b) {
    color: var(--help-deep) !important;
    text-shadow: none !important;
}
.stApp :is(.main, [data-testid="stMain"]) :is(em, i) { color: inherit !important; }
.stApp :is(.main, [data-testid="stMain"]) a {
    color: var(--help-accent-text) !important;
    text-underline-offset: 0.2em;
}
.stApp :is(.main, [data-testid="stMain"]) hr {
    border-color: var(--help-line) !important;
    margin: 1.6rem 0 !important;
}
.stApp [data-testid="stCaptionContainer"] {
    /* Streamlit adds opacity: .6; our muted palette already supplies contrast. */
    opacity: 1 !important;
}
.stApp :is(.main, [data-testid="stMain"]) [data-testid="stCaptionContainer"] p,
.stApp :is(.main, [data-testid="stMain"]) .help-muted {
    color: var(--help-muted) !important;
    font-size: 0.86rem;
}
.stApp :is(.main, [data-testid="stMain"]) code {
    background: var(--help-surface-soft) !important;
    color: var(--help-accent-text) !important;
    border-radius: 3px;
}
.stApp :is(.main, [data-testid="stMain"]) pre,
.stApp :is(.main, [data-testid="stMain"]) [data-testid="stCode"] {
    background: var(--help-surface-soft) !important;
    border-radius: 6px;
}
.stApp :is(.main, [data-testid="stMain"]) pre code {
    white-space: pre;
    line-height: 1.5;
}

/* The dark rail follows Nyquist's nested navigation treatment. */
.stApp section[data-testid="stSidebar"] {
    background: var(--help-sidebar) !important;
    border-right: 1px solid var(--help-sidebar-line);
}
.stApp section[data-testid="stSidebar"] :is(p, span, label, li, a, strong, b, em, code),
.stApp section[data-testid="stSidebar"] [data-testid="stMarkdownContainer"] {
    color: var(--help-sidebar-ink) !important;
    text-shadow: none !important;
}
.stApp section[data-testid="stSidebar"] :is(h1, h2, h3, h4) {
    color: var(--help-orange) !important;
    font-family: var(--help-heading-font) !important;
    font-weight: 500 !important;
}
.stApp section[data-testid="stSidebar"] [data-testid="stCaptionContainer"] p,
.stApp section[data-testid="stSidebar"] .help-muted {
    color: var(--help-sidebar-muted) !important;
}
.stApp section[data-testid="stSidebar"] hr {
    border-color: var(--help-sidebar-line) !important;
    opacity: 1;
}
.stApp section[data-testid="stSidebar"] [data-baseweb="radio"] {
    padding: 0.28rem 0;
}
.stApp section[data-testid="stSidebar"] [data-baseweb="radio"]:has(input:checked) {
    background: var(--help-sidebar-surface);
    border-radius: 5px;
}
.stApp section[data-testid="stSidebar"] [data-baseweb="radio"] p {
    font-size: 0.9rem;
}
.stApp section[data-testid="stSidebar"] [data-baseweb="select"] > div,
.stApp section[data-testid="stSidebar"] [data-baseweb="input"],
.stApp section[data-testid="stSidebar"] [data-baseweb="base-input"] {
    background: var(--help-sidebar-surface) !important;
    color: var(--help-sidebar-ink) !important;
    border-color: var(--help-sidebar-line) !important;
}
.stApp section[data-testid="stSidebar"] :is(input, textarea) {
    color: var(--help-sidebar-ink) !important;
    background: var(--help-sidebar-surface) !important;
}
.stApp section[data-testid="stSidebar"] :is(.stButton, .stDownloadButton) > button {
    background: var(--help-sidebar-surface) !important;
    color: var(--help-sidebar-ink) !important;
    border: 1px solid var(--help-sidebar-line) !important;
    box-shadow: none !important;
}
.stApp section[data-testid="stSidebar"] .stButton > button[kind="primary"] {
    background: #2a9d8f25 !important;
    border-color: var(--help-accent) !important;
    border-left: 3px solid var(--help-orange) !important;
}
.stApp section[data-testid="stSidebar"] .stButton > button[kind="primary"] p {
    font-weight: 700;
}
.stApp section[data-testid="stSidebar"] [data-testid="stExpander"] {
    background: var(--help-sidebar-surface) !important;
    border-color: var(--help-sidebar-line) !important;
}
.stApp section[data-testid="stSidebar"] [data-testid="stExpander"] summary {
    color: var(--help-sidebar-ink) !important;
}
.stApp section[data-testid="stSidebar"] [data-testid="stSidebarCollapseButton"] button {
    color: var(--help-sidebar-ink) !important;
}

/* Reusable editorial components. Specificity survives the host dashboard CSS. */
.stApp .help-hero {
    position: relative;
    overflow: hidden;
    padding: clamp(1.5rem, 3.5vw, 3.1rem);
    margin: 0 0 1.25rem;
    border: 1px solid var(--help-deep);
    border-radius: 10px;
    background: radial-gradient(ellipse at 100% 0%, #2a9d8f26, transparent 60%), var(--help-hero) !important;
}
.stApp :is(.main, [data-testid="stMain"]) .help-hero h1 {
    color: var(--help-hero-text) !important;
    font-size: clamp(2.2rem, 4.1vw, 3.85rem);
    line-height: 1.08;
    border: 0;
    padding: 0;
    margin: 0.55rem 0 1rem;
    max-width: 920px;
}
.stApp :is(.main, [data-testid="stMain"]) .help-hero p {
    color: var(--help-hero-muted) !important;
    font-size: 1.02rem;
    max-width: 760px;
    margin: 0;
    line-height: 1.7;
}
.stApp :is(.main, [data-testid="stMain"]) :is(.help-eyebrow, .help-kicker) {
    color: var(--help-accent-text) !important;
    font-family: 'Courier New', Consolas, monospace;
    font-size: 0.71rem;
    font-weight: 700;
    line-height: 1.5;
    letter-spacing: 0.13em;
    text-transform: uppercase;
}
.stApp :is(.main, [data-testid="stMain"]) .help-hero .help-eyebrow {
    color: var(--help-orange) !important;
}
.stApp .help-kicker { margin: 1.25rem 0 0.45rem; }
.stApp .help-path-grid {
    display: grid;
    grid-template-columns: repeat(4, minmax(0, 1fr));
    gap: 0.85rem;
    margin: 0.7rem 0 1.3rem;
}
.stApp .help-card {
    position: relative;
    height: 100%;
    padding: 1.15rem;
    border: 1px solid var(--help-line);
    border-radius: 7px;
    background: var(--help-surface) !important;
}
.stApp .help-card-active {
    border-color: var(--help-accent);
    box-shadow: inset 0 3px 0 var(--help-accent);
    background: var(--help-accent-soft) !important;
}
.stApp .help-card .help-kicker { margin: 0; }
.stApp .help-card .help-badge { margin-top: 0.9rem; }
.stApp :is(.main, [data-testid="stMain"]) .help-card h3 {
    margin: 0.65rem 0 0.45rem;
    padding: 0;
    font-size: 1.4rem;
    color: var(--help-deep) !important;
}
.stApp :is(.main, [data-testid="stMain"]) .help-card p {
    font-size: 0.85rem;
    line-height: 1.6;
    margin: 0;
}
.stApp :is(.main, [data-testid="stMain"]) .help-badge {
    display: inline-block;
    padding: 0.2rem 0.45rem;
    border: 1px solid var(--help-line);
    border-radius: 3px;
    color: var(--help-muted) !important;
    font-family: 'Courier New', Consolas, monospace;
    font-size: 0.63rem;
    font-weight: 700;
    letter-spacing: 0.07em;
    text-transform: uppercase;
}
.stApp :is(.main, [data-testid="stMain"]) .help-card-active .help-badge {
    color: var(--help-accent-text) !important;
    border-color: var(--help-accent);
}
.stApp .help-callout {
    padding: 1rem 1.2rem;
    margin: 0.8rem 0 1.2rem;
    background: var(--help-accent-soft) !important;
    border: 1px solid var(--help-line);
    border-left: 3px solid var(--help-accent);
    border-radius: 0 5px 5px 0;
    font-size: 0.91rem;
    line-height: 1.65;
}
.stApp :is(.main, [data-testid="stMain"]) .help-callout {
    color: var(--help-ink) !important;
}
.stApp .help-route-strip {
    display: flex;
    flex-wrap: wrap;
    align-items: center;
    gap: 0.5rem;
    margin: 1.2rem 0 0;
}
.stApp :is(.main, [data-testid="stMain"]) .help-route-strip span {
    display: inline-block;
    padding: 0.25rem 0.65rem;
    border: 1px solid var(--help-line);
    border-radius: 3px;
    color: var(--help-ink) !important;
    font-family: 'Courier New', Consolas, monospace;
    font-size: 0.73rem;
}
.stApp :is(.main, [data-testid="stMain"]) .help-hero .help-route-strip span {
    color: var(--help-hero-muted) !important;
    border-color: #719b8c66;
}
.stApp .help-metrics {
    display: grid;
    grid-template-columns: repeat(3, minmax(0, 1fr));
    gap: 0;
    border: 1px solid var(--help-line);
    border-radius: 6px;
    background: var(--help-surface) !important;
    margin: 1rem 0 1.3rem;
}
.stApp .help-metric { padding: 1rem 1.25rem; }
.stApp .help-metric + .help-metric { border-left: 1px solid var(--help-line); }
.stApp :is(.main, [data-testid="stMain"]) .help-metric strong {
    display: block;
    font-size: 1.6rem;
    font-family: var(--help-heading-font);
    font-weight: 500;
    line-height: 1.3;
    color: var(--help-deep) !important;
}
.stApp :is(.main, [data-testid="stMain"]) .help-metric span {
    display: block;
    color: var(--help-muted) !important;
    font-size: 0.77rem;
    margin-top: 0.2rem;
}
.stApp .help-pipeline {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(150px, 1fr));
    gap: 0.7rem;
    margin: 1rem 0;
}
/* Armada-style overview: colored provider headers over compact capability rows. */
.stApp .help-armada-grid {
    display: grid;
    grid-template-columns: repeat(4, minmax(0, 1fr));
    align-items: stretch;
    gap: 1.1rem;
    margin: 0.7rem 0 1.15rem;
}
.stApp .help-pipeline-column {
    --path-color: var(--help-purple);
    --path-surface: var(--help-purple-soft);
    --path-ink: var(--help-purple-ink);
    display: flex;
    flex-direction: column;
    min-width: 0;
}
.stApp .help-pipeline-column[data-path="forge"] {
    --path-color: var(--help-amber);
    --path-surface: var(--help-amber-soft);
    --path-ink: var(--help-amber-ink);
}
.stApp .help-pipeline-column[data-path="invoke"] {
    --path-color: var(--help-blue);
    --path-surface: var(--help-blue-soft);
    --path-ink: var(--help-blue-ink);
}
.stApp .help-pipeline-column[data-path="comfyui"] {
    --path-color: var(--help-green);
    --path-surface: var(--help-green-soft);
    --path-ink: var(--help-green-ink);
}
.stApp .help-pipeline-head {
    padding: 0.95rem 0.9rem;
    margin-bottom: 0.6rem;
    border: 2px solid var(--path-color);
    border-radius: 10px;
    background: var(--path-surface) !important;
}
.stApp :is(.main, [data-testid="stMain"]) .help-pipeline-head h3 {
    margin: 0 0 0.35rem;
    padding: 0;
    color: var(--path-ink) !important;
    font-family: inherit !important;
    font-size: 1.07rem;
    font-weight: 700 !important;
    letter-spacing: -0.02em;
    line-height: 1.4;
}
.stApp :is(.main, [data-testid="stMain"]) .help-pipeline-head h3::before {
    content: "";
    display: inline-block;
    width: 0.65rem;
    height: 0.65rem;
    margin-right: 0.45rem;
    border-radius: 50%;
    background: var(--path-color);
}
.stApp :is(.main, [data-testid="stMain"]) .help-pipeline-head p {
    margin: 0 0 0.55rem;
    color: var(--help-ink) !important;
    font-size: 0.83rem;
    line-height: 1.5;
}
.stApp :is(.main, [data-testid="stMain"]) .help-pipeline-head .help-badge {
    color: var(--path-ink) !important;
    background: var(--help-surface) !important;
    border-color: var(--path-color);
    font-size: 0.61rem;
    letter-spacing: 0.04em;
}
.stApp .help-capability-row {
    --row-color: var(--help-purple-ink);
    --row-surface: var(--help-purple-soft);
    display: grid;
    grid-template-columns: 0.5rem 3.55rem minmax(0, 1fr);
    align-items: start;
    column-gap: 0.4rem;
    padding: 0.28rem 0.05rem;
    min-height: 1.85rem;
}
.stApp .help-capability-row[data-kind="strength"] {
    --row-color: var(--help-green-ink);
    --row-surface: var(--help-green-soft);
}
.stApp .help-capability-row[data-kind="tradeoff"] {
    --row-color: var(--help-amber-ink);
    --row-surface: var(--help-amber-soft);
}
.stApp .help-capability-row[data-kind="next"] {
    --row-color: var(--help-blue-ink);
    --row-surface: var(--help-blue-soft);
}
.stApp .help-status-dot {
    display: inline-block;
    width: 0.4rem;
    height: 0.4rem;
    margin-top: 0.4rem;
    border: 1px solid var(--path-color);
    border-radius: 50%;
    background: var(--path-color);
}
.stApp .help-status-dot.planned {
    border-color: var(--help-muted);
    background: transparent;
}
.stApp :is(.main, [data-testid="stMain"]) .help-capability-tag {
    display: inline-block;
    padding: 0.1rem 0.2rem;
    border: 1px solid var(--row-color);
    border-radius: 10px;
    background: var(--row-surface) !important;
    color: var(--row-color) !important;
    font-size: 0.6rem;
    font-weight: 700;
    line-height: 1.5;
    text-align: center;
    white-space: nowrap;
}
.stApp :is(.main, [data-testid="stMain"]) .help-capability-text {
    color: var(--help-ink) !important;
    font-size: 0.78rem;
    line-height: 1.55;
    overflow-wrap: anywhere;
}
.stApp :is(.main, [data-testid="stMain"]) .help-column-note {
    margin-top: auto;
    padding: 0.7rem 0.05rem 0;
    color: var(--help-muted) !important;
    font-size: 0.74rem;
    line-height: 1.55;
}
.stApp :is(.main, [data-testid="stMain"]) .help-column-note p {
    color: var(--help-muted) !important;
    font-size: 0.74rem;
    line-height: 1.55;
    margin: 0;
}
.stApp :is(.main, [data-testid="stMain"]) .help-footer {
    color: var(--help-muted) !important;
    border-top: 1px solid var(--help-line);
    padding-top: 1rem;
    margin-top: 2.5rem;
    font-size: 0.75rem;
    line-height: 1.7;
}

/* Native tabs and collapsible sections retain Streamlit keyboard behavior. */
.stApp :is(.main, [data-testid="stMain"]) .stTabs [data-baseweb="tab-list"] {
    gap: 1.4rem;
    border-bottom: 1px solid var(--help-line);
    background: transparent !important;
}
.stApp :is(.main, [data-testid="stMain"]) .stTabs [data-baseweb="tab"] {
    padding: 0.7rem 0 0.85rem;
    height: auto;
    background: transparent !important;
    white-space: nowrap;
}
.stApp :is(.main, [data-testid="stMain"]) .stTabs [data-baseweb="tab"] p {
    color: var(--help-muted) !important;
    font-size: 0.88rem;
    font-weight: 600;
}
.stApp :is(.main, [data-testid="stMain"]) .stTabs [aria-selected="true"] p {
    color: var(--help-accent-text) !important;
}
.stApp .stTabs [data-baseweb="tab-highlight"] { background: var(--help-accent) !important; }
.stApp .stTabs [data-baseweb="tab-border"] { background: transparent !important; }
.stApp :is(.main, [data-testid="stMain"]) .stTabs .stTabs [data-baseweb="tab-list"] {
    gap: 0.35rem;
    padding-top: 0.15rem;
}
.stApp :is(.main, [data-testid="stMain"]) .stTabs .stTabs [data-baseweb="tab"] {
    padding: 0.4rem 0.65rem 0.5rem;
    border-radius: 4px 4px 0 0;
}
.stApp :is(.main, [data-testid="stMain"]) .stTabs .stTabs [data-baseweb="tab"] p {
    font-size: 0.79rem;
    font-weight: 500;
}
.stApp :is(.main, [data-testid="stMain"]) .stTabs .stTabs [data-baseweb="tab"][aria-selected="true"] {
    background: var(--help-accent-soft) !important;
}
.stApp :is(.main, [data-testid="stMain"]) .stTabs .stTabs [data-baseweb="tab"][aria-selected="true"] p {
    color: var(--help-accent-text) !important;
    font-weight: 600;
}
.stApp :is(.main, [data-testid="stMain"]) [data-testid="stExpander"] {
    border: 1px solid var(--help-line) !important;
    border-radius: 6px;
    background: var(--help-surface) !important;
}
.stApp :is(.main, [data-testid="stMain"]) [data-testid="stExpander"] summary {
    padding-top: 0.85rem;
    padding-bottom: 0.85rem;
    color: var(--help-ink) !important;
}
.stApp :is(.main, [data-testid="stMain"]) [data-testid="stExpander"] summary p {
    font-weight: 600;
    font-size: 0.9rem;
}
.stApp :is(.main, [data-testid="stMain"]) [data-testid="stVerticalBlockBorderWrapper"] {
    border-color: var(--help-line) !important;
    border-radius: 6px;
    background: var(--help-surface) !important;
}

/* Form controls, including the dropdown menu rendered outside the main area. */
.stApp :is(.main, [data-testid="stMain"]) [data-baseweb="select"] > div,
.stApp :is(.main, [data-testid="stMain"]) [data-baseweb="input"],
.stApp :is(.main, [data-testid="stMain"]) [data-baseweb="base-input"],
.stApp :is(.main, [data-testid="stMain"]) [data-baseweb="textarea"] {
    background: var(--help-surface) !important;
    color: var(--help-ink) !important;
    border-color: var(--help-line) !important;
    border-radius: 5px;
}
.stApp :is(.main, [data-testid="stMain"]) [data-baseweb="select"] :is(div, span),
.stApp :is(.main, [data-testid="stMain"]) :is(input, textarea) {
    color: var(--help-ink) !important;
}
.stApp :is(.main, [data-testid="stMain"]) :is(input, textarea) {
    background: var(--help-surface) !important;
    caret-color: var(--help-accent);
}
.stApp :is(.main, [data-testid="stMain"]) :is(input, textarea)::placeholder {
    color: var(--help-muted) !important;
    opacity: 0.8;
}
.stApp :is(.main, [data-testid="stMain"]) [data-testid="stWidgetLabel"] p {
    font-size: 0.83rem;
    font-weight: 600;
}
[data-baseweb="popover"] [data-baseweb="menu"],
[data-baseweb="popover"] [role="listbox"] {
    background: var(--help-surface) !important;
    border: 1px solid var(--help-line);
}
[data-baseweb="popover"] [role="option"],
[data-baseweb="popover"] [role="option"] :is(div, span, li) {
    color: var(--help-ink) !important;
    background: var(--help-surface) !important;
}
[data-baseweb="popover"] [role="option"]:hover,
[data-baseweb="popover"] [role="option"][aria-selected="true"],
[data-baseweb="popover"] [role="option"][aria-selected="true"] :is(div, span) {
    background: var(--help-accent-soft) !important;
}
.stApp :is(.main, [data-testid="stMain"]) :is(.stButton, .stDownloadButton, .stLinkButton) > :is(button, a) {
    min-height: 2.65rem;
    padding: 0.55rem 0.9rem;
    border: 1px solid var(--help-line) !important;
    border-radius: 5px;
    background: var(--help-surface) !important;
    color: var(--help-ink) !important;
    font-family: inherit !important;
    box-shadow: none !important;
}
.stApp :is(.main, [data-testid="stMain"]) :is(.stButton, .stDownloadButton, .stLinkButton) > :is(button, a):hover {
    background: var(--help-accent-soft) !important;
    border-color: var(--help-accent) !important;
}
.stApp :is(.main, [data-testid="stMain"]) :is(.stButton, .stDownloadButton) > button[kind="primary"] {
    background: var(--help-accent-text) !important;
    border-color: var(--help-accent-text) !important;
}
.stApp :is(.main, [data-testid="stMain"]) :is(.stButton, .stDownloadButton) > button[kind="primary"] p {
    color: var(--help-paper) !important;
}
.stApp :is(.main, [data-testid="stMain"]) button:disabled { opacity: 0.5; }
.stApp :is(.main, [data-testid="stMain"]) :is(button, a, input, textarea):focus-visible {
    outline: 2px solid var(--help-accent) !important;
    outline-offset: 3px;
}
.stApp :is(.main, [data-testid="stMain"]) .stProgress [role="progressbar"] {
    background: var(--help-surface-soft) !important;
}
.stApp :is(.main, [data-testid="stMain"]) .stProgress [role="progressbar"] > div {
    background: var(--help-accent) !important;
}
.stApp :is(.main, [data-testid="stMain"]) [data-testid="stFileUploaderDropzone"] {
    border: 1px dashed var(--help-line) !important;
    border-radius: 6px;
    background: var(--help-surface) !important;
}
.stApp :is(.main, [data-testid="stMain"]) [data-testid="stFileUploaderDropzone"] :is(button, small, span) {
    color: var(--help-ink) !important;
}
.stApp :is(.main, [data-testid="stMain"]) .stAlert {
    background: var(--help-accent-soft) !important;
    border: 1px solid var(--help-line) !important;
    border-radius: 5px;
}
.stApp :is(.main, [data-testid="stMain"]) :is(table, th, td) {
    color: var(--help-ink) !important;
    border-color: var(--help-line) !important;
}
.stApp :is(.main, [data-testid="stMain"]) table {
    background: var(--help-surface) !important;
    font-size: 0.83rem;
}
.stApp :is(.main, [data-testid="stMain"]) th {
    background: var(--help-accent-soft) !important;
    text-align: left;
}

@media (max-width: 1100px) {
    .stApp .help-path-grid { grid-template-columns: repeat(2, minmax(0, 1fr)); }
    .stApp .help-armada-grid { grid-template-columns: repeat(2, minmax(0, 1fr)); }
    .stApp :is(.main, [data-testid="stMain"]) .block-container {
        padding-left: 1.65rem !important;
        padding-right: 1.65rem !important;
    }
}
@media (max-width: 640px) {
    .stApp :is(.main, [data-testid="stMain"]) .block-container {
        padding: 2.75rem 1rem 3rem !important;
    }
    .stApp .help-path-grid { grid-template-columns: minmax(0, 1fr); }
    .stApp .help-armada-grid { grid-template-columns: minmax(0, 1fr); gap: 1.4rem; }
    .stApp .help-hero { padding: 1.5rem; border-radius: 6px; }
    .stApp .help-metrics { grid-template-columns: minmax(0, 1fr); }
    .stApp .help-metric + .help-metric {
        border-left: 0;
        border-top: 1px solid var(--help-line);
    }
    .stApp .help-metric { padding: 0.85rem 1rem; }
    .stApp :is(.main, [data-testid="stMain"]) .stTabs [data-baseweb="tab-list"] { gap: 1rem; }
    .stApp .help-pipeline { grid-template-columns: minmax(0, 1fr); }
}
"""


def apply_theme(matrix_mode: bool = False) -> None:
    """Apply this console's theme for the current Streamlit render.

    Call after the host dashboard theme when embedding. Variables are declared
    on :root too because Base Web dropdowns render in a document-level portal.
    No JavaScript, network fonts or external assets are needed.
    """
    palette = _MATRIX if matrix_mode else _LIGHT
    variables = "\n".join(f"--help-{name}: {value};" for name, value in palette.items())
    st.markdown(
        '<style data-help-theme="' + ("matrix" if matrix_mode else "ledger") + '">'
        + ":root, .stApp {" + variables + "}"
        + _CSS
        + "</style>",
        unsafe_allow_html=True,
    )
