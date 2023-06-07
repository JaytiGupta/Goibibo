from selenium.webdriver.common.by import By


def locator_dynamic_radio_btn(question, answer):
    if question.lower() == "all":
        question = ""

    if answer.lower() == "yes":
        x_path = f'//div[contains(text(),"{question}")]/ancestor::tr//input[@type="radio"][@value="true"]'
    else:
        x_path = f'//div[contains(text(),"{question}")]/ancestor::tr//input[@type="radio"][@value="false"]'

    return By.XPATH, x_path


def locator_dynamic_input_box(question):
    x_path = f'//div[contains(text(),"{question}")]/ancestor::tr//input[@type="text"]'
    return By.XPATH, x_path
