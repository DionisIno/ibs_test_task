import time
import allure
from framework.test_api_section.api_expected_result.base_url_and_path import GetUrl
from framework.test_api_section.pages_api.base_page import BasePage
from framework.test_api_section.pages_api.my_requests import MyRequests


class GetListResource(BasePage):
    url = GetUrl()

    @allure.description("Get delay response")
    def get_list_resource_response(self):
        response = MyRequests.get(f"""{self.url.GET_LIST_USERS}""")
        return response

