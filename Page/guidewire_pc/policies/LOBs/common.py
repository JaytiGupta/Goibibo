# Created separate folder for common - will delete this file after some time


# import time
# from re import sub
#
# from selenium.common import WebDriverException
# from selenium.webdriver.common.by import By
# from Base.baseelement import BaseElement
# from Base.baseelement import NestedElement
# from Base.basepage import BasePage
# from Util.logs import getLogger
# from Page.guidewire_pc.policies.info_bar import InfoBar
# import random
# from selenium.webdriver.support.wait import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from Page.guidewire_pc.policies.common.workspace import Workspace


# class TableQuestionnaires:
#     log = getLogger()
#
#     def __init__(self, driver):
#         self.driver = driver
#
#     @staticmethod
#     def radio_btn_locator(question, answer):
#         if question.lower() == "all":
#             question = ""
#
#         if answer.lower() == "yes":
#             x_path = f'//div[contains(text(),"{question}")]/ancestor::tr//input[@type="radio"][@value="true"]'
#         else:
#             x_path = f'//div[contains(text(),"{question}")]/ancestor::tr//input[@type="radio"][@value="false"]'
#
#         locator = (By.XPATH, x_path)
#         return locator
#
#     def select_radio_btn(self, question, answer):
#         locator = self.radio_btn_locator(question, answer)
#         radio_btn = BaseElement(self.driver, locator)
#         radio_btn.click_element()
#         self.log.info(f"Select {answer} for {question}.")
#
#     def select_all_radio_btn(self, answer):
#         locator = self.radio_btn_locator("all", answer)
#         all_radio_btn_elm = BaseElement(self.driver, locator)
#         all_radio_btn_elm.click_all_elements()
#         self.log.info(f"Select all radio button questions as {answer}.")
#
#     def input_box(self, question, answer):
#         x_path = f'//div[contains(text(),"{question}")]/ancestor::tr//input[@type="text"]'
#         locator = (By.XPATH, x_path)
#         input_box = BaseElement(self.driver, locator)
#         input_box.enter_text(answer)
#         self.log.info(f"Enter {answer} for {question}.")
#
#     def dropdown(self, question, dropdown_text):
#         x_path = f'//div[contains(text(),"{question}")]/ancestor::tr//select'
#         locator = (By.XPATH, x_path)
#         dropdown_elm = BaseElement(self.driver, locator)
#         dropdown_elm.select_option(text=dropdown_text)


# class Sidebar(BasePage):
#     log = getLogger()
#
#     def __init__(self, driver):
#         super().__init__(driver=driver, url=None)
#
#     @property
#     def side_bar(self):
#         locator = (By.XPATH, '//div[@aria-label="west panel"]')
#         return BaseElement(self.driver, locator)
#
#     @property
#     def heading(self):
#         locator = (By.XPATH, '//div[@aria-label="west panel"]//div[@role="heading"]')
#         return BaseElement(self.driver, locator)
#
#     def transaction_number(self) -> str:
#         heading_text: str = self.heading.get_text()
#         transaction_number: str = heading_text.split(" ")[-1]
#         return transaction_number


# now importing from other module


# class Workspace_old:
#     log = getLogger()
#
#     def __init__(self, driver):
#         self.driver = driver
#         self.risk_analysis_screen = RiskAnalysis(self.driver)
#
#     @property
#     def validation_results(self):
#         locator = (By.XPATH, '//div[text()="Validation Results"]')
#         return BaseElement(self.driver, locator)
#
#     @property
#     def error(self):
#         locator = (By.XPATH, '//div[@id="gw-south-panel"]//div[contains(text(),"Error")]')
#         return BaseElement(self.driver, locator)
#
#     @property
#     def warning(self):
#         locator = (By.XPATH, '//div[@id="gw-south-panel"]//div[contains(text(),"Warning")]')
#         return BaseElement(self.driver, locator)
#
#     @property
#     def information(self):
#         locator = (By.XPATH, '//div[@id="gw-south-panel"]//div[contains(text(),"Information")]')
#         return BaseElement(self.driver, locator) #


