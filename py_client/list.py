import requests
from getpass import getpass


auth_endpoint = "http://127.0.0.1:8000/api/auth/"

password = getpass()
auth_response = requests.post(auth_endpoint, json={"username":"admin", "password":password })
print(auth_response.json())

# data = {
# "title" : "this filed is done "
# }
#
# get_response = requests.get(endpoint)

# print(auth_response.json())
