"""
API tests for GET list resource.
"""
import random

import allure
import pytest
from framework.data.test_data_main_page import ApiTestData
from framework.test_api_section.api_expected_result.base_url_and_path import GetUrl
from framework.test_api_section.api_expected_result.expected_result import ExpectedRequestsResult as er
from framework.test_api_section.pages_api.assertions import Assertion
from framework.test_api_section.pages_api.get_list_resource import GetListResource


@allure.epic('Testing POST login successful and unsuccessful')
class TestGetListResource:
    url = GetUrl()
    random_number = random.randint(2, 5)

    @pytest.mark.parametrize("elem", range(1, random_number))
    @allure.title("Test get list resource get status code 200")
    def test_get_list_resource_get_status_code_200(self, elem):
        """
        This test checks that the response has status code is 200
        """
        get_method = GetListResource()
        response = get_method.get_list_resource_response()
        Assertion.assert_status_code(response, er.STATUS_CODE_OK)

    @pytest.mark.parametrize("elem", range(1, random_number))
    @allure.title("Test get list resource response should be a json")
    def test_get_list_resource_response_should_be_json(self, elem):
        """
        This test checks that the response should be a json
        """
        get_method = GetListResource()
        response = get_method.get_list_resource_response()
        Assertion.assert_response_have_be_json(response)

    @pytest.mark.parametrize("elem", range(1, random_number))
    @allure.title("The test checks that in the response per_page, total, total_pages should have the correct values")
    def test_get_list_resource_in_response_per_page_total_total_pages_should_have_correct_values(self, elem):
        """
        This test checks that in the response per_page, total, total_pages should have the correct values
        """
        get_method = GetListResource()
        response = get_method.get_list_resource_response()
        Assertion.assert_check_in_response_per_page_total_total_pages_have_correct_values(response)

    @pytest.mark.parametrize("elem", range(1, random_number))
    @allure.title("The test is to check if the response has a valid page number")
    def test_get_list_resource_check_count_items_in_response_data(self, elem):
        """
        This test checks that the response has a valid page number
        """
        get_method = GetListResource()
        response = get_method.get_list_resource_response()
        Assertion.assert_check_count_of_response_data(response)

    @pytest.mark.parametrize("elem", range(1, random_number))
    @allure.title("The test is to check if the response should have data key")
    def test_get_list_resource_response_should_have_data_key(self, elem):
        """
        This test checks that the response should have data key
        """
        get_method = GetListResource()
        response = get_method.get_list_resource_response()
        Assertion.assert_response_should_have_data_key(response)

    @pytest.mark.parametrize("elem", range(1, random_number))
    @allure.title("The test is to check if the response should have support key")
    def test_get_list_resource_response_should_have_support_key(self, elem):
        """
        This test checks that the response should have support key
        """
        get_method = GetListResource()
        response = get_method.get_list_resource_response()
        Assertion.assert_response_should_have_support_key(response)

    @pytest.mark.parametrize("elem", range(1, random_number))
    @allure.title("The test is to check if the response should have support email")
    def test_get_list_resource_response_should_have_support_email(self, elem):
        """
        This test checks that the response should have support email
        """
        get_method = GetListResource()
        response = get_method.get_list_resource_response()
        Assertion.assert_support_have_correct_url(response)

    @pytest.mark.parametrize("elem", range(1, random_number))
    @allure.title("The test is to check if the response should have support text")
    def test_get_list_resource_response_should_have_support_text(self, elem):
        """
        This test checks that the response should have support text
        """
        get_method = GetListResource()
        response = get_method.get_list_resource_response()
        Assertion.assert_support_have_correct_text(response)