# class TitleToolbar(BasePage):
#     log = getLogger()
#
#     def __init__(self, driver):
#         super().__init__(driver=driver, url=None)
#         self.risk_analysis_screen = RiskAnalysis(self.driver)
#         self.workspace = Workspace(self.driver)
#         self.info_bar = InfoBar(self.driver)
#         self.quote_screen = Quote(self.driver)
#
#     @property
#     def screen_title_element(self):
#         locator = (By.XPATH, '//div[@id="gw-center-title-toolbar"]//div[@role="heading"]')
#         return BaseElement(self.driver, locator)
#
#     @property
#     def next_btn(self):
#         locator = (By.XPATH, '//div[@id="gw-center-title-toolbar"]//div[contains(@aria-label, "Next")]/parent::div')
#         return BaseElement(self.driver, locator)
#
#     @property
#     def next_btn_text(self):
#         locator = (By.XPATH, '//div[@id="gw-center-title-toolbar"]//div[contains(@aria-label, "Next")]')
#         return BaseElement(self.driver, locator)
#
#     @property
#     def back_btn(self):
#         locator = (By.XPATH, '//div[@id="gw-center-title-toolbar"]//div[text()="Back"]')
#         return BaseElement(self.driver, locator)
#
#     @property
#     def quote_btn(self):
#         locator = (By.XPATH, '//div[@id="gw-center-title-toolbar"]//div[@aria-label="Quote"]')
#         return BaseElement(self.driver, locator)
#
#     @property
#     def save_draft_btn(self):
#         locator = (By.XPATH, '//div[@id="gw-center-title-toolbar"]//div[@aria-label="Save Draft"]')
#         return BaseElement(self.driver, locator)
#
#     @property
#     def close_option_btn(self):
#         locator = (By.XPATH, '//div[@id="gw-center-title-toolbar"]//div[@aria-label="Close Options"]')
#         return BaseElement(self.driver, locator)
#
#     @property
#     def reinstate_btn(self):
#         locator = (By.XPATH, '//div[@id="gw-center-title-toolbar"]//div[@aria-label="Reinstate"]')
#         return BaseElement(self.driver, locator)
#
#     @property
#     def bind_options_btn(self):
#         locator = (By.XPATH, '//div[@id="gw-center-title-toolbar"]//div[@aria-label="Bind Options"]')
#         return BaseElement(self.driver, locator)
#
#     @property
#     def bind_only_btn(self):
#         locator = (By.XPATH, '//div[@id="gw-center-title-toolbar"]//div[@aria-label="Bind Only"]')
#         return BaseElement(self.driver, locator)
#
#     @property
#     def issue_policy_btn(self):
#         locator = (By.XPATH, '//div[@id="gw-center-title-toolbar"]//div[@aria-label="Issue Policy"]')
#         return BaseElement(self.driver, locator)
#
#     @property
#     def cancel_now_btn(self):
#         locator = (By.XPATH, '//div[@id="gw-center-title-toolbar"]//'
#                              'div[contains(@id,"BindOptions")]//'
#                              'div[@aria-label="Cancel Now"]')
#         return BaseElement(self.driver, locator)
#
#     @property
#     def schedule_cancellation_btn(self):
#         locator = (By.XPATH, '//div[@id="gw-center-title-toolbar"]//'
#                              'div[contains(@id,"BindOptions")]//'
#                              'div[@aria-label="Schedule Cancellation"]')
#         return BaseElement(self.driver, locator)
#
#     @property
#     def details_btn(self):
#         locator = (By.XPATH, '//div[@id="gw-center-title-toolbar"]//div[text()="Details"]')
#         return BaseElement(self.driver, locator)
#
#     def screen_title_text(self):
#         text = self.screen_title_element.get_text()
#         return text
#
#     def wait_for_screen(self, screen_title_text):
#         self.screen_title_element.wait_till_text_to_be_present_in_element(screen_title_text)
#
#     def next(self):
#         title = self.screen_title_text()
#         self.next_btn.click_element()
#         self.screen_title_element.wait_till_text_to_be_not_present_in_element(title)
#         self.back_btn.wait_till_text_to_be_present_in_element("Back")
#
#     def navigate_till_screen(self, screen_title):
#         actual_screen_title = self.screen_title_text()
#
#         while screen_title != actual_screen_title:
#             self.next()
#             actual_screen_title = self.screen_title_text()
#
#     def quote2(self):
#         self.back_btn.wait_till_text_to_be_present_in_element("Back")
#         initial_screen_title = self.screen_title_text()
#         self.log.info(f"{initial_screen_title} screen")
#
#         self.quote_btn.click_element()
#         self.log.info("Clicked Quote button.")
#         time.sleep(3)
#
#         if self.screen_title_text() == "Quote":
#             self.log.info("Quoted successfully")
#         elif self.screen_title_text() == "Pre-Quote Issues":
#             self.log.info("Pre-Quote Issues screen")
#             self.details_btn.click_element()
#             self.log.debug("Navigate to Underwriter issues tab at Risk Analysis screen.")
#             self.risk_analysis_screen.approve_all_uw_issues()
#             self.log.debug("All underwriter issues approved.")
#             self.wait_for_screen("Risk Analysis")
#             self.quote2()
#         elif self.workspace.is_workspace_present():
#             message_types = self.workspace.get_all_message_types()
#             if any("error" in message_type.lower() for message_type in message_types):
#                 self.log.debug("Getting error and unable to quote")
#                 raise Exception("Getting error and unable to quote")
#             else:
#                 self.workspace.clear_btn.click_element()
#                 self.quote2()
#
#     def quote(self):
#         initial_screen_title = self.screen_title_text()
#
#         self.log.info(f"{initial_screen_title} screen")
#         self.quote_btn.click_element()
#         self.log.info("Clicked Quote button.")
#
#
#         time.sleep(5)
#
#         if self.screen_title_text() == "Quote":
#             self.log.info("Quoted successfully")
#         elif self.screen_title_text() == "Pre-Quote Issues":
#             self.log.info("Pre-Quote Issues screen")
#             self.details_btn.click_element()
#             self.log.debug("Navigate to Underwriter issues tab at Risk Analysis screen.")
#             self.risk_analysis_screen.approve_all_uw_issues()
#             self.log.debug("All underwriter issues approved.")
#             self.wait_for_screen("Risk Analysis")
#             self.quote()
#         elif self.screen_title_text() == initial_screen_title:
#             self.log.info(f"{initial_screen_title} screen")
#             if self.workspace.error.is_element_present():
#                 self.log.debug("Getting error and unable to quote")
#                 raise Exception("Getting error and unable to quote")
#             elif self.workspace.warning.is_element_present() or self.workspace.information.is_element_present():
#                 self.log.info("Getting warnings or information")
#             self.quote()
#
#     def bind_policy(self):
#         self.bind_options_btn.click_element()
#         self.bind_only_btn.click_element()
#         self.log.info(f"Clicked Bind Only button.")
#
#     def issue_policy(self):
#         initial_screen_title = self.screen_title_text()
#
#         # bind option is not present for change policy transaction. Issue policy btn is on title toolbar.
#         if self.bind_options_btn.is_element_present():
#             self.bind_options_btn.click_element()
#
#         self.issue_policy_btn.click_element()
#         self.log.info(f"Clicked Issue Policy button.")
#         self.accept_alert()
#
#
#         time.sleep(3)
#
#         if self.screen_title_text() == "Submission Bound":
#             self.log.info("Your Submission has been bound.")
#         elif self.screen_title_text() == "Policy Change Bound":
#             self.log.info("Your Policy Change has been bound.")
#         elif self.workspace.is_workspace_present():
#             message_types = self.workspace.get_all_message_types()
#             self.log.info(f"Getting messages(types) - {', '.join(message_types)}")
#             if any("error" in message_type.lower() for message_type in message_types):
#                 self.log.debug("Getting error and unable to quote")
#                 raise Exception("Getting error and unable to quote")
#             else:
#                 self.issue_policy()
#
#     def schedule_cancellation(self):
#         pass
#
#     def cancel_now(self):
#         initial_screen_title = self.screen_title_text()
#         self.bind_options_btn.click_element()
#         self.cancel_now_btn.click_element()
#         self.log.info(f"Clicked Cancel Now button.")
#         self.accept_alert()
#         self.screen_title_element.wait_till_text_to_be_not_present_in_element(initial_screen_title)
#         if self.screen_title_text() == "Cancellation Bound":
#             self.log.info("Your Cancellation has been bound.")
#
#     def reinstate(self):
#         initial_screen_title = self.screen_title_text()
#         self.reinstate_btn.click_element()
#         self.accept_alert()
#         self.screen_title_element.wait_till_text_to_be_not_present_in_element(initial_screen_title)
#         if self.screen_title_text() == "Reinstatement Bound":
#             self.log.info("Your Reinstatement has been bound.")


