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
def test_new_work_comp_policy_creation(browser):
    PC = PolicyCenterHome(browser)
    PC.tab_bar.go_to_desktop()
    PC.tab_bar.search_account("7325149628")

    account = Account(browser)
    account.summary.click_new_submission()

    policy = Policy(browser)
    policy.new_submission_screen.select_base_state("Virginia")
    policy.new_submission_screen.enter_eff_date("10/01/2023")
    policy.new_submission_screen.select_lob_btn("Workers' Compensation")
    assert "Workers' Compensation" in policy.info_bar.get_lob()

    # Qualification Screen
    wc_policy = policy.work_comp
    wc_policy.qualification_screen.table_questionnaires.select_all_radio_btn("yes")
    wc_policy.qualification_screen.table_questionnaires.input_box("Total annual payroll:", "12345")
    wc_policy.title_toolbar.next()

    # Policy Info Screen
    wc_policy.policy_info_screen.input_FEIN("456545654")
    wc_policy.policy_info_screen.industry_code_input("0782")
    wc_policy.policy_info_screen.select_org_type(type_of_org="LLC")
    wc_policy.policy_info_screen.policy_effective_date("08/01/2023")
    wc_policy.title_toolbar.next()

    # Locations Screen
    address = random_address.get_one_address("VA")
    wc_policy.location_screen.add_new_location(address1=address["Address_1"],
                                               city= address["City"],
                                               state=address["State"],
                                               zip_code=address["Zip_Code"])
    wc_policy.title_toolbar.next()

    # WC Coverages Screen
    wc_policy.wc_coverages_screen.add_class(row_number=1,
                                            gov_law= "State Act",
                                            location=2,
                                            code= "0044",
                                            employees=36,
                                            basis_value=12246)
    wc_policy.title_toolbar.next()

    # Supplemental Screen
    wc_policy.supplement_screen.table_questionnaires.select_all_radio_btn("no")
    wc_policy.supplement_screen.table_questionnaires.select_radio_btn("Any employees under 16 or over 60 years of age?", "Yes")
    wc_policy.title_toolbar.next()

    # WC option Screen
    wc_policy.title_toolbar.next()

    # risk analysis screen
    wc_policy.title_toolbar.next()

    # policy review screen
    wc_policy.title_toolbar.quote()

    # Quote Screen
    assert wc_policy.quote_screen.total_premium_amount() > 0
    wc_policy.title_toolbar.next()

    # Forms Screen
    wc_policy.title_toolbar.next()

    # Payment Screen
    wc_policy.title_toolbar.issue_policy()

    time.sleep(20)
    take_screenshot(browser)


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
    # wc_policy.title_toolbar.issue_policy()

    time.sleep(20)
