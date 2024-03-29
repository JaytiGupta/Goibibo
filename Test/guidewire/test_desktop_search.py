from Page.guidewire_pc.policy_center_home import PolicyCenterHome
from Page.guidewire_pc.accounts.account import Account
from Page.guidewire_pc.policies.policy_summary import PolicySummary
from Page.guidewire_pc.policies.common.sidebar import Sidebar
from Util.screenshot import Screenshot
from pytest import mark, fixture
from Util.csv_data_converter import CSVTestData


j_test_data = CSVTestData.load_testcase("11")
s_test_data = CSVTestData.load_testcase("1")


@fixture(params=s_test_data)
def data(request):
    yield request.param


@mark.regression
@mark.smoke
@mark.search
class DesktopSearchTests:

    @fixture(params=s_test_data, autouse=True)
    def data_setup(self, data):
        self.account_number = data["account_number"]
        self.policy_number = data["policy_number"]
        self.submission_number = data["submission_number"]

    @mark.account
    def test_search_account(self, browser_pc):
        account_number = self.account_number
        page = PolicyCenterHome(browser_pc)
        page.tab_bar.search_account("432545245")
        account = Account(browser_pc)
        assert account.summary.account_summary_title_present()
        Screenshot.capture(browser_pc)

    def test_search_submission(self, browser_pc):
        submission_number = self.submission_number
        page = PolicyCenterHome(browser_pc)
        page.tab_bar.search_submission(submission_number)
        policy_sidebar = Sidebar(browser_pc)
        assert submission_number in policy_sidebar.heading.get_text()
        Screenshot.highlight_and_capture(browser_pc, policy_sidebar.heading)
    #
    # def test_search_policy(self, browser_pc):
    #     policy_number = self.policy_number
    #     page = PolicyCenterHome(browser_pc)
    #     page.tab_bar.search_policy(policy_number)
    #     policy_summary_screen = PolicySummary(browser_pc)
    #     policy_number_in_details = policy_summary_screen.get_policy_number()
    #     assert policy_number == policy_number_in_details
    #     Screenshot.capture(browser_pc)