# class PolicyInfo(BasePage):
#     log = getLogger()
#
#     def __init__(self, driver):
#         super().__init__(driver=driver, url=None)
#         self.SCREEN_TITLE = "Policy Info"
#         self._locator_FEIN_input_box = (By.XPATH, '//div[text()="FEIN"]/parent::div//input')
#         self._locator_industry_code_input_box = (By.XPATH, '//div[text()="Industry Code"]/parent::div//input')
#         self._locator_year_business_started_input_box = (
#             By.XPATH, '//div[text()="Year Business Started"]/parent::div//input')
#         self._locator_term_type_dropdown = (By.XPATH, '//div[text()="Term Type"]/parent::div//select')
#         self._locator_effective_date_input_box = (By.XPATH, '//div[text()="Effective Date"]/parent::div//input')
#         self._locator_underwriter_companies_dropdown = (By.XPATH, '//select[contains(@name, "UWCompanyInputSet")]')
#
#     @property
#     def organization_type_dropdown(self):
#         locator = (By.XPATH, '//div[text()="Organization Type"]/parent::div//select')
#         return BaseElement(self.driver, locator)
#
#     def input_FEIN(self, text):
#         fein = BaseElement(self.driver, self._locator_FEIN_input_box)
#         fein.enter_text(text)  # text must be 9-digit no.
#         self.log.info(f"Enter FEIN - {text}")
#
#     def industry_code_input(self, industry_code):
#         industry_code_elm = BaseElement(self.driver, self._locator_industry_code_input_box)
#         industry_code_elm.enter_text(industry_code)
#         self.log.info(f"Enter Industry Code - {industry_code}")
#
#     def select_organization_type(self, type_of_org):
#         self.organization_type_dropdown.select_option(text=type_of_org)
#         self.log.info(f"Select Organisation Type - {type_of_org}")
#
#     def term_type(self, pol_term):
#         term_type_elm = BaseElement(self.driver, self._locator_term_type_dropdown)
#         term_type_elm.select_option(text=pol_term)
#         self.log.info(f"Select Policy Term Type - {pol_term}")
#
#     def policy_effective_date(self, policy_date):
#         eff_date_elm = BaseElement(self.driver, self._locator_effective_date_input_box)
#         eff_date_elm.enter_text(policy_date)
#         self.log.info(f"Enter Policy Effective Date - {policy_date}")
#
#     def uw_companies(self, uw_company):
#         uw_company_elm = BaseElement(self.driver, self._locator_underwriter_companies_dropdown)
#         uw_company_elm.select_option(text=uw_company)
#         self.log.info(f"Select Underwriting company - {uw_company}")
#
#     # select only from first page
#     def select_random_industry_code(self):
#         locator_industry_code_search_icon = (By.XPATH, '//div[text()="Industry Code"]/parent::div//'
#                                                        'span[@aria-label="gw-search-icon"]')
#         industry_code_search_btn = BaseElement(self.driver, locator_industry_code_search_icon)
#         industry_code_search_btn.click_element()
#
#         locator_industry_code_page_all_select_btn = (By.XPATH, '//div[text()="Select"]')
#         industry_code_page_all_select_btn = BaseElement(self.driver, locator_industry_code_page_all_select_btn)
#
#         random_select_button = random.choice(industry_code_page_all_select_btn.get_all_elements())
#         random_select_button.click()
#
#     def fill_random_details(self):
#         fein = random.randint(10**8, (10**9-1))
#         self.input_FEIN(fein)
#         self.select_random_industry_code()
#         self.organization_type_dropdown.select_random_dropdown_option('<none>')
#         return None


