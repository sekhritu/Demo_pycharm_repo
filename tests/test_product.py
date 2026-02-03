import time

import pytest

from pages.login_page import LoginPage
from pages.product_page import ProductPage
from utilities.common_functions import get_data_from_input_file


class TestProduct:

    def __init__(self):
        self.driver = None

    @pytest.mark.usefixtures('lunch_the_application')
    def test_validate_login_functionality(self):
        login_page = LoginPage(self.driver)
        username = get_data_from_input_file("username")
        password = get_data_from_input_file("password")
        login_page.enter_username(username)
        login_page.enter_password(password)
        login_page.click_on_submit()
        product_page = ProductPage(self.driver)
        time.sleep(2)
        product_page.capture_all_product()


    @pytest.mark.usefixtures('lunch_the_application')
    def test_select_product(self):
        login_page = LoginPage(self.driver)
        username = get_data_from_input_file("username")
        password = get_data_from_input_file("password")
        login_page.enter_username(username)
        login_page.enter_password(password)
        login_page.click_on_submit()
        product_page = ProductPage(self.driver)
        time.sleep(2)
        product_page.click_on_first_product()