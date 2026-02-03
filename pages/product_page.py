from selenium.webdriver.common.by import By

from pages.basic_action import BasicActions


class ProductPage(BasicActions):
    all_product = (By.XPATH, "//div[@data-test='inventory-item-name']")
    first_product = (By.CSS_SELECTOR, "#add-to-cart-sauce-labs-backpack")


    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def capture_all_product(self):
        value = self.get_all_locator_text(self.all_product)
        print(value)

    def click_on_first_product(self):
        self.click_me(self.first_product)