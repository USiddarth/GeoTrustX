# 🌍 GeoTrustX

**Trust & Verification Layer for Geospatial AI**

Current AI systems ask *what happened*. GeoTrustX asks — *can you trust it?* 
GeoTrustX is a robust, multi-layer verification engine that sits on top of your geospatial prediction models. It scores source reliability, checks sensor agreement, calibrates confidence, validates physical constraints, and outputs a single, audited Trust Score.

---

## ✨ Features

* **📡 Source Ingestion & Reliability:** Real-time scoring of data sources (Optical, SAR, Weather, Ground) based on quality, noise interference, and temporal decay.
* **🔗 Consistency Engine:** Cross-checks every source against one another using upper-triangle pairwise disagreement matrices.
* **📊 Confidence Engine:** Converts deep-ensemble standard deviation spread ($\sigma$) into calibrated confidence bounds.
* **🌊 Physics & Hydrology Validation:** Evaluates AI predictions against strict topographical and physical constraints (e.g., rainfall vs. flood plain elevation).
* **🗺️ 3D Trust Map:** GPU-accelerated interactive 3D spatial extrusion mapping built with Deck.gl and MapLibre.
* **🤖 AI Copilot:** Context-aware geospatial AI assistant for querying session telemetry and sensor conflicts.

---

## 🛠️ Tech Stack

* **Frontend:** Streamlit, HTML5, Tailwind CSS, Chart.js
* **Backend:** FastAPI, Uvicorn, Python, WebSockets
* **Geospatial Rendering:** Deck.gl, MapLibre GL JS, CARTO Basemaps
* **Data Processing:** NumPy, Pandas

---

## 🚀 How to Run Locally

### 1. Clone the repository
```bash
git clone [https://github.com/tspratham09-hue/GeoTrustX.git](https://github.com/tspratham09-hue/GeoTrustX.git)
cd GeoTrustX
