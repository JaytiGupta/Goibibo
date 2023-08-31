import time

from Base.basepage import BasePage
from Base.baseelement import BaseElement
from selenium.webdriver.common.by import By
from Util.logs import getLogger
from Page.guidewire_pc.policies.common.titlebar import TitleToolbar


class Cancel(BasePage):
    log = getLogger()

    def __init__(self, driver):
        super().__init__(driver=driver, url=None)
        self.title_toolbar = CancelTitleToolbar(self.driver)
        self.refund_method = None
        self.start_cancellation_for_policy_screen = StartCancellationForPolicy(self.driver)
        self.confirmation_screen = Confirmation(self.driver)


class CancelTitleToolbar(TitleToolbar):
    log = getLogger()

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


class StartCancellationForPolicy(BasePage):
    log = getLogger()

    def __init__(self, driver):
        super().__init__(driver=driver, url=None)
        self.refund_method = None

    @property
    def source_dropdown(self):
        locator = (By.XPATH, '//div[text()="Source"]/following-sibling::div//select')
        return BaseElement(self.driver, locator)

    @property
    def reason_dropdown(self):
        locator = (By.XPATH, '//div[text()="Reason"]/following-sibling::div//select')
        return BaseElement(self.driver, locator)

    @property
    def reason_description_input_box(self):
        locator = (By.XPATH, '//div[text()="Reason Description"]/following-sibling::div//textarea')
        return BaseElement(self.driver, locator)

    @property
    def refund_method_text_elm(self):
        locator = (By.XPATH, '//div[text()="Refund Method"]/following-sibling::div//div[@class="gw-label"]')
        return BaseElement(self.driver, locator)

    @property
    def cancellation_effective_date(self):
        locator = (By.XPATH, '//div[text()="Cancellation Effective Date"]/following-sibling::div//input')
        return BaseElement(self.driver, locator)

    @property
    def cancellation_effective_date_text_elm_for_flat_cancel(self):
        locator = (By.XPATH, '//div[text()="Cancellation Effective Date"]/following-sibling::div'
                             '//div[@class="gw-value-readonly-wrapper"]')
        return BaseElement(self.driver, locator)

    @property
    def start_cancellation_button(self):
        locator = (By.XPATH, '//div[@role="button"]//div[@aria-label="Start Cancellation"]')
        return BaseElement(self.driver, locator)

    @property
    def cancel_button(self):
        locator = (By.XPATH, '//div[@role="button"]//div[@aria-label="Cancel"]')
        return BaseElement(self.driver, locator)

    def fill_details(self, source, reason, reason_description=None, effective_date=None):
        self.log.info(f"'Start Cancellation For Policy' Screen.")
        self.source_dropdown.select_option(text=source)
        time.sleep(1)
        self.reason_dropdown.select_option(text=reason)
        self.log.info(f"Source: {source}.")
        self.log.info(f"Reason: {reason}.")

        if reason_description is not None:
            self.reason_description_input_box.enter_text(reason_description)
            self.log.info(f"Reason description: {reason_description}.")

        self.refund_method = self.refund_method_text_elm.get_text()
        self.log.info(f"Refund method is {self.refund_method}")

        if (self.refund_method == "Flat") and (effective_date is not None):
            flat_cancellation_effective_date = self.cancellation_effective_date_text_elm_for_flat_cancel
            self.log.info(f"Cancellation Effective Date is not editable for Flat cancellation. "
                     f"Cancellation Effective Date is {flat_cancellation_effective_date} ")
            self.cancellation_effective_date.enter_text(effective_date)

    def click_start_cancellation_button(self):
        self.start_cancellation_button.click_element()
        self.start_cancellation_button.wait_till_element_not_present()
        self.log.info("click 'start cancellation' button.")
        self.log.info("Navigate to 'Confirmation' screen")


class Confirmation(BasePage):
    log = getLogger()

    def __init__(self, driver):
        super().__init__(driver=driver, url=None)

    @property
    def _total_cost_elm(self):
        locator = (By.XPATH, '//div[contains(text(), "Total Cost: $")]')
        return BaseElement(self.driver, locator)

    def get_total_cost(self):
        total_cost_string = self._total_cost_elm.get_text()
        total_cost = float(total_cost_string.split("$")[1])
        self.log.info(f"{total_cost_string}")
        return total_cost
