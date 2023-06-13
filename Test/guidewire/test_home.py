import time
from Util import random_address
from Page.guidewire_pc.policy_center_home import PolicyCenterHome
from Page.guidewire_pc.accounts.account import Account
from Page.guidewire_pc.policies.policy import Policy
from Util.screenshot import take_screenshot
from pytest import mark


def test_website_is_available(browser):
    home_page = PolicyCenterHome(browser)
    home_page.go()
    assert home_page.get_title() == home_page.expected_title
    take_screenshot(browser)


def test_user_is_able_to_login(browser):
    home_page = PolicyCenterHome(browser)
    home_page.login_page.login(username='su', password='gw')
    assert home_page.login_page.is_login_successful()
    take_screenshot(browser)


@mark.skip
def test_search_account(browser):
    page = PolicyCenterHome(browser)
    page.tab_bar.go_to_desktop()
    page.tab_bar.search_account("7325149628")
    account = Account(browser)
    assert account.summary.account_summary_title_present()


@mark.skip
def test_search_submission(browser):
    page = PolicyCenterHome(browser)
    page.tab_bar.go_to_desktop()
    page.tab_bar.search_submission("0002960698")
    policy = Policy(browser)
    assert "Workers' Compensation" in policy.info_bar.get_lob()

@mark.skip
def test_new_account_creation(browser):
    page = PolicyCenterHome(browser)
    page.tab_bar.go_to_desktop()
    page.tab_bar.create_new_account_btn()
    account = Account(browser)
    account.new_account.create_default_new_account("Company")
    assert account.summary.account_summary_title_present()


# @mark.skip
def test_new_work_comp_policy_creation(browser):
    page = PolicyCenterHome(browser)
    page.tab_bar.go_to_desktop()
    page.tab_bar.search_account("7325149628")

    account = Account(browser)
    account.summary.click_new_submission()

    policy = Policy(browser)
    policy.new_submission_screen.select_base_state("Virginia")
    policy.new_submission_screen.enter_eff_date("10/01/2023")
    policy.new_submission_screen.select_lob_btn("Workers' Compensation")
    assert "Workers' Compensation" in policy.info_bar.get_lob()

    wc_policy = policy.work_comp
    wc_policy.qualification_screen.table_questionnaires.select_all_radio_btn("yes")
    take_screenshot(browser)
    wc_policy.qualification_screen.table_questionnaires.input_box("Total annual payroll:", "12345")
    wc_policy.title_toolbar.next()

    # "Policy Info"
    wc_policy.policy_info_screen.input_FEIN("456545654")
    wc_policy.policy_info_screen.industry_code_input("0782")
    wc_policy.policy_info_screen.select_org_type(type_of_org="LLC")
    wc_policy.policy_info_screen.policy_effective_date("08/01/2023")
    wc_policy.title_toolbar.next()

    # "Locations"
    address = random_address.get_one_address("VA")
    wc_policy.location_screen.add_new_location(address1=address["Address_1"],
                                               city= address["City"],
                                               state=address["State"],
                                               zip_code=address["Zip_Code"])
    wc_policy.title_toolbar.next()

    #  "WC Coverages"
    wc_policy.wc_coverages_screen.add_class(row_number=1,
                                            gov_law= "State Act",
                                            location=2,
                                            code= "0044",
                                            employees=36,
                                            basis_value=12246)
    wc_policy.title_toolbar.next()

    # Supplemental Screen
    wc_policy.supplement_screen.table_questionnaires.select_all_radio_btn("no")
    wc_policy.supplement_screen.table_questionnaires.radio_btn("Any employees under 16 or over 60 years of age?", "Yes")
    wc_policy.title_toolbar.next()

    # WC option Screen
    # wc_policy.title_toolbar.wait_for_screen(wc_policy.wc_options_screen.SCREEN_TITLE)
    wc_policy.title_toolbar.next()

    # risk analysis screen
    # wc_policy.title_toolbar.wait_for_screen(wc_policy.risk_analysis_screen.SCREEN_TITLE)
    wc_policy.title_toolbar.next()

    # policy review screen
    # wc_policy.title_toolbar.wait_for_screen(wc_policy.policy_review_screen.SCREEN_TITLE)
    wc_policy.title_toolbar.quote()

    # Quote Screen
    # wc_policy.title_toolbar.wait_for_screen(wc_policy.quote_screen.SCREEN_TITLE)
    assert wc_policy.quote_screen.total_premium_amt() > 0
    take_screenshot(browser)
    wc_policy.title_toolbar.next()

    # Forms Screen
    # wc_policy.title_toolbar.wait_for_screen(wc_policy.forms_screen.SCREEN_TITLE)
    wc_policy.title_toolbar.next()

    # Payment Screen
    # wc_policy.title_toolbar.wait_for_screen(wc_policy.payment_screen.SCREEN_TITLE)
    wc_policy.title_toolbar.issue_policy()

    time.sleep(20)
    take_screenshot(browser)

    # wc_policy.accept_alert()



