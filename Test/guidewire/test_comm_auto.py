import time
from Util import random_data
from Page.guidewire_pc.policy_center_home import PolicyCenterHome
from Page.guidewire_pc.accounts.account import Account
from Page.guidewire_pc.policies.policy import Policy
from Util.screenshot import take_screenshot


def test_login(browser, login_data):
    home_page = PolicyCenterHome(browser)
    home_page.go()
    home_page.login_page.login(username=login_data["username"],
                               password=login_data["password"])


def test_new_commercial_auto_creation(browser, data):
    PC = PolicyCenterHome(browser)
    PC.tab_bar.go_to_desktop()
    PC.tab_bar.search_account("1342104490") #data["Account#"])

    account = Account(browser)
    account.summary.click_new_submission_btn()

    policy = Policy(browser)
    policy.new_submission_screen.select_base_state(data["base_state"])
    policy.new_submission_screen.enter_effective_date(data["effective_date"])
    policy.new_submission_screen.select_lob.commercial_auto()
    assert "Commercial Auto" in policy.info_bar.get_lob()

    # Offerings screen
    ca_policy = policy.comm_auto
    ca_policy.offerings_screen.select_offering(text=data["offering"])
    ca_policy.title_toolbar.next()

    # Qualification screen
    ca_policy.qualification_screen.table_questionnaires.select_all_radio_btn(data["all_radio_btn"])
    ca_policy.qualification_screen.table_questionnaires.dropdown(data["question"],
                                                                 data["answer"])
    ca_policy.title_toolbar.next()

    # Policy Info screen
    ca_policy.policy_info_screen.input_FEIN(data["FEIN"])
    ca_policy.policy_info_screen.industry_code_input(data["industry_code"])
    ca_policy.policy_info_screen.select_organization_type(type_of_org=data["org_type"])
    ca_policy.policy_info_screen.policy_effective_date(data["effective_date"])
    ca_policy.title_toolbar.next()

    # Commercial Auto Line screen
    ca_policy.comm_auto_line_screen.ca_coverages(product=data["product"], fleet=data["fleet"])
    ca_policy.comm_auto_line_screen.wait_liability_covg()
    ca_policy.comm_auto_line_screen.hired_auto_coverages(data["hired_auto_cvg1"])
    ca_policy.comm_auto_line_screen.hired_auto_coverages(data["hired_auto_cvg2"])
    ca_policy.comm_auto_line_screen.hired_auto_coverages(data["hired_auto_cvg3"])
    ca_policy.comm_auto_line_screen.hired_auto_state(cost_of_hire=data["cost_of_hire"], state=data["base_state"])
    ca_policy.comm_auto_line_screen.non_owned_auto_covg()
    ca_policy.comm_auto_line_screen.non_owned_auto_state(emp_no=data["emp_no"], partners=data["partners"],
                                                         volunteers=data["volunteers"], state=data["base_state"])
    ca_policy.title_toolbar.next()

    # Locations screen
    address = random_address.get_one_address("VA")
    ca_policy.location_screen.add_new_location(address1=address["Address_1"],
                                               city= address["City"],
                                               state=address["State"],
                                               zip_code=address["Zip_Code"])
    ca_policy.title_toolbar.next()

    # Vehicles screen
    ca_policy.vehicles_screen.add_vehicle(garage_location=data["garage_loc"], type_of_vehicle=data["vehicle_type"],
                                          vehicle_cost=data["vehicle_cost"])
    ca_policy.vehicles_screen.vehicle_class_code(radius=data["radius"])
    ca_policy.title_toolbar.next()

    # State Info screen
    ca_policy.state_info_screen.uninsured_motorist_bodily_injury(bodily_injury_package=data["um_package"])
    ca_policy.state_info_screen.uninsured_motorist_property_damage(property_damage_limit=data["um_prop_limit"])
    ca_policy.title_toolbar.next()

    # Drivers screen
    ca_policy.drivers_screen.driver_details(fn=data["fn"], ln=data["ln"], driver_gender=data["gender"],
                                            dob=data["dob"], license_state=data["lic_state"])
    ca_policy.title_toolbar.next()

    # Covered Vehicles screen
    # Not required for a smoke run
    # ca_policy.title_toolbar.next()

    # Modifiers screen
    # Not required for a smoke run
    # ca_policy.title_toolbar.next()

    # Risk Analysis screen
    ca_policy.title_toolbar.quote()

    # Quote screen
    assert ca_policy.quote_screen.total_premium_amount() > 0
    ca_policy.title_toolbar.next()

    # Forms screen
    ca_policy.title_toolbar.next()

    # Payment screen
    ca_policy.title_toolbar.issue_policy()

    time.sleep(20)
    take_screenshot(browser)
