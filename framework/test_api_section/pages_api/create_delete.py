import allure
from framework.test_api_section.api_expected_result.base_url_and_path import GetUrl
from framework.test_api_section.pages_api.assertions import Assertion
from framework.test_api_section.pages_api.base_page import BasePage
from framework.test_api_section.pages_api.my_requests import MyRequests
from framework.test_api_section.api_expected_result.expected_result import ExpectedRequestsResult as er, CreateUser


class CreateDelete(BasePage):
    url = GetUrl()

    @allure.description("Delete user")
    def delete_user(self, elem, data):
        """
        Creates a user with the keys name and job,
        checks that the status code is 201
        and that the response came in json format
        """
        data = self.prepare_creating_date()
        response = MyRequests.delete(f"""{self.url.GET_SINGLE_USER}{elem}""", data)
        return response
