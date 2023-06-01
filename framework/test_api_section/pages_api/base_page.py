import allure
from framework.generator.generator import generated_person


class BasePage:

    @allure.description("This method get registration date")
    def prepare_creating_date(self, name=None, job=None):
        person = next(generated_person())
        if name is None:
            name = person.name
        if job is None:
            job = person.job
        return {
            "name": name,
            "job": job
        }

    @allure.description("This method gets the registration date of the job only")
    def prepare_creating_date_job_only(self, job=None):
        person = next(generated_person())
        if job is None:
            job = person.job
        return {
            "job": job
        }

    @allure.description("This method gets the registration date of the name only")
    def prepare_creating_date_name_only(self, name=None):
        person = next(generated_person())
        if name is None:
            name = person.name
        return {
            "name": name
        }

    @allure.description("This method get registration date")
    def prepare_creating_registration_data(self, email=None, password=None):
        person = next(generated_person())
        if email is None:
            email = person.email
        if password is None:
            password = person.password
        return {
            "email": email,
            "password": password
        }

    @allure.description("This method get email")
    def prepare_creating_email(self, email=None):
        person = next(generated_person())
        if email is None:
            email = person.email
        return {
            "email": email,
        }

    @allure.description("This method get password")
    def prepare_creating_password(self, password=None):
        person = next(generated_person())
        if password is None:
            password = person.password
        return {
            "password": password
        }
