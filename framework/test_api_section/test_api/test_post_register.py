"""
API tests for POST register.
"""
import random
import allure
import pytest
from framework.test_api_section.api_expected_result.base_url_and_path import GetUrl
from framework.test_api_section.api_expected_result.expected_result import RegisterUser, ExpectedRequestsResult as er
from framework.test_api_section.pages_api.assertions import Assertion
from framework.test_api_section.pages_api.post_register import RegisterPost


@allure.epic('Testing POST register successful and unsuccessful')
class TestPostRegister:
    url = GetUrl()
    random_number = random.randint(2, 5)

    @pytest.mark.parametrize("elem", range(1, random_number))
    @allure.title("Test register user successfully")
    def test_post_register_user_successfully(self, elem):
        """
        This test checks that the user was registered successfully
        and status code is 200
        """
        post_method = RegisterPost()
        response, email = post_method.register()
        Assertion.assert_status_code(response, er.STATUS_CODE_OK)

    @pytest.mark.parametrize("elem", range(1, random_number))
    @allure.title("Test register user successfully and check id and token keys")
    def test_post_register_get_token_and_id(self, elem):
        """
        This test checks that the user was registered successfully
        and check token and id keys
        """
        post_method = RegisterPost()
        response, email = post_method.register()
        Assertion.assert_json_has_keys(response, RegisterUser.register)

    @pytest.mark.parametrize("elem", range(1, random_number))
    @allure.title("Test check that email and id are correct")
    def test_post_register_get_user_by_id_after_registration(self, elem):
        """
        This test checks that the user was registered successfully,
        id and email are correct
        """
        post_method = RegisterPost()
        response_before, email = post_method.register()
        response_after, s_id = post_method.get_user_by_id_after_registration(response_before)
        post_method.check_email(email, response_after)
        post_method.check_id(s_id, response_after)

    @pytest.mark.parametrize("elem", range(1, random_number))
    @allure.title("Test check registration with wrong email address, password present. Get status code 400")
    def test_post_unsuccessful_register_get_status_code(self, elem):
        """
        This test check unsuccessful registration and expect status code 400
        """
        post_method = RegisterPost()
        response = post_method.register_with_wrong_email()
        print(response.json())
        Assertion.assert_status_code(response, er.BAD_REQUEST)

    @pytest.mark.parametrize("elem", range(1, random_number))
    @allure.title("Test check registration without email address, password present. Get status code 400")
    def test_post_unsuccessful_register_get_status_code_without_email(self, elem):
        """
        This test check unsuccessful registration without email and expect status code 400
        """
        post_method = RegisterPost()
        response = post_method.register_without_email()
        Assertion.assert_status_code(response, er.BAD_REQUEST)

    @pytest.mark.parametrize("elem", range(1, random_number))
    @allure.title("Test check registration without password. Get status code 400")
    def test_post_unsuccessful_register_get_status_code_without_password(self, elem):
        """
        This test check unsuccessful registration without password and expect status code 400
        """
        post_method = RegisterPost()
        response = post_method.register_without_password()
        Assertion.assert_status_code(response, er.BAD_REQUEST)

    @pytest.mark.parametrize("elem", range(1, random_number))
    @allure.title("Test check registration without password, wrong email. Get status code 400")
    def test_post_unsuccessful_register_get_status_code_without_password_wrong_email(self, elem):
        """
        This test check unsuccessful registration without password, wrong email and expect status code 400
        """
        post_method = RegisterPost()
        response = post_method.register_without_password_wrong_email()
        Assertion.assert_status_code(response, er.BAD_REQUEST)

    @pytest.mark.parametrize("elem", range(1, random_number))
    @allure.title("Test check unsuccessful registration and get error message")
    def test_post_unsuccessful_register_get_status_code_without_password_wrong_email(self, elem):
        """
        This test check unsuccessful registration and get error message
        """
        post_method = RegisterPost()
        wrong_methods = [post_method.register_with_wrong_email(),
                         post_method.register_without_email(),
                         post_method.register_without_password(),
                         post_method.register_without_password_wrong_email()]
        response = random.choice(wrong_methods)
        post_method.check_error_message(response)
