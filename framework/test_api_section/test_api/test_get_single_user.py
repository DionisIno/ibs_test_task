import random

import allure
import pytest

from framework.test_api_section.api_expected_result.base_url_and_path import GetUrl
from framework.test_api_section.api_expected_result.expected_result import ExpectedRequestsResult
from framework.test_api_section.pages_api.assertions import Assertion
from framework.test_api_section.pages_api.get_single_user import SingleUser
from framework.test_api_section.pages_api.my_requests import MyRequests


@allure.epic("Testing GET SINGLE USER")
class TestGetSingleUser:
    url = GetUrl()
    random_number = random.randint(2, 13)
    status_code = ExpectedRequestsResult()

    @pytest.mark.parametrize("elem", range(1, random_number))
    @allure.title("Test should return status code")
    def test_get_single_user_should_return_status_code_200(self, elem):
        response = MyRequests.get(f"""{self.url.GET_SINGLE_USER}{elem}""")
        Assertion.assert_status_code(response, self.status_code.STATUS_CODE_OK)

    @pytest.mark.parametrize("elem", range(1, random_number))
    @allure.title("Test test should check if the response is in json format")
    def test_get_single_user_should_have_be_json(self, elem):
        response = MyRequests.get(f"""{self.url.GET_SINGLE_USER}{elem}""")
        Assertion.assert_response_have_be_json(response)

    @pytest.mark.parametrize("elem", range(1, random_number))
    @allure.title("The test checks that the single user response has data key")
    def test_get_single_user_check_data_key(self, elem):
        response = MyRequests.get(f"""{self.url.GET_SINGLE_USER}{elem}""")
        Assertion.assert_response_should_have_data_key(response)

    @pytest.mark.parametrize("elem", range(1, random_number))
    @allure.title("The test checks that the single user response has support key")
    def test_get_single_user_check_response_has_support_key(self, elem):
        response = MyRequests.get(f"""{self.url.GET_SINGLE_USER}{elem}""")
        Assertion.assert_response_should_have_support_key(response)

    @pytest.mark.parametrize("elem", range(1, random_number))
    @allure.title("The test checks that the single user response has correct id")
    def test_get_single_user_check_response_has_correct_id(self, elem):
        response = MyRequests.get(f"""{self.url.GET_SINGLE_USER}{elem}""")
        SingleUser.assert_check_correct_id(response, "id", elem)

    @pytest.mark.parametrize("elem", range(1, random_number))
    @allure.title("The test checks that the single user response has email")
    def test_get_single_user_check_response_has_email(self, elem):
        response = MyRequests.get(f"""{self.url.GET_SINGLE_USER}{elem}""")
        SingleUser.assert_response_has_key(response, "email")

    @pytest.mark.parametrize("elem", range(1, random_number))
    @allure.title("The test checks that the single user response has first name")
    def test_get_single_user_check_response_has_first_name(self, elem):
        response = MyRequests.get(f"""{self.url.GET_SINGLE_USER}{elem}""")
        SingleUser.assert_response_has_key(response, "first_name")

    @pytest.mark.parametrize("elem", range(1, random_number))
    @allure.title("The test checks that the single user response has last name")
    def test_get_single_user_check_response_has_last_name(self, elem):
        response = MyRequests.get(f"""{self.url.GET_SINGLE_USER}{elem}""")
        SingleUser.assert_response_has_key(response, "last_name")

    @pytest.mark.parametrize("elem", range(1, random_number))
    @allure.title("The test checks that the single user response has avatar")
    def test_get_single_user_check_response_has_avatar(self, elem):
        response = MyRequests.get(f"""{self.url.GET_SINGLE_USER}{elem}""")
        SingleUser.assert_response_has_key(response, "avatar")

    @pytest.mark.parametrize("elem", range(1, random_number))
    @allure.title("The test checks that the avatar image has a status code of 200")
    def test_get_single_user_check_avatar_image_link_has_status_code_200(self, elem):
        response = MyRequests.get(f"""{self.url.GET_SINGLE_USER}{elem}""")
        SingleUser.assert_single_user_avatar_image_link_has_status_code_200(response)

    @pytest.mark.parametrize("elem", range(1, random_number))
    @allure.title("The test checks that the support has correct url")
    def test_get_single_user_check_support_has_correct_email(self, elem):
        response = MyRequests.get(f"""{self.url.GET_SINGLE_USER}{elem}""")
        SingleUser.assert_single_user_support_have_correct_url(response)

    @pytest.mark.parametrize("elem", range(1, random_number))
    @allure.title("The test checks that the support has correct text")
    def test_get_single_user_check_support_has_correct_email(self, elem):
        response = MyRequests.get(f"""{self.url.GET_SINGLE_USER}{elem}""")
        SingleUser.assert_single_user_support_have_correct_text(response)
