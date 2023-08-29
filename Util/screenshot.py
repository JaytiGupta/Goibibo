import definitions
import os
import random
import string
from datetime import datetime


# This Folder should be present in project directory
SCREENSHOTS_FOLDER_PATH = definitions.ROOT_DIR + "\\ResultFiles\\screenshots\\"


class Screenshot:
    test_run_started = False
    screenshot_folder = None

    @staticmethod
    def capture(driver):
        if definitions.CONFIG.take_screenshot:
            if not Screenshot.test_run_started:
                Screenshot._create_screenshot_folder()

            screenshot_filename = Screenshot._generate_unique_filename()
            driver.save_screenshot(screenshot_filename)
            return open(screenshot_filename, 'rb').read()
        else:
            pass

    @staticmethod
    def highlight_and_capture(driver, base_element):
        if definitions.CONFIG.take_screenshot:
            # Highlight the element by adding a red border
            driver.execute_script("arguments[0].style.border='2px solid red'", base_element.web_element)
            # Scroll to the element to ensure it's visible in the viewport
            driver.execute_script("arguments[0].scrollIntoView(true);", base_element.web_element)
            Screenshot.capture(driver)

    @staticmethod
    def _create_screenshot_folder(base_path=SCREENSHOTS_FOLDER_PATH):
        timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        folder_name = f"run_{timestamp}"
        Screenshot.screenshot_folder = os.path.join(base_path, folder_name)
        # Create the folder if it doesn't exist
        os.makedirs(Screenshot.screenshot_folder, exist_ok=True)
        Screenshot.test_run_started = True
        return Screenshot.screenshot_folder

    @staticmethod
    def _generate_unique_filename(file_extension=".png"):
        timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        random_string = ''.join(random.choices(string.ascii_lowercase + string.digits, k=6))
        filename = f"{timestamp}_{random_string}{file_extension}"
        return os.path.join(Screenshot.screenshot_folder, filename)

