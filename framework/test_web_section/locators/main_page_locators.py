"""This section contains homepage locators"""

from selenium.webdriver.common.by import By


class MainPageLocators:

    """Locators for the header section"""
    LOGO = (By.CSS_SELECTOR, "h1[class='logo'] > a > img")