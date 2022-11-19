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




@pytest.fixture()
def driver(browser):
    if browser == 'chrome':
        chrome_option = ChromeOptions()
        chrome_option.headless = conf.BROWSER_HEADLESS
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=chrome_option
                                  )
    elif browser == 'firefox':
        gecko_option = FirefoxOptions()
        gecko_option.headless = conf.BROWSER_HEADLESS
        driver = webdriver.Firefox(
            service=FirefoxService(GeckoDriverManager().install()), options=gecko_option
        )
    elif browser == 'safari':
        driver = webdriver.Safari()
        driver.headless = conf.BROWSER_HEADLESS

    elif browser == 'edge':
        edge_options = EdgeOptions()
        driver = webdriver.Edge(
            service=EdgeService(EdgeChromiumDriverManager().install()),
            options=edge_options,
        )
    else:
        raise Exception("Wrong browser")

    return driver


@pytest.fixture(autouse=True)
def tear_down(driver, url):
    print('\n*** start fixture = setup ***\n')
    driver.get(url)
    yield
    driver.quit()
    print('\n*** end fixture = teardown ***\n')


@pytest.fixture()
def browser(request):
    return request.config.getoption("--browser")

@pytest.fixture()
def url(request):
    return request.config.getoption("--url")


def pytest_addoption(parser):
    parser.addoption("--browser")
    parser.addoption("--url")

    #     default="'https://www.saucedemo.com/'",
    #     help="define url: https://www.saucedemo.com/"
    # )
#

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
