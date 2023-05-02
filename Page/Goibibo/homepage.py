import time
from selenium.webdriver.common.by import By
from Base.basepage import BasePage
from Base.baseelement import BaseElement
from selenium.webdriver.common.keys import Keys
from datetime import datetime

class HomePage(BasePage):

    def popupclose(self):
        return BaseElement(self.driver, By.XPATH, '//span[@class="logSprite icClose"]')

    def from_location(self):
        return BaseElement(self.driver, By.XPATH, '//span[text()="From"]//parent::div')

    def from_location_text(self):
        return BaseElement(self.driver, By.XPATH, "//span[text()='From']/following-sibling::input")

    def to_location(self):
        return BaseElement(self.driver, By.XPATH, "//span[text()='To']//parent::div")

    def to_location_text(self):
        return BaseElement(self.driver, By.XPATH, "//span[text()='To']/following-sibling::input")

    def set_from_location(self, text):
        self.from_location().click_element()
        self.from_location_text().enter_text(text)
        time.sleep(1)
        self.from_location_text().enter_text(Keys.ENTER)

    def set_to_location(self, text):
        self.to_location_text().enter_text(text)
        time.sleep(1)
        self.to_location_text().enter_text(Keys.ENTER)

    def departure_date(self, dep_date):
        input_datetime_str = dep_date
        input_datetime_obj = datetime.strptime(input_datetime_str, '%d,%B %Y')

        if input_datetime_obj < datetime.today():
            raise Exception('The input date is in the past. Please enter valid date.')

        # To navigate to the desired month of departure date
        while True:
            month = BaseElement(self.driver, By.XPATH, '//div[@class="DayPicker-Months"]/div[1]/div/div').get_text()
            next_arrow = BaseElement(self.driver, By.XPATH, '//span[@aria-label="Next Month"]')
            if dep_date.split(",")[1] == month:
                break
            next_arrow.click_element()

        dep_date = BaseElement(self.driver, By.XPATH, '//div[@class ="DayPicker-Months"]/div[1]//p[text()={}]'.format(dep_date.split(",")[0]))
        dep_date.click_element()

    def calendar_done_btn(self):
        return BaseElement(self.driver, By.CSS_SELECTOR, 'span[class="fswTrvl__done"]')

    def trvl_adults(self):
        return BaseElement(self.driver, By.XPATH, "//p[contains(text(), 'Adults')]//parent::div//span[3]")

    def trvl_children(self):
        return BaseElement(self.driver, By.XPATH, "//p[contains(text(), 'Children')]//parent::div//span[3]")

    def trvl_infants(self):
        return BaseElement(self.driver, By.XPATH, "//p[contains(text(), 'Infants')]//parent::div//span[3]")

    def set_traveller(self, adults, children, infants):
        for i in range(adults-1):
            self.trvl_adults().click_element()

        for i in range(children):
            self.trvl_children().click_element()

        for i in range(infants):
            self.trvl_infants().click_element()

        self.trvlr_done_btn().click_element()

    def trvlr_done_btn(self):
        return BaseElement(self.driver, By.XPATH, '//a[text()="Done"]')

    def search_flight_btn(self):
        BaseElement(self.driver, By.XPATH, '//span[text()="SEARCH FLIGHTS"]').click_element()

    def page_header_text(self):
        return BaseElement(self.driver, By.XPATH, '//h2').get_text()

    def radiobtn_oneway(self):
        return BaseElement(self.driver, By.XPATH, "//span[text()='One-way']//preceding-sibling::span")

    def radiobtn_roundtrip(self):
        return BaseElement(self.driver, By.XPATH, "//span[text()='Round-trip']//preceding-sibling::span")

    def forex_btn(self):
        return BaseElement(self.driver, By.XPATH, '//a[text()="Forex"]')

