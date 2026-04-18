import pandas as pd
import joblib

# Charger modèle
model = joblib.load("models/well_detector.pkl")
print("✅ Modèle chargé")

# Exemple point (test)
data = pd.DataFrame([{
    'NDVI': 0.3,
    'NDWI': 0.1,
    'elevation': 400,
    'slope': 3
}])

# Prédiction
prob = model.predict_proba(data)[0][1]

print(f"🌊 Probabilité d'eau : {prob:.2f}")