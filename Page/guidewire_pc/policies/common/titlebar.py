import time

from selenium.common import WebDriverException
from selenium.webdriver.common.by import By
from Util.logs import getLogger
from Base.basepage import BasePage
from Base.baseelement import BaseElement
from Page.guidewire_pc.policies.info_bar import InfoBar
from Page.guidewire_pc.policies.common.workspace import Workspace
from Page.guidewire_pc.policies.common.screens import RiskAnalysis
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class TitleToolbar(BasePage):
    log = getLogger()

    def __init__(self, driver):
        super().__init__(driver=driver, url=None)
        self.risk_analysis_screen = RiskAnalysis(self.driver)
        self.workspace = Workspace(self.driver)
        self.info_bar = InfoBar(self.driver)

    @property
    def screen_title_element(self):
        locator = (By.XPATH, '//div[@id="gw-center-title-toolbar"]//div[@role="heading"]')
        return BaseElement(self.driver, locator)

    @property
    def next_btn(self):
        locator = (By.XPATH, '//div[@id="gw-center-title-toolbar"]//div[contains(@aria-label, "Next")]')
        return BaseElement(self.driver, locator)

    @property
    def back_btn(self):
        locator = (By.XPATH, '//div[@id="gw-center-title-toolbar"]//div[text()="Back"]')
        return BaseElement(self.driver, locator)

    @property
    def quote_btn(self):
        locator = (By.XPATH, '//div[@id="gw-center-title-toolbar"]//div[@aria-label="Quote"]')
        return BaseElement(self.driver, locator)

    @property
    def save_draft_btn(self):
        locator = (By.XPATH, '//div[@id="gw-center-title-toolbar"]//div[@aria-label="Save Draft"]')
        return BaseElement(self.driver, locator)

    @property
    def close_option_btn(self):
        locator = (By.XPATH, '//div[@id="gw-center-title-toolbar"]//div[@aria-label="Close Options"]')
        return BaseElement(self.driver, locator)

    @property
    def reinstate_btn(self):
        locator = (By.XPATH, '//div[@id="gw-center-title-toolbar"]//div[@aria-label="Reinstate"]')
        return BaseElement(self.driver, locator)

    @property
    def bind_options_btn(self):
        locator = (By.XPATH, '//div[@id="gw-center-title-toolbar"]//div[@aria-label="Bind Options"]')
        return BaseElement(self.driver, locator)

    @property
    def bind_only_btn(self):
        locator = (By.XPATH, '//div[@id="gw-center-title-toolbar"]//div[@aria-label="Bind Only"]')
        return BaseElement(self.driver, locator)

    @property
    def issue_policy_btn(self):
        locator = (By.XPATH, '//div[@id="gw-center-title-toolbar"]//div[@aria-label="Issue Policy"]')
        return BaseElement(self.driver, locator)

    @property
    def cancel_now_btn(self):
        locator = (By.XPATH, '//div[@id="gw-center-title-toolbar"]//'
                             'div[contains(@id,"BindOptions")]//'
                             'div[@aria-label="Cancel Now"]')
        return BaseElement(self.driver, locator)

    @property
    def schedule_cancellation_btn(self):
        locator = (By.XPATH, '//div[@id="gw-center-title-toolbar"]//'
                             'div[contains(@id,"BindOptions")]//'
                             'div[@aria-label="Schedule Cancellation"]')
        return BaseElement(self.driver, locator)

    @property
    def details_btn(self):
        locator = (By.XPATH, '//div[@id="gw-center-title-toolbar"]//div[text()="Details"]')
        return BaseElement(self.driver, locator)

    def screen_title_text(self):
        text = self.screen_title_element.get_text()
        return text

    def wait_for_screen(self, screen_title_text):
        self.screen_title_element.wait_till_text_to_be_present_in_element(screen_title_text)

    def next(self):
        title = self.screen_title_text()
        self.next_btn.click_element()
        try:
            self.next_btn.wait_till_staleness_of_element()
        except WebDriverException:
            self.screen_title_element.wait_till_text_to_be_not_present_in_element(title)

    def navigate_till_screen(self, screen_title):
        actual_screen_title = self.screen_title_text()
        while screen_title != actual_screen_title:
            self.next()
            actual_screen_title = self.screen_title_text()

    def quote(self):  # TODO needs to update max depth for recursion
        initial_screen_title = self.screen_title_text()
        self.log.info(f"{initial_screen_title} screen")

        self.quote_btn.click_element()
        self.log.info("Clicked Quote button.")
        time.sleep(3)
        # Policy Quoted without any stop - reached quote screen after one click
        # Getting error, warnings in workspace
        # Pre-Quote issues

        if self.screen_title_text() == "Quote":
            self.log.info("Quoted successfully")
        elif self.screen_title_text() == "Pre-Quote Issues":
            self.log.info("Pre-Quote Issues screen")
            self.details_btn.click_element()
            self.log.debug("Navigate to Underwriter issues tab at Risk Analysis screen.")
            self.risk_analysis_screen.approve_all_uw_issues()
            self.log.debug("All underwriter issues approved.")
            self.wait_for_screen("Risk Analysis")
            self.quote()
        elif self.workspace.is_workspace_present():
            message_types = self.workspace.get_all_message_types()
            if any("error" in message_type.lower() for message_type in message_types):
                self.log.debug("Getting error and unable to quote")
                raise Exception("Getting error and unable to quote")
            else:
                self.quote()

    def bind_policy(self):
        self.bind_options_btn.click_element()
        self.bind_only_btn.click_element()
        self.log.info(f"Clicked Bind Only button.")

    def issue_policy(self): # TODO needs to update max depth for recursion
        initial_screen_title = self.screen_title_text()

        # bind option is not present for change policy transaction. Issue policy btn is on title toolbar.
        if self.bind_options_btn.is_element_present():
            self.bind_options_btn.click_element()

        self.issue_policy_btn.click_element()
        self.log.info(f"Clicked Issue Policy button.")
        self.accept_alert()

        # TODO: update need to wait for page after click, screen can be same, pre_quote or quote
        time.sleep(5)

        if self.screen_title_text() == "Submission Bound":
            self.log.info("Your Submission has been bound.")
        elif self.screen_title_text() == "Policy Change Bound":
            self.log.info("Your Policy Change has been bound.")
        elif self.screen_title_text() == initial_screen_title:
            self.log.info(f"{initial_screen_title} screen")
            if self.workspace.error.is_element_present():
                self.log.debug("Getting error and unable to quote")
                raise Exception("Getting error and unable to quote")
            elif self.workspace.warning.is_element_present():
                self.log.info("Getting warnings")
            # TODO elif Information
            self.issue_policy()

    def schedule_cancellation(self):
        pass

    def cancel_now(self):
        initial_screen_title = self.screen_title_text()
        self.bind_options_btn.click_element()
        self.cancel_now_btn.click_element()
        self.log.info(f"Clicked Cancel Now button.")
        self.accept_alert()
        self.screen_title_element.wait_till_text_to_be_not_present_in_element(initial_screen_title)
        if self.screen_title_text() == "Cancellation Bound":
            self.log.info("Your Cancellation has been bound.")

    def reinstate(self):
        initial_screen_title = self.screen_title_text()
        self.reinstate_btn.click_element()
        self.accept_alert()
        self.screen_title_element.wait_till_text_to_be_not_present_in_element(initial_screen_title)
        if self.screen_title_text() == "Reinstatement Bound":
            self.log.info("Your Reinstatement has been bound.")
