import json
import pathlib
from fastapi import FastAPI, WebSocket, WebSocketDisconnect
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import HTMLResponse, FileResponse
from engine import GeoTrustXEngine

app = FastAPI(title="GeoTrustX Engine API", version="2.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

engine = GeoTrustXEngine()

# Serve dashboard.html at http://127.0.0.1:8000/
@app.get("/")
async def get_dashboard():
    html_file = pathlib.Path("dashboard.html")
    if html_file.exists():
        return FileResponse("dashboard.html")
    return HTMLResponse(content="<h1>dashboard.html not found in folder</h1>")

@app.websocket("/ws/stream")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    print("--> Client connected to WebSocket stream!")
    try:
        while True:
            raw_data = await websocket.receive_text()
            payload = json.loads(raw_data)
            
            sources = payload.get("sources", {})
            probs = [s["pEvent"] for s in sources.values()]
            physics_input = payload.get("physics", {})

            # Execute Engine Math
            rel_scores = engine.compute_reliability(sources)
            avg_rel = sum(rel_scores.values()) / len(rel_scores) if rel_scores else 0
            
            consistency_score, max_conflict, matrix = engine.compute_pairwise_consistency(probs)
            conf_stats = engine.compute_ensemble_confidence(probs)
            phys_mult, phys_msg = engine.validate_physics_constraints(
                physics_input.get("rain", 0),
                physics_input.get("slope", 0),
                conf_stats["mean_p"]
            )
            
            physics_score = 100.0 * phys_mult
            composite_trust = (avg_rel * 0.25 + consistency_score * 0.25 + conf_stats["confidence_score"] * 0.25 + physics_score * 0.25)

            matrix_list = matrix.tolist() if hasattr(matrix, 'tolist') else matrix

            response = {
                "composite_trust": round(composite_trust, 1),
                "reliability": round(avg_rel, 1),
                "consistency": round(consistency_score, 1),
                "confidence": conf_stats["confidence_score"],
                "physics_score": round(physics_score, 1),
                "physics_message": phys_msg,
                "conflict_matrix": matrix_list,
                "ensemble_stats": conf_stats
            }

            await websocket.send_text(json.dumps(response))
    except WebSocketDisconnect:
        print("<-- Client disconnected")
    except Exception as e:
        print("WebSocket Error:", e)