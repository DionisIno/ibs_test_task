# Description

https://reqres.in/ - Открытое API 
 
Необходимо на Python + PyTest написать тесты, где реализовать следующие пункты: 
1) Написать позитивные и негативные API тесты, которые представлены на главной странице как образец 
2) Написать WEB тесты с главной страницы + добавить проверку, что при нажатии на кнопку отправки образца запроса, получаемый результат (тело ответа и статус код) такой же как и через API запрос 
3) Все тесты параметризировать и добавить фикстуры 
4) Добавить возможность масштабировать проект (К примеру: если в WEB - добавится новая страница, а в API добавится новая версия API. То в таком случае добавляется новый класс и не нарушается текущая реализация)

![Python Version](https://img.shields.io/badge/python-3.11-blue)
[![dependency - selenium](https://img.shields.io/badge/dependency-selenium-blue?logo=selenium&logoColor=white)](https://pypi.org/project/selenium)
[![dependency - pytest](https://img.shields.io/badge/dependency-pytest-blue?logo=pytest&logoColor=white)](https://pypi.org/project/pytest)
[![dependency - Faker](https://img.shields.io/badge/dependency-Faker-blue)](https://pypi.org/project/Faker)
[![dependency - allure-pytest](https://img.shields.io/badge/dependency-allure--pytest-blue?logo=qameta&logoColor=white)](https://pypi.org/project/allure-pytest)
[![dependency - requests](https://img.shields.io/badge/dependency-requests-blue?logo=qameta&logoColor=white)](https://pypi.org/project/requests/)

## How to work with this repository:

- Clone repository to your machine.

- Navigate to the root folder of the project.
- Create a virtual environment.
- Run command **pip install -r requirements.txt**
- After, execute **pytest -s -v** to run tests.