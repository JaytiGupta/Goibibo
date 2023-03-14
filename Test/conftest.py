import pytest
from selenium import webdriver
from Util.screenshot import Screenshot


@pytest.fixture(scope="session")
def browser():
    # return webdriver.Chrome()
    yield webdriver.Chrome()
    print("Browser is closed")


@pytest.fixture(scope="session")
def picture(browser):
    return Screenshot(browser)


@pytest.fixture(scope="session")
def homepage_url():
    return "https://www.goibibo.com/"


@pytest.fixture(params=[{"brand": "Sony", "size": "34inch"},
                        {"brand": "Samsung", "size": "24inch"},
                        {"brand": "Panasonic", "size": "52inch"}])
def tv_brand(request):
    tv = request.param
    return tv

