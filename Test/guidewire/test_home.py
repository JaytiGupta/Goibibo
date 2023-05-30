import time

from Page.guidewire.tab_bar import TabBar
from Page.guidewire.gwpc import GWPC
from Page.guidewire.create_account import CreateAccount
from Page.guidewire.account_summary import AccountSummary
from Page.guidewire.new_submission import NewSubmission
from Page.guidewire.LOBs.work_comp import WorkersCompensation



class HomeTests:

    def test_home(self, browser):
        page = GWPC(browser)
        page.go()
        assert page.get_title() == page.expected_title

    def test_get_account_number(self, browser):
        page = GWPC(browser)
        page.login(username='su', password='gw')
        tab_bar = TabBar(browser)
        # tab_bar.create_new_account_btn()
        # create_act_page = CreateAccount(browser)
        # create_act_page.create_default_new_account("Company")
        # time.sleep(14)
        # tab_bar.search_account("3415781253")
        tab_bar.search_submission("0000553505")

    # def test_new_submission(self, browser):
    #     page = AccountSummary(browser)
    #     page.click_new_submission()
    #     page1 = NewSubmission(browser)
    #     page1.select_base_state("Virginia")
    #     page1.enter_eff_date("05/05/2023")
    #     page1.select_lob_btn("Workers' Compensation")
    #     time.sleep(3)
    #     assert page1.draft_sub()

    def test_work_comp_policy_creation(self, browser):
        page = WorkersCompensation(browser)
        page.select_qualification_all_radio_btn_as_yes()
        page.enter_qualification_input_box("Total annual payroll:", "12345")
        time.sleep(10)