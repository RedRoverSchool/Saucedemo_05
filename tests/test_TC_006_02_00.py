from selenium.webdriver.common.by import By


def test_mp_presence_copywriter_robot(d, correct_login):
    d.find_element(By.CLASS_NAME, "app_logo").click()
    assert d.title == "Swag Labs", "NOT FOUNDED"
    a = d.find_element(By.CLASS_NAME, "footer_copy")
    assert (
        a.text
        == "© 2022 Sauce Labs. All Rights Reserved. Terms of Service | Privacy Policy"
    ), ("copywriter NOT " "FOUND ")
    img = d.find_element(
        By.XPATH, '//body/div[@id="root"]/div[@id="page_wrapper"]/footer[1]/img[1]'
    )
    print(f"IMG Present_{img.is_displayed()}")
