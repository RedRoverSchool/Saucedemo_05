from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium import webdriver
from pprint import pprint
from collections import OrderedDict


def browser():
    """Функция  создания драйвера"""
    browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    browser.maximize_window()
    return browser

def get_all_product(browser: webdriver.Chrome):
    """Функция  получения данных о товарах со страницы сайта"""
    browser.get("https://www.saucedemo.com/")

    assert browser.current_url == "https://www.saucedemo.com/"

    # login
    browser.find_element(By.XPATH, "//input[@id='user-name']").send_keys("standard_user")
    browser.find_element(By.XPATH, "//input[@id='password']").send_keys("secret_sauce")
    browser.find_element(By.XPATH, "//input[@id='login-button']").click()
    assert browser.current_url == "https://www.saucedemo.com/inventory.html"

    inventory_list = browser.find_elements(By.CSS_SELECTOR, ".inventory_item")

    # inventory_item_name = browser.find_element(By.CSS_SELECTOR, '.inventory_item_name').text    # Получение названия товара
    # inventory_item_desc = browser.find_element(By.CSS_SELECTOR, ".inventory_item_desc").text    # Получение описания товара
    # inventory_item_price = browser.find_element(By.CSS_SELECTOR, '.inventory_item_price').text  # Получение цены товара
    # link_img_product = browser.find_element(By.CSS_SELECTOR, ".inventory_item_img .inventory_item_img").get_attribute('src') # Получение линка на товара

    list_inventory = []  # Пустой массив для сохранения всех продуктов

    for product in inventory_list:             # смотрим по одному элементу
        inventory_item_name = product.find_element(By.CSS_SELECTOR, '.inventory_item_name').text
        inventory_item_price = product.find_element(By.CSS_SELECTOR, '.inventory_item_price').text
        inventory_item_desc = product.find_element(By.CSS_SELECTOR, ".inventory_item_desc").text

        list_inventory.append({
            '1_product': inventory_item_name,
            '2_price': inventory_item_price,
            '3_description': inventory_item_desc,
        })


def sort_price_low_to_high(browser: webdriver.Chrome):

    browser.get("https://www.saucedemo.com/")
    assert browser.current_url == "https://www.saucedemo.com/"

    browser.find_element(By.XPATH, "//input[@id='user-name']").send_keys("standard_user")
    browser.find_element(By.XPATH, "//input[@id='password']").send_keys("secret_sauce")
    browser.find_element(By.XPATH, "//input[@id='login-button']").click()
    assert browser.current_url == "https://www.saucedemo.com/inventory.html"

    browser.find_element(By.CSS_SELECTOR, '.product_sort_container :nth-child(3)').click()

    inventory_list = browser.find_elements(By.CSS_SELECTOR, ".inventory_item")
    list_inventory = []  # Пустой массив для сохранения всех продуктов

    for product in inventory_list:  # смотрим по одному элементу
        inventory_item_name = product.find_element(By.CSS_SELECTOR, '.inventory_item_name').text
        inventory_item_price = product.find_element(By.CSS_SELECTOR, '.inventory_item_price').text

        list_inventory.append(inventory_item_price, )

    price_list = []
    for i in range(1, len(list_inventory)):
        price_el = float(list_inventory[i].replace('$', '', 1))

        price_list.append(price_el, )
    # print(price_list)

    for i in range(0, len(price_list) - 1):
        assert (price_list[i] <= price_list[i + 1])


    browser.quit()
    return price_listpytest --fixtures


if __name__ == '__main__':
    br = browser()
    product = get_all_product(br)
    pprint(product)

    price_sorted = sort_price_low_to_high(br)
    print(price_sorted)
