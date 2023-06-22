import time
from Util import random_data
from Page.guidewire_pc.policy_center_home import PolicyCenterHome
from Page.guidewire_pc.accounts.account import Account
from Page.guidewire_pc.policies.policy import Policy
from Util.screenshot import take_screenshot
from pytest import mark


def test_website_is_available(browser):
    home_page = PolicyCenterHome(browser)
    home_page.go()
    assert home_page.get_title() == home_page.expected_title
    take_screenshot(browser)


def test_user_is_able_to_login(browser):
    home_page = PolicyCenterHome(browser)
    home_page.login_page.login(username='su', password='gw')
    # assert home_page.login_page.is_login_successful()
    # take_screenshot(browser)


@mark.skip
def test_search_account(browser):
    page = PolicyCenterHome(browser)
    page.tab_bar.go_to_desktop()
    page.tab_bar.search_account("7325149628")
    account = Account(browser)
    assert account.summary.account_summary_title_present()


@mark.skip
def test_search_submission(browser):
    page = PolicyCenterHome(browser)
    page.tab_bar.go_to_desktop()
    # page.tab_bar.search_submission("0001930088")
    page.tab_bar.search_submission("0000079835")  # Amendment transaction
    # policy = Policy(browser)
    # assert "Workers' Compensation" in policy.info_bar.get_lob()
    page2 = Policy(browser)
    page2.work_comp.title_toolbar.next()
    a = page2.work_comp.forms_screen.all_form_list()
    print(a)








