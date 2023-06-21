import time

import definitions
from Util import random_address, csv_data_converter
from Page.guidewire_pc.policy_center_home import PolicyCenterHome
from Page.guidewire_pc.accounts.account import Account
from Page.guidewire_pc.policies.policy import Policy
from Util.screenshot import take_screenshot
from pytest import mark, fixture


file_path = definitions.ROOT_DIR + "/Data/data_newbusiness_work_comp.csv"
test_data = csv_data_converter.get_rows(file_path, "TestCase", "1")


@fixture(params=test_data)
def data(request):
    yield request.param


def test_login(browser, login_data):
    home_page = PolicyCenterHome(browser)
    home_page.go()
    home_page.login_page.login(username=login_data["username"], password=login_data["password"])


# @mark.skip
def test_new_work_comp_policy_creation(browser, data):
    PC = PolicyCenterHome(browser)
    PC.tab_bar.go_to_desktop()
    PC.tab_bar.search_account(data["Account_number"])

    account = Account(browser)
    account.summary.click_new_submission_btn()

    policy = Policy(browser)
    policy.new_submission_screen.select_base_state(data["new_submission_screen_base_state"])
    policy.new_submission_screen.enter_effective_date(data["new_submission_screen_effective_date"])
    policy.new_submission_screen.select_lob.workers_compensation()
    assert "Workers' Compensation" in policy.info_bar.get_lob()

    # Qualification Screen
    wc_policy = policy.work_comp
    wc_policy.qualification_screen.table_questionnaires.select_all_radio_btn("no")
    wc_policy.qualification_screen.table_questionnaires.input_box("Total annual payroll:", "12345")
    wc_policy.title_toolbar.next()

    # Policy Info Screen
    # wc_policy.policy_info_screen.fill_random_details()
    wc_policy.policy_info_screen.input_FEIN(data["policy_info_screent_FEIN"])
    wc_policy.policy_info_screen.industry_code_input(data["policy_info_screent_industry_code"])
    wc_policy.policy_info_screen.select_organization_type(type_of_org=data["policy_info_screent_organization_type"])
    # wc_policy.policy_info_screen.policy_effective_date(data["policy_info_screent_effective_date"])
    wc_policy.title_toolbar.next()

    # Locations Screen
    if data["location_screen_add_new_location"]:
    # address = random_address.get_one_address("VA")
        wc_policy.location_screen.add_new_location(address1=data["location_screen_address1"],
                                                   city= data["location_screen_city"],
                                                   state=data["location_screen_state"],
                                                   zip_code=data["location_screen_zip_code"])
    wc_policy.title_toolbar.next()

    # WC Coverages Screen
    wc_policy.wc_coverages_screen.add_class(row_number=data["wc_coverages_screen_class_row"],
                                            gov_law= data["wc_coverages_screen_gov_law"],
                                            location=data["wc_coverages_screen_location"],
                                            code= data["wc_coverages_screen_class_code"],
                                            employees=data["wc_coverages_screen_employees#"],
                                            basis_value=data["wc_coverages_screen_basis_value"])
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