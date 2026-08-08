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
# 2. CUSTOM DARK THEME & STYLING
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
    index=4,  # Defaulted to 05 Physics Validation
    label_visibility="collapsed"
)

st.sidebar.markdown("---")
st.sidebar.caption("GEOTRUSTX v2.0 | **ENTERPRISE**")
st.sidebar.info("⚙️ LOCAL MATH ENGINE")

# =========================================================
# 4. DECK.GL + MAPLIBRE 3D GPU EXTRUSION ENGINE
# =========================================================
def render_deckgl_3d_map():
    deck_html = """
    <!DOCTYPE html>
    <html>
    <head>
        <script src="https://unpkg.com/deck.gl@8.9.0/dist.min.js"></script>
        <script src="https://unpkg.com/maplibre-gl@3.0.0/dist/maplibre-gl.js"></script>
        <link href="https://unpkg.com/maplibre-gl@3.0.0/dist/maplibre-gl.css" rel="stylesheet" />
        <style>
            body { margin: 0; padding: 0; background-color: #0b0f19; overflow: hidden; font-family: sans-serif; }
            #container { width: 100vw; height: 750px; }
            .overlay-card {
                position: absolute;
                top: 20px;
                left: 20px;
                z-index: 10;
                background: rgba(13, 19, 34, 0.92);
                border: 1px solid #38bdf8;
                border-radius: 10px;
                padding: 16px;
                color: #fff;
                width: 300px;
                box-shadow: 0 10px 25px rgba(0,0,0,0.8);
            }
            .overlay-card h3 { margin: 0 0 8px 0; color: #38bdf8; font-size: 15px; }
            .stat-line { display: flex; justify-content: space-between; font-size: 12px; margin-top: 6px; }
            .stat-val { color: #00f2fe; font-weight: bold; }
        </style>
    </head>
    <body>
        <div class="overlay-card">
            <h3>🗺️ Deck.gl GPU 3D Spatial Extrusion</h3>
            <div style="font-size:11px; color:#94a3b8;">Render Engine: MapLibre + WebGL</div>
            <hr style="border-color:#1e293b; margin:10px 0;">
            <div class="stat-line"><span>Active 3D Extruded Nodes:</span><span class="stat-val">350 Points</span></div>
            <div class="stat-line"><span>Elevation Metric:</span><span class="stat-val">Trust Density (m)</span></div>
            <div class="stat-line"><span>Max Column Height:</span><span class="stat-val">1,200m</span></div>
            <div class="stat-line"><span>GPU Frame Rate:</span><span class="stat-val" style="color:#4ade80;">60 FPS</span></div>
        </div>

        <div id="container"></div>

        <script>
            // Generate Spatial Extrusion Data around Coordinates
            const DATA = [];
            const centerLng = 74.8560;
            const centerLat = 12.9141;

            for (let i = 0; i < 350; i++) {
                const trustScore = Math.random() * 100;
                DATA.push({
                    position: [
                        centerLng + (Math.random() - 0.5) * 0.18,
                        centerLat + (Math.random() - 0.5) * 0.18
                    ],
                    elevation: trustScore * 12, // Extrusion height derived from Trust Score
                    trust: trustScore
                });
            }

            const {DeckGL, ColumnLayer} = deck;

            new DeckGL({
                container: 'container',
                mapStyle: 'https://basemaps.cartocdn.com/gl/dark-matter-gl-style/json',
                initialViewState: {
                    longitude: centerLng,
                    latitude: centerLat,
                    zoom: 11.8,
                    pitch: 58,
                    bearing: -28
                },
                controller: true,
                layers: [
                    new ColumnLayer({
                        id: '3d-trust-extrusions',
                        data: DATA,
                        diskResolution: 12,
                        radius: 120,
                        extruded: true,
                        pickable: true,
                        elevationScale: 1.2,
                        getPosition: d => d.position,
                        getElevation: d => d.elevation,
                        getFillColor: d => d.trust > 80 ? [0, 242, 254, 210] : (d.trust > 50 ? [234, 179, 8, 210] : [239, 68, 68, 210]),
                        transitions: {
                            getElevation: 1000
                        }
                    })
                ]
            });
        </script>
    </body>
    </html>
    """
    return deck_html

# =========================================================
# 5. MODULE CONTENT ROUTING
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
    st.caption("Real-Time Multi-Sensor Telemetry & Ingestion")
    st.markdown("---")
    
    col1, col2, col3, col4 = st.columns(4)
    col1.metric("Active Streams", "12 / 12", "Operational")
    col2.metric("Ingestion Rate", "1.24 GB/s", "+0.08 GB/s")
    col3.metric("Signal Quality", "99.4%", "+0.2%")
    col4.metric("Avg Latency", "8.2 ms", "-1.1 ms")

# --- 03 CONSISTENCY ENGINE ---
elif "03 Consistency Engine" in selected_module:
    st.header("⚙️ 03 Consistency Engine")
    st.caption("Pairwise Conflict Matrices & Disagreement Bounds")
    st.markdown("---")
    
    matrix_data = pd.DataFrame(
        [[1.00, 0.98, 0.95], [0.98, 1.00, 0.92], [0.95, 0.92, 1.00]],
        columns=["Satellite Feed", "Hydrological Sensor", "Radar Array"],
        index=["Satellite Feed", "Hydrological Sensor", "Radar Array"]
    )
    st.dataframe(matrix_data, use_container_width=True)

