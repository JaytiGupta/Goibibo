import os
import datetime

x = datetime.datetime.now()

# To create unique folder names along with time stamp for storing screenshots

folder_name = x.strftime("%Y_%m_%d-%H_%M_%S")
os.mkdir(os.environ['USERPROFILE'] + "\\Documents\\Automation\\screenshots\\{}".format(folder_name))


class Screenshot:

    def __init__(self, driver):
        self._parent = None
        self.driver = driver

    def capture(self):
        y = datetime.datetime.now()
        ss_name = y.strftime("capture" + "%Y_%m_%d-%H_%M_%S%f" + ".png")
        self.driver.save_screenshot(os.environ['USERPROFILE'] +
                                    '\\Documents\\Automation\\screenshots\\{}\\{}'.format(folder_name, ss_name))

