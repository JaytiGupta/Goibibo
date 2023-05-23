import time
from datetime import datetime
from random import randint, choice
from Base.basepage import BasePage
from Base.baseelement import BaseElement
from selenium.webdriver.common.by import By


class CreateAccount(BasePage):

    def __init__(self, driver):
        super().__init__(driver=driver, url=None)
        self.locator_input_company_name = (By.XPATH,
                                           '//input[@name="NewAccount-NewAccountScreen-NewAccountSearchDV-'
                                           'GlobalContactNameInputSet-Name"]')
        self.locator_input_first_name = (By.XPATH,
                                         '//input[@name="NewAccount-NewAccountScreen-NewAccountSearchDV-'
                                         'GlobalPersonNameInputSet-FirstName"]')
        self.locator_input_last_name = (By.XPATH,
                                        '//input[@name="NewAccount-NewAccountScreen-NewAccountSearchDV-'
                                        'GlobalPersonNameInputSet-LastName"]')
        self.locator_search_btn = (By.XPATH,
                                   '//div[@id="NewAccount-NewAccountScreen-NewAccountSearchDV-SearchAndResetInputSet-'
                                   'SearchLinksInputSet-Search"]')
        self.locator_zero_results = (By.XPATH, '//div[contains(text(),"The search returned zero results.")]')
        self.locator_new_account_btn = (By.XPATH, '//div[@aria-label="Create New Account"]')
        self.locator_company_dropdown = (By.XPATH, '//div[@aria-label="Company"]')
        self.locator_person_dropdown = (By.XPATH, '//div[@aria-label="Person"]')
        self.locator_address_book_dropdown = (By.XPATH, '//div[@aria-label="From Address Book"]')
        self.locator_office_phone = (By.XPATH, '//div[contains(text(),"Office Phone")]/following-sibling::div//input')
        self.locator_primary_email = (By.XPATH, '//div[contains(text(),"Primary Email")]/following-sibling::div//input')
        self.locator_address1 = (By.XPATH, '//div[contains(text(),"Address 1")]/following-sibling::div//input')
        self.locator_address2 = (By.XPATH, '//div[contains(text(),"Address 2")]/following-sibling::div//input')
        self.locator_address3 = (By.XPATH, '//div[contains(text(),"Address 3")]/following-sibling::div//input')
        self.locator_input_city = (By.XPATH, '//div[contains(text(),"City")]/following-sibling::div//input')
        self.locator_select_state = (By.XPATH, '//div[contains(text(),"State")]/following-sibling::div//select')
        self.locator_input_zip = (By.XPATH, '//div[contains(text(),"ZIP Code")]/following-sibling::div//input')
        self.locator_select_address_type = (By.XPATH, '//div[contains(text(),"Address Type")]/'
                                                      'following-sibling::div//select')

        self.locator_producer_input_org = (By.XPATH, '//div[text()="Organization"]/following-sibling::div//input')
        self.locator_producer_org_search_btn = (By.XPATH, '//div[text()="Organization"]/following-sibling::div'
                                                          '//span[@aria-label="gw-search-icon"]')
        self.locator_select_producer_code = (By.XPATH, '//div[text()="Producer Code"]/following-sibling::div//select')

        # self.locator_input_org = (By.XPATH,
        # '//div[contains(text(),"Organization Type")]/following-sibling::div//select')
        # self.locator_input_producer_org_name = (By.XPATH, '//input[@name="OrganizationSearchPopup-'
        #                                                   'OrganizationSearchPopupScreen-OrganizationSearchDV-'
        #                                                   'GlobalContactNameInputSet-Name"]')
        # self.locator_input_producer_org_search_btn2 = (By.XPATH, '//div[@id="OrganizationSearchPopup-'
        #                                                          'OrganizationSearchPopupScreen-OrganizationSearchDV-'
        #                                                          'SearchAndResetInputSet-SearchLinksInputSet-Search"]')

        self.locator_update_btn = (By.XPATH, '//div[@aria-label="Update"]')
        self.locator_cancel_btn = (By.XPATH, '//div[@aria-label="Cancel"]')

    # Page1 - Enter Account Information - Applicant information

    def input_company_name(self, name):
        company_name = BaseElement(self.driver, self.locator_input_company_name)
        company_name.enter_text(name)

    def input_first_name(self, name):
        first_name = BaseElement(self.driver, self.locator_input_first_name)
        first_name.enter_text(name)

    def input_last_name(self, name):
        last_name = BaseElement(self.driver, self.locator_input_last_name)
        last_name.enter_text(name)

    def click_search_btn(self):
        search_btn = BaseElement(self.driver, self.locator_search_btn)
        search_btn.click_element()

    def validate_zero_results(self):
        zero_results = BaseElement(self.driver, self.locator_zero_results)
        if zero_results == "The search returned zero results.":
            pass
        #         TODO log info for no matching account found
        else:
            pass

    #         TODO click on the first search result

    def create_new_account(self, account_type):
        new_account_btn = BaseElement(self.driver, self.locator_new_account_btn)
        new_account_btn.click_element()
        if account_type.lower() == "company":
            BaseElement(self.driver, self.locator_company_dropdown).click_element()
        elif account_type.lower() == "person":
            BaseElement(self.driver, self.locator_person_dropdown).click_element()
        else:
            BaseElement(self.driver, self.locator_address_book_dropdown).click_element()

    # Page2 - Create account
    def input_office_phone(self, number):
        office_phn = BaseElement(self.driver, self.locator_office_phone)
        office_phn.enter_text(number)

    def input_primary_email(self, text):
        primary_email = BaseElement(self.driver, self.locator_primary_email)
        primary_email.enter_text(text)

    def input_address_1(self, text):
        address1 = BaseElement(self.driver, self.locator_address1)
        address1.enter_text(text)

    def input_city(self, text):
        city = BaseElement(self.driver, self.locator_input_city)
        city.enter_text(text)

    def input_state(self, state):
        state_elm = BaseElement(self.driver, self.locator_select_state)
        state_elm.select_option(text=state)

    def input_zip(self, text):
        zip_elm = BaseElement(self.driver, self.locator_input_zip)
        zip_elm.enter_text(text)

    def select_address_type(self, value):
        address_type = BaseElement(self.driver, self.locator_select_address_type)
        address_type.select_option(text=value)

    def select_producer(self, organization, producer_code):
        input_organization_elm = BaseElement(self.driver, self.locator_producer_input_org)
        btn_organization_search_elm = BaseElement(self.driver, self.locator_producer_org_search_btn)

        input_organization_elm.enter_text(organization)
        btn_organization_search_elm.click_element()

        # Producer code element generates after the organization search
        # hence searching it after clicking on search button
        select_producer_code_elm = BaseElement(self.driver, self.locator_select_producer_code)
        select_producer_code_elm.select_option(text=producer_code)

    def click_btn_update(self):
        update_btn = BaseElement(self.driver, self.locator_update_btn)
        update_btn.click_element()

    def click_btn_cancel(self):
        btn = BaseElement(self.driver, self.locator_cancel_btn)
        btn.click_element()

    # ---------------------

    def input_address(self, address1, city, state, zip_code, address_type, address2=None, address3=None):
        address1_elm = BaseElement(self.driver, self.locator_address1)
        address2_elm = BaseElement(self.driver, self.locator_address2)
        address3_elm = BaseElement(self.driver, self.locator_address3)
        city_elm = BaseElement(self.driver, self.locator_input_city)
        state_elm = BaseElement(self.driver, self.locator_select_state)
        zip_elm = BaseElement(self.driver, self.locator_input_zip)
        address_type_elm = BaseElement(self.driver, self.locator_select_address_type)

        address1_elm.enter_text(address1)
        if address2 is not None:
            address2_elm.enter_text(address2)
        if address3 is not None:
            address3_elm.enter_text(address3)
        city_elm.enter_text(city)
        state_elm.select_option(text=state)
        zip_elm.enter_text(zip_code)
        address_type_elm.select_option(text=address_type)

    # ----------------------

    def create_default_new_account(self, account_type, address="Po Box 70,Unionville,Virginia,22567"):
        """
        :param account_type: company or person
        :param address: address1,city,state,zip (All 4 mandatory address fields separated by coma and no space
        :return: create a new default account
        """
        current_datetime = datetime.now()
        unique_string = current_datetime.strftime("%y%m%d%H%M%S")

        if account_type.lower() == "company":
            self.input_company_name("company-" + unique_string)
        if account_type.lower() == "person":
            self.input_first_name("first-" + unique_string)
            self.input_last_name("last-" + unique_string)
        self.click_search_btn()
        self.create_new_account(account_type)

        if account_type.lower() == "company":
            self.input_office_phone(f"(650) {randint(101, 999)}-{randint(1001, 9999)}")
        self.input_primary_email(f"my_email{unique_string}@test.com")
        split_address = address.split(",")
        address1 = split_address[0]
        city = split_address[1]
        state = split_address[2]
        zip_code = split_address[3]
        address_type = choice(["Billing", "Business", "Home", "Other"])
        self.input_address(address1, city, state, zip_code, address_type)
        time.sleep(1)
        self.select_producer("Armstrong and Company", "100-002541 Armstrong (Premier)")
        self.click_btn_update()
