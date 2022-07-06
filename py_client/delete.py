import requests

product_id = input ("input the product id of the product you will want to delete \n")
try:
    product_id = int(product_id)
except:
    product_id = None
    print(f'{product_id} cannot be found ')

if product_id:
    endpoint = f"http://127.0.0.1:8000/api/product/{product_id}/delete/"
    get_response = requests.delete(endpoint)
    print(get_response.status_code, get_response.status_code==204)

# print(get_response.json())
