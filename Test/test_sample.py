from faker import Faker

fake = Faker()

print(fake.name())

# ----------------------------
#
# def wait_for_any_ec(driver, *conditions):
#     for condition in conditions:
#         try:
#             element = WebDriverWait(driver, 1).until(condition)
#             return element
#         except:
#             continue
#     raise Exception("None of the conditions were satisfied")
#
# condetion1 = EC.visibility_of(self.details_btn.web_element)
# condetion2 = EC.visibility_of(self.quote_screen._total_premium_amt.web_element)
# condetion3 = EC.visibility_of(self.workspace.workspace_area.web_element)
#
# wait_for_any_ec(self.driver, condetion1, condetion3, condetion2)
# ----------------------------
