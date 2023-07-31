import random
import time

from Base.basepage import BasePage
from Base.baseelement import BaseElement, NestedElement
from selenium.webdriver.common.by import By
from Page.guidewire_pc.policies.LOBs import common
from Page.guidewire_pc.policies.common.elements import TableQuestionnaires
from Page.guidewire_pc.policies.common.sidebar import Sidebar
from Page.guidewire_pc.policies.common import screens
from Util.logs import getLogger


class WorkersCompensation(BasePage):
    log = getLogger()

    def __init__(self, driver):
        super().__init__(driver=driver, url=None)
        self.title_toolbar = common.TitleToolbar(self.driver)
        self.sidebar = Sidebar(self.driver)
        self.qualification_screen = Qualification(self.driver)
        self.policy_info_screen = screens.PolicyInfo(self.driver)
        self.location_screen = screens.Location(self.driver)
        self.wc_coverages_screen = WCCoverages(self.driver)
        self.supplement_screen = Supplemental(self.driver)
        self.wc_options_screen = WCOptions(self.driver)
        self.risk_analysis_screen = screens.RiskAnalysis(self.driver)
        self.policy_review_screen = screens.PolicyReview(self.driver)
        self.quote_screen = screens.Quote(self.driver)
        self.forms_screen = screens.Forms(self.driver)
        self.payment_screen = Payment(self.driver)
        self.workspace_screen = common.Workspace(self.driver)
        self.transaction_bound_screen = screens.TransactionBoundScreen(self.driver)


class Qualification:
    log = getLogger()

    def __init__(self, driver):
        self.driver = driver
        self.SCREEN_TITLE = "Qualification"
        self.table_questionnaires = TableQuestionnaires(self.driver)


class WCCoverages(BasePage):
    log = getLogger()

    def __init__(self, driver):
        super().__init__(driver=driver, url=None)
        self.SCREEN_TITLE = "WC Coverages"
        self._locator_NCCI_interstate_id_input_box = (
            By.XPATH, '//div[contains(text(),"NCCI Interstate ID")]/parent::div//input')
        self._locator_AddClass_btn = (By.XPATH, '//div[@aria-label="Add Class"]')
        self._locator_covered_employee_txt = (By.XPATH, '//div[text()="Covered Employees"]')

    @staticmethod
    def _locator_dynamic_wc_coverages_screen_add_class(row_number):
        governing_law_xpath = f'//div[text()="Class Code"]/ancestor::tr/following-sibling::' \
                              f'tr[{row_number}]/td[2]//select'  # Govering law
        location_xpath = f'//div[text()="Class Code"]/ancestor::tr/following-sibling::tr[{row_number}]' \
                         f'/td[3]//select'  # Location
        class_code_xpath = f'//div[text()="Class Code"]/ancestor::tr/following-sibling::tr[{row_number}]' \
                           f'/td[4]//input'  # class code
        employees_xpath = f'//div[text()="Class Code"]/ancestor::tr/following-sibling::tr[{row_number}]' \
                          f'/td[6]//input'  # Employees
        basis_xpath = f'//div[text()="Class Code"]/ancestor::tr/following-sibling::tr[{row_number}]' \
                      f'/td[8]//input'  # Basis

        return {
            "Governing Law": (By.XPATH, governing_law_xpath),
            "Location": (By.XPATH, location_xpath),
            "Class Code": (By.XPATH, class_code_xpath),
            "Employees": (By.XPATH, employees_xpath),
            "Basis": (By.XPATH, basis_xpath)
        }

    def add_class(self, row_number, gov_law, location, code, employees, basis_value):
        add_class_button = BaseElement(self.driver, self._locator_AddClass_btn)
        add_class_button.click_element()

        outside_elm = BaseElement(self.driver, self._locator_covered_employee_txt)

        locator_dict_add_class = self._locator_dynamic_wc_coverages_screen_add_class(row_number)

        governing_law = BaseElement(self.driver, locator_dict_add_class["Governing Law"])
        governing_law.select_option(text=gov_law)

        loc = BaseElement(self.driver, locator_dict_add_class["Location"])
        loc.select_option(index=location)
        outside_elm.click_element()

        class_code = BaseElement(self.driver, locator_dict_add_class["Class Code"])
        class_code.enter_text(code)
        outside_elm.click_element()
        # class_code.press_tab_key() # text not updating in basis field without pressing tab

        emp_number = BaseElement(self.driver, locator_dict_add_class["Employees"])
        emp_number.enter_text(employees)
        outside_elm.click_element()
        # emp_number.press_tab_key()  # text not updating in basis field without pressing tab

        basis = BaseElement(self.driver, locator_dict_add_class["Basis"])
        basis.enter_text(basis_value)

        self.log.info(f"Covered Employees section - New Class Added. Row Number - {row_number}")

    def update_class(self, row_number, gov_law=None, location=None, code=None,
                     employees=None, basis_value=None):
        outside_elm = BaseElement(self.driver, self._locator_covered_employee_txt)

        locator_dict_add_class = self._locator_dynamic_wc_coverages_screen_add_class(row_number)

        if gov_law is not None:
            governing_law = BaseElement(self.driver, locator_dict_add_class["Governing Law"])
            governing_law.select_option(text=gov_law)

        if location is not None:
            loc = BaseElement(self.driver, locator_dict_add_class["Location"])
            loc.select_option(index=location)
            outside_elm.click_element()

        if code is not None:
            class_code = BaseElement(self.driver, locator_dict_add_class["Class Code"])
            class_code.enter_text(code)
            outside_elm.click_element()
            # class_code.press_tab_key() # text not updating in basis field without pressing tab

        if employees is not None:
            emp_number = BaseElement(self.driver, locator_dict_add_class["Employees"])
            emp_number.enter_text(employees)
            outside_elm.click_element()
            # emp_number.press_tab_key()  # text not updating in basis field without pressing tab

        if basis_value is not None:
            basis = BaseElement(self.driver, locator_dict_add_class["Basis"])
            basis.enter_text(basis_value)

        self.log.info(f"Covered Employees section - New Class Added. Row Number - {row_number}")


