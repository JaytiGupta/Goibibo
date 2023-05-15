from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import ElementClickInterceptedException
from Util.logs import getLogger
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import inspect


class BaseElement:

    log = getLogger()

    def __init__(self, driver, locator):
        self.locator = locator[0]
        self.locator_value = locator[1]
        self.driver = driver
        self.element = self.get_element()

    def get_element(self):
        try:
            return WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((self.locator, self.locator_value)))
        except:
            caller_file = inspect.stack()[2][1].split("\\")[-1]
            caller_function = inspect.stack()[2][3]
            self.log.debug(f" {caller_file} - {caller_function}() - An element is not found.")
            return "Element is not found."

    def get_elements(self):
        return WebDriverWait(self.driver, 10).\
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
            self.log.debug("Element is not clickable.")

    def enter_text(self, text):
        self.element.clear()
        self.element.send_keys(text)

    def get_text(self):
        return self.element.text

    def is_elm_selected(self):
        return self.element.is_selected()

    def elm_is_displayed(self):
        return self.element.is_displayed()

    def scroll_to_element(self):
        actions = ActionChains(self.driver)
        actions.move_to_element(self.element).perform()
        # Or we can use
        # driver.execute_script("arguments[0].scrollIntoView();", self.element)

    def press_enter_key(self):
        self.element.send_keys(Keys.ENTER)
