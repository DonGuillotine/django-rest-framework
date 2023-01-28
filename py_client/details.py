import requests

endpoint = 'http://localhost:8000/api/products/1'

returned_data = requests.get(endpoint)

returned_data.raise_for_status()

print(returned_data.json())