"""
API tests for PUT Create method.
"""
import random
import allure
import pytest
from framework.test_api_section.api_expected_result.base_url_and_path import GetUrl
from framework.test_api_section.api_expected_result.expected_result import CreateUser
from framework.test_api_section.pages_api.assertions import Assertion
from framework.test_api_section.pages_api.base_page import BasePage
from framework.test_api_section.pages_api.create_post import CreatePost
from framework.test_api_section.pages_api.create_put import CreatePut



@allure.epic('Testing PUT Create method')
class TestPutCreate(BasePage):
    url = GetUrl()
    random_number = random.randint(2, 13)

    @pytest.mark.parametrize("elem", range(1, random_number))
    @allure.title("Test update user successfully PUT method")
    def test_create_put_user_update_user(self, elem):
        """
        This test checks that the data has changed
        """
        post_method = CreatePost()
        put_method = CreatePut()
        """Create new user"""
        response_before, data_before = post_method.create_new_user(elem)
        """Update created user"""
        response_after, data_after = put_method.put_update_user(elem)
        """Check that values changed"""
        Assertion.assert_check_dict_values_name_changed(response_before, response_after)
        Assertion.assert_check_dict_values_job_changed(response_before, response_after)

    @pytest.mark.parametrize("elem", range(1, random_number))
    @allure.title("Test check of the updated user for the presence of all keys")
    def test_create_put_user_has_all_keys(self, elem):
        """
        This test verifies that the response has all keys
        :param for check response_before keys - ["name", "job", "id", "createdAt"]
        :param for check response_after keys - ["name", "job", "updatedAt"]
        """
        post_method = CreatePost()
        put_method = CreatePut()
        """Create new user and check all keys"""
        response_before, data_before = post_method.create_new_user(elem)
        Assertion.assert_json_has_keys(response_before, CreateUser.create)
        """Update created user and check all keys"""
        response_after, data_after = put_method.put_update_user(elem)
        Assertion.assert_json_has_keys(response_after, CreateUser.update)

    @pytest.mark.parametrize("elem", range(1, random_number))
    @allure.title("Test update user without name PUT method")
    def test_create_put_user_update_user_without_name(self, elem):
        """
        This test checks that the data has updated,
        there is no key called 'name'
        """
        post_method = CreatePost()
        put_method = CreatePut()
        """Create new user"""
        response_before, data_before = post_method.create_new_user(elem)
        """Create new user with job only"""
        response_after, data_after = put_method.put_update_user_with_job_only(elem)
        """Check that key 'job' value changed and not key 'name'"""
        Assertion.assert_check_dict_values_job_changed(response_before, response_after)
        Assertion.assert_json_has_not_key(response_after, "name")

    @pytest.mark.parametrize("elem", range(1, random_number))
    @allure.title("Test update user without job PUT method")
    def test_create_put_user_update_user_without_job(self, elem):
        """
        This test checks that the data has updated,
        there is no key called 'job'
        """
        post_method = CreatePost()
        put_method = CreatePut()
        """Create new user"""
        response_before, data_before = post_method.create_new_user(elem)
        """Create new user with name only"""
        response_after, data_after = put_method.put_update_user_with_name_only(elem)
        """Check that key 'name' value changed and not key 'job'"""
        Assertion.assert_check_dict_values_name_changed(response_before, response_after)
        Assertion.assert_json_has_not_key(response_after, "job")

    @pytest.mark.parametrize("elem", range(1, random_number))
    @allure.title("Test update user without job PUT method")
    def test_create_put_user_update_user_without_data(self, elem):
        """
        This test checks that the data has updated,
        the status code is 200, passed in the response json
        and that there is no key called "job"
        """
        post_method = CreatePost()
        put_method = CreatePut()
        """Create new user"""
        response_before, data_before = post_method.create_new_user(elem)
        """Create new user without data"""
        response_after = put_method.put_update_user_without_data(elem)
        """Check that not keys 'name' and 'job'"""
        Assertion.assert_json_has_not_keys(response_after, CreateUser.check_update)




