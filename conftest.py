import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from conf.browser_config import browser_config


# from selenium.webdriver.firefox.options import Options as FirefoxOptions
# from selenium.webdriver.firefox.service import Service as FirefoxService
# from webdriver_manager.firefox import GeckoDriverManager


@pytest.fixture
def set_chrome_options():
    headless = browser_config["headless"]
    proxy_server = browser_config["proxy_server"]
    user_agent = browser_config["user_agent"]

    options = ChromeOptions()
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("no-first-run")
    options.add_argument("--disable-gpu")
    options.add_argument("--log-level-3")
    options.add_argument("no-default-browser-check")
    options.add_argument("--disable-infobars")
    options.add_argument("--disable-notifications")
    options.add_argument("--disable-blink-features")
    options.add_argument("--disable-setuid-sandbox")
    options.add_argument("--disable-blink-features=AutomationControlled")
    options.add_experimental_option("useAutomationExtension", False)
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
def browser(set_chrome_options):
    options = set_chrome_options
    browser = webdriver.Chrome(
        service=ChromeService(ChromeDriverManager().install()), options=options
    )
    browser.maximize_window()
    yield browser
    browser.quit()
