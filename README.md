Water Well Detection AI 
Overview :

This project is an AI-powered solution designed to help identify the most suitable locations for drilling water wells using satellite data.

The application allows users to select a location on a map and receive a probability of groundwater presence, helping reduce the risks, costs, and uncertainty associated with drilling.

AI Model

The model is trained to classify locations based on environmental features.

🔹 Input Features
NDVI → Vegetation index 
NDWI → Water/moisture index 
Elevation → Terrain altitude 
Slope → Terrain inclination 
🔹 Output
Probability of groundwater presence (0 → 1)

Data Sources
Real well locations from OpenStreetMap (Overpass API)
Satellite data via Google Earth Engine
Environmental indices derived from Sentinel-2 and SRTM


How It Works
Collect real well data (OpenStreetMap)
Generate dataset with positive & negative samples
Extract satellite features using Google Earth Engine
Train machine learning model
Serve model via Flask API
Mobile app sends coordinates → receives prediction


Run the Project
1. Prepare Dataset
python src1/prepare_dataset_reel.py
2. Extract Features
python src1/extract_features.py
3. Train Model
python src1/train_model.py
4. Run API
python src1/app.py
5. Test API
python src1/test_api.py
6. Run Mobile App
npx expo start



Mobile App
Interactive map (React Native)
Click on any location
Send coordinates to backend
Display water probability