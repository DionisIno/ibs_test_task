import requests
from requests import Response

from framework.test_api_section.api_expected_result.expected_result import ExpectedRequestsResult as er, SupportData
from framework.test_api_section.pages_api.assertions import Assertion


class SingleUser:

    @staticmethod
    def assert_check_correct_id(response: Response, key: str, elem):
        Assertion.assert_status_code(response, er.STATUS_CODE_OK)
        Assertion.assert_response_have_be_json(response)
        if len(response.json()) > 0:
            json_response = response.json()["data"]
            user_id = json_response.get(key)
            assert user_id is not None, "Error: User does not have key 'id' or its value is None"
            assert isinstance(user_id, int), f"Error: Key value ({user_id}) is not a number"
            assert user_id == elem, \
                f"The current id does not match the expected id. Expected {elem}, but go {user_id}"
        else:
            assert isinstance(response.json()["data"], dict), \
                f"Expected an empty list but got {type(response.json()['data'])}"

    @staticmethod
    def assert_response_has_key(response: Response, value: str):
        Assertion.assert_status_code(response, er.STATUS_CODE_OK)
        Assertion.assert_response_have_be_json(response)
        if len(response.json()) > 0:
            json_response = response.json()["data"]
            value = json_response.get(value)
            assert value is not None, f"Error: User does not have key '{value}' or its value is None"
            assert isinstance(value, str), f"Error: Key value ({value}) is not a string"
        else:
            assert isinstance(response.json()["data"], dict), \
                f"Expected an empty list but got {type(response.json()['data'])}"

    @staticmethod
    def assert_single_user_avatar_image_link_has_status_code_200(response: Response):
        Assertion.assert_status_code(response, er.STATUS_CODE_OK)
        Assertion.assert_response_have_be_json(response)
        if len(response.json()) > 0:
            json_response = response.json()["data"]
            img_link = json_response.get("avatar")
            assert requests.get(img_link).status_code == er.STATUS_CODE_OK, \
                f"Status code avatar img link is not equal {er.STATUS_CODE_OK}"

    @staticmethod
    def assert_single_user_support_have_correct_url(response: Response):
        Assertion.assert_status_code(response, er.STATUS_CODE_OK)
        Assertion.assert_response_have_be_json(response)
        actual_support_email = response.json()['support']['url']
        expected_support_email = SupportData.url
        assert actual_support_email == expected_support_email, \
            f"Actual support email is not equal {expected_support_email}"

    @staticmethod
    def assert_single_user_support_have_correct_text(response: Response):
        Assertion.assert_status_code(response, er.STATUS_CODE_OK)
        Assertion.assert_response_have_be_json(response)
        actual_support_text = response.json()['support']['text']
        expected_support_text = SupportData.message
        assert actual_support_text == expected_support_text, \
            f"Actual support email is not equal {expected_support_text}"
