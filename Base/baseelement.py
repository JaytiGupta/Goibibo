from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import ElementClickInterceptedException
from selenium.webdriver.common.by import By


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

    def get_elements(self):
        return WebDriverWait(self.driver, 20).\
            until(EC.visibility_of_all_elements_located((self.locator, self.locator_value)))

    def get_elements_text(self):
        elm_list = self.get_elements()
        txt_list = []
        for i in elm_list:
            txt_list.append(i.text)
        return txt_list

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

    def elm_is_displayed(self):
        return self.element.is_displayed()



