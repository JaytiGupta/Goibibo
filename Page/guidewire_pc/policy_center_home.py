from Base.basepage import BasePage
from Util.logs import getLogger
from Page.guidewire_pc.tab_bar import TabBar
from Page.guidewire_pc.login import Login


TITLE = "[DEV mode - 10.2.2.1786] Guidewire PolicyCenter"


class PolicyCenterHome(BasePage):

    log = getLogger()

    def __init__(self, driver):
        super().__init__(driver=driver, url=None)
        self.expected_title = TITLE
        self.login_page = Login(self.driver)
        self.tab_bar = TabBar(self.driver)

