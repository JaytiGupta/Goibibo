from selenium import webdriver
from pytest import fixture
import definitions
from Util.logs import getLogger
from Util.read_json import config_data
from Page.guidewire_pc.login import Login
from Page.guidewire_pc.policy_center_home import PolicyCenterHome


@fixture(scope="session")
def browser():
    getLogger().info("Opening Chrome Browser.")
    yield webdriver.Chrome()


@fixture(scope="function")
def browser_pc(browser):
    environment_data = config_data(definitions.CONFIG.env)
    browser.maximize_window()
    browser.get(environment_data.base_url)
    login_page = Login(browser)
    login_page.login(environment_data.username, environment_data.password)
    yield browser
    pc_home = PolicyCenterHome(browser)
    pc_home.tab_bar.log_out_user()


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


fixture_executed = False  # Session-scoped flag variable


# Define the finalizer function
def finalizer(log):
    log.info("************* Execution complete *************")


@fixture(scope='session', autouse=True)
def app_config(request, env, take_screenshots):
    global fixture_executed
    if not fixture_executed:
        log2 = getLogger()
        log2.info("************* Starting Execution *************")
        definitions.CONFIG.env = "test"  # env.lower()
        definitions.CONFIG.take_screenshot = take_screenshots
        fixture_executed = True  # Set the flag to True to indicate the fixture has been executed once

        # Add the finalizer to the request
        request.addfinalizer(lambda: finalizer(log2))

    # Yield here, fixture execution will resume after all tests are done
    yield
