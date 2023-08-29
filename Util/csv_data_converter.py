import os
import pandas
import inspect
import definitions


def list_of_dicts(file_path):
    """
    Read a CSV file and return its contents as a list of dictionaries.

    :param file_path: Path to the input CSV file.
    :return: List of dictionaries containing CSV data.
    """
    csv_data = pandas.read_csv(file_path, dtype=str)
    converted_data = csv_data.to_dict(orient="records")
    return converted_data


def get_rows(file_path, reference_column, *reference_column_value):
    """
    Retrieve rows from the CSV file that match the provided reference values.

    :param file_path: Path to the input CSV file.
    :param reference_column: Column name to use as a reference for filtering.
    :param reference_column_values: Values to match in the reference column.
    :return: List of dictionaries containing matching rows.
    """
    data_list = list_of_dicts(file_path)
    key, value = reference_column, reference_column_value
    matching_dicts = [matching_dict for matching_dict in data_list if matching_dict[key] in value]
    return matching_dicts


# def get_row(file_path, reference_column, reference_column_value) -> dict:
#     """
#     reference_column, reference_column_value should be unique.
#     """
#     row = get_rows(file_path, reference_column, reference_column_value)
#     return row[0]


def get_column_data(file_path, column_name) -> list:
    """
    Retrieve data from a specific column of the CSV file.

    :param file_path: Path to the input CSV file.
    :param column_name: Name of the column to retrieve data from.
    :return: List of values from the specified column.
    """
    csv_data = pandas.read_csv(file_path)
    column_data = csv_data[column_name].tolist()
    return column_data


def update_csv_cell(file_path, reference_column, reference_column_value, column, value):
    """
    Update a specific cell in the CSV file.

    :param file_path: Path to the CSV file to be updated.
    :param reference_column: Column name used as a reference for locating the cell to update.
    :param reference_column_value: Value in the reference column to identify the cell to update.
    :param column: Name of the column to update.
    :param value: New value to set in the specified cell.
    """
    data = pandas.read_csv(file_path, dtype=str)
    data.loc[data[reference_column].astype(str) == reference_column_value, column] = value
    data.to_csv(file_path, index=False)
    return None


class CSVTestData:

    @staticmethod
    def _data_file():
        """
        Generate the path to the corresponding data CSV file based on the calling test file.

        :return: Path to the data CSV file.
        """
        file_path = os.path.join(definitions.ROOT_DIR, "Data", "data_driven_tests")
        test_file_name = os.path.basename(inspect.stack()[2].filename)
        data_file_name = test_file_name.replace("test", "data", 1).replace(".py", ".csv")
        data_file = os.path.join(file_path, data_file_name)
        return data_file

    @staticmethod
    def load_testcase(*test_case_numbers):
        """
        Load test case data from the data CSV file based on provided test case numbers.

        :param test_case_numbers: Test case numbers or names to load data for.
        :return: List of dictionaries containing test case data.
        """
        str_args = [str(tc) if isinstance(tc, int) else tc for tc in test_case_numbers]
        test_data = get_rows(CSVTestData._data_file(), "TestCase", *str_args)
        return test_data

    @staticmethod
    def update(test_case, column_name, value):
        """
        Update a specific column of a test case in the data CSV file.

        :param test_case: Test case number or name to update.
        :param column_name: Name of the column to update.
        :param value: New value to set in the specified cell.
        """
        test_case_str = str(test_case) if isinstance(test_case, int) else test_case
        file_path = CSVTestData._data_file()
        update_csv_cell(file_path, "TestCase", test_case_str, column_name, value)
        return None

# def list_of_dicts(file_path, sheet_name=None): # to read excel as well
#     if file_path.endswith('.csv'):
#         data = pandas.read_csv(file_path, dtype=str)
#     elif file_path.endswith('.xlsx') or file_path.endswith('.xls'):
#         if sheet_name is None:
#             raise ValueError("For Excel files, you need to specify a sheet name.")
#         data = pandas.read_excel(file_path, sheet_name=sheet_name, dtype=str)
#     else:
#         raise ValueError("Unsupported file format. Only CSV and Excel files are supported.")
#
#     converted_data = data.to_dict(orient="records")
#     return converted_data


if __name__ == "__main__":
    data_file_path = definitions.ROOT_DIR + "\\Data\\data_driven_tests\\"
    data_file_path2 = os.path.join(definitions.ROOT_DIR, "Data", "data_driven_tests")
    print(data_file_path)
    print(data_file_path2)
