import pandas


def csv_to_ipdate(file_path, number_of_rows=None):
    """
    :param file_path: A csv file for input data
    :param number_of_rows: Optional parameter return number of data rows required from data sheet
    :return: A list of dictionary in which each dict has its key as input csv data header
    and values as row data of input csv file.
    """
    data = pandas.read_csv(file_path)
    # variables_list = data.columns.tolist()
    # converted_data = [{variable: row[variable] for variable in variables_list} for (index, row) in data.iterrows()]
    converted_data = data.to_dict(orient="records")
    if number_of_rows is None:
        return converted_data
    else:
        return converted_data[:number_of_rows]


def update_csv(file_path, by_column, by_value, to_column, to_value):
    """
    :param file_path: file with its path that needs to be updated
    :param by_column: column name which we are referring to update desired column in file
    :param by_value: Value of by_column which we are referring to update desired column in file
    :param to_column: column to update
    :param to_value: value to update
    :return: update the value of desired data field
    """
    # Read the CSV file
    data = pandas.read_csv(file_path)
    # Modify the data in dataframe
    data.loc[data[by_column].astype(str) == by_value, to_column] = to_value
    # Write the updated Dataframe back to CSV file
    data.to_csv(file_path, index=False)


if __name__ == "__main__":
    update_csv("../Data/output_data.csv", "account_name", "NewAccount_3", "account_number", 565538)
