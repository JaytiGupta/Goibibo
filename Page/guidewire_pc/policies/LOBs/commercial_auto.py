#0001404737 - shubham
# 0000035081 - jayti

import time
from re import sub
from Base.basepage import BasePage
from Base.baseelement import BaseElement
from selenium.webdriver.common.by import By
from Page.guidewire_pc.policies.LOBs import common
from Util.logs import getLogger
from Util import random_data


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
        self.location_screen = Location(self.driver)
        self.vehicles_screen = Vehicles(self.driver)
        self.state_info_screen = StateInfo(self.driver)
        self.drivers_screen = Drivers(self.driver)
        self.covered_vehicles_screen = CoveredVehicles(self.driver)
        self.risk_analysis_screen = common.RiskAnalysis(self.driver)
        self.policy_review_screen = common.PolicyReview(self.driver)
        self.quote_screen = common.Quote(self.driver)
        self.forms_screen = common.Forms(self.driver)
        # self.payment_screen = Payment(self.driver)
        self.workspace_screen = common.Workspace(self.driver)
        self.sidebar = common.Sidebar(self.driver)


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
        self.log.info("Offering selected")


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
        self._locator_liability_covg_text = (By.XPATH, '//div[@aria-label="Liability"]//div[text()="Liability"]')
        self._locator_hired_auto_select_state = (By.XPATH, '//select[contains(@name,"SelectStateHiredAuto")]')
        self._locator_hired_auto_add_state_btn = (By.XPATH, '//div[text() = "dd State"]')
        self._locator_hired_auto_cost_of_hire = (By.XPATH, '//input[contains(@name,"CostHire")]')
        self._locator_non_owned_auto_select_state = (By.XPATH, '//select[contains(@name,"SelectStateNonowned")]')
        self._locator_non_owned_auto_add_state_btn = (By.XPATH, '//div[text()="Non-owned Liability States"]'
                                                                '/following-sibling::div//div[text()="Add State"]')
        self._locator_non_owned_auto_state_no_of_emp = (By.XPATH, '//input[contains(@name,"NumEmployees")]')
        self._locator_non_owned_auto_state_total_partners = (By.XPATH, '//input[contains(@name,"TotalPartners")]')
        self._locator_non_owned_auto_state_total_volunteers = (By.XPATH, '//input[contains(@name,"TotalVolunteers")]')
        self._locator_non_owned_auto_checkbox = (By.XPATH, '//input[contains(@aria-label,"Non-Owned")]')

    def ca_coverages(self, product, fleet):
        product_elm = BaseElement(self.driver, self._locator_product)
        product_elm.select_option(text=product)
        fleet_elm = BaseElement(self.driver, self._locator_fleet)
        fleet_elm.select_option(text=fleet)

    # def wait_liability_covg(self):
    #     liability_text = BaseElement(self.driver, self._locator_liability_covg_text)
    #     liability_text.wait_till_text_to_be_present_in_element("Liability")

    def add_hired_auto_coverages(self, coverage):
        _locator_hired_auto_covg = (By.XPATH, f'//input[contains(@aria-label,"{coverage}")]')
        coverage_elm = BaseElement(self.driver, _locator_hired_auto_covg)
        coverage_elm.click_element()
        self.log.info(f"'{coverage}' coverage selected under the Hired Auto coverage section")
        return None

    def add_hired_auto_state(self, cost_of_hire, state):
        hired_state = BaseElement(self.driver, self._locator_hired_auto_select_state)
        hired_state.select_option(text=state)
        add_state = BaseElement(self.driver, self._locator_hired_auto_add_state_btn)
        add_state.click_element()

        def new_row(row_number):
            locator = (By.XPATH, f'//div[contains(@id,"HiredAutoLVInput")]//table//tr[{row_number + 1}]')
            return BaseElement(self.driver, locator)

        new_row(1).wait_till_text_to_be_present_in_attribute("role", "row")

        cost_of_hire_elm = BaseElement(self.driver, self._locator_hired_auto_cost_of_hire)
        cost_of_hire_elm.enter_text(cost_of_hire)
        self.log.info(f"Details for the selected state {state} entered - under the Hired Auto coverage section")

    def add_non_owned_auto_covg(self):
        non_owned = BaseElement(self.driver, self._locator_non_owned_auto_checkbox)
        non_owned.click_element()
        self.log.info("Non Owned Auto coverage selected")
        return None

    def add_non_owned_auto_state(self, emp_no, partners, volunteers, state):
        non_owned_state = BaseElement(self.driver, self._locator_non_owned_auto_select_state)
        non_owned_state.select_option(text=state)
        add_state = BaseElement(self.driver, self._locator_non_owned_auto_add_state_btn)
        add_state.click_element()

        def new_row(row_number):
            locator = (By.XPATH, f'//div[contains(@id,"NonownedLVInput")]//table//tr[{row_number + 1}]')
            return BaseElement(self.driver, locator)

        new_row(1).wait_till_text_to_be_present_in_attribute("role", "row")

        no_of_emp = BaseElement(self.driver, self._locator_non_owned_auto_state_no_of_emp)
        no_of_emp.enter_text(emp_no)
        total_partners = BaseElement(self.driver, self._locator_non_owned_auto_state_total_partners)
        total_partners.enter_text(partners)
        total_volunteers = BaseElement(self.driver, self._locator_non_owned_auto_state_total_volunteers)
        total_volunteers.enter_text(volunteers)
        self.log.info(f"Details for the selected state {state} entered - under the Non Owned Auto coverage section")


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
        self._locator_class_code_radius = (By.XPATH, '//div[text()="Radius"]/following-sibling::div//select')
        self._locator_class_code_screen_search = (By.XPATH, '//div[contains(@id,"VehicleClassCodeSearchDV'
                                                            '-SearchAndResetInputSet-SearchLinksInputSet-Search")]')
        self._locator_class_code_first_result = (By.XPATH, '//tr[contains(@id,"VehicleClassCodeSearch'
                                                           'ResultsLV-0-0")]/child::td[contains(@id,'
                                                           '"VehicleClassCodeSearchResultsLV-0-1")]')
        self._locator_vehicle_ok_btn = (By.XPATH, '//div[@aria-label = "OK"]')

    def add_vehicle(self, garage_location, type_of_vehicle, vehicle_cost):
        add_vehicle_btn = BaseElement(self.driver, self._locator_create_vehicle_btn)
        add_vehicle_btn.click_element()
        garaged_location = BaseElement(self.driver, self._locator_garaged_location)
        garaged_location.select_option(index=garage_location)
        vehicle_type = BaseElement(self.driver, self._locator_vehicle_type)
        vehicle_type.select_option(text=type_of_vehicle)
        cost = BaseElement(self.driver, self._locator_cost)
        cost.enter_text(vehicle_cost)
        vin_elm = BaseElement(self.driver, self._locator_vin)
        vin = random_data.random_VIN()
        vin_elm.enter_text(vin)
        self.log.info(f"Vehicle type {type_of_vehicle} added on the Vehicles screen "
                      f"for the Location {garage_location}")

    def vehicle_class_code(self, radius):
        search_class_code = BaseElement(self.driver, self._locator_class_code_search_btn)
        search_class_code.click_element()
        # years_of_experience_elm = BaseElement(self.driver, self._locator_class_code_experience)
        # years_of_experience_elm.select_option(text=years_of_experience)
        radius_elm = BaseElement(self.driver, self._locator_class_code_radius)
        radius_elm.select_option(text=radius)
        screen_search_btn = BaseElement(self.driver, self._locator_class_code_screen_search)
        screen_search_btn.click_element()
        result = BaseElement(self.driver, self._locator_class_code_first_result)
        result.click_element()
        ok_btn = BaseElement(self.driver, self._locator_vehicle_ok_btn)
        ok_btn.click_element()
        self.log.info("Class code for the entered vehicle is selected")


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

    def uninsured_motorist_bodily_injury(self, bodily_injury_package):
        bodily_injury = BaseElement(self.driver, self._locator_uninsured_bodily_injury)
        bodily_injury.select_option(value=bodily_injury_package)
        self.log.info(f"Bodily Injury package {bodily_injury_package} is selected for the "
                      f"Uninsured Motorist coverage")

    def uninsured_motorist_property_damage(self, property_damage_limit):
        property_damage = BaseElement(self.driver, self._locator_uninsured_prop_damage)
        property_damage.select_option(value=property_damage_limit)
        self.log.info(f"Property Damage Limit {property_damage_limit} is selected for the "
                      f"Uninsured Motorist coverage")


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
                                              'DateOfBirth"]//input')
        self._locator_driver_license_number = (By.XPATH, '//input[contains(@name, "BADriversDV-LicenseNumber")]')
        self._locator_driver_license_state = (By.XPATH, '//select[contains(@name, "BADriversDV-LicenseState")]')
        self._locator_driver_details_ok_btn = (By.XPATH, '//div[@aria-label = "OK"]')

    def driver_details(self, fn, ln, driver_gender, dob, license_state):
        add_driver_btn = BaseElement(self.driver, self._locator_add_driver_btn)
        add_driver_btn.click_element()
        first_name = BaseElement(self.driver, self._locator_driver_first_name)
        first_name.enter_text(fn)
        last_name = BaseElement(self.driver, self._locator_driver_last_name)
        last_name.enter_text(ln)
        gender = BaseElement(self.driver, self._locator_driver_gender)
        gender.select_option(text=driver_gender)
        license_number_elm = BaseElement(self.driver, self._locator_driver_license_number)
        lic = random_data.random_license()
        license_number_elm.enter_text(lic)
        birth_date = BaseElement(self.driver, self._locator_driver_dob)
        birth_date.click_element()
        birth_date.enter_text(dob)
        license_state_elm = BaseElement(self.driver, self._locator_driver_license_state)
        license_state_elm.select_option(text=license_state)
        ok_btn = BaseElement(self.driver, self._locator_driver_details_ok_btn)
        ok_btn.click_element()
        self.log.info("Driver details are entered")


