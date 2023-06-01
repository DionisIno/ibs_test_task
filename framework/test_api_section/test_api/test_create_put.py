"""
API tests for PUT Create method.
"""
import random
import allure
import pytest
from framework.test_api_section.api_expected_result.base_url_and_path import GetUrl
from framework.test_api_section.api_expected_result.expected_result import ExpectedRequestsResult as er, CreateUser
from framework.test_api_section.pages_api.assertions import Assertion
from framework.test_api_section.pages_api.base_page import BasePage
from framework.test_api_section.pages_api.create_put import CreatePut
from framework.test_api_section.pages_api.my_requests import MyRequests


@allure.epic('Testing PUT Create method')
class TestPutCreate(BasePage):
    url = GetUrl()
    random_number = random.randint(2, 13)

    @pytest.mark.parametrize("elem", range(1, random_number))
    @allure.title("Test update user successfully PUT method")
    def test_create_put_user_update_user(self, elem):
        """
        This test checks that the data has changed,
        the status code is 200, passed in the response json
        """
        data = self.prepare_creating_date()
        response = MyRequests.put(f"""{self.url.GET_SINGLE_USER}{elem}""", data)
        Assertion.assert_status_code(response, er.STATUS_CODE_OK)
        Assertion.assert_response_have_be_json(response)

    @pytest.mark.parametrize("elem", range(1, random_number))
    @allure.title("Test check of the updated user for the presence of all keys")
    def test_create_put_user_has_all_keys(self, elem):
        """
        This test verifies that the response has all keys
        """
        data = self.prepare_creating_date()
        response = MyRequests.put(f"""{self.url.GET_SINGLE_USER}{elem}""", data)
        Assertion.assert_json_has_keys(response, CreateUser.update)

    #
    @pytest.mark.parametrize("elem", range(1, random_number))
    @allure.title("Test validation of the generated data")
    def test_create_put_user_created_data_is_correct(self, elem):
        """
        This test verifies that the response has the keys 'name' and 'job'
        """
        data = self.prepare_creating_date()
        response = MyRequests.put(f"""{self.url.GET_SINGLE_USER}{elem}""", data)
        CreatePut.assert_check_job_and_name_in_response(response, data)

    @pytest.mark.parametrize("elem", range(1, random_number))
    @allure.title("Test update user without name PUT method")
    def test_create_put_user_update_user_without_name(self, elem):
        """
        This test checks that the data has updated,
        the status code is 200, passed in the response json
        and that there is no key called 'name'
        """
        data = self.prepare_creating_date_job_only()
        response = MyRequests.put(f"""{self.url.GET_SINGLE_USER}{elem}""", data)
        Assertion.assert_status_code(response, er.STATUS_CODE_OK)
        Assertion.assert_response_have_be_json(response)
        Assertion.assert_json_has_not_key(response, "name")

    @pytest.mark.parametrize("elem", range(1, random_number))
    @allure.title("Test update user without job PUT method")
    def test_create_put_user_update_user_without_job(self, elem):
        """
        This test checks that the data has updated,
        the status code is 200, passed in the response json
        and that there is no key called 'job'
        """
        data = self.prepare_creating_date_name_only()
        response = MyRequests.put(f"""{self.url.GET_SINGLE_USER}{elem}""", data)
        Assertion.assert_status_code(response, er.STATUS_CODE_OK)
        Assertion.assert_response_have_be_json(response)
        Assertion.assert_json_has_not_key(response, "job")

    @pytest.mark.parametrize("elem", range(1, random_number))
    @allure.title("Test update user without job PUT method")
    def test_create_put_user_update_user_without_data(self, elem):
        """
        This test checks that the data has updated,
        the status code is 200, passed in the response json
        and that there is no key called "job"
        """
        response = MyRequests.put(f"""{self.url.GET_SINGLE_USER}{elem}""")
        Assertion.assert_status_code(response, er.STATUS_CODE_OK)
        Assertion.assert_response_have_be_json(response)
        Assertion.assert_json_has_not_keys(response, CreateUser.check_update)



