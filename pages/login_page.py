# from .locators import LoginPageLocators
# from .base_page import BasePage
# from .locators import LoginPageLocators
# from selenium.common import NoSuchElementException
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium import webdriver


# class LoginPage(BasePage):
#
#     def should_be_login_page(self):
#         self.should_be_login_link()
#         # self.should_be_login_form()
#         # self.should_be_register_form()
#
#     def should_be_login_link(self):
#         assert 'login' in self.browser.current_url, 'wrong url'

url = "https://www.saucedemo.com/"
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.maximize_window()
driver.get("https://www.saucedemo.com/")

assert driver.current_url == "https://www.saucedemo.com/"

# login
driver.find_element(By.XPATH, "//input[@id='user-name']").send_keys("standard_user")
driver.find_element(By.XPATH, "//input[@id='password']").send_keys("secret_sauce")
driver.find_element(By.XPATH, "//input[@id='login-button']").click()
assert driver.current_url == "https://www.saucedemo.com/inventory.html"

# logout
driver.find_element(By.XPATH, "//button[@id='react-burger-menu-btn']").click()
wait = WebDriverWait(driver, 5)
wait.until(
    EC.visibility_of_element_located((By.XPATH, "//a[contains(.,'Logout')]"))
).click()
assert driver.current_url == "https://www.saucedemo.com/"

driver.close()
