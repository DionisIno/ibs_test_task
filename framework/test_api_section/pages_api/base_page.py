import allure
from framework.generator.generator import generated_person


class BasePage:

    @staticmethod
    def prepare_creating_date(name=None, job=None):
        """This method get registration date"""
        if name is None:
            return {
                "job": job
            }
        elif job is None:
            return {
                "name": name,
            }
        else:
            return {
                "name": name,
                "job": job
            }

    @allure.description("This method get registration date")
    def prepare_creating_registration_data(self, email=None, password=None):
        if email is None:
            return {
                "password": password
            }
        elif password is None:
            return {
                "password": email
            }
        else:
            return {
                "email": email,
                "password": password
            }
