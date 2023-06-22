import definitions
from Util import random_data, csv_data_converter
from Page.guidewire_pc.policy_center_home import PolicyCenterHome
from Page.guidewire_pc.accounts.account import Account
from Util.screenshot import take_screenshot
from pytest import mark, fixture


file_path = definitions.ROOT_DIR + "/Data/data_new_account.csv"
test_data = csv_data_converter.get_rows(file_path, "TestCase", "1",  "2")


@fixture(params=test_data)
def data(request):
    yield request.param


def test_login(browser, login_data):
    home_page = PolicyCenterHome(browser)
    home_page.go()
    home_page.login_page.login(username=login_data["username"], password=login_data["password"])


# @mark.skip
def test_new_account_creation(browser, data):

    pc = PolicyCenterHome(browser)
    pc.tab_bar.go_to_desktop()
    pc.tab_bar.create_new_account_btn()
    account = Account(browser)
    new_account = account.new_account

    account_type = data["account_type"]

    # Enter Account Information Page
    if account_type.lower() == "company":
        new_account.enter_account_information_screen.\
            input_company_name(new_account.random_company_name)

    if account_type.lower() == "person":
        new_account.enter_account_information_screen.\
            input_name(new_account.random_first_name, new_account.random_last_name)

    new_account.enter_account_information_screen.search_btn.click_element()
    new_account.enter_account_information_screen.select_new_account_type(account_type)

    # Create account Page
    if account_type.lower() == "company":
        new_account.create_account_screen.input_office_phone(data["office_Phone"])

    new_account.create_account_screen.input_primary_email(data["primary_email"])

    new_account.create_account_screen.input_address(address1=data["address_1"],
                                                    city=data["city"],
                                                    state=data["state"],
                                                    zip_code=data["zip_code"],
                                                    address_type=data["address_type"])

    new_account.create_account_screen.select_producer(organization=data["organization"],
                                                      producer_code=data["producer"])
    new_account.create_account_screen.click_btn_update()


@mark.skip
def test_default_company_account_creation(browser):
    page = PolicyCenterHome(browser)
    page.tab_bar.go_to_desktop()
    page.tab_bar.create_new_account_btn()
    account = Account(browser)
    account.new_account.create_default_new_account("Company")
    assert account.summary.account_summary_title_present()
