from Page.guidewire_pc.policy_center_home import PolicyCenterHome
from Page.guidewire_pc.accounts.account import Account
from Util.screenshot import Screenshot
from pytest import mark, fixture
from Util.csv_data_converter import CSVTestData


s_test_data = CSVTestData.load_testcase("1", "2", "3", "4", "5", "6")
j_test_data = CSVTestData.load_testcase("11", "12", "13", "15", "16", "14")


@fixture(params=s_test_data)
def data(request):
    yield request.param


@mark.account
@mark.account_creation
@mark.smoke
def test_new_account_creation(browser_pc, data):
    pc = PolicyCenterHome(browser_pc)
    pc.tab_bar.go_to_desktop()
    pc.tab_bar.create_new_account_btn()
    account = Account(browser_pc)
    new_account = account.new_account

    account_type = data["account_type"]

    # Enter Account Information Page
    if account_type.lower() == "company":
        new_account.enter_account_information_screen.\
            input_company_name(new_account.random_company_name)
        new_account.enter_account_information_screen.create_new_account.company()

    if account_type.lower() == "person":
        new_account.enter_account_information_screen.\
            input_name(new_account.random_first_name, new_account.random_last_name)
        new_account.enter_account_information_screen.create_new_account.person()

    # Create account Page
    if account_type.lower() == "company":
        new_account.create_account_screen.input_office_phone(data["office_Phone"])

    new_account.create_account_screen.input_primary_email(new_account.random_email_address)

    new_account.create_account_screen.input_address(address1=data["address_1"],
                                                    city=data["city"],
                                                    state=data["state"],
                                                    zip_code=data["zip_code"],
                                                    address_type=data["address_type"])

    new_account.create_account_screen.select_producer(organization=data["organization"],
                                                      producer_code=data["producer"])
    new_account.create_account_screen.click_btn_update()
    account_number = account.summary.get_account_number()
    Screenshot.capture(browser_pc)
    CSVTestData.update(data["TestCase"], "account_number", account_number)
