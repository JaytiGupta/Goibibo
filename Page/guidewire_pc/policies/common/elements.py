import random

from selenium.webdriver.common.by import By
from Base.baseelement import BaseElement
from Util.logs import getLogger


class TableQuestionnaires:
    log = getLogger()

    def __init__(self, driver):
        self.driver = driver

    @staticmethod
    def radio_btn_locator(question, answer):
        if question.lower() == "all":
            question = ""

        if answer.lower() == "yes":
            x_path = f'//div[contains(text(),"{question}")]/ancestor::tr//input[@type="radio"][@value="true"]'
        else:
            x_path = f'//div[contains(text(),"{question}")]/ancestor::tr//input[@type="radio"][@value="false"]'

        locator = (By.XPATH, x_path)
        return locator

    def select_radio_btn(self, question, answer):
        locator = self.radio_btn_locator(question, answer)
        radio_btn = BaseElement(self.driver, locator)
        radio_btn.click_element()
        self.log.info(f"Select {answer} for {question}.")

    def select_all_radio_btn(self, answer):
        locator = self.radio_btn_locator("all", answer)
        all_radio_btn_elm = BaseElement(self.driver, locator)
        all_radio_btn_elm.click_all_elements()
        self.log.info(f"Select all radio button questions as {answer}.")

    def input_box(self, question, answer):
        x_path = f'//div[contains(text(),"{question}")]/ancestor::tr//input[@type="text"]'
        locator = (By.XPATH, x_path)
        input_box = BaseElement(self.driver, locator)
        input_box.enter_text(answer)
        self.log.info(f"Enter {answer} for {question}.")

    def dropdown(self, question, dropdown_text):
        x_path = f'//div[contains(text(),"{question}")]/ancestor::tr//select'
        locator = (By.XPATH, x_path)
        dropdown_elm = BaseElement(self.driver, locator)
        dropdown_elm.select_option(text=dropdown_text)


class SearchOptionPicker:
    log = getLogger()

    def __init__(self, driver, search_btn_xpath):
        self.driver = driver
        self.search_btn_xpath = search_btn_xpath

    @property
    def _search_btn_locator(self):
        locator = (By.XPATH, self.search_btn_xpath)
        return BaseElement(self.driver, locator)

    @property
    def _last_page_locator(self):
        locator = (By.XPATH, '//div[@class="gw-paging--label-post"]')
        return BaseElement(self.driver, locator)

    @property
    def _page_input(self):
        locator = (By.XPATH, '//input[@class="gw-paging--input gw-noTrack"]')
        return BaseElement(self.driver, locator)

    @property
    def _select_button(self):
        locator = (By.XPATH, '//div[text()="Select"]')
        return BaseElement(self.driver, locator)

    def select_random_option_on_page(self):
        all_select_buttons = self._select_button.get_all_elements()
        random.choice(all_select_buttons).click()

    def _navigate_to_random_page(self):
        last_page_text = self._last_page_locator.get_text()
        last_page = int(last_page_text.replace("/", ""))

        page_to_navigate = random.randint(1, last_page)

        self._page_input.enter_text(page_to_navigate)
        self._page_input.press_enter_key()

    def select_random_option(self):
        self._search_btn_locator.click_element()
        self._navigate_to_random_page()
        self.select_random_option_on_page()



# class InputSet:
#     log = getLogger()
#
#     def __init__(self, driver):
#         self.driver = driver
#         self.tr_xpath = '//div[text()="Class Code"]/ancestor::tr'
#
#     def input_set_row(self, row_number, column_number, tag_name):
#         xpath = f'{self.tr_xpath}/following-sibling::tr[{row_number}]/td[{column_number}]//{tag_name}'
#         locator = (By.XPATH, xpath)
#         return BaseElement(self.driver, locator)
#
#
#     def add_class(self, row_number, gov_law, location, code, employees, basis_value):
#         add_class_button = BaseElement(self.driver, self._locator_AddClass_btn)
#         add_class_button.click_element()
#
#         outside_elm = BaseElement(self.driver, self._locator_covered_employee_txt)
#
#         locator_dict_add_class = self._locator_dynamic_wc_coverages_screen_add_class(row_number)
#
#         governing_law = BaseElement(self.driver, locator_dict_add_class["Governing Law"])
#         governing_law.select_option(text=gov_law)
#
#         loc = BaseElement(self.driver, locator_dict_add_class["Location"])
#         loc.select_option(index=location)
#         outside_elm.click_element()
#
#         class_code = BaseElement(self.driver, locator_dict_add_class["Class Code"])
#         class_code.enter_text(code)
#         outside_elm.click_element()
#         # class_code.press_tab_key() # text not updating in basis field without pressing tab
#
#         emp_number = BaseElement(self.driver, locator_dict_add_class["Employees"])
#         emp_number.enter_text(employees)
#         outside_elm.click_element()
#         # emp_number.press_tab_key()  # text not updating in basis field without pressing tab
#
#         basis = BaseElement(self.driver, locator_dict_add_class["Basis"])
#         basis.enter_text(basis_value)
#
#         self.log.info(f"Covered Employees section - New Class Added. Row Number - {row_number}")