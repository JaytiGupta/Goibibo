from pytest import fixture, mark
import definitions
from Page.guidewire_pc.policy_center_home import PolicyCenterHome
from Page.guidewire_pc.policies.policy import Policy
from Page.guidewire_pc.policies.Trasactions.cancel import Cancel
from Page.guidewire_pc.policies.Trasactions.reinstate import Reinstate
from Util import csv_data_converter
from Util.screenshot import Screenshot


file_path = definitions.ROOT_DIR + "/Data/data_cancel_reinstate_work_comp.csv"
test_data = csv_data_converter.get_rows(file_path, "TestCase", "11", "12")


@fixture(params=test_data)
def data(request):
    yield request.param


def test_work_comp_cancel_policy_transaction(browser_pc, data):
    pc = PolicyCenterHome(browser_pc)
    pc.tab_bar.go_to_desktop()
    pc.tab_bar.search_policy(data["policy_number"])

    policy = Policy(browser_pc)
    policy.summary.new_transaction.cancel_policy()

    # Cancel
    cancel_transaction = Cancel(browser_pc)
    cancel_transaction.start_cancellation_for_policy_screen.\
        fill_details(source=data["cancellation_source"],
                     reason=data["cancellation_reason"],
                     reason_description=data["cancellation_reason_description"])
    cancel_transaction.start_cancellation_for_policy_screen.click_start_cancellation_button()

    # confirmation_screen
    cancel_transaction.title_toolbar.cancel_now()
    pc.tab_bar.search_policy(data["policy_number"])

    # Reinstate
    policy.summary.new_transaction.reinstate_policy()
    reinstate = Reinstate(browser_pc)
    reinstate.start_reinstatement_screen.fill_details(reason=data["reinstate_reason"],
                                                      reason_description= data["reinstate_reason_description"])  #Other
    reinstate.title_toolbar.quote()

    # Quote Screen
    reinstate.title_toolbar.reinstate()
    Screenshot.capture(browser_pc)
