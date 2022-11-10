from selenium.webdriver.common.by import By
import unittest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

user_name = 'standard_user'
password = 'secret_sauce'

class BaseTest(unittest.TestCase):
    def setUp(self, url=None):
        service = Service(ChromeDriverManager().install())
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument('--window-size=1920,1080')
        self.driver = webdriver.Chrome(service=service, options=chrome_options)
        self.driver.get('https://www.saucedemo.com/')

    def tearDown(self):
        self.driver.quit()

class BasePage(BaseTest):
    def test_sausedemo_tc002_00_01(self):

        #login as an authorithed user
        self.driver.find_element(By.ID, 'user-name').send_keys(user_name)
        self.driver.find_element(By.ID, 'password').send_keys(password)
        self.driver.find_element(By.ID, 'login-button').click()

        #verifying I am on a right link
        self.assertEqual('https://www.saucedemo.com/inventory.html', self.driver.current_url)

        #clicking on a add to cart button
        self.driver.find_element(By.ID, 'add-to-cart-sauce-labs-backpack').click()
        count_item_1 = self.driver.find_element(By.CLASS_NAME, 'shopping_cart_badge').text

        #make sure cart is counting right sum of items every click
        self.assertEqual('1', count_item_1)

        #second_ and third click to add another items to cart
        self.driver.find_element(By.ID, 'add-to-cart-sauce-labs-bike-light').click()
        self.driver.find_element(By.ID, 'add-to-cart-sauce-labs-onesie').click()









if __name__ == '__main__':
    unittest.main()


