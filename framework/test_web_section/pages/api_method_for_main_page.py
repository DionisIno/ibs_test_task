import json

import requests


class GetApiMethod:
    @staticmethod
    def get_list_user(url):
        response = requests.get(url)
        get_status_code = response.status_code

        get_text = response.text
        return get_status_code, get_text

