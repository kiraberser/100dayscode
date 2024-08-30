import requests
from datetime import datetime

USERNAME = "kirabersek"
TOKEN = "jio309ad8313l3sd"
pixela_endpoint = "https://pixe.la/v1/users"

user_params = {
    "token": "jio309ad8313l3sd",
    "username": "kirabersek",
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

#response = requests.post(url=pixela_endpoint, json=user_params)
#print(response.text)

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_config = {
    "id": "graph31",
    "name": "Running Graph",
    "unit": "Km",
    "type": "float",
    "color": "ajisai"
}

headers = {
    "X-USER-TOKEN": TOKEN
}

#response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
#print(response)

pixel_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/graph31"
today = datetime.now()


pixel_config = {
    "date": today.strftime("%Y%m%d"),
    "quantity": input("How many kilometers did you run today?: "),
}

response = requests.post(url=pixel_endpoint, json=pixel_config, headers=headers)
print(response.text)

#puth
pixel_endpoint_update = f"{pixela_endpoint}/{USERNAME}/graphs/graph31/{today.strftime("%Y%m%d")}"

#response = requests.put(url=pixel_endpoint_update, json=pixel_config, headers=headers)
#print(response.text)

#delete
#pixel_endpoint_delete = f"{pixela_endpoint}/{USERNAME}/graphs/graph31/{today.strftime("%Y%m%d")}"
#response = requests.delete(url=pixel_endpoint_update, headers=headers)
#print(response.text)
