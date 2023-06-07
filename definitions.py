from datetime import datetime
import os

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))

# TODO: Put screenshot and env variables in some other dict like config
global_dict = {
    "screenshot_folder": "",
    "env": "test",
    "screenshots": False
}


def set_value(key, value):
    global_dict[key] = value


# To create unique folder names along with time stamp for storing screenshots
def create_screenshot_folder():
    current_datetime = datetime.now()
    folder_name = current_datetime.strftime("%Y_%m_%d-%H_%M_%S")
    set_value("screenshot_folder", folder_name)


# TODO exception handling
# TODO reporting - separate file creation for each run
# TODO logs - separate file creation for each run
# TODO screenshots - separate folder creation for each run
# Add 8-10 test cases with lists/collections etc...   ----- 1 with each feature
# TODO parallel/linear execution ------- 6
# pass URL as parameter  ------ 1
# github (try this first) /gitlab ------ 4