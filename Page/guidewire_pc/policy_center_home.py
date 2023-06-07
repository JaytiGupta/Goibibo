from Base.basepage import BasePage
from Base.baseelement import BaseElement
from selenium.webdriver.common.by import By
import definitions
from Util.logs import getLogger
from Util.screenshot import take_screenshot
from .tab_bar import TabBar
from .login import Login


URL = {
    "test": "http://localhost:8180/pc/PolicyCenter.do",
    "dev" : "somthing dev"
       }[definitions.global_dict["env"]]
TITLE = "[DEV mode - 10.2.2.1786] Guidewire PolicyCenter"


class PolicyCenterHome(BasePage):

    log = getLogger()

    def __init__(self, driver):
        super().__init__(driver=driver, url=URL)
        self.expected_title = TITLE
        self.login_page = Login(self.driver)
        self.tab_bar = TabBar(self.driver)