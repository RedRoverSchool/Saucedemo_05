from selenium.webdriver.common.by import By
from ..pages.locators import InventoryPageLocators


def test_cart_page_copywriter(d, correct_login):
    d.find_element(*InventoryPageLocators.CART_BTN).click()
    d.find_element(By.CLASS_NAME, "app_logo").click()
    assert d.title == "Swag Labs", "NOT FOUNDED"
    a = d.find_element(By.CLASS_NAME, "footer_copy")
    assert (
        a.text
        == "© 2022 Sauce Labs. All Rights Reserved. Terms of Service | Privacy Policy"
    ), "copywriter NOT FOUND"
    img = d.find_element(
        By.XPATH, '//body/div[@id="root"]/div[@id="page_wrapper"]/footer[1]/img[1]'
    )
    if "ng-hide" in img.get_attribute("class"):
        print("Image is not visible on screen")
    else:
        print("Image is visible on screen")
