import time
from re import sub
from selenium.webdriver.common.by import By
from Base.baseelement import BaseElement
from Base.basepage import BasePage
from Util.logs import getLogger


class Common:

    def __init__(self, driver):
        self.driver = driver
        self.title_toolbar = TitleToolbar(self.driver)
        self.workspace_screen = Workspace(self.driver)
        self.risk_analysis_screen = RiskAnalysis(self.driver)
        self.policy_review_screen = PolicyReview(self.driver)
        self.quote_screen = Quote(self.driver)
        self.forms_screen = Forms(self.driver)


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

    def radio_btn(self, question, answer):
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
        dropdown_elm = BaseElement(self.driver,locator)
        dropdown_elm.select_option(text=dropdown_text)


class TitleToolbar(BasePage):
    log = getLogger()

    def __init__(self, driver):
        super().__init__(driver=driver, url=None)
        self.risk_analysis_screen = RiskAnalysis(self.driver)
        self.workspace = Workspace(self.driver)

    @property
    def screen_title(self):
        locator = (By.XPATH, '//div[@id="gw-center-title-toolbar"]//div[@role="heading"]')
        return BaseElement(self.driver, locator)

    @property
    def next_btn(self):
        locator = (By.XPATH, '//div[@id="gw-center-title-toolbar"]//div[text()="Next"]')
        return BaseElement(self.driver, locator)

    @property
    def back_btn(self):
        locator = (By.XPATH, '//div[@id="gw-center-title-toolbar"]//div[text()="Back"]')
        return BaseElement(self.driver, locator)

    @property
    def quote_btn(self):
        locator = (By.XPATH, '//div[@id="gw-center-title-toolbar"]//div[@aria-label="Quote"]')
        return BaseElement(self.driver, locator)

    @property
    def save_draft_btn(self):
        locator = (By.XPATH, '//div[@id="gw-center-title-toolbar"]//div[@aria-label="Save Draft"]')
        return BaseElement(self.driver, locator)

    @property
    def close_option_btn(self):
        locator = (By.XPATH, '//div[@id="gw-center-title-toolbar"]//div[@aria-label="Close Options"]')
        return BaseElement(self.driver, locator)

    @property
    def bind_options_btn(self):
        locator = (By.XPATH, '//div[@id="gw-center-title-toolbar"]//div[@aria-label="Bind Options"]')
        return BaseElement(self.driver, locator)

    @property
    def bind_only_btn(self):
        locator = (By.XPATH, '//div[@id="gw-center-title-toolbar"]//div[@aria-label="Bind Only"]')
        return BaseElement(self.driver, locator)

    @property
    def issue_policy_btn(self):
        locator = (By.XPATH, '//div[@id="gw-center-title-toolbar"]//div[@aria-label="Issue Policy"]')
        return BaseElement(self.driver, locator)

    @property
    def details_btn(self):
        locator = (By.XPATH, '//div[@id="gw-center-title-toolbar"]//div[text()="Details"]')
        return BaseElement(self.driver, locator)

    def screen_title_text(self):
        text = self.screen_title.get_text()
        return text

    def next(self):
        title = self.screen_title_text()
        self.next_btn.click_element()
        self.screen_title.wait_till_text_to_be_not_present_in_element(title)

    def quote(self):  # TODO needs to update max depth for recursion
        initial_screen_title = self.screen_title_text()

        self.log.info(f"{initial_screen_title} screen")
        self.quote_btn.click_element()
        self.log.info("Clicked Quote button.")

        # TODO: update need to wait for page after click, screen can be same, pre_quote or quote
        time.sleep(5)

        if self.screen_title_text() == "Quote":
            self.log.info("Quoted successfully")
        elif self.screen_title_text() == "Pre-Quote Issues":
            self.log.info("Pre-Quote Issues screen")
            self.details_btn.click_element()
            self.log.debug("Navigate to Underwriter issues tab at Risk Analysis screen.")
            self.risk_analysis_screen.approve_all_uw_issues()
            self.log.debug("All underwriter issues approved.")
            self.wait_for_screen("Risk Analysis")
            self.quote()
        elif self.screen_title_text() == initial_screen_title:
            self.log.info(f"{initial_screen_title} screen")
            if self.workspace.error().is_element_present():
                self.log.debug("Getting error and unable to quote")
                raise Exception("Getting error and unable to quote")
            elif self.workspace.warning().is_element_present():
                self.log.info("Getting warnings")
            # TODO elif Information
            self.quote()

    def wait_for_screen(self, screen_title_text):
        self.screen_title.wait_till_text_to_be_present_in_element(screen_title_text)

    def bind_policy(self):
        self.bind_options_btn.click_element()
        self.bind_only_btn.click_element()
        self.log.info(f"Clicked Bind Only button.")

    def issue_policy(self): # TODO needs to update max depth for recursion
        initial_screen_title = self.screen_title_text()

        self.bind_options_btn.click_element()
        self.issue_policy_btn.click_element()
        self.log.info(f"Clicked Issue Policy button.")
        self.accept_alert()

        # TODO: update need to wait for page after click, screen can be same, pre_quote or quote
        time.sleep(5)

        if self.screen_title_text() == "Submission Bound":
            self.log.info("Your Submission has been bound")
        elif self.screen_title_text() == initial_screen_title:
            self.log.info(f"{initial_screen_title} screen")
            if self.workspace.error().is_element_present():
                self.log.debug("Getting error and unable to quote")
                raise Exception("Getting error and unable to quote")
            elif self.workspace.warning().is_element_present():
                self.log.info("Getting warnings")
            # TODO elif Information
            self.issue_policy()


