from ..pages.locators import *


def test_check_item_info(d, correct_login):
    d.find_element(*InventoryPageLocators.FLEECE_JACKET_ADD_BTN).click()
    d.find_element(*InventoryPageLocators.CART_BTN).click()
    d.find_element(By.CLASS_NAME, "inventory_item_name").is_displayed()
    d.find_element(By.CLASS_NAME, "inventory_item_desc").is_displayed()
    d.find_element(By.CLASS_NAME, "inventory_item_price").is_displayed()
