from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_signup_and_login():
    r = client.post("/api/v1/signup", json={"username": "alice", "password": "secret"})
    assert r.status_code == 200

    r = client.post("/api/v1/login", data={"username": "alice", "password": "secret"})
    assert r.status_code == 200
    token = r.json()["access_token"]

    r = client.get("/api/v1/protected", headers={"Authorization": f"Bearer {token}"})
    assert r.status_code == 200

