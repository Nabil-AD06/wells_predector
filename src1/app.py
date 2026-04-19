from flask_cors import CORS
from flask import Flask, request, jsonify
import joblib
import ee

# Init
app = Flask(__name__)
CORS(app)
ee.Initialize(project='water-detection-ai')

# Charger modèle
model = joblib.load("models/well_detector.pkl")

# Préparer images
s2 = ee.ImageCollection('COPERNICUS/S2_SR_HARMONIZED') \
    .filterDate('2022-01-01', '2023-12-31') \
    .median()

ndvi = s2.normalizedDifference(['B8', 'B4']).rename('NDVI')
ndwi = s2.normalizedDifference(['B3', 'B8']).rename('NDWI')

srtm = ee.Image('USGS/SRTMGL1_003')
elevation = srtm.rename('elevation')
slope = ee.Terrain.slope(srtm).rename('slope')

composite = ndvi.addBands(ndwi).addBands(elevation).addBands(slope)

# 🚀 Route API
@app.route('/')
def home():
    return "API Water Detection is running "
@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = request.json
        lat = data['lat']
        lon = data['lon']

        point = ee.Geometry.Point([lon, lat])

        values = composite.reduceRegion(
            reducer=ee.Reducer.mean(),
            geometry=point.buffer(100),
            scale=30
        ).getInfo()

        # Sécurité si données manquantes
        if values is None:
            return jsonify({"probability": 0.0})

        features = [[
            values.get('NDVI', 0),
            values.get('NDWI', 0),
            values.get('elevation', 0),
            values.get('slope', 0)
        ]]

        prob = model.predict_proba(features)[0][1]

        return jsonify({"probability": float(prob)})

    except Exception as e:
        print("ERROR:", e)
        return jsonify({"error": str(e)}), 500

# Run server
if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)