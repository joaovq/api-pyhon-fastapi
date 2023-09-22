from fastapi.testclient import TestClient
from fastapi import status 
from main import app 

client = TestClient(app)
def test_person_return_status_200_OK():
    response = client.get("/person/")
    assert response.status_code == status.HTTP_200_OK