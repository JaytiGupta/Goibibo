import datetime
from definitions import ROOT_DIR, global_dict


def take_screenshot(driver, base_element=None):
    if global_dict["screenshots"]:
        file_path = create_file_path()
        if base_element is not None:
            base_element.scroll_to_element()
        driver.save_screenshot(file_path)
    else:
        pass


def highlight_element_and_take_screenshot(driver, base_element):
    if global_dict["screenshots"]:
        file_path = create_file_path()
        base_element.scroll_to_element()
        highlight_element(driver, base_element.web_element)
        driver.save_screenshot(file_path)
    else:
        pass


def create_file_path():
    current_datetime = datetime.datetime.now()
    image_name = current_datetime.strftime("capture" + "-%H%M%S%f" + ".png")
    file_path = ROOT_DIR + f"\\ResultFiles\\screenshots\\{global_dict['screenshot_folder']}\\{image_name}"
    return file_path


def highlight_element(driver, web_element):
    driver.execute_script("arguments[0].style.border='2px solid red'", web_element)
