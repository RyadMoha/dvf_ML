import pandas as pd

FEATURE_ORDER = ["Surface reelle bati", "Surface terrain", "Nombre de lots"]

def to_dataframe(features: dict) -> pd.DataFrame:
    df = pd.DataFrame([features])
    # Harmoniser les noms pour qu’ils collent au pipeline
    df.columns = ["Surface reelle bati", "Surface terrain", "Nombre de lots"]
    return df[FEATURE_ORDER]
