import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.core.utils import ChromeType
from .pages.locators import *


"""
-----------------------------------------------------
----------------- DRIVER SELECTION ------------------
-----------------------------------------------------
"""
driver = None
headless = True


@pytest.fixture(scope="class")
def d(browser):
    global driver
    global headless
    if browser == "firefox":
        o = webdriver.FirefoxOptions()
        o.headless = headless
        driver = webdriver.Firefox(
            service=FirefoxService(GeckoDriverManager().install()), options=o
        )
    else:
        o = webdriver.ChromeOptions()
        o.headless = headless
        driver = webdriver.Chrome(
            service=ChromeService(ChromeDriverManager().install()), options=o
        )
    return driver


# ------- 2 функции определяют параметр, котрый принимает pytest (browser)
def pytest_addoption(parser):
    parser.addoption(
        "--browser",
        default="chrome",
        help="define browser: chrome or firefox, --firefox",
    )


# ------- browser сами назвали так параметр
# ------- default - что будет запускаться по умолчанию
@pytest.fixture(scope="class")
def browser(request):
    return request.config.getoption("--browser")


"""
-----------------------------------------------------
--------------- Open and quit browser ---------------
-----------------------------------------------------
"""


@pytest.fixture(scope="class", autouse=True)
def g(d):
    print("\n***** start fixture = setup *****\n")
    d.get("https://www.saucedemo.com/")
    yield d
    d.quit()
    print("\n***** end fixture = teardown *****\n")


"""
-----------------------------------------------------
---------------- HTML-Report Title ------------------
-----------------------------------------------------
"""


def pytest_html_report_title(report):
    report.title = "Saucedemo - Let's do it!"


"""
-----------------------------------------------------
---------- Add screenshots to report html -----------
-----------------------------------------------------
"""


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    pytest_html = item.config.pluginmanager.getplugin("html")
    outcome = yield
    report = outcome.get_result()
    extra = getattr(report, "extra", [])
    if report.when == "call":
        extra.append(pytest_html.extras.url(driver.current_url))
        xfail = hasattr(report, "wasxfail")
        if (report.skipped and xfail) or (report.failed and not xfail):
            # test_name = os.environ.get('PYTEST_CURRENT_TEST').split(':')[-1].split(' ')[0]
            screenshot = driver.get_screenshot_as_base64()
            extra.append(pytest_html.extras.image(screenshot, ""))
        report.extra = extra


"""
-----------------------------------------------------
------------ Sign in with valid username ------------
-----------------------------------------------------
"""


@pytest.fixture(
    params=["standard_user", "problem_user", "performance_glitch_user"],
    scope="function",
)
def login_from_list(d, request):
    d.get("https://www.saucedemo.com/")
    d.find_element(*LoginPageLocators.USERNAME_INPUT).send_keys(request.param)
    d.find_element(*LoginPageLocators.PASSWORD_INPUT).send_keys("secret_sauce")
    d.find_element(*LoginPageLocators.LOGIN_BTN).click()


@pytest.fixture(scope="function")
def correct_login(d):
    d.get("https://www.saucedemo.com/")
    d.find_element(*LoginPageLocators.USERNAME_INPUT).send_keys(
        LoginPageLocators.USER_NAME
    )
    d.find_element(*LoginPageLocators.PASSWORD_INPUT).send_keys(
        LoginPageLocators.PASSWORD
    )
    d.find_element(*LoginPageLocators.LOGIN_BTN).click()
    assert (
        d.current_url == "https://www.saucedemo.com/inventory.html"
    ), "____YOU NOT ENTER______"
