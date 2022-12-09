import pytest
from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import conf
from pathlib import Path
import logging

drv = None
directory = 'report/assets/'


@pytest.fixture(scope='function')
def driver(browser, headless):
    global drv
    Path(directory).mkdir(parents=True, exist_ok=True)
    if browser == 'chrome':
        o = webdriver.ChromeOptions()
        o.headless = headless
        drv = webdriver.Chrome(
            service=ChromeService(ChromeDriverManager().install()), options=o
        )
    else:
        o = webdriver.FirefoxOptions()
        o.headless = headless
        drv = webdriver.Firefox(
            service=FirefoxService(GeckoDriverManager().install()), options=o
        )
    return drv


def pytest_addoption(parser):
    parser.addoption(
        "--browser",
        default="firefox",
        help="define browser: chrome or firefox, --browser=chrome",
    )
    parser.addoption(
        "--headless",
        action="store_true",
        help="headless mode on or off, --headless",
    )


@pytest.fixture(scope='function')
def browser(request):
    return request.config.getoption("--browser")


@pytest.fixture(scope='function')
def headless(request):
    return request.config.getoption("--headless")


@pytest.fixture(scope='function', autouse=True)
def setup(driver):
    logging.info('*** start fixture = setup ***')
    driver.get(conf.URL)
    yield driver
    logging.info('*** end fixture = teardown ***')
    driver.quit()


def pytest_html_report_title(report):
    report.title = "REPORT"


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    pytest_html = item.config.pluginmanager.getplugin("html")
    outcome = yield
    report = outcome.get_result()
    extra = getattr(report, "extra", [])
    if report.when == "call":
        # always add url to report
        extra.append(pytest_html.extras.url(drv.current_url))
        xfail = hasattr(report, "wasxfail")
        if (report.skipped and xfail) or (report.failed and not xfail):
            file_name = report.nodeid.split('::')[-1] + ".png"
            file_name_ = "." + directory + file_name
            file_name_html = 'assets/' + file_name
            drv.get_screenshot_as_file(file_name_)
            if file_name_:
                html = f"<div><img src='{file_name_html}' alt='screenshot'"
                html += "onclick='window.open(this.src)' style='width:400px;'"
                html += " align='right'/></div>"
                extra.append(pytest_html.extras.html(html))
        report.extra = extra