class Workspace:
    log = getLogger()

    def __init__(self, driver):
        self.driver = driver
        self.risk_analysis_screen = RiskAnalysis(self.driver)

    def validation_results(self):
        locator = (By.XPATH, '//div[text()="Validation Results"]')
        return BaseElement(self.driver, locator)

    def error(self):
        locator = (By.XPATH, '//div[@id="gw-south-panel"]//div[contains(text(),"Error")]')
        return BaseElement(self.driver, locator)

    def warning(self):
        locator = (By.XPATH, '//div[@id="gw-south-panel"]//div[contains(text(),"Warning")]')
        return BaseElement(self.driver, locator)


class RiskAnalysis(BasePage):
    log = getLogger()

    def __init__(self, driver):
        super().__init__(driver=driver, url=None)
        self.SCREEN_TITLE = "Risk Analysis"
        self._locator_all_pending_approval_check_box = (
            By.XPATH, '//div[text()="Approve"]/ancestor::td[not(contains(@colspan,"1"))]'
                      '/preceding-sibling::td[4]//input[@type="checkbox"]')
        self._locator_header_approve_btn = (By.XPATH, '//div[@class="gw-ListView--UI-left"]'
                                                       '//div[text()="Approve"]')

        # Screen: Risk Approval Details
        self._locator_ok_btn = (By.XPATH, '//div[@role="button"]//div[@aria-label="OK"]')

    # TODO: select only the required check boxes
    def approve_all_uw_issues(self):
        all_check_box = BaseElement(self.driver, self._locator_all_pending_approval_check_box)
        all_check_box.click_all_elements()
        header_approve_btn = BaseElement(self.driver, self._locator_header_approve_btn)
        header_approve_btn.click_element()

        risk_approval_screen_ok_btn = BaseElement(self.driver, self._locator_ok_btn)
        risk_approval_screen_ok_btn.click_element()

        self.accept_alert()
        if all_check_box.is_element_present():
            self.log.debug("All UW Issues are not approved yet.")
        else:
            self.log.info("All UW Issues are approved.")


class PolicyReview(BasePage):
    log = getLogger()

    def __init__(self, driver):
        super().__init__(driver=driver, url=None)
        self.SCREEN_TITLE = "Policy Review"


class Quote(BasePage):
    log = getLogger()

    def __init__(self, driver):
        super().__init__(driver=driver, url=None)
        self.SCREEN_TITLE = "Quote"
        self._locator_total_premium_amt = (By.XPATH, '//div[text()="Total Premium"]'
                                                     '/following-sibling::div//div[contains(text(), "$")]')

    def total_premium_amt(self):
        elm = BaseElement(self.driver, self._locator_total_premium_amt)
        premium_txt =  elm.get_text()
        premium = float(sub(r'[^\d.]', '', premium_txt))
        self.log.info(f"Total Premium is {premium_txt}")
        return premium


class Forms(BasePage):
    log = getLogger()

    def __init__(self, driver):
        super().__init__(driver=driver, url=None)
        self.SCREEN_TITLE = "Forms"
        # self._locator_s = (By.XPATH, '//div[text()="Form #"]/ancestor::tr/following-sibling::tr')
        self._locator_ph_notice = (By.XPATH, '//div[contains(text(),"Notice to Policyholders")]')

    def ph_notice(self):
        ph_notice = BaseElement(self.driver, self._locator_ph_notice)
        if ph_notice.get_text() == "Notice to Policyholders":
            print("Notice to Policyholders form is generated")
            self.log.info("Policy Forms are generated")
        else:
            print("PH Notice is not generated for the quote")
            self.log.info("Forms are not generated correctly")
