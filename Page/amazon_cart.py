from Base.basepage import BasePage
from Base.baseelement import BaseElement
from selenium.webdriver.common.by import By
from re import sub


class AmazonCart(BasePage):

    def cart_item_price_list(self):
        list1 = BaseElement(self.driver, By.XPATH,
                            '//form[@id="activeCartViewForm"]//div[@class="sc-item-price-block"]').get_elements_text()
        list2 = []
        for item in list1:
            x = (sub(r'[^\d.]', '', item))
            list2.append(float(x))
        return list2

    def cart_total_amt(self):
        xpath = '//span[@id="sc-subtotal-amount-activecart"]'
        cart_total = float(BaseElement(self.driver, By.XPATH, xpath).get_text())
        return cart_total
