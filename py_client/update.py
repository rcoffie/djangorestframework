import requests

endpoint = "http://127.0.0.1:8000/api/product/1/update/"
data = {"title":"updating title"}
get_response = requests.put(endpoint, data=data)

print(get_response.json())
