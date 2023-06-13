from selenium.common import TimeoutException
from Base.basepage import BasePage
from Base.baseelement import BaseElement
from selenium.webdriver.common.by import By
from re import sub


class AmazonCart(BasePage):

    def empty_cart_text(self):
        return BaseElement(self.driver, (By.XPATH, '//div[@class="a-row sc-your-amazon-cart-is-empty"]/h2')).get_text()

    def cart_item_price_list(self):
        list1 = BaseElement(self.driver, By.XPATH,
                            '//form[@id="activeCartViewForm"]//div[@class="sc-item-price-block"]').get_all_elements_text()
        list2 = []
        for item in list1:
            x = (sub(r'[^\d.]', '', item))
            list2.append(float(x))
        return list2

    def cart_total_amt(self):
        xpath = '//span[@id="sc-subtotal-amount-activecart"]'
        cart_total = BaseElement(self.driver, By.XPATH, xpath).get_text()
        cart_total_int = float(sub(r'[^\d.]', '', cart_total))
        return cart_total_int

    def verify_cart_not_empty(self):
        element = BaseElement(self.driver, By.XPATH,
                           '//div[@class="a-row sc-your-amazon-cart-is-empty"]/h2').web_element
        return element == 'Element is not found.'
