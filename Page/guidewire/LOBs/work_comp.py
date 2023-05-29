from Base.basepage import BasePage
from Base.baseelement import BaseElement
from selenium.webdriver.common.by import By


class NewSubmission(BasePage):

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

        # Screen - WC Coverages
        self.locator_NCCI_interstate_id_input_box = (By.XPATH, '//div[contains(text(),"NCCI Interstate ID")]/parent::div//input')
        self.locator_NCCI_Intrastate_id_input_box = (By.XPATH, '//div[contains(text(),"NCCI Intrastate ID")]/parent::div//input')
        self.locator_AddClass_btn = (By.XPATH, '//div[@aria-label="Add Class"]')
        self.locator_governing_law_select = (By.XPATH, '//div[contains(@id, "WorkersCompClassesInputSet-0")]//tr[2]/td[2]//select')
        self.locator_location_select = (By.XPATH, '//div[contains(@id, "WorkersCompClassesInputSet-0")]//tr[2]/td[3]//select')
        self.locator_class_code_input_box = (By.XPATH, '//div[contains(@id, "WorkersCompClassesInputSet-0")]//tr[2]/td[4]//input')
        self.locator_employees_input_box = (By.XPATH, '//div[contains(@id, "WorkersCompClassesInputSet-0")]//tr[2]/td[6]//input')
        self.locator_if_any_check_box = (By.XPATH, '//div[contains(@id, "WorkersCompClassesInputSet-0")]//tr[2]/td[7]//input')
        self.locator_basis_input_box = (By.XPATH, '//div[contains(@id, "WorkersCompClassesInputSet-0")]//tr[2]/td[8]//input')

        # Supplemental

    # Dynamic Locator - Qualification
    def locator_dynamic_qualification_radio_btn(self, question, answer):
        if answer.lower() == "yes":
            x_path = f'//div[contains(text(),"{question}")]/ancestor::tr//input[@type="radio"][@value="true"]'
        else:
            x_path = f'//div[contains(text(),"{question}")]/ancestor::tr//input[@type="radio"][@value="false"]'
        return (By.XPATH, x_path)

    def locator_dynamic_qualification_input_box(self, question):
        x_path = f'//div[contains(text(),"{question}")]/ancestor::tr//input[@value="true"]'
        return (By.XPATH, x_path)

    # Dynamic Locator - Supplemental
    def locator_dynamic_supplemental_radio_btn(self, question, answer):
        if answer.lower() == "yes":
            x_path = f'//div[contains(text(),"{question}")]/ancestor::tr//input[@type="radio"][@value="true"]'
        else:
            x_path = f'//div[contains(text(),"{question}")]/ancestor::tr//input[@type="radio"][@value="false"]'
        return (By.XPATH, x_path)

    # Qualification
    def select_qualification_radio_btn_option(self, question, answer):
        radio_btn = BaseElement(self.driver, self.locator_dynamic_qualification_radio_btn(question, answer))
        radio_btn.click_element()

    def enter_qualification_input_box(self, question, answer):
        input_box = BaseElement(self.driver, self.locator_dynamic_qualification_input_box(question))
        input_box.enter_text(answer)

    # Supplemental
    def select_supplemental_radio_btn_option(self, question, answer):
        radio_btn = BaseElement(self.driver, self.locator_dynamic_qualification_radio_btn(question, answer))
        radio_btn.click_element()



