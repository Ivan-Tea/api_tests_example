import pytest
import allure
from faker import Faker
from api_data import data_lists


@allure.step('step in conftest.py')
def conftest_step():
    pass


@pytest.fixture()
def new_list():
    conftest_step()
    fake = Faker()
    data_for_list = {
        'name': f'{fake.first_name()}',
        'idBoard': '61e43d6f3fad02330a0a580f'
    }
    new_list = data_lists.create_list(data_for_list)
    return new_list.json()
