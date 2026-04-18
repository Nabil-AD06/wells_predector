import pandas as pd
import numpy as np

np.random.seed(42)

# 🇲🇦 Zones connues (où il y a de l’eau)
zones_eau = [
    (30.9, -7.5, 40),   # Souss-Massa
    (31.5, -8.0, 30),   # Haouz
    (34.0, -5.0, 25),   # Gharb
    (33.5, -7.6, 35),   # Chaouia
    (30.0, -5.5, 20),   # Draa
]

# 🟢 Points positifs (puits)
wells = []
for lat_c, lon_c, n in zones_eau:
    for _ in range(n):
        wells.append({
            'latitude': lat_c + np.random.normal(0, 0.3),
            'longitude': lon_c + np.random.normal(0, 0.3),
            'label': 1
        })

# 🔴 Points négatifs (zones aléatoires)
for _ in range(300):
    wells.append({
        'latitude': np.random.uniform(27.5, 35.9),
        'longitude': np.random.uniform(-13.0, -1.0),
        'label': 0
    })

# 📊 Créer dataframe
df = pd.DataFrame(wells)

# 💾 Sauvegarde
df.to_csv("data/wells.csv", index=False)

print("✅ Dataset créé !")
print(df.head())
print("\nDistribution :")
print(df['label'].value_counts())