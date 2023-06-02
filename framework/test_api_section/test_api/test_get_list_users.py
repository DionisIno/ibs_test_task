"""
API tests for GET LIST USERS.
"""
import random
import allure
import pytest
from framework.test_api_section.api_expected_result.base_url_and_path import GetUrl
from framework.test_api_section.pages_api.assertions import Assertion
from framework.test_api_section.pages_api.my_requests import MyRequests
from framework.test_api_section.api_expected_result.expected_result import ExpectedRequestsResult as er


@allure.epic("Testing GET LIST USERS")
class TestGetListUsers:
    url = GetUrl()
    random_number = random.randint(2, 13)

    @pytest.mark.parametrize("elem", range(1, random_number))
    @allure.title("Test should return status code 200")
    def test_get_list_users_should_return_status_code_200(self, elem):
        """
        This test checks that the response has status code is 200
        """
        response = MyRequests.get(f"""{self.url.GET_LIST_USERS}{elem}""")
        Assertion.assert_status_code(response, er.STATUS_CODE_OK)

    @pytest.mark.parametrize("elem", range(1, random_number))
    @allure.title("Test test should check if the response is in json format")
    def test_get_list_users_should_have_be_json(self, elem):
        """
        This test checks that the response should be a json
        """
        response = MyRequests.get(f"""{self.url.GET_LIST_USERS}{elem}""")
        Assertion.assert_response_have_be_json(response)

    @pytest.mark.parametrize("elem", range(1, random_number))
    @allure.title("The test is to check if the response has a valid page number")
    def test_get_list_users_response_should_have_correct_page_number(self, elem):
        """
        This test checks if the response has a valid page number
        """
        response = MyRequests.get(f"""{self.url.GET_LIST_USERS}{elem}""")
        Assertion.assert_response_should_have_valid_page_number(response, elem)

    @pytest.mark.parametrize("elem", range(1, random_number))
    @allure.title("The test is to check count items in response data")
    def test_get_list_users_check_count_items_in_response_data(self, elem):
        """
        This test check count items in response data
        """
        response = MyRequests.get(f"""{self.url.GET_LIST_USERS}{elem}""")
        Assertion.assert_check_count_of_response_data(response)

    @pytest.mark.parametrize("elem", range(1, random_number))
    @allure.title("The test checks that in the response per_page, total, total_pages should have the correct values")
    def test_get_list_users_in_response_per_page_total_total_pages_should_have_correct_values(self, elem):
        """
        This test checks that in the response per_page, total, total_pages should have the correct values
        """
        response = MyRequests.get(f"""{self.url.GET_LIST_USERS}{elem}""")
        Assertion.assert_check_in_response_per_page_total_total_pages_have_correct_values(response)

    @pytest.mark.parametrize("elem", range(1, random_number))
    @allure.title("The test checks that the list user response has data key")
    def test_get_list_users_check_response_has_data_key(self, elem):
        """
        This test checks that the list user response has data key
        """
        response = MyRequests.get(f"""{self.url.GET_LIST_USERS}{elem}""")
        Assertion.assert_response_should_have_data_key(response)

    @pytest.mark.parametrize("elem", range(1, random_number))
    @allure.title("The test checks that the list user response has support key")
    def test_get_list_users_check_response_has_support_key(self, elem):
        """
        This test checks that the list user response has support key
        """
        response = MyRequests.get(f"""{self.url.GET_LIST_USERS}{elem}""")
        Assertion.assert_response_should_have_support_key(response)

    @pytest.mark.parametrize("elem", range(1, random_number))
    @allure.title("The test checks that the support has correct email")
    def test_get_list_users_check_support_has_correct_url(self, elem):
        """
        This test checks that the response should have support email
        """
        response = MyRequests.get(f"""{self.url.GET_LIST_USERS}{elem}""")
        Assertion.assert_support_have_correct_url(response)

    @pytest.mark.parametrize("elem", range(1, random_number))
    @allure.title("The test checks that the support has correct text")
    def test_get_list_users_check_support_has_correct_text(self, elem):
        """
        This test checks that the response should have support text
        """
        response = MyRequests.get(f"""{self.url.GET_LIST_USERS}{elem}""")
        Assertion.assert_support_have_correct_text(response)

    @pytest.mark.parametrize("elem", range(1, random_number))
    @allure.title("The test checks that all users have ids")
    def test_get_list_users_check_ids(self, elem):
        """
        This test checks that the response should have id
        """
        response = MyRequests.get(f"""{self.url.GET_LIST_USERS}{elem}""")
        Assertion.assert_users_have_id(response, "id")

    @pytest.mark.parametrize("elem", range(1, random_number))
    @allure.title("The test checks that all users have emails")
    def test_get_list_users_check_email(self, elem):
        """
        This test checks that the response should have emails
        """
        response = MyRequests.get(f"""{self.url.GET_LIST_USERS}{elem}""")
        Assertion.assert_users_have_keys(response, "email")

    @pytest.mark.parametrize("elem", range(1, random_number))
    @allure.title("The test checks that all users have first names")
    def test_get_list_users_check_first_name(self, elem):
        """
        This test checks that the response should have first names
        """
        response = MyRequests.get(f"""{self.url.GET_LIST_USERS}{elem}""")
        Assertion.assert_users_have_keys(response, "first_name")

    @pytest.mark.parametrize("elem", range(1, random_number))
    @allure.title("The test checks that all users have last names")
    def test_get_list_users_check_last_name(self, elem):
        """
        This test checks that the response should have last names
        """
        response = MyRequests.get(f"""{self.url.GET_LIST_USERS}{elem}""")
        Assertion.assert_users_have_keys(response, "last_name")

    @pytest.mark.parametrize("elem", range(1, random_number))
    @allure.title("The test checks that all users have avatars")
    def test_get_list_users_check_avatar(self, elem):
        """
        This test checks that the response should have avatars
        """
        response = MyRequests.get(f"""{self.url.GET_LIST_USERS}{elem}""")
        Assertion.assert_users_have_keys(response, "avatar")

    @pytest.mark.parametrize("elem", range(1, random_number))
    @allure.title("The test checks that the avatar image has a status code of 200")
    def test_get_list_users_check_avatar_image_link_has_status_code_200(self, elem):
        """
        This test checks that the avatar image has a status code of 200
        """
        response = MyRequests.get(f"""{self.url.GET_LIST_USERS}{elem}""")
        Assertion.assert_avatar_image_link_has_status_code_200(response)
