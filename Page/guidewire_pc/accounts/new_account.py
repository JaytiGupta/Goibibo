import random

from selenium.common import WebDriverException

from Base.basepage import BasePage
from Base.baseelement import BaseElement
from selenium.webdriver.common.by import By
from Util.logs import getLogger
from Util import random_data
from Page.guidewire_pc.accounts.titilebar import TitleBar
from faker import Faker


class NewAccount(BasePage):

    log = getLogger()

    def __init__(self, driver):
        super().__init__(driver=driver, url=None)
        self.enter_account_information_screen = EnterAccountInformation(self.driver)
        self.create_account_screen = CreateAccountPage(self.driver)

        # random input data
        fake = Faker(locale="en_US")
        self.random_company_name = fake.company()
        self.random_first_name = fake.first_name()
        self.random_last_name = fake.last_name()
        self.random_phone_number = fake.unique.numerify('###-###-####')
        self.random_email_address = fake.company_email()

        # self.random_address = random_data.random_address("VA")

        self.random_address_type = random.choice(["Billing", "Business", "Home", "Other"])
        self.random_organization = "Armstrong and Company"
        self.random_producer_code = "100-002541 Armstrong (Premier)"

    def create_default_new_account(self, account_type, state):
        """
        :param account_type: company or person
        Creates a new account with all mandatory fields filled as random values.
        """

        # Enter Account Information Page
        if account_type.lower() == "company":
            self.enter_account_information_screen.input_company_name(self.random_company_name)
            self.enter_account_information_screen.create_new_account.company()

        if account_type.lower() == "person":
            self.enter_account_information_screen.input_name(self.random_first_name, self.random_last_name)
            self.enter_account_information_screen.create_new_account.person()

        # Create account Page
        if account_type.lower() == "company":
            self.create_account_screen.input_office_phone(self.random_phone_number)

        self.create_account_screen.input_primary_email(self.random_email_address)

        random_address = random_data.random_address(state)
        self.create_account_screen.input_address(address1=random_address.Address_1,
                                                 city=random_address.City,
                                                 state=random_address.State,
                                                 zip_code=random_address.Zip_Code,
                                                 address_type=self.random_address_type)

        self.create_account_screen.select_producer(organization=self.random_organization,
                                                   producer_code=self.random_producer_code)
        self.create_account_screen.click_btn_update()


class EnterAccountInformation(BasePage):
    log = getLogger()

    def __init__(self, driver):
        super().__init__(driver=driver, url=None)
        self.titlebar = TitleBar(self.driver)
        self.create_new_account = self.CreateNewAccount(self.driver)

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
    def zero_results_information_tag(self):
        locator = (By.XPATH, '//div[contains(text(),"The search returned zero results.")]')
        return BaseElement(self.driver, locator)

    class CreateNewAccount:
        log = getLogger()

        def __init__(self, driver):
            self.driver = driver
            self.titlebar = TitleBar(self.driver)

        @property
        def _search_btn(self):
            locator = (By.XPATH, '//div[@id="NewAccount-NewAccountScreen-NewAccountSearchDV-SearchAndResetInputSet-'
                                 'SearchLinksInputSet-Search"]')
            return BaseElement(self.driver, locator)

        @property
        def _create_new_account_btn(self):
            locator = (By.XPATH, '//div[@aria-label="Create New Account"]')
            return BaseElement(self.driver, locator)

        @property
        def _company_option(self):
            locator = (By.XPATH, '//div[@aria-label="Company"]')
            return BaseElement(self.driver, locator)

        @property
        def _person_option(self):
            locator = (By.XPATH, '//div[@aria-label="Person"]')
            return BaseElement(self.driver, locator)

        def _select_new_account_type(self, account_type):
            self._search_btn.click_element()
            self.log.info(f"Clicked Search button.")

            self._create_new_account_btn.click_element()

            if not self._company_option.is_element_present():
                self._create_new_account_btn.click_element()

            if account_type.lower() == "company":
                self._company_option.click_element()
                self.log.info(f"Clicked Create New Account 'Company'.")
            elif account_type.lower() == "person":
                self._person_option.click_element()
                self.log.info(f"Clicked Create New Account 'Person'.")

            self.titlebar.wait_for_screen("Create account")
            self.log.info(f"Navigated to 'Create account' screen.")

        def person(self):
            self._select_new_account_type("person")

        def company(self):
            self._select_new_account_type("company")

    def input_company_name(self, name):
        self.company_name_input_box.enter_text(name)
        self.log.info(f"Company Name '{name}' value entered.")

    def input_name(self, first_name, last_name):
        self.first_name_input_box.enter_text(first_name)
        self.log.info(f"First Name: '{first_name}' value entered.")

        self.last_name_input_box.enter_text(last_name)
        self.log.info(f"Last Name: '{last_name}' value entered.")

    def validate_zero_results(self):
        if self.zero_results_information_tag == "The search returned zero results.":
            self.log.info("No matching records found")
        else:
            self.log.info("Account Search results found for the entered information")


class CreateAccountPage(BasePage):
    log = getLogger()

    def __init__(self, driver):
        super().__init__(driver=driver, url=None)
        self.title_bar = TitleBar(self.driver)

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
        # Page is reloading after entering the phone number
        self.title_bar.wait_for_screen("Create account")

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
        self.title_bar.wait_for_screen("Account Summary")

    def click_btn_cancel(self):
        self.cancel_btn.click_element()
        self.log.info(f"Clicked Cancel button.")
