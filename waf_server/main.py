from fastapi import FastAPI, Request, WebSocket, WebSocketDisconnect, Response
from fastapi.middleware.cors import CORSMiddleware
from rules import quick_signature_check
from ai_analyzer import analyze_payload_with_ai

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

active_connections: list[WebSocket] = []

@app.websocket("/ws/logs")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    active_connections.append(websocket)
    try:
        while True:
            await websocket.receive_text()
    except WebSocketDisconnect:
        active_connections.remove(websocket)

async def broadcast_log(log_data: dict):
    for connection in active_connections:
        try:
            await connection.send_json(log_data)
        except Exception:
            pass

@app.api_route("/{path:path}", methods=["GET", "POST", "PUT", "DELETE"])
async def waf_proxy(request: Request, path: str):
    body = await request.body()
    body_str = body.decode("utf-8", errors="ignore")
    headers = dict(request.headers)
    
    # 1. Quick Signature Check
    local_check = quick_signature_check(body_str)
    is_blocked = False
    threat_type = local_check["type"]
    reasoning = "Signature Rule Triggered"
    
    if local_check["flagged"]:
        is_blocked = True
    elif body_str.strip(): # 2. AI Check for non-empty requests
        ai_result = analyze_payload_with_ai(body_str, headers)
        if ai_result.get("is_threat") and ai_result.get("confidence_score", 0) > 0.6:
            is_blocked = True
            threat_type = ai_result.get("threat_type", "AI Anomaly")
            reasoning = ai_result.get("reasoning", "Flagged by LLM")

    log_entry = {
        "ip": request.client.host if request.client else "127.0.0.1",
        "path": f"/{path}",
        "method": request.method,
        "blocked": is_blocked,
        "threat_type": threat_type,
        "reasoning": reasoning,
        "payload": body_str[:150]
    }
    await broadcast_log(log_entry)

    if is_blocked:
        return Response(content=f"Blocked by ShadowWall AI WAF. Reason: {threat_type}", status_code=403)

    return Response(content='{"status": "success", "message": "Request allowed by WAF"}', status_code=200, media_type="application/json")
