from typing import Annotated
from fastapi import Depends, FastAPI
from fastapi.staticfiles import StaticFiles
from database import create_tables
import person
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