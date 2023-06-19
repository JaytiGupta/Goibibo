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
    policy.new_submission_screen.select_lob.commercial_auto()
    assert "Commercial Auto" in policy.info_bar.get_lob()

    # Offerings screen
    ca_policy = policy.comm_auto
    ca_policy.offerings_screen.select_offering(text="Standard")
    ca_policy.title_toolbar.next()

    # Qualification screen
    ca_policy.qualification_screen.table_questionnaires.select_all_radio_btn("no")
    ca_policy.qualification_screen.table_questionnaires.dropdown("How many hours per day are vehicles in use?",
                                                                 "Under 12 hours/day")
    ca_policy.title_toolbar.next()

    # Policy Info screen
    ca_policy.policy_info_screen.input_FEIN("456545654")
    ca_policy.policy_info_screen.industry_code_input("0782")
    ca_policy.policy_info_screen.select_organization_type(type_of_org="LLC")
    ca_policy.policy_info_screen.policy_effective_date("08/01/2023")
    ca_policy.title_toolbar.next()

    # Commercial Auto Line screen
    ca_policy.comm_auto_line_screen.ca_coverages(text="Business Auto", text1="Fewer than 10 units")
    ca_policy.comm_auto_line_screen.hired_auto_coverages("Hired Auto Liability")
    ca_policy.comm_auto_line_screen.hired_auto_coverages("Hired Auto Comprehensive")
    ca_policy.comm_auto_line_screen.hired_auto_coverages("Hired Auto Collision")
    ca_policy.comm_auto_line_screen.hired_auto_state("35000", text="Virginia")
    ca_policy.comm_auto_line_screen.non_owned_auto_covg()
    ca_policy.comm_auto_line_screen.non_owned_auto_state("250", "10", "20", text="Virginia")
    ca_policy.title_toolbar.next()



