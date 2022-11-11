import time
from typing import List

from selenium.common import TimeoutException
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By


class BasePage:
    def __init__(self, browser: WebDriver, url: str):
        self.browser = browser
        self.url = url
        self.wait = WebDriverWait(self.browser, 5, 0.3)

    def open(self):
        self.browser.get(self.url)

    def navigate_to(self, url: str):
        self.browser.get(url)

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
            "arguments[0].style.border='3px solid red'", element
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
        dropdown = self.element_is_clickable(locator)
        for option in dropdown.find_elements(By.TAG_NAME, "option"):
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
            result = self.wait.until(
                EC.text_to_be_present_in_element_value(locator, value)
            )
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
        result = self.wait.until(
            EC.element_located_selection_state_to_be(locator, selected)
        )
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

    def refresh_page(self):
        self.browser.refresh()

    def scroll_down(self, offset=0):
        if offset:
            self.browser.execute_script("window.scrollTo(0, {0});".format(offset))
        else:
            self.browser.execute_script(
                "window.scrollTo(0, document.body.scrollHeight);"
            )

    def scroll_up(self, offset=0):
        if offset:
            self.browser.execute_script("window.scrollTo(0, -{0});".format(offset))
        else:
            self.browser.execute_script(
                "window.scrollTo(0, -document.body.scrollHeight);"
            )

    def switch_to_iframe(self, iframe):
        self.browser.switch_to.frame(iframe)

    def switch_out_iframe(self):
        self.browser.switch_to.default_content()

    def get_current_url(self):
        return self.browser.current_url

    def get_page_source(self):
        source = ""
        try:
            source = self.browser.page_source
        except:
            return None
        return source

    def check_js_errors(self, ignore_list=None):
        ignore_list = ignore_list or []
        logs = self.browser.get_log("browser")
        for log_message in logs:
            if log_message["level"] != "WARNING":
                ignore = False
                for issue in ignore_list:
                    if issue in log_message["message"]:
                        ignore = True
                        break
                assert ignore, f'JS error "{log_message}" on the page!'

    # def wait_page_loaded(
    #     self,
    #     timeout=60,
    #     check_js_complete=True,
    #     check_page_changes=False,
    #     check_images=False,
    #     wait_for_element=None,
    #     wait_element_to_disappear="",
    #     sleep_time=2,
    # ):
    #     page_loaded = False
    #     double_check = False
    #     k = 0
    #     if sleep_time:
    #         time.sleep(sleep_time)
    #     source = ""
    #     try:
    #         source = self.browser.page_source
    #     except:
    #         pass
    #     # Wait until page loaded (and scroll it, to make sure all objects will be loaded):
    #     while not page_loaded:
    #         time.sleep(0.5)
    #         k += 1
    #         if check_js_complete:
    #             # Scroll down and wait when page will be loaded:
    #             try:
    #                 self.browser.execute_script(
    #                     "window.scrollTo(0, document.body.scrollHeight);"
    #                 )
    #                 page_loaded = self.browser.execute_script(
    #                     "return document.readyState == 'complete';"
    #                 )
    #             except Exception as e:
    #                 pass
    #         if page_loaded and check_page_changes:
    #             # Check if the page source was changed
    #             new_source = ""
    #             try:
    #                 new_source = self.browser.page_source
    #             except:
    #                 pass
    #             page_loaded = new_source == source
    #             source = new_source
    #         # Wait when some element will disappear:
    #         if page_loaded and wait_for_xpath_to_disappear:
    #             bad_element = None
    #             try:
    #                 bad_element = WebDriverWait(self.browser, 0.1).until(
    #                     EC.presence_of_element_located((wait_element_to_disappear))
    #                 )
    #             except:
    #                 pass  # Ignore timeout errors
    #             page_loaded = not bad_element
    #         if page_loaded and wait_for_element:
    #             try:
    #                 page_loaded = WebDriverWait(self.browser, 0.1).until(
    #                     EC.element_to_be_clickable(wait_for_element._locator)
    #                 )
    #             except:
    #                 pass  # Ignore timeout errors
    #         assert k < timeout, "The page loaded more than {0} seconds!".format(timeout)
    #         if page_loaded and not double_check:
    #             page_loaded = False
    #             double_check = True
    #     self.browser.execute_script("window.scrollTo(document.body.scrollHeight, 0);")
