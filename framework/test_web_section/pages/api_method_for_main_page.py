import json

import requests


class GetApiMethod:
    @staticmethod
    def get_method(url):
        response = requests.get(url)
        get_status_code = response.status_code
        get_text = response.text
        return get_status_code, get_text

    @staticmethod
    def post_method(url, data):
        response = requests.post(url, data=data)
        get_status_code = response.status_code
        get_text = response.text
        return get_status_code, get_text

    @staticmethod
    def put_method(url, data):
        response = requests.put(url, data=data)
        get_status_code = response.status_code
        get_text = response.text
        return get_status_code, get_text

