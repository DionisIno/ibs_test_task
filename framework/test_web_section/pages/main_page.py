import allure
import requests
from selenium.webdriver.common.by import By

from framework.test_api_section.api_expected_result.expected_result import ExpectedRequestsResult
from framework.data.test_data_main_page import TestData
from framework.test_web_section.locators.main_page_locators import MainPageLocators
from framework.test_web_section.pages.base_page import BasePage


class MainPage(BasePage):
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

