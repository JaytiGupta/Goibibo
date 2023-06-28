import definitions
from Util import csv_data_converter
from Page.guidewire_pc.policy_center_home import PolicyCenterHome
from Page.guidewire_pc.accounts.account import Account
from Page.guidewire_pc.policies.policy import Policy
from Util.screenshot import take_screenshot
from Page.guidewire_pc.policies.common.workspace import Workspace
from Page.guidewire_pc.policies.common.workspace import Workspace


def test_scripts(browser):
    home_page = PolicyCenterHome(browser)
    home_page.go()
    home_page.login_page.login("su", "gw")

    PC = PolicyCenterHome(browser)
    PC.tab_bar.go_to_desktop()
    PC.tab_bar.search_submission('0000958285')

    policy = Policy(browser)

    wc_policy = policy.work_comp
    wc_policy.title_toolbar.navigate_till_screen("WC Coverages")
    wc_policy.title_toolbar.next()
    wc_policy.title_toolbar.next()
    wc_policy.title_toolbar.next()

    # wc_policy.title_toolbar.quote2()