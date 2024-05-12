import requests
from configuration import API_URl, USERS_ENDPOINT, KITS_ENDPOINT
from data import user_data_min


def post_new_client_kit(kit_body, auth_token):
    url = API_URl + KITS_ENDPOINT
    headers = {
        "Authorization": f"Bearer {auth_token}",
        "Content-Type": "application/json"
    }
    response = requests.post(url, json=kit_body, headers=headers)
    return response

def get_new_user_token(user_data):
    url = API_URl + USERS_ENDPOINT
    headers = {
        "Content-Type": "application/json"
    }
    response = requests.post(url, json=user_data, headers=headers)
    return response


response = get_new_user_token(user_data_min)
if response.status_code == 201:
    auth_token = response.json().get("authToken")
    print("Успешное создание пользователя.")
    print(f"AuthToken: {auth_token}")
else:
    print("Ошибка при создании пользователя.")
    print(f"Статус код: {response.status_code}")



