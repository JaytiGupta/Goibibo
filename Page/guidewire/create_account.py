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
        self.locator_office_phone = (By.XPATH, '//div[contains(text(),"Office Phone")]/following-sibling::div')
        self.locator_primary_email = (By.XPATH, '//div[contains(text(),"Primary Email")]/following-sibling::div')
        self.locator_address1 = (By.XPATH, '//div[contains(text(),"Address 1")]/following-sibling::div')
        self.locator_input_city = (By.XPATH, '//div[contains(text(),"City")]/following-sibling::div')
        self.locator_input_state = (By.XPATH, '//div[contains(text(),"State")]/following-sibling::div')
        self.locator_input_zip = (By.XPATH, '//div[contains(text(),"ZIP Code")]/following-sibling::div')
        self.locator_input_address_type = (By.XPATH, '//div[contains(text(),"Address Type")]/following-sibling::div')
        self.locator_input_org = (By.XPATH, '//div[contains(text(),"Organization Type")]/following-sibling::div')
        self.locator_input_producer_org_search_btn = (By.XPATH,
                                                      '//div[@id="CreateAccount-CreateAccountScreen-CreateAccountDV-'
                                                      'ProducerSelectionInputSet-Producer-SelectOrganization"]')
        self.locator_input_producer_org_name = (By.XPATH, '//input[@name="OrganizationSearchPopup-'
                                                          'OrganizationSearchPopupScreen-OrganizationSearchDV-'
                                                          'GlobalContactNameInputSet-Name"]')
        self.locator_input_producer_org_search_btn2 = (By.XPATH, '//div[@id="OrganizationSearchPopup-'
                                                      'OrganizationSearchPopupScreen-OrganizationSearchDV-'
                                                      'SearchAndResetInputSet-SearchLinksInputSet-Search"]')
        self.locator_update_btn = (By.XPATH, '//div[@aria-label="Update"]')

    # Page1 - Enter Account Information

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

    def validate_zero_results(self):
        zero_results = BaseElement(self.driver, self.locator_zero_results)
        if zero_results == "The search returned zero results.":
            pass
    #         TODO log info for no matching account found
        else
    #         TODO click on the first search result

    def create_new_account(self, type):
        new_account_btn = BaseElement(self.driver, self.locator_new_account_btn)
        new_account_btn.click_element()
        if type == "Company":
            BaseElement(self.driver, self.locator_company_dropdown).click_element()
        elif type == "Person":
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

    def input_state(self, text):
        state = BaseElement(self.driver, self.locator_input_state)
        state.enter_text(text)

    def input_zip(self, text):
        zip = BaseElement(self.driver, self.locator_input_zip)
        zip.enter_text(text)

    def select_address_type(self):
        address_type = BaseElement(self.driver, self.locator_input_address_type)
        address_type.click_element()
        # TODO code for selecting from dropdown

    def select_org(self):
        org_dropdown = BaseElement(self.driver, self.locator_input_org)
        org_dropdown.click_element()
    #     TODO code for selecting from dropdown

    def select_producer(self, text):
        producer_search_btn = BaseElement(self.driver, self.locator_input_producer_org_search_btn)
        producer_search_btn.click_element()
        producer_org_name = BaseElement(self.driver, self.locator_input_producer_org_name)
        producer_org_name.enter_text(text)
        search_btn2 = BaseElement(self.driver, self.locator_input_producer_org_search_btn2)
        search_btn2.click_element()
    # TODO select from the list of producers

    def update_btn(self):
        update_btn = BaseElement(self.driver, self.locator_update_btn)
        update_btn.click_element()







