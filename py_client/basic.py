import requests

endpoint = "https://httpbin.org/status/200/"

endpoint = "http://127.0.0.1:8000/api/"

get_response = requests.get(endpoint, params={"abc":123}, json={"query":"Hello world"})
# print(get_response.text)
# print(get_response.status_code)
# print(get_response.json()['message'])
print(get_response.json())


#
# REST APIs -> Web Api
#
# HTTP Request -> HTML
# REST API HTTP Request -> JSON (xml)
# printing something in a json file
#
# print(get_response.json())
