from requests import Response


class CreatePost:
    @staticmethod
    def assert_check_job_and_name_in_response(response: Response, data):
        json_value = response.json()
        actual_name = json_value["name"]
        actual_job = json_value["job"]
        expected_name = data["name"]
        expected_job = data["job"]
        assert actual_job == expected_job, f"Actual name is not equal {expected_job}"
        assert actual_name == expected_name, f"Actual name is not equal {expected_name}"