"""
API tests for POST login.
"""
import random
import allure
import pytest
from framework.test_api_section.api_expected_result.base_url_and_path import GetUrl
from framework.test_api_section.api_expected_result.expected_result import RegisterUser, ExpectedRequestsResult as er
from framework.test_api_section.pages_api.assertions import Assertion
from framework.test_api_section.pages_api.post_login import LoginPost


@allure.epic('Testing POST login successful and unsuccessful')
class TestPostRegister:
    url = GetUrl()
    random_number = random.randint(2, 5)

    @pytest.mark.parametrize("elem", range(1, random_number))
    @allure.title("Test login user successfully")
    def test_post_login_user_successfully(self, elem):
        """
        This test checks that the user was login successfully
        and status code is 200
        """
        post_method = LoginPost()
        response = post_method.login()
        Assertion.assert_status_code(response, er.STATUS_CODE_OK)

    @pytest.mark.parametrize("elem", range(1, random_number))
    @allure.title("Test login user successfully and check token keys")
    def test_post_login_get_token(self, elem):
        """
        This test checks that the user was login successfully
        and check token keys
        """
        post_method = LoginPost()
        response = post_method.login()
        Assertion.assert_json_has_key(response, RegisterUser.login)

    @pytest.mark.parametrize("elem", range(1, random_number))
    @allure.title("Test check login with wrong email address, password present. Get status code 400")
    def test_post_unsuccessful_login_get_status_code(self, elem):
        """
        This test check unsuccessful login with wrong email and expect status code 400
        """
        post_method = LoginPost()
        response = post_method.login_with_wrong_email()
        print(response.json())
        Assertion.assert_status_code(response, er.BAD_REQUEST)

    @pytest.mark.parametrize("elem", range(1, random_number))
    @allure.title("Test check login without email address, password present. Get status code 400")
    def test_post_unsuccessful_login_get_status_code_without_email(self, elem):
        """
        This test check unsuccessful login without email and expect status code 400
        """
        post_method = LoginPost()
        response = post_method.login_without_email()
        print(response.json())
        Assertion.assert_status_code(response, er.BAD_REQUEST)

    @pytest.mark.parametrize("elem", range(1, random_number))
    @allure.title("Test check login without password. Get status code 400")
    def test_post_unsuccessful_login_get_status_code_without_password(self, elem):
        """
        This test check unsuccessful login without password and expect status code 400
        """
        post_method = LoginPost()
        response = post_method.login_without_password()
        print(response.json())
        Assertion.assert_status_code(response, er.BAD_REQUEST)

    @pytest.mark.parametrize("elem", range(1, random_number))
    @allure.title("Test check login without password, wrong email. Get status code 400")
    def test_post_unsuccessful_login_get_status_code_without_password_wrong_email(self, elem):
        """
        This test check unsuccessful login without password, wrong email and expect status code 400
        """
        post_method = LoginPost()
        response = post_method.login_without_password_wrong_email()
        print(response.json())
        Assertion.assert_status_code(response, er.BAD_REQUEST)

    @pytest.mark.parametrize("elem", range(1, random_number))
    @allure.title("Test check login without password and email. Get status code 400")
    def test_post_unsuccessful_login_get_status_code_without_password_and_email(self, elem):
        """
        This test check unsuccessful login without password and email and expect status code 400
        """
        post_method = LoginPost()
        response = post_method.login_without_password_and_email()
        print(response.json())
        Assertion.assert_status_code(response, er.BAD_REQUEST)

    @pytest.mark.parametrize("elem", range(1, random_number))
    @allure.title("Test check unsuccessful login and get error message")
    def test_post_unsuccessful_login_get_status_code_without_password_wrong_email(self, elem):
        """
        This test check unsuccessful login and get error message
        """
        post_method = LoginPost()
        wrong_methods = [post_method.login_with_wrong_email(),
                         post_method.login_without_email(),
                         post_method.login_without_password(),
                         post_method.login_without_password_wrong_email(),
                         post_method.login_without_password_and_email()]
        response = random.choice(wrong_methods)
        post_method.check_error_login_message(response)
