from selenium.webdriver.common.by import By

link = "https://www.saucedemo.com/"


class InventoryPageLocators:
    CART_BADGE = (By.CSS_SELECTOR, ".shopping_cart_badge")
    APPER_LOGO = (By.XPATH, "//div[@id='root']//div[@class='app_logo']")
    CART_BTN = (By.ID, "shopping_cart_container")
    PRODUCTS_TITLE = (By.XPATH, '//div[@id="header_container"]//span[@class="title"]')
    UPPER_ROBOT_LOGO = (By.XPATH, "UPPER_ROBOT_LOGO")
    SORT_MENU_BUTTON = (By.CSS_SELECTOR, ".product_sort_container")
    SORT_OPTION_BUTTON_AZ = (By.XPATH, "//option[@value='az']")
    SORT_OPTION_BUTTON_ZA = (By.XPATH, "//option[@value='za']")
    SORT_OPTION_BUTTON_LOWHIGH = (By.XPATH, "//option[@value='lohi']")
    SORT_OPTION_BUTTON_HIGHLOW = (By.XPATH, "//option[@value='hilo']")
    # burger menu locators
    BURGER_BTN = (By.ID, "react-burger-menu-btn")
    BURGER_MENU_ALL_ITEMS_BTN = (By.ID, "inventory_sidebar_link")
    BURGER_MENU_ABOUT_BTN = (By.ID, "about_sidebar_link")
    BURGER_MENU_LOGOUT_BTN = (By.ID, "logout_sidebar_link")
    BURGER_MENU_RESER_APP_STATE_BTN = (By.ID, "reset_sidebar_link")
    # Sort menu locators Сортировка
    SORT_BTN = (By.XPATH, "//select[@class='product_sort_container']")
    ACTIVE_SORT_OPTION = (
        By.XPATH,
        "//span[@class='active_option']",
    )  # текущая сортировка страницы
    AZ_SORT_OPTION = (
        By.XPATH,
        "//select[@class='product_sort_container']//option[@value='az']",
    )
    ZA_SORT_OPTION = (
        By.XPATH,
        "//select[@class='product_sort_container']//option[@value='za']",
    )
    LOHI_SORT_OPTION = (
        By.XPATH,
        "//select[@class='product_sort_container']//option[@value='lohi']",
    )
    HILO_SORT_OPTION = (
        By.XPATH,
        "//select[@class='product_sort_container']//option[@value='hilo']",
    )
    # Backpack locators
    BACKPACK_LINK = (By.ID, "item_4_title_link")
    BACKPACK_LABEL = (By.CSS_SELECTOR, "#item_4_title_link .inventory_item_name")
    BACKPACK_IMG = (By.XPATH, "//a[@id='item_4_img_link']//img")
    BACKPACK_ADD_BTN = (By.ID, "add-to-cart-sauce-labs-backpack")
    BACKPACK_REMOVE_BTN = (By.ID, "remove-sauce-labs-backpack")
    BACKPACK_PRICE = (
        By.XPATH,
        "//div[@class='inventory_list']//a[@id='item_4_title_link']/../..//div[@class='inventory_item_price']",
    )
    BACKPACK_DESCRIPTION = (
        By.XPATH,
        "//div[@class='inventory_list']//a[@id='item_4_title_link']/../..//div[@class='inventory_item_desc']",
    )
    # Bike Light locators
    BIKELIGHT_LINK = (By.ID, "item_0_title_link")
    BIKELIGHT_LABEL = (By.CSS_SELECTOR, "#item_0_title_link .inventory_item_name")
    BIKELIGHT_IMG = (By.XPATH, "//a[@id='item_0_img_link']//img")
    BIKELIGHT_ADD_BTN = (By.ID, "add-to-cart-sauce-labs-bike-light")
    BIKELIGHT_REMOVE_BTN = (By.ID, "remove-sauce-labs-bike-light")
    BIKELIGHT_PRICE = (
        By.XPATH,
        "//div[@class='inventory_list']//a[@id='item_0_title_link']/../..//div[@class='inventory_item_price']",
    )
    BIKELIGHT_DESCRIPTION = (
        By.XPATH,
        "//div[@class='inventory_list']//a[@id='item_0_title_link']/../..//div[@class='inventory_item_desc']",
    )
    # Red T-Shirt locators
    RED_TSHIRT_LINK = (By.ID, "item_3_title_link")
    RED_TSHIRT_LABEL = (By.CSS_SELECTOR, "#item_3_title_link .inventory_item_name")
    RED_TSHIRT_IMG = (By.XPATH, "//a[@id='item_3_img_link']//img")
    RED_TSHIRT_ADD_BTN = (By.ID, "add-to-cart-test.allthethings()-t-shirt-(red)")
    RED_TSHIRT_REMOVE_BTN = (By.ID, "remove-test.allthethings()-t-shirt-(red)")
    RED_TSHIRT_PRISE = (
        By.XPATH,
        "//div[@class='inventory_list']//a[@id='item_3_title_link']/../..//div[@class='inventory_item_price']",
    )
    RED_TSHIRT_DESCRIPTION = (
        By.XPATH,
        "//div[@class='inventory_list']//a[@id='item_3_title_link']/../..//div[@class='inventory_item_desc']",
    )
    # Bolt T-Shirt locators
    BOLT_TSHIRT_LINK = (By.ID, "item_1_title_link")
    BOLT_TSHIRT_LABEL = (By.ID, "#item_1_title_link .inventory_item_name")
    BOLT_TSHIRT_IMG = (By.XPATH, "//a[@id='item_1_img_link']//img")
    BOLT_TSHIRT_ADD_BTN = (By.ID, "add-to-cart-sauce-labs-bolt-t-shirt")
    BOLT_TSHIRT_REMOVE_BTN = (By.ID, "remove-sauce-labs-bolt-t-shirt")
    BOLT_TSHIRT_PRICE = (
        By.XPATH,
        "//div[@class='inventory_list']//a[@id='item_1_title_link']/../..//div[@class='inventory_item_price']",
    )
    BOLT_TSHIRT_DESCRIPTION = (
        By.XPATH,
        "//div[@class='inventory_list']//a[@id='item_1_title_link']/../..//div[@class='inventory_item_desc']",
    )
    # Fleece Jacket locators
    FLEECE_JACKET_LINK = (By.ID, "item_5_title_link")
    FLEECE_JACKET_LABEL = (By.CSS_SELECTOR, "#item_5_title_link .inventory_item_name")
    FLEECE_JACKET_IMG = (By.XPATH, "//a[@id='item_5_img_link']//img")
    FLEECE_JACKET_ADD_BTN = (By.ID, "add-to-cart-sauce-labs-fleece-jacket")
    FLEECE_JACKET_REMOVE_BTN = (By.ID, "remove-sauce-labs-fleece-jacket")
    FLEECE_JACKET_PRICE = (
        By.XPATH,
        "//div[@class='inventory_list']//a[@id='item_5_title_link']/../..//div[@class='inventory_item_price']",
    )
    FLEECE_JACKET_DESCRIPTION = (
        By.XPATH,
        "//div[@class='inventory_list']//a[@id='item_5_title_link']/../..//div[@class='inventory_item_desc']",
    )
    # Onesie locators
    ONESIE_LINK = (By.ID, "item_2_title_link")
    ONESIE_LABEL = (By.CSS_SELECTOR, "#item_2_title_link .inventory_item_name")
    ONESIE_IMG = (By.XPATH, "//a[@id='item_2_img_link']//img")
    ONESIE_ADD_BTN = (By.ID, "add-to-cart-sauce-labs-onesie")
    ONESIE_REMOVE_BTN = (By.ID, "remove-sauce-labs-onesie")
    ONESIE_PRICE = (
        By.XPATH,
        "//div[@class='inventory_list']//a[@id='item_2_title_link']/../..//div[@class='inventory_item_price']",
    )
    ONESIE_DESCRIPTION = (
        By.XPATH,
        "//div[@class='inventory_list']//a[@id='item_2_title_link']/../..//div[@class='inventory_item_desc']",
    )


