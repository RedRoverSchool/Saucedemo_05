<a name="readme-top"></a>
# Saucedemo_05 [![GitHub Actions saucedemo](https://github.com/ivanovajulika/RedRover/actions/workflows/action.yml/badge.svg)](https://github.com/ivanovajulika/RedRover/actions/workflows/action.yml)

<!-- ABOUT THE PROJECT -->
## Python UI testing framework

[![Product Name Screen Shot][product-screenshot]](https://example.com)

<p align="right">(<a href="#readme-top">back to top</a>)</p>

### Built With

This section should list any major frameworks/libraries used to bootstrap your project. Leave any add-ons/plugins for the acknowledgements section. Here are a few examples.

* [![Python][python.org]][https://www.python.org/]
* [![Poetry][python-poetry.org]][https://python-poetry.org/]
* [![Selenium][selenium.dev]][https://www.selenium.dev/]
* [![Pytest][pytest.org]][https://pytest.org/]

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- GETTING STARTED -->
## Getting Started

### Prerequisites

- install python ^3.10
- install poetry

### Installation

_Below is an example of how you can instruct your audience on installing and setting up your app. This template doesn't rely on any external dependencies or services._

1. Install dependencies `$poetry install` 

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- USAGE EXAMPLES -->
## Usage

- Run all tests
`$poetry run pytest`

- Run only specific test
`$poetry run pytest tests/<test_filename>`

- Run only specific function from the test
`$poetry run pytest -k '<part_of_test_fn_name>'`

- Run only smoke tests
`$poetry run pytest -m smoke`

- Run only regression tests
`$poetry run pytest -m regression`

<p align="right">(<a href="#readme-top">back to top</a>)</p>

### Links

target: https://www.saucedemo.com/

Homework 18.11.2022:
- write test cases in python
- play with fixtures by yourself (by yourself or with group)
- add screenshots to the failed pytest-html reports
- setup and configure allure report
- update README and add instructions how to use all this ...
    - https://github.com/othneildrew/Best-README-Template
- next Friday one person from each team will show what they achieved so far