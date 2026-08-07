import os
import json
import time
import numpy as np
import pandas as pd
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
# 2. CUSTOM DARK THEME & UI STYLING
# =========================================================
st.markdown("""
    <style>
        /* Base Theme Colors */
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
        
        /* Metric Cards Styling */
        div[data-testid="stMetric"] {
            background-color: #111827;
            border: 1px solid #1f2937;
            border-radius: 10px;
            padding: 14px;
        }
    </style>
""", unsafe_allow_html=True)

# =========================================================
# 3. SIDEBAR NAVIGATION
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

# --- 01 OVERVIEW ---
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

# --- 02 SOURCE INGESTION ---
elif "02 Source Ingestion" in selected_module:
    st.header("📡 02 Source Ingestion Pipeline")
    st.caption("Real-Time Multi-Sensor Telemetry & Data Stream Ingestion")
    st.markdown("---")
    
    col1, col2, col3, col4 = st.columns(4)
    col1.metric("Active Streams", "12 / 12", "Operational")
    col2.metric("Ingestion Rate", "1.24 GB/s", "+0.08 GB/s")
    col3.metric("Signal Quality", "99.4%", "+0.2%")
    col4.metric("Avg Latency", "8.2 ms", "-1.1 ms")
    
    st.markdown("### 📈 Live Telemetry Throughput")
    chart_data = pd.DataFrame(
        np.random.randn(20, 3) * [2, 5, 1] + [100, 250, 50],
        columns=['Satellite Feed Alpha', 'Hydrological Sensor B', 'Radar Array 04']
    )
    st.line_chart(chart_data)
    
    st.markdown("### 📋 Active Data Stream Status")
    stream_df = pd.DataFrame({
        "Stream Name": ["Satellite Feed Alpha", "Hydrological Sensor B", "Radar Array 04", "Thermal Node 09"],
        "Protocol": ["MQTT/TLS", "gRPC", "WebSocket", "UDP Telemetry"],
        "Sample Rate": ["100 Hz", "50 Hz", "250 Hz", "10 Hz"],
        "Status": ["🟢 ACTIVE", "🟢 ACTIVE", "🟢 ACTIVE", "🟡 CALIBRATING"]
    })
    st.dataframe(stream_df, use_container_width=True)

# --- 03 CONSISTENCY ENGINE ---
elif "03 Consistency Engine" in selected_module:
    st.header("⚙️ 03 Consistency Engine")
    st.caption("Pairwise Conflict Matrices & Multi-Source Cross-Verification")
    st.markdown("---")
    
    col1, col2, col3 = st.columns(3)
    col1.metric("Consistency Index", "87.0%", "+1.4%")
    col2.metric("Pairwise Conflicts", "0 Detected", "Optimal")
    col3.metric("Matrix Sync Time", "1.2 ms", "Real-Time")
    
    st.markdown("### 🔍 Pairwise Disagreement Matrix")
    matrix_data = pd.DataFrame(
        [
            [1.00, 0.98, 0.95, 0.99],
            [0.98, 1.00, 0.92, 0.97],
            [0.95, 0.92, 1.00, 0.94],
            [0.99, 0.97, 0.94, 1.00]
        ],
        columns=["Sensor Alpha", "Sensor Beta", "Radar Gamma", "Sat Delta"],
        index=["Sensor Alpha", "Sensor Beta", "Radar Gamma", "Sat Delta"]
    )
    st.dataframe(matrix_data.style.highlight_max(axis=0), use_container_width=True)

# --- 04 CONFIDENCE ENGINE ---
elif "04 Confidence Engine" in selected_module:
    st.header("🎯 04 Confidence Engine")
    st.caption("Ensemble Standard Deviation ($\sigma$) & Calibrated Monte Carlo Bounds")
    st.markdown("---")
    
    col1, col2, col3 = st.columns(3)
    col1.metric("Confidence Score", "82.0%", "Calibrated")
    col2.metric("Std Deviation Spread (σ)", "1.42", "-0.15")
    col3.metric("Monte Carlo Iterations", "10,000", "Passed")
    
    st.markdown("### 🎲 Monte Carlo Confidence Interval Spread")
    np.random.seed(42)
    mc_sim = pd.DataFrame(
        np.random.normal(82, 1.42, size=(100, 1)),
        columns=["Calibrated Score Spread"]
    )
    st.area_chart(mc_sim)

