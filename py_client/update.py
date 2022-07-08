import requests



endpoint = "http://127.0.0.1:8000/api/product/1/update/"

data = {
"title" : "updated this filed is done "
}

get_response = requests.put(endpoint, json=data)

print(get_response.json())
