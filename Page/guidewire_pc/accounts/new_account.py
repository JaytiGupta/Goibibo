import time
from datetime import datetime
from random import randint, choice

from selenium.common import WebDriverException

from Base.basepage import BasePage
from Base.baseelement import BaseElement
from selenium.webdriver.common.by import By
from Util.logs import getLogger
from Util import random_data


class NewAccount(BasePage):

    log = getLogger()

    def __init__(self, driver):
        super().__init__(driver=driver, url=None)
        self.enter_account_information_screen = EnterAccountInformation(self.driver)
        self.create_account_screen = CreateAccountPage(self.driver)

        # random input data
        current_datetime = datetime.now()
        unique_string = current_datetime.strftime("%y%m%d%H%M%S")
        self.random_company_name = "company-" + unique_string
        self.random_first_name = "first-" + unique_string
        self.random_last_name = "last-" + unique_string
        self.random_phone_number = f"(650) {randint(101, 999)}-{randint(1001, 9999)}"
        self.random_email_address = f"my_email{unique_string}@test.com"
        address = random_data.random_address("VA")
        self.random_address1 = address.Address_1,
        self.random_city = address.City,
        self.random_state = address.State,
        self.random_zip_code = address.Zip_Code,
        self.random_address_type = choice(["Billing", "Business", "Home", "Other"])
        self.random_organization = "Armstrong and Company",
        self.random_producer_code = "100-002541 Armstrong (Premier)"

    def create_default_new_account(self, account_type):
        """
        :param account_type: company or person
        Creates a new account with all mandatory fields filled as random values.
        """

        # Enter Account Information Page
        if account_type.lower() == "company":
            self.enter_account_information_screen.input_company_name(self.random_company_name)

        if account_type.lower() == "person":
            self.enter_account_information_screen.input_name(self.random_first_name, self.random_last_name)

        self.enter_account_information_screen.search_btn.click_element()
        self.enter_account_information_screen.select_new_account_type(account_type)

        # Create account Page
        if account_type.lower() == "company":
            self.create_account_screen.input_office_phone(self.random_phone_number)

        self.create_account_screen.input_primary_email(self.random_email_address)
        self.create_account_screen.input_address(address1=self.random_address1,
                                                 city=self.random_city,
                                                 state=self.random_state,
                                                 zip_code=self.random_zip_code,
                                                 address_type=self.random_address_type)

        self.create_account_screen.select_producer(organization=self.random_organization,
                                                   producer_code=self.random_producer_code)
        self.create_account_screen.click_btn_update()


class EnterAccountInformation(BasePage):
    log = getLogger()

    def __init__(self, driver):
        super().__init__(driver=driver, url=None)

    @property
    def company_name_input_box(self):
        locator = (By.XPATH, '//div[text()="Company Name"]/following-sibling::div//input')
        return BaseElement(self.driver, locator)

    @property
    def first_name_input_box(self):
        locator = (By.XPATH, '//div[text()="First name"]/following-sibling::div//input')
        return BaseElement(self.driver, locator)

    @property
    def last_name_input_box(self):
        locator = (By.XPATH, '//div[text()="Last name"]/following-sibling::div//input')
        return BaseElement(self.driver, locator)

    @property
    def search_btn(self):
        locator = (By.XPATH, '//div[@id="NewAccount-NewAccountScreen-NewAccountSearchDV-SearchAndResetInputSet-'
                               'SearchLinksInputSet-Search"]')
        return BaseElement(self.driver, locator)

    @property
    def zero_results_information_tag(self):
        locator = (By.XPATH, '//div[contains(text(),"The search returned zero results.")]')
        return BaseElement(self.driver, locator)

    @property
    def new_account_btn(self):
        locator = (By.XPATH, '//div[@aria-label="Create New Account"]')
        return BaseElement(self.driver, locator)

    @property
    def company_dropdown(self):
        locator = (By.XPATH, '//div[@aria-label="Company"]')
        return BaseElement(self.driver, locator)

    @property
    def person_dropdown(self):
        locator = (By.XPATH, '//div[@aria-label="Person"]')
        return BaseElement(self.driver, locator)

    @property
    def address_book_dropdown(self):
        locator = (By.XPATH, '//div[@aria-label="From Address Book"]')
        return BaseElement(self.driver, locator)

    def input_company_name(self, name):
        self.company_name_input_box.enter_text(name)
        self.log.info(f"Company Name '{name}' value entered.")

    def input_name(self, first_name, last_name):
        self.first_name_input_box.enter_text(first_name)
        self.log.info(f"First Name: '{first_name}' value entered.")

        self.last_name_input_box.enter_text(last_name)
        self.log.info(f"Last Name: '{last_name}' value entered.")

    def click_search_btn(self):
        self.search_btn.click_element()
        self.log.info(f"Clicked Search button.")
        self.new_account_btn.wait_till_visibility_of_element()

    def validate_zero_results(self):
        if self.zero_results_information_tag == "The search returned zero results.":
            self.log.info("No matching records found")
        else:
            self.log.info("Account Search results found for the entered information")

    def select_new_account_type(self, account_type):
        self.new_account_btn.click_element()
        if account_type.lower() == "company":
            self.company_dropdown.click_element()
            self.log.info(f"Clicked Create New Account 'Company'.")
        elif account_type.lower() == "person":
            self.person_dropdown.click_element()
            self.log.info(f"Clicked Create New Account 'Person'.")
        elif account_type.lower() == "from address book":
            self.address_book_dropdown.click_element()
            self.log.info(f"Clicked Create New Account 'From Address Book'.")
        # try:
        #     self.search_btn.wait_till_staleness_of_element()
        # except WebDriverException:
        #     pass


