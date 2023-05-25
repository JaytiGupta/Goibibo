from Base.basepage import BasePage
from Base.baseelement import BaseElement
from selenium.webdriver.common.by import By


class NewSubmission(BasePage):

    def __init__(self, driver):
        super().__init__(driver=driver, url=None)
        self.locator_eff_date_input = (By.XPATH,
                                       '//input[@class="gw-min-visible gw-DateValueWidget--dateInput"]')
        self.locator_base_state_dropdown = (By.XPATH,
                                            '//select[@name="NewSubmission-NewSubmissionScreen-'
                                            'ProductSettingsDV-DefaultBaseState"]')
        self.locator_select_work_comp_btn = (By.XPATH,
                                             '//div[@id="NewSubmission-NewSubmissionScreen-ProductOffersDV'
                                             '-ProductSelectionLV-6-addSubmission"]')

        self.locator_select_business_owners_btn = (By.XPATH,
                                                   '//div[@id="NewSubmission-NewSubmissionScreen-'
                                                   'ProductOffersDV-ProductSelectionLV-0-addSubmission"]')

    def enter_eff_date(self, date):
        eff_date = BaseElement(self.driver, self.locator_eff_date_input)
        eff_date.enter_text(date)

    def select_base_state(self, state):
        base_state = BaseElement(self.driver, self.locator_base_state_dropdown)
        base_state.select_option(text=state)

    def select_lob_btn(self, lob):
        # elm = ''
        if lob == "Workers' Compensation":
            elm = BaseElement(self.driver, self.locator_select_work_comp_btn)
        elif lob == "Business Owners":
            elm = BaseElement(self.driver, self.locator_select_business_owners_btn)
        else:
            raise ValueError(f"No such LOB {lob}")
        elm.elm_clickable()
        elm.hover_and_click()

    def draft_sub(self):
        draft_sub_text = BaseElement(self.driver, (By.XPATH, '//div[text()="Submission (Draft)"]'))
        return not draft_sub_text.element == "Element is not found."
