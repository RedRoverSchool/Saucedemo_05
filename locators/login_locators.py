from selenium.webdriver.common.by import By


class LoginLocators:
    input_username = (By.ID, 'user-name')
    input_password = (By.ID, 'password')
    login_btn = (By.ID, 'login-button')
    hamburger_btn = (By.ID, 'react-burger-menu-btn')
    logout_btn = (By.ID, 'logout_sidebar_link')
    title = 'Swag Labs'
