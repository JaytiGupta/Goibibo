import inspect
import random

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.select import Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException

from Util.logs import getLogger


MAX_WAIT_TIME = 10


class BaseElement:

    log = getLogger()

    def __init__(self, driver: webdriver.Chrome, locator):
        self.locator = locator
        self.driver = driver
        self.web_element = None
        self.find()

    def find(self):
        is_element_found = True
        try:
            element = WebDriverWait(self.driver, MAX_WAIT_TIME).until(
                EC.visibility_of_element_located(self.locator)
            )
        except TimeoutException:
            is_element_found = False
        else:
            self.web_element = element
        finally:
            if not is_element_found:
                caller_file = inspect.stack()[2][1].split("\\")[-1]
                caller_function = inspect.stack()[2][3]
                line = inspect.getframeinfo(inspect.stack()[1][0]).lineno
                self.log.debug(f" {caller_file} - {caller_function}() at line{line} - An element is not found.")
            return None

    def is_element_present(self) -> bool:
        return self.web_element is not None

    def click_element(self):
        element = WebDriverWait(self.driver, MAX_WAIT_TIME).until(
            EC.element_to_be_clickable(self.locator)
        )
        element.click()
        return None

    def double_click(self):
        action_chains = ActionChains(self.driver)
        action_chains.double_click(self.web_element).perform()
        return None

    def enter_text(self, text):
        self.web_element.clear()
        self.web_element.send_keys(text)
        return None

    def get_text(self):
        text = self.web_element.text
        return text

    def get_attribute(self, attr_name):
        attribute = self.web_element.get_attribute(attr_name)
        return attribute

    def is_selected(self):
        return self.web_element.is_selected()

    def is_displayed(self):
        return self.web_element.is_displayed()

    def scroll_into_view(self):
        actions = ActionChains(self.driver)
        actions.move_to_element(self.web_element).perform()
        return None
        # Or we can use
        # driver.execute_script("arguments[0].scrollIntoView();", self.element)

    def press_enter_key(self):
        self.web_element.send_keys(Keys.ENTER)
        return None

    def press_tab_key(self):
        self.web_element.send_keys(Keys.TAB)
        return None

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
            self.log.debug(
                f"No option present for which dropdown {list(kwargs.keys())[0]} "
                f"is \"{list(kwargs.values())[0]}\""
            )
            raise ValueError(
                f"No option present for which dropdown {list(kwargs.keys())[0]} "
                f"is \"{list(kwargs.values())[0]}\""
            )
        return None

    def select_random_dropdown_option(self, *options_to_remove: str):
        """
        Selects a random option from a dropdown, excluding specified options.

        This method selects a random option from the dropdown list, excluding any options
        specified as parameters. If specific options to exclude are provided, they will
        not be considered in the random selection.

        :param options_to_remove: Optional. A variable number of strings representing options
                                  that should be excluded from random selection.
        """
        all_dropdown_option_locator = (By.XPATH, ".//option")  # All dropdown elements are always present in option tags
        nested_element_list = NestedElement(self.web_element, all_dropdown_option_locator).get_all_elements()
        all_dropdown_option_text = [element.text for element in nested_element_list]

        for option in options_to_remove:
            if option in all_dropdown_option_text:
                all_dropdown_option_text.remove(option)
            else:
                self.log.info(f"Option '{option}' is not in the dropdown options "
                              f"to be removed for selection.")

        random_element_text = random.choice(all_dropdown_option_text)

        self.select_option(text=random_element_text)
        self.log.info(f"'{random_element_text}' selected from dropdown option.")

        return None

    #
    # # Waiting Methods
    def wait_till_text_to_be_present_in_element(self, text):
        WebDriverWait(self.driver, MAX_WAIT_TIME).until(
            EC.text_to_be_present_in_element(self.locator, text)
        )
        return None

    def wait_till_text_to_be_present_in_value(self, text):
        WebDriverWait(self.driver, MAX_WAIT_TIME).until(
            EC.text_to_be_present_in_element_value(self.locator, text)
        )
        return None

    def wait_till_text_to_be_present_in_attribute(self, attribute, text):
        WebDriverWait(self.driver, MAX_WAIT_TIME).until(
            EC.text_to_be_present_in_element_attribute(self.locator, attribute, text)
        )
        return None

    def wait_till_element_attribute_to_include(self, attribute):
        WebDriverWait(self.driver, MAX_WAIT_TIME).until(
            EC.element_attribute_to_include(self.locator, attribute)
        )
        return None

    def wait_till_text_to_be_not_present_in_element(self, text):
        WebDriverWait(self.driver, MAX_WAIT_TIME).until_not(
            EC.text_to_be_present_in_element(self.locator, text)
        )
        return None

    def wait_till_text_to_be_not_present_in_value(self, text):
        WebDriverWait(self.driver, MAX_WAIT_TIME).until_not(
            EC.text_to_be_present_in_element_value(self.locator, text)
        )
        return None

    def wait_till_text_to_be_not_present_in_attribute(self, attribute, text):
        WebDriverWait(self.driver, MAX_WAIT_TIME).until_not(
            EC.text_to_be_present_in_element_attribute(self.locator, attribute, text)
        )
        return None

    def wait_till_element_not_present(self):
        WebDriverWait(self.driver, MAX_WAIT_TIME).until(
            EC.invisibility_of_element_located(self.locator)
        )
        return None

    # def wait_till_staleness_of_element(self):
    #     WebDriverWait(self.driver, MAX_WAIT_TIME).until(EC.staleness_of(self.web_element))

    #
    # # Methods for handling multiple returned elements
    def get_all_elements(self) -> list:
        return WebDriverWait(self.driver, MAX_WAIT_TIME).until(
            EC.visibility_of_all_elements_located(self.locator)
        )

    def get_all_elements_text(self) -> list:
        elm_list = self.get_all_elements()
        return [elm.text for elm in elm_list]

    def get_all_elements_attribute(self, attr_name) -> list:
        elm_list = self.get_all_elements()
        return [elm.get_attribute(attr_name) for elm in elm_list]

    def click_all_elements(self):
        elm_list = self.get_all_elements()
        if len(elm_list) > 0:
            for elm in elm_list:
                elm.click()
        else:
            self.log.debug("No element found to click.")
        return None


class NestedElement:

    """
    Used to find an element inside another element
    """
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

    def get_all_elements(self) -> list:
        by = self.locator[0]
        value = self.locator[1]
        elements = self.parent_web_element.find_elements(by=by, value=value)
        return elements

    def click_element(self):
        self.web_element.click()

    def enter_text(self, text):
        self.web_element.clear()
        self.web_element.send_keys(text)

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
            raise ValueError(f"No option present for which dropdown {list(kwargs.keys())[0]} "
                             f"is \"{list(kwargs.values())[0]}\"")
