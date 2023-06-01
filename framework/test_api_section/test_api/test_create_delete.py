"""
API tests for DELETE method.
"""
import random
import allure
import pytest
from framework.test_api_section.api_expected_result.base_url_and_path import GetUrl
from framework.test_api_section.api_expected_result.expected_result import CreateUser, ExpectedRequestsResult as er
from framework.test_api_section.pages_api.assertions import Assertion
from framework.test_api_section.pages_api.create_delete import CreateDelete
from framework.test_api_section.pages_api.create_post import CreatePost


@allure.epic('Testing DELETE method')
class TestDelete:
    url = GetUrl()
    random_number = random.randint(2, 13)

    @pytest.mark.parametrize("elem", range(1, random_number))
    @allure.title("Test delete user")
    def test_delete_user(self, elem):
        """
        This test checks that the user was deleted
        and status code 204
        """
        post_method = CreatePost()
        delete_method = CreateDelete()
        """Create new user"""
        response_before, data = post_method.create_new_user(elem)
        """Delete user"""
        response_after = delete_method.delete_user(elem, data)
        """checks that the status code is 204"""
        Assertion.assert_status_code(response_after, er.NO_CONTENT)

    @pytest.mark.parametrize("elem", range(1, random_number))
    @allure.title("Test delete user has not data")
    def test_delete_user_has_empty_data(self, elem):
        """
        This test checks that the user was deleted
        and response is empty
        """
        post_method = CreatePost()
        delete_method = CreateDelete()
        """Create new user"""
        response_before, data = post_method.create_new_user(elem)
        """Delete user"""
        response_after = delete_method.delete_user(elem, data)
        """checks that the response is empty"""
        Assertion.assert_check_response_is_empty(response_after)



