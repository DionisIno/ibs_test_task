import allure
from framework.test_api_section.api_expected_result.base_url_and_path import GetUrl
from framework.test_api_section.pages_api.assertions import Assertion
from framework.test_api_section.pages_api.base_page import BasePage
from framework.test_api_section.pages_api.my_requests import MyRequests
from framework.test_api_section.api_expected_result.expected_result import ExpectedRequestsResult as er, CreateUser


class CreatePost(BasePage):
    url = GetUrl()

    @allure.description("Create user with job and name")
    def create_new_user(self, elem):
        """
        Creates a user with the keys name and job,
        checks that the status code is 201
        and that the response came in json format
        """
        data = self.prepare_creating_date()
        response = MyRequests.post(f"""{self.url.GET_SINGLE_USER}{elem}""", data)
        Assertion.assert_status_code(response, er.CREATED)
        Assertion.assert_response_have_be_json(response)
        return response, data

    @allure.description("Create user with name only")
    def create_new_user_with_only_name(self, elem):
        """
            Creates a user with the keys name,
            checks that the status code is 201
            and that the response came in json format
        """
        data = self.prepare_creating_date_name_only()
        response = MyRequests.post(f"""{self.url.GET_SINGLE_USER}{elem}""", data)
        Assertion.assert_status_code(response, er.CREATED)
        Assertion.assert_response_have_be_json(response)
        return response, data

    @allure.description("Create user with job only")
    def create_new_user_with_only_job(self, elem):
        """
            Creates a user with the keys job,
            checks that the status code is 201
            and that the response came in json format
        """
        data = self.prepare_creating_date_job_only()
        response = MyRequests.post(f"""{self.url.GET_SINGLE_USER}{elem}""", data)
        Assertion.assert_status_code(response, er.CREATED)
        Assertion.assert_response_have_be_json(response)
        return response, data

    @allure.description("Create user without job and name")
    def create_new_user_without_data(self, elem):
        """
            Creates a user without data,
            checks that the status code is 201
            and that the response came in json format
        """
        response = MyRequests.post(f"""{self.url.GET_SINGLE_USER}{elem}""")
        Assertion.assert_status_code(response, er.CREATED)
        Assertion.assert_response_have_be_json(response)
        return response
