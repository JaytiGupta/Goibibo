import time

from Page.guidewire.tab_bar import TabBar
from Page.guidewire.gwpc import GWPC
from Page.guidewire.create_account import CreateAccount


class HomeTests:

    def test_home(self, browser):
        page = GWPC(browser)
        page.go()
        assert page.get_title() == page.expected_title

    def test_home2(self, browser, data):
        page = GWPC(browser)
        # page.go()
        page.login(username='su', password='gw')
        tab_bar = TabBar(browser)
        tab_bar.create_new_account_btn()

        acct_page = CreateAccount(browser)
        acct_page.input_company_name(data["company_name"])
        acct_page.input_first_name(data["first_name"])
        acct_page.input_last_name(data["last_name"])
        time.sleep(1)

        tab_bar.log_out_user()
        page.accept_alert()
        # time.sleep(3)
