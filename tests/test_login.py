import time

import pytest

from pages.login_page import LoginPage
from utilities.common_functions import get_data_from_input_file


class TestLogin:

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
        time.sleep(5)
