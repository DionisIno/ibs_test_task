import requests
from requests import Response

from framework.test_api_section.api_expected_result.expected_result import ExpectedCountUserList, SupportData


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
        expected_number = ExpectedCountUserList.PER_PAGE
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
        assert per_page == ExpectedCountUserList.PER_PAGE, \
            f"Per Page s not equal {ExpectedCountUserList.PER_PAGE}"
        assert total == ExpectedCountUserList.TOTAL, \
            f"Total is not equal {ExpectedCountUserList.TOTAL}"
        assert total_pages == ExpectedCountUserList.TOTAL_PAGES, \
            f"Total Page s not equal {ExpectedCountUserList.TOTAL_PAGES}"

    @staticmethod
    def assert_response_should_have_support(response: Response):
        json_response = response.json()
        assert "support" in json_response, "Error: Key 'support' is missing from JSON response"

    @staticmethod
    def assert_support_have_correct_email(response: Response):
        Assertion.assert_response_should_have_support(response)
        actual_support_email = response.json()['support']['url']
        expected_support_email = SupportData.url
        assert actual_support_email == expected_support_email, \
            f"Actual support email is not equal {expected_support_email}"

    @staticmethod
    def assert_support_have_correct_text(response: Response):
        Assertion.assert_response_should_have_support(response)
        actual_support_text = response.json()['support']['text']
        expected_support_text = SupportData.message
        assert actual_support_text == expected_support_text, \
            f"Actual support email is not equal {expected_support_text}"

    @staticmethod
    def assert_users_have_values(response: Response, key):
        json_response = response.json()['data']
        if len(json_response) > 0:
            if key == "id":
                for elem in json_response:
                    user_id = elem.get("id")
                    assert user_id is not None, "Error: User does not have key 'id' or its value is None"
                    assert isinstance(user_id, int), f"Error: Key value ({user_id}) is not a number"
            elif key == "email":
                for elem in json_response:
                    email = elem.get("email")
                    assert email is not None, "Error: User does not have key 'email' or its value is None"
                    assert isinstance(email, str), f"Error: Key value ({email}) is not a string"
            elif key == "first_name":
                for elem in json_response:
                    first_name = elem.get("first_name")
                    assert first_name is not None, "Error: User does not have key 'first_name' or its value is None"
                    assert isinstance(first_name, str), f"Error: Key value ({first_name}) is not a string"
            elif key == "last_name":
                for elem in json_response:
                    last_name = elem.get("last_name")
                    assert last_name is not None, "Error: User does not have key 'last_name' or its value is None"
                    assert isinstance(last_name, str), f"Error: Key value ({last_name}) is not a string"
            elif key == "avatar":
                for elem in json_response:
                    avatar = elem.get("avatar")
                    assert avatar is not None, "Error: User does not have key 'avatar' or its value is None"
                    assert isinstance(avatar, str), f"Error: Key value ({avatar}) is not a string"
        else:
            assert len(json_response) == 0, \
                "Expected an empty data but got nothing"

    @staticmethod
    def assert_avatar_image_link_has_status_code_200(response: Response):
        json_response = response.json()['data']
        if len(json_response) > 0:
            for elem in json_response:
                img_link = elem.get("avatar")
                assert requests.get(img_link).status_code == 200, \
                    "Status code avatar img link is not equal 200"
        else:
            assert len(json_response) == 0, \
                "Expected an empty data but got nothing"
