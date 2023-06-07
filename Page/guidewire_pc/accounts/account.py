from Base.basepage import BasePage
from .account_summary import AccountSummary
from .create_account import CreateAccount


class Account(BasePage):

    def __init__(self, driver):
        super().__init__(driver=driver, url=None)
        self.summary = AccountSummary(self.driver)
        self.new_account = CreateAccount(self.driver)