import time
from Page.guidewire_pc.policy_center_home import PolicyCenterHome
from Page.guidewire_pc.accounts.account import Account
from Page.guidewire_pc.policies.policy import Policy
from Page.guidewire_pc.policies.Trasactions.cancel import Cancel
from Page.guidewire_pc.policies.Trasactions.reinstate import Reinstate
from Util.screenshot import take_screenshot


def test_login(browser, data):
    home_page = PolicyCenterHome(browser)
    home_page.go()
    home_page.login_page.login(username=data["username"],
                               password=data["password"])


# @mark.skip
def test_work_comp_cancel_policy_transaction(browser, data):
    pc = PolicyCenterHome(browser)
    pc.tab_bar.go_to_desktop()
    pc.tab_bar.search_policy(data["policy_number"])

    policy = Policy(browser)
    policy.summary.new_transaction.cancel_policy()

    # Cancel
    cancel_transaction = Cancel(browser)
    cancel_transaction.start_cancellation_for_policy_screen.fill_details(source=data["cancellation_source"],
                                                                         reason=data["cancellation_reason"])
    cancel_transaction.start_cancellation_for_policy_screen.click_start_cancellation_button()

    # confirmation_screen
    cancel_transaction.title_toolbar.cancel_now()
    pc.tab_bar.search_policy(data["policy_number"])

    # Reinstate
    policy.summary.new_transaction.reinstate_policy()
    reinstate = Reinstate(browser)
    reinstate.start_reinstatement_screen.fill_details(reason=data["reinstate_reason"],
                                                      reason_description= data["reinstate_reason_description"])  #Other
    reinstate.title_toolbar.quote()

    # Quote Screen
    reinstate.title_toolbar.reinstate()
