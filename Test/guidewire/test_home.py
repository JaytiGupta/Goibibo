import time

from Page.guidewire.tab_bar import TabBar
from Page.guidewire.gwpc import GWPC
from Page.guidewire.create_account import CreateAccount
from Page.guidewire.account_summary import AccountSummary


class HomeTests:

    def test_home(self, browser):
        page = GWPC(browser)
        page.go()
        assert page.get_title() == page.expected_title

    def test_get_account_number(self, browser):
        page = GWPC(browser)
        page.login(username='su', password='gw')
        tab_bar = TabBar(browser)
        tab_bar.search_account(1342104490)

        page_act_summary = AccountSummary(browser)
        print(page_act_summary.get_account_number())
        print(page_act_summary.get_account_holder_name())
        page_act_summary.click_new_submission()
        time.sleep(3)


    # def test_create_random_account(self, browser):
    #     page = GWPC(browser)
    #     page.login(username='su', password='gw')
    #     tab_bar = TabBar(browser)
    #     tab_bar.create_new_account_btn()
    #
    #     acct_page = CreateAccount(browser)
    #     # acct_page.create_default_new_account("person")
    #     acct_page.create_default_new_account("company")
    #     time.sleep(15)
        # acct_page.click_btn_cancel()
        # tab_bar.log_out_user()

    # @mark.skip
    # def test_home2(self, browser, data):
    #     page = GWPC(browser)
    #     # page.go()
    #     page.login(username='su', password='gw')
    #     tab_bar = TabBar(browser)
    #     tab_bar.create_new_account_btn()
    #
    #     acct_page = CreateAccount(browser)
    #     acct_page.input_company_name(data["company_name"])
    #     acct_page.click_search_btn()
    #     acct_page.create_new_account(data["account_type"])
    #
    #     acct_page.input_office_phone(data["office_Phone"])
    #     acct_page.input_primary_email(data["primary_email"])
    #     acct_page.input_address(address1=data["address_1"],
    #                             city=data["city"],
    #                             state=data["state"],
    #                             zip=data["zip_code"],
    #                             address_type=data["address_type"])
    #
    #     # acct_page.input_address_1(data["address_1"])
    #     # acct_page.input_city(data["city"])
    #     # acct_page.input_state(data["state"])
    #     # acct_page.input_zip(data["zip_code"])
    #     # acct_page.select_address_type(data["address_type"])
    #
    #     time.sleep(3)
    #     acct_page.cancel_btn()
    #     tab_bar.log_out_user()
    #
    #     page.accept_alert()
    #     # time.sleep(3)
