""" Helper functions for api_data """
import allure
from schema import Schema


def check_status_code(response):
    with allure.step('Check status code'):
        assert response.status_code == 200


def check_required_fields(response, fields):
    with allure.step('Check required fields'):
        response_json = response.json()
        required_fields = [field for field in fields if response_json.get(field) is None]
        assert required_fields == []


def check_json_scheme(response, scheme):
    with allure.step('Check json scheme'):
        schema_json = Schema(scheme)
        response_json = response.json()
        assert schema_json.is_valid(response_json)
