import datetime
from definitions import ROOT_DIR, global_dict


def take_screenshot(driver, base_element=None):
    current_datetime = datetime.datetime.now()
    image_name = current_datetime.strftime("capture" + "-%H%M%S%f" + ".png")
    if not base_element is None:
        base_element.scroll_to_element()
    driver.save_screenshot(ROOT_DIR +
                           f"\\ResultFiles\\screenshots\\{global_dict['screenshot_folder']}\\{image_name}")



