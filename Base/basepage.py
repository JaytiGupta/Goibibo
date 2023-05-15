class BasePage:

    def __init__(self, driver, url):
        self.driver = driver
        self.url = url

    def go(self):
        self.driver.maximize_window()
        self.driver.get(self.url)

    # To get the title of the page
    def get_title(self):
        return self.driver.title


