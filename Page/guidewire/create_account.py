from Base.basepage import BasePage
from Base.baseelement import BaseElement
from selenium.webdriver.common.by import By


class TabBar(BasePage):

    def __init__(self, driver):
        super().__init__(driver=driver, url=None)

    # Page1 - Enter Account Information
    def input_company_name(self, name):
        pass

    def input_first_name(self, name):
        pass

    def input_last_name(self, name):
        pass

    def click_search_btn(self):
        pass

    def validate_zero_results(self):
        pass

    def create_new_account(self, type):
        pass

    # Page2 - Create account
    def input_office_phone(self):
        pass

    def input_primary_email(self):
        pass

    def input_address_1(self):
        pass

    def input_city(self):
        pass

    def input_state(self):
        pass

    def input_zip(self):
        pass

    def select_address_type(self):
        pass

    def select_org(self):
        pass

    def select_producer(self):
        pass

    def update_btn(self):
        pass







