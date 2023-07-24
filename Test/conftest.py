from selenium import webdriver
from pytest import fixture
import definitions
from Util.logs import getLogger
from Test.config import Config
from Util.read_json import config_test
from Util.config import Config, Environment
from Page.guidewire_pc.login import Login


log = getLogger()


# @fixture(scope='session')
# def app_config(request):
#     env_option = request.config.getoption("--env")
#     screenshot_option = request.config.getoption("--screenshot")
#
#     env = Environment[env_option.upper()] if env_option else Environment.TEST
#     take_screenshots = screenshot_option
#
#     cfg = Config(env, take_screenshots)
#     return cfg


@fixture(autouse=True, scope="session")
def setup_before_tests(request):
    # Code to run before any test starts
    log.info("************* Starting Execution *************")
    definitions.set_value("take_screenshots", request.config.getoption("--screenshot"))
    definitions.set_value("env", request.config.getoption("--env"))
    yield
    # Code to run after all tests have finished (pytest_sessionfinish)
    print("\nAll tests have finished. Performing cleanup or final actions here.")
    log.info("************* Execution complete *************")


@fixture(scope="function")
def browser():
    log = getLogger()
    log.info("Opening Chrome Browser.")
    yield webdriver.Chrome()


@fixture(scope="function")
def browser_pc(request, browser):
    log = getLogger()
    log.info("Opening Guidewire Policy Center.")
    environment_data = config_test(request.config.getoption("--env"))
    # environment_data = config_test(definitions.global_dict["env"])
    browser.maximize_window()
    browser.get(environment_data.base_url)
    login_page = Login(browser)
    login_page.login(environment_data.username, environment_data.password)
    yield browser


def pytest_addoption(parser):
    parser.addoption(
        "--env",
        action="store",
        help="Environment to run tests against"
    )
    parser.addoption(
        "--screenshot",
        action="store_true",
        help="Capture screenshots during test execution"
    )


@fixture(scope='session')
def env(request):
    return request.config.getoption("--env")


@fixture(scope='session')
def app_config(env):
    cfg = Config(env)
    return cfg


# test_data = config_test(definitions.global_dict["env"])
file_path = definitions.ROOT_DIR + "/Data/login_data.csv"
test_data = [{'username': 'su', 'password': 'gw'}]
# test_data = csv_data_converter.get_rows(file_path, "username", "su")
# test_data = csv_data_converter.get_rows(file_path, "env", definitions.global_dict["env"])


@fixture(params=test_data)
def login_data(request):
    yield request.param


if __name__ == "__main__":
    pass


