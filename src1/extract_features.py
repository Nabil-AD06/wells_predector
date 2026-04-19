import ee
import pandas as pd

ee.Initialize(project='ur-project-id')

print(" GEE connecté !")

# Charger dataset
df = pd.read_csv("data/wells.csv")
print(f"Points chargés : {len(df)}")

# Image Sentinel-2
s2 = ee.ImageCollection('COPERNICUS/S2_SR_HARMONIZED') \
    .filterDate('2022-01-01', '2023-12-31') \
    .filter(ee.Filter.lt('CLOUDY_PIXEL_PERCENTAGE', 20)) \
    .median()

# Indices
ndvi = s2.normalizedDifference(['B8', 'B4']).rename('NDVI')
ndwi = s2.normalizedDifference(['B3', 'B8']).rename('NDWI')

# Terrain
srtm = ee.Image('USGS/SRTMGL1_003')
elevation = srtm.rename('elevation')
slope = ee.Terrain.slope(srtm).rename('slope')

# Composite
composite = ndvi.addBands(ndwi) \
               .addBands(elevation) \
               .addBands(slope)

#  Extraction pour tous les points
results = []

for i, row in df.iterrows():
    if i % 50 == 0:
        print(f"Progression : {i}/{len(df)}")

    try:
        point = ee.Geometry.Point(row['lon'], row['lat'])

        values = composite.reduceRegion(
            reducer=ee.Reducer.mean(),
            geometry=point.buffer(100),
            scale=30
        ).getInfo()

        if values:
            values['lat'] = row['lat']
            values['lon'] = row['lon']
            values['label'] = row['label']

            results.append(values)

    except Exception as e:
        print("Erreur:", e)

#  Convertir en DataFrame
dataset = pd.DataFrame(results)

#  Sauvegarder
dataset.to_csv("data/dataset.csv", index=False)

print("\n✅ Dataset créé !")
print(dataset.head())