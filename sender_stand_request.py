import requests
from configuration import API_URl, USERS_ENDPOINT, KITS_ENDPOINT

def post_new_client_kit(kit_body, auth_token):
    url = API_URl + KITS_ENDPOINT
    headers = {
        "Authorization": f"Bearer {auth_token}",
        "Content-Type": "application/json"
    }
    response = requests.post(url, json=kit_body, headers=headers)
    return response

def get_new_user_token():
    return ()




