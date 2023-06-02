import allure
from requests import Response

from framework.test_api_section.api_expected_result.base_url_and_path import GetUrl
from framework.test_api_section.pages_api.base_page import BasePage
from framework.test_api_section.pages_api.my_requests import MyRequests


class GetSingleResource(BasePage):
    url = GetUrl()

    @allure.description("Get delay response")
    def get_single_resource_response(self, elem):
        response = MyRequests.get(f"""{self.url.SINGLE_RESOURCE}{elem}""")
        return response

    @staticmethod
    def assert_get_single_user_not_found_has_empty_json(response: Response):
        assert not response.json(), "Error: JSON is not empty"
