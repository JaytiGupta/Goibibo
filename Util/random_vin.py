from Util.csv_data_converter import list_of_dicts
import random
from definitions import ROOT_DIR

# VIN[] =

# TODO
def get_one_vin():
    vin_list = list_of_dicts(ROOT_DIR + "/Data/VIN.csv")
    vin = random.choice(vin_list)
    return vin["VIN"]




