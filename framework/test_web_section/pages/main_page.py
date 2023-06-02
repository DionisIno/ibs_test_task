import json

import allure
import requests

from framework.test_api_section.api_expected_result.expected_result import ExpectedRequestsResult
from framework.data.test_data_main_page import TestData
from framework.test_web_section.locators.main_page_locators import MainPageLocators
from framework.test_web_section.pages.api_method_for_main_page import GetApiMethod
from framework.test_web_section.pages.base_page import BasePage


class MainPage(BasePage, GetApiMethod):
    locators = MainPageLocators
    test_data = TestData
    status_code = ExpectedRequestsResult

    @allure.step("Get main page url")
    def get_url(self):
        expected_url = self.test_data.main_page_url
        actual_url = self.driver.current_url
        return expected_url, actual_url

    @allure.step("Get main page title")
    def get_title(self):
        expected_title = self.test_data.main_page_title
        actual_title = self.driver.title
        return expected_title, actual_title

    @allure.step("Get logo link")
    def get_logo_link(self):
        expected_logo_link = self.test_data.logo_link
        actual_logo_link = self.element_is_visible(self.locators.LOGO).get_attribute("src")
        return expected_logo_link, actual_logo_link

    @allure.step("Get logo link status code")
    def get_status_code(self):
        expected_status_code = self.status_code.STATUS_CODE_OK
        link = self.element_is_visible(self.locators.LOGO).get_attribute("src")
        actual_status_code = requests.get(link).status_code
        return expected_status_code, actual_status_code

    @allure.step("Get logo content type")
    def get_image_content_type(self):
        expected_content_type = self.test_data.image_content_type
        link = self.element_is_visible(self.locators.LOGO).get_attribute("src")
        actual_content_type = requests.get(link).headers.get("Content-Type")
        return expected_content_type, actual_content_type

    @allure.step("Get count of h1 heading")
    def get_count_of_h1_heading(self):
        actual_count_h1_heading = self.driver.execute_script("return document.getElementsByTagName('h1');")
        return actual_count_h1_heading

    @allure.step("Get text heading")
    def get_text_heading(self, item, elem=0):
        if item == 'h2':
            expected_text = self.test_data.main_h2_heading[elem]
            actual_text = self.element_is_visible(self.locators.MAIN_H2_HEADING[elem])
            return expected_text, actual_text.text
        elif item == 'h3':
            expected_text = self.test_data.main_h3_heading[elem]
            actual_text = self.elements_are_visible(self.locators.MAIN_H3_HEADINGS)
            return expected_text, actual_text[elem].text
        elif item == 'h2-center':
            expected_text = self.test_data.home_content_h2_heading[elem]
            actual_text = self.elements_are_visible(self.locators.H2_CENTER_HEADING)
            return expected_text, actual_text[elem].text

    @allure.step("Get text paragraph")
    def get_text_paragraph(self, elem=0):
        expected_text = self.test_data.main_paragraph[elem]
        actual_text = self.elements_are_visible(self.locators.MAIN_PARAGRAPHS)
        return expected_text, actual_text[elem].text

    @allure.step("Get support button text")
    def get_support_button_text(self):
        expected_text = self.test_data.support_button_text
        actual_text = self.element_is_visible(self.locators.SUPPORT_BUTTON).text
        return expected_text, actual_text

    @allure.step("Click on the button and get text")
    def click_on_the_support_button(self):
        button = self.element_is_visible(self.locators.SUPPORT_BUTTON)
        button.click()
        text = self.element_is_visible(self.locators.SUPPORT_TITLE).text
        return text

    @allure.step("GET USER LIST. Compare data on the site and get data from the request")
    def click_on_the_get_list_user_button(self):
        with allure.step("Click on the button"):
            button = self.element_is_visible(self.locators.GET_LIST_USERS_BUTTON)
            button.click()
        with allure.step("Get url"):
            url = self.request_method()
        with allure.step("Get data from website"):
            status_code, response_output = self.response_method()
            response_out_ui = json.loads(response_output)
            response_out_ui = json.dumps(response_out_ui, indent=None)
        with allure.step("Get data from the request"):
            get_status_code, get_text = self.get_list_user(url)
            response_out_api_call = json.loads(get_text)
            response_out_api_call = json.dumps(response_out_api_call, indent=None)
        assert response_out_ui == response_out_api_call, "Responses are not identical"

    @allure.step("GET SINGLE USER. Compare data on the site and get data from the request")
    def click_on_the_get_single_user_button(self):
        with allure.step("Click on the button"):
            button = self.element_is_visible(self.locators.GET_SINGLE_USER_BUTTON)
            button.click()
        with allure.step("Get url"):
            url = self.request_method()
        with allure.step("Get data from website"):
            status_code, response_output = self.response_method()
            response_out_ui = json.loads(response_output)
            response_out_ui = json.dumps(response_out_ui, indent=None)
        with allure.step("Get data from the request"):
            get_status_code, get_text = self.get_list_user(url)
            response_out_api_call = json.loads(get_text)
            response_out_api_call = json.dumps(response_out_api_call, indent=None)
        assert int(status_code) == get_status_code, f"Status code not equal {get_status_code}"
        assert response_out_ui == response_out_api_call, "Responses are not identical"

    def request_method(self):
        url = self.element_is_visible(self.locators.REQUEST_URL).get_attribute("href")
        return url

    def response_method(self):
        status_code = self.element_is_visible(self.locators.STATUS_CODE).text
        response_output = self.element_is_visible(self.locators.RESPONSE_OUTPUT).text
        return status_code, response_output
