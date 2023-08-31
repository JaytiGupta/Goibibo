from selenium.webdriver.common.by import By
from Base.baseelement import BaseElement
from Util.logs import getLogger


class Workspace:
    log = getLogger()

    def __init__(self, driver):
        self.driver = driver

    @property
    def workspace_area(self):  # always present hidden
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
    def clear_btn(self):
        locator = (By.XPATH, '//div[@id="gw-south-panel"]//div[contains(text(),"Clear")]')
        return BaseElement(self.driver, locator)

    @property
    def information(self):
        locator = (By.XPATH, '//div[@id="gw-south-panel"]//div[contains(text(),"Information")]')
        return BaseElement(self.driver, locator)

    @property
    def messages_types(self):
        locator = (By.XPATH, '//div[@class="gw-MessagesWidget--severity-sub-group"]')
        return BaseElement(self.driver, locator)

    def is_workspace_present(self) -> bool:

        workspace_present_and_visible = self.workspace_area.get_attribute("aria-hidden") is None

        if workspace_present_and_visible:
            self.log.info("Workspace area is present.")
        else:
            self.log.info("Workspace area is not present.")

        return workspace_present_and_visible

    def get_all_message_types(self) -> list:
        message_types = self.messages_types.get_all_elements_attribute("aria-label")
        self.log.info(f"Getting messages(types) - {', '.join(message_types)}")
        return [message_type for message_type in message_types]

    def has_error_messages(self):
        message_types = self.get_all_message_types()
        return any("error" in message_type.lower() for message_type in message_types)

    def clear_workspace(self):
        if self.has_error_messages():
            self.log.debug("Getting error.")
            raise Exception("Getting error.")
        else:
            self.clear_btn.click_element()
            self.log.debug("Clicked clear button at workspace")
            self.workspace_area.wait_till_text_to_be_present_in_attribute("aria-hidden", "true")

    def clear_workspace_old(self):
        self.clear_btn.click_element()
        self.log.debug("Clicked clear button at workspace")
        self.workspace_area.wait_till_text_to_be_present_in_attribute("aria-hidden", "true")

    # def clear_workspace(self):
