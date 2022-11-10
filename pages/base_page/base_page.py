from typing import List

from selenium.common import TimeoutException
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.select import Select


class BasePage:
    def __init__(self, browser: WebDriver, url: str):
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

    def move_to_element(self, locator):
        element = self.element_is_visible(locator)
        ActionChains(self.browser).move_to_element(element).perform()
        return element

    def select_dropdown_option(self, locator, option_text):
        dropdown = self.browser.element_is_clickable(locator)
        for option in dropdown.find_elements_by_tag_name("option"):
            if option.text == option_text:
                option.click()
                break

    def get_page_title(self):
        return self.browser.title

    def back(self):
        self.browser.back()

    def forward(self):
        self.browser.forward()

    def wait(self, seconds):
        self.browser.implicitly_wait(seconds)

    def get_element_text(self, locator):
        element = self.browser.find_element(locator)
        return element.text

    def get_attribute(self, locator, name):
        element = self.browser.find_element(locator)
        return element.get_attribute(name)

    def js_execute(self, js):
        return self.browser.execute_script(js)

    def js_scroll_top(self):
        js = "window.scrollTo(0,0)"
        self.browser.execute_script(js)

    def js_scroll_bottom(self):
        js = "window.scrollTo(0,document.body.scrollHeight)"
        self.browser.execute_script(js)

    def select_by_index(self, locator, index):
        element = self.browser.find_element(locator)
        Select(element).select_by_index(index)

    def select_by_value(self, locator, value):
        element = self.browser.find_element(locator)
        Select(element).select_by_value(value)

    def select_by_text(self, locator, text):
        element = self.browser.find_element(locator)
        Select(element).select_by_value(text)

    def is_text_in_element(self, locator, text):
        try:
            result = self.wait.until(EC.text_to_be_present_in_element(locator, text))
        except TimeoutException:
            return False
        else:
            return result

    def is_text_in_value(self, locator, value):
        try:
            result = self.wait.until(EC.text_to_be_present_in_element_value(locator, value))
        except TimeoutException:
            return False
        else:
            return result

    def is_title(self, title):
        result = self.wait.until(EC.title_is(title))
        return result

    def is_title_contains(self, title):
        result = self.wait.until(EC.title_contains(title))
        return result

    def is_selected(self, locator):
        result = self.wait.until(EC.element_located_to_be_selected(locator))
        return result

    def is_selected_be(self, locator, selected=True):
        result = self.wait.until(EC.element_located_selection_state_to_be(locator, selected))
        return result

    def is_alert_present(self):
        result = self.wait.until(EC.alert_is_present())
        return result

    def click_alert(self):
        alert = self.browser.switch_to.alert
        alert.accept()

    def alert_text(self):
        alert = self.browser.switch_to.alert
        return alert.text()

