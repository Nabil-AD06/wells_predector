import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, roc_auc_score
import joblib

# Charger dataset
df = pd.read_csv("data/dataset.csv")

print(f"Dataset : {len(df)} lignes")

# Features
features = ['NDVI', 'NDWI', 'elevation', 'slope']

X = df[features]
y = df['label']

# Split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

# Modèle
model = RandomForestClassifier(
    n_estimators=100,
    max_depth=10,
    class_weight='balanced',
    random_state=42
)

# Train
model.fit(X_train, y_train)

print("✅ Modèle entraîné !")

# Évaluation
y_pred = model.predict(X_test)
y_prob = model.predict_proba(X_test)[:, 1]

print("\n📊 Résultats :")
print(classification_report(y_test, y_pred))
print("AUC :", roc_auc_score(y_test, y_prob))

# Sauvegarde
joblib.dump(model, "models/well_detector.pkl")
print("\n💾 Modèle sauvegardé !")