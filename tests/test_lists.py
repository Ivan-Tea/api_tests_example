""" Tests for lists.py """
import allure
from api_data import data_lists, helper


@allure.severity(allure.severity_level.BLOCKER)
def test_get_list(new_list, custom_api_key, custom_api_token):
    """ Test get list """
    required_fields = ['name', 'id', 'idBoard']
    get_list = data_lists.get_list(new_list['id'], custom_api_key, custom_api_token)
    helper.check_status_code(get_list)
    helper.check_required_fields(get_list, required_fields)
    assert [get_list.json()['id'], get_list.json()['name'], get_list.json()['idBoard']]\
           == \
           [new_list['id'], new_list['name'], new_list['idBoard']]


@allure.severity(allure.severity_level.BLOCKER)
def test_update_list(new_list, custom_api_key, custom_api_token):
    """ Test update list """
    new_data_for_list = {'name': 'updated_list'}
    update_list = data_lists.update_list(
        new_list['id'], new_data_for_list,
        custom_api_key, custom_api_token
    )
    helper.check_status_code(update_list)
    assert update_list.json()['name'] == 'updated_list'


@allure.severity(allure.severity_level.BLOCKER)
def test_create_list(custom_api_key, custom_api_token):
    """ Test create list """
    required_fields = ['id', 'name']
    data_for_list = {
        'name': 'test_list',
        'idBoard': '61e43d6f3fad02330a0a580f'
    }
    create_list = data_lists.create_list(
        data_for_list,
        custom_api_key,
        custom_api_token
    )
    helper.check_status_code(create_list)
    helper.check_required_fields(create_list, required_fields)
    helper.check_required_fields(create_list, required_fields)
    assert create_list.json()['name'] == data_for_list['name']


@allure.severity(allure.severity_level.CRITICAL)
def test_archive_list(new_list, custom_api_key, custom_api_token):
    """ Test archive list """
    value = {'closed': 'true'}
    archived_list = data_lists.archive_a_list(
        new_list['id'],
        value,
        custom_api_key,
        custom_api_token
    )
    helper.check_status_code(archived_list)
    assert archived_list.json()['closed']


@allure.severity(allure.severity_level.CRITICAL)
def test_unarchive_list(new_list, custom_api_key, custom_api_token):
    """ Test unarchive list """
    archive_value = {'closed': 'true'}
    archived_list = data_lists.archive_a_list(
        new_list['id'], 
        archive_value,
        custom_api_key,
        custom_api_token
    )
    unarchive_value = {'closed': 'false'}
    unarchived_list = data_lists.archive_a_list(
        archived_list.json()['id'],
        unarchive_value,
        custom_api_key,
        custom_api_token
    )
    helper.check_status_code(unarchived_list)
    assert unarchived_list.json()['closed'] is False
