from Base.basepage import BasePage
from Base.baseelement import BaseElement
from selenium.webdriver.common.by import By
from Util.logs import getLogger
from Page.guidewire_pc.policies.LOBs.common import TitleToolbar


class NewSubmissionScreen(BasePage):
    log = getLogger()

    def __init__(self, driver):
        super().__init__(driver=driver, url=None)
        self._locator_eff_date_input = (By.XPATH, '//input[@class="gw-min-visible gw-DateValueWidget--dateInput"]')
        self._locator_base_state_dropdown = (
        By.XPATH, '//select[@name="NewSubmission-NewSubmissionScreen-ProductSettingsDV-DefaultBaseState"]')
        self._locator_effective_date_text = (By.XPATH, '//div[text()="Default Effective Date"]')
        self.title_toolbar = TitleToolbar(self.driver)

    @staticmethod
    def _locator_dynamic_lob_select_btn(lob):
        x_path = f'//div[text()="{lob}"]//ancestor::tr[1]//div[text()="Select"]'
        return By.XPATH, x_path

    def enter_eff_date(self, date):
        eff_date = BaseElement(self.driver, self._locator_eff_date_input)
        eff_date.enter_text(date)
        eff_date.press_tab_key()
        self.log.info(f"Enter effective Date - {date}")

    def select_base_state(self, state):
        base_state = BaseElement(self.driver, self._locator_base_state_dropdown)
        base_state.select_option(text=state)
        self.log.info(f"Select Base State - {state}")

    def select_lob_btn(self, lob):
        """
        :param lob: (options) - Workers' Compensation | Inland Marine | General Liability | Commercial Property |
        Commercial Package | Commercial Auto | Businessowners
        """

        title = self.title_toolbar.screen_title_text()

        BaseElement(self.driver, self._locator_effective_date_text).click_element()  # clicking outside with no impact
        BaseElement(self.driver, self._locator_effective_date_text).click_element()  # clicking outside with no impact
        lob_btn_elm = BaseElement(self.driver, self._locator_dynamic_lob_select_btn(lob))
        lob_btn_elm.click_element()
        self.log.info(f"Select LOB - {lob}")

        self.title_toolbar.screen_title_element.wait_till_text_to_be_not_present_in_element(title)