from selenium.webdriver.common.by import By
import pytest

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service


def test_kate():
    browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    browser.get('https://www.selenium.dev/downloads')
    browser.find_element(By.XPATH, "//a[contains(@href,'https://github.com/SeleniumHQ/')]").click()
    assert True
    browser.quit()


# from string import printable
#
# print(printable)
