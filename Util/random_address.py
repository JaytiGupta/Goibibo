from Util.csv_data_converter import list_of_dicts
import random
from definitions import ROOT_DIR
from dataclasses import dataclass

ADDRESS_DATA_FILE_PATH = ROOT_DIR + "/Data/Address.csv"


state_codes = {
    "AL": "Alabama", "AK": "Alaska", "AZ": "Arizona", "AR": "Arkansas", "CA": "California", "CO": "Colorado", "CT": "Connecticut", "DE": "Delaware", "DC": "District of Columbia", "FL": "Florida", "GA": "Georgia", "HI": "Hawaii", "ID": "Idaho", "IL": "Illinois", "IN": "Indiana", "IA": "Iowa", "KS": "Kansas", "KY": "Kentucky", "LA": "Louisiana", "ME": "Maine", "MD": "Maryland", "MA": "Massachusetts", "MI": "Michigan", "MN": "Minnesota", "MS": "Mississippi", "MO": "Missouri", "MT": "Montana", "NE": "Nebraska",
    "NV": "Nevada", "NH": "New Hampshire", "NJ": "New Jersey", "NM": "New Mexico", "NY": "New York", "NC": "North Carolina", "ND": "North Dakota", "OH": "Ohio", "OK": "Oklahoma", "OR": "Oregon", "PA": "Pennsylvania", "PR": "Puerto Rico", "RI": "Rhode Island", "SC": "South Carolina", "SD": "South Dakota", "TN": "Tennessee", "TX": "Texas", "UT": "Utah", "VT": "Vermont", "VA": "Virginia", "VI": "Virgin Islands", "WA": "Washington", "WV": "West Virginia", "WI": "Wisconsin", "WY": "Wyoming",
}


def get_address_list(*states):
    """
    :param states: states for which list of address required.
    :return: list of address where each address is a dictionary
    includes key - Address_1, Address_2, City, County, State, State_Code, Zip_Code, Phone_Number.
    """
    addresses = list_of_dicts(ADDRESS_DATA_FILE_PATH)
    return_address_list = []
    for address in addresses:
        state_code = address["State_Code"]
        address["State"] = state_codes[state_code]
        try:
            if states[0].lower() == "all":
                return_address_list.append(address)
            elif state_code.lower() in (s.lower() for s in states):
                return_address_list.append(address)
            elif state_codes[state_code].lower() in (s.lower() for s in states):
                return_address_list.append(address)
        except KeyError:
            pass

    return return_address_list


def get_one_address(*state):
    address_list = get_address_list(*state)
    address = random.choice(address_list)
    return address


@dataclass
class RandomAddressesList:
    Address_1: str
    Address_2: str
    City: str
    County: str
    State_Code: str
    Zip_Code: str
    Phone_Number: str
    State: str


@dataclass
class RandomAddress:
    Address_1: str
    Address_2: str
    City: str
    County: str
    State_Code: str
    Zip_Code: str
    Phone_Number: str
    State: str


def random_address():
    address = get_one_address("va")
    address_object = RandomAddress(**address)
    return address_object


if __name__ == "__main__":
    # # print(get_address_list("virGinia", 'AK'))
    # add1 = get_one_address("va")
    # print(add1["Address_1"])
    # dataobj = RandomAddress(**add1)
    # print(dataobj.Address_1)
    #
    # address_list = get_address_list("VA")
    # print(address_list)
    # data_list_obj = [RandomAddressesList(**address) for address in address_list]
    # print(data_list_obj)
    # print(data_list_obj[0].Address_1)
    address = random_address()

