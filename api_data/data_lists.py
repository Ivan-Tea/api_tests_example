""" This module contains the lists data. """
import requests
from config.urls import LISTS_URL


def get_list(id_list, api_key, api_token):
    """Get a list from the API"""
    response = requests.get(url=LISTS_URL+id_list+f'?key={api_key}&token={api_token}', timeout=10)
    return response


def update_list(id_list, data, api_key, api_token):
    """Update a list from the API"""
    request = requests.put(url=LISTS_URL+id_list+f'?key={api_key}&token={api_token}', data=data, timeout=10)
    return request


def create_list(data, api_key, api_token):
    """Create a list from the API"""
    request = requests.post(url=LISTS_URL+f'?key={api_key}&token={api_token}', data=data, timeout=10)
    return request


def archive_a_list(id_list, value, api_key, api_token):
    """Archive a list from the API"""
    request = requests.put(url=LISTS_URL+id_list+f'?key={api_key}&token={api_token}', params=value, timeout=10)
    return request
