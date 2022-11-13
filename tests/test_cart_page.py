from selenium.webdriver.common.by import By
from selenium import webdriver
import conf


url = "https://www.saucedemo.com/"


def test_add_to_cart(browser: webdriver.Chrome):
    browser.get(url)
    assert browser.current_url == conf.URL

    # login
    browser.find_element(By.XPATH, "//input[@id='user-name']").send_keys(
        "standard_user"
    )

    browser.find_element(By.XPATH, "//input[@id='password']").send_keys("secret_sauce")

    browser.find_element(By.XPATH, "//input[@id='login-button']").click()
    assert browser.current_url == "https://www.saucedemo.com/inventory.html"

    add_to_cart_button = browser.find_element(
        By.CSS_SELECTOR, "#add-to-cart-sauce-labs-backpack"
    ).text

    assert add_to_cart_button == "ADD TO CART"
    browser.find_element(By.CSS_SELECTOR, "#add-to-cart-sauce-labs-backpack").click()

    shopping_cart = browser.find_element(By.CSS_SELECTOR, ".shopping_cart_link").text
    assert shopping_cart == "1"

    remove_from_cart_button = browser.find_element(
        By.CSS_SELECTOR, "#remove-sauce-labs-backpack"
    ).text
    assert remove_from_cart_button == "REMOVE"

    browser.find_element(By.CSS_SELECTOR, "#remove-sauce-labs-backpack").click()

    shopping_cart = browser.find_element(By.CSS_SELECTOR, ".shopping_cart_link").text
    assert shopping_cart == ""

    browser.quit()


if __name__ == "__main__":
    browser = init_browser()
    test_add_to_cart(browser)
