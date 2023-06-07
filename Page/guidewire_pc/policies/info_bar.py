from Base.basepage import BasePage
from Base.baseelement import BaseElement
from selenium.webdriver.common.by import By


class InfoBar(BasePage):

    def __init__(self, driver):
        super().__init__(driver=driver, url=None)
        self._locator_job = (By.XPATH, '//div[@id="SubmissionWizard-JobWizardInfoBar-JobLabel"]')
        self._locator_lob = (By.XPATH, '//div[@id="SubmissionWizard-JobWizardInfoBar-LOBLabel"]')
        self._locator_effective_date = (By.XPATH, '//div[@id="SubmissionWizard-JobWizardInfoBar-EffectiveDate"]')
        self._locator_account_name = (By.XPATH, '//div[@id="SubmissionWizard-JobWizardInfoBar-AccountName"]')
        self._locator_account_number = (By.XPATH, '//div[@id="SubmissionWizard-JobWizardInfoBar-AccountNumber"]')
        self._locator_policy_number = (By.XPATH, '//div[@id="SubmissionWizard-JobWizardInfoBar-PolicyNumber"]')
        self._locator_underwriter = (By.XPATH, '//div[@id="SubmissionWizard-JobWizardInfoBar-Underwriter"]')

    def get_current_job(self):
        elm = BaseElement(self.driver, self._locator_job)
        return elm.get_text()

    def get_lob(self):
        elm = BaseElement(self.driver, self._locator_lob)
        return elm.get_text()

    def get_effective_date(self):
        pass

    def get_account_name(self):
        pass

    def get_account_number(self):
        pass

    def get_policy_number(self):
        pass

    def get_underwriter(self):
        pass
