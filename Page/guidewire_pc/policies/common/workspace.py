from selenium.webdriver.common.by import By
from Base.baseelement import BaseElement
from Util.logs import getLogger


class Workspace:
    log = getLogger()

    def __init__(self, driver):
        self.driver = driver

    @property
    def workspace_area(self):
        locator = (By.XPATH, '//div[@id="gw-south-panel"]')
        return BaseElement(self.driver, locator)

    @property
    def validation_results(self):
        locator = (By.XPATH, '//div[text()="Validation Results"]')
        return BaseElement(self.driver, locator)

    @property
    def error(self):
        locator = (By.XPATH, '//div[@id="gw-south-panel"]//div[contains(text(),"Error")]')
        return BaseElement(self.driver, locator)

    @property
    def warning(self):
        locator = (By.XPATH, '//div[@id="gw-south-panel"]//div[contains(text(),"Warning")]')
        return BaseElement(self.driver, locator)

    @property
    def information(self):
        locator = (By.XPATH, '//div[@id="gw-south-panel"]//div[contains(text(),"Information")]')
        return BaseElement(self.driver, locator)

    @property
    def messages_types(self):
        locator = (By.XPATH, '//div[@class="gw-MessagesWidget--severity-sub-group"]')
        return BaseElement(self.driver, locator)

    def is_workspace_present(self):
        is_present =  self.workspace_area.is_element_present()
        if is_present:
            self.log.info("Workspace area is present.")
        else:
            self.log.info("Workspace area is not present.")
        return is_present

    def get_all_message_types(self) -> list:
        message_types = self.messages_types.get_all_elements_attribute("aria-label")
        return [message_type for message_type in message_types]