# class RiskAnalysis(BasePage):
#     log = getLogger()
#
#     def __init__(self, driver):
#         super().__init__(driver=driver, url=None)
#         self.SCREEN_TITLE = "Risk Analysis"
#
#     @property
#     def _all_pending_approval_check_box(self):
#         locator = (By.XPATH, '//div[text()="Approve"]/ancestor::td[not(contains(@colspan,"1"))]'
#                              '/preceding-sibling::td[4]'
#                              '//input[@type="checkbox"]')
#         return BaseElement(self.driver, locator)
#
#     @property
#     def _header_approve_btn(self):
#         locator = (By.XPATH, '//div[@class="gw-ListView--UI-left"]//div[text()="Approve"]')
#         return BaseElement(self.driver, locator)
#
#     @property
#     def _risk_approval_details_screen_ok_button(self):
#         locator = (By.XPATH, '//div[@role="button"]//div[@aria-label="OK"]')
#         return BaseElement(self.driver, locator)
#
#     def approve_all_uw_issues(self):
#         self._all_pending_approval_check_box.click_all_elements()
#         self._header_approve_btn.click_element()
#         self._risk_approval_details_screen_ok_button.click_element()
#         self.accept_alert()
#
#         pending_check_boxes = self._all_pending_approval_check_box.is_element_present()
#         if pending_check_boxes:
#             self.log.debug("All UW Issues are not approved yet.")
#         else:
#             self.log.info("All UW Issues are approved.")


