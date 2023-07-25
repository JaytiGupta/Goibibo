from Page.guidewire_pc.policy_center_home import PolicyCenterHome
from Page.guidewire_pc.accounts.account import Account
from Util.screenshot import Screenshot
from pytest import mark


@mark.regression
def test_default_company_account_creation(browser_pc):
    page = PolicyCenterHome(browser_pc)
    page.tab_bar.create_new_account_btn()
    account = Account(browser_pc)
    account.new_account.create_default_new_account("Company", "VA")
    Screenshot.capture(browser_pc)
    assert account.summary.account_summary_title_present()


@mark.regression
def test_default_person_account_creation(browser_pc):
    page = PolicyCenterHome(browser_pc)
    page.tab_bar.create_new_account_btn()
    account = Account(browser_pc)
    account.new_account.create_default_new_account("Person", "NY")
    Screenshot.capture(browser_pc)
    assert account.summary.account_summary_title_present()
