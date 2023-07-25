from Base.basepage import BasePage
from Base.baseelement import BaseElement
from selenium.webdriver.common.by import By
import definitions
from Util.logs import getLogger
from Page.guidewire_pc.tab_bar import TabBar
from Page.guidewire_pc.login import Login
from Util.read_json import config_data


# # URL = config_settings("test").base_url
# URL = {
#     "test": "http://localhost:8180/pc/PolicyCenter.do",
#     "dev" : "somthing dev"
#        }[definitions.global_dict["env"]]
TITLE = "[DEV mode - 10.2.2.1786] Guidewire PolicyCenter"


class PolicyCenterHome(BasePage):

    log = getLogger()

    def __init__(self, driver):
        super().__init__(driver=driver, url=None)
        self.expected_title = TITLE
        self.login_page = Login(self.driver)
        self.tab_bar = TabBar(self.driver)

