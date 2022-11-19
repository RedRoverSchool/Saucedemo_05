from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.edge.options import Options as EdgeOptions
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager
# from selenium.webdriver.safari.options import Options as SafariOptions
# from selenium.webdriver.safari.service import Service as SafariService
import pytest
import conf
import logging

logging.basicConfig(format='%(asctime)s %(name)s %(message)s', level=logging.INFO)
logger = logging.getLogger('QA Envirement')


@pytest.fixture()
def driver(browser):
    if browser == 'chrome':
        chrome_option = ChromeOptions()
        chrome_option.headless = conf.BROWSER_HEADLESS
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=chrome_option
                                  )
        logger.info('Tests are running on Chrome browser')
    elif browser == 'firefox':
        gecko_option = FirefoxOptions()
        gecko_option.headless = conf.BROWSER_HEADLESS
        driver = webdriver.Firefox(
            service=FirefoxService(GeckoDriverManager().install()), options=gecko_option
        )
        logger.info('Tests are running on FireFox browser')
    elif browser == 'safari':
        driver = webdriver.Safari()
        driver.headless = conf.BROWSER_HEADLESS
        logger.info('Tests are running on Safari browser')
    elif browser == 'edge':
        edge_options = EdgeOptions()
        driver = webdriver.Edge(
            service=EdgeService(EdgeChromiumDriverManager().install()),
            options=edge_options,
        )
        logger.info('Tests are running on Edge browser')
    else:
        raise Exception("Wrong browser")

    return driver


@pytest.fixture(autouse=True)
def tear_down(driver, url):
    logger.info('Trying to get url')
    driver.get(url)
    yield
    logger.info('Trying close url')
    driver.quit()



@pytest.fixture()
def browser(request):
    return request.config.getoption("--browser")


@pytest.fixture()
def url(request):
    return request.config.getoption("--url")


def pytest_addoption(parser):
    parser.addoption("--browser",
                     default="chrome"
                     )

    parser.addoption("--url",
                     default="https://www.saucedemo.com/"
                     )


#
# fixture for crossbrowser testing
# @pytest.fixture(params=['chrome', 'safari'], autouse=True)
# def driver(request):
#     if request.param == 'chrome':
#         driver = webdriver.Chrome(
#             service=Service(ChromeDriverManager().install()), options=Options()
#         )
#     else:
#         driver = webdriver.Safari()
#
#     driver.get('https://www.saucedemo.com/')
#     yield driver
#     driver.quit()
