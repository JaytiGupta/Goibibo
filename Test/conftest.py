# Import statements
import allure
from allure_commons.types import AttachmentType
from selenium import webdriver
from pytest import fixture, hookimpl

# Project-specific imports
import definitions
from Util.logs import getLogger
from Util.read_json import config_data
from Page.guidewire_pc.login import Login
from Page.guidewire_pc.policy_center_home import PolicyCenterHome
from Util.screenshot import Screenshot


# Command-line options parsing
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


# Fixtures

@fixture(scope='session')
def env(request):
    return request.config.getoption("--env")


@fixture(scope='session')
def take_screenshots(request):
    return request.config.getoption("--screenshot")


@fixture(scope='session', autouse=True)
def app_config(env, take_screenshots):
    """
    Configure the test environment and finalize execution.

    This fixture sets up the test environment configuration based on command-line arguments,
    logs the start and completion of test execution, and ensures that the setup logic is
    performed only once per test session.

    :param env: Environment value fetched from command-line options.
    :param take_screenshots: Boolean indicating whether to capture screenshots during test execution.

    Usage:
    - The fixture is automatically used due to autouse=True.
    - The configuration is set up before the tests start and finalized after they are done.
    - The fixture_executed flag prevents redundant setup across multiple test runs.
    """
    if not hasattr(app_config, "fixture_executed"):
        log = getLogger()
        log.info("************* Starting Execution *************")
        definitions.CONFIG.env = "test" #env.lower()
        definitions.CONFIG.take_screenshot = False #take_screenshots

        yield
        log.info("************* Execution complete *************")
        app_config.fixture_executed = True
    else:
        yield


@fixture(scope="session")
def browser():
    getLogger().info("Opening Chrome Browser.")
    yield webdriver.Chrome()


@fixture(scope="function")
def browser_pc(browser):
    """
    This fixture initializes a WebDriver instance for PolicyCenter tests.

    It opens the browser, navigates to the base URL, logs in to the PolicyCenter application,
    and sets up the browser environment for testing.
    After the test function completes, it logs out the user from the application.

    Args:
    browser (WebDriver): WebDriver instance from the 'browser' fixture.

    Returns:
    WebDriver: WebDriver instance with PolicyCenter application logged in.
    """
    environment_data = config_data(definitions.CONFIG.env)
    browser.maximize_window()
    browser.get(environment_data.base_url)
    login_page = Login(browser)
    login_page.login(environment_data.username, environment_data.password)
    yield browser
    pc_home = PolicyCenterHome(browser)
    pc_home.tab_bar.log_out_user()


# Custom hook for test report generation
@hookimpl(hookwrapper=True, tryfirst=True)  # this is required for 'log_on_failure' fixture
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    setattr(item, "rep_" + rep.when, rep)
    return rep


# Fixture to log failures and attach screenshots
@fixture(autouse=True)
def log_on_failure(request, browser):
    yield
    item = request.node
    if item.rep_call.failed:
        screenshot = Screenshot.capture(browser)
        allure.attach(screenshot, attachment_type=AttachmentType.PNG)
