import time
from Page.guidewire_pc.policy_center_home import PolicyCenterHome
from Page.guidewire_pc.policies.policy import Policy
from Page.guidewire_pc.policies.Trasactions.change_policy import ChangePolicy
from Util.screenshot import Screenshot
from pytest import mark, fixture
import definitions
from Util import csv_data_converter


file_path = definitions.ROOT_DIR + "/Data/data_policy_change_work_comp.csv"
test_data = csv_data_converter.get_rows(file_path, "TestCase", "1")


@fixture(params=test_data)
def data(request):
    yield request.param


@mark.policychange
# @mark.skip
def test_work_comp_change_policy_transaction(browser_pc, data):
    PC = PolicyCenterHome(browser_pc)
    PC.tab_bar.go_to_desktop()
    PC.tab_bar.search_policy(data["policy_number"])

    policy = Policy(browser_pc)
    policy.summary.new_transaction.change_policy()

    amendment = ChangePolicy(browser_pc)
    amendment.start_policy_change_screen.fill_all_details(data["change_effective_date"],
                                                          data["description"])
    amendment.next_btn(browser_pc)
    # amendment.title_toolbar.next()

    # Policy Info Screen
    wc_policy = policy.work_comp
    wc_policy.title_toolbar.navigate_till_screen("Supplemental")
    wc_policy.supplement_screen.table_questionnaires.\
        select_radio_btn("Are athletic teams sponsored?", "Yes")
    wc_policy.supplement_screen.table_questionnaires. \
        select_radio_btn("Are employee health plans provided?", "Yes")
    wc_policy.title_toolbar.navigate_till_screen("Policy Review")
    wc_policy.title_toolbar.quote()
    # Quote Screen
    wc_policy.title_toolbar.next()
    # Forms Screen
    wc_policy.title_toolbar.next()
    # Payment Screen
    submission_number: str = wc_policy.sidebar.transaction_number()
    wc_policy.title_toolbar.issue_policy()
    Screenshot.capture(browser_pc)
    csv_data_converter.update_csv(file_path, "TestCase", data["TestCase"], "policy_change_number", submission_number)

