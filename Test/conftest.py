import pytest
from selenium import webdriver
# from Util.screenshot import Screenshot
from Util.logs import getLogger
from definitions import set_value, ROOT_DIR, global_dict
from datetime import datetime
import os


# To create unique folder names along with time stamp for storing screenshots
current_datetime = datetime.now()
folder_name = current_datetime.strftime("%Y_%m_%d-%H_%M_%S")
set_value("screenshot_folder", folder_name)


@pytest.fixture(scope="session")
def browser():
    # return webdriver.Chrome()
    log = getLogger()
    os.mkdir(ROOT_DIR + f"\\ResultFiles\\screenshots\\{global_dict['screenshot_folder']}")
    yield webdriver.Chrome()
    log.info("Teardown")


# @pytest.fixture(scope="session")
# def picture(browser):
#     return Screenshot(browser)


@pytest.fixture(scope="session")
def homepage_url():
    return "https://www.goibibo.com/"


@pytest.fixture(scope="session")
def amazonpage_url():
    return "https://www.amazon.in/"


@pytest.fixture(params=[{"brand": "Sony", "size": "34inch"},
                        {"brand": "Samsung", "size": "24inch"},
                        {"brand": "Panasonic", "size": "52inch"}])
def tv_brand(request):
    tv = request.param
    return tv

