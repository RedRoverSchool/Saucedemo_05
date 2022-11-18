import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture(params=['chrome', 'safari'], autouse=True)
def driver(request):
    if request.param == 'chrome':
        driver = webdriver.Chrome(
            service=Service(ChromeDriverManager().install()), options=Options()
        )
    else:
        driver = webdriver.Safari()

    driver.get('https://www.saucedemo.com/')
    yield driver
    driver.quit()

