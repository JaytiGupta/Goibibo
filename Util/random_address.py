from Util.csv_data_converter import list_of_dicts
from Util import csv_data_converter
import random
from definitions import ROOT_DIR
from dataclasses import dataclass


ADDRESS_DATA_FILE_PATH = ROOT_DIR + "/Data/Address.csv"
VIN_FILE_PATH = ROOT_DIR + "/Data/VIN.csv"
LICENSE_FILE_PATH = ROOT_DIR + "/Data/License.csv"


def get_address_list(*states):
    """
    :param states: states (or state code) for which list of address required.
    :return: list of address where each address is a dictionary
    includes key - Address_1, Address_2, City, County, State, State_Code, Zip_Code, Phone_Number.
    """

    state_codes = {
        "AL": "Alabama", "AK": "Alaska", "AZ": "Arizona", "AR": "Arkansas", "CA": "California", "CO": "Colorado",
        "CT": "Connecticut", "DE": "Delaware", "DC": "District of Columbia", "FL": "Florida", "GA": "Georgia",
        "HI": "Hawaii", "ID": "Idaho", "IL": "Illinois", "IN": "Indiana", "IA": "Iowa", "KS": "Kansas",
        "KY": "Kentucky", "LA": "Louisiana", "ME": "Maine", "MD": "Maryland", "MA": "Massachusetts", "MI": "Michigan",
        "MN": "Minnesota", "MS": "Mississippi", "MO": "Missouri", "MT": "Montana", "NE": "Nebraska",
        "NV": "Nevada", "NH": "New Hampshire", "NJ": "New Jersey", "NM": "New Mexico", "NY": "New York",
        "NC": "North Carolina", "ND": "North Dakota", "OH": "Ohio", "OK": "Oklahoma", "OR": "Oregon",
        "PA": "Pennsylvania", "PR": "Puerto Rico", "RI": "Rhode Island", "SC": "South Carolina", "SD": "South Dakota",
        "TN": "Tennessee", "TX": "Texas", "UT": "Utah", "VT": "Vermont", "VA": "Virginia", "VI": "Virgin Islands",
        "WA": "Washington", "WV": "West Virginia", "WI": "Wisconsin", "WY": "Wyoming",
    }

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


# TODO - Need to update random_addrees() in place of get_one_address() then delete it.
def get_one_address(*state):
    address_list = get_address_list(*state)
    return random.choice(address_list)


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


def random_address(*state):
    address_list = get_address_list(*state)
    address = random.choice(address_list)
    address_object = RandomAddress(**address)
    return address_object


def random_VIN():
    vin_list = csv_data_converter.get_column_data(VIN_FILE_PATH, "VIN")
    return random.choice(vin_list)


def random_license():
    license_list =csv_data_converter.get_column_data(LICENSE_FILE_PATH, "License")
    return random.choice(license_list)


if __name__ == "__main__":
    print(random_address("VA").Address_1)
    print(random_license())
    print(random_VIN())
