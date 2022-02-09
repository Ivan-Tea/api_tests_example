import requests
import config.auth
from config.urls import LISTS_URL

auth = f'?key={config.auth.api_key}&token={config.auth.api_token}'


def get_list(id_list):
    response = requests.get(url=LISTS_URL+id_list+auth)
    return response


def update_list(id_list, data):
    request = requests.put(url=LISTS_URL+id_list+auth, data=data)
    return request


def create_list(data):
    request = requests.post(url=LISTS_URL+auth, data=data)
    return request


def archive_a_list(id_list, value):
    request = requests.put(url=LISTS_URL+id_list+auth, params=value)
    return request
