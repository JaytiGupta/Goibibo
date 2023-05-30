from Base.basepage import BasePage
from Base.baseelement import BaseElement
from selenium.webdriver.common.by import By
from Page.guidewire.LOBs import common


#0000008751
class WorkersCompensation(BasePage):

    def __init__(self, driver):
        super().__init__(driver=driver, url=None)

        # Title Toolbar
        self.locator_Next_btn = (By.XPATH, '//div[@id="gw-center-title-toolbar"]//div[text()="Next"]')
        self.locator_Back_btn = (By.XPATH, '//div[@id="gw-center-title-toolbar"]//div[text()="Back"]')
        self.locator_Quote_btn = (By.XPATH, '//div[@id="gw-center-title-toolbar"]//div[@aria-label="Quote"]')
        self.locator_SaveDraft_btn = (By.XPATH, '//div[@id="gw-center-title-toolbar"]//div[@aria-label="Save Draft"]')
        self.locator_CloseOption_btn = (By.XPATH, '//div[@id="gw-center-title-toolbar"]//div[@aria-label="Close Options"]')

        # Screen - Policy Info (General Xpath -> //div[text()="{FIELD_TEXT}"]/parent::div//input)
        self.locator_FEIN_input_box = (By.XPATH, '//div[text()="FEIN"]/parent::div//input')
        self.locator_industry_code_input_box = (By.XPATH, '//div[text()="Industry Code"]/parent::div//input')
        self.locator_year_business_started_input_box = (By.XPATH, '//div[text()="Year Business Started"]/parent::div//input')
        self.locator_organization_type_dropdown = (By.XPATH, '//div[text()="Organization Type"]/parent::div//select')
        self.locator_term_type_dropdown = (By.XPATH, '//div[text()="Term Type"]/parent::div//select')
        self.locator_effective_date_input_box = (By.XPATH, '//div[text()="Effective Date"]/parent::div//input')
        self.locator_underwriter_companies_dropdown = (By.XPATH, '//select[contains(@name, "UWCompanyInputSet")]')

        #Screen - Location
        self.locator_add_new_location_btn = (By.XPATH, '//div[contains(text(), "New Loc")]')
        self.locator_address1 = (By.XPATH, '//div[contains(text(),"Address 1")]/following-sibling::div//div')
        self.locator_address2 = (By.XPATH, '//div[contains(text(),"Address 2")]/following-sibling::div//div')
        self.locator_address3 = (By.XPATH, '//div[contains(text(),"Address 3")]/following-sibling::div//div')
        self.locator_input_city = (By.XPATH, '//div[contains(text(),"City")]/following-sibling::div//div')
        self.locator_select_state = (By.XPATH, '//div[contains(text(),"State")]/following-sibling::div//div')
        self.locator_input_zip = (By.XPATH, '//div[contains(text(),"ZIP Code")]/following-sibling::div//div')
        self.locator_ok_btn = (By.XPATH, '//div[@id="LocationPopup-LocationScreen-Update"]')

        # Screen - WC Coverages
        self.locator_NCCI_interstate_id_input_box = (By.XPATH, '//div[contains(text(),"NCCI Interstate ID")]/parent::div//input')
        self.locator_AddClass_btn = (By.XPATH, '//div[@aria-label="Add Class"]')
        self.locator_governing_law_select = (By.XPATH, '//div[contains(@id, "WorkersCompClassesInputSet-0")]//tr[2]/td[2]//select')
        self.locator_location_select = (By.XPATH, '//div[contains(@id, "WorkersCompClassesInputSet-0")]//tr[2]/td[3]//select')
        self.locator_class_code_input_box = (By.XPATH, '//div[contains(@id, "WorkersCompClassesInputSet-0")]//tr[2]/td[4]//input')
        self.locator_employees_input_box = (By.XPATH, '//div[contains(@id, "WorkersCompClassesInputSet-0")]//tr[2]/td[6]//input')
        self.locator_if_any_check_box = (By.XPATH, '//div[contains(@id, "WorkersCompClassesInputSet-0")]//tr[2]/td[7]//input')
        self.locator_basis_input_box = (By.XPATH, '//div[contains(@id, "WorkersCompClassesInputSet-0")]//tr[2]/td[8]//input')

    # Qualification
    def select_qualification_radio_btn_option(self, question, answer):
        radio_btn = BaseElement(self.driver, common.locator_dynamic_radio_btn(question=question, answer=answer))
        radio_btn.click_element()

    def enter_qualification_input_box(self, question, answer):
        input_box = BaseElement(self.driver, common.locator_dynamic_input_box(question=question))
        input_box.enter_text(answer)

    def select_qualification_all_radio_btn_as_yes(self):
        all_radio_btn_elm = BaseElement(self.driver, common.locator_dynamic_radio_btn(question="all", answer="yes"))
        all_radio_btn_elm.click_all_elements()

    #PolicyInfo
    def input_FEIN(self, text):
        fein = BaseElement(self.driver, self.locator_FEIN_input_box)
        fein.enter_text(text) #text must be 9-digit no.

    def industry_code_input(self, code):
        industry_code = BaseElement(self.driver, self.locator_industry_code_input_box)
        industry_code.enter_text(code)

    def select_org_type(self, type_of_org):
        org_type = BaseElement(self.driver, self.locator_organization_type_dropdown)
        org_type.select_option(text=type_of_org)

    def term_type(self, pol_term):
        term_type = BaseElement(self.driver, self.locator_term_type_dropdown)
        if term_type == 'Annual':
             pass
        else:
             term_type.select_option(text=pol_term)

    def pol_eff_date(self, pol_date):
        eff_date = BaseElement(self.driver, self.locator_effective_date_input_box)
        eff_date.enter_text(pol_date)

    def uw_companies(self, uw_company):
        uw_comp = BaseElement(self.driver, self.locator_underwriter_companies_dropdown)
        uw_comp.select_option(text=uw_company)

    def click_next(self):
        next_btn = BaseElement(self.driver, self.locator_Next_btn)
        next_btn.click_element()

    # Location
    def add_new_location(self, address1, city, state, zip_code, address_type, address2=None, address3=None):
        address1_elm = BaseElement(self.driver, self.locator_address1)
        address2_elm = BaseElement(self.driver, self.locator_address2)
        address3_elm = BaseElement(self.driver, self.locator_address3)
        city_elm = BaseElement(self.driver, self.locator_input_city)
        state_elm = BaseElement(self.driver, self.locator_select_state)
        zip_elm = BaseElement(self.driver, self.locator_input_zip)

        address1_elm.enter_text(address1)
        if address2 is not None:
            address2_elm.enter_text(address2)
        if address3 is not None:
            address3_elm.enter_text(address3)
        city_elm.enter_text(city)
        state_elm.select_option(text=state)
        zip_elm.enter_text(zip_code)
        self.log.info(f"Page: Locations - new location added.")
        ok_btn = BaseElement(self.driver, self.locator_ok_btn)
        ok_btn.click_element()

    click_next()

    # WC Coverages - State Coverages
    def add_class(self, gov_law, location, code, emp_no, basis_value):
        governing_law = BaseElement(self.driver, self.locator_governing_law_select)
        governing_law.select_option(text=gov_law)
        loc = BaseElement(self.driver, self.locator_location_select)
        loc.select_option(type=location)
        class_code = BaseElement(self.driver, self.locator_class_code_input_box)
        class_code.enter_text(code)
        emp_number = BaseElement(self.driver, self.locator_employees_input_box)
        emp_number.enter_text(emp_no)
        basis = BaseElement(self.driver, self.locator_basis_input_box)
        basis.enter_text(basis_value)

     #WC Coverages - Policy Coverages and Exclusions
    # add code if required
    click_next()

    # Supplemental
    def select_supplemental_radio_btn_option(self, question, answer):
        radio_btn = BaseElement(self.driver, common.locator_dynamic_radio_btn(question=question, answer=answer))
        radio_btn.click_element()

    click_next()

    # WC Options
