from selenium.common import TimeoutException, NoAlertPresentException
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from Util.logs import getLogger


class BasePage:

    log = getLogger()

    def __init__(self, driver, url):
        self.driver = driver
        self.driver.set_page_load_timeout(5)
        self.url = url

    def go(self):
        self.driver.maximize_window()
        self.driver.get(self.url)

    # To get the title of the page
    def get_title(self):
        return self.driver.title

    def get_alert(self):
        return WebDriverWait(self.driver, 5).until(EC.alert_is_present())

    def accept_alert(self):
        try:
            self.get_alert().accept()
            self.log.info("alert accepted")
        except:
            self.log.info("no alert")

