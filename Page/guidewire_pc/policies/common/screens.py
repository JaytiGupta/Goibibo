import time
from re import sub
from selenium.webdriver.common.by import By
from Base.baseelement import BaseElement
from Base.baseelement import NestedElement
from Base.basepage import BasePage
from Util.logs import getLogger
import random
from Page.guidewire_pc.policies.common.titlebar import TitleToolbar


class PolicyInfo(BasePage):
    log = getLogger()

    def __init__(self, driver):
        super().__init__(driver=driver, url=None)
        self.SCREEN_TITLE = "Policy Info"
        self._locator_FEIN_input_box = (By.XPATH, '//div[text()="FEIN"]/parent::div//input')
        self._locator_industry_code_input_box = (By.XPATH, '//div[text()="Industry Code"]/parent::div//input')
        self._locator_year_business_started_input_box = (
            By.XPATH, '//div[text()="Year Business Started"]/parent::div//input')
        self._locator_term_type_dropdown = (By.XPATH, '//div[text()="Term Type"]/parent::div//select')
        self._locator_effective_date_input_box = (By.XPATH, '//div[text()="Effective Date"]/parent::div//input')
        self._locator_underwriter_companies_dropdown = (By.XPATH, '//select[contains(@name, "UWCompanyInputSet")]')

    @property
    def organization_type_dropdown(self):
        locator = (By.XPATH, '//div[text()="Organization Type"]/parent::div//select')
        return BaseElement(self.driver, locator)

    def input_FEIN(self, text):
        fein = BaseElement(self.driver, self._locator_FEIN_input_box)
        fein.enter_text(text)  # text must be 9-digit no.
        self.log.info(f"Enter FEIN - {text}")

    def industry_code_input(self, industry_code):
        industry_code_elm = BaseElement(self.driver, self._locator_industry_code_input_box)
        industry_code_elm.enter_text(industry_code)
        self.log.info(f"Enter Industry Code - {industry_code}")

    def select_organization_type(self, type_of_org):
        self.organization_type_dropdown.select_option(text=type_of_org)
        self.log.info(f"Select Organisation Type - {type_of_org}")

    def term_type(self, pol_term):
        term_type_elm = BaseElement(self.driver, self._locator_term_type_dropdown)
        term_type_elm.select_option(text=pol_term)
        self.log.info(f"Select Policy Term Type - {pol_term}")

    def policy_effective_date(self, policy_date):
        eff_date_elm = BaseElement(self.driver, self._locator_effective_date_input_box)
        eff_date_elm.enter_text(policy_date)
        self.log.info(f"Enter Policy Effective Date - {policy_date}")

    def uw_companies(self, uw_company):
        uw_company_elm = BaseElement(self.driver, self._locator_underwriter_companies_dropdown)
        uw_company_elm.select_option(text=uw_company)
        self.log.info(f"Select Underwriting company - {uw_company}")

    # select only from first page
    def select_random_industry_code(self):
        locator_industry_code_search_icon = (By.XPATH, '//div[text()="Industry Code"]/parent::div//'
                                                       'span[@aria-label="gw-search-icon"]')
        industry_code_search_btn = BaseElement(self.driver, locator_industry_code_search_icon)
        industry_code_search_btn.click_element()

        locator_industry_code_page_all_select_btn = (By.XPATH, '//div[text()="Select"]')
        industry_code_page_all_select_btn = BaseElement(self.driver, locator_industry_code_page_all_select_btn)

        random_select_button = random.choice(industry_code_page_all_select_btn.get_all_elements())
        random_select_button.click()

    def fill_random_details(self):
        fein = random.randint(10**8, (10**9-1))
        self.input_FEIN(fein)
        self.select_random_industry_code()
        self.organization_type_dropdown.select_random_dropdown_option('<none>')
        return None


class RiskAnalysis(BasePage):
    log = getLogger()

    def __init__(self, driver):
        super().__init__(driver=driver, url=None)
        self.SCREEN_TITLE = "Risk Analysis"

    @property
    def _all_pending_approval_check_box(self):
        locator = (By.XPATH, '//div[text()="Approve"]/ancestor::td[not(contains(@colspan,"1"))]'
                             '/preceding-sibling::td[4]'
                             '//input[@type="checkbox"]')
        return BaseElement(self.driver, locator)

    @property
    def _header_approve_btn(self):
        locator = (By.XPATH, '//div[@class="gw-ListView--UI-left"]//div[text()="Approve"]')
        return BaseElement(self.driver, locator)

    @property
    def _risk_approval_details_screen_ok_button(self):
        locator = (By.XPATH, '//div[@role="button"]//div[@aria-label="OK"]')
        return BaseElement(self.driver, locator)

    def approve_all_uw_issues(self):
        self._all_pending_approval_check_box.click_all_elements()
        self._header_approve_btn.click_element()
        self._risk_approval_details_screen_ok_button.click_element()
        self.accept_alert()

        pending_check_boxes = self._all_pending_approval_check_box.is_element_present()
        if pending_check_boxes:
            self.log.debug("All UW Issues are not approved yet.")
        else:
            self.log.info("All UW Issues are approved.")


