import time
from datetime import datetime
from random import randint, choice
from Base.basepage import BasePage
from Base.baseelement import BaseElement
from selenium.webdriver.common.by import By
from Util.logs import getLogger
from Util import random_address


class NewAccount(BasePage):

    log = getLogger()

    def __init__(self, driver):
        super().__init__(driver=driver, url=None)
        self.enter_account_information_screen = EnterAccountInformation(self.driver)
        self.create_account_screen = CreateAccountPage(self.driver)

    def create_default_new_account(self, account_type):
        """
        :param account_type: company or person
        :param address: address1,city,state,zip (All 4 mandatory address fields separated by coma and no space
        :return: create a new default account
        """
        current_datetime = datetime.now()
        unique_string = current_datetime.strftime("%y%m%d%H%M%S")
        company_name = "company-" + unique_string
        first_name = "first-" + unique_string
        last_name = "last-" + unique_string
        phone_number = f"(650) {randint(101, 999)}-{randint(1001, 9999)}"
        email_address = f"my_email{unique_string}@test.com"
        address = random_address.get_one_address("VA")
        address1 = address["Address_1"]
        city = address["City"]
        state = address["State"]
        zip_code = address["Zip_Code"]

        if account_type.lower() == "company":
            my_box = self.enter_account_information_screen.company_name_input_box
            my_box.enter_text(company_name)
        if account_type.lower() == "person":
            self.enter_account_information_screen.first_name_input_box.enter_text(first_name)
            self.enter_account_information_screen.last_name_input_box.enter_text(last_name)
        self.enter_account_information_screen.search_btn.click_element()
        self.enter_account_information_screen.create_new_account_btn(account_type)
        if account_type.lower() == "company":
            self.create_account_screen.input_office_phone(phone_number)
        self.create_account_screen.input_primary_email(email_address)
        address_type = choice(["Billing", "Business", "Home", "Other"])
        self.create_account_screen.input_address(address1, city, state, zip_code, address_type)
        self.create_account_screen.select_producer("Armstrong and Company", "100-002541 Armstrong (Premier)")
        # self.create_account_screen.click_btn_update()


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

    def validate_zero_results(self):
        if self.zero_results_information_tag == "The search returned zero results.":
            pass
        #         TODO log info for no matching account found
        else:
            pass

    #         TODO click on the first search result

    def create_new_account_btn(self, account_type):
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
        self.organization_search_btn.click_element()
        self.producer_code_dropdown.select_option(text=producer_code)
        self.log.info(f"Section: Select Producer - Organization & Producer Code selected.")

    def click_btn_update(self):
        self.update_btn.click_element()
        self.log.info(f"Clicked Update button.")

    def click_btn_cancel(self):
        self.cancel_btn.click_element()
        self.log.info(f"Clicked Cancel button.")
