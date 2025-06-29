# 🏡 ImmoPrice API

Une API simple de prédiction du prix au m² d'un bien immobilier (maison ou appartement) à Lille.  
Modèle entraîné sur les données DVF.

---

## 🚀 Lancer l'API en local

1. **Créer l'environnement virtuel**

```bash
python3 -m venv .venv
source .venv/bin/activate
```

2. **Installer les dépendances**

```bash
pip install -r requirements.txt
```

3. **Lancer le serveur FastAPI**

```bash
uvicorn app.main:app --reload
```

📂 Accès à la doc interactive sur : [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)

---

## 🔎 Prédiction

### Endpoint

```http
POST /predict
```

### Exemple de requête

```json
{
  "ville": "LILLE",
  "type_local": "APPARTEMENT",
  "features": {
    "surface_reelle_bati": 80,
    "surface_terrain": 0,
    "nombre_lots": 3
  }
}
```

### Exemple de réponse

```json
{
  "prix_m2_estime": 3750.45
}
```

---

## 🧪 Lancer les tests

```bash
pytest -v -s test/
```

---

## 📂 Structure du projet

```
.
├── app/
│   ├── main.py
│   ├── schemas.py
│   ├── predict.py
│   └── model_loader.py
├── models/
│   ├── model_lille_appartement.pkl
│   └── model_lille_maison.pkl
├── test/
│   ├── test_predict_appart.py
│   └── test_predict_maison.py
├── data/
├── requirements.txt
└── README.md
```

---

## 🧠 Modèles

- `RandomForestRegressor` pour les **appartements**
- `LinearRegression` pour les **maisons**

Modèles entraînés sur les données DVF nettoyées pour la ville de Lille.

---

## 📌 À venir

- Généralisation à d'autres villes (ex. : Bordeaux)
- Amélioration des performances sur les maisons
- Enrichissement des features (ex. : géolocalisation, années de construction, etc.)
