import time
from re import sub
from Base.basepage import BasePage
from Base.baseelement import BaseElement
from selenium.webdriver.common.by import By
from Page.guidewire_pc.policies.LOBs import common
from Util.logs import getLogger


class WorkersCompensation(BasePage):
    log = getLogger()

    def __init__(self, driver):
        super().__init__(driver=driver, url=None)

        # Title Toolbar locators
        # self._locator_screen_title = (By.XPATH, '//div[@id="gw-center-title-toolbar"]//div[@role="heading"]')
        # self._locator_Next_btn = (By.XPATH, '//div[@id="gw-center-title-toolbar"]//div[text()="Next"]')
        # self._locator_Back_btn = (By.XPATH, '//div[@id="gw-center-title-toolbar"]//div[text()="Back"]')
        # self._locator_Quote_btn = (By.XPATH, '//div[@id="gw-center-title-toolbar"]//div[@aria-label="Quote"]')
        # self._locator_SaveDraft_btn = (By.XPATH, '//div[@id="gw-center-title-toolbar"]//div[@aria-label="Save Draft"]')
        # self._locator_CloseOption_btn = (By.XPATH, '//div[@id="gw-center-title-toolbar"]//div[@aria-label="Close Options"]')
        # self._locator_BindOptions_btn = (By.XPATH, '//div[@id="gw-center-title-toolbar"]//div[@aria-label="Bind Options"]')
        # self._locator_BindOptions_BindOnly_btn = (By.XPATH, '//div[@id="gw-center-title-toolbar"]//div[@aria-label="Bind Only"]')
        # self._locator_BindOptions_IssuePolicy_btn = (By.XPATH, '//div[@id="gw-center-title-toolbar"]//div[@aria-label="Issue Policy"]')
        # self._locator_details_btn = (By.XPATH, '//div[@id="gw-center-title-toolbar"]//div[text()="Details"]')

        # Workspace
        # self._locator_validation_results = (By.XPATH, '//div[text()="Validation Results"]')
        # self._locator_error = (By.XPATH, '//div[@id="gw-south-panel"]//div[contains(text(),"Error")]')
        # self._locator_warning = (By.XPATH, '//div[@id="gw-south-panel"]//div[contains(text(),"Warning")]')
        # screens
        self.title_toolbar = common.TitleToolbar(self.driver)
        self.qualification_screen = Qualification(self.driver)
        self.policy_info_screen = PolicyInfo(self.driver)
        self.location_screen = Location(self.driver)
        self.wc_coverages_screen = WCCoverages(self.driver)
        self.supplement_screen = Supplemental(self.driver)
        self.wc_options_screen = WCOptions(self.driver)
        self.risk_analysis_screen = common.RiskAnalysis(self.driver)
        self.policy_review_screen = common.PolicyReview(self.driver)
        self.quote_screen = common.Quote(self.driver)
        self.forms_screen = common.Forms(self.driver)
        self.payment_screen = Payment(self.driver)
        self.workspace_screen = common.Workspace(self.driver)

    # Title Toolbar
    # def next(self):
    #     # old_title = self.get_title()
    #
    #     next_btn = BaseElement(self.driver, self._locator_Next_btn)
    #     next_btn.click_element()
    #
        # waiting till next screen load
        # max_wait_time = 10
        # t_end = time.time() + max_wait_time
        # while time.time() < t_end:
        #     new_title = self.get_title()
        #     if old_title != new_title:
        #         self.log.info(f"Clicked Next button at {old_title[61:]} screen. "
        #                       f"Navigated to {new_title[61:]} screen.")
        #         break
    #
    # def quote(self): # TODO needs to update max depth for recursion
    #     initial_screen_title = self.screen_title()
    #
    #     self.log.info(f"{initial_screen_title} screen")
    #     quote_btn = BaseElement(self.driver, self._locator_Quote_btn)
    #     quote_btn.click_element()
    #     self.log.info("Clicked Quote button.")
    #
    #     # TODO: update need to wait for page after click, screen can be same, pre_quote or quote
    #     time.sleep(5)
    #
    #     if self.screen_title() == self.quote_screen.SCREEN_TITLE:
    #         self.log.info("Quoted successfully")
    #     elif self.screen_title() == "Pre-Quote Issues":
    #         self.log.info("Pre-Quote Issues screen")
    #         details_btn = BaseElement(self.driver, self._locator_details_btn)
    #         details_btn.click_element()
    #         self.log.debug("Navigate to Underwriter issues tab at Risk Analysis screen.")
    #         self.risk_analysis_screen.approve_all_uw_issues()
    #         self.log.debug("All underwriter issues approved.")
    #         self.wait_for_screen("Risk Analysis")
    #         self.quote()
    #     elif self.screen_title() == initial_screen_title:
    #         self.log.info(f"{initial_screen_title} screen")
    #         workspace_error = BaseElement(self.driver, self._locator_error)
    #         workspace_warning = BaseElement(self.driver, self._locator_warning)
    #         if workspace_error.is_element_present():
    #             self.log.debug("Getting error and unable to quote")
    #             raise Exception("Getting error and unable to quote")
    #         elif workspace_warning.is_element_present():
    #             self.log.info("Getting warnings")
    #         # TODO elif Information
    #         self.quote()
    #
    # def screen_title(self):
    #     screen_title_elm = BaseElement(self.driver, self._locator_screen_title)
    #     return screen_title_elm.get_text()
    #
    # def wait_for_screen(self, screen_title_text):
    #     screen_title_elm = BaseElement(self.driver, self._locator_screen_title)
    #     screen_title_elm.wait_till_text_to_be_present_in_element(screen_title_text)
    #
    # def bind_policy(self):
    #     bind_option_btn_elm = BaseElement(self.driver, self._locator_BindOptions_btn)
    #     bind_option_btn_elm.click_element()
    #     bind_only_btn_elm = BaseElement(self.driver, self._locator_BindOptions_BindOnly_btn)
    #     bind_only_btn_elm.click_element()
    #     self.log.info(f"Clicked Bind Only button.")
    #
    # def issue_policy(self):
    #     initial_screen_title = self.screen_title()
    #
    #     bind_option_btn_elm = BaseElement(self.driver, self._locator_BindOptions_btn)
    #     bind_option_btn_elm.click_element()
    #     issue_policy_elm = BaseElement(self.driver, self._locator_BindOptions_IssuePolicy_btn)
    #     issue_policy_elm.click_element()
    #     self.log.info(f"Clicked Issue Policy button.")
    #     self.accept_alert()
    #
    #     # TODO: update need to wait for page after click, screen can be same, pre_quote or quote
    #     time.sleep(5)
    #
    #     if self.screen_title() == "Submission Bound":
    #         self.log.info("Your Submission has been bound")
    #     elif self.screen_title() == initial_screen_title:
    #         self.log.info(f"{initial_screen_title} screen")
    #         workspace_error = BaseElement(self.driver, self._locator_error)
    #         workspace_warning = BaseElement(self.driver, self._locator_warning)
    #         if workspace_error.is_element_present():
    #             self.log.debug("Getting error and unable to quote")
    #             raise Exception("Getting error and unable to quote")
    #         elif workspace_warning.is_element_present():
    #             self.log.info("Getting warnings")
    #         self.issue_policy()


