"""This section contain main page locators"""

from selenium.webdriver.common.by import By


class MainPageLocators:

    """Locators for the header section"""
    LOGO = (By.CSS_SELECTOR, "h1[class='logo'] > a > img")

    """Locators for the main section"""
    MAIN_H2_HEADING = [(By.CSS_SELECTOR, "h2[class='tagline']:nth-child(1)"),
               (By.CSS_SELECTOR, "h2[class='tagline']:nth-child(3)")]
    MAIN_H3_HEADINGS = (By.CSS_SELECTOR, "div[class='v-center'] > h3")
    MAIN_PARAGRAPHS = (By.CSS_SELECTOR, "div[class='v-center'] > p")

    """Locators for the home-content"""
    H2_CENTER_HEADING = (By.CSS_SELECTOR, "h2[class='t-center heading']")
    SUPPORT_BUTTON = (By.CSS_SELECTOR, "div[class='t-center'] button a")

    """Support section"""
    SUPPORT_TITLE = (By.CSS_SELECTOR, "h2[id='support-heading']")

    """Request"""
    REQUEST_URL = (By.CSS_SELECTOR, "a[class='link try-link']")
    REQUEST_INPUT = (By.CSS_SELECTOR, "pre[data-key='output-request']")

    """Response"""
    STATUS_CODE_200 = (By.CSS_SELECTOR, "span[class='response-code']")
    STATUS_CODE_404 = (By.CSS_SELECTOR, "span[class='response-code bad']")
    RESPONSE_OUTPUT = (By.CSS_SELECTOR, "pre[data-key='output-response']")

    """API call buttons"""
    GET_LIST_USERS_BUTTON = (By.CSS_SELECTOR, "div[class='endpoints'] ul li[data-id='users']")
    GET_SINGLE_USER_BUTTON = (By.CSS_SELECTOR, "div[class='endpoints'] ul li[data-id='users-single']")
    GET_SINGLE_USER_NOT_FOUND_BUTTON = (By.CSS_SELECTOR, "div[class='endpoints'] ul li["
                                                         "data-id='users-single-not-found']")
    GET_LIST_RESOURCE_BUTTON = (By.CSS_SELECTOR, "div[class='endpoints'] ul li[data-id='unknown']")
    GET_SINGLE_RESOURCE_BUTTON = (By.CSS_SELECTOR, "div[class='endpoints'] ul li[data-id='unknown-single']")
    GET_SINGLE_RESOURCE_NOT_FOUND_BUTTON = (By.CSS_SELECTOR, "div[class='endpoints'] ul li["
                                                             "data-id='unknown-single-not-found']")
