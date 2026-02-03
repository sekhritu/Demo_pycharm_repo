

import pytest

from pages.basic_action import BasicActions
from utilities.common_functions import get_data_from_input_file

global driver
driver = None



@pytest.fixture(scope="function")
def lunch_the_application(request):
    browser = get_data_from_input_file("Browser")
    url = get_data_from_input_file("url")
    global driver
    basic_action = BasicActions(driver= None)
    driver = basic_action.open_my_browser(browser)
    basic_action.open_application(url)
    request.cls.driver = driver
    yield
    basic_action.close_application()