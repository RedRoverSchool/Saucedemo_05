#!/bin/bash

rm -Rf ./allure-report
poetry run pytest -s -v --browser=safari --alluredir=./allure-report
allure serve ./allure-report