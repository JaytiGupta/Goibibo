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
        self.offerings_screen = Offerings(self.driver)
        self.qualification_screen = Qualification(self.driver)
        self.policy_info_screen = common.PolicyInfo(self.driver)
        self.comm_auto_line_screen = CommercialAutoLine(self.driver)
        self.location_screen = common.Location(self.driver)
        self.vehicles_screen = Vehicles(self.driver)
        self.state_info_screen = StateInfo(self.driver)
        self.drivers_screen = Drivers(self.driver)
        self.risk_analysis_screen = common.RiskAnalysis(self.driver)
        self.policy_review_screen = common.PolicyReview(self.driver)
        self.quote_screen = common.Quote(self.driver)
        self.forms_screen = common.Forms(self.driver)
        # self.payment_screen = PaymentCA(self.driver)
        self.workspace_screen = common.Workspace(self.driver)


class Offerings:
    log = getLogger()

    def __init__(self, driver):
        self.driver = driver
        self.SCREEN_TITLE = "Offerings"
        self._locator_offering_selection = (By.XPATH, '//div[contains(text(),"Offering Selection")]'
                                                      '/following-sibling::div')

    def select_offering(self, text):
        offering = BaseElement(self.driver, self._locator_offering_selection)
        offering.select_option(text=text)


class Qualification:
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
        self._locator_hired_auto_select_state = (By.XPATH, '//select[contains(@name,"SelectStateHiredAuto")]')
        self._locator_hired_auto_add_state_btn = (By.XPATH, '//div[text() = "dd State")]')
        self._locator_hired_auto_cost_of_hire = (By.XPATH, '//input[contains(@name,"CostHire")]')
        self._locator_non_owned_auto_select_state = (By.XPATH, '//select[contains(@name,"SelectStateNonowned")]')
        self._locator_non_owned_auto_add_state_btn = (By.XPATH, '//div[text() = "Add State")]')
        self._locator_non_owned_auto_state_no_of_emp = (By.XPATH, '//input[contains(@name,"NumEmployees")]')
        self._locator_non_owned_auto_state_total_partners = (By.XPATH, '//input[contains(@name,"TotalPartners")]')
        self._locator_non_owned_auto_state_total_volunteers = (By.XPATH, '//input[contains(@name,"TotalVolunteers")]')
        self._locator_non_owned_auto_checkbox = (By.XPATH, '//input[contains(@aria-label,"Non-Owned")]')

    def hired_auto_coverages(self, coverage):
        _locator_hired_auto_covg = (By.XPATH, f'//input[contains(@aria-label,f{coverage})]')
        coverage = BaseElement(self.driver, _locator_hired_auto_covg)
        return coverage

    def hired_auto_state(self, text, cost_of_hire):
        hired_state = BaseElement(self.driver, self._locator_hired_auto_select_state)
        hired_state.enter_text(text)
        cost_of_hire_elm = BaseElement(self.driver, self._locator_hired_auto_cost_of_hire)
        cost_of_hire_elm.enter_text(cost_of_hire)

    def non_owned_auto_covg(self):
        non_owned = BaseElement(self.driver, self._locator_non_owned_auto_checkbox)
        non_owned.click_element()

    def non_owned_auto_state(self, text, emp_no, partners, volunteers):
        non_owned_state = BaseElement(self.driver, self._locator_non_owned_auto_select_state)
        non_owned_state.select_option(text=text)
        add_state = BaseElement(self.driver, self._locator_non_owned_auto_add_state_btn)
        add_state.click_element()
        no_of_emp = BaseElement(self.driver, self._locator_non_owned_auto_state_no_of_emp)
        no_of_emp.enter_text(emp_no)
        total_partners = BaseElement(self.driver, self._locator_non_owned_auto_state_total_partners)
        total_partners.enter_text(partners)
        total_volunteers = BaseElement(self.driver, self._locator_non_owned_auto_state_total_volunteers)
        total_volunteers.enter_text(volunteers)


