from selenium.webdriver.common.by import By


def test_widget_FB(d, correct_login):
    d.find_element(By.XPATH, '//a[contains(text(),"Facebook")]').click()
    handles = d.window_handles
    d.switch_to.window(handles[1])
    url = d.current_url
    assert (
        "https://www.facebook.com" in url and "saucelabs" in url
    ), "you are NOT on correct Facebook page"
