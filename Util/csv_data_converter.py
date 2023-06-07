import pandas
import definitions


def list_of_dicts(csv_file, number_of_rows=None):
    """
    :param csv_file: A csv file for input data
    :param number_of_rows: Optional parameter return number of data rows required from data sheet
    :return: A list of dictionary in which each dict has its key as input csv data header
    and values as row data of input csv file.
    """
    data = pandas.read_csv(csv_file)
    # variables_list = data.columns.tolist()
    # converted_data = [{variable: row[variable] for variable in variables_list} for (index, row) in data.iterrows()]
    converted_data = data.to_dict(orient="records")
    if number_of_rows is None:
        return converted_data
    else:
        return converted_data[:number_of_rows]


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
    update_csv(definitions.ROOT_DIR + "/Data/account_creation_data.csv", "company_name", "new_company_1", "account_type", "person")
    l = list_of_dicts(definitions.ROOT_DIR + "/Data/account_creation_data.csv")
    print(l)
    for item in l:
        print(item)
    print(l[0]["company_name"])