class CoveredVehicles:

    log = getLogger()

    def __init__(self, driver):
        self.driver = driver

    def edit_covered_vehicles(self):
        self.log.info("Details of the Covered Vehicle are not updated")
        return None


class Location(common.Location):
    log = getLogger()

    def __init__(self, driver):
        super().__init__(driver=driver)
        self._locator_autofill_territory_code_btn = (By.XPATH, '//div[text() = "Autofill Territory Codes"]')

        # locate only when value is filled in input box
        self._locator_territory_input_box = (By.XPATH, '//div[text()="Territory Code for Commercial Auto Line"]/'
                                                          'following-sibling::div//input')

    def add_new_location(self, address1, city, state, zip_code, address2=None, address3=None):
        add_new_location_btn = BaseElement(self.driver, self._locator_add_new_location_btn)
        add_new_location_btn.click_element()

        policy_title = common.TitleToolbar(self.driver)
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

        territory_code_btn = BaseElement(self.driver, self._locator_autofill_territory_code_btn)
        territory_code_btn.click_element()

        territory_input_box = BaseElement(self.driver, self._locator_territory_input_box)
        # Wait until the element's value attribute has any text present
        territory_input_box.wait_till_text_to_be_present_in_value("322")

        self.log.info(f"Page: Locations - new location added. {address1}, {city}, {state}, {zip_code}.")

        ok_btn = BaseElement(self.driver, self._locator_ok_btn)
        ok_btn.click_element()
        policy_title.wait_for_screen(self.SCREEN_TITLE)
