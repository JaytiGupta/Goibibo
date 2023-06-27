from selenium.webdriver.common.by import By
from Base.baseelement import BaseElement
from Util.logs import getLogger


class TableQuestionnaires:
    log = getLogger()

    def __init__(self, driver):
        self.driver = driver

    @staticmethod
    def radio_btn_locator(question, answer):
        if question.lower() == "all":
            question = ""

        if answer.lower() == "yes":
            x_path = f'//div[contains(text(),"{question}")]/ancestor::tr//input[@type="radio"][@value="true"]'
        else:
            x_path = f'//div[contains(text(),"{question}")]/ancestor::tr//input[@type="radio"][@value="false"]'

        locator = (By.XPATH, x_path)
        return locator

    def select_radio_btn(self, question, answer):
        locator = self.radio_btn_locator(question, answer)
        radio_btn = BaseElement(self.driver, locator)
        radio_btn.click_element()
        self.log.info(f"Select {answer} for {question}.")

    def select_all_radio_btn(self, answer):
        locator = self.radio_btn_locator("all", answer)
        all_radio_btn_elm = BaseElement(self.driver, locator)
        all_radio_btn_elm.click_all_elements()
        self.log.info(f"Select all radio button questions as {answer}.")

    def input_box(self, question, answer):
        x_path = f'//div[contains(text(),"{question}")]/ancestor::tr//input[@type="text"]'
        locator = (By.XPATH, x_path)
        input_box = BaseElement(self.driver, locator)
        input_box.enter_text(answer)
        self.log.info(f"Enter {answer} for {question}.")

    def dropdown(self, question, dropdown_text):
        x_path = f'//div[contains(text(),"{question}")]/ancestor::tr//select'
        locator = (By.XPATH, x_path)
        dropdown_elm = BaseElement(self.driver, locator)
        dropdown_elm.select_option(text=dropdown_text)

