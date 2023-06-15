import time

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import ElementClickInterceptedException, TimeoutException, NoSuchElementException
from Util.logs import getLogger
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
import inspect

MAX_WAIT_TIME = 10


class BaseElement:

    log = getLogger()

    def __init__(self, driver, locator):
        self.locator = locator
        self.driver = driver
        self.web_element = None
        self.find()

    def find(self):
        is_element_found = True
        try:
            element = WebDriverWait(self.driver, MAX_WAIT_TIME).until(
                EC.visibility_of_element_located(self.locator))
        except TimeoutException:
            is_element_found = False
        else:
            self.web_element = element
        finally:
            if not is_element_found:
                caller_file = inspect.stack()[2][1].split("\\")[-1]
                caller_function = inspect.stack()[2][3]
                line = inspect.getframeinfo(inspect.stack()[1][0]).lineno
                self.log.debug(f" {caller_file} - {caller_function}() - An element is not found.")
                # raise Exception(f"Unable to find web element in {caller_file} file {caller_function}() function")
            return None

    def click_element(self):
        try:
            element = WebDriverWait(self.driver, MAX_WAIT_TIME).until(
                EC.element_to_be_clickable(self.locator))
            element.click()
        except ElementClickInterceptedException:
            self.log.debug("Element is not clickable.")

    def enter_text(self, text):
        # calling_object = inspect.currentframe().f_back.f_locals.get('self', None)
        # object_name = calling_object.__class__.__name__ if calling_object else "Unknown Object"
        # function_name = inspect.currentframe().f_back.f_code.co_name
        # self.log.info(f"{function_name} - {object_name} - Sending text: {text}")
        self.web_element.clear()
        self.web_element.send_keys(text)

    def get_text(self):
        text = self.web_element.text
        return text

    def is_elm_selected(self):
        return self.web_element.is_selected()

    def elm_is_displayed(self):
        return self.web_element.is_displayed()

    def scroll_to_element(self):
        actions = ActionChains(self.driver)
        actions.move_to_element(self.web_element).perform()
        # Or we can use
        # driver.execute_script("arguments[0].scrollIntoView();", self.element)

    def press_enter_key(self):
        self.web_element.send_keys(Keys.ENTER)

    def press_tab_key(self):
        self.web_element.send_keys(Keys.TAB)

    def select_option(self, **kwargs):
        """
        :param kwargs: index or text or value (only one required)
        """
        elm = Select(self.web_element)
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
        return self.web_element is not None

    def double_click(self):
        action_chains = ActionChains(self.driver)
        action_chains.double_click(self.web_element).perform()

    def wait_till_text_to_be_present_in_element(self, text):
        WebDriverWait(self.driver, MAX_WAIT_TIME).\
            until(EC.text_to_be_present_in_element(self.locator, text))

    def wait_till_text_to_be_not_present_in_element(self, text):
        WebDriverWait(self.driver, MAX_WAIT_TIME).\
            until_not(EC.text_to_be_present_in_element(self.locator, text))

    def wait_till_element_not_present(self):
        WebDriverWait(self.driver, MAX_WAIT_TIME).\
            until(EC.invisibility_of_element_located(self.locator))

    # methods for multiple elements returned
    def get_all_elements(self) -> list:
        return WebDriverWait(self.driver, MAX_WAIT_TIME). \
            until(EC.visibility_of_all_elements_located(self.locator))

    def get_all_elements_text(self) -> list:
        elm_list = self.get_all_elements()
        return [elm.text for elm in elm_list]

    def click_all_elements(self):
        elm_list = self.get_all_elements()
        if len(elm_list) > 0:
            for elm in elm_list:
                elm.click()
        else:
            self.log.debug("No element found to click.")


class NestedElement:

    log = getLogger()

    def __init__(self, parent_web_element, locator):
        self.parent_web_element = parent_web_element
        self.locator = locator
        self.web_element = None
        self.find()

    def find(self):
        by = self.locator[0]
        value = self.locator[1]
        element = self.parent_web_element.find_element(by=by, value=value)
        self.web_element = element
        return None

    def get_text(self):
        text = self.web_element.text
        return text