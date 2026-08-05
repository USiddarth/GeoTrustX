import streamlit as st
import streamlit.components.v1 as components
import engine

# 1. Custom Dark Theme Styling
st.markdown("""
<style>
    .stApp { background-color: #0b0f19; color: #e2e8f0; }
    [data-testid="stSidebar"] { background-color: #111827; }
</style>
""", unsafe_allow_html=True)

# 2. SVG Logo Setup
SVG_LOGO = """<svg width="200" height="200" viewBox="0 0 200 200" xmlns="http://www.w3.org/2000/svg">
<rect width="200" height="200" rx="40" fill="#0f172a"/>
<circle cx="100" cy="100" r="70" fill="none" stroke="#1e293b" stroke-width="6"/>
<circle cx="100" cy="100" r="45" fill="none" stroke="#334155" stroke-width="4" stroke-dasharray="8 6"/>
<line x1="100" y1="20" x2="100" y2="180" stroke="#1e293b" stroke-width="3"/>
<line x1="20" y1="100" x2="180" y2="100" stroke="#1e293b" stroke-width="3"/>
<line x1="65" y1="65" x2="135" y2="135" stroke="#22c55e" stroke-width="18" stroke-linecap="round"/>
<line x1="135" y1="65" x2="65" y2="135" stroke="#22c55e" stroke-width="18" stroke-linecap="round"/>
<circle cx="100" cy="100" r="10" fill="#ffffff"/>
</svg>"""

with open("logo.svg", "w") as f:
    f.write(SVG_LOGO)

# 3. Configure Page Layout
st.set_page_config(
    page_title="GeoTrustX – Trust & Verification Layer",
    page_icon="logo.svg",
    layout="wide",
    initial_sidebar_state="expanded"
)

if hasattr(st, "logo"):
    st.logo("logo.svg", icon_image="logo.svg")

# Hide default headers & footers

# Hide default headers & footers and fix spacing
st.markdown("""
    <style>
        /* Hide default header/footer */
        header {visibility: hidden;}
        footer {visibility: hidden;}

        /* Reduce top and bottom page padding */
        .block-container {
            padding-top: 1.5rem !important;
            padding-bottom: 1rem !important;
            max-width: 95% !important;
        }
        
        /* Reduce vertical gap between elements */
        div[data-testid="stVerticalBlock"] > div {
            gap: 0.8rem !important;
        }
    </style>
""", unsafe_allow_html=True)
# 4. Sidebar Navigation
st.sidebar.title("GeoTrustX")
selected_module = st.sidebar.radio(
    "Select Module:",
    [
        "01 Overview", "02 Source Ingestion", "03 Consistency Engine",
        "04 Confidence Engine", "05 Physics Validation", "06 Trust & Decision",
        "07 3D Trust Map", "08 Search & Directions", "09 AI Copilot"
    ]
)

# 5. Dynamic Module Views
if "01 Overview" in selected_module:
  import os
        BASE_DIR = os.path.dirname(os.path.abspath(__file__))
        html_path = os.path.join(BASE_DIR, "dashboard.html")
        
        try:
            with open(html_path, "r", encoding="utf-8") as f:
                html_code = f.read()
            components.html(html_code, height=900, scrolling=True)
        except FileNotFoundError:
            st.error("dashboard.html not found.")  
elif "02 Source Ingestion" in selected_module:
    st.title("02 :: Source Ingestion Engine")
    col1, col2, col3 = st.columns(3)
    col1.metric("GPS Streams", "Active", "12 ms latency")
    col2.metric("Cellular Signals", "100%", "+2.4%")
    col3.metric("WiFi Triangulation", "Connected", "Stable")
    st.dataframe({"Source ID": ["GPS_01", "CELL_04", "WIFI_02"], "Status": ["OK", "OK", "DEGRADED"], "Trust": [0.98, 0.91, 0.64]})

elif "03 Consistency Engine" in selected_module:
    st.title("03 :: Cross-Source Consistency Engine")
    st.line_chart([0.88, 0.92, 0.89, 0.95, 0.91, 0.96])

elif "04 Confidence Engine" in selected_module:
    st.title("04 :: Confidence Score Generator")
    col1, col2 = st.columns(2)
    col1.metric("Aggregate Confidence", "94.2%", "+1.1%")
    col2.metric("Variance Index", "0.032", "-0.005")
    st.bar_chart([85, 90, 88, 94, 92, 97])

elif "05 Physics Validation" in selected_module:
    st.title("05 :: Physical Constraint & Bounds Check")
    st.warning("No velocity violations detected in current spatial frame.")
    st.json({"max_allowed_velocity_ms": 33.3, "measured_velocity_ms": 14.2, "physics_bound_pass": True})

elif "06 Trust & Decision" in selected_module:
    st.title("06 :: Automated Trust & Decision Matrix")
    col1, col2 = st.columns(2)
    col1.metric("Current Decision Status", "VERIFIED", "High Trust")
    col2.metric("Anomalies Flagged", "0", "Clear")

elif "07 3D Trust Map" in selected_module:
    st.title("07 :: 3D Geospatial Trust Visualization")
    st.map({"lat": [37.7749, 37.7750, 37.7752], "lon": [-122.4194, -122.4195, -122.4190]})

elif "08 Search & Directions" in selected_module:
    st.title("08 :: Trust-Aware Routing & Directions")
    destination = st.text_input("Enter target coordinates / address:", "37.7749, -122.4194")
    if st.button("Calculate Safe Path"):
        st.success(f"Route generated avoiding low-trust zones for: {destination}")

elif "09 AI Copilot" in selected_module:
    st.title("09 :: GeoTrustX AI Assistant")
    user_query = st.chat_input("Ask GeoTrustX Copilot about telemetry anomalies...")
    if user_query:
        st.write(f"**User:** {user_query}")
        st.write(f"**Copilot:** Analyzing telemetry metrics for query '{user_query}'... All primary signals remain within 95% confidence intervals.")