import allure
from framework.test_api_section.api_expected_result.base_url_and_path import GetUrl
from framework.test_api_section.pages_api.assertions import Assertion
from framework.test_api_section.pages_api.base_page import BasePage
from framework.test_api_section.pages_api.my_requests import MyRequests
from framework.test_api_section.api_expected_result.expected_result import ExpectedRequestsResult as er, CreateUser


class CreatePatch(BasePage):
    url = GetUrl()

    @allure.description("Update user data using name and job")
    def patch_update_user(self, elem):
        """
        Update a user with the keys name and job,
        checks that the status code is 200
        and that the response came in json format
        """
        data = self.prepare_creating_date()
        response = MyRequests.patch(f"""{self.url.GET_SINGLE_USER}{elem}""", data)
        Assertion.assert_status_code(response, er.STATUS_CODE_OK)
        Assertion.assert_response_have_be_json(response)
        return response, data

    @allure.description("Update user data using name only")
    def patch_update_user_with_name_only(self, elem):
        """
        Update a user with the key name,
        checks that the status code is 200
        and that the response came in json format
        """
        data = self.prepare_creating_date_name_only()
        response = MyRequests.patch(f"""{self.url.GET_SINGLE_USER}{elem}""", data)
        Assertion.assert_status_code(response, er.STATUS_CODE_OK)
        Assertion.assert_response_have_be_json(response)
        return response, data

    @allure.description("Update user data using job only")
    def patch_update_user_with_job_only(self, elem):
        """
        Update a user with the key job,
        checks that the status code is 200
        and that the response came in json format
        """
        data = self.prepare_creating_date_job_only()
        response = MyRequests.patch(f"""{self.url.GET_SINGLE_USER}{elem}""", data)
        Assertion.assert_status_code(response, er.STATUS_CODE_OK)
        Assertion.assert_response_have_be_json(response)
        return response, data

    @allure.description("Update user data using job only")
    def patch_update_user_without_data(self, elem):
        """
        Update a user without data,
        checks that the status code is 200
        and that the response came in json format
        """
        response = MyRequests.patch(f"""{self.url.GET_SINGLE_USER}{elem}""")
        Assertion.assert_status_code(response, er.STATUS_CODE_OK)
        Assertion.assert_response_have_be_json(response)
        return response
