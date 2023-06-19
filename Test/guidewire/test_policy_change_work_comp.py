import time
from Util import random_address
from Page.guidewire_pc.policy_center_home import PolicyCenterHome
from Page.guidewire_pc.accounts.account import Account
from Page.guidewire_pc.policies.policy import Policy
from Page.guidewire_pc.policies.Trasactions.change_policy import ChangePolicy
from Util.screenshot import take_screenshot
from pytest import mark


def test_login(browser):
    home_page = PolicyCenterHome(browser)
    home_page.go()
    home_page.login_page.login(username='su', password='gw')


@mark.skip
def test_work_comp_change_policy_transaction(browser):
    PC = PolicyCenterHome(browser)
    PC.tab_bar.go_to_desktop()
    PC.tab_bar.search_policy("2488493129")

    policy = Policy(browser)
    policy.summary.new_transaction.change_policy()

    amendment = ChangePolicy(browser)
    amendment.start_policy_change_screen.fill_all_details("06/15/2023", "test")
    amendment.title_toolbar.next()

    # Policy Info Screen
    wc_policy = policy.work_comp
    wc_policy.navigate_till_screen("WC Options")
    wc_policy.wc_options_screen.add_wc_option("Federal Liability")
    wc_policy.wc_options_screen.add_federal_class(location_index=1,
                                                  class_code=7333,
                                                  emp_no=15,
                                                  basis_value=5000)

    wc_policy.navigate_till_screen("Policy Review")

    wc_policy.title_toolbar.quote()
    # Quote Screen
    wc_policy.title_toolbar.next()
    # Forms Screen
    wc_policy.title_toolbar.next()
    # Payment Screen
    wc_policy.title_toolbar.issue_policy()

    time.sleep(10)