from pytest import fixture
import pandas


def csv_to_ipdate(file_path):
    """
    :param file_path: A csv file for input data
    :return: A list of dictionary in which each dict has its key as input csv data header
    and values as row data of input csv file.
    """
    data = pandas.read_csv(file_path)
    variables_list = data.columns.tolist()
    converted_data = [{variable: row[variable] for variable in variables_list} for (index, row) in data.iterrows()]
    return converted_data



