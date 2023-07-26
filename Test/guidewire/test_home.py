from Page.guidewire_pc.policy_center_home import PolicyCenterHome
from Page.guidewire_pc.accounts.account import Account
from Page.guidewire_pc.policies.policy_summary import PolicySummary
from Util.screenshot import Screenshot
from pytest import mark
from Page.guidewire_pc.policies.common.sidebar import Sidebar


@mark.regression
@mark.smoke
def test_search_account(browser_pc):
    page = PolicyCenterHome(browser_pc)
    page.tab_bar.search_account("5635397383")
    account = Account(browser_pc)
    assert account.summary.account_summary_title_present()
    Screenshot.capture(browser_pc)


@mark.smoke
@mark.regression
def test_search_submission(browser_pc):
    submission_number = "0001930088"
    page = PolicyCenterHome(browser_pc)
    page.tab_bar.search_submission(submission_number)
    policy_sidebar = Sidebar(browser_pc)
    assert submission_number in policy_sidebar.heading.get_text()
    Screenshot.highlight_and_capture(browser_pc, policy_sidebar.heading)


@mark.smoke
@mark.regression
def test_search_policy(browser_pc):
    policy_number_to_search = "7823570597"
    page = PolicyCenterHome(browser_pc)
    page.tab_bar.search_policy(policy_number_to_search)
    policy_summary_screen = PolicySummary(browser_pc)
    policy_number_in_details = policy_summary_screen.get_policy_number()
    assert policy_number_to_search == policy_number_in_details
    Screenshot.capture(browser_pc)








