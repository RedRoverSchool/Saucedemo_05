import pytest
from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.edge.options import Options as EdgeOptions
from selenium.webdriver.edge.service import Service as EdgeService
from selenium.webdriver.safari.options import Options as SafariOptions
from selenium.webdriver.safari.service import Service as SafariService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.opera import OperaDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from conf.browser_config import browser_config


@pytest.fixture
def set_browser_options():
    browser_name, headless, proxy_server, user_agent = (
        browser_config["browser"],
        browser_config["headless"],
        browser_config["proxy_server"],
        browser_config["user_agent"],
    )
    match browser_name:
        case "Firefox":
            options = FirefoxOptions()
        case "Edge":
            options = EdgeOptions()
        case "Safari":
            options = SafariOptions()
        # case "Opera":
        #     options = ChromeOptions()
        #     options.add_argument('allow-elevated-browser')
        #     options.add_argument('disable-infobars')
        #     options.add_argument('--no-sandbox')
        #     options.add_argument('--disable-dev-shm-usage')
        #     options.add_argument('start-maximized')
        #     options.add_experimental_option('w3c', True)
        case _:
            options = ChromeOptions()

    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    # options.add_argument("no-first-run")
    # options.add_argument("--disable-gpu")
    # options.add_argument("--log-level-3")
    # options.add_argument("no-default-browser-check")
    # options.add_argument("--disable-infobars")
    # options.add_argument("--disable-notifications")
    # options.add_argument("--disable-blink-features")
    # options.add_argument("--disable-setuid-sandbox")
    # options.add_argument("--disable-blink-features=AutomationControlled")
    # options.add_experimental_option("useAutomationExtension", False)
    if headless:
        options.add_argument("--headless")
        options.add_experimental_option(
            "prefs", {"profile.managed_default_content_settings.images": 2}
        )
    if proxy_server:
        options.add_argument(f"--proxy-server={proxy_server}")
    if user_agent:
        options.add_argument(f"user-agent={user_agent}")
    return options


@pytest.fixture(scope="function")
def browser(set_browser_options):
    browser_name = browser_config["browser"]
    options = set_browser_options
    match browser_name:
        case "Firefox":
            browser: WebDriver = webdriver.Firefox(
                service=FirefoxService(GeckoDriverManager().install()), options=options
            )
        # case "Opera":
        #     browser: WebDriver = webdriver.Chrome(
        #         service=ChromeService(OperaDriverManager().install()), options=options
        #     )
        case "Safari":
            browser: WebDriver = webdriver.Safari(
                service=SafariService(), options=options
            )
        case "Edge":
            browser: WebDriver = webdriver.Edge(
                service=EdgeService(EdgeChromiumDriverManager().install()),
                options=options,
            )
        case _:  # Chrome is default browser
            browser: WebDriver = webdriver.Chrome(
                service=ChromeService(ChromeDriverManager().install()), options=options
            )

    # browser.maximize_window()
    yield browser
    browser.quit()
