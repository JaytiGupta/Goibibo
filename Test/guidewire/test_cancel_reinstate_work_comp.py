from pytest import fixture, mark
import definitions
from Page.guidewire_pc.policy_center_home import PolicyCenterHome
from Page.guidewire_pc.policies.policy import Policy
from Page.guidewire_pc.policies.Trasactions.cancel import Cancel
from Page.guidewire_pc.policies.Trasactions.reinstate import Reinstate
from Util import csv_data_converter
from Util.screenshot import take_screenshot


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


def test_work_comp_cancel_policy_transaction(browser, data):
    pc = PolicyCenterHome(browser)
    pc.tab_bar.go_to_desktop()
    pc.tab_bar.search_policy(data["policy_number"])

    policy = Policy(browser)
    policy.summary.new_transaction.cancel_policy()

    # Cancel
    cancel_transaction = Cancel(browser)
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
    reinstate = Reinstate(browser)
    reinstate.start_reinstatement_screen.fill_details(reason=data["reinstate_reason"],
                                                      reason_description= data["reinstate_reason_description"])  #Other
    reinstate.title_toolbar.quote()

    # Quote Screen
    reinstate.title_toolbar.reinstate()