class Supplemental(BasePage):
    log = getLogger()

    def __init__(self, driver):
        super().__init__(driver=driver, url=None)
        self.table_questionnaires = TableQuestionnaires(self.driver)


class WCOptions(BasePage):
    log = getLogger()

    def __init__(self, driver):
        super().__init__(driver=driver, url=None)
        self.SCREEN_TITLE = "WC Options"
        self._locator_add_option_btn = (By.XPATH, '//div[contains(text(),"Add Option")]')
        self._locator_add_federal_class = (By.XPATH, '//div[@aria-label="Add"]')
        self._locator_federal_location_dropdown = (By.XPATH, '//select[contains(@name,"WCLine_WCCovEmpLV-0-Loc")]')
        self._locator_federal_class_code_input_box = (By.XPATH, '//input[contains(@name,"ClassCode")]')
        self._locator_federal_no_of_emp_input_box = (By.XPATH, '//input[contains(@name,"NumEmployees")]')
        self._locator_federal_basis_input_box = (By.XPATH, '//input[contains(@name,"AnnualRenum")]')

    @staticmethod
    def _locator_dynamic_wc_options_selection(wc_option_name):
        xpath = f'//div[contains(text(),"Add Option")]' \
                f'/parent::div/following-sibling::div[2]//' \
                f'div[contains(text(),"{wc_option_name}")]'
        return By.XPATH, xpath

    @property
    def random_text_element(self):
        locator = (By.XPATH, '//div[contains(text(),"Federal Liability Classes")]')
        return BaseElement(self.driver, locator)

    @property
    def class_code_search_option(self):
        locator = (By.XPATH, '//div[contains(@id,"ClassCode")]//span[@aria-label="gw-search-icon"]')
        return BaseElement(self.driver, locator)

    @property
    def class_code_select_button(self):
        locator = (By.XPATH, '//div[text()="Select"]')
        return BaseElement(self.driver, locator)

    def add_wc_option(self, option):
        add_option_btn = BaseElement(self.driver, self._locator_add_option_btn)
        add_option_btn.click_element()
        select_option = BaseElement(self.driver, self._locator_dynamic_wc_options_selection(option))
        select_option.click_element()

    def select_random_federal_class_code(self):
        self.class_code_search_option.click_element()
        all_select_btns = self.class_code_select_button.get_all_elements()
        random.choice(all_select_btns).click()

    def add_federal_class(self, location_index, emp_no, basis_value, class_code=None):
        add_class_btn = BaseElement(self.driver, self._locator_add_federal_class)
        add_class_btn.click_element()

        location = BaseElement(self.driver, self._locator_federal_location_dropdown)
        location.select_option(index=location_index)
        self.random_text_element.click_element()

        emp = BaseElement(self.driver, self._locator_federal_no_of_emp_input_box)
        emp.enter_text(emp_no)

        self.select_random_federal_class_code()

        basis = BaseElement(self.driver, self._locator_federal_basis_input_box)
        basis.enter_text(basis_value)


class Payment(BasePage):
    log = getLogger()

    def __init__(self, driver):
        super().__init__(driver=driver, url=None)
        self.SCREEN_TITLE = "Payment"
        self._locator_billing_method_dropdown = (By.XPATH, '//div[text()="Billing Method"]/following-sibling'
                                                           '::div//select')
        self._locator_plan_type_dropdown = (By.XPATH, '//div[text()="Plan Type"]/following-sibling::div//select')
        self._locator_premium_reporting_plan_dropdown = (By.XPATH, '//div[text()="Premium Reporting Plan"]'
                                                                   '/following-sibling::div//select')

    def select_billing_method(self, text):
        elm = BaseElement(self.driver, self._locator_billing_method_dropdown)
        elm.select_option(text=text)

    def select_plan_type(self, text):
        elm = BaseElement(self.driver, self._locator_plan_type_dropdown)
        elm.select_option(text=text)

    def select_premium_reporting_plan(self, text):
        elm = BaseElement(self.driver, self._locator_premium_reporting_plan_dropdown)
        elm.select_option(text=text)
