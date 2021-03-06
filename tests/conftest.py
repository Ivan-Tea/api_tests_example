import pytest
import allure
from faker import Faker
from api_data import data_lists


def pytest_addoption(parser):
    parser.addoption("--api_key", action="store", default="oops")
    parser.addoption("--api_token", action="store", default="oops")


@pytest.fixture()
def api_key(pytestconfig):
    return pytestconfig.getoption("api_key")


@pytest.fixture()
def api_token(pytestconfig):
    return pytestconfig.getoption("api_token")


@allure.step('step in conftest.py')
def conftest_step():
    pass


@pytest.fixture()
def new_list(api_key, api_token):
    conftest_step()
    fake = Faker()
    data_for_list = {
        'name': f'{fake.first_name()}',
        'idBoard': '61e43d6f3fad02330a0a580f'
    }
    new_list = data_lists.create_list(data_for_list, api_key, api_token)
    return new_list.json()
