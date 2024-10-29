import os
import uuid
from fastapi import APIRouter, FastAPI, \
WebSocket, WebSocketDisconnect, Request, HTTPException, Depends
from ..socket.utils import get_token
from ..socket.connection import ConnectionManager

chat = APIRouter()
manager =  ConnectionManager()

# @route  POST /token
# @desc   Route to generate chat token
# @access Public

@chat.post("/token")
async def token_generator(name: str, request: Request):
    if name == "":
        raise HTTPException(status_code=400, 
                            detail={"loc": "name", "msg":"Enter a valid name"})
    token = str(uuid.uuid4())
    data = {"name": name, "token": token}

    return data


# POST  /refresh_token
# Route to refresh token
# Public

@chat.post("/refresh_token")
async def refresh_token(request: Request):
    return None


# websocket /chat
# Socket for the chatbot
# Public access
@chat.websocket("/chat")
async def websocket_endpoint(websocket: WebSocket, 
                             token: str = Depends(get_token)):
    await manager.connect(websocket)
    try:
        while True:
            data = await websocket.receive_text()
            print(data)
            await manager.send_personal_message(
                f"Response: Simulating response from the GPT service", websocket)
    except WebSocketDisconnect:
        manager.disconnect(websocket)
    return None