class Vehicles:

    log = getLogger()

    def __init__(self, driver):
        self.driver = driver
        self.SCREEN_TITLE = "Vehicles"
        self._locator_create_vehicle_btn = (By.XPATH, '//div[@aria-label = "Create Vehicle"]')
        self._locator_garaged_location = (By.XPATH, '//select[contains(@name,"GarageLocationInput")]')
        self._locator_vehicle_type = (By.XPATH, '//select[contains(@name,"VehicleDV-Type")]')
        self._locator_vin = (By.XPATH, '//input[contains(@name,"VehicleDV-Vin")]')
        self._locator_cost = (By.XPATH, '//input[contains(@name,"VehicleDV-Cost")]')
        self._locator_class_code_search_btn = (By.XPATH, '//div[contains(@id,"VehicleDV-ClassCode'
                                                         '-SelectClassCode")]')
        self._locator_class_code_experience = (By.XPATH, '//select[contains(@name,"VehicleClassCodeSearchDV'
                                                         '-YearsExperience")]')
        self._locator_class_code_radius = (By.XPATH, '//select[contains(@name,"VehicleClassCodeSearchDV'
                                                     '-Radius")]')
        self._locator_class_code_screen_search = (By.XPATH, '//div[contains(@id,"VehicleClassCodeSearchDV'
                                                            '-SearchAndResetInputSet-SearchLinksInputSet-Search")]')
        self._locator_class_code_first_result = (By.XPATH, '//tr[contains(@id,"VehicleClassCodeSearch'
                                                           'ResultsLV-0-0")]/child::td[contains(@id,'
                                                           '"VehicleClassCodeSearchResultsLV-0-1")]')
        self._locator_vehicle_ok_btn = (By.XPATH, '//div[@aria-label = "OK"]')

    def add_vehicle(self, index, text, vin):
        add_vehicle_btn = BaseElement(self.driver, self._locator_create_vehicle_btn)
        add_vehicle_btn.click_element()
        garaged_location = BaseElement(self.driver, self._locator_garaged_location)
        garaged_location.select_option(index=index)
        vehicle_type = BaseElement(self.driver, self._locator_vehicle_type)
        vehicle_type.select_option(text=text)
        vin = BaseElement(self.driver, self._locator_vin)
        vin.enter_text(vin) #TODO random vin enteries

    def vehicle_class_code(self,exp, rad):
        search_class_code = BaseElement(self.driver, self._locator_class_code_search_btn)
        search_class_code.click_element()
        years_of_exp = BaseElement(self.driver, self._locator_class_code_experience)
        years_of_exp.select_option(text=exp)
        radius = BaseElement(self.driver, self._locator_class_code_radius)
        radius.select_option(text=rad)
        screen_search_btn = BaseElement(self.driver, self._locator_class_code_screen_search)
        screen_search_btn.click_element()
        result = BaseElement(self.driver, self._locator_class_code_first_result)
        result.click_element()
        ok_btn = BaseElement(self.driver, self._locator_vehicle_ok_btn)
        ok_btn.click_element()


class StateInfo:

    log = getLogger()

    def __init__(self, driver):
        self.driver = driver
        self._locator_uninsured_bodily_injury = (By.XPATH, '//select[contains(@name,"BAStateInfoScreen-'
                                                           'BAStateCoveragesPanelSet-BAPVehicleStateGrp'
                                                           'Iterator-0")]')
        self._locator_uninsured_prop_damage = (By.XPATH, '//select[contains(@name,"BAStateInfoScreen-'
                                                         'BAStateCoveragesPanelSet-BAPVehicleStateGrp'
                                                         'Iterator-1")]')

    def uninsured_motorist_bodily_injury(self, value):
        bodily_injury = BaseElement(self.driver, self._locator_uninsured_bodily_injury)
        bodily_injury.select_option(value=value)

    def uninsured_motorist_property_damage(self, value):
        property_damage = BaseElement(self.driver, self._locator_uninsured_prop_damage)
        property_damage.select_option(value=value)


class Drivers:

    log = getLogger()

    def __init__(self, driver):
        self.driver = driver



