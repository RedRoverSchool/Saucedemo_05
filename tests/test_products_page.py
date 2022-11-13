import conf
from pages.locators import LoginPageLocators
from pages.locators import ProductPageLocators

# from pprint import pprint


class TestProductPage:
    def test_get_all_product(self, d):

        assert d.current_url == conf.URL
        # login
        d.find_element(*LoginPageLocators.LOGIN_FORM).send_keys("standard_user")
        d.find_element(*LoginPageLocators.PASSWORD_FORM).send_keys("secret_sauce")
        d.find_element(*LoginPageLocators.LOGIN_BUTTON).click()
        assert d.current_url == "https://www.saucedemo.com/inventory.html"

        inventory_list = d.find_elements(*ProductPageLocators.INVENTORY_LIST)

        list_inventory = []

        for product in inventory_list:
            inventory_item_name = product.find_element(
                *ProductPageLocators.INVENTORY_ITEM_NAME
            ).text
            inventory_item_price = product.find_element(
                *ProductPageLocators.INVENTORY_ITEM_PRICE
            ).text
            inventory_item_desc = product.find_element(
                *ProductPageLocators.INVENTORY_ITEM_DESC
            ).text

            list_inventory.append(
                {
                    "1_product": inventory_item_name,
                    "2_price": inventory_item_price,
                    "3_description": inventory_item_desc,
                }
            )

        # return list_inventory

    def test_sort_price_low_to_high(self, d):

        d.find_element(*ProductPageLocators.PRICE_LOW_TO_HIGH).click()

        inventory_list = d.find_elements(*ProductPageLocators.INVENTORY_LIST)
        list_inventory = []

        for product in inventory_list:
            # inventory_item_name = product
            # .find_element(By.CSS_SELECTOR, '.inventory_item_name').text
            inventory_item_price = product.find_element(
                *ProductPageLocators.INVENTORY_ITEM_PRICE
            ).text

            list_inventory.append(
                inventory_item_price,
            )

        price_low_to_high = []
        for i in range(1, len(list_inventory)):
            price_el = float(list_inventory[i].replace("$", "", 1))

            price_low_to_high.append(
                price_el,
            )

        for i in range(0, len(price_low_to_high) - 1):
            assert price_low_to_high[i] <= price_low_to_high[i + 1]

        d.quit()
        # return price_low_to_high

    # if __name__ == "__main__":
    #     product = test_get_all_product(d)
    #     pprint(product)
    #
    #     price_sorted = test_sort_price_low_to_high(d)
    #     print(f"price_low_to_high: {price_sorted}")
