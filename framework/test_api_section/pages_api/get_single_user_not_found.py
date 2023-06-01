from requests import Response


class SingleUserNotFound:
    @staticmethod
    def assert_get_single_user_not_found_has_empty_json(response: Response):
        assert not response.json(), "Error: JSON is not empty"
