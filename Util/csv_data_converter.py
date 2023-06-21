import random
import pandas
import definitions


def list_of_dicts(csv_file, number_of_rows=None):
    """
    :param csv_file: A csv file for input data
    :param number_of_rows: Optional parameter return number of data rows required from data sheet
    :return: A list of dictionary in which each dict has its key as input csv data header
    and values as row data of input csv file.
    """

    data = pandas.read_csv(csv_file, dtype=str)

    # variables_list = data.columns.tolist()
    # converted_data = [{variable: row[variable] for variable in variables_list} for (index, row) in data.iterrows()]
    converted_data = data.to_dict(orient="records")
    if number_of_rows is None:
        return converted_data
    else:
        return converted_data[:number_of_rows]


def get_row(file_path, reference_column, reference_column_value) -> dict:
    """
    return the first matching row. reference_column, reference_column_value should be unique.
    """
    data_list = list_of_dicts(file_path)
    key = reference_column
    value = reference_column_value
    matching_dict = [d for d in data_list if d[key] == value]
    return matching_dict[0]


def get_rows(file_path, reference_column, *reference_column_value) -> list:
    """
    reference_column, reference_column_value should be unique.
    """
    data_list = list_of_dicts(file_path)
    key = reference_column
    value = reference_column_value
    matching_dict = [d for d in data_list if d[key] in value]
    return matching_dict


def update_csv(file, reference_column, reference_column_value, column, value):
    """
    :param file: csv file with its path that needs to be updated
    :param reference_column: column name which we are referring to update desired column in file
    :param reference_column_value: Value of by_column which we are referring to update desired column in file
    :param column: column to update
    :param value: value to update
    :return: update the value of desired data field
    """
    data = pandas.read_csv(file)
    # Modify the data in dataframe
    data.loc[data[reference_column].astype(str) == reference_column_value, column] = value
    # Write the updated Dataframe back to CSV file
    data.to_csv(file, index=False)


if __name__ == "__main__":
    # file_path = definitions.ROOT_DIR + "/Data/data_policy_change_work_comp.csv"
    # # row = get_row(file_path, "Test#", 1)
    # # print(row)
    #
    # r = get_rows(file_path, "Test#", 1, 2)
    # print(r)
    # for item in r:
    #     print(item)

    file_path = definitions.ROOT_DIR + "/Data/data_newbusiness_work_comp.csv"
    data = list_of_dicts(file_path)
