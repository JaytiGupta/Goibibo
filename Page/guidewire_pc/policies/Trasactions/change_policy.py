from Base.basepage import BasePage
from Base.baseelement import BaseElement
from selenium.webdriver.common.by import By
from Util.logs import getLogger
from Page.guidewire_pc.policies.LOBs import common
from Page.guidewire_pc.policies.info_bar import InfoBar
from Page.guidewire_pc.policies.LOBs.work_comp import WorkersCompensation


class ChangePolicy(BasePage):
    log = getLogger()

    def __init__(self, driver):
        super().__init__(driver=driver, url=None)
        self.info_bar = InfoBar(self.driver)
        self.title_toolbar = common.TitleToolbar(self.driver)
        self.start_policy_change_screen = StartPolicyChange(self.driver)


class StartPolicyChange(BasePage):
    log = getLogger()

    def __init__(self, driver):
        super().__init__(driver=driver, url=None)

    @property
    def effective_date_input_box(self):
        locator = (By.XPATH, '//div[text()="Effective Date"]/following-sibling::div//input')
        return BaseElement(self.driver, locator)

    @property
    def description_input_box(self):
        locator = (By.XPATH, '//div[text()="Description"]/following-sibling::div//input')
        return BaseElement(self.driver, locator)

    def fill_all_details(self, effective_date, description=None):
        self.log.info(f"Start Policy Change Screen.")
        self.effective_date_input_box.click_element()
        if description is not None:
            self.description_input_box.enter_text(description)
            self.log.info(f"Description: {description}.")

        self.effective_date_input_box.enter_text(effective_date)
        self.log.info(f"Effective Date: {effective_date}.")

