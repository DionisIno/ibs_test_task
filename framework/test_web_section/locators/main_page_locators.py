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