class CreateAccountPage(BasePage):
    log = getLogger()

    def __init__(self, driver):
        super().__init__(driver=driver, url=None)

    @property
    def office_phone(self):
        locator = (By.XPATH, '//div[contains(text(),"Office Phone")]/following-sibling::div//input')
        return BaseElement(self.driver, locator)

    @property
    def primary_email(self):
        locator = (By.XPATH, '//div[contains(text(),"Primary Email")]/following-sibling::div//input')
        return BaseElement(self.driver, locator)

    @property
    def address1(self):
        locator = (By.XPATH, '//div[contains(text(),"Address 1")]/following-sibling::div//input')
        return BaseElement(self.driver, locator)

    @property
    def address2(self):
        locator = (By.XPATH, '//div[contains(text(),"Address 2")]/following-sibling::div//input')
        return BaseElement(self.driver, locator)

    @property
    def address3(self):
        locator = (By.XPATH, '//div[contains(text(),"Address 3")]/following-sibling::div//input')
        return BaseElement(self.driver, locator)

    @property
    def city(self):
        locator = (By.XPATH, '//div[contains(text(),"City")]/following-sibling::div//input')
        return BaseElement(self.driver, locator)

    @property
    def state_dropdown(self):
        locator = (By.XPATH, '//div[contains(text(),"State")]/following-sibling::div//select')
        return BaseElement(self.driver, locator)

    @property
    def zip(self):
        locator = (By.XPATH, '//div[contains(text(),"ZIP Code")]/following-sibling::div//input')
        return BaseElement(self.driver, locator)

    @property
    def address_type_dropdown(self):
        locator = (By.XPATH, '//div[contains(text(),"Address Type")]/following-sibling::div//select')
        return BaseElement(self.driver, locator)

    @property
    def organization_input_box(self):
        locator = (By.XPATH, '//div[text()="Organization"]/following-sibling::div//input')
        return BaseElement(self.driver, locator)

    @property
    def organization_search_btn(self):
        locator = (By.XPATH, '//div[text()="Organization"]/following-sibling::div//span[@aria-label="gw-search-icon"]')
        return BaseElement(self.driver, locator)

    @property
    def producer_code_dropdown(self):
        locator = (By.XPATH, '//div[text()="Producer Code"]/following-sibling::div//select')
        return BaseElement(self.driver, locator)

    @property
    def update_btn(self):
        locator = (By.XPATH, '//div[@aria-label="Update"]')
        return BaseElement(self.driver, locator)

    @property
    def cancel_btn(self):
        locator = (By.XPATH, '//div[@aria-label="Cancel"]')
        return BaseElement(self.driver, locator)

    def input_office_phone(self, number):
        self.office_phone.enter_text(number)
        self.log.info(f"Office Phone: '{number}' value entered.")

    def input_primary_email(self, text):
        self.primary_email.enter_text(text)
        self.log.info(f"Primary Email: '{text}' value entered.")

    def input_address(self, address1, city, state, zip_code, address_type, address2=None, address3=None):
        self.address1.enter_text(address1)
        if address2 is not None:
            self.address2.enter_text(address2)
        if address3 is not None:
            self.address3.enter_text(address3)
        self.city.enter_text(city)
        self.state_dropdown.select_option(text=state)
        self.zip.enter_text(zip_code)
        self.address_type_dropdown.select_option(text=address_type)
        self.log.info(f"Address entered.")

    def select_producer(self, organization, producer_code):
        self.organization_input_box.enter_text(organization)
        self.organization_input_box.press_tab_key()
        # self.organization_search_btn.click_element()
        self.producer_code_dropdown.select_option(text=producer_code)
        self.log.info(f"Section: Select Producer - Organization & Producer Code selected.")

    def click_btn_update(self):
        self.update_btn.click_element()
        self.log.info(f"Clicked Update button.")
        try:
            self.update_btn.wait_till_staleness_of_element()
        except WebDriverException:
            pass

    def click_btn_cancel(self):
        self.cancel_btn.click_element()
        self.log.info(f"Clicked Cancel button.")
