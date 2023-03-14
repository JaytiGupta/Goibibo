from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import ElementClickInterceptedException


class BaseElement:

    def __init__(self, driver, locator, locator_value):
        self.locator = locator
        self.locator_value = locator_value
        self.driver = driver
        self.element = self.get_element()

    def get_element(self):
        try:
            return WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located((self.locator, self.locator_value)))
        except:
            print("Element is not found.")

    def click_element(self):
        try:
            self.element.click()
        except ElementClickInterceptedException:
            print("Element is not clickable.")

    def enter_text(self, text):
        self.element.clear()
        self.element.send_keys(text)

    def get_text(self):
        return self.element.text

    def is_elm_selected(self):
        return self.element.is_selected()