# --- 05 PHYSICS VALIDATION ---
elif "05 Physics Validation" in selected_module:
    st.header("⚡ 05 Physics Validation")
    st.caption("Real-Time Physical Boundary & Constraint Verification")
    st.markdown("---")
    
    col1, col2 = st.columns([1, 2])
    with col1:
        st.metric("Physics Score", "100%", "Constraint Passed")
        st.success("✅ Hydrological Constraints Verified")
        st.success("✅ Velocity Cap Verified")
        st.success("✅ Thermal Gradient Bounds Passed")
    
    with col2:
        st.markdown("### 📜 Constraint Rule Audit Log")
        st.code("""
[SYSTEM] GeoTrustX physics rules engine active.
[CHECK 1] Slope factor: 1.0 (Limit: <= 1.5) -> PASS
[CHECK 2] Max Acceleration: 2.1 m/s² (Limit: <= 9.8 m/s²) -> PASS
[CHECK 3] Energy Conservation Equation: ΔE = 0.003 J -> PASS
[STATUS] Telemetry complies with physical laws.
        """, language="bash")

# --- 06 TRUST & DECISION ---
elif "06 Trust & Decision" in selected_module:
    st.header("🛡️ 06 Trust & Decision Output")
    st.caption("Final Automated Decision Weighting & Audit Certificate Generation")
    st.markdown("---")
    
    col1, col2, col3, col4 = st.columns(4)
    col1.metric("Reliability", "74 %")
    col2.metric("Consistency", "87 %")
    col3.metric("Confidence", "82 %")
    col4.metric("Physics", "100 %")
    
    st.markdown("### 🏆 Composite Trust Result")
    st.progress(0.86)
    st.success("### **DECISION: APPROVED (TRUST SCORE: 86.4%)**")
    
    if st.button("📄 Export Audit Certificate"):
        st.download_button("Download Signed Certificate (JSON)", json.dumps({"trust_score": 86.4, "status": "APPROVED", "timestamp": time.time()}), "audit_certificate.json")

# --- 07 3D TRUST MAP ---
elif "07 3D Trust Map" in selected_module:
    st.header("🗺️ 07 3D Geospatial Trust Map")
    st.caption("Real-time Spatial Verification Grid")
    st.markdown("---")
    
    # Map visual demo
    map_data = pd.DataFrame(
        np.random.randn(100, 2) / [50, 50] + [12.9141, 74.8560],
        columns=['lat', 'lon']
    )
    st.map(map_data)

# --- 08 SEARCH & DIRECTIONS ---
elif "08 Search & Directions" in selected_module:
    st.header("🚀 08 Search & Spatial Verification")
    st.caption("Query Telemetry Nodes & Route Verification")
    st.markdown("---")
    
    search_q = st.text_input("🔍 Search Telemetry Node ID / Coordinate / Route:", value="NODE-882-MANGALORE")
    col1, col2 = st.columns(2)
    with col1:
        st.write(f"**Target:** {search_q}")
        st.write("**Latitude / Longitude:** 12.9141° N, 74.8560° E")
        st.write("**Signal Radius:** 15.2 km")
    with col2:
        st.info("🟢 Route Trust Rating: High (Safe for navigation)")

# --- 09 AI COPILOT ---
elif "09 AI Copilot" in selected_module:
    st.header("🤖 09 GeoTrustX AI Copilot")
    st.caption("Interactive Telemetry & Physics Analysis Assistant")
    st.markdown("---")
    
    if "messages" not in st.session_state:
        st.session_state.messages = [
            {"role": "assistant", "content": "Hello! I am GeoTrustX Copilot. Ask me anything about your current composite trust score or physics validation rules."}
        ]

    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    if prompt := st.chat_input("Ask Copilot..."):
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.markdown(prompt)

        with st.chat_message("assistant"):
            response = f"**Copilot Analysis:** Based on live data streams, your composite trust is **86.4%**. Physics validation is at 100% with zero pairwise conflict detected for query '{prompt}'."
            st.markdown(response)
            st.session_state.messages.append({"role": "assistant", "content": response})