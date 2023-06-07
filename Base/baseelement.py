from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import ElementClickInterceptedException, TimeoutException, NoSuchElementException
from Util.logs import getLogger
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
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
            return WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located(
                (self.locator, self.locator_value)))
        except TimeoutException:
            caller_file = inspect.stack()[2][1].split("\\")[-1]
            caller_function = inspect.stack()[2][3]
            self.log.debug(f" {caller_file} - {caller_function}() - An element is not found.")
            return "Element is not found."

    def click_element(self):
        try:
            self.element.click()
        except ElementClickInterceptedException:
            self.log.debug("Element is not clickable.")

    def enter_text(self, text):
        self.element.clear()
        self.element.send_keys(text)
        # self.press_tab_key()

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

    def press_tab_key(self):
        self.element.send_keys(Keys.TAB)

    def select_option(self, **kwargs):
        """
        :param kwargs: index or text or value (only one required)
        """
        elm = Select(self.element)
        try:
            if kwargs.get("index") is not None:
                elm.select_by_index(kwargs.get("index"))
            elif kwargs.get("text") is not None:
                elm.select_by_visible_text(kwargs.get("text"))
            elif kwargs.get("value") is not None:
                elm.select_by_value(kwargs.get("value"))
        except NoSuchElementException:
            self.log.debug(f"- No option present for which dropdown {list(kwargs.keys())[0]} "
                           f"is \"{list(kwargs.values())[0]}\"")
            raise ValueError(f"No option present for which dropdown {list(kwargs.keys())[0]} is \"{list(kwargs.values())[0]}\"")

    def is_element_present(self):
        """
        :return: True or False
        """
        return not self.element == "Element is not found."

    def double_click(self):
        action_chains = ActionChains(self.driver)
        action_chains.double_click(self.element).perform()

    # methods for multiple elements returned
    def get_all_elements(self) -> list:
        return WebDriverWait(self.driver, 20). \
            until(EC.visibility_of_all_elements_located((self.locator, self.locator_value)))

    def get_all_elements_text(self) -> list:
        elm_list = self.get_all_elements()
        txt_list = []
        for elm in elm_list:
            txt_list.append(elm.text)
        return txt_list
        # Or we can do this
        # elm_list = self.get_all_elements()
        # return [elm.text for elm in elm_list]

    def click_all_elements(self):
        elm_list = self.get_all_elements()
        if len(elm_list) > 0:
            for elm in elm_list:
                elm.click()
        else:
            self.log.debug("No element to click.")

