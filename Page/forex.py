from selenium.webdriver.common.by import By
from Base.basepage import BasePage
from Base.baseelement import BaseElement
from selenium.webdriver.common.keys import Keys


class Forex(BasePage):

    def select_city(self, cityname):
        city_dropdown = BaseElement(self.driver, By.XPATH, '//span[@id="select2-buysell-cityCode-container"]')
        city_searchbox = BaseElement(self.driver, By.XPATH, '//input[@class="select2-search__field"]')
        city_dropdown.click_element()
        city_searchbox.enter_text(cityname)
        city_searchbox.enter_text(Keys.ENTER)

    def currency_you_have_text(self):
        return BaseElement(self.driver, By.XPATH, '//span[@id="select2-sell-curr-inr-container"]/span').get_text()

    def currency_you_want_text(self):
        return BaseElement(self.driver, By.XPATH,
                           '//span[@id="select2-buysell-currencyCode-container"]/span').get_text()

    def currency_want_dropdown(self, currency):
        dropdown = BaseElement(self.driver, By.XPATH,
                               '//span[@id="select2-buysell-currencyCode-container"]/following-sibling::span')
        dropdown_searchbox = BaseElement(self.driver, By.XPATH, '//input[@class="select2-search__field"]')
        dropdown.click_element()
        dropdown_searchbox.enter_text(currency)
        dropdown_searchbox.enter_text(Keys.ENTER)

    def forex_amount(self, amount):
        input_box = BaseElement(self.driver, By.XPATH, '//input[@name="foreignAmount"]')
        input_box.enter_text(amount)

    def click_add_btn(self):
        add_btn = BaseElement(self.driver, By.XPATH,
                              '//div[contains(@class, "buy_forex_item")]//a[@class="add_product anchorbtn"]')
        add_btn.click_element()

    def get_total_amt(self):
        total_amt_elm = BaseElement(self.driver, By.XPATH,
                                    '//div[contains(@class, "buy_forex_item")]//span[@class="buysell-order_total"]')
        total_amt = total_amt_elm.get_text()
        return total_amt.replace(',', '')

    def get_rate(self):
        rate = BaseElement(self.driver, By.XPATH, '//div[contains(@class, "buy_forex_item")]//span[@class="ratedata"]')
        return rate.get_text()
