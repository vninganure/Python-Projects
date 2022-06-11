import requests
from datetime import datetime

TOKEN = "sjkadfh3r32jhw4444hdjkfjk76"
USERNAME = "vijay12345"
pexela_endpoint = "https://pixe.la/v1/users"

user_parms = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor":"yes"
}

# response = requests.post(url=pexela_endpoint, json=user_parms)
# print(response.text)

graph_endpoint = f"{pexela_endpoint}/{USERNAME}/graphs"

graph_config = {
    "id": "graph1",
    "name": "Cyclic graph",
    "unit": "km",
    "type": "float",
    "color": "ajisai"
}

headers ={
    "X-USER-TOKEN": TOKEN
}

# responce = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(responce.text)

graph_post_endpoint = f"{graph_endpoint}/{graph_config['id']}"

today = datetime.now()
today = today.strftime("%Y%m%d")

travell = input("How many km you have travelled today?")


graph_post_config = {
    "date": today,
    "quantity": travell
}
# response = requests.post(url=graph_post_endpoint, json=graph_post_config, headers=headers)
# print(response.text)

update_endpoint = f"{graph_post_endpoint}/{today}"

update_pixel_data = {
    "quantity": travell
}

responce = requests.put(url=update_endpoint, json=update_pixel_data, headers=headers)
print(responce.text)