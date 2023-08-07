# from faker import Faker
#
# fake = Faker(locale="en_US")
#
# print(fake.name())
# print(fake.first_name())
# print(fake.last_name())
# print(fake.company_email())
# print(fake.company())
# print(fake.unique.numerify('###-###-####'))
# import definitions
# from Util import csv_data_converter
#
#
# def decorator(function):
#
#     def wrapper_function():
#         print("Before your function")
#         function()
#         print("After yor function")
#
#     return wrapper_function
#
#
# def second_decorator(function):
#
#     def wrapper_function():
#         print("----------------------------")
#         function()
#         print("----------------------------")
#
#     return wrapper_function
#
#
# @decorator
# @second_decorator
# def say_hello():
#     print("Hello")
#     return None


# say_hello()


import os
import definitions
from Util import csv_data_converter


# file_name = os.path.basename(__file__)
# print(file_name)
#
#
# def ttest_data(*test_case_number):
#     current_file_name = "test_newbusiness_work_comp.py"  # os.path.basename(__file__)
#     data_file_path = definitions.ROOT_DIR + "/Data/data_driven_tests/"
#     data_file_name = current_file_name.replace("test", "data", 1).replace(".py", ".csv")
#     data_file = data_file_path + data_file_name
#
#     str_args = [str(tc) if isinstance(tc, int) else tc for tc in test_case_number]
#
#     test_data = csv_data_converter.get_rows(data_file, "TestCase", *str_args)
#     return test_data


# @fixture(params=test_data)
# def data(request):
#     yield request.param


