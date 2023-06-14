from Base.basepage import BasePage
from Base.baseelement import BaseElement
from selenium.webdriver.common.by import By
from Util.logs import getLogger


# 1933106343
class PolicySummary(BasePage):
    log = getLogger()

    def __init__(self, driver):
        super().__init__(driver=driver, url=None)
        self.new_transaction = NewTransaction(self.driver)


class NewTransaction(BasePage):
    log = getLogger()

    def __init__(self, driver):
        super().__init__(driver=driver, url=None)

    @property
    def _new_transaction_button(self):
        locator = (By.XPATH, '//div[text()="New Transaction"]')
        return BaseElement(self.driver, locator)

    def _transaction_type(self, transaction):
        locator = (By.XPATH, f'//div[text()="New Transaction"]/parent::div/'
                             f'following-sibling::div[@role="menu"]//div[text()="{transaction}"]')
        return BaseElement(self.driver, locator)

    def _select_transaction(self, transaction):
        """
        :param transaction: Change Policy, Cancel Policy, Renew Policy
        """
        self._new_transaction_button.click_element()
        self._transaction_type(transaction).click_element()
        return None

    def change_policy(self):
        self._select_transaction("Change Policy")

    def cancel_policy(self):
        self._select_transaction("Cancel Policy")

    def renew_policy(self):
        self._select_transaction("Renew Policy")

    def reinstate_policy(self):
        self._select_transaction("Reinstate Policy")
