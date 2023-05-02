from Base.basepage import BasePage
from Base.baseelement import BaseElement
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from Util.logs import getLogger


class AmazonSearchResult(BasePage):

    log = getLogger()

    def set_price_range(self, min_amt, max_amt):
        min_price_elm = BaseElement(self.driver, By.XPATH, '//input[@name="low-price"]')
        max_price_elm = BaseElement(self.driver, By.XPATH, '//input[@name="high-price"]')
        go = BaseElement(self.driver, By.XPATH, '//li[contains(@id,"price-range")]//input[@type="submit"]')
        min_price_elm.enter_text(min_amt)
        max_price_elm.enter_text(max_amt)
        go.click_element()
        self.log.info(f"Price range for the searched item is set between {min_amt} and {max_amt}")

    def all_item_price_list(self):
        price_xpath = '//div[@data-component-type="s-search-result"]//span[@class="a-price-whole"]'
        price_list_str = BaseElement(self.driver, By.XPATH, price_xpath)
        price_list = price_list_str.get_elements_text()
        # print(price_list)
        final_price_list = []
        for i in price_list:
            x = int(i.replace(',', ''))
            final_price_list.append(x)
        return final_price_list

    def search_result_text(self):
        text_xpath = '//div[@class="a-section a-spacing-small a-spacing-top-small"]'
        text_str = BaseElement(self.driver, By.XPATH, text_xpath).get_text()
        return text_str

    def first_search_elm(self):
        first_elm = '//div[@data-component-type="s-search-result"]//span[@class="a-price-whole"]'
        first_elm_price = '//div[@data-component-type="s-search-result"][@data-index="2"]//span[@class="a-price-whole"]'
        return BaseElement(self.driver, By.XPATH, first_elm)

    def add_to_cart(self):
        self.first_search_elm().click_element()
        self.log.info("Clicked on the first search result displayed")
        p = self.driver.current_window_handle  #will be used to check if p equals parent
        window = self.driver.window_handles[0]
        if window == p:
            parent = self.driver.window_handles[0]
            chld = self.driver.window_handles[1]
        else:
            chld = self.driver.window_handles[0]
            parent = self.driver.window_handles[1]
        self.driver.switch_to.window(chld)
        self.log.info("Switching to the window of the searched item")
        add_to_cart_btn = BaseElement(self.driver, By.XPATH, '//input[@id="add-to-cart-button"]')
        add_to_cart_btn.click_element()
        self.verify_added_elm()
        self.log.info("Item is added to the cart")
        self.driver.close()
        self.driver.switch_to.window(parent)
        self.log.info("Switching to the main window")

    def verify_added_elm(self):
        return BaseElement(self.driver, By.XPATH, "//span[contains(text(),'Added to Cart')]").elm_is_displayed()

