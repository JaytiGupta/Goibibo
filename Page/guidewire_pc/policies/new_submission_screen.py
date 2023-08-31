from Base.basepage import BasePage
from Base.baseelement import BaseElement
from selenium.webdriver.common.by import By
from Util.logs import getLogger
from Page.guidewire_pc.policies.common.titlebar import TitleToolbar


class NewSubmissionScreen(BasePage):
    log = getLogger()

    def __init__(self, driver):
        super().__init__(driver=driver, url=None)
        self.select_lob = self._SelectLOB(self.driver)

    @property
    def _effective_date_input_box(self):
        locator = (By.XPATH, '//input[@class="gw-min-visible gw-DateValueWidget--dateInput"]')
        return BaseElement(self.driver, locator)

    @property
    def _base_state_dropdown(self):
        locator = (By.XPATH, '//select[@name="NewSubmission-NewSubmissionScreen-ProductSettingsDV-'
                             'DefaultBaseState"]')
        return BaseElement(self.driver, locator)

    def enter_effective_date(self, date):
        self._effective_date_input_box.enter_text(date)
        # self._effective_date_input_box.press_tab_key()
        self.log.info(f"Enter effective Date - {date}")

    def select_base_state(self, state):
        self._base_state_dropdown.select_option(text=state)
        self.log.info(f"Select Base State - {state}")

    class _SelectLOB:
        log = getLogger()

        def __init__(self, driver):
            self._driver = driver

        @property
        def _random_text_element_at_screen(self):
            locator = (By.XPATH, '//div[text()="Default Effective Date"]')
            return BaseElement(self._driver, locator)

        def _dynamic_lob_select_button_element(self, lob):
            locator = (By.XPATH, f'//div[text()="{lob}"]//ancestor::tr[1]//div[text()="Select"]')
            return BaseElement(self._driver, locator)

        def _select_lob(self, lob):
            title_toolbar = TitleToolbar(self._driver)
            title = title_toolbar.screen_title_text()

            self._random_text_element_at_screen.click_element() # clicking outside with no impact
            self._random_text_element_at_screen.click_element() # clicking outside with no impact

            self._dynamic_lob_select_button_element(lob).click_element()
            self.log.info(f"Select LOB: {lob}")

            # TODO - Change this to wait for Submission Text in sidebar
            title_toolbar.screen_title_element.wait_till_text_to_be_not_present_in_element(title)
            return None

        def business_owners(self):
            self._select_lob("Businessowners")
            return None

        def commercial_auto(self):
            self._select_lob("Commercial Auto")
            return None

        def commercial_package(self):
            self._select_lob("Commercial Package")
            return None

        def commercial_property(self):
            self._select_lob("Commercial Property")
            return None

        def general_liability(self):
            self._select_lob("General Liability")
            return None

        def inland_marine(self):
            self._select_lob("Inland Marine")
            return None

        def workers_compensation(self):
            self._select_lob("Workers' Compensation")
            return None
