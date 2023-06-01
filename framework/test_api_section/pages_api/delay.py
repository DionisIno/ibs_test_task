import time
import allure
from framework.test_api_section.api_expected_result.base_url_and_path import GetUrl
from framework.test_api_section.pages_api.base_page import BasePage
from framework.test_api_section.pages_api.my_requests import MyRequests


class DelayResponse(BasePage):
    url = GetUrl()

    @allure.description("Get delay response")
    def get_delay_response(self, elem):
        response = MyRequests.get(f"""{self.url.DELAY}{elem}""")
        return response

    @allure.description("Get delay response")
    def get_delay_check_page_loading(self, elem):
        start_time = time.time()
        MyRequests.get(f"""{self.url.DELAY}{elem}""")
        end_time = time.time()
        delay = end_time - start_time
        assert delay <= 30, "Page load time exceeds 30 seconds"
