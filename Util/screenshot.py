import os
import datetime
from definitions import ROOT_DIR


# To create unique folder names along with time stamp for storing screenshots
current_datetime = datetime.datetime.now()
save_path = current_datetime.strftime("%Y_%m_%d-%H_%M_%S")
os.mkdir(ROOT_DIR + f"\\Test Files\\screenshots\\{save_path}")


class Screenshot:

    def __init__(self, driver):
        self.driver = driver

    def capture(self):
        current_datetime = datetime.datetime.now()
        image_name = current_datetime.strftime("capture" + "%Y_%m_%d-%H_%M_%S%f" + ".png")
        self.driver.save_screenshot(ROOT_DIR + f"\\ResultFiles\\screenshots\\{save_path}\\{image_name}")

