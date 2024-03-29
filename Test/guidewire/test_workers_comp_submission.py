from Page.guidewire_pc.policy_center_home import PolicyCenterHome
from Page.guidewire_pc.accounts.account import Account
from Page.guidewire_pc.policies.policy import Policy
from Util.screenshot import Screenshot
from pytest import mark, fixture
from Util.csv_data_converter import CSVTestData


j_test_data = CSVTestData.load_testcase(11)  # , "12", "13", "14")
s_test_data = CSVTestData.load_testcase("2")   # , "3", "4")


@fixture(params=s_test_data)
def data(request):
    yield request.param


@mark.workcomp
@mark.newbusiness
def test_new_work_comp_policy_creation(browser_pc, data):
    pc = PolicyCenterHome(browser_pc)
    pc.tab_bar.search_account(data["Account_number"])

    account = Account(browser_pc)
    account.summary.click_new_submission_btn()

    policy = Policy(browser_pc)
    policy.new_submission_screen.select_base_state(data["new_submission_screen_base_state"])
    policy.new_submission_screen.enter_effective_date(data["new_submission_screen_effective_date"])
    policy.new_submission_screen.select_lob.workers_compensation()
    assert "Workers' Compensation" in policy.info_bar.get_lob()

    # Qualification Screen
    wc_policy = policy.work_comp
    wc_policy.qualification_screen.table_questionnaires.select_all_radio_btn("yes")
    wc_policy.qualification_screen.table_questionnaires.input_box("Total annual payroll:", "12345")
    wc_policy.title_toolbar.next()

    # Policy Info Screen
    wc_policy.policy_info_screen.input_FEIN(data["policy_info_screent_FEIN"])
    wc_policy.policy_info_screen.industry_code_input(data["policy_info_screent_industry_code"])
    wc_policy.policy_info_screen.select_organization_type(type_of_org=data["policy_info_screent_organization_type"])
    wc_policy.title_toolbar.next()

    # Locations Screen
    if data["location_screen_add_new_location"]:
        wc_policy.location_screen.add_new_location(address1=data["location_screen_address1"],
                                                   city=data["location_screen_city"],
                                                   state=data["location_screen_state"],
                                                   zip_code=data["location_screen_zip_code"])
    wc_policy.title_toolbar.next()

    # WC Coverages Screen
    wc_policy.wc_coverages_screen.add_class(row_number=data["wc_coverages_screen_class_row"],
                                            gov_law=data["wc_coverages_screen_gov_law"],
                                            location=data["wc_coverages_screen_location"],
                                            code=data["wc_coverages_screen_class_code"],
                                            employees=data["wc_coverages_screen_employees#"],
                                            basis_value=data["wc_coverages_screen_basis_value"])
    wc_policy.title_toolbar.next()

    # Supplemental Screen
    wc_policy.supplement_screen.table_questionnaires.select_all_radio_btn("no")
    wc_policy.supplement_screen.table_questionnaires.\
        select_radio_btn("Any employees under 16 or over 60 years of age?", "Yes")
    wc_policy.title_toolbar.next()

    # WC option Screen
    wc_policy.wc_options_screen.add_wc_option("Federal Liability")
    wc_policy.wc_options_screen.add_federal_class(location_index=1,
                                                  class_code=7333,
                                                  emp_no=15,
                                                  basis_value=5000)
    wc_policy.title_toolbar.next()
    # wc_policy.risk_analysis_screen.SCREEN_TITLE

    # risk analysis screen
    Screenshot.capture(browser_pc)
    wc_policy.title_toolbar.next()

    # policy review screen
    wc_policy.title_toolbar.quote()

    # Quote Screen
    assert wc_policy.quote_screen.total_premium_amount() > 0
    wc_policy.title_toolbar.next()

    # Forms Screen
    wc_policy.title_toolbar.next()

    # Payment Screen
    submission_number: str = wc_policy.sidebar.transaction_number()
    wc_policy.title_toolbar.issue_policy()

    wc_policy.title_toolbar.screen_title_element.wait_till_text_to_be_present_in_element("Submission Bound")
    Screenshot.capture(browser_pc)
    CSVTestData.update(data["TestCase"], "submission_number", submission_number)
