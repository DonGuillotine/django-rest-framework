import requests

endpoint = "http://localhost:8000/api/products"

data = {
    "title": "Welcome to Misery"
}

data_response = requests.post(endpoint, json=data)

print(data_response.json())