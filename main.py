from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from database import create_tables
from person import person


create_tables()

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}

app.mount("/static", StaticFiles(directory='static'), name="static")
app.mount('', person, name='person')