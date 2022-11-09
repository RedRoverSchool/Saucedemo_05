from typing import List
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class BasePage:
    def __init__(self, browser, url):
        self.browser = browser
        self.url = url
        self.wait = WebDriverWait(self.browser, 5, 0.3)

    def open(self):
        self.browser.get(self.url)

    def element_is_visible(self, locator) -> WebElement:
        return self.wait.until(EC.visibility_of_element_located(locator))

    def elements_are_visible(self, locator) -> List[WebElement]:
        return self.wait.until(EC.visibility_of_all_elements_located(locator))

    def element_is_present(self, locator) -> WebElement:
        return self.wait.until(EC.presence_of_element_located(locator))

    def elements_are_present(self, locator) -> List[WebElement]:
        return self.wait.until(EC.presence_of_all_elements_located(locator))

    def element_is_not_visible(self, locator) -> WebElement:
        return self.wait.until(EC.invisibility_of_element_located(locator))

    def element_is_clickable(self, locator) -> WebElement:
        return self.wait.until(EC.element_to_be_clickable(locator))

    def go_to_element(self, element):
        self.browser.execute_script("argument[0].scrollIntoView;", element)
