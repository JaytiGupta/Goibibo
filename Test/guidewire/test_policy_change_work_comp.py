import time
from Page.guidewire_pc.policy_center_home import PolicyCenterHome
from Page.guidewire_pc.policies.policy import Policy
from Page.guidewire_pc.policies.Trasactions.change_policy import ChangePolicy
from Util.screenshot import take_screenshot
from pytest import mark, fixture
import definitions
from Util import csv_data_converter


file_path = definitions.ROOT_DIR + "/Data/data_policy_change_work_comp.csv"
test_data = csv_data_converter.get_rows(file_path, "TestCase", "1")


@fixture(params=test_data)
def data(request):
    yield request.param


def test_login(browser, login_data):
    home_page = PolicyCenterHome(browser)
    home_page.go()
    home_page.login_page.login(username=login_data["username"],
                               password=login_data["password"])


# @mark.skip
def test_work_comp_change_policy_transaction(browser, data):
    PC = PolicyCenterHome(browser)
    PC.tab_bar.go_to_desktop()
    PC.tab_bar.search_policy(data["policy_number"])

    policy = Policy(browser)
    policy.summary.new_transaction.change_policy()

    amendment = ChangePolicy(browser)
    amendment.start_policy_change_screen.fill_all_details(effective_date=data["change_effective_date"],
                                                          description=data["description"])
    amendment.title_toolbar.next()

    # Policy Info Screen
    wc_policy = policy.work_comp
    wc_policy.navigate_till_screen("WC Coverages")
    wc_policy.wc_coverages_screen.add_class(row_number=data["wc_coverages_screen_class_rows#"],
                                            gov_law=data["wc_coverages_screen_gov_law"],
                                            location=data["wc_coverages_screen_location"],
                                            code=data["wc_coverages_screen_class_code"],
                                            employees=data["wc_coverages_screen_employee"],
                                            basis_value=data["wc_coverages_screen_basis_value"])

    wc_policy.navigate_till_screen("Policy Review")

    wc_policy.title_toolbar.quote()
    # Quote Screen
    wc_policy.title_toolbar.next()
    # Forms Screen
    wc_policy.title_toolbar.next()
    # Payment Screen
    submission_number: str = wc_policy.sidebar.transaction_number()
    wc_policy.title_toolbar.issue_policy()
    take_screenshot(browser)
    csv_data_converter.update_csv(file_path, "TestCase", data["TestCase"], "policy_change_number", submission_number)

