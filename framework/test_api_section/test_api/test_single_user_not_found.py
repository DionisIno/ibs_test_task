import random
import allure
import pytest

from framework.test_api_section.api_expected_result.base_url_and_path import GetUrl
from framework.test_api_section.api_expected_result.expected_result import ExpectedRequestsResult
from framework.test_api_section.pages_api.assertions import Assertion
from framework.test_api_section.pages_api.get_single_user_not_found import SingleUserNotFound
from framework.test_api_section.pages_api.my_requests import MyRequests


@allure.epic("Testing GET SINGLE USER NOT FOUND")
class TestGetSingleUserNotFound:
    url = GetUrl()
    random_number = list(range(20, 100))
    status_code = ExpectedRequestsResult()

    @pytest.mark.parametrize("elem", [random.choice(random_number)])
    @allure.title("Test should return status code 404")
    def test_get_single_user_not_found_should_return_status_code_404(self, elem):
        response = MyRequests.get(f"""{self.url.GET_SINGLE_USER}{elem}""")
        Assertion.assert_status_code(response, self.status_code.NOT_FOUND)

    @pytest.mark.parametrize("elem", [random.choice(random_number)])
    @allure.title("Test should check that response has json format")
    def test_get_single_user_not_found_should_be_json(self, elem):
        response = MyRequests.get(f"""{self.url.GET_SINGLE_USER}{elem}""")
        Assertion.assert_response_have_be_json(response)

    @pytest.mark.parametrize("elem", [random.choice(random_number)])
    @allure.title("Test should check that response is empty")
    def test_get_single_user_not_found_should_be_empty(self, elem):
        response = MyRequests.get(f"""{self.url.GET_SINGLE_USER}{elem}""")
        SingleUserNotFound.assert_get_single_user_not_found_has_empty_json(response)
