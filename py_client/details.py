import requests

endpoint = 'http://localhost:8000/api/products/1'

data_response = requests.get(endpoint)

print(data_response.json())