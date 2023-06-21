from selenium import webdriver
from pytest import fixture
# from Util.screenshot import Screenshot
import definitions
from Util import csv_data_converter
from Util.logs import getLogger
from definitions import set_value, ROOT_DIR, global_dict, create_screenshot_folder
from Util.csv_data_converter import list_of_dicts
from Test.config import Config
import os


@fixture(scope="session")
def browser():
    # return webdriver.Chrome()
    log = getLogger()
    log.info("************* Starting Execution *************")
    create_screenshot_folder()
    if global_dict["screenshots"]:
        os.mkdir(ROOT_DIR + f"\\ResultFiles\\screenshots\\{global_dict['screenshot_folder']}")
    yield webdriver.Chrome()
    log.info("************* Execution complete *************")

# -----------------------------


def pytest_addoption(parser):
    parser.addoption(
        "--env",
        action="store",
        help="Environment to run tests against"
    )


@fixture(scope='session')
def env(request):
    return request.config.getoption("--env")


@fixture(scope='session')
def app_config(env):
    cfg = Config(env)
    return cfg


# -----------------------------
file_path = definitions.ROOT_DIR + ""
test_data = csv_data_converter.get_rows(file_path, "user", "su")


@fixture(params=test_data)
def login_data(request):
    yield request.param


file_path = definitions.ROOT_DIR + "/Data/data_policy_change_work_comp.csv"
test_data = csv_data_converter.get_rows(file_path, "Test#", 1, 2)

file_path_ca = definitions.ROOT_DIR + "/Data/data_new_submission_comm_auto.csv"
test_data_ca = csv_data_converter.get_rows(file_path_ca, "Test", 1)


@fixture(params=test_data_ca)
def data(request):
    yield request.param


if __name__ == "__main__":
    # print(test_data)
    print(type(webdriver.Chrome()))


