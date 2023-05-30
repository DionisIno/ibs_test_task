import allure

from framework.test_web_section.pages.main_page import MainPage

MAIN_PAGE_LINK = 'https://reqres.in/'


@allure.epic("Testing header content")
class TestHeaderContent:
    @allure.suite("Testing Head Section")
    class TestHeadSection:
        @allure.title("Main page URL must be correct")
        def test_check_url_main_page(self, driver):
            """Check that the url is correct"""
            main_page = MainPage(driver, MAIN_PAGE_LINK)
            main_page.open()
            expected_url, actual_url = main_page.get_url()
            assert expected_url == actual_url, \
                f"Expected url {expected_url} is not equal actual url {actual_url}"

        @allure.title("The main page must have a title and it must be correct")
        def test_check_title_main_page(self, driver):
            """Check main page title"""
            main_page = MainPage(driver, MAIN_PAGE_LINK)
            main_page.open()
            expected_title, actual_title = main_page.get_title()
            assert expected_title == actual_title, \
                f"Expected title {expected_title} is not equal actual title {actual_title}"

    @allure.suite("Testing header section")
    class TestHeaderSection:

        @allure.title("Logo link must have status code 200")
        def test_check_logo_link_status_code(self, driver):
            """Check logo link status code"""
            main_page = MainPage(driver, MAIN_PAGE_LINK)
            main_page.open()

        @allure.title("The logo must have a valid link")
        def test_check_logo_link(self, driver):
            """Check logo link"""
            main_page = MainPage(driver, MAIN_PAGE_LINK)
            main_page.open()
            expected_logo_link, actual_logo_link = main_page.get_logo_link()
            assert expected_logo_link == actual_logo_link, \
                f"Expected logo link {expected_logo_link} is not equal actual logo link {actual_logo_link}"
