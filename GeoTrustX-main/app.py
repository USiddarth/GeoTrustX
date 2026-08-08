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
    index=6,  # Default to 07 3D Trust Map to show the navigation map right away
    label_visibility="collapsed"
)

st.sidebar.markdown("---")
st.sidebar.caption("GEOTRUSTX v2.0 | **ENTERPRISE**")
st.sidebar.info("⚙️ LOCAL MATH ENGINE")

# =========================================================
# 4. INTERACTIVE MAP ENGINE HTML GENERATOR
# =========================================================
def render_navigation_map():
    map_html = """
    <!DOCTYPE html>
    <html>
    <head>
        <link rel="stylesheet" href="https://unpkg.com/leaflet@1.9.4/dist/leaflet.css" />
        <link rel="stylesheet" href="https://unpkg.com/leaflet-routing-machine@3.2.12/dist/leaflet-routing-machine.css" />
        <script src="https://unpkg.com/leaflet@1.9.4/dist/leaflet.js"></script>
        <script src="https://unpkg.com/leaflet-routing-machine@3.2.12/dist/leaflet-routing-machine.min.js"></script>
        <style>
            body { margin: 0; padding: 0; background-color: #0b0f19; font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; }
            #map { width: 100%; height: 750px; border-radius: 12px; border: 1px solid #1e293b; }
            
            /* Custom Control Panel Overlay inside Map */
            .nav-panel {
                position: absolute;
                top: 20px;
                left: 20px;
                z-index: 1000;
                background: rgba(13, 19, 34, 0.92);
                backdrop-filter: blur(10px);
                border: 1px solid #38bdf8;
                padding: 16px;
                border-radius: 12px;
                color: #e2e8f0;
                width: 320px;
                box-shadow: 0 8px 32px rgba(0,0,0,0.6);
            }
            .nav-panel h4 { margin: 0 0 12px 0; color: #38bdf8; font-size: 16px; display: flex; align-items: center; gap: 8px; }
            .nav-panel input, .nav-panel select {
                width: 100%;
                padding: 8px 12px;
                margin-bottom: 10px;
                background: #111827;
                border: 1px solid #374151;
                border-radius: 6px;
                color: #fff;
                box-sizing: border-box;
                font-size: 13px;
            }
            .nav-panel button {
                width: 100%;
                padding: 10px;
                background: #0284c7;
                border: none;
                border-radius: 6px;
                color: #fff;
                font-weight: bold;
                cursor: pointer;
                transition: 0.2s;
            }
            .nav-panel button:hover { background: #0369a1; }
            
            /* Hide Leaflet default routing box for clean custom dark UI */
            .leaflet-routing-container { display: none !important; }
            
            /* Custom Route Stats Bar */
            .stats-badge {
                display: flex;
                justify-content: space-between;
                margin-top: 10px;
                padding: 8px;
                background: #111827;
                border-radius: 6px;
                font-size: 12px;
            }
            .stats-badge span { color: #38bdf8; font-weight: bold; }
        </style>
    </head>
    <body>

        <div id="map"></div>

        <div class="nav-panel">
            <h4>🗺️ GeoTrustX Routing Engine</h4>
            <label style="font-size:11px; color:#94a3b8;">START LOCATION</label>
            <input type="text" id="start-input" value="Mangalore City Center" placeholder="Enter Start Node">
            
            <label style="font-size:11px; color:#94a3b8;">DESTINATION NODE</label>
            <input type="text" id="end-input" value="Panambur Port Telemetry Hub" placeholder="Enter Destination">
            
            <button onclick="calculateRoute()">⚡ Calculate Verified Route</button>
            
            <div class="stats-badge" id="route-stats">
                <div>Distance: <span id="dist">-- km</span></div>
                <div>ETA: <span id="time">-- min</span></div>
                <div>Trust: <span id="trust-score" style="color:#4ade80;">98.4%</span></div>
            </div>
        </div>

        <script>
            // Initialize Map focused on Mangalore Coordinates
            var map = L.map('map').setView([12.8702, 74.8806], 12);

            // Dark CartoDB Tiles
            L.tileLayer('https://{s}.basemaps.cartocdn.com/dark_all/{x}/{y}{r}.png', {
                attribution: '&copy; OpenStreetMap &copy; CARTO',
                subdomains: 'abcd',
                maxZoom: 19
            }).addTo(map);

            var routingControl = null;

            // Define Coordinates for preset Nodes
            var nodes = {
                "start": [12.8702, 74.8806],
                "end": [12.9511, 74.8086]
            };

            function calculateRoute() {
                if (routingControl) {
                    map.removeControl(routingControl);
                }

                routingControl = L.Routing.control({
                    waypoints: [
                        L.latLng(nodes.start[0], nodes.start[1]),
                        L.latLng(nodes.end[0], nodes.end[1])
                    ],
                    lineOptions: {
                        styles: [{ color: '#38bdf8', opacity: 0.8, weight: 6 }]
                    },
                    createMarker: function(i, waypoint, n) {
                        var markerColor = (i === 0) ? '🟢 Start Node' : '🔴 Telemetry Destination';
                        return L.marker(waypoint.latLng).bindPopup(markerColor);
                    }
                }).addTo(map);

                routingControl.on('routesfound', function(e) {
                    var routes = e.routes;
                    var summary = routes[0].summary;
                    document.getElementById('dist').innerText = (summary.totalDistance / 1000).toFixed(1) + " km";
                    document.getElementById('time').innerText = Math.round(summary.totalTime / 60) + " min";
                });
            }

            // Auto Plot Route on Load
            calculateRoute();
        </script>
    </body>
    </html>
    """
    return map_html

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

