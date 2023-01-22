import requests

# An endpoint i.e url
# endpoint = 'https://httpbin.org/anything';
endpoint = 'http://localhost:8000/api/'

# Getting data from the endpoint
response_data = requests.get(endpoint, params={"abc": 123}, json={"query": "Backend Developer"})

# response_data.text, status_code, json() etc
# print(response_data.text)
print(response_data.json())
# print(response_data.status_code)