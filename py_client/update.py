import requests

endpoint = "http://localhost:8000/api/products/1/update/"

data = {
    "title":"Hello world",
    "price": 0.00
}

get_response = requests.put(endpoint, json=data) # HTTP request
print(get_response.json())
