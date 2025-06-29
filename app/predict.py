# app/predict.py
# ───────────────────────────────────────────────
from pathlib import Path
import joblib
import pandas as pd

from .utils import FEATURE_ORDER   # colonne-strict order ["Surface reelle bati", ...]
from .model_loader import load_model
from .schemas import PredictionRequest


def _to_dataframe(req: PredictionRequest) -> pd.DataFrame:
    """Convertit l’objet Pydantic en DataFrame scikit-learn compatible."""
    record = {
        "Surface reelle bati": req.features.surface_reelle_bati,
        "Surface terrain": req.features.surface_terrain,
        "Nombre de lots": req.features.nombre_lots,
    }
    # Assure l’ordre des colonnes attendu par le pipeline sauvegardé
    return pd.DataFrame([record])[FEATURE_ORDER]


def predict_price(req: PredictionRequest) -> float:
    """
    Charge le modèle correspondant (ville + type_local),
    applique le pipeline (imputer/scaler/forêt, etc.) et renvoie
    le prix au m² estimé (float arrondi à 2 décimales).
    """
    model = load_model(req.ville, req.type_local)   # caching interne
    X = _to_dataframe(req)
    pred = model.predict(X)[0]                      # numpy.float64
    return round(float(pred), 2)
