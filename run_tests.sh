#!/bin/bash

rm -Rf ./allure-report
poetry run pytest --alluredir=allure-results -n auto --screenshot=on
allure serve ./allure-report