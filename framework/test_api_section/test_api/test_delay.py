"""
API tests for DELAYED RESPONSE.
"""
import allure
import pytest
from framework.data.test_data_main_page import ApiTestData
from framework.test_api_section.api_expected_result.base_url_and_path import GetUrl
from framework.test_api_section.api_expected_result.expected_result import ExpectedRequestsResult as er
from framework.test_api_section.pages_api.assertions import Assertion
from framework.test_api_section.pages_api.delay import DelayResponse


@allure.epic('Testing DELAYED RESPONSE')
class TestDelayResponse:
    url = GetUrl()
    random_list = ApiTestData()

    @pytest.mark.parametrize("elem", random_list.get_random_list())
    @allure.title("Test delay get status code 200")
    def test_get_delay_get_status_code_200(self, elem):
        """
        This test checks that the response has status code is 200
        """
        get_method = DelayResponse()
        response = get_method.get_delay_response(elem)
        Assertion.assert_status_code(response, er.STATUS_CODE_OK)

    @pytest.mark.parametrize("elem", random_list.get_random_list())
    @allure.title("checks that the response has json format")
    def test_get_delay_response_should_be_json(self, elem):
        """
        This test checks that the response has json format
        """
        get_method = DelayResponse()
        response = get_method.get_delay_response(elem)
        Assertion.assert_response_have_be_json(response)

    @pytest.mark.parametrize("elem", random_list.get_random_list())
    @allure.title("Test delay checking how long the page takes to load")
    def test_get_delay_check_page_loading(self, elem):
        """
        This test checking how long the page takes to load
        Max download time made 30 seconds
        """
        get_method = DelayResponse()
        get_method.get_delay_check_page_loading(elem)
