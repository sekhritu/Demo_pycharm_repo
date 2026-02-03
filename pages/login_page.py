from selenium.webdriver.common.by import By

from pages.basic_action import BasicActions


class LoginPage(BasicActions):
    username = (By.XPATH, "//input[@id='user-name']")
    password = (By.XPATH, "//input[@id='password']")
    submit_btn = (By.XPATH, '//input[@id="login-button"]')

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def enter_username(self, username_value):
        self.type_word(self.username, username_value)

    def enter_password(self, password_value):
        self.type_word(self.password, password_value)

    def click_on_submit(self):
        self.click_me(self.submit_btn )