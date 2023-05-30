import allure

from framework.data.test_data_main_page import TestData
from framework.test_web_section.locators.main_page_locators import MainPageLocators
from framework.test_web_section.pages.base_page import BasePage


class MainPage(BasePage, TestData):
    locators = MainPageLocators

    @allure.step("Get main page url")
    def get_url(self):
        expected_url = self.main_page_url
        actual_url = self.driver.current_url
        return expected_url, actual_url

    @allure.step("Get main page title")
    def get_title(self):
        expected_title = self.main_page_title
        actual_title = self.driver.title
        return expected_title, actual_title

    @allure.step("Get logo link")
    def get_logo_link(self):
        expected_logo_link = self.logo_link
        actual_logo_link = self.element_is_visible(self.locators.LOGO).get_attribute("src")
        return expected_logo_link, actual_logo_link