# class PolicyReview(BasePage):
#     log = getLogger()
#
#     def __init__(self, driver):
#         super().__init__(driver=driver, url=None)
#         self.SCREEN_TITLE = "Policy Review"


# class Quote(BasePage):
#     log = getLogger()
#
#     def __init__(self, driver):
#         super().__init__(driver=driver, url=None)
#         self.SCREEN_TITLE = "Quote"
#
#     @property
#     def _total_premium_amt(self):
#         locator = (By.XPATH, '//div[text()="Total Premium"]/following-sibling::div//div[contains(text(), "$")]')
#         return BaseElement(self.driver, locator)
#
#     def total_premium_amount(self):
#         premium_amount_text = self._total_premium_amt.get_text()
#         premium = float(sub(r'[^\d.]', '', premium_amount_text))
#         self.log.info(f"Total Premium is {premium_amount_text}")
#         return premium


# class Location(BasePage):
#     log = getLogger()
#
#     def __init__(self, driver):
#         super().__init__(driver=driver, url=None)
#         self.SCREEN_TITLE = "Locations"
#         self._locator_add_new_location_btn = (By.XPATH, '//div[contains(text(), "New Loc")]')
#         self._locator_address1 = (By.XPATH, '//div[contains(text(),"Address 1")]/following-sibling::div//input')
#         self._locator_address2 = (By.XPATH, '//div[contains(text(),"Address 2")]/following-sibling::div//input')
#         self._locator_address3 = (By.XPATH, '//div[contains(text(),"Address 3")]/following-sibling::div//input')
#         self._locator_input_city = (By.XPATH, '//div[contains(text(),"City")]/following-sibling::div//input')
#         self._locator_select_state = (By.XPATH, '//div[contains(text(),"State")]/following-sibling::div//select')
#         self._locator_input_zip = (By.XPATH, '//div[contains(text(),"ZIP Code")]/following-sibling::div//input')
#         self._locator_ok_btn = (By.XPATH, '//div[@id="LocationPopup-LocationScreen-Update"]')
#         self._locator_add_existing_location_btn = (By.XPATH, '//div[text()="Add Existing Location"]')
#
#     def add_new_location(self, address1, city, state, zip_code, address2=None, address3=None):
#         add_new_location_btn = BaseElement(self.driver, self._locator_add_new_location_btn)
#         add_new_location_btn.click_element()
#         policy_title = TitleToolbar(self.driver)
#         policy_title.wait_for_screen("Location Information")
#
#         address1_elm = BaseElement(self.driver, self._locator_address1)
#         address1_elm.enter_text(address1)
#
#         if address2 is not None:
#             address2_elm = BaseElement(self.driver, self._locator_address2)
#             address2_elm.enter_text(address2)
#
#         if address3 is not None:
#             address3_elm = BaseElement(self.driver, self._locator_address3)
#             address3_elm.enter_text(address3)
#
#         city_elm = BaseElement(self.driver, self._locator_input_city)
#         city_elm.enter_text(city)
#
#         state_elm = BaseElement(self.driver, self._locator_select_state)
#         state_elm.select_option(text=state)
#
#         zip_elm = BaseElement(self.driver, self._locator_input_zip)
#         zip_elm.enter_text(zip_code)
#
#         ok_btn = BaseElement(self.driver, self._locator_ok_btn)
#         ok_btn.click_element()
#         policy_title.wait_for_screen(self.SCREEN_TITLE)
#
#     def add_existing_location(self, index):
#         existing_loc_list = BaseElement(self.driver, self._locator_add_existing_location_btn)
#         existing_loc_list.select_option(index=index)
#         ok_btn = BaseElement(self.driver, self._locator_ok_btn)
#         ok_btn.click_element()


