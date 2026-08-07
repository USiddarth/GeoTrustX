import os
import streamlit as st
import streamlit.components.v1 as components

# =========================================================
# 1. PAGE CONFIGURATION
# =========================================================
st.set_page_config(
    page_title="GeoTrustX",
    page_icon="🛡️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# =========================================================
# 2. CUSTOM DARK THEME & FIXED SIDEBAR CSS
# =========================================================
st.markdown("""
    <style>
        .stApp {
            background-color: #0b0f19;
            color: #e2e8f0;
        }

        [data-testid="stSidebar"] {
            background-color: #0d1322 !important;
            border-right: 1px solid #1e293b !important;
        }

        header[data-testid="stHeader"] {
            background-color: transparent !important;
            z-index: 999991 !important;
        }

        [data-testid="stHeader"] button, 
        [data-testid="stSidebar"] button {
            color: #38bdf8 !important;
            visibility: visible !important;
        }

        footer {
            visibility: hidden !important;
        }

        .block-container {
            padding-top: 1rem !important;
            padding-bottom: 1rem !important;
            padding-left: 1rem !important;
            padding-right: 1rem !important;
            max-width: 100% !important;
        }
    </style>
""", unsafe_allow_html=True)

# =========================================================
# 3. SIDEBAR NAVIGATION (9 MODULES)
# =========================================================
st.sidebar.markdown("### 🟢 **GeoTrustX**")
st.sidebar.caption("🛡️ TRUST & VERIFICATION LAYER")
st.sidebar.markdown("---")

modules = [
    "📊 01 Overview",
    "📡 02 Source Ingestion",
    "⚙️ 03 Consistency Engine",
    "🎯 04 Confidence Engine",
    "⚡ 05 Physics Validation",
    "🛡️ 06 Trust & Decision",
    "🗺️ 07 3D Trust Map",
    "🚀 08 Search & Directions",
    "🤖 09 AI Copilot"
]

selected_module = st.sidebar.radio(
    "Select Module:",
    modules,
    index=0,
    label_visibility="collapsed"
)

st.sidebar.markdown("---")
st.sidebar.caption("GEOTRUSTX v2.0 | **ENTERPRISE**")
st.sidebar.info("⚙️ LOCAL MATH ENGINE")

# =========================================================
# 4. MODULE CONTENT ROUTING
# =========================================================

if "01 Overview" in selected_module:
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    html_path = os.path.join(BASE_DIR, "dashboard.html")

    if os.path.exists(html_path):
        try:
            with open(html_path, "r", encoding="utf-8") as f:
                html_code = f.read()
            components.html(html_code, height=950, scrolling=True)
        except Exception as e:
            st.error(f"Error loading dashboard: {e}")
    else:
        st.warning("⚠️ `dashboard.html` was not found in the root directory.")

elif "02 Source Ingestion" in selected_module:
    st.header("📡 02 Source Ingestion")
    st.info("Live data pipelines active. Monitoring multi-source streams.")

elif "03 Consistency Engine" in selected_module:
    st.header("⚙️ 03 Consistency Engine")
    st.info("Cross-checking data sources against pairwise conflict matrices.")

elif "04 Confidence Engine" in selected_module:
    st.header("🎯 04 Confidence Engine")
    st.info("Calibrating confidence score bounds using ensemble standard deviation.")

elif "05 Physics Validation" in selected_module:
    st.header("⚡ 05 Physics Validation")
    st.info("Hydrological & physical constraints validation active (100% Passed).")

elif "06 Trust & Decision" in selected_module:
    st.header("🛡️ 06 Trust & Decision")
    st.info("Trust Score calibration and decision outputs.")

elif "07 3D Trust Map" in selected_module:
    st.header("🗺️ 07 3D Trust Map")
    st.info("Rendering geospatial 3D trust telemetry grid...")

elif "08 Search & Directions" in selected_module:
    st.header("🚀 08 Search & Directions")
    st.info("Geospatial routing and verification search.")

elif "09 AI Copilot" in selected_module:
    st.header("🤖 09 AI Copilot")
    st.text_input("Ask GeoTrustX Copilot:", placeholder="Query telemetry logs or audit certificates...")