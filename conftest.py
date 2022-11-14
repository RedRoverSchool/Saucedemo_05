import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture
def set_chrome_options():
    chrome_options = Options()
    # options.add_argument("--headless")
    return chrome_options


@pytest.fixture
def driver_init(set_chrome_options):
    options = set_chrome_options
    driver = webdriver.Chrome(
        service=Service(ChromeDriverManager().install()), options=options
    )
    return driver


@pytest.fixture(autouse=True)
def driver(driver_init):
    driver_init.get('https://www.saucedemo.com/')
    yield driver_init
    driver_init.quit()
