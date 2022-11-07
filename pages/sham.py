import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from pprint import pprint

def browser():
    """Функция  создания драйвера"""
    browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    return browser


def get_all_product(browser: webdriver.Chrome):
    """Функция  получения данных о товарах со страницы свайта"""
    browser.get("https://www.saucedemo.com/")
    browser.find_element(By.CSS_SELECTOR, "[placeholder ='Username']").send_keys('standard_user')
    time.sleep(1)
    browser.find_element(By.CSS_SELECTOR, "[placeholder ='Password']").send_keys('secret_sauce')
    time.sleep(1)
    browser.find_element(By.CSS_SELECTOR, "#login-button").click()
    time.sleep(2)

    all_card_products = browser.find_elements(By.CSS_SELECTOR, ".inventory_item")
    time.sleep(2)

    all_data_page = []  # Массив для записи полученных данных
    for product in all_card_products:
        title_product = product.find_element(By.CSS_SELECTOR, ".inventory_item_name").text  # Получение названия товара
        description_product = product.find_element(By.CSS_SELECTOR,
                                                   ".inventory_item_desc").text  # Получение описания товара
        price_prodict = product.find_element(By.CSS_SELECTOR, ".inventory_item_price").text  # Получение цены товара
        link_img_product = product.find_element(By.CSS_SELECTOR,
                                                ".inventory_item_img .inventory_item_img").get_attribute(
            'src')  # Получение линка на товара
        all_data_page.append({  # Запись словаря с данными о товаре в массив
            "title_product": title_product,
            "description_product": description_product,
            "price_prodict": price_prodict,
            "link_img_product": link_img_product
        })
    browser.quit()
    return all_data_page


if __name__ == '__main__':
    br = browser()
    product = get_all_product(br)
    pprint(product)
