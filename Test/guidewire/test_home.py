import time
from Util import random_address
from Page.guidewire_pc.policy_center_home import PolicyCenterHome
from Page.guidewire_pc.accounts.account import Account
from Page.guidewire_pc.policies.policy import Policy
from Util.screenshot import take_screenshot


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


def test_search_submission(browser):
    page = PolicyCenterHome(browser)
    page.tab_bar.go_to_desktop()
    page.tab_bar.search_submission("0002960698")
    policy = Policy(browser)
    assert "Workers' Compensation" in policy.info_bar.get_lob()


def test_search_account(browser):
    page = PolicyCenterHome(browser)
    page.tab_bar.go_to_desktop()
    page.tab_bar.search_account("7325149628")
    account = Account(browser)
    assert account.summary.account_summary_title_present()


# def test_new_account_creation(browser):
#     page = PolicyCenterHome(browser)
#     page.tab_bar.go_to_desktop()
#     page.tab_bar.create_new_account_btn()
#     account = Account(browser)
#     account.new_account.create_default_new_account("Company")
#     assert account.summary.account_summary_title_present()


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
    wc_policy.qualification_screen.select_all_radio_btn_as_no()
    take_screenshot(browser)
    wc_policy.qualification_screen.enter_input_box("Total annual payroll:", "12345")
    wc_policy.next()

    # "Policy Info"
    wc_policy.policy_info_screen.input_FEIN("456545654")
    wc_policy.policy_info_screen.industry_code_input("0782")
    wc_policy.policy_info_screen.select_org_type(type_of_org="LLC")
    wc_policy.policy_info_screen.policy_effective_date("08/01/2023")
    wc_policy.next()

    # "Locations"
    address = random_address.get_one_address("VA")
    wc_policy.location_screen.add_new_location(address1=address["Address_1"],
                                               city= address["City"],
                                               state=address["State"],
                                               zip_code=address["Zip_Code"])
    wc_policy.next()

    #  "WC Coverages"
    wc_policy.wc_coverages_screen.add_class(row_number=1,
                                            gov_law= "State Act",
                                            location=2,
                                            code= "0044",
                                            employees=36,
                                            basis_value=12246)
    wc_policy.next()

    # Supplemental Screen
    wc_policy.supplement_screen.select_all_radio_btn_as_no()
    wc_policy.supplement_screen.select_radio_btn_option("Any employees under 16 or over 60 years of age?", "Yes")
    time.sleep(15)
    wc_policy.next()

    # WC option Screen
    wc_policy.next()

    # risk analysis screen
    wc_policy.next()

    # policy review screen
    wc_policy.quote()

    # Quote Screen
    assert wc_policy.quote_screen.total_premium_amt() > 0
    take_screenshot(browser)
    wc_policy.next()

    # Forms Screen
    wc_policy.next()

    # Payment Screen
    # wc_policy.issue_policy()
    take_screenshot(browser)
    time.sleep(10)

    # wc_policy.accept_alert()



