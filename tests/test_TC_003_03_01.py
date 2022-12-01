from ..pages.locators import InventoryPageLocators
from ..pages.locators import InventoryItemPageLocator


def test_compare_item_names(d, correct_login):
    get_name_list = d.find_element(*InventoryPageLocators.BIKELIGHT_LABEL).text
    d.find_element(*InventoryPageLocators.BIKELIGHT_LABEL).click()
    get_name_card = d.find_element(*InventoryItemPageLocator.INVENTORY_ITMEM_LABEL).text
    assert get_name_list == get_name_card, "Item Name !ARE NOT! the same"


def test_compare_item_desc(d, correct_login):
    get_desc_list = d.find_element(*InventoryPageLocators.BIKELIGHT_DESCRIPTION).text
    d.find_element(*InventoryPageLocators.BIKELIGHT_LABEL).click()
    get_desc_card = d.find_element(
        *InventoryItemPageLocator.INVENTORY_ITMEM_DESCRIPTION
    ).text
    assert get_desc_list == get_desc_card, "Item description !ARE NOT! the same"


def test_compare_item_price(d, correct_login):
    get_price_list = d.find_element(*InventoryPageLocators.BIKELIGHT_PRICE).text
    d.find_element(*InventoryPageLocators.BIKELIGHT_LABEL).click()
    get_price_card = d.find_element(
        *InventoryItemPageLocator.INVENTORY_ITMEM_PRICE
    ).text
    assert get_price_list == get_price_card, "Item Price !ARE NOT! the same"


def test_compare_item_img(d, correct_login):
    get_img_list = d.find_element(*InventoryPageLocators.BIKELIGHT_IMG).get_attribute(
        "src"
    )
    d.find_element(*InventoryPageLocators.BIKELIGHT_LABEL).click()
    get_img_card = d.find_element(
        *InventoryItemPageLocator.INVENTORY_ITMEM_IMG
    ).get_attribute("src")
    assert get_img_list == get_img_card, "Item image !ARE NOT! the same"
