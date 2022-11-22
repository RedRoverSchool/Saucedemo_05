#!/bin/bash

rm -Rf ./allure-report
poetry run pytest -s -v --alluredir=./allure-report -n auto
allure serve ./allure-report