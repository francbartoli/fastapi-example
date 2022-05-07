# fastapi-example

[![Tests](https://github.com/Progyan1997/fastapi-example/actions/workflows/tests.yml/badge.svg)](https://github.com/Progyan1997/fastapi-example/actions/workflows/tests.yml)

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![FastAPI](https://img.shields.io/badge/FastAPI-005571?style=for-the-badge&logo=fastapi)
![Swagger](https://img.shields.io/badge/-Swagger-%23Clojure?style=for-the-badge&logo=swagger&logoColor=white)
![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg?style=for-the-badge)

## Description

_Example Application Interface using FastAPI framework in Python 3_

This example showcases Repository Pattern in Hexagonal Architecture _(also known as Clean Architecture)_. Here we have two Entities - Books and Authors, whose relationships have been exploited to create CRUD endpoint in REST under OpenAPI standard.

## Installation

- Install all the project dependency using [Pipenv](pipenv.pypa.io):

  ```sh
  $ pipenv install --dev
  ```

- Run the application from command prompt:
  ```sh
  $ pipenv run uvicorn main:app --reload
  ```
- Open `localhost:8000/docs` for API Documentation

## Testing

For Testing, `unittest` module is used for Test Suite and Assertion, whereas `pytest` is being used for Test Runner and Coverage Reporter.

- Run the following command to initiate test:
  ```sh
  $ pipenv run pytest
  ```
- To include Coverage Reporting as well:
  ```sh
  $ pipenv run pytest --cov-report xml --cov .
  ```

## License

&copy; MIT License
