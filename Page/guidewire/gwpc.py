from Base.basepage import BasePage
from Base.baseelement import BaseElement
from selenium.webdriver.common.by import By
import definitions
from Util.logs import getLogger
from Util.screenshot import take_screenshot

URL = {
    "test": "http://localhost:8180/pc/PolicyCenter.do",
    "dev" : "somthing dev"
       }[definitions.global_dict["env"]]
TITLE = "[DEV mode - 10.2.2.1786] Guidewire PolicyCenter"


class GWPC(BasePage):

    log = getLogger()

    def __init__(self, driver):
        self.url = URL
        self.expected_title = TITLE
        super().__init__(driver=driver, url=self.url)
        self.locator_user_name = (By.XPATH, '//input[@name="Login-LoginScreen-LoginDV-username"]')
        self.locator_password = (By.XPATH, '//input[@name="Login-LoginScreen-LoginDV-password"]')
        self.locator_btn_login = (By.XPATH, '//div[@aria-label="Log In"]')
        self.locator_txt_my_summary = (By.XPATH, '//div[@class="gw-TitleBar--title"]')

    def input_user_name(self, text):
        username_input_elm = BaseElement(self.driver, self.locator_user_name)
        username_input_elm.enter_text(text)

    def input_password(self, text):
        pass_input_elm = BaseElement(self.driver, self.locator_password)
        pass_input_elm.enter_text(text)

    def click_log_in_button(self):
        btn_login = BaseElement(self.driver, self.locator_btn_login)
        btn_login.click_element()

    def is_login_successful(self):
        my_summary = BaseElement(self.driver, self.locator_txt_my_summary)
        return not (my_summary.element == "Element is not found.")

    def login(self, username, password):
        self.input_user_name(username)
        self.input_password(password)
        self.click_log_in_button()

        if self.is_login_successful():
            take_screenshot(self.driver)
            self.log.info("Login Successful")
        else:
            take_screenshot(self.driver)
            self.log.info("Unable to Login. Invalid Credentials")

