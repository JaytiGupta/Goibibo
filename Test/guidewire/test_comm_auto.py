import time
from Util import random_address
from Page.guidewire_pc.policy_center_home import PolicyCenterHome
from Page.guidewire_pc.accounts.account import Account
from Page.guidewire_pc.policies.policy import Policy
from Util.screenshot import take_screenshot
from Page.guidewire_pc.policies.LOBs.commercial_auto import CommercialAuto
from pytest import mark


def test_login(browser):
    home_page = PolicyCenterHome(browser)
    home_page.go()
    home_page.login_page.login(username='su', password='gw')


def test_search_account(browser):
    page = PolicyCenterHome(browser)
    page.tab_bar.go_to_desktop()
    page.tab_bar.search_account("9519613281")
    account = Account(browser)
    assert account.summary.account_summary_title_present()


def test_new_commercial_auto_creation(browser):
    PC = PolicyCenterHome(browser)
    PC.tab_bar.go_to_desktop()
    PC.tab_bar.search_account("9519613281")

    account = Account(browser)
    account.summary.click_new_submission_btn()

    policy = Policy(browser)
    policy.new_submission_screen.select_base_state("Virginia")
    policy.new_submission_screen.enter_effective_date("7/1/2023")
    policy.new_submission_screen._select_lob("Commercial Auto")
    assert "Commercial Auto" in policy.info_bar.get_lob()

    # Offerings screen
    ca_policy = policy.comm_auto
    ca_policy.offerings_screen.select_offering("Standard")
    ca_policy.title_toolbar.next()

    # Qualification screen
    ca_policy.qualification_screen.table_questionnaires.select_all_radio_btn("yes")
    ca_policy.qualification_screen.table_questionnaires.dropdown("How many hours per day are vehicles in use?",
                                                                 "Under 12 hours/day")
    ca_policy.title_toolbar.next()

    # Policy Info screen