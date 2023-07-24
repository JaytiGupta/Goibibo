from Page.guidewire_pc.policy_center_home import PolicyCenterHome
from Page.guidewire_pc.accounts.account import Account
from Page.guidewire_pc.policies.policy import Policy
from Util.screenshot import Screenshot
from pytest import mark


@mark.skip
def test_website_is_available(pc):
    home_page = PolicyCenterHome(pc)
    home_page.go()
    assert home_page.get_title() == home_page.expected_title
    Screenshot.capture(pc)


@mark.skip
def test_user_is_able_to_login(pc):
    home_page = PolicyCenterHome(pc)
    home_page.login_page.login(username='su', password='gw')
    # assert home_page.login_page.is_login_successful()
    # take_screenshot(browser)


# @mark.skip
def test_search_account(pc):
    page = PolicyCenterHome(pc)
    # page.tab_bar.go_to_desktop()
    page.tab_bar.search_account("7325149628")
    account = Account(pc)
    assert account.summary.account_summary_title_present()


@mark.skip
def test_search_submission(pc):
    page = PolicyCenterHome(pc)
    page.tab_bar.go_to_desktop()
    # page.tab_bar.search_submission("0001930088")
    page.tab_bar.search_submission("0000079835")  # Amendment transaction
    # policy = Policy(browser)
    # assert "Workers' Compensation" in policy.info_bar.get_lob()
    page2 = Policy(pc)
    page2.work_comp.title_toolbar.next()
    a = page2.work_comp.forms_screen.all_form_list()
    print(a)








