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
