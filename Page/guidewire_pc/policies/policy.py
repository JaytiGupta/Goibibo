from Base.basepage import BasePage
from Base.baseelement import BaseElement
from selenium.webdriver.common.by import By
from .policy_summary import PolicySummary
from .new_submission_screen import NewSubmissionScreen
from .LOBs.work_comp import WorkersCompensation
from .LOBs.commercial_auto import CommercialAuto
from .info_bar import InfoBar
from Util.logs import getLogger


class Policy(BasePage):
    log = getLogger()

    def __init__(self, driver):
        super().__init__(driver=driver, url=None)
        self.summary = PolicySummary(self.driver)
        self.new_submission_screen = NewSubmissionScreen(self.driver)
        self.work_comp = WorkersCompensation(self.driver)
        self.comm_auto = CommercialAuto(self.driver)
        self.info_bar = InfoBar(self.driver)