class Qualification:
    log = getLogger()

    def __init__(self, driver):
        self.driver = driver
        self.SCREEN_TITLE = "Qualification"
        self.table_questionnaires = common.TableQuestionnaires(self.driver)


class PolicyInfo(BasePage):
    log = getLogger()

    def __init__(self, driver):
        super().__init__(driver=driver, url=None)
        self.SCREEN_TITLE = "Policy Info"
        self._locator_FEIN_input_box = (By.XPATH, '//div[text()="FEIN"]/parent::div//input')
        self._locator_industry_code_input_box = (By.XPATH, '//div[text()="Industry Code"]/parent::div//input')
        self._locator_year_business_started_input_box = (
            By.XPATH, '//div[text()="Year Business Started"]/parent::div//input')
        self._locator_organization_type_dropdown = (By.XPATH, '//div[text()="Organization Type"]/parent::div//select')
        self._locator_term_type_dropdown = (By.XPATH, '//div[text()="Term Type"]/parent::div//select')
        self._locator_effective_date_input_box = (By.XPATH, '//div[text()="Effective Date"]/parent::div//input')
        self._locator_underwriter_companies_dropdown = (By.XPATH, '//select[contains(@name, "UWCompanyInputSet")]')

    def input_FEIN(self, text):
        fein = BaseElement(self.driver, self._locator_FEIN_input_box)
        fein.enter_text(text)  # text must be 9-digit no.
        self.log.info(f"Enter FEIN - {text}")

    def industry_code_input(self, industry_code):
        industry_code_elm = BaseElement(self.driver, self._locator_industry_code_input_box)
        industry_code_elm.enter_text(industry_code)
        self.log.info(f"Enter Industry Code - {industry_code}")

    def select_org_type(self, type_of_org):
        org_type_elm = BaseElement(self.driver, self._locator_organization_type_dropdown)
        org_type_elm.select_option(text=type_of_org)
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

    def add_new_location(self, address1, city, state, zip_code, address2=None, address3=None):
        add_new_location_btn = BaseElement(self.driver, self._locator_add_new_location_btn)
        add_new_location_btn.click_element()

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

        self.log.info(f"Page: Locations - new location added. {address1}, {city}, {state}, {zip_code}.")

        ok_btn = BaseElement(self.driver, self._locator_ok_btn)
        ok_btn.click_element()


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
        governing_law_xpath = f'//div[text()="Class Code"]/ancestor::tr/following-sibling::tr[{row_number}]/td[2]//select'  # Govering law
        location_xpath = f'//div[text()="Class Code"]/ancestor::tr/following-sibling::tr[{row_number}]/td[3]//select'  # Location
        class_code_xpath = f'//div[text()="Class Code"]/ancestor::tr/following-sibling::tr[{row_number}]/td[4]//input'  # class code
        employees_xpath = f'//div[text()="Class Code"]/ancestor::tr/following-sibling::tr[{row_number}]/td[6]//input'  # Employees
        basis_xpath = f'//div[text()="Class Code"]/ancestor::tr/following-sibling::tr[{row_number}]/td[8]//input'  # Basis

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


