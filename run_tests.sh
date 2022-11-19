#!/bin/bash

rm -Rf ./allure-report
poetry run pytest -s -v --browser=chrome --url=https://www.saucedemo.com/ --alluredir=./allure-report
allure serve ./allure-report