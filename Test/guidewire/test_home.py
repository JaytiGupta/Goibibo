from Page.guidewire_pc.policy_center_home import PolicyCenterHome
from Page.guidewire_pc.accounts.account import Account
from Page.guidewire_pc.policies.policy import Policy
from Util.screenshot import Screenshot
from pytest import mark


def test_search_account(browser_pc):
    page = PolicyCenterHome(browser_pc)
    page.tab_bar.search_account("7325149628")
    account = Account(browser_pc)
    assert account.summary.account_summary_title_present()


def test_search_submission(browser_pc):
    page = PolicyCenterHome(browser_pc)
    page.tab_bar.search_submission("0001930088")


def test_search_policy(browser_pc):
        page = PolicyCenterHome(browser_pc)
        page.tab_bar.search_submission("7823570597")







