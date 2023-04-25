import requests

headers = {'Authorization': 'Bearer 6464677477832472837838'}
endpoint = "http://localhost:8000/api/products/"

data = {
    "pk": "16",
    "title": "Product is available now",
    "content": "it is available now",
    "price": 32.99
}
get_response = requests.post(endpoint, json=data, headers=headers) # HTTP request
print(get_response.json())
