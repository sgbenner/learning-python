import requests
from datetime import datetime
import os

USERNAME = os.environ.get("USERNAME")
TOKEN = os.environ.get("TOKEN")

pixela_endpoint = "https://pixe.la/v1/users"

user_params = {
    "username": USERNAME,
    "token": TOKEN,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

graphID = "graph1"
graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_config = {
    "id": graphID,
    "name": "Pages Read Graph",
    "unit": "Pages",
    "type": "int",
    "color": "ichou"
}

headers = {
    "X-USER-TOKEN": TOKEN
}

# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)


# post data to endpoint
post_data_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{graphID}"

today_fmt = datetime.now().strftime("%Y%m%d")

post_data_config = {
    "date": today_fmt,
    "quantity": "300"
}

headers = {
    "X-USER-TOKEN": TOKEN
}

response = requests.post(url=post_data_endpoint, json=post_data_config, headers=headers)
print(response.text)
