from selenium.webdriver.common.by import By
import allure

user_name = 'standard_user'
password = 'secret_sauce'


class TestSample:
    @allure.epic('Login test')
    @allure.story('ent')
    @allure.suite('regression')
    def test_url(self, driver):
        # login as an authorized user
        driver.find_element(By.ID, 'user-name').send_keys(user_name)
        driver.find_element(By.ID, 'password').send_keys(password)
        driver.find_element(By.ID, 'login-button').click()

        # verifying I am on a right link
        assert 'https://www.saucedemo.com/inventory.html' == driver.current_url, 'different window opened'

    # def test_tc002_00_01(self, driver):
    #     # clicking on add to cart button
    #     self.driver.find_element(By.ID, 'add-to-cart-sauce-labs-backpack').click()
    #     count_item_1 = self.driver.find_element(By.CLASS_NAME, 'shopping_cart_badge').text
    #
    #     # make sure cart is counting right sum of items every click
    #     assert '1' == count_item_1, 'not right amount'
    #
    #     # second_ and third click to add another items to cart
    #     self.driver.find_element(By.ID, 'add-to-cart-sauce-labs-bike-light').click()
    #     self.driver.find_element(By.ID, 'add-to-cart-sauce-labs-onesie').click()
    #
    #     # make sure cart is counting right sum of items every click
    #     count_item_3 = self.driver.find_element(By.CLASS_NAME, 'shopping_cart_badge').text
    #     assert '3' == count_item_3, 'not right amount'
# jhbgjlkh.jnsz
# skkjhkjhns
# hhjhkjk;lljncjknjbnjknb
# kmkjknjkjnjknhjklcd
