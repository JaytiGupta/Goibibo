import time


def highlight(self):
    """Highlights (blinks) a Selenium Webdriver element"""

    driver = self._parent

    def apply_style(s):
        driver.execute_script("arguments[0].setAttribute('style', arguments[1]);",
                              self, s)

    original_style = self.get_attribute('style')
    apply_style("background: yellow; border: 2px solid red;")
    time.sleep(.3)
    apply_style(original_style)


def get_attribute(self, param):
    pass