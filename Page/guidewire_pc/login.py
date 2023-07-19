from Base.basepage import BasePage
from Base.baseelement import BaseElement
from selenium.webdriver.common.by import By
import definitions
from Util.logs import getLogger
from Util.screenshot import take_screenshot


class Login(BasePage):

    log = getLogger()

    def __init__(self, driver):
        super().__init__(driver=driver, url=None)

    @property
    def _user_name_input_box(self):
        locator = (By.XPATH, '//input[@name="Login-LoginScreen-LoginDV-username"]')
        return BaseElement(self.driver, locator)

    @property
    def _password_input_box(self):
        locator = (By.XPATH, '//input[@name="Login-LoginScreen-LoginDV-password"]')
        return BaseElement(self.driver, locator)

    @property
    def login_button(self):
        locator = (By.XPATH, '//div[@aria-label="Log In"]')
        return BaseElement(self.driver, locator)

    @property
    def _home_screen_title(self):
        locator = (By.XPATH, '//div[@class="gw-TitleBar--title"]')
        return BaseElement(self.driver, locator)

    def login(self, username, password):
        self._user_name_input_box.enter_text(username)
        self._password_input_box.enter_text(password)
        self.login_button.click_element()

        if self._home_screen_title.is_element_present():
            take_screenshot(self.driver)
            self.log.info("Login Successful")
        else:
            take_screenshot(self.driver)
            self.log.info("Unable to Login. Invalid Credentials")

