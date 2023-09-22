from fastapi import FastAPI
from fastapi.testclient import TestClient
from fastapi import status 
from main import app


client = TestClient(app)


def test_root_get_is_status_code_401_unauthorized():
    response = client.get('/')
    assert response.status_code == status.HTTP_401_UNAUTHORIZED