from Base.basepage import BasePage
from Base.baseelement import BaseElement
from selenium.webdriver.common.by import By
from Util.logs import getLogger


class TabBar(BasePage):
    log = getLogger()

    def __init__(self, driver):
        super().__init__(driver=driver, url=None)
        self._locator_desktop_btn = (By.XPATH, '//div[@id="TabBar-DesktopTab"]//div[@aria-label="Desktop"]')
        self._locator_account_dropdown = (By.XPATH, '//div[@id="TabBar-AccountTab"]/div[@class="gw-action--expand-button"]')
        self._locator_policy_dropdown = (By.XPATH, '//div[@id="TabBar-PolicyTab"]/div[@class="gw-action--expand-button"]')
        self._locator_administration_btn = (By.XPATH, '//div[@id="TabBar-AdminTab"]//div[@aria-label="Administration"]')
        self._locator_administration_dropdown = (By.XPATH, '//div[@id="TabBar-AdminTab"]/div[@class="gw-action--expand-button"]')
        self._locator_account_input_box = (By.XPATH, '//div[@id="TabBar-AccountTab"]//input')
        self._locator_new_Account_btn = (By.XPATH, '//div[@id="TabBar-AccountTab"]//div[text()="New Account"]')
        self._locator_account_search_btn = (By.XPATH, '//div[@id="TabBar-AccountTab"]//span[@aria-label="gw-search-icon"]')
        self._locator_submission_input_box = (By.XPATH, '//input[@name="TabBar-PolicyTab-PolicyTab_SubmissionNumberSearchItem"]')
        self._locator_policy_input_box = (By.XPATH, '//input[@name="TabBar-PolicyTab-PolicyTab_PolicyRetrievalItem"]')
        self._locator_options_btn = (By.XPATH, '//div[@id="TabBar"]//div[@aria-label="settings"]')
        self._locator_options_logout = (By.XPATH, '//div[@id="TabBar"]//div[contains(text(), "Log Out")]')
        self._locator_logo = (By.XPATH, '//div[@aria-label="company logo"]')

    def policy_dropdown(self):
        return BaseElement(self.driver, self._locator_policy_dropdown)

    def options_btn(self):
        return BaseElement(self.driver, self._locator_options_btn)

    @property
    def account_dropdown_btn(self):
        return BaseElement(self.driver, self._locator_account_dropdown)

    def search_account(self, account_num):
        # account_dropdown_btn = BaseElement(self.driver, self._locator_account_dropdown)
        self.account_dropdown_btn.click_element()
        input_box = BaseElement(self.driver, self._locator_account_input_box)
        input_box.enter_text(account_num)
        search_button = BaseElement(self.driver, self._locator_account_search_btn)
        search_button.click_element()
        self.log.info(f"Search account {account_num}")

    def create_new_account_btn(self):
        account_dropdown_btn = BaseElement(self.driver, self._locator_account_dropdown)
        account_dropdown_btn.click_element()
        new_account_btn = BaseElement(self.driver, self._locator_new_Account_btn)
        new_account_btn.click_element()
        self.log.info(f"Click New Account button from Account dropdown.")

    def search_submission(self, submission_num):
        self.policy_dropdown().click_element()
        input_box = BaseElement(self.driver, self._locator_submission_input_box)
        input_box.enter_text(submission_num)
        input_box.press_enter_key()
        self.log.info(f"Search submission {submission_num}")

    def search_policy(self, policy_num):
        self.policy_dropdown().click_element()
        input_box = BaseElement(self.driver, self._locator_policy_input_box)
        input_box.enter_text(policy_num)
        input_box.press_enter_key()
        self.log.info(f"Search policy {policy_num}")

    def go_to_admin(self):
        elm = BaseElement(self.driver, self._locator_administration_btn)
        elm.click_element()
        self.log.info(f"Navigate to admin tab.")

    def log_out_user(self):
        self.options_btn().click_element()
        sign_out_btn = BaseElement(self.driver, self._locator_options_logout)
        sign_out_btn.click_element()
        self.log.info(f"Logged out.")

    def go_to_desktop(self):
        desktop_btn = BaseElement(self.driver, self._locator_desktop_btn)
        desktop_btn.click_element()
        self.log.info(f"Navigate to desktop.")
        logo = BaseElement(self.driver, self._locator_logo)
        logo.click_element()

