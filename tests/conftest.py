import pytest
from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import conf


@pytest.fixture(scope="class")
def d(browser):

    if browser == "chrome":
        options = webdriver.ChromeOptions()
        options.headless = conf.BROWSER_HEADLESS
        driver = webdriver.Chrome(
            service=ChromeService(ChromeDriverManager().install()), options=options
        )

    elif browser == "firefox":
        options = webdriver.FirefoxOptions()
        options.headless = conf.BROWSER_HEADLESS
        driver = webdriver.Firefox(
            service=FirefoxService(GeckoDriverManager().install()), options=options
        )

    return driver


def pytest_addoption(parser):
    parser.addoption(
        "--browser",
        default="chrome",
        help="define browser: chrome or firefox, --browser=chrome",
    )


@pytest.fixture(scope="class")
def browser(request):
    return request.config.getoption("--browser")


@pytest.fixture(scope="class", autouse=True)
def g(d):
    print("\n*** start fixture = setup ***\n")
    d.get(conf.URL)
    yield d
    d.quit()
    print("\n*** end fixture = teardown ***\n")


def pytest_html_report_title(report):
    report.title = "Saucedemo report"
