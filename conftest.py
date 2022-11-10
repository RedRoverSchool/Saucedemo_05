import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

options = Options()
options.add_argument("start-maximized")


@pytest.fixture(scope="class")
def driver_init(request):
    chrome_driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    request.cls.driver = chrome_driver
    yield
    chrome_driver.quit()
