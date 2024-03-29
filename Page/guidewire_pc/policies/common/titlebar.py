import time
from selenium.webdriver.common.by import By
from Util.logs import getLogger
from Base.basepage import BasePage
from Base.baseelement import BaseElement
from Page.guidewire_pc.policies.info_bar import InfoBar
from Page.guidewire_pc.policies.common.workspace import Workspace
from Page.guidewire_pc.policies.common.screens import RiskAnalysis


class TitleToolbar(BasePage):
    log = getLogger()

    def __init__(self, driver):
        super().__init__(driver=driver, url=None)
        self.workspace = Workspace(self.driver)
        self.info_bar = InfoBar(self.driver)

    @property
    def screen_title_element(self):
        locator = (By.XPATH, '//div[@id="gw-center-title-toolbar"]//div[@role="heading"]')
        return BaseElement(self.driver, locator)

    @property
    def next_btn(self):
        locator = (By.XPATH, '//div[@id="gw-center-title-toolbar"]//div[contains(@aria-label, "Next")]/parent::div')
        return BaseElement(self.driver, locator)

    @property
    def next_btn_text(self):
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
        self.screen_title_element.wait_till_text_to_be_not_present_in_element(title)
        self.back_btn.wait_till_text_to_be_present_in_element("Back")
        self.screen_title_element.wait_till_text_to_be_present_in_element("")
        self.log.info(f"Navigating from {title} to {self.screen_title_text()} screen.")

    def navigate_till_screen(self, screen_title):
        actual_screen_title = self.screen_title_text()

        while screen_title != actual_screen_title:
            self.next()
            actual_screen_title = self.screen_title_text()

    def quote(self, recursive_calls=0, max_recursive_calls=2):
        if recursive_calls >= max_recursive_calls:
            self.log.error("Maximum recursive calls reached. Stopping.")
            raise Exception("Unable to quote.")

        initial_title = self.screen_title_text()
        self.quote_btn.click_element()
        self.log.info("Clicked Quote button.")

        # Working fine now. But if any problem comes time.sleep() for 1-2 second might be required here.
        if self.workspace.is_workspace_present():
            self.workspace.clear_workspace()
            self.quote_btn.click_element()
            self.log.info("Clicked Quote button.")

        self.screen_title_element.wait_till_text_to_be_not_present_in_element(initial_title)
        self.screen_title_element.wait_till_text_to_be_present_in_element("")

        if self.screen_title_text() == "Quote":
            self.log.info("Quoted successfully")
        elif self.screen_title_text() == "Pre-Quote Issues":
            self.resolve_pre_quote_issues()
            self.quote(recursive_calls + 1, max_recursive_calls)

    def resolve_pre_quote_issues(self):
        self.log.info("Pre-Quote Issues screen")
        self.details_btn.click_element()
        self.wait_for_screen("Risk Analysis")
        self.log.debug("Navigate to Underwriter issues tab at Risk Analysis screen.")
        risk_analysis_screen = RiskAnalysis(self.driver)
        risk_analysis_screen.approve_all_uw_issues()
        self.log.debug("All underwriter issues approved.")
        self.wait_for_screen("Risk Analysis")

    def bind_policy(self):
        self.bind_options_btn.click_element()
        self.bind_only_btn.click_element()
        self.log.info(f"Clicked Bind Only button.")

    def click_issue_btn(self):
        # bind dropdown option is not present for change policy transaction.
        # Issue policy btn is on title toolbar.
        if self.bind_options_btn.is_element_present():
            self.bind_options_btn.click_element()
        self.issue_policy_btn.click_element()
        self.log.info(f"Clicked Issue Policy button.")
        self.accept_alert()

    def issue_policy(self):
        initial_title = self.screen_title_text()
        self.click_issue_btn()

        # Working fine now. But if any problem comes time.sleep() for 1-2 second might be required here.
        if self.workspace.is_workspace_present():
            self.workspace.clear_workspace()
            self.click_issue_btn()

        self.screen_title_element.wait_till_text_to_be_not_present_in_element(initial_title)
        self.screen_title_element.wait_till_text_to_be_present_in_element("")

        if self.screen_title_text() == "Submission Bound":
            self.log.info("Your Submission has been bound.")
        elif self.screen_title_text() == "Policy Change Bound":
            self.log.info("Your Policy Change has been bound.")

    # def issue_policy_old(self, recursive_calls=0, max_recursive_calls=2):
    #     if recursive_calls >= max_recursive_calls:
    #         self.log.error("Maximum recursive calls reached. Stopping.")
    #         raise Exception("Unable to Issue Policy.")
    #
    #     # bind option is not present for change policy transaction.
    #     # Issue policy btn is on title toolbar.
    #     if self.bind_options_btn.is_element_present():
    #         self.bind_options_btn.click_element()
    #
    #     self.issue_policy_btn.click_element()
    #     self.log.info(f"Clicked Issue Policy button.")
    #     self.accept_alert()
    #
    #
    #     time.sleep(3)
    #
    #     if self.screen_title_text() == "Submission Bound":
    #         self.log.info("Your Submission has been bound.")
    #     elif self.screen_title_text() == "Policy Change Bound":
    #         self.log.info("Your Policy Change has been bound.")
    #     elif self.workspace.is_workspace_present():
    #         if self.workspace.has_error_messages():
    #             self.log.debug("Getting error and unable to issue")
    #             raise Exception("Getting error. Hence unable to Issue Policy")
    #         else:
    #             self.workspace.clear_btn.click_element()
    #             self.issue_policy_old(recursive_calls + 1, max_recursive_calls)
    #
    # def quote_old(self, recursive_calls=0, max_recursive_calls=6):
    #     if recursive_calls >= max_recursive_calls:
    #         self.log.error("Maximum recursive calls reached. Stopping.")
    #         raise Exception("Unable to quote.")
    #
    #     # self.back_btn.wait_till_text_to_be_present_in_element("Back")
    #     self.quote_btn.click_element()
    #     self.log.info("Clicked Quote button.")
    #     time.sleep(3)
    #     self.screen_title_element.wait_till_text_to_be_present_in_element("")
    #     self.back_btn.wait_till_text_to_be_present_in_element("Back")
    #
    #     if self.screen_title_text() == "Quote":
    #         self.log.info("Quoted successfully")
    #     elif self.screen_title_text() == "Pre-Quote Issues":
    #         self.resolve_pre_quote_issues()
    #         self.quote_old(recursive_calls + 1, max_recursive_calls)
    #     elif self.workspace.is_workspace_present():
    #         if self.workspace.has_error_messages():
    #             self.log.debug("Getting error and unable to quote")
    #             raise Exception("Getting error. Hence unable to quote")
    #         else:
    #             self.workspace.clear_workspace()
    #         self.quote_old(recursive_calls + 1, max_recursive_calls)