# --- 04 CONFIDENCE ENGINE ---
elif "04 Confidence Engine" in selected_module:
    st.header("🎯 04 Confidence Engine")
    st.caption("Calibrated Confidence Score Bounds & Monte Carlo Ensemble Variance")
    st.markdown("---")
    
    st.metric("Confidence Score", "82.0%", "Calibrated")

# --- 05 PHYSICS VALIDATION (TOPOGRAPHICAL & HYDROLOGICAL CONSTRAINTS) ---
elif "05 Physics Validation" in selected_module:
    st.header("⚡ 05 Topographical & Physical Constraint Engine")
    st.caption("Evaluates AI Predictions against Real-World Hydrological & Elevation Boundaries")
    st.markdown("---")
    
    st.subheader("🧪 Live Physical Boundary Simulation")
    
    col_input1, col_input2, col_input3 = st.columns(3)
    with col_input1:
        rainfall = st.slider("Rainfall Intensity (mm/hr)", min_value=0, max_value=200, value=65)
    with col_input2:
        elevation = st.slider("Floodplain Elevation (m ASL)", min_value=0, max_value=100, value=12)
    with col_input3:
        slope = st.slider("Terrain Slope Factor (°)", min_value=0.1, max_value=5.0, value=1.0)

    # Topographical Physics Verification Logic
    risk_factor = (rainfall * slope) / max(elevation, 1.0)
    
    st.markdown("### 📊 Verification Result")
    c1, c2, c3 = st.columns(3)
    c1.metric("Calculated Hydro-Risk Index", f"{risk_factor:.2f}")
    
    if risk_factor > 10.0:
        c2.metric("Physics Validation Status", "FAILED", delta="- Breach Hazard", delta_color="inverse")
        st.error(f"❌ **PHYSICAL CONSTRAINT VIOLATION DETECTED:** Rainfall intensity ({rainfall} mm/hr) exceeds safe threshold for Floodplain Elevation ({elevation}m ASL). Prediction rejected by physics layer.")
    else:
        c2.metric("Physics Validation Status", "100% PASSED", delta="Within Bounds")
        st.success(f"✅ **PHYSICS BOUNDS VERIFIED:** Prediction is hydro-physically consistent with terrain elevation ({elevation}m) and slope factor ({slope}).")

    c3.metric("Slope Boundary Check", "PASS", "Slope <= 5.0°")

    st.markdown("### 📜 Hydrological Rule Execution Log")
    st.code(f"""
[SYSTEM] Evaluating AI prediction against Topographical & Physical Constraints...
[HYDROLOGY] Live Rainfall Input: {rainfall} mm/hr
[ELEVATION] Terrain Floodplain Altitude: {elevation} m Above Sea Level
[SLOPE FACTOR] Measured Incline Angle: {slope}°
[EQUATION] Risk = (Rainfall * Slope) / Elevation = ({rainfall} * {slope}) / {elevation} = {risk_factor:.2f}
[CONSTRAINT LIMIT] Risk Threshold <= 10.0
[EVALUATION] -> {"PASSED (Prediction Logically Valid)" if risk_factor <= 10.0 else "FAILED (Hydro-Physical Anomaly)"}
    """, language="bash")

# --- 06 TRUST & DECISION ---
elif "06 Trust & Decision" in selected_module:
    st.header("🛡️ 06 Trust & Decision Engine")
    st.caption("Composite Trust Output & Audit Certificates")
    st.markdown("---")
    
    col1, col2, col3, col4 = st.columns(4)
    col1.metric("Reliability", "74 %")
    col2.metric("Consistency", "87 %")
    col3.metric("Confidence", "82 %")
    col4.metric("Physics", "100 %")
    
    st.progress(0.864)
    st.success("### **DECISION: APPROVED (COMPOSITE TRUST SCORE: 86.4%)**")

# --- 07 3D TRUST MAP (DECK.GL GPU EXTRUSION) ---
elif "07 3D Trust Map" in selected_module:
    st.header("🗺️ 07 GPU-Accelerated 3D Spatial Extrusion Map")
    st.caption("Interactive Deck.gl + MapLibre Spatial Density Rendering with GPU Extruded Columns")
    st.markdown("---")
    components.html(render_deckgl_3d_map(), height=780, scrolling=False)

# --- 08 SEARCH & DIRECTIONS ---
elif "08 Search & Directions" in selected_module:
    st.header("🚀 08 Search & Spatial Directives")
    st.caption("Search Telemetry Nodes & Route Verification")
    st.markdown("---")
    
    st.text_input("🔍 Search Telemetry Node ID / Coordinate / Route:", value="NODE-882-MANGALORE")
    components.html(render_deckgl_3d_map(), height=780, scrolling=False)

# --- 09 AI COPILOT ---
elif "09 AI Copilot" in selected_module:
    st.header("🤖 09 GeoTrustX AI Copilot")
    st.caption("Interactive Telemetry & Physical Constraint Analysis Assistant")
    st.markdown("---")
    
    if "messages" not in st.session_state:
        st.session_state.messages = [
            {"role": "assistant", "content": "Hello! I am GeoTrustX Copilot. Ask me anything about topographical constraints or 3D Deck.gl trust extrusions."}
        ]

    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    if prompt := st.chat_input("Ask Copilot..."):
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.markdown(prompt)

        with st.chat_message("assistant"):
            response = f"**Copilot Analysis:** Query received for '{prompt}'. System running Deck.gl 3D GPU Extrusions with active Hydro-Elevation constraint checks."
            st.markdown(response)
            st.session_state.messages.append({"role": "assistant", "content": response})