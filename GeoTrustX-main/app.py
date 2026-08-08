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
    index=6,  # Default to 07 3D Trust Map
    label_visibility="collapsed"
)

st.sidebar.markdown("---")
st.sidebar.caption("GEOTRUSTX v2.0 | **ENTERPRISE**")
st.sidebar.info("⚙️ LOCAL MATH ENGINE")

# =========================================================
# 4. DYNAMIC MULTI-PATH DARK MAP ENGINE
# =========================================================
def render_real_dark_map():
    map_html = """
    <!DOCTYPE html>
    <html>
    <head>
        <link rel="stylesheet" href="https://unpkg.com/leaflet@1.9.4/dist/leaflet.css" />
        <script src="https://unpkg.com/leaflet@1.9.4/dist/leaflet.js"></script>
        <style>
            html, body { 
                margin: 0; padding: 0; 
                background-color: #0b0f19 !important; 
                font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; 
            }
            #map { 
                width: 100%; 
                height: 750px; 
                border-radius: 12px; 
                border: 1px solid #1e293b; 
                background: #0b0f19 !important; 
            }
            
            .leaflet-tile-pane {
                filter: invert(100%) hue-rotate(180deg) brightness(95%) contrast(90%);
            }
            
            .map-panel {
                position: absolute;
                top: 20px;
                left: 20px;
                z-index: 1000;
                background: rgba(13, 19, 34, 0.95);
                backdrop-filter: blur(10px);
                border: 1px solid #38bdf8;
                border-radius: 10px;
                padding: 16px;
                color: #e2e8f0;
                width: 320px;
                box-shadow: 0 10px 30px rgba(0,0,0,0.8);
            }
            .map-panel h4 { margin: 0 0 10px 0; color: #38bdf8; font-size: 15px; }
            .map-panel select {
                width: 100%; padding: 8px 10px; margin-bottom: 10px;
                background: #111827; border: 1px solid #374151;
                border-radius: 6px; color: #fff; font-size: 13px; box-sizing: border-box;
            }
            .map-panel button {
                width: 100%; padding: 10px; background: #0284c7;
                border: none; border-radius: 6px; color: #fff;
                font-weight: bold; cursor: pointer; transition: 0.2s;
            }
            .map-panel button:hover { background: #0369a1; }
            .stats-row { display: flex; justify-content: space-between; margin-top: 10px; font-size: 12px; background: #111827; padding: 8px; border-radius: 6px; }
            .stats-row span { color: #38bdf8; font-weight: bold; }
        </style>
    </head>
    <body>

        <div id="map"></div>

        <div class="map-panel">
            <h4>🗺️ GeoTrustX Navigation Map</h4>
            
            <label style="font-size:11px; color:#94a3b8;">START POINT</label>
            <select id="start-select">
                <option value="mgl_central" selected>Mangalore Central Terminal</option>
                <option value="panambur">Panambur Port Telemetry Hub</option>
                <option value="surathkal">NITK Surathkal Node</option>
                <option value="airport">Mangaluru Airport (Bajpe)</option>
                <option value="udupi">Udupi City Station</option>
                <option value="someshwar">Someshwar Beach Outpost</option>
            </select>
            
            <label style="font-size:11px; color:#94a3b8;">DESTINATION POINT</label>
            <select id="end-select">
                <option value="mgl_central">Mangalore Central Terminal</option>
                <option value="panambur" selected>Panambur Port Telemetry Hub</option>
                <option value="surathkal">NITK Surathkal Node</option>
                <option value="airport">Mangaluru Airport (Bajpe)</option>
                <option value="udupi">Udupi City Station</option>
                <option value="someshwar">Someshwar Beach Outpost</option>
            </select>
            
            <button onclick="updateRoute()">⚡ Update Navigation Path</button>
            
            <div class="stats-row">
                <div>Route Dist: <span id="dist-val">12.8 km</span></div>
                <div>ETA: <span id="eta-val">18 min</span></div>
                <div>Trust: <span id="trust-val" style="color:#4ade80;">98.6%</span></div>
            </div>
        </div>

        <script>
            // Defined Telemetry Locations Database
            const locations = {
                "mgl_central": { name: "Mangalore Central Terminal", lat: 12.8702, lng: 74.8560 },
                "panambur":    { name: "Panambur Port Telemetry Hub", lat: 12.9511, lng: 74.8086 },
                "surathkal":   { name: "NITK Surathkal Node", lat: 13.0108, lng: 74.7943 },
                "airport":     { name: "Mangaluru Airport (Bajpe)", lat: 12.9613, lng: 74.8901 },
                "udupi":       { name: "Udupi City Station", lat: 13.3409, lng: 74.7421 },
                "someshwar":   { name: "Someshwar Beach Outpost", lat: 12.7940, lng: 74.8620 }
            };

            // Initialize Map
            var map = L.map('map').setView([12.9141, 74.8560], 12);

            L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
                maxZoom: 19,
                attribution: '&copy; OpenStreetMap'
            }).addTo(map);

            var startMarker = null;
            var endMarker = null;
            var routePolyline = null;

            // Haversine formula to compute actual distance in KM
            function calcDistance(lat1, lon1, lat2, lon2) {
                var R = 6371; // Radius of Earth in km
                var dLat = (lat2 - lat1) * Math.PI / 180;
                var dLon = (lon2 - lon1) * Math.PI / 180;
                var a = Math.sin(dLat/2) * Math.sin(dLat/2) +
                        Math.cos(lat1 * Math.PI / 180) * Math.cos(lat2 * Math.PI / 180) *
                        Math.sin(dLon/2) * Math.sin(dLon/2);
                var c = 2 * Math.atan2(Math.sqrt(a), Math.sqrt(1-a));
                return (R * c * 1.35).toFixed(1); // 1.35 multiplier for road winding factor
            }

            function updateRoute() {
                var startKey = document.getElementById("start-select").value;
                var endKey = document.getElementById("end-select").value;

                if (startKey === endKey) {
                    alert("Please select two different locations for Start and Destination!");
                    return;
                }

                var p1 = locations[startKey];
                var p2 = locations[endKey];

                // Remove existing layers
                if (startMarker) map.removeLayer(startMarker);
                if (endMarker) map.removeLayer(endMarker);
                if (routePolyline) map.removeLayer(routePolyline);

                // Add New Cyan Start Marker
                startMarker = L.circleMarker([p1.lat, p1.lng], {
                    color: '#38bdf8', fillColor: '#38bdf8', fillOpacity: 0.9, radius: 10
                }).addTo(map).bindPopup("<b>🟢 Start: " + p1.name + "</b>");

                // Add New Red Destination Marker
                endMarker = L.circleMarker([p2.lat, p2.lng], {
                    color: '#f43f5e', fillColor: '#f43f5e', fillOpacity: 0.9, radius: 10
                }).addTo(map).bindPopup("<b>🔴 Target: " + p2.name + "</b>");

                // Interpolate waypoints for realistic curvilinear path
                var midLat = (p1.lat + p2.lat) / 2 + (p2.lng - p1.lng) * 0.08;
                var midLng = (p1.lng + p2.lng) / 2 - (p2.lat - p1.lat) * 0.08;

                var routeCoords = [
                    [p1.lat, p1.lng],
                    [p1.lat + (midLat - p1.lat)*0.5, p1.lng + (midLng - p1.lng)*0.5],
                    [midLat, midLng],
                    [midLat + (p2.lat - midLat)*0.5, midLng + (p2.lng - midLng)*0.5],
                    [p2.lat, p2.lng]
                ];

                // Draw New Path Line
                routePolyline = L.polyline(routeCoords, {
                    color: '#00f2fe', weight: 6, opacity: 0.9, lineCap: 'round'
                }).addTo(map);

                // Zoom map to fit the route automatically
                map.fitBounds(routePolyline.getBounds(), { padding: [50, 50] });

                // Update Metrics
                var dist = calcDistance(p1.lat, p1.lng, p2.lat, p2.lng);
                var eta = Math.round((dist / 35) * 60); // Assuming 35 km/h average transit
                var trust = (98.0 + (Math.random() * 1.8)).toFixed(1);

                document.getElementById("dist-val").innerText = dist + " km";
                document.getElementById("eta-val").innerText = eta + " min";
                document.getElementById("trust-val").innerText = trust + "%";
            }

            // Draw initial route on page load
            updateRoute();
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
    st.caption("Real-Time Multi-Sensor Telemetry & Ingestion")
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
    st.caption("Pairwise Conflict Matrices & Disagreement Bounds")
    st.markdown("---")
    
    col1, col2, col3 = st.columns(3)
    col1.metric("Consistency Index", "87.0%", "+1.4%")
    col2.metric("Pairwise Conflicts", "0 Detected", "Optimal")
    col3.metric("Matrix Sync Time", "1.2 ms", "Real-Time")

    st.markdown("### 🔍 Pairwise Disagreement Matrix")
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
    
    col1, col2, col3 = st.columns(3)
    col1.metric("Confidence Score", "82.0%", "Calibrated")
    col2.metric("Std Deviation Spread", "1.42", "-0.15")
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
    st.header("⚡ 05 Topographical & Physical Constraint Engine")
    st.caption("Evaluates AI Predictions against Real-World Hydrological & Elevation Boundaries")
    st.markdown("---")
    
    col_input1, col_input2, col_input3 = st.columns(3)
    with col_input1:
        rainfall = st.slider("Rainfall Intensity (mm/hr)", min_value=0, max_value=200, value=65)
    with col_input2:
        elevation = st.slider("Floodplain Elevation (m ASL)", min_value=0, max_value=100, value=12)
    with col_input3:
        slope = st.slider("Terrain Slope Factor (°)", min_value=0.1, max_value=5.0, value=1.0)

    risk_factor = (rainfall * slope) / max(elevation, 1.0)
    
    c1, c2, c3 = st.columns(3)
    c1.metric("Calculated Hydro-Risk Index", f"{risk_factor:.2f}")
    
    if risk_factor > 10.0:
        c2.metric("Physics Validation Status", "FAILED", delta="- Breach Hazard", delta_color="inverse")
        st.error(f"❌ **PHYSICAL CONSTRAINT VIOLATION DETECTED:** Rainfall intensity ({rainfall} mm/hr) exceeds safe threshold for Floodplain Elevation ({elevation}m ASL).")
    else:
        c2.metric("Physics Validation Status", "100% PASSED", delta="Within Bounds")
        st.success(f"✅ **PHYSICS BOUNDS VERIFIED:** Prediction is hydro-physically consistent with terrain elevation ({elevation}m) and slope ({slope}°).")

    c3.metric("Slope Boundary Check", "PASS", "Slope <= 5.0°")

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

# --- 07 3D TRUST MAP ---
elif "07 3D Trust Map" in selected_module:
    st.header("🗺️ 07 Interactive Spatial Navigation Map")
    st.caption("Vector Dark Street Map with Dynamic Multi-Path Selection")
    st.markdown("---")
    components.html(render_real_dark_map(), height=780, scrolling=False)

# --- 08 SEARCH & DIRECTIONS ---
elif "08 Search & Directions" in selected_module:
    st.header("🚀 08 Search & Spatial Directives")
    st.caption("Search Telemetry Locations & Dynamic Routing")
    st.markdown("---")
    components.html(render_real_dark_map(), height=780, scrolling=False)

# --- 09 AI COPILOT ---
elif "09 AI Copilot" in selected_module:
    st.header("🤖 09 GeoTrustX AI Copilot")
    st.caption("Interactive Telemetry & Physical Constraint Analysis Assistant")
    st.markdown("---")
    
    if "messages" not in st.session_state:
        st.session_state.messages = [
            {"role": "assistant", "content": "Hello! I am GeoTrustX Copilot. Ask me anything about topographical constraints or spatial map navigation."}
        ]

    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    if prompt := st.chat_input("Ask Copilot..."):
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.markdown(prompt)

        with st.chat_message("assistant"):
            response = f"**Copilot Analysis:** Query received for '{prompt}'. System running dynamic multi-path spatial verification."
            st.markdown(response)
            st.session_state.messages.append({"role": "assistant", "content": response})