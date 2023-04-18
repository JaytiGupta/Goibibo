from Base.basepage import BasePage
from Base.baseelement import BaseElement
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


class AmazonHeader(BasePage):

    def search_item(self, item):
        search_box_elm = BaseElement(self.driver, By.XPATH, '//input[@id="twotabsearchtextbox"]')
        search_button_elm = BaseElement(self.driver, By.XPATH, '//input[@value="Go"]')
        search_box_elm.enter_text(item)
        search_button_elm.click_element()

    def search_dropbox(self, value):
        elm = BaseElement(self.driver, By.XPATH, '//select[@id="searchDropdownBox"]')
        Select(elm).select_by_visible_text(value)

    def go_to_cart(self):
        BaseElement(self.driver, By.XPATH, '//span[@id="nav-cart-count"]').click_element()
