from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import  expected_conditions as EC


class BasicActions:

    def __init__(self, driver= None):
        self.driver= driver

    def get_web_element(self, locator):
        try:
            element = self.driver.find_element(locator[0], locator[1])
            return element
        except Exception as e:
            print(f"exception occours {e}")

    def get_web_elements(self, locator):
        try:
            elements = self.driver.find_elements(locator[0], locator[1])
            return elements
        except Exception as e:
            print(f"exception occours {e}")

    def click_me(self,locator):
        try:
            self.wait_for_object(locator)
            elements = self.get_web_element(locator)
            elements.click()
        except Exception as e:
            print(f"exception occours {e}")

    def type_word(self,locator, value):
        try:
            self.wait_for_object(locator)
            elements = self.get_web_element(locator)
            elements.send_keys(value)
        except Exception as e:
            print(f"exception occours {e}")

    def open_my_browser(self, browser):
        if browser == "chrome":
            self.driver = self.open_chrome()
        elif browser == "firefox":
            self.driver = self.open_firefox()
        else:
            self.driver = self.open_edge()
        return self.driver


    def open_chrome(self):
        self.driver = webdriver.Chrome()
        return self.driver

    def open_firefox(self):
        self.driver = webdriver.Firefox()
        return self.driver

    def open_edge(self):
        self.driver = webdriver.Edge()
        return self.driver

    def open_application(self, url):
        self.driver.get(url)

    def close_application(self):
        self.driver.close()

    def wait_for_object(self, locator):
        try:
            WebDriverWait(self.driver, 20).until(EC.presence_of_element_located(locator))
        except Exception as e:
            print(f"excepiton occured as {e}")

    def double_method(self, locator):
        action = ActionChains(self.driver)
        element = self.get_web_element(locator)
        action.double_click(element).perform()

    def get_text(self, locator):
        self.wait_for_object(locator)
        element = self.get_web_element(locator)
        return element.text

    def get_all_locator_text(self, locator):
        text = []
        self.wait_for_object(locator)
        elements = self.get_web_elements(locator)
        for element in elements:
            text.append(element.text)
        return text