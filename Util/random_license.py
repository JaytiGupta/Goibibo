from Util.csv_data_converter import list_of_dicts
import random
from definitions import ROOT_DIR


def get_one_license():
    license_list = list_of_dicts(ROOT_DIR + "/Data/License.csv")
    license_no = random.choice(license_list)
    return license_no



