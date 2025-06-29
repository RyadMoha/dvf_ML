from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from .schemas import PredictionRequest, PredictionResponse
from .predict import predict_price

app = FastAPI(title="ImmoPrice API", version="0.1.0")

# CORS (origins="*" seulement en développement)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["POST", "GET"],
    allow_headers=["*"],
)

@app.get("/health")
def health():
    return {"status": "ok"}

@app.post("/predict", response_model=PredictionResponse)
def predict(req: PredictionRequest):
    """
    Retourne le prix au m² estimé pour un bien.
    """
    prix = predict_price(req)
    return {"prix_m2_estime": prix}
