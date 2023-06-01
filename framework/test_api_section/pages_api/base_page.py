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