import requests

endpoint = "http://localhost:8000/api/products/132112321123/"

get_response = requests.get(endpoint) # HTTP request
print(get_response.json())
