import requests

url = "http://127.0.0.1:5000/predict"

data = {
    "lat": 31.5,
    "lon": -7.8
}

response = requests.post(url, json=data)

print(response.json())