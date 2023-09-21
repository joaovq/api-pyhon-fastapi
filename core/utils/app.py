from fastapi import FastAPI
import os
from dotenv import load_dotenv
load_dotenv()

def create_app(
    debug= True if os.environ.get('DEBUG', "1") == "1" else False,
    version="0.1.0"
) -> FastAPI:
    return FastAPI(
        debug=debug,
        version=version,    
    )