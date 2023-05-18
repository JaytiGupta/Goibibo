from selenium.webdriver.common.alert import Alert
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:

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

    def accept_alert(self):
        try:
            WebDriverWait(self.driver, 3).until(EC.alert_is_present())
            alert = self.driver.switch_to.alert
            alert.accept()
            alert.accept()
        except:
            pass


