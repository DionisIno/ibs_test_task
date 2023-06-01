import random

import allure
from requests import Response

from framework.test_api_section.api_expected_result.base_url_and_path import GetUrl
from framework.test_api_section.pages_api.base_page import BasePage
from framework.test_api_section.pages_api.my_requests import MyRequests
from framework.test_api_section.api_expected_result.expected_result import Email, RegisterUser


class RegisterPost(BasePage):
    url = GetUrl()
    email = Email.email

    @allure.description("Register a new user")
    def register(self):
        """This method registers a new user"""
        email = random.choice(self.email)
        data = self.prepare_creating_registration_data(email)
        response = MyRequests.post(self.url.REGISTER_USER, data)
        return response, email

    @allure.description("Get user by id after registration")
    def get_user_by_id_after_registration(self, response):
        """This method get user by id"""
        s_id = response.json()["id"]
        response = MyRequests.get(f"{self.url.GET_SINGLE_USER}{s_id}")
        return response, s_id

    @allure.description("Registration with wrong email, password present")
    def register_with_wrong_email(self):
        """This method registers a new user with wrong email, password present"""
        data = self.prepare_creating_registration_data()
        response = MyRequests.post(self.url.REGISTER_USER, data)
        return response

    @allure.description("Registration without email, password present")
    def register_without_email(self):
        """This method registers a new user without email, password present"""
        data = self.prepare_creating_password()
        response = MyRequests.post(self.url.REGISTER_USER, data)
        return response

    @allure.description("Registration without password, email present")
    def register_without_password(self):
        """This method registers a new user without password, email present"""
        email = random.choice(self.email)
        data = self.prepare_creating_email(email)
        response = MyRequests.post(self.url.REGISTER_USER, data)
        return response

    @allure.description("Registration without password, email is wrong")
    def register_without_password_wrong_email(self):
        """This method registers a new user without password, email is wrong"""
        data = self.prepare_creating_email()
        response = MyRequests.post(self.url.REGISTER_USER, data)
        return response

    @staticmethod
    def check_email(email, response_after: Response):
        """Check email"""
        response = response_after.json()["data"]
        assert email == response.get("email"), f"Email is not equal {email}"

    @staticmethod
    def check_id(s_id, response_after: Response):
        """Check id"""
        response = response_after.json()["data"]
        assert s_id == response.get("id"), f"Id is not equal {s_id}"

    @staticmethod
    def check_error_message(response: Response):
        error_message = RegisterUser.error_message
        actual_error_message = response.json()["error"]
        assert actual_error_message in error_message, \
            f"Unexpected error message {actual_error_message}"

