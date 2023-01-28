import requests


endpoint = "http://localhost:8000/api/products"

returned_data = requests.get(endpoint)

print(returned_data.json())