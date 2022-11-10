from typing import List

from selenium.webdriver import ActionChains
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

    def go_to_element_with_locator(self, locator):
        element = self.browser.find_element(locator)
        self.browser.execute_script("argument[0].scrollIntoView;", element)

    def send_keys_to_input(self, locator, keys: str):
        input_field = self.element_is_present(locator)
        input_field.clear()
        input_field.send_keys(keys)

    def click_button(self, locator):
        button = self.element_is_clickable(locator)
        button.click()

    def random_wait(self, t_min, t_max):
        import time
        import random

        random_time = random.randrange(t_min, t_max)
        time.sleep(random_time)

    def pick_random_list_item(self, we_list: List[WebElement]) -> WebElement:
        import random

        random_index = random.randint(0, len(we_list) - 1)
        return we_list[random_index]

    def highlight_web_element(self, locator) -> None:
        element = self.element_is_visible(locator)
        self.browser.execute_script(
            "arguments[0].style.border='3px ridge #33ffff'", element
        )

    def double_click(self, locator) -> WebElement:
        element = self.element_is_clickable(locator)
        ActionChains(self.browser).double_click(on_element=element).perform()
        return element

    def context_click(self, locator) -> WebElement:
        element = self.element_is_clickable(locator)
        ActionChains(self.browser).context_click(on_element=element)
        return element

    def click_and_hold(self, locator) -> WebElement:
        element = self.element_is_clickable(locator)
        ActionChains(self.browser).click_and_hold(on_element=element)
        return element

    def hover(self, locator):
        element = self.element_is_visible(locator)
        ActionChains(self.browser).move_to_element(element).perform()
        return element
