""" Pytest configuration file """
import pytest
import allure
from faker import Faker
from api_data import data_lists


def pytest_addoption(parser):
    """ Add command line options """
    parser.addoption("--api_key", action="store", default="oops")
    parser.addoption("--api_token", action="store", default="oops")


@pytest.fixture()
def custom_api_key(pytestconfig):
    """ Return the API key """
    return pytestconfig.getoption("api_key")


@pytest.fixture()
def custom_api_token(pytestconfig):
    """ Return the API token """
    return pytestconfig.getoption("api_token")


@allure.step('step in conftest.py')
def conftest_step():
    """ A step in conftest.py """


@pytest.fixture()
def new_list(api_key, api_token):
    """ Return a new list """
    conftest_step()
    fake = Faker()
    data_for_list = {
        'name': f'{fake.first_name()}',
        'idBoard': '61e43d6f3fad02330a0a580f'
    }
    create_new_list = data_lists.create_list(data_for_list, api_key, api_token)
    return create_new_list.json()
