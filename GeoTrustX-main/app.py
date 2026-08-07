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
    initial_sidebar_state="collapsed"
)

# =========================================================
# 2. CUSTOM CSS (Clean, Full-Screen Dark Theme)
# =========================================================
st.markdown("""
    <style>
        /* Base Dark Theme Colors */
        .stApp {
            background-color: #0b0f19;
            color: #e2e8f0;
        }

        /* Hide Sidebar Completely */
        [data-testid="stSidebar"] {
            display: none !important;
        }

        /* Hide Footer & Header Bar */
        footer {
            visibility: hidden !important;
        }
        
        header[data-testid="stHeader"] {
            background: transparent !important;
        }

        /* Maximize Full Screen Space */
        .block-container {
            padding-top: 0.5rem !important;
            padding-bottom: 0rem !important;
            padding-left: 0.5rem !important;
            padding-right: 0.5rem !important;
            max-width: 100% !important;
        }
    </style>
""", unsafe_allow_html=True)

# =========================================================
# 3. DIRECT DASHBOARD RENDERING
# =========================================================
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
html_path = os.path.join(BASE_DIR, "dashboard.html")

if os.path.exists(html_path):
    try:
        with open(html_path, "r", encoding="utf-8") as f:
            html_code = f.read()
        
        # Render HTML directly across the entire screen
        components.html(html_code, height=950, scrolling=True)
    except Exception as e:
        st.error(f"Error loading dashboard: {e}")
else:
    st.warning("⚠️ `dashboard.html` was not found in the root directory. Please make sure it is saved in your project folder and pushed to GitHub.")