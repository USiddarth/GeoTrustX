import os
import streamlit as st
import streamlit.components.v1 as components

# Safely import custom engine module if available
try:
    import engine
except ImportError:
    engine = None

# =========================================================
# 1. PAGE CONFIGURATION (Must be the very first Streamlit command)
# =========================================================
st.set_page_config(
    page_title="GeoTrustX",
    page_icon="🛡️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# =========================================================
# 2. CUSTOM DARK THEME & STYLING
# =========================================================
# Note: 'header' is left visible so the sidebar toggle arrow (>) is always accessible.
st.markdown("""
    <style>
        /* Dark Theme Colors */
        .stApp {
            background-color: #0b0f19;
            color: #e2e8f0;
        }
        [data-testid="stSidebar"] {
            background-color: #111827;
        }

        /* Hide Footer Only */
        footer {
            visibility: hidden;
        }

        /* Layout & Spacing Tweaks */
        .block-container {
            padding-top: 1.5rem !important;
            padding-bottom: 1rem !important;
            max-width: 95% !important;
        }

        /* Reduce Vertical Gap */
        div[data-testid="stVerticalBlock"] > div {
            gap: 0.5rem;
        }
    </style>
""", unsafe_allow_html=True)

# =========================================================
# 3. LOGO SETUP
# =========================================================
if hasattr(st, "logo"):
    try:
        st.logo("logo.svg", icon_image="logo.svg")
    except Exception:
        pass

# =========================================================
# 4. SIDEBAR NAVIGATION
# =========================================================
st.sidebar.title("GeoTrustX Navigation")
selected_module = st.sidebar.radio(
    "Select Module:",
    ["01 Overview", "02 Analytics", "03 Settings"],
    index=0
)

# =========================================================
# 5. MODULE RENDERING
# =========================================================
if "01 Overview" in selected_module:
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    html_path = os.path.join(BASE_DIR, "dashboard.html")

    if os.path.exists(html_path):
        try:
            with open(html_path, "r", encoding="utf-8") as f:
                html_code = f.read()
            components.html(html_code, height=900, scrolling=True)
        except Exception as e:
            st.error(f"Error reading dashboard.html: {e}")
    else:
        st.warning("⚠️ `dashboard.html` was not found in the root folder. Please ensure the file is uploaded to GitHub.")

elif "02 Analytics" in selected_module:
    st.header("Analytics Module")
    st.info("Analytics module active.")

elif "03 Settings" in selected_module:
    st.header("Settings Module")
    st.write("Configuration panel.")