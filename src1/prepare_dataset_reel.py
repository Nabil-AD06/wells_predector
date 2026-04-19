import json
import csv
import random

# Charger JSON (puits réels)
with open("data/interpreter.json", encoding="utf-8") as f:
    data = json.load(f)

rows = []

# 1️ Ajouter puits (label = 1)
for el in data["elements"]:
    rows.append([el["lat"], el["lon"], 1])

# 2️ Ajouter points négatifs
for _ in range(len(rows)):
    lat = random.uniform(28, 36)
    lon = random.uniform(-10, -1)
    rows.append([lat, lon, 0])

# 3️ Sauvegarder dataset
with open("data/wells.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["lat", "lon", "label"])
    writer.writerows(rows)

print("✅ Dataset prêt !")