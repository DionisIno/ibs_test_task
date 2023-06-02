"""
API tests for GET single resource.
"""
import random
import allure
import pytest
from framework.test_api_section.api_expected_result.base_url_and_path import GetUrl
from framework.test_api_section.api_expected_result.expected_result import ExpectedRequestsResult as er
from framework.test_api_section.pages_api.assertions import Assertion
from framework.test_api_section.pages_api.get_single_resource import GetSingleResource


@allure.epic('Testing GET single resource successful')
class TestGetSingleResource:
    url = GetUrl()
    random_number = random.randint(2, 13)

    @pytest.mark.parametrize("elem", range(1, random_number))
    @allure.title("Test get single resource get status code 200")
    def test_get_single_resource_get_status_code_200(self, elem):
        """
        This test checks that the response has status code is 200
        """
        get_method = GetSingleResource()
        response = get_method.get_single_resource_response(elem)
        Assertion.assert_status_code(response, er.STATUS_CODE_OK)

    @pytest.mark.parametrize("elem", range(1, random_number))
    @allure.title("Test test should check if the response is in json format")
    def test_get_single_resource_should_have_be_json(self, elem):
        """
        This test checks that the response has json format
        """
        get_method = GetSingleResource()
        response = get_method.get_single_resource_response(elem)
        Assertion.assert_response_have_be_json(response)

    @pytest.mark.parametrize("elem", range(1, random_number))
    @allure.title("Test test should check if the response has data key")
    def test_get_single_resource_check_response_has_data_key(self, elem):
        """
        This test checks that the response has data key
        """
        get_method = GetSingleResource()
        response = get_method.get_single_resource_response(elem)
        Assertion.assert_response_should_have_data_key(response)

    @pytest.mark.parametrize("elem", range(1, random_number))
    @allure.title("Test test should check if the response has data key")
    def test_get_single_resource_check_response_has_support_key(self, elem):
        """
        This test checks that the response has data key
        """
        get_method = GetSingleResource()
        response = get_method.get_single_resource_response(elem)
        Assertion.assert_response_should_have_support_key(response)


@allure.epic('Testing GET single resource unsuccessful')
class TestGetSingleResourceNotFound:
    url = GetUrl()
    random_number = list(range(20, 100))

    @pytest.mark.parametrize("elem", [random.choice(random_number)])
    @allure.title("Test get single resource get status code 404")
    def test_get_single_resource_not_found_get_status_code_404(self, elem):
        """
        This test checks that the response has status code is 404
        """
        get_method = GetSingleResource()
        response = get_method.get_single_resource_response(elem)
        print(response.json())
        Assertion.assert_status_code(response, er.NOT_FOUND)

    @pytest.mark.parametrize("elem", [random.choice(random_number)])
    @allure.title("Test test should check if the response is in json format")
    def test_get_single_resource_not_found_should_have_be_json(self, elem):
        """
        This test checks that the response has json format
        """
        get_method = GetSingleResource()
        response = get_method.get_single_resource_response(elem)
        Assertion.assert_response_have_be_json(response)

    @pytest.mark.parametrize("elem", [random.choice(random_number)])
    @allure.title("Test should check that response is empty")
    def test_get_single_resource_not_found_should_be_empty(self, elem):
        """
        This test checks that the response has json format
        """
        get_method = GetSingleResource()
        response = get_method.get_single_resource_response(elem)
        get_method.assert_get_single_user_not_found_has_empty_json(response)
