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
        self.locator_effective_date_text = (By.XPATH, '//div[text()="Default Effective Date"]')

    def locator_dynamic_lob_select_btn(self, lob):
        x_path = f'//div[text()="{lob}"]//ancestor::tr[1]//div[text()="Select"]'
        return (By.XPATH, x_path)

    def enter_eff_date(self, date):
        eff_date = BaseElement(self.driver, self.locator_eff_date_input)
        eff_date.enter_text(date)
        eff_date.press_tab_key()

    def select_base_state(self, state):
        base_state = BaseElement(self.driver, self.locator_base_state_dropdown)
        base_state.select_option(text=state)

    def select_lob_btn(self, lob):
        """
        :param lob: (options) - Workers' Compensation | Inland Marine | General Liability | Commercial Property |
        Commercial Package | Commercial Auto | Businessowners
        """
        BaseElement(self.driver, self.locator_effective_date_text).click_element()
        BaseElement(self.driver, self.locator_effective_date_text).click_element()
        locator = self.locator_dynamic_lob_select_btn(lob)
        BaseElement(self.driver, locator).click_element()

    def draft_sub(self):
        elm = BaseElement(self.driver, (By.XPATH, '//div[text()="Submission (Draft)"]'))
        return elm.is_element_present()