import inspect
import os
import pandas
import random
import definitions


def list_of_dicts(file_path):
    """
    :param file_path: A csv file for input data
    :return: A list of rows. Where each row is a dictionary containing input csv file data.
    :return: A list of dictionary in which each dict has its key as input csv data header
    and values as row data of input csv file.
    """
    csv_data = pandas.read_csv(file_path, dtype=str)
    converted_data = csv_data.to_dict(orient="records")
    return converted_data


def get_rows(file_path, reference_column, *reference_column_value):
    """
    reference_column, reference_column_value should be unique.
    """
    data_list = list_of_dicts(file_path)
    key, value = reference_column, reference_column_value
    matching_dicts = [matching_dict for matching_dict in data_list if matching_dict[key] in value]
    return matching_dicts


def get_row(file_path, reference_column, reference_column_value) -> dict:
    """
    reference_column, reference_column_value should be unique.
    """
    row = get_rows(file_path, reference_column, reference_column_value)
    return row[0]


def get_column_data(file_path, column_name) -> list:
    csv_data = pandas.read_csv(file_path)
    column_data = csv_data[column_name].tolist()
    return column_data


def update_csv(file_path, reference_column, reference_column_value, column, value):
    """
    :param file_path: csv file with its path that needs to be updated
    :param reference_column: column name which we are referring to update desired column in file
    :param reference_column_value: Value of by_column which we are referring to update desired column in file
    :param column: column to update
    :param value: value to update
    :return: update the value of desired data field
    """
    data = pandas.read_csv(file_path, dtype=str)
    # Modify the data in dataframe
    data.loc[data[reference_column].astype(str) == reference_column_value, column] = value
    # Write the updated Dataframe back to CSV file
    data.to_csv(file_path, index=False)


class CSVTestData:

    @staticmethod
    def _data_file():
        file_name = os.path.basename(inspect.stack()[2].filename)
        data_file_path = definitions.ROOT_DIR + "\\Data\\data_driven_tests\\"
        data_file_name = file_name.replace("test", "data", 1).replace(".py", ".csv")
        data_file = data_file_path + data_file_name
        return data_file

    @staticmethod
    def load_testcase(*test_case_numbers):
        str_args = [str(tc) if isinstance(tc, int) else tc for tc in test_case_numbers]
        test_data = get_rows(CSVTestData._data_file(), "TestCase", *str_args)
        return test_data

    @staticmethod
    def update(test_case, column_name, value):
        test_case_str = str(test_case) if isinstance(test_case, int) else test_case
        file_path = CSVTestData._data_file()
        update_csv(file_path, "TestCase", test_case_str, column_name, value)


if __name__ == "__main__":
    pass
