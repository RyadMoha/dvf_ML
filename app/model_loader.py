from pathlib import Path
import joblib

_model_cache: dict[str, object] = {}

def load_model(ville: str, type_local: str):
    key = f"{ville}_{type_local}"
    if key not in _model_cache:
        path = Path("models") / f"model_{ville.lower()}_{type_local.lower()}.pkl"
        _model_cache[key] = joblib.load(path)
    return _model_cache[key]
