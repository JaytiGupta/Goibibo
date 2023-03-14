from Base.basepage import BasePage
from Base.baseelement import BaseElement
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


class AmazonSearchResult(BasePage):

    def set_price_range(self, min_amt, max_amt):
        min =  BaseElement(self.driver, By.XPATH, '//input[@name="low-price"]')
        max = BaseElement(self.driver, By.XPATH, '//input[@name="high-price"]')
        go = BaseElement(self.driver, By.XPATH, '//input[@class="a-button-input"]')
        min.enter_text(min_amt)
        max.enter_text(max_amt)
        go.click_element()

    def all_item_price_list(self):
        pass

