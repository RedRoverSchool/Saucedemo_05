import pytest
from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import conf


@pytest.fixture(scope='class', autouse=True)
def browser(request):
    browser = request.config.getoption("--browser")
    if browser == 'chrome':
        o = webdriver.ChromeOptions()
        o.headless = conf.BROWSER_HEADLESS
        driver = webdriver.Chrome(
            service=ChromeService(ChromeDriverManager().install()), options=o
        )
        print('\n*** start fixture = setup ***\n')
        driver.get(conf.URL)
        yield driver
        driver.quit()
        print('\n*** end fixture = teardown ***\n')
    else:
        o = webdriver.FirefoxOptions()
        o.headless = conf.BROWSER_HEADLESS
        driver = webdriver.Firefox(
            service=FirefoxService(GeckoDriverManager().install()), options=o
        )
        print('\n*** start fixture = setup ***\n')
        driver.get(conf.URL)
        yield driver
        driver.quit()
        print('\n*** end fixture = teardown ***\n')
    return driver


def pytest_addoption(parser):
    parser.addoption(
        "--browser",
        default="firefox",
        help="define browser: chrome or firefox, --browser=chrome",
    )




def pytest_html_report_title(report):
    report.title = "REPORT"
