import requests
from config.urls import LISTS_URL

# auth = f'?key={api_key}&token={api_token}'


def get_list(id_list, api_key, api_token):
    response = requests.get(url=LISTS_URL+id_list+f'?key={api_key}&token={api_token}')
    return response


def update_list(id_list, data, api_key, api_token):
    request = requests.put(url=LISTS_URL+id_list+f'?key={api_key}&token={api_token}', data=data)
    return request


def create_list(data, api_key, api_token):
    request = requests.post(url=LISTS_URL+f'?key={api_key}&token={api_token}', data=data)
    return request


def archive_a_list(id_list, value, api_key, api_token):
    request = requests.put(url=LISTS_URL+id_list+f'?key={api_key}&token={api_token}', params=value)
    return request
