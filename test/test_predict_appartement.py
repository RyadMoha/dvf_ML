from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_predict_appartement():
    payload = {
        "ville": "LILLE",
        "type_local": "APPARTEMENT",
        "features": {
            "surface_reelle_bati": 80,
            "surface_terrain": 0,
            "nombre_lots": 3
        }
    }
    r = client.post("/predict", json=payload)
    assert r.status_code == 200
    data = r.json()
    assert "prix_m2_estime" in data
    assert data["prix_m2_estime"] > 0
