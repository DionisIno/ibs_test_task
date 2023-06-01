import random
import allure
from requests import Response
from framework.test_api_section.api_expected_result.base_url_and_path import GetUrl
from framework.test_api_section.pages_api.base_page import BasePage
from framework.test_api_section.pages_api.my_requests import MyRequests
from framework.test_api_section.api_expected_result.expected_result import Email, RegisterUser


class LoginPost(BasePage):
    url = GetUrl()
    email = Email.email

    @allure.description("User login successfully")
    def login(self):
        """This method registers a new user"""
        email = random.choice(self.email)
        data = self.prepare_creating_registration_data(email)
        response = MyRequests.post(self.url.LOGIN_USER, data)
        return response

    @allure.description("Login with wrong email, password present")
    def login_with_wrong_email(self):
        """This method login a new user with wrong email, password present"""
        data = self.prepare_creating_registration_data()
        response = MyRequests.post(self.url.LOGIN_USER, data)
        return response

    @allure.description("Registration without email, password present")
    def login_without_email(self):
        """This method login a new user without email, password present"""
        data = self.prepare_creating_password()
        response = MyRequests.post(self.url.LOGIN_USER, data)
        return response

    @allure.description("Login without password, email present")
    def login_without_password(self):
        """This method login a new user without password, email present"""
        email = random.choice(self.email)
        data = self.prepare_creating_email(email)
        response = MyRequests.post(self.url.LOGIN_USER, data)
        return response

    @allure.description("Login without password, email is wrong")
    def login_without_password_wrong_email(self):
        """This method login a new user without password, email is wrong"""
        data = self.prepare_creating_email()
        response = MyRequests.post(self.url.LOGIN_USER, data)
        return response

    @allure.description("Login without password and email")
    def login_without_password_and_email(self):
        """This method login a new user without password and email"""
        response = MyRequests.post(self.url.LOGIN_USER)
        return response

    @staticmethod
    def check_error_login_message(response: Response):
        error_message = RegisterUser.error_login_message
        actual_error_message = response.json()["error"]
        assert actual_error_message in error_message, \
            f"Unexpected error message {actual_error_message}"
