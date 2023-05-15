import pytest
from selenium import webdriver
# from Util.screenshot import Screenshot
from Util.logs import getLogger
from definitions import set_value, ROOT_DIR, global_dict, create_screenshot_folder
import os


@pytest.fixture(scope="session")
def browser():
    # return webdriver.Chrome()
    log = getLogger()
    log.info("************* Starting Execution *************")
    create_screenshot_folder()
    if global_dict["screenshots"]:
        os.mkdir(ROOT_DIR + f"\\ResultFiles\\screenshots\\{global_dict['screenshot_folder']}")
    yield webdriver.Chrome()
    log.info("************* Execution complete *************")


@pytest.fixture(scope="session")
def homepage_url():
    return "https://www.goibibo.com/"


@pytest.fixture(scope="session")
def amazonpage_url():
    return "https://www.amazon.in/"


