from selenium.webdriver.common.by import By


def test_pp_social_logo(d, correct_login):
    d.find_element(By.CLASS_NAME, "app_logo").click()
    assert d.title == "Swag Labs", "NOT FOUNDED"
    d.find_element(By.CLASS_NAME, "social").is_displayed(), "NOT FOUND"
