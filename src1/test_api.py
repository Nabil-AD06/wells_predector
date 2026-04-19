import requests

url = "URL-dpnner-par-app.py/predict"

data = {
    "lat": 31.5,
    "lon": -7.8
}

response = requests.post(url, json=data)

print(response.json())