class PolicyReview(BasePage):
    log = getLogger()

    def __init__(self, driver):
        super().__init__(driver=driver, url=None)
        self.SCREEN_TITLE = "Policy Review"


class Quote(BasePage):
    log = getLogger()

    def __init__(self, driver):
        super().__init__(driver=driver, url=None)
        self.SCREEN_TITLE = "Quote"

    @property
    def _total_premium_amt(self):
        locator = (By.XPATH, '//div[text()="Total Premium"]/following-sibling::div//div[contains(text(), "$")]')
        return BaseElement(self.driver, locator)

    def total_premium_amount(self):
        premium_amount_text = self._total_premium_amt.get_text()
        premium = float(sub(r'[^\d.]', '', premium_amount_text))
        self.log.info(f"Total Premium is {premium_amount_text}")
        return premium


class Location(BasePage):
    log = getLogger()

    def __init__(self, driver):
        super().__init__(driver=driver, url=None)
        self.SCREEN_TITLE = "Locations"
        self._locator_add_new_location_btn = (By.XPATH, '//div[contains(text(), "New Loc")]')
        self._locator_address1 = (By.XPATH, '//div[contains(text(),"Address 1")]/following-sibling::div//input')
        self._locator_address2 = (By.XPATH, '//div[contains(text(),"Address 2")]/following-sibling::div//input')
        self._locator_address3 = (By.XPATH, '//div[contains(text(),"Address 3")]/following-sibling::div//input')
        self._locator_input_city = (By.XPATH, '//div[contains(text(),"City")]/following-sibling::div//input')
        self._locator_select_state = (By.XPATH, '//div[contains(text(),"State")]/following-sibling::div//select')
        self._locator_input_zip = (By.XPATH, '//div[contains(text(),"ZIP Code")]/following-sibling::div//input')
        self._locator_ok_btn = (By.XPATH, '//div[@id="LocationPopup-LocationScreen-Update"]')
        self._locator_add_existing_location_btn = (By.XPATH, '//div[text()="Add Existing Location"]')

    def add_new_location(self, address1, city, state, zip_code, address2=None, address3=None):
        add_new_location_btn = BaseElement(self.driver, self._locator_add_new_location_btn)
        add_new_location_btn.click_element()

        policy_title = TitleToolbar(self.driver)
        policy_title.wait_for_screen("Location Information")

        address1_elm = BaseElement(self.driver, self._locator_address1)
        address1_elm.enter_text(address1)

        if address2 is not None:
            address2_elm = BaseElement(self.driver, self._locator_address2)
            address2_elm.enter_text(address2)

        if address3 is not None:
            address3_elm = BaseElement(self.driver, self._locator_address3)
            address3_elm.enter_text(address3)

        city_elm = BaseElement(self.driver, self._locator_input_city)
        city_elm.enter_text(city)

        state_elm = BaseElement(self.driver, self._locator_select_state)
        state_elm.select_option(text=state)

        zip_elm = BaseElement(self.driver, self._locator_input_zip)
        zip_elm.enter_text(zip_code)

        ok_btn = BaseElement(self.driver, self._locator_ok_btn)
        ok_btn.click_element()
        policy_title.wait_for_screen(self.SCREEN_TITLE)

    def add_existing_location(self, index):
        existing_loc_list = BaseElement(self.driver, self._locator_add_existing_location_btn)
        existing_loc_list.select_option(index=index)
        ok_btn = BaseElement(self.driver, self._locator_ok_btn)
        ok_btn.click_element()


class Forms(BasePage):
    log = getLogger()

    def __init__(self, driver):
        super().__init__(driver=driver, url=None)
        self.SCREEN_TITLE = "Forms"

    @property
    def all_form_rows(self):
        locator = (By.XPATH, '//table//tr[1]/following-sibling::tr')
        return BaseElement(self.driver, locator)

    def all_form_list(self):
        """
        :return: list of all forms, where each form is a dictionary contains 'Form#' and 'Description'
        """
        form_details_list = []
        all_form_row_elements = self.all_form_rows.get_all_elements()

        for form_row_element in all_form_row_elements:
            """
            If you start an XPath expression with //, it begins searching from the root of document.
            To search relative to a particular element, you should prepend the expression with '.' instead
            """
            form_number_locator = (By.XPATH, './/div[contains(@id, "FormNumber")]')
            form_description_locator = (By.XPATH, './/div[contains(@id, "Description")]')
            form_number = NestedElement(form_row_element, form_number_locator).get_text()
            form_description = NestedElement(form_row_element, form_description_locator).get_text()

            form_dict = {
                    "Form#": form_number,
                    "Description": form_description,
                }

            form_details_list.append(form_dict)

        return form_details_list


class TransactionBoundScreen(BasePage):
    log = getLogger()

    def __init__(self, driver):
        super().__init__(driver=driver, url=None)

    @property
    def transaction_link_elm(self):
        locator = (By.XPATH, '//div[contains(@id, "ViewJob")]//div[@role="link"]')
        return BaseElement(self.driver, locator)

    @property
    def policy_link_elm(self):
        locator = (By.XPATH, '//div[contains(@id, "ViewPolicy")]//div[@role="link"]')
        return BaseElement(self.driver, locator)

