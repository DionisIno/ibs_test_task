"""
API tests for POST Create method.
"""
import allure
import pytest

from framework.test_api_section.api_expected_result.base_url_and_path import GetUrl as url
from framework.test_api_section.api_expected_result.expected_result import ExpectedRequestsResult as er, CreateUser
from framework.test_api_section.pages_api.assertions import Assertion
from framework.test_api_section.pages_api.base_page import BasePage
from framework.test_api_section.pages_api.create_post import CreatePost
from framework.test_api_section.pages_api.my_requests import MyRequests


@allure.epic('Testing POST Create method')
class TestPostCreate(BasePage):
    @pytest.mark.parametrize("elem", range(1, 5))
    @allure.title("Test created user successfully")
    def test_create_post_user_successfully(self, elem):
        data = self.prepare_creating_date()
        response = MyRequests.post(url.GET_SINGLE_USER, data=data)
        Assertion.assert_status_code(response, er.CREATED)
        Assertion.assert_response_have_be_json(response)

    @pytest.mark.parametrize("elem", range(1, 5))
    @allure.title("Test check of the created user for the presence of all keys")
    def test_create_post_user_has_all_keys(self, elem):
        data = self.prepare_creating_date()
        response = MyRequests.post(url.GET_SINGLE_USER, data=data)
        Assertion.assert_json_has_keys(response, CreateUser.create)

    @pytest.mark.parametrize("elem", range(1, 5))
    @allure.title("Test validation of the generated data")
    def test_create_post_user_created_data_is_correct(self, elem):
        data = self.prepare_creating_date()
        response = MyRequests.post(url.GET_SINGLE_USER, data=data)
        CreatePost.assert_check_job_and_name_in_response(response, data)




