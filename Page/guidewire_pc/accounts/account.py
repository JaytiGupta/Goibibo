from Base.basepage import BasePage
from .account_summary import AccountSummary
from .new_account import NewAccount


class Account(BasePage):

    def __init__(self, driver):
        super().__init__(driver=driver, url=None)
        self.summary = AccountSummary(self.driver)
        self.new_account = NewAccount(self.driver)