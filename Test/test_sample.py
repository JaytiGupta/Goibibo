import time
from Page.guidewire_pc.policy_center_home import PolicyCenterHome
from Page.guidewire_pc.accounts.account import Account
from Page.guidewire_pc.policies.policy import Policy


def test_work_comp(browser_pc):
    pc = PolicyCenterHome(browser_pc)
    pc.tab_bar.search_submission("0002507580")

    wc_policy = Policy(browser_pc).work_comp
    wc_policy.title_toolbar.navigate_till_screen("Policy Review")

    wc_policy.title_toolbar.quote()

    assert wc_policy.quote_screen.total_premium_amount() > 0
    wc_policy.title_toolbar.next()

