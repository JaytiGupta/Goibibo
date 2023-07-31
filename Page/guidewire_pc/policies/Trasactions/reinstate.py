import time

from Base.basepage import BasePage
from Base.baseelement import BaseElement
from selenium.webdriver.common.by import By
from Util.logs import getLogger
from Page.guidewire_pc.policies.common.titlebar import TitleToolbar
from Page.guidewire_pc.policies.common import screens


class Reinstate(BasePage):
    log = getLogger()

    def __init__(self, driver):
        super().__init__(driver=driver, url=None)
        self.title_toolbar = TitleToolbar(self.driver)
        self.title_toolbar = ReinTitleToolbar(self.driver)
        self.start_reinstatement_screen = StartReinstatement(self.driver)
        self.risk_analysis_screen = screens.RiskAnalysis(self.driver)
        self.quote_screen = screens.Quote(self.driver)
        self.payment_screen = Payment(self.driver)


class StartReinstatement(BasePage):
    log = getLogger()

    def __init__(self, driver):
        super().__init__(driver=driver, url=None)

    @property
    def reason_dropdown(self):
        locator = (By.XPATH, '//div[text()="Reason"]/following-sibling::div//select')
        return BaseElement(self.driver, locator)

    @property
    def reason_description_input_box(self):
        locator = (By.XPATH, '//div[text()="Reason Description"]/following-sibling::div//textarea')
        return BaseElement(self.driver, locator)

    def fill_details(self, reason, reason_description=None):
        self.log.info(f"Start Reinstatement Screen.")
        self.reason_dropdown.select_option(text=reason)
        self.log.info(f"Reason: {reason}.")

        if reason_description is not None:
            self.reason_description_input_box.enter_text(reason_description)
            self.log.info(f"Reason description: {reason_description}.")


class Payment(BasePage):
    log = getLogger()

    def __init__(self, driver):
        super().__init__(driver=driver, url=None)
        self.SCREEN_TITLE = "Payment"


class ReinTitleToolbar(TitleToolbar):
    log = getLogger()

    @property
    def reinstate_btn(self):
        locator = (By.XPATH, '//div[@id="gw-center-title-toolbar"]//div[@aria-label="Reinstate"]')
        return BaseElement(self.driver, locator)

    def quote(self):
        self.next_btn_text.wait_till_text_to_be_present_in_element("Next")
        initial_screen_title = self.screen_title_text()
        self.log.info(f"{initial_screen_title} screen")
        self.quote_btn.click_element()
        self.log.info("Clicked Quote button.")
        time.sleep(3)

        if self.screen_title_text() == "Quote":
            self.log.info("Quoted successfully")
        elif self.workspace.is_workspace_present():
            message_types = self.workspace.get_all_message_types()
            if any("error" in message_type.lower() for message_type in message_types):
                self.log.debug("Getting error and unable to quote")
                raise Exception("Getting error and unable to quote")
            else:
                self.workspace.clear_btn.click_element()
                self.quote()

    def reinstate(self):
        initial_screen_title = self.screen_title_text()
        self.reinstate_btn.click_element()
        self.accept_alert()
        self.screen_title_element.wait_till_text_to_be_not_present_in_element(initial_screen_title)
        if self.screen_title_text() == "Reinstatement Bound":
            self.log.info("Your Reinstatement has been bound.")