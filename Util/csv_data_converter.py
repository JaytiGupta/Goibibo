from pytest import fixture
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


def update_csv(file_path, **kwargs):
    new_dict = {key: [value] for (key, value) in kwargs.items()}
    print(new_dict)
    new_data = pandas.DataFrame(new_dict)
    new_data.to_csv(file_path, mode="a", index=False, header=False)


if __name__ == "__main__":
    update_csv("../output_data.csv", account_name="NewAccount_3", account_number="565303533")