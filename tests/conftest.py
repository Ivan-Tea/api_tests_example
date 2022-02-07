import pytest
from faker import Faker
from test_data import data_lists


@pytest.fixture()
def new_list():
    fake = Faker()
    data_for_list = {
        'name': f'{fake.first_name()}',
        'idBoard': '61e43d6f3fad02330a0a580f'
    }
    new_list = data_lists.create_list(data_for_list)
    return new_list.json()
