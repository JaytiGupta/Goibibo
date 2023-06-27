from selenium.webdriver.common.by import By
from Base.baseelement import BaseElement
from Base.basepage import BasePage
from Util.logs import getLogger


class Sidebar(BasePage):
    log = getLogger()

    def __init__(self, driver):
        super().__init__(driver=driver, url=None)

    @property
    def side_bar(self):
        locator = (By.XPATH, '//div[@aria-label="west panel"]')
        return BaseElement(self.driver, locator)

    @property
    def heading(self):
        locator = (By.XPATH, '//div[@aria-label="west panel"]//div[@role="heading"]')
        return BaseElement(self.driver, locator)

    def transaction_number(self) -> str:
        heading_text: str = self.heading.get_text()
        transaction_number: str = heading_text.split(" ")[-1]
        return transaction_number

