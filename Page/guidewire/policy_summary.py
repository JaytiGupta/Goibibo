from Base.basepage import BasePage
from Base.baseelement import BaseElement
from selenium.webdriver.common.by import By


class AccountSummary(BasePage):

    def __init__(self, driver):
        super().__init__(driver=driver, url=None)