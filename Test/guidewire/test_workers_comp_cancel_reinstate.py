from pytest import fixture, mark
from Page.guidewire_pc.policy_center_home import PolicyCenterHome
from Page.guidewire_pc.policies.policy import Policy
from Page.guidewire_pc.policies.Trasactions.cancel import Cancel
from Page.guidewire_pc.policies.Trasactions.reinstate import Reinstate
from Util.screenshot import Screenshot
from Util.csv_data_converter import CSVTestData


s_test_data = CSVTestData.load_testcase(2)
j_test_data = CSVTestData.load_testcase("14")


@fixture(params=s_test_data)
def data(request):
    yield request.param


@mark.cancel_rein
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
