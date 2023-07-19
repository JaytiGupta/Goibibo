from Base.basepage import BasePage
from Base.baseelement import BaseElement
from selenium.webdriver.common.by import By
from Util.logs import getLogger


class TitleBar(BasePage):

    log = getLogger()

    def __init__(self, driver):
        super().__init__(driver=driver, url=None)

    @property
    def screen_title(self):
        locator = (By.XPATH, '//div[@id="gw-center-title-toolbar"]//div[@role="heading"]')
        return BaseElement(self.driver, locator)

    def wait_for_screen(self, screen_heading_text):
        self.screen_title.wait_till_text_to_be_present_in_element(screen_heading_text)