# class Forms(BasePage):
#     log = getLogger()
#
#     def __init__(self, driver):
#         super().__init__(driver=driver, url=None)
#         self.SCREEN_TITLE = "Forms"
#
#     @property
#     def all_form_rows(self):
#         locator = (By.XPATH, '//table//tr[1]/following-sibling::tr')
#         return BaseElement(self.driver, locator)
#
#     def all_form_list(self):
#         """
#         :return: list of all forms, where each form is a dictionary contains 'Form#' and 'Description'
#         """
#         form_details_list = []
#         all_form_row_elements = self.all_form_rows.get_all_elements()
#
#         for form_row_element in all_form_row_elements:
#             """
#             If you start an XPath expression with //, it begins searching from the root of document.
#             To search relative to a particular element, you should prepend the expression with '.' instead
#             """
#             form_number_locator = (By.XPATH, './/div[contains(@id, "FormNumber")]')
#             form_description_locator = (By.XPATH, './/div[contains(@id, "Description")]')
#             form_number = NestedElement(form_row_element, form_number_locator).get_text()
#             form_description = NestedElement(form_row_element, form_description_locator).get_text()
#
#             form_dict = {
#                     "Form#": form_number,
#                     "Description": form_description,
#                 }
#
#             form_details_list.append(form_dict)
#
#         return form_details_list


# class TransactionBoundScreen(BasePage):
#     log = getLogger()
#
#     def __init__(self, driver):
#         super().__init__(driver=driver, url=None)
#
#     @property
#     def transaction_link_elm(self):
#         locator = (By.XPATH, '//div[contains(@id, "ViewJob")]//div[@role="link"]')
#         return BaseElement(self.driver, locator)
#
#     @property
#     def policy_link_elm(self):
#         locator = (By.XPATH, '//div[contains(@id, "ViewPolicy")]//div[@role="link"]')
#         return BaseElement(self.driver, locator)

