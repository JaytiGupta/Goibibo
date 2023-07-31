from Base.basepage import BasePage
from Base.baseelement import BaseElement
from selenium.webdriver.common.by import By
from Util.logs import getLogger
from Page.guidewire_pc.policies.LOBs import common
from Page.guidewire_pc.policies.common import screens


class Reinstate(BasePage):
    log = getLogger()

    def __init__(self, driver):
        super().__init__(driver=driver, url=None)
        self.title_toolbar = common.TitleToolbar(self.driver)
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

