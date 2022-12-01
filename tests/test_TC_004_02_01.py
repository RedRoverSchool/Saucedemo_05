from selenium.webdriver.common.by import By


def test_add_to_cart_check_item(d, correct_login):
    d.find_element(By.ID, "add-to-cart-test.allthethings()-t-shirt-(red)").click()
    d.find_element(By.ID, "shopping_cart_container").click()
    assert (
        d.find_element(By.CLASS_NAME, "inventory_item_name").text
        == "Test.allTheThings() T-Shirt (Red)"
    ), "NOT FOUND"
