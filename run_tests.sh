#!/bin/bash

rm -Rf ./allure-report
poetry run pytest -s -v --alluredir=./allure-report
allure serve ./allure-report