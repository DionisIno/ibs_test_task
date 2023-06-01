import requests
from requests import Response

from framework.test_api_section.api_expected_result.expected_result import \
    ExpectedCountUserList as el, SupportData, ExpectedRequestsResult as er


class Assertion:
    @staticmethod
    def assert_status_code(response: Response, expected_status_code):
        actual_status_code = response.status_code
        assert actual_status_code == expected_status_code, \
            f"Unexpected status code. Expected {expected_status_code}. Actual: {actual_status_code}"

    @staticmethod
    def assert_response_have_be_json(response: Response):
        assert 'application/json' in response.headers.get('Content-Type', ''), \
            "Error: Response is not in JSON format"

    @staticmethod
    def assert_response_should_have_valid_page_number(response: Response, send_number: int):
        page_number = response.json()["page"]
        assert page_number == send_number, \
            f"Answer page number should have {send_number} number but has {page_number} number"

    @staticmethod
    def assert_check_count_of_response_data(response: Response):
        data_list = response.json()["data"]
        expected_number = el.PER_PAGE
        if len(data_list) > 0:
            assert len(data_list) <= expected_number, \
                f"The number of users in 1 response is more than {expected_number}"
        else:
            assert len(data_list) == 0, \
                "Expected an empty data but got nothing"

    @staticmethod
    def assert_check_in_response_per_page_total_total_pages_have_correct_values(response: Response):
        per_page = response.json()["per_page"]
        total = response.json()["total"]
        total_pages = response.json()["total_pages"]
        assert per_page == el.PER_PAGE, \
            f"Per Page s not equal {el.PER_PAGE}"
        assert total == el.TOTAL, \
            f"Total is not equal {el.TOTAL}"
        assert total_pages == el.TOTAL_PAGES, \
            f"Total Page s not equal {el.TOTAL_PAGES}"

    @staticmethod
    def assert_response_should_have_data_key(response: Response):
        json_response = response.json()
        assert "data" in json_response, "Error: Key 'data' is missing from JSON response"

    @staticmethod
    def assert_response_should_have_support_key(response: Response):
        json_response = response.json()
        assert "support" in json_response, "Error: Key 'support' is missing from JSON response"

    @staticmethod
    def assert_support_have_correct_url(response: Response):
        Assertion.assert_response_should_have_support_key(response)
        actual_support_email = response.json()['support']['url']
        expected_support_email = SupportData.url
        assert actual_support_email == expected_support_email, \
            f"Actual support email is not equal {expected_support_email}"

    @staticmethod
    def assert_support_have_correct_text(response: Response):
        Assertion.assert_response_should_have_support_key(response)
        actual_support_text = response.json()['support']['text']
        expected_support_text = SupportData.message
        assert actual_support_text == expected_support_text, \
            f"Actual support email is not equal {expected_support_text}"

    @staticmethod
    def assert_users_have_id(response: Response, key):
        Assertion.assert_status_code(response, er.STATUS_CODE_OK)
        Assertion.assert_response_have_be_json(response)
        json_response = response.json()['data']
        if len(json_response) > 0:
            for elem in json_response:
                user_id = elem.get(key)
                assert user_id is not None, "Error: User does not have key 'id' or its value is None"
                assert isinstance(user_id, int), f"Error: Key value ({user_id}) is not a number"
        else:
            assert isinstance(json_response, list), \
                f"Expected an empty list but got {type(json_response)}"

    @staticmethod
    def assert_users_have_keys(response: Response, key):
        Assertion.assert_status_code(response, er.STATUS_CODE_OK)
        Assertion.assert_response_have_be_json(response)
        json_response = response.json()['data']
        if len(json_response) > 0:
            for elem in json_response:
                value = elem.get(key)
                assert value is not None, f"Error: User does not have key '{value}' or its value is None"
                assert isinstance(value, str), f"Error: Key value ({value}) is not a string"
        else:
            assert isinstance(json_response, list), \
                f"Expected an empty list but got {type(json_response)}"

    @staticmethod
    def assert_avatar_image_link_has_status_code_200(response: Response):
        json_response = response.json()['data']
        if len(json_response) > 0:
            for elem in json_response:
                img_link = elem.get("avatar")
                assert requests.get(img_link).status_code == er.STATUS_CODE_OK, \
                    f"Status code avatar img link is not equal {er.STATUS_CODE_OK}"