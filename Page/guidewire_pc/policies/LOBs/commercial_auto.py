#0001404737 - shubham
# 0000035081 - jayti

import time
from re import sub
from Base.basepage import BasePage
from Base.baseelement import BaseElement
from selenium.webdriver.common.by import By
from Page.guidewire_pc.policies.LOBs import common
from Util.logs import getLogger
from Util import random_vin
from Util import random_license


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
        # self.payment_screen = Payment(self.driver)
        self.workspace_screen = common.Workspace(self.driver)


class Offerings:
    log = getLogger()

    def __init__(self, driver):
        self.driver = driver
        self.SCREEN_TITLE = "Offerings"
        self._locator_offering_selection = (By.XPATH, '//select[@name="SubmissionWizard-OfferingScreen'
                                                      '-OfferingSelection"]')

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
        self._locator_product = (By.XPATH, '//select[contains(@name,"BALineDV-PolicyType")]')
        self._locator_fleet = (By.XPATH, '//select[contains(@name,"BALineDV-Fleet")]')
        self._locator_hired_auto_select_state = (By.XPATH, '//select[contains(@name,"SelectStateHiredAuto")]')
        self._locator_hired_auto_add_state_btn = (By.XPATH, '//div[text() = "dd State")]')
        self._locator_hired_auto_cost_of_hire = (By.XPATH, '//input[contains(@name,"CostHire")]')
        self._locator_non_owned_auto_select_state = (By.XPATH, '//select[contains(@name,"SelectStateNonowned")]')
        self._locator_non_owned_auto_add_state_btn = (By.XPATH, '//div[text() = "Add State")]')
        self._locator_non_owned_auto_state_no_of_emp = (By.XPATH, '//input[contains(@name,"NumEmployees")]')
        self._locator_non_owned_auto_state_total_partners = (By.XPATH, '//input[contains(@name,"TotalPartners")]')
        self._locator_non_owned_auto_state_total_volunteers = (By.XPATH, '//input[contains(@name,"TotalVolunteers")]')
        self._locator_non_owned_auto_checkbox = (By.XPATH, '//input[contains(@aria-label,"Non-Owned")]')

    def ca_coverages(self, text, text1):
        product = BaseElement(self.driver, self._locator_product)
        product.select_option(text=text)
        fleet = BaseElement(self.driver, self._locator_fleet)
        fleet.select_option(text=text1)

    def hired_auto_coverages(self, coverage):
        _locator_hired_auto_covg = (By.XPATH, f'//input[contains(@aria-label,f{coverage})]')
        coverage = BaseElement(self.driver, _locator_hired_auto_covg)
        return coverage

    def hired_auto_state(self, cost_of_hire, state):
        hired_state = BaseElement(self.driver, self._locator_hired_auto_select_state)
        hired_state.select_option(text=state)
        add_state = BaseElement(self.driver, self._locator_hired_auto_add_state_btn)
        add_state.click_element()
        cost_of_hire_elm = BaseElement(self.driver, self._locator_hired_auto_cost_of_hire)
        cost_of_hire_elm.enter_text(cost_of_hire)

    def non_owned_auto_covg(self):
        non_owned = BaseElement(self.driver, self._locator_non_owned_auto_checkbox)
        non_owned.click_element()

    def non_owned_auto_state(self, emp_no, partners, volunteers, text):
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
        vin_elm = BaseElement(self.driver, self._locator_vin)
        vin_elm.enter_text(random_vin.get_one_vin())

    def vehicle_class_code(self, years_of_experience, radius):
        search_class_code = BaseElement(self.driver, self._locator_class_code_search_btn)
        search_class_code.click_element()
        years_of_experience_elm = BaseElement(self.driver, self._locator_class_code_experience)
        years_of_experience_elm.select_option(text=years_of_experience)
        radius_elm = BaseElement(self.driver, self._locator_class_code_radius)
        radius_elm.select_option(text=radius)
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
        self._locator_add_driver_btn = (By.XPATH, '//div[text()="Add Driver"]')
        self._locator_driver_first_name = (By.XPATH, '//input[contains(@name, "BADriversDV-'
                                                     'GlobalPersonNameInputSet-FirstName")]')
        self._locator_driver_last_name = (By.XPATH, '//input[contains(@name, "BADriversDV-'
                                                    'GlobalPersonNameInputSet-LastName")]')
        self._locator_driver_gender = (By.XPATH, '//select[contains(@name, "BADriversDV-Gender")]')
        self._locator_driver_dob = (By.XPATH, '//div[@id="BADriverPopup-BADriverScreen-BADriversDV-'
                                              'DateOfBirth"]')
        self._locator_driver_license_number = (By.XPATH, '//input[contains(@name, "BADriversDV-LicenseNumber")]')
        self._locator_driver_license_state = (By.XPATH, '//select[contains(@name, "BADriversDV-LicenseState")]')
        self._locator_driver_details_ok_btn = (By.XPATH, '//div[@aria-label = "OK"]')

    def driver_details(self, fn, ln, value, dob, text):
        first_name = BaseElement(self.driver, self._locator_driver_first_name)
        first_name.enter_text(fn)
        last_name = BaseElement(self.driver, self._locator_driver_last_name)
        last_name.enter_text(ln)
        gender = BaseElement(self.driver, self._locator_driver_gender)
        gender.select_option(value=value)
        birth_date = BaseElement(self.driver, self._locator_driver_dob)
        birth_date.enter_text(dob)
        license_number_elm = BaseElement(self.driver, self._locator_driver_dob)
        license_number_elm.enter_text(random_license.get_one_license())
        license_state_elm = BaseElement(self.driver, self._locator_driver_license_state)
        license_state_elm.select_option(text=text)
        ok_btn = BaseElement(self.driver, self._locator_driver_details_ok_btn)
        ok_btn.click_element()





