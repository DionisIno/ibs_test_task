import allure
import pytest

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
                f"Actual url is not equal {expected_url}"

        @allure.title("The main page must have a title and it must be correct")
        def test_check_title_main_page(self, driver):
            """Check main page title"""
            main_page = MainPage(driver, MAIN_PAGE_LINK)
            main_page.open()
            expected_title, actual_title = main_page.get_title()
            assert expected_title == actual_title, \
                f"Actual title is not equal {expected_title}"

    @allure.suite("Testing header section")
    class TestHeaderSection:

        @allure.title("Logo link must have status code 200")
        def test_check_logo_link_status_code(self, driver):
            """Check logo link status code"""
            main_page = MainPage(driver, MAIN_PAGE_LINK)
            main_page.open()
            expected_status_code, actual_status_code = main_page.get_status_code()
            assert expected_status_code == actual_status_code, \
                f"Actual status code is not equal {expected_status_code}"

        @allure.title("The logo must have a valid link")
        def test_check_logo_link(self, driver):
            """Check logo link"""
            main_page = MainPage(driver, MAIN_PAGE_LINK)
            main_page.open()
            expected_logo_link, actual_logo_link = main_page.get_logo_link()
            assert expected_logo_link == actual_logo_link, \
                f"Actual logo link is not equal {expected_logo_link}"

        @allure.title("The logo must have a image content type")
        def test_check_logo_content_type(self, driver):
            """Check logo content type"""
            main_page = MainPage(driver, MAIN_PAGE_LINK)
            main_page.open()
            expected_content_type, actual_content_type = main_page.get_image_content_type()
            assert expected_content_type == actual_content_type, \
                f"Actual image content type is not equal {expected_content_type}"

        @allure.title("The main page should have only one h1 heading")
        def test_check_count_h1_heading(self, driver):
            """Check that main page has only 1 h1 heading"""
            main_page = MainPage(driver, MAIN_PAGE_LINK)
            main_page.open()
            actual_count_of_h1_heading = main_page.get_count_of_h1_heading()
            assert len(actual_count_of_h1_heading) == 1, \
                "Actual count of h1 heading is not equal 1"

    @allure.suite("Testing main section")
    class TestMainSection:
        @pytest.mark.parametrize("elem", range(2))
        @allure.title("The main section must contain correct text in h2 headings")
        def test_check_text_h2_heading(self, driver, elem):
            """Check that h2 heading main section has correct text"""
            main_page = MainPage(driver, MAIN_PAGE_LINK)
            main_page.open()
            expected_text, actual_text = main_page.get_text_heading('h2', elem)
            assert expected_text == actual_text, f"Actual h2 text heading is not equal {expected_text}"

        @pytest.mark.parametrize("elem", range(3))
        @allure.title("The main section must contain correct text in h3 headings")
        def test_check_text_h3_heading(self, driver, elem):
            """Check that h3 heading main section has correct text"""
            main_page = MainPage(driver, MAIN_PAGE_LINK)
            main_page.open()
            expected_text, actual_text = main_page.get_text_heading('h3', elem)
            assert expected_text == actual_text, f"Actual h3 text heading is not equal {expected_text}"

        @pytest.mark.parametrize("elem", range(3))
        @allure.title("The main section must contain correct text in paragraph")
        def test_check_paragraph_text(self, driver, elem):
            """Check that paragraph main section has correct text"""
            main_page = MainPage(driver, MAIN_PAGE_LINK)
            main_page.open()
            expected_text, actual_text = main_page.get_text_paragraph(elem)
            assert expected_text == actual_text, f"Actual paragraph text is not equal {expected_text}"

    @allure.suite("Testing home content section")
    class TestHomeContent:
        @pytest.mark.parametrize("elem", range(8))
        @allure.title("The home content section must contain correct text in h2 headings")
        def test_check_h2_heading_text(self, driver, elem):
            """Check that h2 heading home content section has correct text"""
            main_page = MainPage(driver, MAIN_PAGE_LINK)
            main_page.open()
            expected_text, actual_text = main_page.get_text_heading("h2-center", elem)
            assert expected_text == actual_text, f"Actual h2 text heading is not equal {expected_text}"

        @allure.title("Check support button text")
        def test_check_support_button_text(self, driver):
            """Check that support button has correct text"""
            main_page = MainPage(driver, MAIN_PAGE_LINK)
            main_page.open()
            expected_text, actual_text = main_page.get_support_button_text()
            assert expected_text == actual_text, f"Actual button text is not equal {expected_text}"

        @allure.title("Check that after clicking on the button, a redirect to another section occurs")
        def test_check_that_the_button_redirects_to_another_section(self, driver):
            """Check redirect to another section"""
            main_page = MainPage(driver, MAIN_PAGE_LINK)
            main_page.open()
            text = main_page.click_on_the_support_button()
            assert text == "Support", "The redirect did not happen or happened to another location"

    @allure.suite("Testing console try api-links section")
    class TestApiCall:

        @allure.title("On the main page can see the correct data of the section 'List Users'")
        def test_get_list_users(self, driver):
            """
            This test takes the results of an API call and compares them
            with the results that are taken from the website.
            :param: GET USER LIST
            """
            page = MainPage(driver, MAIN_PAGE_LINK)
            page.open()
            page.get_list_user_data()

        @allure.title("On the main page can see the correct data of the section 'Single Users'")
        def test_get_single_users(self, driver):
            """
            This test takes the results of an API call and compares them
            with the results that are taken from the website.
            :param: GET SINGLE USER
            """
            page = MainPage(driver, MAIN_PAGE_LINK)
            page.open()
            page.get_single_user_data()

        @allure.title("On the main page can see the correct data of the section 'Single Users Not Found'")
        def test_get_single_user_not_found(self, driver):
            """
            This test takes the results of an API call and compares them
            with the results that are taken from the website.
            :param: SINGLE USER NOT FOUND
            """
            page = MainPage(driver, MAIN_PAGE_LINK)
            page.open()
            page.get_single_user_not_found()

        @allure.title("On the main page can see the correct data of the section 'Get List Resource'")
        def test_get_list_resource(self, driver):
            """
            This test takes the results of an API call and compares them
            with the results that are taken from the website.
            :param: LIST RESOURCE
            """
            page = MainPage(driver, MAIN_PAGE_LINK)
            page.open()
            page.get_list_resource()

        @allure.title("On the main page can see the correct data of the section 'Get Single Resource'")
        def test_get_single_resource(self, driver):
            """
            This test takes the results of an API call and compares them
            with the results that are taken from the website.
            :param: SINGLE RESOURCE
            """
            page = MainPage(driver, MAIN_PAGE_LINK)
            page.open()
            page.get_single_resource()

        @allure.title("On the main page can see the correct data of the section 'Get Single Resource Not Found'")
        def test_get_single_resource_not_found(self, driver):
            """
            This test takes the results of an API call and compares them
            with the results that are taken from the website.
            :param: SINGLE RESOURCE NOT FOUND
            """
            page = MainPage(driver, MAIN_PAGE_LINK)
            page.open()
            page.get_single_resource_not_found()