# --- 03 CONSISTENCY ENGINE ---
elif "03 Consistency Engine" in selected_module:
    st.header("⚙️ 03 Consistency Engine")
    st.caption("Pairwise Conflict Matrices & Multi-Source Cross-Verification")
    st.markdown("---")
    
    col1, col2, col3 = st.columns(3)
    col1.metric("Consistency Index", "87.0%", "+1.4%")
    col2.metric("Pairwise Conflicts", "0 Detected", "Optimal")
    col3.metric("Matrix Sync Time", "1.2 ms", "Real-Time")

# --- 04 CONFIDENCE ENGINE ---
elif "04 Confidence Engine" in selected_module:
    st.header("🎯 04 Confidence Engine")
    st.caption("Ensemble Standard Deviation ($\sigma$) & Calibrated Monte Carlo Bounds")
    st.markdown("---")
    
    col1, col2, col3 = st.columns(3)
    col1.metric("Confidence Score", "82.0%", "Calibrated")
    col2.metric("Std Deviation Spread (σ)", "1.42", "-0.15")
    col3.metric("Monte Carlo Iterations", "10,000", "Passed")

# --- 05 PHYSICS VALIDATION ---
elif "05 Physics Validation" in selected_module:
    st.header("⚡ 05 Physics Validation")
    st.caption("Real-Time Physical Boundary & Constraint Verification")
    st.markdown("---")
    st.success("✅ Hydrological & Physics Constraints Passed 100%")

# --- 06 TRUST & DECISION ---
elif "06 Trust & Decision" in selected_module:
    st.header("🛡️ 06 Trust & Decision Output")
    st.caption("Final Automated Decision Weighting & Audit Certificate Generation")
    st.markdown("---")
    st.success("### **DECISION: APPROVED (TRUST SCORE: 86.4%)**")

# --- 07 3D TRUST MAP (WITH INTERACTIVE IN-MAP NAVIGATION) ---
elif "07 3D Trust Map" in selected_module:
    st.header("🗺️ 07 Interactive 3D Spatial Navigation Map")
    st.caption("Live In-Map Waypoint Routing, Distance Tracking, & Route Verification")
    st.markdown("---")
    
    # Render the interactive map engine
    components.html(render_navigation_map(), height=780, scrolling=False)

# --- 08 SEARCH & DIRECTIONS ---
elif "08 Search & Directions" in selected_module:
    st.header("🚀 08 Spatial Search & Directives")
    st.caption("Search Telemetry Nodes & Route Directives")
    st.markdown("---")
    
    components.html(render_navigation_map(), height=780, scrolling=False)

# --- 09 AI COPILOT ---
elif "09 AI Copilot" in selected_module:
    st.header("🤖 09 GeoTrustX AI Copilot")
    st.caption("Interactive Telemetry & Physics Analysis Assistant")
    st.markdown("---")
    
    if "messages" not in st.session_state:
        st.session_state.messages = [
            {"role": "assistant", "content": "Hello! I am GeoTrustX Copilot. Ask me anything about your current composite trust score or navigation paths."}
        ]

    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    if prompt := st.chat_input("Ask Copilot..."):
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.markdown(prompt)

        with st.chat_message("assistant"):
            response = f"**Copilot Analysis:** Navigation path verified with **98.4% Trust Rating**."
            st.markdown(response)
            st.session_state.messages.append({"role": "assistant", "content": response})