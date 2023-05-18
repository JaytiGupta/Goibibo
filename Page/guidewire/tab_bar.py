from Base.basepage import BasePage
from Base.baseelement import BaseElement
from selenium.webdriver.common.by import By


class TabBar(BasePage):

    def __init__(self, driver):
        super().__init__(driver=driver, url=None)
        self.locator_account_dropdown = (By.XPATH, '//div[@id="TabBar-AccountTab"]/div[@class="gw-action--expand-button"]')
        self.locator_policy_dropdown = (By.XPATH, '//div[@id="TabBar-PolicyTab"]/div[@class="gw-action--expand-button"]')
        self.locator_administration_btn = (By.XPATH, '//div[@id="TabBar-AdminTab"]//div[@aria-label="Administration"]')
        self.locator_administration_dropdown = (By.XPATH, '//div[@id="TabBar-AdminTab"]/div[@class="gw-action--expand-button"]')
        self.locator_account_input_box = (By.XPATH, '//div[@id="TabBar-AccountTab"]//input')
        self.locator_new_Account_btn = (By.XPATH, '//div[@id="TabBar-AccountTab"]//div[text()="New Account"]')
        self.locator_account_search_btn = (By.XPATH, '//div[@id="TabBar-AccountTab"]//span[@aria-label="gw-search-icon"]')
        self.locator_submission_input_box = (By.XPATH, '//input[@name="TabBar-PolicyTab-PolicyTab_SubmissionNumberSearchItem"]')
        self.locator_policy_input_box = (By.XPATH, '//input[@name="TabBar-PolicyTab-PolicyTab_PolicyRetrievalItem"]')
        self.locator_options_btn = (By.XPATH, '//div[@id="TabBar"]//div[@aria-label="settings"]')
        self.locator_options_logout = (By.XPATH, '//div[@id="TabBar"]//div[contains(text(), "Log Out")]')

    def account_dropdown(self):
        return BaseElement(self.driver, self.locator_account_dropdown)

    def policy_dropdown(self):
        return BaseElement(self.driver, self.locator_policy_dropdown)

    def administration_button(self):
        return BaseElement(self.driver, self.locator_administration_btn)

    def administration_dropdown(self):
        return BaseElement(self.driver, self.locator_administration_dropdown)

    def options_btn(self):
        return BaseElement(self.driver, self.locator_options_btn)

    def search_account(self, account_num):
        self.account_dropdown().click_element()
        input_box = BaseElement(self.driver, self.locator_account_input_box)
        input_box.enter_text(account_num)
        search_button = BaseElement(self.driver, self.locator_account_search_btn)
        search_button.click_element()

    def create_new_account_btn(self):
        self.account_dropdown().click_element()
        btn = BaseElement(self.driver, self.locator_new_Account_btn)
        btn.click_element()

    def search_submission(self, submission_num):
        self.policy_dropdown().click_element()
        input_box = BaseElement(self.driver, self.locator_submission_input_box)
        input_box.enter_text(submission_num)
        input_box.press_enter_key()

    def search_policy(self, policy_num):
        self.policy_dropdown().click_element()
        input_box = BaseElement(self.driver, self.locator_policy_input_box)
        input_box.enter_text(policy_num)
        input_box.press_enter_key()

    def go_to_admin(self):
        self.administration_button().click_element()

    def log_out_user(self):
        self.options_btn().click_element()
        sign_out_btn = BaseElement(self.driver, self.locator_options_logout)
        sign_out_btn.click_element()

