from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_predict_maison():
    payload = {
        "ville": "LILLE",
        "type_local": "MAISON",
        "features": {
            "surface_reelle_bati": 120,
            "surface_terrain": 200,
            "nombre_lots": 2
        }
    }
    r = client.post("/predict", json=payload)
    assert r.status_code == 200
    data = r.json()
    assert "prix_m2_estime" in data
    assert data["prix_m2_estime"] > 0
