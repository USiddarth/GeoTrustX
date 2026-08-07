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
# 2. CUSTOM DARK THEME & FIXED SIDEBAR TOGGLE CSS
# =========================================================
st.markdown("""
    <style>
        /* Base Dark Background */
        .stApp {
            background-color: #0b0f19;
            color: #e2e8f0;
        }

        /* Sidebar Dark Background */
        [data-testid="stSidebar"] {
            background-color: #111827 !important;
            border-right: 1px solid #1f2937 !important;
        }

        /* Bring Streamlit Header & Sidebar Toggle Button to Top Layer */
        header[data-testid="stHeader"] {
            background-color: transparent !important;
            z-index: 999991 !important;
        }

        /* Force Sidebar Toggle Arrow/X Button to be Visible */
        [data-testid="stHeader"] button, 
        [data-testid="stSidebar"] button {
            color: #38bdf8 !important;
            visibility: visible !important;
        }

        /* Hide Streamlit Footer */
        footer {
            visibility: hidden !important;
        }

        /* Layout Margins */
        .block-container {
            padding-top: 1.5rem !important;
            padding-bottom: 1rem !important;
            max-width: 98% !important;
        }
    </style>
""", unsafe_allow_html=True)

# =========================================================
# 3. SIDEBAR NAVIGATION
# =========================================================
st.sidebar.title("🛡️ GeoTrustX")
st.sidebar.caption("Real-Time Telemetry & Trust Engine v2.0")
st.sidebar.markdown("---")

selected_module = st.sidebar.radio(
    "Select System Module:",
    [
        "01 Overview Dashboard",
        "02 Telemetry Analytics",
        "03 Physics Engine Rules",
        "04 System Settings"
    ],
    index=0
)

st.sidebar.markdown("---")
st.sidebar.success("● Engine Operational")

# =========================================================
# 4. MODULE CONTROLLERS
# =========================================================

# --- MODULE 1: OVERVIEW (Renders dashboard.html) ---
if "01 Overview" in selected_module:
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    html_path = os.path.join(BASE_DIR, "dashboard.html")

    if os.path.exists(html_path):
        try:
            with open(html_path, "r", encoding="utf-8") as f:
                html_code = f.read()
            components.html(html_code, height=920, scrolling=True)
        except Exception as e:
            st.error(f"Error loading dashboard: {e}")
    else:
        st.warning("⚠️ `dashboard.html` not found in the root folder.")

# --- MODULE 2: TELEMETRY ANALYTICS ---
elif "02 Telemetry" in selected_module:
    st.header("📊 Telemetry Analytics")
    st.subheader("Live Confidence Interval Data")
    
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric(label="Data Stream Frequency", value="240 Hz", delta="Normal")
    with col2:
        st.metric(label="Latency", value="14 ms", delta="-2 ms")
    with col3:
        st.metric(label="Packet Retention", value="99.98%", delta="0.01%")
        
    st.info("Module running live anomaly detection across active nodes.")

# --- MODULE 3: PHYSICS ENGINE RULES ---
elif "03 Physics" in selected_module:
    st.header("⚡ Physics Engine Validation")
    st.subheader("Rule Compliance & Boundaries")
    
    st.json({
        "physics_validation": "100%",
        "active_rules": [
            "Velocity Cap Check",
            "Thermal Threshold Monitoring",
            "Trajectory Variance Filter"
        ],
        "status": "PASS"
    })

# --- MODULE 4: SYSTEM SETTINGS ---
elif "04 System" in selected_module:
    st.header("⚙️ System Settings")
    st.write("Configure GeoTrustX Telemetry parameters:")
    
    st.slider("Stream Refresh Interval (seconds)", min_value=1, max_value=10, value=2)
    st.toggle("Enable Live Physics Checks", value=True)
    st.toggle("Auto-Archive Logs", value=False)