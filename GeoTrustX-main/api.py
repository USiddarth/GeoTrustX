from fastapi import FastAPI, WebSocket, WebSocketDisconnect
from fastapi.responses import HTMLResponse, FileResponse
import os

app = FastAPI(title="GeoTrustX API")

# Serve the main dashboard at the root URL (http://127.0.0.1:8000/)
@app.get("/", response_class=HTMLResponse)
async def get_dashboard():
    dashboard_path = os.path.join(os.path.dirname(__file__), "dashboard.html")
    if os.path.exists(dashboard_path):
        with open(dashboard_path, "r", encoding="utf-8") as f:
            return f.read()
    return HTMLResponse(content="<h1>dashboard.html not found!</h1>", status_code=404)

# Also serve at /dashboard for convenience
@app.get("/dashboard", response_class=HTMLResponse)
async def get_dashboard_alias():
    return await get_dashboard()

# WebSocket Endpoint for live streaming telemetry
@app.websocket("/ws/stream")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    try:
        while True:
            data = await websocket.receive_json()
            # Echo back basic response structure
            await websocket.send_json({
                "composite_trust": 86,
                "reliability": 80,
                "consistency": 87,
                "confidence": 82,
                "physics_score": 100,
                "ensemble_stats": {"mean_p": 0.69, "std_dev": 0.090}
            })
    except WebSocketDisconnect:
        pass