class Supplemental(BasePage):
    log = getLogger()

    def __init__(self, driver):
        super().__init__(driver=driver, url=None)
        self.table_questionnaires = common.TableQuestionnaires(self.driver)


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
                f'/parent::div/following-sibling::div[2]//div[contains(text(),{wc_option_name})]'
        return By.XPATH, xpath

    def add_wc_option(self, option):
        add_option_btn = BaseElement(self.driver, self._locator_add_option_btn)
        add_option_btn.click_element()
        select_option = BaseElement(self.driver, self._locator_dynamic_wc_options_selection(option))
        select_option.click_element()

    def add_federal_class(self, location_index, class_code, emp_no, basis_value):
        add_class_btn = BaseElement(self.driver, self._locator_add_federal_class)
        add_class_btn.click_element()
        location = BaseElement(self.driver, self._locator_federal_location_dropdown)
        location.select_option(index=location_index)
        class_code_elm = BaseElement(self.driver, self._locator_federal_class_code_input_box)
        class_code_elm.enter_text(class_code)
        emp = BaseElement(self.driver, self._locator_federal_no_of_emp_input_box)
        emp.enter_text(emp_no)
        basis = BaseElement(self.driver, self._locator_federal_basis_input_box)
        basis.enter_text(basis_value)


# class RiskAnalysis(BasePage):
#     log = getLogger()
#
#     def __init__(self, driver):
#         super().__init__(driver=driver, url=None)
#         self.SCREEN_TITLE = "Risk Analysis"
#         self._locator_all_pending_approval_check_box = (
#             By.XPATH, '//div[text()="Approve"]/ancestor::td[not(contains(@colspan,"1"))]'
#                       '/preceding-sibling::td[4]//input[@type="checkbox"]')
#         self._locator_header_approve_btn = (By.XPATH, '//div[@class="gw-ListView--UI-left"]'
#                                                        '//div[text()="Approve"]')
#
#         # Screen: Risk Approval Details
#         self._locator_ok_btn = (By.XPATH, '//div[@role="button"]//div[@aria-label="OK"]')
#
#     # //div[@id="gw-south-panel"]//div[contains(text(),"Error")]
#     # TODO: select only the required check boxes
#     def approve_all_uw_issues(self):
#         all_check_box = BaseElement(self.driver, self._locator_all_pending_approval_check_box)
#         all_check_box.click_all_elements()
#         header_approve_btn = BaseElement(self.driver, self._locator_header_approve_btn)
#         header_approve_btn.click_element()
#
#         risk_approval_screen_ok_btn = BaseElement(self.driver, self._locator_ok_btn)
#         risk_approval_screen_ok_btn.click_element()
#
#         self.accept_alert()
#         if all_check_box.is_element_present():
#             self.log.debug("All UW Issues are not approved yet.")
#         else:
#             self.log.info("All UW Issues are approved.")
#
#
# class PolicyReview(BasePage):
#     log = getLogger()
#
#     def __init__(self, driver):
#         super().__init__(driver=driver, url=None)
#         self.SCREEN_TITLE = "Policy Review"
#
#
# class Quote(BasePage):
#     log = getLogger()
#
#     def __init__(self, driver):
#         super().__init__(driver=driver, url=None)
#         self.SCREEN_TITLE = "Quote"
#         self._locator_total_premium_amt = (By.XPATH, '//div[text()="Total Premium"]'
#                                                      '/following-sibling::div//div[contains(text(), "$")]')
#
#     def total_premium_amt(self):
#         elm = BaseElement(self.driver, self._locator_total_premium_amt)
#         premium_txt =  elm.get_text()
#         premium = float(sub(r'[^\d.]', '', premium_txt))
#         self.log.info(f"Total Premium is {premium_txt}")
#         return premium
#
#
# class Forms(BasePage):
#     log = getLogger()
#
#     def __init__(self, driver):
#         super().__init__(driver=driver, url=None)
#         self.SCREEN_TITLE = "Forms"
#         # self._locator_s = (By.XPATH, '//div[text()="Form #"]/ancestor::tr/following-sibling::tr')
#         self._locator_ph_notice = (By.XPATH, '//div[contains(text(),"Notice to Policyholders")]')
#
#     def ph_notice(self):
#         ph_notice = BaseElement(self.driver, self._locator_ph_notice)
#         if ph_notice.get_text() == "Notice to Policyholders":
#             print("Notice to Policyholders form is generated")
#             self.log.info("Policy Forms are generated")
#         else:
#             print("PH Notice is not generated for the quote")
#             self.log.info("Forms are not generated correctly")


class Payment(BasePage):
    log = getLogger()

    def __init__(self, driver):
        super().__init__(driver=driver, url=None)
        self.SCREEN_TITLE = "Payment"
        self._locator_billing_method_dropdown = (By.XPATH, '//div[text()="Billing Method"]/following-sibling::div//select')
        self._locator_plan_type_dropdown = (By.XPATH, '//div[text()="Plan Type"]/following-sibling::div//select')
        self._locator_premium_reporting_plan_dropdown = (By.XPATH, '//div[text()="Premium Reporting Plan"]/following-sibling::div//select')

    def select_billing_method(self, text):
        elm = BaseElement(self.driver, self._locator_billing_method_dropdown)
        elm.select_option(text=text)

    def select_plan_type(self, text):
        elm = BaseElement(self.driver, self._locator_plan_type_dropdown)
        elm.select_option(text=text)

    def select_premium_reporting_plan(self, text):
        elm = BaseElement(self.driver, self._locator_premium_reporting_plan_dropdown)
        elm.select_option(text=text)
