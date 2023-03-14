
"""
import time
from selenium import webdriver
from Page.forex import Forex
from Page.homepage import HomePage
from pytest import mark

driver = webdriver.Chrome()
page = HomePage(driver)
page.go()
page.forex_btn().click_element()

p = driver.current_window_handle
parent = driver.window_handles[0]
chld = driver.window_handles[1]
driver.switch_to.window(chld)

forexpage = Forex(driver)
forexpage.select_city("Chennai")

@mark.skip
def test_currency_you_have():
    assert forexpage.currency_you_have_text() == 'Indian Rupee'

@mark.skip
def test_currency_you_want():
    assert forexpage.currency_you_want_text() == 'US Dollar'

@mark.skip
def test_total_amt():
    forexpage.forex_amount(1000)
    rate_usdollar = float(forexpage.get_rate())
    forexpage.click_add_btn()
    forexpage.currency_want_dropdown("Euro")
    forexpage.forex_amount(2000)
    rate_euro = float(forexpage.get_rate())
    forexpage.click_add_btn()
    expected_rate = 1000 * rate_usdollar + 2000 * rate_euro
    actual_rate = float(forexpage.get_total_amt())
    assert expected_rate == actual_rate
    time.sleep(5)
"""
#
# exception handling ------- 2
# reporting --------- 3
# logs --------- 5
# add 8-10 test cases with lists/collections etc...   ----- 1 with each feature
# parallel/linear execution ------- 6
# pass URL as parameter  ------ 1 (create config file for URL)
#  github (try this first) /gitlab ------ 4

