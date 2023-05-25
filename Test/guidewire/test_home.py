import time

from Page.guidewire.tab_bar import TabBar
from Page.guidewire.gwpc import GWPC
from Page.guidewire.create_account import CreateAccount
from Page.guidewire.account_summary import AccountSummary
from Page.guidewire.new_submission import NewSubmission


class HomeTests:

    def test_home(self, browser):
        page = GWPC(browser)
        page.go()
        assert page.get_title() == page.expected_title

    def test_get_account_number(self, browser):
        page = GWPC(browser)
        page.login(username='su', password='gw')
        tab_bar = TabBar(browser)
        tab_bar.search_account("9519613281")
        # page1 = CreateAccount(browser)
        # page1.create_default_new_account('Company')
        time.sleep(3)

    def test_new_submission(self, browser):
        page = AccountSummary(browser)
        page.click_new_submission()
        page1 = NewSubmission(browser)
        page1.enter_eff_date("05/05/2023")
        page1.select_base_state("Virginia")
        time.sleep(5)
        page1.select_lob_btn("Workers' Compensation")
        assert page1.draft_sub()
        time.sleep(10)

