import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture(scope='class')
def set_chrome_options():
    options = Options()
    # options.add_argument("--headless")
    # options.add_argument("--no-sandbox")
    # options.add_argument("--disable-dev-shm-usage")
    # options.add_argument("--disable-notifications")
    # options.add_argument("--disable-setuid-sandbox")
    return options


@pytest.fixture()
def driver(set_chrome_options):
    options = set_chrome_options
    driver = webdriver.Chrome(
        service=Service(ChromeDriverManager().install()), options=options
    )
    return driver

@pytest.fixture(autouse=True)
def c(driver):
    driver.get('https://www.saucedemo.com/')
    yield
    driver.quit()