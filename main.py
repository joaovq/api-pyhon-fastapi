from typing import Annotated
from fastapi import Depends, FastAPI, WebSocket, WebSocketDisconnect
from fastapi.staticfiles import StaticFiles
from core.sockets.conn_socket import ConnectionManager, get_manager
from database import create_tables
import person
from schemas.user import Subscription
import user
from core.auth.scheme import oauth2_scheme


create_tables()

app = FastAPI()

@app.get("/")
async def root(token: Annotated[str, Depends(oauth2_scheme)]):
    return {"message": "Hello World", "token": token}

app.mount("/static", StaticFiles(directory='static'), name="static")
# This is amazing
app.include_router(
    router=user.router,
    prefix='',
    tags=["users"],
    dependencies=[],
    responses={418: {"description": "I'm a teapot"}},
)
app.include_router(person.router)

# Web hooks
@app.webhooks.post('new-subscription')
async def created_user(body: Subscription):
    """
    When created user, send message for sms or email soon 
    """
    return print(body)

@app.websocket("/ws/{client_id}")
async def websocket_endpoint(websocket: WebSocket, client_id: int, manager:Annotated[ConnectionManager, Depends(get_manager)]):
    await manager.connect(websocket)
    try:
        while True:
            data = await websocket.receive_text()
            await manager.send_personal_message(f"You wrote: {data}", websocket)
            await manager.broadcast(f"Client #{client_id} says: {data}")
    except WebSocketDisconnect:
        manager.disconnect(websocket)
        await manager.broadcast(f"Client #{client_id} left the chat")