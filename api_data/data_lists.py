""" This module contains the lists data. """
import requests
from config.urls import LISTS_URL


def make_url(id_list, api_key, api_token):
    """ This function makes the url for the lists data. """
    return LISTS_URL+id_list+f'?key={api_key}&token={api_token}'


def get_list(id_list, api_key, api_token):
    """Get a list from the API"""
    response = requests.get(url=make_url(id_list, api_key, api_token), timeout=10)
    return response


def update_list(id_list, data, api_key, api_token):
    """Update a list from the API"""
    request = requests.put(url=make_url(id_list, api_key, api_token), data=data, timeout=10)
    return request


def create_list(data, id_list, api_key, api_token):
    """Create a list from the API"""
    request = requests.post(url=make_url(id_list, api_key, api_token), data=data, timeout=10)
    return request


def archive_a_list(id_list, value, api_key, api_token):
    """Archive a list from the API"""
    request = requests.put(url=make_url(id_list, api_key, api_token), params=value, timeout=10)
    return request
