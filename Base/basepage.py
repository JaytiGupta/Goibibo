from selenium.common import NoAlertPresentException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from Util.logs import getLogger
from selenium import webdriver


class BasePage:

    log = getLogger()

    def __init__(self, driver: webdriver.Chrome, url):
        self.driver = driver
        self.url = url

    def go(self):
        self.driver.maximize_window()
        self.driver.get(self.url)

    # To get the title of the page
    def get_title(self):
        return self.driver.title

    def accept_alert(self):
        try:
            alert = self.driver.switch_to.alert
            alert.accept()
            self.log.info("alert accepted")
        except NoAlertPresentException:
            pass