class LoginPageLocators:
    LOGIN_BTN = (By.ID, "login-button")
    USERNAME_INPUT = (By.ID, "user-name")
    PASSWORD_INPUT = (By.ID, "password")
    LOGIN_BOX = (By.CLASS_NAME, "login-box")
    MESSAGE_EPIC_SADFACE = (By.XPATH, "//*[contains(text(), 'Epic sadface')]")
    USER_NAME = "standard_user"
    PASSWORD = "secret_sauce"


class InventoryItemPageLocator:
    BACK_TO_PRODUCKS_BTN = (By.ID, "back-to-products")
    # ADD_BTN и REMOVE_BTN локаторы в карточке продукта СОВПАДАЮ! c локаторами на InventoryPageLocators
    # для каждого продукта свой набор локаторов
    # поэтому используем их и в карточке продукта!
    #
    # Item product cart locators !!!ОДИНАКОВЫЕ ДЛЯ ВСЕХ ТОВАРОВ, когда мы зашли на карточку описания продукта
    INVENTORY_ITMEM_LABEL = (
        By.XPATH,
        "//div[@id='inventory_item_container']//div[@class='inventory_details_name large_size']",
    )
    INVENTORY_ITMEM_IMG = (
        By.XPATH,
        "//div[@id='inventory_item_container']//img[@class='inventory_details_img']",
    )
    INVENTORY_ITMEM_PRICE = (
        By.XPATH,
        "//div[@id='inventory_item_container']//div[@class='inventory_details_price']",
    )
    INVENTORY_ITMEM_DESCRIPTION = (
        By.XPATH,
        "//div[@id='inventory_item_container']//div[@class='inventory_details_desc large_size']",
    )
    INVENTORY_ITMEM_DESCRIPTION = (
        By.XPATH,
        "//div[@id='inventory_item_container']//div[@class='inventory_details_desc large_size']",
    )
    SORT_MENU_BUTTON = (By.CSS_SELECTOR, ".product_sort_container")
    SORT_OPTION_BUTTON_AZ = (By.XPATH, "//option[@value='az']")
    SORT_OPTION_BUTTON_ZA = (By.XPATH, "//option[@value='za']")
    SORT_OPTION_BUTTON_LOWHIGH = (By.XPATH, "//option[@value='lohi']")
    SORT_OPTION_BUTTON_HIGHLOW = (By.XPATH, "//option[@value='hilo']")


class CartPageLocators:
    CART_ITEM_BLOCK = (By.CLASS_NAME, "cart_item")
    REMOVE_ITEM_BTN = (By.ID, "remove-sauce-labs-backpack")
    CART_ICON = (By.ID, "shopping_cart_container")
    BT_CHECKOUT = (By.ID, "checkout")
    CONTINUE_SHOPPING = (By.ID, "continue-shopping")


class CheckoutPageLocators:
    FIRS_NAME = (By.ID, "first-name")
    LAST_NAME = (By.ID, "last-name")
    ZIP_P_CODE = (By.ID, "postal-code")
    CANCEL = (By.ID, "cancel")
    CONTINUE = (By.ID, "continue")
    FINISH = (By.ID, "finish")


class Widgets:
    FB_WIDGET_ALL_PAGES = (By.XPATH, '//a[contains(text(),"Facebook")]')
    TWITTER_WIDGET_ALL_PAGES = (By.XPATH, '//a[contains(text(),"Twitter")]')
    LINKEDIN_WIDGET_ALL_PAGES = (By.XPATH, '//a[contains(text(),"LinkedIn")]')
