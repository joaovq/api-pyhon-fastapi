## Create venv

``` bash
python -m venv .venv
```
Activate the virtual environment:
Linux/Mac OS X: `source ./.venv/bin/activate`
Windows (PowerShell): `.\.venv\Scripts\activate.ps1`.
Install dependencies in your virtualenv using pip and setup a git hook to run tests before committing code changes with pre-commit hooks, see [pre
Install dependencies in your virtualenv using pip or poetry, depending on which you prefer to use for development and testing of this project.
Install dependencies in your virtualenv with pipenv or poetry, and then install this package into editable mode using setuptools (`pip install --editable .`)

## Install fast api

``` bash
pip install "fastapi[all]" 
```

## Install pytest

``` bash
pip install pytest 

```

## Manage database SQL

``` bash

pip install sqlalchemy

```

### Import the SQLAlchemy parts 

``` python
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

SQLALCHEMY_DATABASE_URL = "sqlite:///./sql_app.db"
# SQLALCHEMY_DATABASE_URL = "postgresql://user:password@postgresserver/db"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

```


### Create a database URL for SQLAlchemy
- [Docs](https://fastapi.tiangolo.com/tutorial/sql-databases/)

``` python
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

SQLALCHEMY_DATABASE_URL = "sqlite:///./sql_app.db"
# SQLALCHEMY_DATABASE_URL = "postgresql://user:password@postgresserver/db"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

```

If you were using a PostgreSQL database instead, you would just have to uncomment the line:


``` python
SQLALCHEMY_DATABASE_URL = "postgresql://user:password@postgresserver/db"
```
## Run migrations with Alembic
Alembic is an open source tool that allows us to easily manage our database schema and make changes as we need them without having to worry about
Migrations for sqlalchemy
[Alembic Docs](https://alembic.sqlalchemy.org/en/latest/#installation)
``` bash
pip install alembic==1.4.3
python -m venv .venv # or use `virtualenv` if not installed on your system already
source ./.venv/bin/activate  # Linux shell (Bash, ZSH, etc.) only
(.venv) $ pip install alembic==1.4.3
(.venv) $ alembic init alembic
(.venv) $ cd alembic && touch env.py
```
Run first migrations
 - Create script for migration
```bash
alembic revision -m "message"
```
- Execute migration
```bash
alembic upgrade head
```

Run after migrations
 - Create script for migration
```bash
alembic revision -m "message"
```
- Execute migration
```bash
alembic upgrade head
```

## OAuth2 
- [Docs Security](https://fastapi.tiangolo.com/tutorial/security/oauth2-jwt/)

## Install multipart
- [Multipart docs](https://github.com/encode/starlette-multipart)
```bash
pip install python-multipart
```

``` bash
pip install "python-jose[cryptography]"
```

## Password hashing¶
``` bash
pip install "passlib[bcrypt]"
```

# Handle JWT tokens¶
Import the modules installed.

Create a random secret key that will be used to sign the JWT tokens.

To generate a secure random secret key use the command:

``` bash
openssl rand -hex 32
```

### Web sockets 

#### Docs
- [Web Sockets](https://fastapi.tiangolo.com/advanced/websockets/)

``` bash
pip install websockets
```

``` python
from fastapi import FastAPI, WebSocket
from fastapi.responses import HTMLResponse

app = FastAPI()

html = """
<!DOCTYPE html>
<html>
    <head>
        <title>Chat</title>
    </head>
    <body>
        <h1>WebSocket Chat</h1>
        <form action="" onsubmit="sendMessage(event)">
            <input type="text" id="messageText" autocomplete="off"/>
            <button>Send</button>
        </form>
        <ul id='messages'>
        </ul>
        <script>
            var ws = new WebSocket("ws://localhost:8000/ws");
            ws.onmessage = function(event) {
                var messages = document.getElementById('messages')
                var message = document.createElement('li')
                var content = document.createTextNode(event.data)
                message.appendChild(content)
                messages.appendChild(message)
            };
            function sendMessage(event) {
                var input = document.getElementById("messageText")
                ws.send(input.value)
                input.value = ''
                event.preventDefault()
            }
        </script>
    </body>
</html>
"""


@app.get("/")
async def get():
    return HTMLResponse(html)


@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    while True:
        data = await websocket.receive_text()
        await websocket.send_text(f"Message text was: {data}")

```

#### Handling disconnections and multiple clients¶

When a WebSocket connection is closed, the await websocket.receive_text() will raise a WebSocketDisconnect exception, which you can then catch and handle like in this example.



```python
from fastapi import FastAPI, WebSocket, WebSocketDisconnect
from fastapi.responses import HTMLResponse

app = FastAPI()

html = """
<!DOCTYPE html>
<html>
    <head>
        <title>Chat</title>
    </head>
    <body>
        <h1>WebSocket Chat</h1>
        <h2>Your ID: <span id="ws-id"></span></h2>
        <form action="" onsubmit="sendMessage(event)">
            <input type="text" id="messageText" autocomplete="off"/>
            <button>Send</button>
        </form>
        <ul id='messages'>
        </ul>
        <script>
            var client_id = Date.now()
            document.querySelector("#ws-id").textContent = client_id;
            var ws = new WebSocket(`ws://localhost:8000/ws/${client_id}`);
            ws.onmessage = function(event) {
                var messages = document.getElementById('messages')
                var message = document.createElement('li')
                var content = document.createTextNode(event.data)
                message.appendChild(content)
                messages.appendChild(message)
            };
            function sendMessage(event) {
                var input = document.getElementById("messageText")
                ws.send(input.value)
                input.value = ''
                event.preventDefault()
            }
        </script>
    </body>
</html>
"""


class ConnectionManager:
    def __init__(self):
        self.active_connections: list[WebSocket] = []

    async def connect(self, websocket: WebSocket):
        await websocket.accept()
        self.active_connections.append(websocket)

    def disconnect(self, websocket: WebSocket):
        self.active_connections.remove(websocket)

    async def send_personal_message(self, message: str, websocket: WebSocket):
        await websocket.send_text(message)

    async def broadcast(self, message: str):
        for connection in self.active_connections:
            await connection.send_text(message)


manager = ConnectionManager()


@app.get("/")
async def get():
    return HTMLResponse(html)


@app.websocket("/ws/{client_id}")
async def websocket_endpoint(websocket: WebSocket, client_id: int):
    await manager.connect(websocket)
    try:
        while True:
            data = await websocket.receive_text()
            await manager.send_personal_message(f"You wrote: {data}", websocket)
            await manager.broadcast(f"Client #{client_id} says: {data}")
    except WebSocketDisconnect:
        manager.disconnect(websocket)
        await manager.broadcast(f"Client #{client_id} left the chat")
```

### For test of websocket
 - [Pie socket](https://www.piesocket.com/websocket-tester)