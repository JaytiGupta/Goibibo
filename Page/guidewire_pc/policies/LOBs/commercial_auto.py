#0001404737 - shubham
# 0000035081 - jayti

import time
from re import sub
from Base.basepage import BasePage
from Base.baseelement import BaseElement
from selenium.webdriver.common.by import By
from Page.guidewire_pc.policies.LOBs import common
from Util.logs import getLogger


class CommercialAuto(BasePage):
    log = getLogger()

    def __init__(self, driver):
        super().__init__(driver=driver, url=None)

        # screens
        self.title_toolbar = common.TitleToolbar(self.driver)
        self.offerings_screen = OfferingsCA(self.driver)
        self.qualification_screen = QualificationCA(self.driver)
        self.policy_info_screen = common.PolicyInfo(self.driver)
        self.comm_auto_line_screen = CommercialAutoLine(self.driver)
        self.location_screen = LocationCA(self.driver)
        self.risk_analysis_screen = common.RiskAnalysis(self.driver)
        self.policy_review_screen = common.PolicyReview(self.driver)
        self.quote_screen = common.Quote(self.driver)
        self.forms_screen = common.Forms(self.driver)
        self.payment_screen = PaymentCA(self.driver)
        self.workspace_screen = common.Workspace(self.driver)


class OfferingsCA:
    log = getLogger()

    def __init__(self, driver):
        self.driver = driver
        self.SCREEN_TITLE = "Offerings"
        self._locator_offering_selection = (By.XPATH, '//div[contains(text(),"Offering Selection")]'
                                                      '/following-sibling::div')

    def select_offering(self, text):
        offering = BaseElement(self.driver, self._locator_offering_selection)
        offering.select_option(text=text)


class QualificationCA:
    log = getLogger()

    def __init__(self, driver):
        self.driver = driver
        self.SCREEN_TITLE = "Qualification"
        self.table_questionnaires = common.TableQuestionnaires(self.driver)


class CommercialAutoLine:
    log = getLogger()

    def __init__(self, driver):
        self.driver = driver
        self.SCREEN_TITLE = "Commercial Auto Line"
        self._locator_product = (By.XPATH, '//div[text()="Product"]/following-sibling::div')
        self._locator_fleet = (By.XPATH, '//div[text()="Fleet"]/following-sibling::div')
        self._locator_state = (By.XPATH, '//select[contains(@name,"SelectStateHiredAuto")]')
        self._locator_add_state_btn = (By.XPATH, '//div[contains(text(),"Add State")]')
        self._locator_state_no_of_emp = (By.XPATH, '//input[contains(@name,"NumEmployees")]')
        self._locator_state_total_partners = (By.XPATH, '//input[contains(@name,"TotalPartners")]')
        self._locator_state_total_volunteers = (By.XPATH, '//input[contains(@name,"TotalVolunteers")]')
        self._locator_non_owned_auto = (By.XPATH, '//input[contains(@aria-label,"Non-Owned")]')

    def hired_auto_coverages(self, coverage):
        _locator_hired_auto_covg = (By.XPATH, f'//input[contains(@aria-label,f{coverage})]')
        coverage = BaseElement(self.driver, _locator_hired_auto_covg)
        return coverage

    def hired_auto_state(self, text, emp_no, partners, volunteers):
        state = BaseElement(self.driver, self._locator_state)
        state.select_option(text=text)
        add_state = BaseElement(self.driver, self._locator_add_state_btn)
        add_state.click_element()
        no_of_emp = BaseElement(self.driver, self._locator_state_no_of_emp)
        no_of_emp.enter_text(self, emp_no)
        total_partners = BaseElement(self.driver, self._locator_state_total_partners)
        total_partners.enter_text(self, partners)
        total_volunteers = BaseElement(self.driver, self._locator_state_total_volunteers)
        total_volunteers.enter_text(self, volunteers)

    def non_owned_auto_covg(self):
        non_owned = BaseElement(self.driver, self._locator_non_owned_auto)
        non_owned.click_element()

#non-owned auto state
