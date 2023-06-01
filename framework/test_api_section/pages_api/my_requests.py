import requests
import allure

BASE_URL = "https://reqres.in"


class MyRequests:

    @staticmethod
    def get(url: str, data: dict = None, headers: dict = None, cookies: dict = None):
        with allure.step(f"GET requests to URL '{url}'"):
            response = MyRequests._send(url, data, headers, cookies, "GET")
            return response

    @staticmethod
    def post(url: str, data: dict = None, headers: dict = None, cookies: dict = None):
        with allure.step(f"POST request to URL '{url}'"):
            response = MyRequests._send(url, data, headers, cookies, "POST")
            return response

    @staticmethod
    def put(url: str, data: dict = None, headers: dict = None, cookies: dict = None):
        with allure.step(f"PUT request to URL '{url}'"):
            response = MyRequests._send(url, data, headers, cookies, "PUT")
            return response

    @staticmethod
    def patch(url: str, data: dict = None, headers: dict = None, cookies: dict = None):
        with allure.step(f"PATCH request to URL '{url}'"):
            response = MyRequests._send(url, data, headers, cookies, "PATCH")
            return response

    @staticmethod
    def delete(url: str, data: dict = None, headers: dict = None, cookies: dict = None):
        with allure.step(f"DELETE request to URL '{url}'"):
            response = MyRequests._send(url, data, headers, cookies, "DELETE")
            return response

    @staticmethod
    def _send(url: str, data: dict, headers: dict, cookies: dict, method: str):
        url = f"""{BASE_URL}{url}"""

        if headers is None:
            headers = {}
        if cookies is None:
            cookies = {}

        if method == "GET":
            response = requests.get(url, params=data, headers=headers, cookies=cookies)
        elif method == "POST":
            response = requests.post(url, data=data, headers=headers, cookies=cookies)
        elif method == "PUT":
            response = requests.put(url, data=data, headers=headers, cookies=cookies)
        elif method == "PATCH":
            response = requests.patch(url, data=data, headers=headers, cookies=cookies)
        elif method == "DELETE":
            response = requests.delete(url, data=data, headers=headers, cookies=cookies)
        else:
            raise Exception(f"""Bad method '{method}' was received""")
        return response
