from selenium import webdriver
from pytest import fixture
import definitions
from Util.logs import getLogger
from Util.read_json import config_data
from Page.guidewire_pc.login import Login

log = getLogger()


@fixture(scope="function")
def browser():
    # log = getLogger()
    log.info("Opening Chrome Browser.")
    yield webdriver.Chrome()


@fixture(scope="function")
def browser_pc(browser):
    # log = getLogger()
    log.info("Opening Guidewire Policy Center.")
    environment_data = config_data(definitions.CONFIG.env)
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
def take_screenshots(request):
    return request.config.getoption("--screenshot")


@fixture(scope='session', autouse=True)
def app_config(env, take_screenshots):
    # log = getLogger()
    log.info("************* Starting Execution *************")
    definitions.CONFIG.env = env.lower()
    definitions.CONFIG.take_screenshot = take_screenshots
    yield
    log.info("************* Execution complete *************")


if __name__ == "__main__":
    pass
