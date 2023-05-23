from Base.basepage import BasePage
from Base.baseelement import BaseElement
from selenium.webdriver.common.by import By


class AccountSummary(BasePage):

    def __init__(self, driver):
        super().__init__(driver=driver, url=None)
        self.locator_account_number = (By.XPATH, '//div[text()="Account No"]/following-sibling::div')
        self.locator_account_holder_name = (By.XPATH, '//div[text()="Account Holder"]/following-sibling::div')
        self.locator_new_submission_btn = (By.XPATH, '//div[@role="button"]//div[text()="New Submission"]')

    def get_account_number(self):
        elm = BaseElement(self.driver, self.locator_account_number)
        return elm.get_text()

    def get_account_holder_name(self):
        elm = BaseElement(self.driver, self.locator_account_holder_name)
        return elm.get_text()

    def click_new_submission(self):
        elm = BaseElement(self.driver, self.locator_new_submission_btn)
        elm.click_element()