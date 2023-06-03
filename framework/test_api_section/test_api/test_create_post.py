"""
API tests for POST Create method.
"""
import random

import allure
import pytest
from framework.test_api_section.api_expected_result.base_url_and_path import GetUrl
from framework.test_api_section.api_expected_result.expected_result import CreateUser
from framework.test_api_section.pages_api.assertions import Assertion
from framework.test_api_section.pages_api.create_post import CreatePost


@allure.epic('Testing POST Create method')
class TestPostCreate:
    url = GetUrl()
    random_number = random.randint(2, 13)

    @pytest.mark.parametrize("elem", range(1, random_number))
    @allure.title("Test created user successfully")
    def test_create_post_user_successfully(self, elem):
        """This test checks that the user was created successfully"""
        post_method = CreatePost()
        response, data = post_method.create_new_user()
        Assertion.assert_check_job_and_name_in_response(response, data)

    @pytest.mark.parametrize("elem", range(1, random_number))
    @allure.title("Test check of the created user for the presence of all keys")
    def test_create_post_user_has_all_keys(self, elem):
        """This test checks if the user was successfully created and if all keys are present"""
        post_method = CreatePost()
        response, data = post_method.create_new_user()
        Assertion.assert_json_has_keys(response, CreateUser.create)

    @pytest.mark.parametrize("elem", range(1, random_number))
    @allure.title("Test validation of the generated data")
    def test_create_post_user_created_data_is_correct(self, elem):
        """This test checks that the values of the keys name and operation match the given data"""
        post_method = CreatePost()
        response, data = post_method.create_new_user()
        Assertion.assert_check_job_and_name_in_response(response, data)

    @pytest.mark.parametrize("elem", range(1, random_number))
    @allure.title("Test created user with name only")
    def test_create_post_user_with_name_only(self, elem):
        """This test checks that the user was created  with name only"""
        post_method = CreatePost()
        response, data = post_method.create_new_user_with_only_name()
        Assertion.assert_json_has_key(response, "name")
        Assertion.assert_json_has_not_key(response, "job")

    @pytest.mark.parametrize("elem", range(1, random_number))
    @allure.title("Test created user with job only")
    def test_create_post_user_with_job_only(self, elem):
        """This test checks that the user was created  with job only"""
        post_method = CreatePost()
        response, data = post_method.create_new_user_with_only_job()
        Assertion.assert_json_has_key(response, "job")
        Assertion.assert_json_has_not_key(response, "name")

    @pytest.mark.parametrize("elem", range(1, random_number))
    @allure.title("Test created user without job and name")
    def test_create_post_user_without_data(self, elem):
        """This test checks that the user was created without job and name"""
        post_method = CreatePost()
        response = post_method.create_new_user_without_data()
        Assertion.assert_json_has_not_keys(response, CreateUser.check_update)

